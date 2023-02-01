import os
import json
import shutil
from pathlib import Path
import jsonpatch
from .base_debugger import BaseDebugger, Language
from .devcontainer_properties import (
    Settings, 
    Build, 
    Image, 
    Extensions, 
    PostStartCommand, 
    ContainerEnv, 
    OverrideCommand, 
    AppPort, 
    RunArgs, 
    ForwardPorts, 
    PostCreateCommand
)

class RDebugger(BaseDebugger):
    def __init__(self, code_dir: str = None, mounts:dict = None, command:str = None, image:str = None, envs:dict = None) -> None:
        self._command = command
        self._image = image
        self._envs = envs
        super().__init__(code_dir, mounts)

    @property
    def name(self) -> str:
        return "R (Community)"

    @property
    def programming_lang(self) -> Language:
        return Language.R

    def get_devcontainer_settings(self) -> Settings:
        # dev container settings
        # "r.plot.useHttpgd": true,
        # "r.rpath.linux": "",
        return Settings(settings={
            "r.rterm.linux": "/usr/local/bin/radian",
            "r.bracketedPaste": True,
            "[r]": {
                "editor.wordSeparators": "`~!@#%$^&*()-=+[{]}\\|;:'\",<>/?"
            }
        })
    
    def get_devcontainer_extensions(self) -> Extensions:
        return Extensions(extensions=["reditorsupport.r","rdebugger.r-debugger"])

    def get_devcontainer_postcreatecmd(self) -> PostCreateCommand:
        return None

    def get_devcontainer_poststartcmd(self) -> PostStartCommand:
        return PostStartCommand("R")

    def get_devcontainer_envs(self) -> ContainerEnv:
        return ContainerEnv(environment_variables=self._envs) if self._envs else None

    def get_devcontainer_build(self) -> Build:
        return Build(dockerfile_path="Dockerfile",args={"BASE_IMAGE": self._image})

    def get_devcontainer_overridecommand(self) -> OverrideCommand:
        return None

    def get_devcontainer_runargs(self) -> RunArgs:
        return None

    def get_devcontainer_image(self) -> Image:
        return None

    def get_devcontainer_appport(self) -> AppPort:
        return None

    def get_devcontainer_forwardports(self) -> ForwardPorts:
        return None

    def prepare_debug_launch_config(self, debug_dir:str):
        src_launchfile_path = str(Path(Path(__file__).parent, "language", self.programming_lang.value, "launch.json").resolve())
        dest_launchfile_path = str(Path(debug_dir, ".vscode", "launch.json").resolve())
        # delete old launch.json if exist
        if os.path.exists(dest_launchfile_path):
            os.remove(dest_launchfile_path)

        # patch(or replace???) the launch debug mode if the start command is known pattern
        if self._command.startswith("Rscript"):
            launch_mode_config = {
                "type": "R-Debugger",
                "name": "Azure ML: R launch Debug",
                "request": "launch",
                "debugMode": "file",
                "workingDirectory": "${workspaceFolder}", 
            }
            # generate start file path
            command_array = self._command.split(" ")
            cleaned_command_array=[x for x in command_array if x]
            start_file = cleaned_command_array[1]
            launch_mode_config.update({"file": "${workspaceFolder}/src/"+start_file})
            # generate launch commandLineArgs if has extra parameters
            if len(cleaned_command_array) > 2:
                args = ["--args"]
                for x in cleaned_command_array[2:]:
                    args.append(x)
                launch_mode_config.update({"commandLineArgs":args})

            with open(src_launchfile_path) as f:
                data = json.load(f)
            patch = jsonpatch.JsonPatch([ {'op': 'replace', 'path': '/configurations/0', 'value': launch_mode_config}])
            updated_data = patch.apply(data)
            with open(dest_launchfile_path, "w") as f:
                f.write(f"{json.dumps(updated_data, indent=4)}\n")
        else:
            shutil.copyfile(src_launchfile_path, dest_launchfile_path)
            
