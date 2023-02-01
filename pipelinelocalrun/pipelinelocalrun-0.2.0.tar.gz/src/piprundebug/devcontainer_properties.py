# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
#
# This file contains devcontainer.json properties as Python classes.
# Reference: https://code.visualstudio.com/docs/remote/devcontainerjson-reference


from typing import Optional


class Image(object):
    """Python object representation of devcontainer image property."""

    def __init__(self, image: str):
        self._image = image

    def to_dict(self) -> dict:
        return {"image": self._image}


class Build(object):
    """Python object representation of devcontainer build.dockerfile property."""

    def __init__(
        self,
        dockerfile_path: str,
        build_context: Optional[str] = None,
        args: Optional[dict] = None,
        target: Optional[str] = None,
    ):
        self._dockerfile_path = dockerfile_path
        self._build_context = build_context
        self._args = args
        self._target = target

    def to_dict(self) -> dict:
        build = {
            "build": {
                "dockerfile": self._dockerfile_path,
            }
        }
        if self._build_context:
            build["build"]["context"] = self._build_context
        if self._args:
            build["build"]["args"] = self._args
        if self._target:
            build["build"]["target"] = self._target
        return build


class ContainerEnv(object):
    """Python object representation of devcontainer containerEnv property."""

    def __init__(self, environment_variables: dict):
        self._environment_variables = environment_variables

    def to_dict(self) -> dict:
        return {"containerEnv": self._environment_variables}


class Mounts(object):
    """Python object representation of devcontainer mounts property."""

    def __init__(self, mounts: list):
        self._mounts = mounts

    def to_dict(self) -> dict:
        return {"mounts": self._mounts}


class Name(object):
    """Python object representation of devcontainer name property."""

    def __init__(self, name: str):
        self._name = name

    def to_dict(self) -> dict:
        return {"name": self._name}


class ForwardPorts(object):
    """Python object representation of devcontainer name property."""

    def __init__(self, port: int):
        self._port = port

    def to_dict(self) -> dict:
        return {"forwardPorts": [self._port]}


class AppPort(object):
    """Python object representation of devcontainer name property."""

    def __init__(self, port: int):
        self._port = port

    def to_dict(self) -> dict:
        return {"appPort": [self._port]}


class RunArgs(object):
    """Python object representation of devcontainer runArgs property."""

    def __init__(self, name: str = None, labels: list = None):
        labels = labels or []
        self._run_args = labels
        if name:
            self._run_args.append(f"--name={name}")

    def to_dict(self) -> dict:
        return {"runArgs": self._run_args}


class OverrideCommand(object):
    def __init__(self, override:bool = False):
        self._override = override

    def to_dict(self) -> dict:
        return {"overrideCommand": self._override}


class Extensions(object):
    def __init__(self, extensions:list = None):
        extensions = extensions or []
        self._extensions = extensions

    def to_dict(self) -> dict:
        return {"extensions": self._extensions}


class Settings(object):
    def __init__(self, settings:dict = {}):
        self._settings = settings

    def to_dict(self) -> dict:
        return {"settings": self._settings}

class PostCreateCommand(object):
    def __init__(self, command:str = None):
        self._command = command

    def to_dict(self) -> dict:
        return {"postCreateCommand": self._command}

class PostStartCommand(object):
    def __init__(self, command:str = None):
        self._command = command

    def to_dict(self) -> dict:
        return {"postStartCommand": self._command}
