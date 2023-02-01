from __future__ import annotations
from abc import abstractmethod
from typing import Dict, Union
import uuid
import hashlib
from azure.ai.ml.entities import CommandComponent, PipelineJob
from azure.ai.ml import Input,Output
from azure.ai.ml.entities._builders import BaseNode
from azure.ai.ml.entities._assets import Environment
from azure.ai.ml.entities._job.pipeline._io import NodeInput, NodeOutput, PipelineInput, PipelineOutput
import re
from string import Template
import os

from pipruncommon import RunType

from .constants import JobRunningStatus, JobLocalRunMode, CuratedEnvironmentDefaultRunMode

class BaseExecutionNode(object):
    """
    """
    def __init__(
        self,
        output_root_dir: str,
        job: BaseNode,
        curated_env_default_run_mode = CuratedEnvironmentDefaultRunMode.CONTAINER,
        **kwargs,
        ):
        self._status = JobRunningStatus.NOT_STARTED
        self._job = job
        self._command: str = job.command
        # create output sub dir for job
        self._outputdir = os.path.join(output_root_dir, job.name)
        if not os.path.exists(self._outputdir):
            os.makedirs(self._outputdir)
        self._curated_env_default_run_mode = curated_env_default_run_mode
    
    @abstractmethod
    def inputs() -> Dict[str, Union[Input, PipelineInput, Output, NodeOutput]]:
        pass

    @abstractmethod
    def outputs() -> Dict[str, Union[Output, NodeOutput]]:
        pass

    def status(self) -> str:
        return self._status

    def mark_run_result(self, success: bool):
        if success:
            self._status = JobRunningStatus.SUCCESS
        else:
            self._status = JobRunningStatus.FAIL

    def is_finish(self) -> bool:
        return self._status == JobRunningStatus.SUCCESS or self._status == JobRunningStatus.FAIL

    @abstractmethod
    def is_ready(selft) -> bool:
        pass

    def get_run_mode(self) -> str:
        if "image" in self._job.tags.keys():
            return JobLocalRunMode.DOCKER
        # need to build container for local environment
        if isinstance(self._job._component, CommandComponent):
            env = self._job._component.environment
            if isinstance(env, Environment) and (env.image or (env.build and env.build.path)):
                return JobLocalRunMode.DOCKER
            if isinstance(env, str) and self._curated_env_default_run_mode == CuratedEnvironmentDefaultRunMode.CONTAINER:
                return JobLocalRunMode.DOCKER
        return JobLocalRunMode.NATIVE

    def command(self) -> str:
        return self._command

_ALLOWED_TYPES = {
        "integer": (int),
        "string": (str),
        "number": (float),
        "boolean": (bool),
    }

class PipelineExecutionNode(object):
    """
    """
    def __init__(
        self,
        output_root_dir: str,
        job: BaseNode,
        pipeline_inputs: Dict[str, NodeInput],
        pipeline_outputs: Dict[str, NodeOutput],
        curated_env_default_run_mode = CuratedEnvironmentDefaultRunMode.CONTAINER,
        **kwargs,
        ):
        self._status = JobRunningStatus.NOT_STARTED
        self._job = job
        self._run_id = str(uuid.uuid1())
        self._node_id = str(uuid.uuid1())
        self._parent_run_id = kwargs.get("parent_run_id", None)
        self._root_run_id = kwargs.get("root_run_id", None)
        self._experiment_name = kwargs.get("experiment_name", None)
        self._experiment_id = kwargs.get("experiment_id", None)
        self._run_type = RunType.COMMAND_JOB
        #if isinstance(job, Command):
        self._command: str = job.command
        component_str = job._component._to_yaml()
        self._component_id = hashlib.md5(component_str.encode('utf-8')).hexdigest()
        job._component._id = self._component_id
        self._dependencies: Dict[str, PipelineExecutionNode] = {}
        # create output sub dir for job
        self._outputdir = os.path.join(output_root_dir, job.name, "outputs")
        if not os.path.exists(self._outputdir):
            os.makedirs(self._outputdir)
        # prepare input path for those data which we need to download from remote
        self._inputs_temp_dir = os.path.join(output_root_dir, "inputs")
        # self._log_path = os.path.join(os.sep, output_root_dir, f"{job.name}_run.log")  # to be refined for mpi job
        self._log_path = os.path.join(os.sep, output_root_dir, job.name, "run.log") 
        self._pipeline_inputs = pipeline_inputs
        self._pipeline_outputs = pipeline_outputs
        self._curated_env_default_run_mode = curated_env_default_run_mode
        # Dict[str, Union[int, bool, float, str, Input, JobInput]]
        self._inputs: Dict[str, NodeInput] = {}
        self._outputs: Dict[str, NodeOutput] = {}
        # iterate node output(PipelineOutput) dic
        for key, output in job.outputs.items():
            # get job output with type `Output`
            job_output = output._to_job_output()
            if job_output is None:
                v = PipelineOutput(name=key, data=Output(path=self._outputdir), meta=output._meta, owner=job)
                self._outputs[key] = v
                continue
            d = job_output.path
            # try to find pipeline output or create new if not defined
            if isinstance(d, str) and d.startswith("$"):
                d = d.strip("${}")
                sections = d.split(".")
                if len(sections) != 3:
                    raise Exception(f"Not supported pipeline job output: {d}")
                output_key = sections[2]
                if output_key in pipeline_outputs.keys():
                    v = pipeline_outputs[output_key]
                    meta = job._component.outputs[key]
                    if v._data is None:
                        joboutput = Output(path=self._outputdir)
                        # joboutput = Output(path=output_root_dir)
                        v = PipelineOutput(name=key, data=joboutput, meta=meta, owner=job)
                    else:
                        if v.path is None:
                            v.path = ""
                        if not os.path.isabs(v.path):
                            v.path = os.path.join(self._outputdir, v.path.strip("./\\"))
                        # TODO: move such logic to a common pre-run step
                        if not os.path.exists(v.path):
                            os.makedirs(v.path)
                        v = PipelineOutput(name=key, data=v._data, meta=meta, owner=job)
                    self._outputs[key] = v
                else:
                    raise Exception(f"job output with key {output_key} not defined in pipeline")
            else:
                if output.path is None:
                    output.path = self._outputdir
                self._outputs[key] = output

    def set_dependencies(self, dependencies: Dict[str, PipelineExecutionNode]):
        self._dependencies = dependencies
        # regenerate input
        for key, input in self._job.inputs.items():
            job_input = input._to_job_input()
            if not isinstance(job_input, Input):
                self._inputs[key] = input
                continue
            input_data = job_input.path
            meta = self._job._component.inputs[key]
            if isinstance(input_data, str) and input_data.startswith("$"):
                input_data = input_data.strip("${}")
                sections = input_data.split(".")
                if len(sections) == 3:
                    # pipeline input
                    input_key = sections[2]
                    if input_key in self._pipeline_inputs.keys():
                        v = self._pipeline_inputs[input_key]
                        if v is None:
                            raise Exception(f"job input {input_key} is found empty in pipeline")
                        # self._inputs[key] = PipelineInput(name=input_key, meta=meta, data=v._data)
                        self._inputs[key] = NodeInput(name=key, meta=meta, data=v, owner=self._job)
                    else:
                        raise Exception(f"job input with key {input_key} not defined in pipeline")
                elif len(sections) == 5:
                    # other job input
                    src_job = sections[2]
                    job_output_key = sections[4]
                    if src_job not in dependencies.keys():
                        raise Exception(f"dependency job with name {src_job} not found")
                    src_node = dependencies[src_job]
                    if job_output_key not in src_node.outputs().keys():
                        raise Exception(f"output name {job_output_key} not found in dependency job {src_job}")
                    self._inputs[key] = NodeInput(name=key, meta=meta, data=src_node.outputs()[job_output_key], owner=self._job)
                else:
                    raise Exception(f"Not supported pipeline job input: {input_data}")
            else:
                 self._inputs[key] = input
        # generate final runnable command
        self._command_template = build_command_template(self._command, self._inputs, self._outputs)
        self._command = generate_runnable_command(self._command, self._inputs, self._outputs)

    def status(self) -> str:
        return self._status

    def mark_run_result(self, success: bool):
        if success:
            self._status = JobRunningStatus.SUCCESS
        else:
            self._status = JobRunningStatus.FAIL

    def is_ready(self) -> bool:
        ready = True
        for _, node in self._dependencies.items():
            if node.status() != JobRunningStatus.SUCCESS:
                ready = False
                break
        return ready
    
    def is_finish(self) -> bool:
        return self._status == JobRunningStatus.SUCCESS or self._status == JobRunningStatus.FAIL
    
    def get_run_mode(self) -> str:
        if "image" in self._job.tags.keys():
            return JobLocalRunMode.DOCKER
        # need to build container for local environment
        if isinstance(self._job._component, CommandComponent):
            env = self._job._component.environment
            if isinstance(env, Environment) and (env.image or (env.build and env.build.path)):
                return JobLocalRunMode.DOCKER
            if isinstance(env, str) and self._curated_env_default_run_mode == CuratedEnvironmentDefaultRunMode.CONTAINER:
                return JobLocalRunMode.DOCKER
        return JobLocalRunMode.NATIVE

    def inputs(self) -> Dict[str, NodeInput]:
        return self._inputs

    def command(self) -> str:
        return self._command

    def outputs(self) -> Dict[str, NodeOutput]:
        return self._outputs

def generate_runnable_command(command: str, inputs: Dict[str, NodeInput], outputs: Dict[str, NodeOutput]) -> str:
    command_template = build_command_template(command, inputs, outputs)
    template_params = {}
    for k, v in inputs.items():
        key = f"inputs_{k}"
        has_path = False
        data = None
        if isinstance(v._data, PipelineInput):
            if isinstance(v._data._data, Input):
                has_path = True
            else:
                data = v._data._data
        elif isinstance(v._data, (Input, Output, NodeOutput)):
            has_path = True
        else:
            data = v._data

        if has_path:
            template_params[key] = v._data.path
        else:
            template_params[key] = data
    for k, v in outputs.items():
        key = f"outputs_{k}"
        if isinstance(v._data, Output):
            template_params[key] = v._data.path
        else:
            template_params[key] = v._data
    return command_template.substitute(template_params)

def build_command_template(command: str, inputs: Dict[str, NodeInput], outputs: Dict[str, NodeOutput]) -> Template:
     # generate runnable command
    optinal_params = re.findall("\[.*?\]", command)
    if len(optinal_params) != 0:
        must_parts = re.split("\[.*?\]", command)
        # check whether optional param has value
        keep = []
        for p in must_parts:
            keep.append(p.strip(" "))
        for p in optinal_params:
            s = re.search("\{\{(.*)\}\}", p)
            param = s.group(1)
            param_parts = param.split(".")
            if len(param_parts) != 2:
                raise Exception(f"command parameter in wrong format: {param}")
            if param_parts[0] == "inputs":
                if param_parts[1] in inputs.keys():
                    keep.append(p.strip("[]"))
            elif param_parts[0] == "outputs":
                # this may not need
                if param_parts[1] in outputs.keys():
                    keep.append(p.strip("[]"))
            else:
                raise Exception(f"unknown param type: {param}")
        command = " ".join(keep)    
    command = command.replace("{{", "").replace("}}","").replace("inputs.", "inputs_").replace("outputs.", "outputs_")
    return Template(command)


class PipelineExecutionGraph(object):
    """
    """
    def __init__(
        self,
        output_root_dir: str,
        pipeline_job: PipelineJob,
        experiment_name:str,
        curated_env_default_run_mode = CuratedEnvironmentDefaultRunMode.CONTAINER,
        **kwargs,
        ):
        self._name = pipeline_job.name
        self._run_mode = curated_env_default_run_mode
        self._job = pipeline_job
        self._status = JobRunningStatus.NOT_STARTED
        self._nodes: Dict[str, PipelineExecutionNode] = {}
        self._dependencies: Dict[str, list] = {}
        self._run_id = kwargs.get("run_id", str(uuid.uuid1()))
        self._node_id = str(uuid.uuid1())
        self._parent_run_id = kwargs.get("parent_run_id", None)
        self._root_run_id = kwargs.get("root_run_id", self._run_id)
        self._run_type = RunType.PIPELINE_JOB
        self._output_root_dir = os.path.join(os.path.sep, output_root_dir, self._run_id)
        self._experiment_name = experiment_name
        self._experiment_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, experiment_name))
        if not os.path.exists(self._output_root_dir):
            os.makedirs(self._output_root_dir)
        # pre-process pipeline inputs
        self._pipeline_inputs : Dict[str, Input] = {}
        for name, input in pipeline_job.inputs.items():
            # why this is needed?
            if hasattr(input._data, "path") and "://" not in input.path:
                input.path = os.path.abspath(input.path)
            self._pipeline_inputs[name] = input
        # create run history for pipeline run
        self._log_path = kwargs.get("log_path")
        for name, job in pipeline_job.jobs.items():
            # print(job._component._to_yaml())
            node = PipelineExecutionNode(
                output_root_dir=self._output_root_dir, 
                job=job, 
                pipeline_inputs=self._pipeline_inputs, 
                pipeline_outputs=pipeline_job.outputs, 
                curated_env_default_run_mode=curated_env_default_run_mode, 
                parent_run_id=self._run_id, 
                root_run_id=self._root_run_id,
                experiment_name=experiment_name,
                experiment_id=self._experiment_id
                )
            self._nodes[name] = node
            dependencies = self._get_dependency_jobs(job)
            self._dependencies[name] = dependencies
        for name, deps in self._dependencies.items():
            dep_nodes: Dict[str, PipelineExecutionNode] = {}
            for dp in deps:
                dep_nodes[dp] = self._nodes[dp]
            self._nodes[name].set_dependencies(dep_nodes)

    def _get_dependency_jobs(self, job: BaseNode) -> list:
        res = []
        for n, input in job.inputs.items():
            if isinstance(input._data, (Output, NodeOutput)):
                res.append(input._data._owner.name)
        return res

    def get_ready_nodes(self) -> Dict[str, PipelineExecutionNode]:
        read_nodes: Dict[str, PipelineExecutionNode] = {}
        for name, node in self._nodes.items():
            if node.is_ready() and not node.is_finish():
                read_nodes[name] = node
        return read_nodes
    
    def is_finish(self) -> bool:
        for name, node in self._nodes.items():
            if node.status() != JobRunningStatus.SUCCESS and node.status() != JobRunningStatus.FAIL:
                return False
        return True

def main():
    command = "python train.py  --training_data ${{inputs.training_data}}  [--max_epochs ${{inputs.max_epochs}}]  --learning_rate ${{inputs.learning_rate}}  [--learning_rate_schedule ${{inputs.learning_rate_schedule}}]  --model_output ${{outputs.model_output}}"
    inputs: Dict[str, Input] = {}
    outputs: Dict[str, Output] = {}
    inputs["training_data"] = Input(name="training_data", meta=None, data=PipelineInput(name="ttt", meta=None, data=Input(path="/train/data")))
    inputs["learning_rate"] =Input(name="learning_rate", meta=None, data=0.5)
    inputs["max_epochs"] = Input(name="max_epochs", meta=None, data=10)
    inputs["learning_rate_schedule"] = Input(name="learning_rate_schedule", meta=None, data="time-based")
    outputs["model_output"] = Output(name= "model_output", meta=None, data=Output(path="/train/output"))
    cmd = generate_runnable_command(command=command, inputs=inputs, outputs=outputs)
    print(cmd)

if __name__ == "__main__":
    main()