from enum import Enum
from typing import Dict
import uuid
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from piprundb import RunHistory, RunHistoryDBOperation, ComponentMetadata, ComponentMetadataDBOperation, ExperimentMetadata, ExperimentMetadataDBOperation
from pipruncommon import GeneralInput, GeneralOutput
from pipruncommon import InputType, OutputType, InputOutputModes
from .constants import JobRunningStatus
import getpass

from .graph import PipelineExecutionGraph, PipelineExecutionNode
from pipruncommon import Graph, GraphEdge, GraphDatasetNode, DataSetDefinition, PortInfo
from pipruncommon import RunInputOutputBase
from pipruncommon import CommandComponent as LocalCommandComponent
from azure.ai.ml import Input,Output
from azure.ai.ml.constants import JobType
from azure.ai.ml.entities import Component, CommandComponent
from azure.ai.ml.entities._job.pipeline._io import NodeInput, NodeOutput, PipelineInput, PipelineOutput

class MetadataUpdateType(Enum):
    READY_TIME= 0,
    START_TIME = 1,
    FINISH_TIME = 2

class MetadataRecorder(object):
    def __init__(self, Session):
        self.Session = Session
        self.run_history_db_operation = RunHistoryDBOperation(Session)
        self.component_metadata_db_operation = ComponentMetadataDBOperation(Session)
        self.experiment_metadata_db_operation = ExperimentMetadataDBOperation(Session)
        self.metadata_generated = False

    def add_pipeline_run_metadata(self, pipeline: PipelineExecutionGraph):
        # create graph
        graph = MetadataRecorder._generate_run_graph(self, pipeline)
        # create inputs/outputs
        inputs = []
        outputs = []
        parameters = []
        for k, v in pipeline._job.inputs.items():
            if isinstance(v._data, (Input, PipelineInput, Output, NodeOutput)):
                # non-parameter type input
                inputs.append(RunInputOutputBase(name=k, type=v._data.type, uri = v._data.path, mode = v._data.mode))
            else:
                # parameter
                parameters.append(RunInputOutputBase(name=k, type=v.type, value=v._data))

        for k, v in pipeline._job.outputs.items():
            output_type = v.type if v.type is not None else OutputType.URI_FOLDER
            output_mode = v.mode if v.mode is not None else InputOutputModes.RW_MOUNT
            outputs.append(RunInputOutputBase(name=k, type=output_type, mode=output_mode))
        # create jobs info
        jobs = {}
        for name, job in pipeline._job.jobs.items():
            # if isinstance(job, BaseNode):
            rest_node_dict = job._to_rest_object()
            jobs[name] = rest_node_dict

        cur_time = datetime.utcnow()

        run_history = RunHistory(run_id=pipeline._run_id,
            run_number=1,
            display_name = pipeline._name,
            run_type="azureml.PipelineRun",
            job_type=pipeline._run_type,
            run_mode=pipeline._run_mode,
            created_by=getpass.getuser(),
            created_time=cur_time,
            ready_time=cur_time, # this might need to change in future if we allow queue in local
            status=pipeline._status,
            total_steps=len(pipeline._nodes),
            log_file=pipeline._log_path, 
            parent_runid=pipeline._parent_run_id,
            root_runid=pipeline._root_run_id,
            node_id=pipeline._node_id,
            inputs=inputs,
            outputs=outputs,
            experiment_id = pipeline._experiment_id,
            tags = pipeline._job.tags,
            jobs = jobs,
            run_root_dir=pipeline._output_root_dir,
            parameters=parameters,
            graph=graph)
        self.run_history_db_operation.insert(run_history)
        self.metadata_generated = True
        # add or update experiment
        experiment_metadata = ExperimentMetadata(
            experiment_id = pipeline._experiment_id,
            experiment_name = pipeline._experiment_name,
            created_by = getpass.getuser(),
            last_run_time = cur_time,
            last_runid = pipeline._run_id,
            job_type = pipeline._job.type
        )
        self.experiment_metadata_db_operation.update(experiment_metadata)

        # add job run
        for n, node in pipeline._nodes.items():
            MetadataRecorder.add_job_run_metadata(self, node)

    def add_job_run_metadata(self, job: PipelineExecutionNode):
        component_str = job._job._component._to_yaml()
        component_id = job._component_id
        # build job inputs/outputs
        inputs = []
        outputs = []
        parameters = []
        for k,v in job._inputs.items():
            pip_reference = None
            param_data = None
            has_path = False
            path_type = None
            if isinstance(v._data, PipelineInput):
                pip_reference = v._data._name
                if isinstance(v._data._data, Input):
                    has_path = True
                    path_type = v._data._data.type
                else:
                    param_data = v._data
            elif isinstance(v._data, (Input, Output, NodeOutput)):
                has_path = True
                path_type = v._data.type
            else:
                param_data = v
            
            if has_path:
                input_mode = v._data.mode
                if input_mode is None:
                    input_mode = InputOutputModes.RO_MOUNT
                inputs.append(RunInputOutputBase(name=k, type=path_type, uri = v._data.path, mode = v._data.mode, pipelineReference=pip_reference))
            else:
                parameters.append(RunInputOutputBase(name=k, type=param_data.type, value=param_data._data, pipelineReference=pip_reference))

        for k, v in job._outputs.items():
            pip_reference = None
            if isinstance(v._data, PipelineOutput):
                pip_reference = v._data._name
                outputs.append(RunInputOutputBase(name=k, type=v._data.type, uri = v._data.path, mode = v._data.mode, pipelineReference=pip_reference))
            elif isinstance(v._data, Output):
                outputs.append(RunInputOutputBase(name=k, type=v._data.type, uri = v._data.path, mode = v._data.mode))

        # job run record
        run_history = RunHistory(run_id=job._run_id,
            run_number=1,
            display_name = job._job.name,
            run_type="azureml.StepRun",
            job_type=job._run_type,
            run_mode=job._curated_env_default_run_mode,
            created_by=getpass.getuser(),
            created_time=datetime.utcnow(),
            status=job._status,
            total_steps=1,  # need to change in future when subgraph is supported
            log_file=job._log_path, 
            parent_runid=job._parent_run_id,
            root_runid=job._root_run_id,
            node_id=job._node_id,
            component_id = component_id,
            experiment_id = job._experiment_id,
            component_base_path = str(job._job._component.base_path),
            run_root_dir=job._outputdir,
            inputs=inputs,
            outputs=outputs,
            parameters=parameters,
            tags = job._job.tags)
        self.run_history_db_operation.insert(run_history)
        # component info
        exist = self.component_metadata_db_operation.get(component_id)
        if exist is None:
            # need to add new component record
            component_type = job._job._component.type
            if component_type == JobType.COMMAND:
                originComponent: CommandComponent = job._job._component
                # build component inputs/outputs
                component_inputs: Dict[str, GeneralInput] = {}
                component_outputs: Dict[str, GeneralOutput] = {}
                for k, v in originComponent.inputs.items():
                    if isinstance(v, Input):
                        path = v.get("path")
                        default = v.default
                        min = v.get("min")
                        max = v.get("max")
                        component_inputs[k] = GeneralInput(name=k, type=v.type, path = path, default = default, min = min, max=max, optional=v.optional, mode=v.mode)
                for k, v in originComponent.outputs.items():
                    if isinstance(v, Output):
                        path = v.get("path")
                        component_outputs[k] = GeneralOutput(name=k, type=v.type, path=path, mode=v.mode)               
                component = LocalCommandComponent(component_id=component_id,
                    component_type=component_type,
                    description= originComponent.description,
                    name = originComponent.name,
                    display_name=originComponent.display_name,
                    version=originComponent.version,
                    tags=originComponent.tags,
                    properties=originComponent.properties,
                    is_deterministic=originComponent.is_deterministic,
                    command=originComponent.command,
                    code=originComponent.code,
                    inputs=component_inputs,
                    outputs=component_outputs,
                    raw_content=component_str
                    )
                component_meta = ComponentMetadata(component_id=component_id, component_type = component_type, created_time=datetime.utcnow(), component = component)
                self.component_metadata_db_operation.insert(component_meta)
            else:
                raise Exception(f"component type {component_type} not supported yet!")
        else:
            print("component already exist!")

    def update_job_status(self, run_id:str, status:JobRunningStatus, update_type: MetadataUpdateType):
        if update_type == MetadataUpdateType.READY_TIME:
            self.run_history_db_operation.update(RunHistory(run_id=run_id, status=status, ready_time=datetime.utcnow()))
        elif update_type == MetadataUpdateType.START_TIME:
            self.run_history_db_operation.update(RunHistory(run_id=run_id, status=status, start_time=datetime.utcnow()))
        elif update_type == MetadataUpdateType.FINISH_TIME:
            finish_time = datetime.utcnow()
            record = self.run_history_db_operation.get(run_id)
            duration = finish_time - record.start_time      # ? decrease 1970-01-01
            self.run_history_db_operation.update(RunHistory(run_id=run_id, status=status, finish_time=finish_time, duration = duration))

    def update_container_build_info(self, component_id:str, docker_file_content:str):
        if docker_file_content is not None:
            self.component_metadata_db_operation.update(ComponentMetadata(component_id=component_id, docker_file_content=docker_file_content))

    def update_container_run_info(self, run_id:str, container_image_id:str, run_command:str, mounts:dict, code_dir:str):
        self.run_history_db_operation.update(RunHistory(
            run_id=run_id, 
            container_image=container_image_id, 
            run_command=run_command,
            mounts=mounts,
            code_dir=code_dir))

    def update_container_id(self, run_id:str, container_id:str):
        self.run_history_db_operation.update(RunHistory(run_id=run_id, container_id=container_id))

    def _generate_run_graph(self, pipeline_graph: PipelineExecutionGraph) -> Graph:
        datasets: Dict[str, GraphDatasetNode] = {}
        edges = []
        for k, v in pipeline_graph._pipeline_inputs.items():
            if isinstance(v._data, (Input, PipelineInput, Output, NodeOutput)):
                # data source input
                node_id = str(uuid.uuid1())
                ds = GraphDatasetNode(id = node_id, dataSetDefinition=DataSetDefinition(parameterName=k, dataTypeShortName="path"))
                datasets[k] = ds

        for name, node in pipeline_graph._nodes.items():
            dst_node_id = node._node_id
            for k, v in node._inputs.items(): 
                if isinstance(v, NodeInput):
                    dst_port = PortInfo(nodeId=dst_node_id, portName=k)
                    if isinstance(v._data, NodeOutput):
                        # input is a job output
                        src_job_name = v._data._owner.name
                        src_node_id = pipeline_graph._nodes[src_job_name]._node_id
                        src_port_name = v._data._name
                        src_port = PortInfo(nodeId=src_node_id, portName=src_port_name)
                        edges.append(GraphEdge(sourceOutputPort=src_port, destinationInputPort=dst_port))
                    elif isinstance(v._data, PipelineInput) and hasattr(v._data._data, "path"):
                        # input is a data source
                        graph_port_name = v._data._name
                        src_dataset :GraphDatasetNode= datasets.get(graph_port_name)
                        src_node_id = src_dataset.id
                        src_port = PortInfo(nodeId=src_node_id)
                        edges.append(GraphEdge(sourceOutputPort=src_port, destinationInputPort=dst_port))
            
            for k, v in node._job.outputs.items():
                # based on output reference to detect whether this is pipeline output
                if isinstance(v, NodeOutput) and isinstance(v._data, PipelineOutput):
                    src_port = PortInfo(nodeId=dst_node_id, portName=k)
                    dst_port = PortInfo(graphPortName=v._data._name)
                    edges.append(GraphEdge(sourceOutputPort=src_port, destinationInputPort=dst_port))
        ds = [p for _, p in datasets.items()]
        return Graph(datasetNodes=ds, edges=edges)