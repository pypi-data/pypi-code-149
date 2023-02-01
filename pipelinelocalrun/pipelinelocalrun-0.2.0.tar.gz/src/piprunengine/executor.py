import subprocess
import os
import re
import sys
import logging
import logging.handlers
from typing import Dict
from pathlib import Path

from azure.ai.ml import MLClient, Input, Output
from azure.ai.ml.entities import PipelineJob, CommandJob, Job
from azure.ai.ml.entities._builders import Command, Sweep
from azure.ai.ml.entities._job.pipeline._io import NodeOutput, PipelineInput, PipelineOutput
from azure.ai.ml.constants import AssetTypes

import docker
from docker import DockerClient
from docker.types import Mount
from docker.errors import NotFound, APIError
from docker.models.containers import Container

from .graph import PipelineExecutionNode, PipelineExecutionGraph
from .image_builder import LocalImageBuilder
from .constants import JobRunningStatus, LocalRunMode, CuratedEnvironmentDefaultRunMode, JobLocalRunMode, BLOB_WASBS_REGEX, BLOB_HTTPS_PATTERN
from .metadata import MetadataRecorder, MetadataUpdateType
from ._utils import server_ok, download
from .logger import log_setup, get_logger

import uuid
from piprundb import all_tables
from pipruncommon import db_setup, DEFAULT_DB_PATH

# def get_logger(logger_name, log_level:int = logging.INFO, log_path:str = None, std_out:bool = False, log_formatter:logging.Formatter = None) -> logging.Logger:
#     logger = logging.getLogger(logger_name)
#     logger.setLevel(log_level)
#     if log_path:
#         fh = logging.handlers.RotatingFileHandler(log_path, mode='w', backupCount=5)
#         if log_formatter:
#             fh.setFormatter(log_formatter)
#         logger.addHandler(fh)
#     if std_out:
#         logger.addHandler(logging.StreamHandler(sys.stdout))
#     return logger

# def get_infra_logger(logger_name, log_path:str = None, ) -> logging.Logger:
#     formatter = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                                     datefmt='%m-%d-%y %H:%M:%S')
#     return get_logger(logger_name=logger_name, log_level=logging.DEBUG, log_path=log_path, std_out=True, log_formatter=formatter)

# def log_setup(log_path):
#     return get_infra_logger("orchestrator",log_path)
HOME_PATH = os.path.join(os.path.sep, str(Path.home()), ".azureml", "piprun")

def run(
    *,
    output_root_dir: str=None,
    job: Job,
    experiment_name: str = None,
    ml_client: MLClient = None,
    run_mode: LocalRunMode = LocalRunMode.COMPUTE_LOCAL_METRICS_LOCAL,
    curated_env_default_run_mode = CuratedEnvironmentDefaultRunMode.CONTAINER,
     **kwargs,
):  
    """
    """
    run_id = str(uuid.uuid1())
    # currently only support COMPUTE_LOCAL_METRICS_LOCAL
    if run_mode != LocalRunMode.COMPUTE_LOCAL_METRICS_LOCAL:
        raise Exception(f"found unsupported mode: {run_mode}, only mode {LocalRunMode.COMPUTE_LOCAL_METRICS_LOCAL} is supported!")
    if isinstance(job, CommandJob):
        raise Exception("standalone job run not supported yet!")
    elif isinstance(job, PipelineJob):
        db_dir = os.path.dirname(DEFAULT_DB_PATH)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)
        Session = db_setup(DEFAULT_DB_PATH, all_tables)
        metadata_recorder = MetadataRecorder(Session)
        try:
            _run_pipeline(output_root_dir=output_root_dir, 
                pipeline_job=job, 
                experiment_name=experiment_name, 
                metadata_recorder = metadata_recorder, 
                ml_client=ml_client, run_mode=run_mode, 
                curated_env_default_run_mode=curated_env_default_run_mode,
                run_id=run_id)
        except:
            if metadata_recorder.metadata_generated:
                metadata_recorder.update_job_status(run_id, JobRunningStatus.FAIL, MetadataUpdateType.FINISH_TIME)
            raise sys.exc_info()[0]
        finally:
            Session.close_all()
    else:
        raise Exception(f"found unsupported Job type: {run_mode}, only mode {LocalRunMode.COMPUTE_LOCAL_METRICS_LOCAL} is supported!")


def _run_pipeline(
    *,
    output_root_dir: str=None,
    pipeline_job: PipelineJob,
    experiment_name: str = None,
    metadata_recorder: MetadataRecorder = None,
    ml_client: MLClient = None,
    run_mode: LocalRunMode = LocalRunMode.COMPUTE_LOCAL_METRICS_LOCAL,
    curated_env_default_run_mode = CuratedEnvironmentDefaultRunMode.CONTAINER,
     **kwargs,
):
    """
    """
    # currently only support COMPUTE_LOCAL_METRICS_LOCAL
    if run_mode != LocalRunMode.COMPUTE_LOCAL_METRICS_LOCAL:
        raise Exception(f"found unsupported mode: {run_mode}, only mode {LocalRunMode.COMPUTE_LOCAL_METRICS_LOCAL} is supported!")
    # validate pipeline job, currently only support command job
    for _, job_instance in pipeline_job.jobs.items():
        if not isinstance(job_instance, Command): #check sweep job?
            raise Exception(f"Not supported pipeline job type: {type(job_instance)}")
    
    if not os.path.exists(HOME_PATH):
        os.makedirs(HOME_PATH)
    if experiment_name is None:
        # use Default as experiment name if not provided
        experiment_name = "Default"
    _run_id = kwargs.get("run_id", str(uuid.uuid1()))
    if output_root_dir is None:
        output_root_dir = HOME_PATH #os.getcwd()
    if not os.path.isabs(output_root_dir):
        output_root_dir = os.path.join(os.path.sep, HOME_PATH, output_root_dir)
    log_path = os.path.join(os.path.sep, output_root_dir, _run_id, "orchestrator.log")
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log = log_setup(log_path=log_path)
    if pipeline_job.name is None:
        pipeline_job.name = _run_id
    # build pipeline execution graph
    graph = PipelineExecutionGraph(output_root_dir=output_root_dir, pipeline_job=pipeline_job, experiment_name=experiment_name, curated_env_default_run_mode=curated_env_default_run_mode, run_id = _run_id, log_path=log_path)
    # record pipeline run metadata
    if metadata_recorder is None:
        Session = db_setup(DEFAULT_DB_PATH, all_tables)
        metadata_recorder = MetadataRecorder(Session)
    metadata_recorder.add_pipeline_run_metadata(graph)
    metadata_recorder.update_job_status(graph._run_id, JobRunningStatus.RUNNING, MetadataUpdateType.START_TIME)
    image_builder = LocalImageBuilder(ml_client, log_path)
    while not graph.is_finish():
        nodes_to_run = graph.get_ready_nodes()
        for name, node in nodes_to_run.items():
            metadata_recorder.update_job_status(node._run_id, JobRunningStatus.NOT_STARTED, MetadataUpdateType.READY_TIME)
        for name, node in nodes_to_run.items():
            # better to record image build time separately
            metadata_recorder.update_job_status(node._run_id, JobRunningStatus.RUNNING, MetadataUpdateType.START_TIME)
            run_mode = node.get_run_mode()
            success = True
            try:
                if run_mode == JobLocalRunMode.NATIVE:
                    # run as native process
                    success = _run_with_native_process(node, log)
                elif run_mode == JobLocalRunMode.DOCKER:
                    # build image using job component environment
                    # TODO: check whether need to build image first
                    image_name, docker_file_content = image_builder.build_container_image(pipeline_job.name, node._job)
                    metadata_recorder.update_container_build_info(node._component_id, docker_file_content)
                    success = _run_with_docker_image(image_name, node, log, metadata_recorder)
                else:
                    # TODO: define error type for this
                    raise Exception(f"Found unsupported run mode: {run_mode}")
            except:
                log.error("Oops! %s occurred.", sys.exc_info()[0])
                success = False
                metadata_recorder.update_job_status(node._run_id, JobRunningStatus.FAIL, MetadataUpdateType.FINISH_TIME)
                raise sys.exc_info()[0]

            if not success:
                log.info(f"pipeline {pipeline_job.name} stopped due to failed job {name}!")
                metadata_recorder.update_job_status(node._run_id, JobRunningStatus.FAIL, MetadataUpdateType.FINISH_TIME)
                metadata_recorder.update_job_status(graph._run_id, JobRunningStatus.FAIL, MetadataUpdateType.FINISH_TIME)
                return
            else:
                metadata_recorder.update_job_status(node._run_id, JobRunningStatus.SUCCESS, MetadataUpdateType.FINISH_TIME)

    log.info(f"pipeline {pipeline_job.name} finished successfully!")
    metadata_recorder.update_job_status(graph._run_id, JobRunningStatus.SUCCESS, MetadataUpdateType.FINISH_TIME)

def _run_with_native_process(node: PipelineExecutionNode, log: logging.Logger) -> bool:
    # run as native process
    name = node._job.name
    working_dir = _get_working_dir(node)
    run_command = node.command()
    cmd_array = run_command.split()
    log.info(f"############################################{name}##############################################")
    log.debug(f"start running job {name}")
    params = {}
    params["capture_output"]=True
    if working_dir is not None:
        params["cwd"] = working_dir
    process = subprocess.run(cmd_array, **params)
    success = (process.returncode == 0)
    job_logger = get_logger(node._job.name, log_path=node._log_path, std_out=True)
    # TODO: update to streaming mode
    print_pretty(process.stdout.decode("utf-8"), job_logger)
    node.mark_run_result(success)
    log.info(f"job {name} finished with result: {success}")
    if not success:
        err_data = process.stderr.decode("utf-8")
        log.info(f"Run job {name} with failure return code: {process.returncode}, error: {err_data}")
        print_pretty(process.stderr.decode("utf-8"), log)
    return success

def _run_with_docker_image(docker_image_name:str, node: PipelineExecutionNode, log: logging.Logger, metadata_recorder: MetadataRecorder, docker_client: DockerClient=None) -> bool:
    container_name= node._job.name
    log.info(f"##########################################{container_name} start################################################")
    log.debug(f"docker image: {docker_image_name}")
    if docker_client is None:
        docker_client = docker.from_env()
    # get working dir
    working_dir = _get_working_dir(node)
    log.debug(f"working dir: {working_dir}")
    # build mount for input/output path
    volumn_mapping: Dict[str, str] = {}
    template_params = {}
    idx = 1
    # TODO: do we need to care about mounting mode? 
    # currently by default ro mode for input and rw mode for output
    for input_name, input in node.inputs().items():
        key = f"inputs_{input_name}"
        has_path = False
        data = None
        path_type = None
        if isinstance(input._data, PipelineInput):
            if isinstance(input._data._data, Input):
                has_path = True
                path_type = input._data._data.type
            else:
                data = input._data._data
            pass
        elif isinstance(input._data, (Input, Output, NodeOutput)):
            has_path = True
            path_type = input._data.type
        else:
            data = input._data

        if has_path:
            if path_type == AssetTypes.URI_FILE:
                input_path = prepare_input_path_for_remote_file(input._data.path, node._inputs_temp_dir, log)
                dir_name = os.path.dirname(input_path)
                file_name = os.path.basename(input_path)
                if dir_name in volumn_mapping.keys():
                    template_params[key] = os.path.join(volumn_mapping[input_path],file_name)
                else:
                    mapping_path = f"/{node._job.name}/inputs/{idx}/{file_name}"
                    idx += 1
                    volumn_mapping[input_path] = mapping_path
                    template_params[key] = mapping_path
            else:
                if input._data.path not in volumn_mapping.keys():
                    mapping_path = f"/{node._job.name}/inputs/{idx}"
                    idx += 1
                    volumn_mapping[input._data.path] = mapping_path
                    template_params[key] = mapping_path
                else:
                    template_params[key] = volumn_mapping[input._data.path]
        else:
            template_params[key] = data
    
    idx = 1
    shared_folder: Dict[str, bool] = {}
    for output_name, output in node.outputs().items():
        key = f"outputs_{output_name}"
        if isinstance(output._data, Output):
            # if output._data.type == AssetTypes.URI_FOLDER or output._data.type == AssetTypes.MLFLOW_MODEL:
            if output._data.type == AssetTypes.URI_FILE:
                dir_name = os.path.dirname(output._data.path)
                file_name = os.path.basename(output._data.path)
                if dir_name in volumn_mapping.keys:
                    # shared folder for input/output
                    shared_folder[dir_name] = True
                    template_params[key] = os.path.join(volumn_mapping[dir_name],file_name)
                else:
                    mapping_path = f"/{node._job.name}/outputs/{idx}/{file_name}"
                    idx += 1
                    volumn_mapping[output._data.path] = mapping_path
                    template_params[key] = mapping_path
            else:
                if output._data.path not in volumn_mapping.keys():
                    mapping_path = f"/{node._job.name}/outputs/{idx}"
                    idx += 1
                    volumn_mapping[output._data.path] = mapping_path
                    template_params[key] = mapping_path
                else:
                    # shared folder for input/output
                    shared_folder[output._data.path] = True
                    template_params[key] = volumn_mapping[output._data.path]
        else:
            template_params[key] = output._data
    log.debug(f'volumn_mapping: {volumn_mapping}')
    log.debug(f'template_params: {template_params}')
    command_template = node._command_template
    command_in_docker = command_template.substitute(template_params)
    log.info(f"Command run in docker: {command_in_docker}")
    # rebuild docker command
    mnts = []
    mnts_meta = {}
    for src, target in volumn_mapping.items():
        read_only = "/inputs/" in target and src not in shared_folder.keys()
        mnt = Mount(source=src, type='bind', read_only=read_only, target=target)
        mnts.append(mnt)
        mnts_meta.update({src: {"bind": target}})

    metadata_recorder.update_container_run_info(node._run_id, docker_image_name, command_in_docker, mnts_meta, working_dir)

    # add code dir mnting
    working_dir_docker = working_dir
    if working_dir is not None:
        dir_name = os.path.dirname(working_dir)
        base_name = os.path.basename(working_dir)
        log.debug(f"dirname: {dir_name}, basename: {base_name}")
        if dir_name in volumn_mapping.keys(): 
            working_dir_docker = f"{volumn_mapping[dir_name]}/{base_name}"
        else:
            working_dir_docker = f"/{node._job.name}/cwd/{base_name}"
            mnt = Mount(source=working_dir, type='bind', target=working_dir_docker)
            mnts.append(mnt)
            log.debug(f"binding {working_dir} to {working_dir_docker} in volumes")
    try:
        container = docker_client.containers.get(container_name)
        if container.status == "running":
            container.stop()
        container.remove()
    except NotFound:
        pass
    params={}
    if working_dir_docker is not None:
        params["working_dir"] = working_dir_docker
    # check whether local mlflow tracking server starts or not, if it start, then set env for container
    mlflow_start = server_ok("http://localhost:5000")
    if mlflow_start:
        params["environment"] = ["MLFLOW_TRACKING_URI=http://host.docker.internal:5000/"]
        mlflow_dir = os.path.join(HOME_PATH, "mlflow")
        target_dir = "/metadata/mlflow"
        mnt = Mount(source=mlflow_dir, type='bind', target=target_dir)
        mnts.append(mnt)
        log.debug(f"binding {mlflow_dir} to {target_dir} in volumes")
    container: Container = docker_client.containers.run(docker_image_name, detach=True, mounts=mnts, name=container_name, command=["/bin/bash", "-c", command_in_docker], **params)
    log.info(f"container-id: {container.id}")
    log_gen = container.logs(stream=True)
    container_logger = get_logger(node._job.name, log_path=node._log_path)
    try:
        while True:
            line = next(log_gen).decode("utf-8").strip()
            if len(line) > 0:
                container_logger.info(line)
    except StopIteration:
        log.info(f'log stream ended for {container_name}')
    result = container.wait()
    success = result['StatusCode'] == 0
    node.mark_run_result(success)
    log.info(f"Container {node._job.name} finished with result: {success}")
    if not success:
        log.info(f"Container {node._job.name} run result: {result}")
    metadata_recorder.update_container_id(node._run_id, container.id)
    log.info(f"##########################################{container_name} Finish################################################")
    return success

def _get_working_dir(node: PipelineExecutionNode) -> str:
    working_dir = None
    if node._job._component.code is not None:
        working_dir = str(node._job._component.code)
    if working_dir is not None and not os.path.isabs(working_dir):
        if  os.path.isabs(node._job._component.base_path):
            working_dir = os.path.join(node._job._component.base_path, working_dir.strip("./"))
        else:
            working_dir = os.path.abspath(working_dir)
    return working_dir

def print_pretty(data: str, log: logging.Logger):
    lines = data.split("\n")
    for l in lines:
        data = l.strip()
        if len(data) > 0:
            log.info(l)
            # print(data)

def prepare_input_path_for_remote_file(path:str, inputs_dir: str, log: logging.Logger) -> str:    
    x = re.match(BLOB_WASBS_REGEX, path)
    if x:
        remote_url = BLOB_HTTPS_PATTERN.format(x.group(2), x.group(1), x.group(3))
        if not os.path.exists(inputs_dir):
            os.makedirs(inputs_dir)
        file_path = os.path.join(inputs_dir, x.group(3))
        if download(remote_url, file_path):
            return file_path
        else:
            log.info(f"Downloading file {remote_url} failed!")
    return path