from __future__ import annotations

import jsonpickle

from sqlalchemy import Column, String, Boolean, PickleType, DateTime, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from .db_query import query

from pipruncommon import IndexEntitiesRequest

Base = declarative_base()

class ComponentMetadata(Base):
    __tablename__ = 'component_metadata'
    component_id = Column(String, primary_key = True)
    component_type = Column(String)
    created_time = Column(DateTime)
    last_modified_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    component = Column(PickleType)
    docker_file_content = Column(String)

    def __repr__(self):
        return ("ComponentMetadata(component_id=" + str(self.component_id) 
        + ", component_type=" + str(self.component_type)
        + ", created_time=" + str(self.created_time)
        + ", component=" + jsonpickle.encode(self.component, unpicklable = False)
        + ", docker_file_content=" + str(self.docker_file_content) + ")"
        )

    def __eq__(self, other: ComponentMetadata):
        return (self.component_id == other.component_id 
            and self.component_type == other.component_type 
            and self.created_time == other.created_time
            and jsonpickle.encode(self.component) == jsonpickle.encode(other.component) 
            and self.docker_file_content == other.docker_file_content)

class ComponentMetadataDBOperation:
    def __init__(self, Session):
        self.Session = Session

    def select(self, index_entities_request: IndexEntitiesRequest) -> list:
        with self.Session(expire_on_commit=False) as session:
            return query(ComponentMetadata, index_entities_request, session)

    def insert(self, insert_data: ComponentMetadata):
        data = insert_data
        with self.Session(expire_on_commit=False) as session:
            session.add(insert_data)
            session.commit()
        return data

    def get(self, component_id) -> ComponentMetadata:
        with self.Session(expire_on_commit=False) as session:
            return session.query(ComponentMetadata).filter(ComponentMetadata.component_id == component_id).first()

    def update(self, update_data:ComponentMetadata):
        with self.Session(expire_on_commit=False) as session:
            ret = session.merge(update_data)
            session.commit()
            return ret

    def delete(self, delete_component_id):
        with self.Session(expire_on_commit=False) as session:
            session.query(ComponentMetadata).filter(ComponentMetadata.component_id == delete_component_id).delete()
            session.commit()
            return True