import os
import binascii
import re

from .base_debugger import Language
from .py_debugger import PythonDebugger
from .r_debugger import RDebugger
from .debug_meta import DebugMetadata

# VSCODE_DEVCONTAINER_INVOKE_CMD_PATTERN = "code --folder-uri vscode-remote://dev-container+{hex_encoded_devcontainer_path}{app_path}"

#TODO: add R support
SUPPORTED_DEBUGGER = [Language.PYTHON, Language.R]

class DebuggerNotSuportedError(Exception):
    def __init__(self, err="debugger not supported") -> None:
        self.err = err
        Exception.__init__(self,err)

def check_job_programming_language(code_dir:str, command:str) -> Language:
    if command:
        exe = command.lstrip(" ").split(" ")[0]
        if command.startswith("python") or exe.endswith(".py"):
            return Language.PYTHON
        if command.startswith("Rscript") or command.startswith("R "):
            return Language.R
    if code_dir is None:
        return Language.NONE
    # TODO: detect language by code_dir (guesslang is too big, consider pygments first)
    return None

def prepare_debug_info(meta: DebugMetadata):
    #1. check programming language
    language = check_job_programming_language(meta.code_dir, meta.command)
    if language == Language.NONE:
        raise DebuggerNotSuportedError(err="No code is provided in this job!")
    if language not in SUPPORTED_DEBUGGER:
        raise DebuggerNotSuportedError(err="Job programming language is not supported now!")

    envs = {"MLFLOW_TRACKING_URI":"http://host.docker.internal:5000/"} if meta.debug_dir_in_container else None
    if meta.environment_variables:
        envs = meta.environment_variables.update(envs) if envs else meta.environment_variables

    # if run in container, use debug_dir_in_container first, otherwise use debug_dir_on_host
    debug_dir = meta.debug_dir_in_container if meta.debug_dir_in_container else meta.debug_dir_on_host
    # run in container
    if not os.path.exists(debug_dir):
        os.makedirs(debug_dir)

    #prepare debug folder (prepare devcontainer.json/Dockerfile/launch.json)
    if language == Language.PYTHON:
        debugger = PythonDebugger(meta.code_dir, meta.mounts, meta.command, meta.container_image, envs)
        debugger.prepare_debug_data(debug_dir)
    elif language == Language.R:
        debugger = RDebugger(meta.code_dir, meta.mounts, meta.command, meta.container_image, envs)
        debugger.prepare_debug_data(debug_dir)

    hex_encoded_devcontainer_path = _encode_hex(meta.debug_dir_on_host)
    return f"code --folder-uri vscode-remote://dev-container+{hex_encoded_devcontainer_path}/workspaces/{meta.app_name}"

def _encode_hex(path: str):
    vscode_path = re.sub("\\s+", "", path)
    return binascii.hexlify(vscode_path.encode()).decode("ascii")