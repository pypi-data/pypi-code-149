import os
import json
import shutil
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional


from enum import Enum
from .devcontainer_properties import (
    Settings, 
    Build, 
    Image, 
    Name, 
    Extensions, 
    Mounts, 
    PostStartCommand, 
    ContainerEnv, 
    OverrideCommand, 
    AppPort, 
    RunArgs, 
    ForwardPorts, 
    PostCreateCommand
)

class Language(Enum):
    NONE = "none"
    PYTHON = "python"
    R = "R"

class BaseDebugger(ABC):
    def __init__(self, code_dir:str = None, mounts:dict = None) -> None:
        self._properties: Optional[dict] = {}
        self._code_dir = code_dir
        self._mounts = self._reformat_mounts(mounts) if mounts else mounts
        # add code dir mount
        self._mounts.append(f"source={code_dir},target=/src,type=bind")

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def programming_lang(self) -> Language:
        pass

    @abstractmethod
    def get_devcontainer_settings(self) -> Settings:
        # dev container settings
        pass
    
    @abstractmethod
    def get_devcontainer_extensions(self) -> Extensions:
        pass

    def get_devcontainer_mounts(self) -> Mounts:
        return Mounts(self._mounts)

    @abstractmethod
    def get_devcontainer_postcreatecmd(self) -> PostCreateCommand:
        pass

    @abstractmethod
    def get_devcontainer_poststartcmd(self) -> PostStartCommand:
        pass

    @abstractmethod
    def get_devcontainer_envs(self) -> ContainerEnv:
        pass

    @abstractmethod
    def get_devcontainer_build(self) -> Build:
        pass

    @abstractmethod
    def get_devcontainer_overridecommand(self) -> OverrideCommand:
        pass

    @abstractmethod
    def get_devcontainer_runargs(self) -> RunArgs:
        pass

    @abstractmethod
    def get_devcontainer_image(self) -> Image:
        pass

    @abstractmethod
    def get_devcontainer_appport(self) -> AppPort:
        pass

    @abstractmethod
    def get_devcontainer_forwardports(self) -> ForwardPorts:
        pass

    def _reformat_mounts(self, mounts: dict) -> list:
        """Reformat mounts from Docker format to DevContainer format.

        :param mounts: Dictionary with mount information for Docker container. For example,
            {
                "<local_source>": {
                    "<mount type i.e. bind>": "<container_dest>"
                }
            }
        :type mounts: dict
        :returns dict: "mounts": ["source=${localWorkspaceFolder}/app-scripts,target=/usr/local/share/app-scripts,type=bind,consistency=cached"]
        """
        devcontainer_mounts = []
        for source, dest in mounts.items():
            for mount_type, container_dest in dest.items():
                devcontainer_mounts.append(f"source={source},target={container_dest},type={mount_type}")
        return devcontainer_mounts

    def _build_devcontainer_properties(self) -> Optional[dict]:
        self._properties = Name(self.name).to_dict()
        
        image = self.get_devcontainer_image()
        build = self.get_devcontainer_build()
        if image:
            self._properties.update(image.to_dict())
        elif build:
            self._properties.update(build.to_dict())
        else:
            msg = "Must provide image or build context for devcontainer.json"
            raise Exception(err=msg)
        
        settings = self.get_devcontainer_settings()
        if settings:
            self._properties.update(settings.to_dict())
        
        extensions = self.get_devcontainer_extensions()
        if extensions:
            self._properties.update(extensions.to_dict())
        
        mounts = self.get_devcontainer_mounts()
        if mounts:
            self._properties.update(mounts.to_dict())

        envs = self.get_devcontainer_envs()
        if envs:
            self._properties.update(envs.to_dict())

        overridecmd = self.get_devcontainer_overridecommand()
        if overridecmd:
            self._properties.update(overridecmd.to_dict())

        appport = self.get_devcontainer_appport()
        if appport:
            self._properties.update(appport.to_dict())

        forwardports = self.get_devcontainer_forwardports()
        if forwardports:
            self._properties.update(forwardports.to_dict())

        postcreatecmd = self.get_devcontainer_postcreatecmd()
        if postcreatecmd:
            self._properties.update(postcreatecmd.to_dict())

        poststartcmd = self.get_devcontainer_poststartcmd()
        if poststartcmd:
            self._properties.update(poststartcmd.to_dict())

        runargs = self.get_devcontainer_runargs()
        if runargs:
            self._properties.update(runargs.to_dict())

    def prepare_devcontainer_config(self, debug_dir:str):
        self._build_devcontainer_properties()
        devcontainer_config_path = str(Path(debug_dir, ".devcontainer", "devcontainer.json").resolve())
        # delete if old on exist
        if os.path.exists(devcontainer_config_path):
            os.remove(devcontainer_config_path)
        with open(devcontainer_config_path, "w") as f:
            f.write(f"{json.dumps(self._properties, indent=4)}\n")

    def prepare_devcontainer_dockerfile(self, debug_dir:str):
        src_dockerfile_path = str(Path(Path(__file__).parent, "language", self.programming_lang.value, "Dockerfile").resolve())
        dest_dockerfile_path = str(Path(debug_dir, ".devcontainer", "Dockerfile").resolve())
        # delete dest if exist
        if os.path.exists(dest_dockerfile_path):
            os.remove(dest_dockerfile_path)
        shutil.copyfile(src_dockerfile_path, dest_dockerfile_path)

    def prepare_debug_launch_config(self, debug_dir:str):
        """prepare vscode debug launch.json file (if needed), by default this just copy the predefined launch.json file, each language debugger
        can customize this with their own implementation.

        :param debug_dir: local debug root dir which will be loaded in the devcontainer
        """
        src_launchfile_path = str(Path(Path(__file__).parent, "language", self.programming_lang.value, "launch.json").resolve())
        dest_launchfile_path = str(Path(debug_dir, ".vscode", "launch.json").resolve())
        # delete old launch.json if exist
        if os.path.exists(dest_launchfile_path):
            os.remove(dest_launchfile_path)
        shutil.copyfile(src_launchfile_path, dest_launchfile_path)

    def prepare_debug_data(self, debug_dir:str):
        # debug_dir should be the path in container here, while calculating the devcontainer invoke command we should use the real path on the node.
        # source code mount from host and copied to debug_dir
        devcontainer_path = Path(debug_dir, ".devcontainer")
        vscode_path = Path(debug_dir, ".vscode")
        devcontainer_path.mkdir(parents=True, exist_ok=True)
        vscode_path.mkdir(parents=True, exist_ok=True)
        self.prepare_devcontainer_config(debug_dir)
        self.prepare_devcontainer_dockerfile(debug_dir)
        self.prepare_debug_launch_config(debug_dir)
        


        
