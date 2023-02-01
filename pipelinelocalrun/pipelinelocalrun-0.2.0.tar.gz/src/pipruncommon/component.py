from typing import Dict
from .input_output import GeneralInput, GeneralOutput

class ComponentType:
    COMMAND = "CommandComponent"

class BaseComponent(object):
    def __init__(self,
        component_id:str,
        component_type:str = ComponentType.COMMAND,
        description:str = None,
        name: str = None,
        display_name :str = None,
        version:str = None,
        tags: dict = None,
        inputs :Dict[str, GeneralInput] = None,
        outputs :Dict[str, GeneralOutput] = None,
        is_deterministic: bool = False,
        raw_content: str = None,
        **kwargs
        ):
        self.component_id = component_id
        self.component_type = component_type
        self.description = description
        self.name = name
        self.display_name = display_name
        self.version = version
        self.tags = tags
        self.inputs = inputs
        self.outputs = outputs
        self.is_deterministic = is_deterministic
        self.raw_content = raw_content    

class CommandComponent(BaseComponent):
    def __init__(self,
        component_id:str,
        component_type:str = ComponentType.COMMAND,
        description:str = None,
        name: str = None,
        display_name :str = None,
        version:str = None,
        tags: dict = None,
        properties: dict = None,
        inputs :Dict[str, GeneralInput] = None,
        outputs :Dict[str, GeneralOutput] = None,
        is_deterministic: bool = False,
        command: str = None,
        code: str = None,
        distribution: str = None,
        resources: str = None,
        raw_content: str = None,
        **kwargs
        ):
        super().__init__(component_id, component_type, description, name, display_name, version, tags, inputs, outputs, is_deterministic, raw_content)
        self.command = command
        self.properties = properties
        self.code = code
        self.distribution = distribution
        self.resources = resources