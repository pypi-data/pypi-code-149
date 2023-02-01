from __future__ import annotations
from typing import Union
from enum import Enum

# define input type for job/components
class InputType:
    # asset type
    URI_FILE = "uri_file"
    URI_FOLDER = "uri_folder"
    MLTABLE = "mltable"
    MLFLOW_MODEL = "mlflow_model"
    CUSTOM_MODEL = "custom_model"
    TRITON_MODEL = "triton_model"
    # parameter type
    INTEGER = "integer"
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"

# define output type for job/components
class OutputType:
    URI_FILE = "uri_file"
    URI_FOLDER = "uri_folder"
    MLTABLE = "mltable"
    MLFLOW_MODEL = "mlflow_model"
    CUSTOM_MODEL = "custom_model"
    TRITON_MODEL = "triton_model"

# define mode for job/component input/output
class InputOutputModes:
    MOUNT = "mount"
    DOWNLOAD = "download"
    UPLOAD = "upload"
    RO_MOUNT = "ro_mount"
    RW_MOUNT = "rw_mount"
    EVAL_MOUNT = "eval_mount"
    EVAL_DOWNLOAD = "eval_download"
    DIRECT = "direct"

# component input
class GeneralInput(object):
    ALLOWED_PARAMETER_TYPES = {
        "integer": (int),
        "string": (str),
        "number": (float),
        "boolean": (bool),
    }

    def __init__(self, *, name: str, type: str = InputType.URI_FILE,
        path: str = None,
        default: Union[str, int, float, bool] = None,
        min: Union[int, float] = None,
        max: Union[int, float] = None,
        description: str = None,
        optional: bool = None,
        mode: str = None,
        **kwargs):
        self.name = name
        self.type = type
        self.path = path
        self.default = default
        self.min = min
        self.max = max
        self.description = description
        self.optional = optional
        self.mode = mode

    def is_parameter_type(self) -> bool:
        return self.type in self.ALLOWED_PARAMETER_TYPES

# component output
class GeneralOutput(object):
     def __init__(self, *, name: str, type: str = OutputType.URI_FOLDER,
        path: str = None,
        description: str = None,
        mode: str = None,
        **kwargs):
        self.name = name
        self.type = type
        self.path = path
        self.description = description
        self.mode = mode

class RunInputOutputBase(object):
    def __init__(self, name:str = None, type:str = None, uri: str = None, mode:str = None, value:str = None, pipelineReference: str = None):
        self.name = name
        self.type = type
        self.uri = uri
        self.mode = mode
        self.value = value
        self.pipelineReference = pipelineReference