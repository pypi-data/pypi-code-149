import os

class DebugMetadata(object):
    def __init__(self, 
        code_dir: str = None, 
        mounts:dict = None, 
        command:str = None, 
        image:str = None, 
        environment_variables:dict = None,
        debug_dir_in_container:str = None,
        debug_dir_on_host:str = None
    ) -> None:
        self.code_dir = code_dir
        self.mounts = mounts
        self.command = command
        self.container_image = image
        self.environment_variables = environment_variables
        self.debug_dir_in_container = debug_dir_in_container
        self.debug_dir_on_host = debug_dir_on_host
        debug_dir = debug_dir_in_container if debug_dir_in_container else debug_dir_on_host
        self.app_name = os.path.basename(debug_dir)