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

POST_START_COMMAND_PREFIX = "cd ${containerWorkspaceFolder}/src && python -m debugpy --listen 0.0.0.0:5678 --wait-for-client"

class PythonDebugger(BaseDebugger):
    def __init__(self, code_dir: str = None, mounts:dict = None, command:str = None, image:str = None, envs:dict = None) -> None:
        self._command = command
        self._image = image
        self._envs = envs
        super().__init__(code_dir, mounts)
    
    @property
    def programming_lang(self) -> Language:
        return Language.PYTHON

    @property
    def name(self) -> str:
        return "Python 3"
    
    def get_devcontainer_settings(self) -> Settings:
        # dev container settings
        return Settings(settings={
            "terminal.integrated.shell.linux": "/bin/bash",
            "python.pythonPath": "/usr/local/bin/python",
            "python.linting.enabled": True,
            "python.linting.pylintEnabled": True,
            "python.formatting.autopep8Path": "/usr/local/py-utils/bin/autopep8",
            "python.formatting.blackPath": "/usr/local/py-utils/bin/black",
            "python.formatting.yapfPath": "/usr/local/py-utils/bin/yapf",
            "python.linting.banditPath": "/usr/local/py-utils/bin/bandit",
            "python.linting.flake8Path": "/usr/local/py-utils/bin/flake8",
            "python.linting.mypyPath": "/usr/local/py-utils/bin/mypy",
            "python.linting.pycodestylePath": "/usr/local/py-utils/bin/pycodestyle",
            "python.linting.pydocstylePath": "/usr/local/py-utils/bin/pydocstyle",
            "python.linting.pylintPath": "/usr/local/py-utils/bin/pylint"
        })
    
    def get_devcontainer_extensions(self) -> Extensions:
        return Extensions(extensions=["ms-python.python"])

    def get_devcontainer_postcreatecmd(self) -> PostCreateCommand:
        return PostCreateCommand(command="rm -rf ${containerWorkspaceFolder}/src && ln -s /src ${containerWorkspaceFolder}/src")

    def get_devcontainer_poststartcmd(self) -> PostStartCommand:
        commandprefix = "python"
        designerprefix = "mldesigner"
        if self._command.startswith(commandprefix):
            command = self._command.removeprefix(commandprefix)
            debug_command = POST_START_COMMAND_PREFIX + command
            return PostStartCommand(debug_command)
        # support new version mldesigner debug
        elif self._command.startswith(designerprefix):
            command = self._command.removeprefix(designerprefix)
            debug_command = "designer_path=`which mldesigner` && " + POST_START_COMMAND_PREFIX + " $designer_path " + command
            return PostStartCommand(debug_command)
        else:
            # user need to do some customized work if the command is not run in python
            return None

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