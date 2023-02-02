
#-----------------------------------
# Imports
#-----------------------------------
import numpy as np
import importlib
import yaml
from typing import Dict

from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.core.plci_core_data_type import DataType, get_data_type
from muphyn.packages.core.box_library.box_library_data import AbstractBoxData, CompositeBoxData, CodeBoxData, MultiPhysicsSimulationBoxData
from muphyn.packages.core.box_library.abstract_box_library_importer import AbstractBoxLibraryImporter

#-----------------------------------
# Class
#-----------------------------------

class BoxLibraryImporter_1_1_0 (AbstractBoxLibraryImporter) :
    """
    Est la classe V 1.1.0 d'importeur de boxes.

    What's new ?
    ------------
     - Importer is now able to link parameter value changed event to external functions
    """
    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        super().__init__()
        
    # -------------
    # Methods
    # -------------

    def import_box (self, path : str, file_name : str, absolute_yaml_file : str, boxes : Dict[str, AbstractBoxData]) -> Dict[str, AbstractBoxData] :
        """Est la méthode pour charger des boxes depuis des fichiers."""
        
        # Open File
        with open(absolute_yaml_file) as yaml_file_data :

            # Open YAML File
            file_data = yaml.load(yaml_file_data, Loader = yaml.FullLoader)

            if 'box' in file_data :
                # Extract Box data
                box_data = file_data['box']

                # Filter Box based library name
                if box_data['library'].startswith('Boxes') :
                    
                    # Build full box name
                    library_name = box_data['library'] + "." + box_data['name']

                    # If box already exists
                    if library_name in boxes :
                        # If existing box has a more recent version → Abort import current box
                        if boxes[library_name].version >= box_data['version']:
                            return None
                    
                    if box_data['type'] in ['code', 'multiphysics-simulation'] :
                        return {'library_name' : library_name, 'box_data' : self._import_code_box(library_name, box_data, path + '/' + file_name + '.py')}

                    if box_data['type'] == 'multiphysics-simulation' :
                        return {'library_name' : library_name, 'box_data' : self._import_multiphysics_simulation_box(library_name, box_data, path + '/' + file_name + '.py')}

                    elif box_data['type'] == 'composite' :
                        return {'library_name' : library_name, 'box_data' : self._import_composite_box(library_name, box_data)}
                    
                elif box_data['library'].startswith('Electrical'):
                    
                    library_name = box_data['library'] + "." + box_data['name']


    def _import_composite_box (self, library_name, box_data) -> CompositeBoxData :
        """Permet de générer un instanciateur de box composite."""

        if box_data['inputs'] == 'None':
            inputs = []
        else :
            inputs = box_data['inputs']

        if box_data['outputs'] == 'None':
            outputs = []
        else :
            outputs = box_data['outputs']

        return CompositeBoxData (
            box_data['name'],
            box_data['library'],
            box_data['creator'],
            box_data['date_creation'],
            box_data['version'],
            box_data['signals'],
            box_data['boxes'],
            inputs,
            outputs,
        )   

    def _import_code_box (self, library_name, box_data, absolute_py_file) -> CodeBoxData :
        """Permet de générer un instanciateur de box de code."""

        # Importations des méthodes du fichier python.
        spec = importlib.util.spec_from_file_location(library_name, absolute_py_file)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)

        # Si la méthode init n'éxiste, pas création de celle-ci.
        if "box_init_method" in box_data and box_data['box_init_method'] != "None" : 
            init_method = getattr(foo, box_data['box_init_method'])
        else :
            init_method = lambda box, scheduler : ...

        # Si la fonction n'éxiste, pas création de celle-ci
        if "box_function" in box_data and box_data['box_function'] != "None" : 
            box_function = getattr(foo, box_data['box_function'])
        else :
            box_function = lambda box, event : ...

        # Si la méthode end n'éxiste, pas création de celle-ci
        if "box_end_method" in box_data and box_data['box_end_method'] != "None" : 
            end_method = getattr(foo, box_data['box_end_method'])
        else :
            end_method = lambda box : ...

        inputs_groups = {}
        if "inputs" in box_data and box_data['inputs'] != 'None' :
            inputs = box_data['inputs']
            for input_index, input_group in enumerate(inputs):
                # Get input name
                input_group_name = f"Unnamed:{input_index}" if "name" not in input_group else input_group["name"]

                # Build input group
                if input_group_name not in inputs_groups:
                    # handling input values
                    inputs_groups[input_group_name] = BoxLibraryImporter_1_1_0.build_io_group(input_group)
                else:
                    LogManager().error(f"Duplicate input name detected for box {library_name} : {input_group_name}")
        else :
            inputs = {}

        outputs_groups = {}
        if "outputs" in box_data and box_data['outputs'] != 'None' :
            outputs = box_data['outputs']
            for output_index, output_group in enumerate(outputs):
                # Get output name
                output_group_name = f"Unnamed:{output_index}" if "name" not in output_group else output_group["name"]

                # Build output group
                if output_group_name not in outputs_groups:
                    # handling output values
                    outputs_groups[output_group_name] = BoxLibraryImporter_1_1_0.build_io_group(output_group)
                else:
                    LogManager().error(f"Duplicate output name detected for box {library_name} : {output_group_name}")
        else :
            outputs = {}

        if "params" in box_data and box_data['params'] != 'None' :
            params = box_data['params']

            # Handle params
            for param_name, param_description in params.items():

                if "type" in param_description:
                    # Handle Choice type
                    if param_description["type"] == "choice":
                        # Handle default index set
                        if "value" in param_description and "choices" in param_description:
                            index = param_description["value"]
                            choices = param_description["choices"]
                            if type(index) == int and index >= -1 and index < len(param_description["choices"]):
                                if type(choices) == list:
                                    param_description["value"] = choices[index]
                                elif type(choices) == dict:
                                    key = list(choices.keys())[index]
                                    param_description["value"] = choices[key]
                                else:
                                    param_description["value"] = None
                            else:
                                param_description["value"] = None

                        else:
                            param_description["value"] = None
                else:
                    LogManager().error(f"{library_name}: No Data type set for {param_name}")

        else :
            params = {}

        # Callbacks
        for param, attributes in params.items():
            if "on_value_changed" in attributes:
                on_value_changed_function_name = attributes["on_value_changed"]
                if hasattr(foo, on_value_changed_function_name):
                    attributes["callback"] = getattr(foo, on_value_changed_function_name)
                else:
                    LogManager().error(f"Function name doesn't exist for param {param}.on_value_changed: {on_value_changed_function_name}")


        if "icon" not in box_data :
            icon = None
        else:
            icon = box_data['icon']

        # Retour de la nouvelle box de code.
        return CodeBoxData(
            box_name = box_data['name'],
            box_library = box_data['library'],
            box_type = box_data["type"],
            wait_for_event = box_data['wait_for_events'],
            wait_for_all_signal_events = box_data['wait_for_all_signal_events'],
            params = params,
            box_init_method_ = init_method, 
            box_function_ = box_function,
            box_end_method_ = end_method, 
            creator = box_data['creator'],
            date_created = box_data['date_creation'],
            version = box_data['version'],
            inputs = inputs_groups,
            outputs = outputs_groups,
            icon = icon
        )

    def _import_multiphysics_simulation_box(self, library_name, box_data, absolute_py_file) -> MultiPhysicsSimulationBoxData:
        code_box_data: CodeBoxData = self._import_code_box(library_name, box_data, absolute_py_file)

        return MultiPhysicsSimulationBoxData.fromCodeBoxData(code_box_data)

    @staticmethod
    def build_io_group(io_group: dict) -> dict:
        # Type 
        io_group_type = DataType.UNDIFINED if "type" not in io_group else get_data_type(io_group["type"])

        # Is Infinite
        io_group_is_infinite = False if "isInfinite" not in io_group else io_group["isInfinite"]
        if type(io_group_is_infinite) != bool:
            LogManager().error(f"Wrong 'isInfinite' value: '{io_group_is_infinite}' instead of 'True' or 'False'\nThis value has been set to 'False'")
            io_group_is_infinite = False

        # Minimum count
        io_group_minimum_count = 0 if "minimumCount" not in io_group else io_group["minimumCount"]
        if io_group_minimum_count < 0:
            LogManager().error(f"Wrong 'minimumCount' value: '{io_group_minimum_count}' is negative.\nThis value has been set to '0'")
            io_group_minimum_count = 0

        # Maximum count
        int32_info = np.iinfo(np.int32)
        io_group_maximum_count = int32_info.max if "maximumCount" not in io_group else io_group["maximumCount"]
        if io_group_maximum_count < io_group_minimum_count:
            LogManager().error(f"Wrong 'maximumCount' value: '{io_group_maximum_count}' is lower than 'minimumCount' value '{io_group_minimum_count}'.\nThis value has been set to '{io_group_minimum_count+1}'")
            io_group_maximum_count = io_group_minimum_count + 1

        # Count
        io_group_count = None if "count" not in io_group else io_group["count"]
        # If no value has been set
        if io_group_count is None:
            # If io group is 'Infinite' → 2 else if io group is 'Finite' → 0 
            io_group_count = 2 if io_group_is_infinite else 0

        return {
            "type": io_group_type,
            "isInfinite": io_group_is_infinite,
            "minimumCount": io_group_minimum_count,
            "maximumCount": io_group_maximum_count,
            "count": io_group_count
        }