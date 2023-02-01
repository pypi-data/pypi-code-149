from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .db_query import query

class RunDefinition(Base):
    __tablename__ = 'run_definition'
    run_id = Column(String, primary_key = True)
    run_definition = Column(String)
    def __repr__(self):
        return "RunDefinition(run_id=" + str(self.run_id) + ", run_definition=" + str(self.run_definition) + ")"
    def __eq__(self, other):
        return self.run_id == other.run_id and self.run_definition == other.run_definition

class RunDefinitionDBOperation:
    def __init__(self, Session):
        self.Session = Session

    def select(self, index_entities_request) -> list:
        with self.Session(expire_on_commit=False) as session:
            return query(RunDefinition, index_entities_request, session)

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
        
    def delete(self, delete_data_run_id):
        with self.Session(expire_on_commit=False) as session:
            session.query(RunDefinition).filter(RunDefinition.run_id == delete_data_run_id).delete()
            session.commit()
            return True