from __future__ import annotations
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .db_query import query

class ExperimentMetadata(Base):
    __tablename__ = 'experiment_metadata'
    experiment_id = Column(String,  primary_key = True)
    experiment_name = Column(String)
    created_by = Column(String)
    created_time = Column(DateTime, server_default=func.now())
    last_run_time = Column(DateTime)
    last_runid = Column(String)
    job_type = Column(String)
    def __repr__(self):
        return ("ExperimentMetadata(experiment_id=" + str(self.experiment_id) 
        + ", experiment_name=" + str(self.experiment_name) 
        + ", created_by=" + str(self.created_by) 
        + ", created_time=" + str(self.created_time) 
        + ", last_run_time=" + str(self.last_run_time) 
        + ", last_runid=" + str(self.last_runid ) 
        + ", job_type=" + str(self.job_type) + ")"
        )
    def __eq__(self, other: ExperimentMetadata):
        return self.experiment_name == other.experiment_name and self.experiment_id == other.experiment_id and self.created_by == other.created_by and self.created_time == other.created_time and self.last_run_time == other.last_run_time and self.last_runid == other.last_runid and self.job_type == other.job_type

class ExperimentMetadataDBOperation():
    def __init__(self, Session):
        self.Session = Session

    def select(self, index_entities_request) -> list:
        with self.Session(expire_on_commit=False) as session:
            return query(ExperimentMetadata, index_entities_request, session)

    def insert(self, insert_data):
        data = insert_data
        with self.Session(expire_on_commit=False) as session:
            session.add(insert_data)
            session.commit()
        return data

    def update(self, update_data):
        with self.Session(expire_on_commit=False) as session:
            ret = session.merge(update_data)
            session.commit()
            return ret

    def delete(self, delete_data_experiment_id):
        with self.Session(expire_on_commit=False) as session:
            session.query(ExperimentMetadata).filter(ExperimentMetadata.experiment_id == delete_data_experiment_id).delete()
            session.commit()
            return True