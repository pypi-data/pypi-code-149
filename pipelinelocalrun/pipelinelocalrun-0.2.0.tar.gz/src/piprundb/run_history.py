from __future__ import annotations
import jsonpickle
from sqlalchemy import JSON, Column, Integer, PickleType, String, DateTime, TIMESTAMP, Interval, select
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import deferred
from .experiment_metadata import ExperimentMetadata
from .db_query import query, query_count
Base = declarative_base()

class RunHistory(Base):
    __tablename__ = 'run_history'
    run_id = Column(String, primary_key = True)
    run_number = Column(Integer)
    display_name = Column(String)   
    run_type = Column(String)
    job_type = Column(String)
    run_mode = Column(String)
    created_by = Column(String)
    created_time = Column(DateTime)
    ready_time = Column(DateTime)
    start_time = Column(DateTime)
    finish_time = Column(DateTime)
    duration = Column(Interval)
    status = Column(String)
    total_steps = Column(Integer)
    inputs = Column(PickleType)  #RunInput
    outputs = Column(PickleType)  #RunOutput
    parameters = Column(PickleType) #RunInput
    container_id = Column(String)
    log_file = Column(String)
    run_command = Column(String, comment="real command run in container")
    mounts = Column(JSON, comment="job run container mounts info")
    code_dir=Column(String, comment="job code dir on the node")
    reuse_run_id = Column(String)
    job_md5 = Column(String)
    experiment_id = Column(String)
    experiment_name = deferred(select([ExperimentMetadata.experiment_name]).where(ExperimentMetadata.experiment_id == experiment_id).scalar_subquery())
    parent_runid = Column(String)
    root_runid = Column(String)
    node_id = Column(String)
    run_uuid = Column(String)
    parent_run_uuid = Column(String)
    root_run_uuid = Column(String)
    component_id = Column(String)
    component_base_path = Column(String)
    run_root_dir = Column(String)
    container_image = Column(String)
    tags = Column(JSON)
    jobs = Column(JSON, comment="pipeline jobs info, only used for pipelinejob")
    graph = Column(PickleType)
    last_modified_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    def __repr__(self):
        return ("RunHistory(run_id=" + str(self.run_id) 
        + ", run_number=" + str(self.run_number) 
        + ", display_name=" + str(self.display_name) 
        + ", run_type=" + str(self.run_type) 
        + ", job_type=" + str(self.job_type)
        +", run_mode=" + str(self.run_mode)
        +", created_by=" + str(self.created_by)
        +", created_time=" + str(self.created_time)
        +", ready_time=" + str(self.ready_time)
        +", start_time=" + str(self.start_time)
        +", finish_time=" + str(self.finish_time)
        +", duration=" + str(self.duration)
        +", status=" + str(self.status)
        +", total_steps=" + str(self.total_steps)
        +", inputs=" + jsonpickle.encode(self.inputs, unpicklable = False)
        +", outputs=" + jsonpickle.encode(self.outputs, unpicklable = False)
        +", parameters=" + jsonpickle.encode(self.parameters, unpicklable = False)
        +", container_id=" + str(self.container_id)
        +", log_file=" + str(self.log_file)
        +", run_command=" + str(self.run_command)
        +", reuse_run_id=" + str(self.reuse_run_id)
        +", job_md5=" + str(self.job_md5)
        +", experiment_id=" + str(self.experiment_id)
        +", parent_runid=" + str(self.parent_runid)
        +", root_runid=" + str(self.root_runid)
        +", node_id=" + str(self.node_id)
        +", run_uuid=" + str(self.run_uuid)
        +", parent_run_uuid=" + str(self.parent_run_uuid)
        +", root_run_uuid=" + str(self.root_run_uuid)
        +", component_id=" + str(self.component_id)
        +", component_base_path=" + str(self.component_base_path)
        +", run_root_dir=" + str(self.run_root_dir)
        +", container_image=" + str(self.container_image)
        +", tags=" + str(self.tags)
        +", jobs=" + str(self.jobs)
        +", graph=" + jsonpickle.encode(self.graph, unpicklable = False) + ")"
        )
    
    def __eq__(self, other: RunHistory):
        return {
            self.run_id == other.run_id
            and self.run_number == other.run_number 
            and self.display_name == other.display_name 
            and self.run_type == other.run_type 
            and self.job_type == other.job_type 
            and self.run_mode == other.run_mode
            and self.created_by == other.created_by
            and self.created_time == other.created_time
            and self.ready_time == other.ready_time
            and self.start_time == other.start_time
            and self.finish_time == other.finish_time
            and self.duration == other.duration
            and self.status == other.status
            and self.total_steps == other.total_steps
            and jsonpickle.encode(self.inputs) == jsonpickle.encode(other.inputs)
            and jsonpickle.encode(self.outputs) == jsonpickle.encode(other.outputs)
            and jsonpickle.encode(self.parameters) == jsonpickle.encode(other.parameters)
            and self.container_id == other.container_id
            and self.log_file == other.log_file
            and self.run_command == other.run_command
            and self.reuse_run_id == other.reuse_run_id
            and self.job_md5 == other.job_md5
            and self.experiment_id == other.experiment_id
            and self.parent_runid == other.parent_runid
            and self.root_runid == other.root_runid
            and self.node_id == other.node_id
            and self.run_uuid == other.run_uuid
            and self.parent_run_uuid == other.parent_run_uuid
            and self.root_run_uuid == other.root_run_uuid
            and self.component_id == other.component_id
            and self.component_base_path == other.component_base_path
            and self.run_root_dir == other.run_root_dir
            and self.container_image == other.container_image
            and self.tags == other.tags
            and self.jobs == other.jobs
            and jsonpickle.encode(self.graph) == jsonpickle.encode(other.graph)
        }

class RunHistoryDBOperation:
    def __init__(self, Session):
        self.Session = Session

    def count(self, index_entities_request) -> int:
        with self.Session(expire_on_commit=False) as session:
            return query_count(RunHistory, index_entities_request, session)

    def select(self, index_entities_request) -> list:
        with self.Session(expire_on_commit=False) as session:
            return query(RunHistory, index_entities_request, session)
    
    def get(self, run_id) -> RunHistory:
        with self.Session(expire_on_commit=False) as session:
            return session.query(RunHistory).filter(RunHistory.run_id == run_id).first()

    def insert(self, insert_data: RunHistory):
        with self.Session(expire_on_commit=False) as session:
            record = session.query(func.max(RunHistory.run_number)).first()
            if record is not None and record[0] is not None:
                insert_data.run_number = record[0] + 1
            session.add(insert_data)
            session.commit()
        return insert_data

    def update(self, update_data):
        with self.Session(expire_on_commit=False) as session:
            ret = session.merge(update_data)
            session.commit()
            return ret

    def delete(self, delete_data_run_id):
        with self.Session(expire_on_commit=False) as session:
            session.query(RunHistory).filter(RunHistory.run_id == delete_data_run_id).delete()
            session.commit()
            return True