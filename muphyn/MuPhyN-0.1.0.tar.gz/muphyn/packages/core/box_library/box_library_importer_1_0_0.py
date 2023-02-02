
#-----------------------------------
# Imports
#-----------------------------------

import importlib
import yaml
from typing import Dict

from .box_library_data import AbstractBoxData, CompositeBoxData, CodeBoxData
from .abstract_box_library_importer import AbstractBoxLibraryImporter

#-----------------------------------
# Class
#-----------------------------------

class BoxLibraryImporter_1_0_0 (AbstractBoxLibraryImporter) :
    """Est la classe V 1.0.0 d'importeur de boxes."""

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

            # Read YAML File
            file_data = yaml.load(yaml_file_data, Loader = yaml.FullLoader)

            if 'box' in file_data :
                # Get Box data                
                box_data = file_data['box']

                # Filter box based on the library name
                if box_data['library'].startswith('Boxes') :
                    # Build fill box name
                    library_name = box_data['library'] + "." + box_data['name']

                    # Si la box est déjà dans la bibliothèques 
                    if library_name in boxes :
                        # Et que sa version est plus haute.
                        if boxes[library_name].version >= box_data['version']:
                            return None
                    
                    if box_data['type'] == 'code' :
                        return {'library_name' : library_name, 'box_data' : self._import_code_box(library_name, box_data, path + '/' + file_name + '.py')}

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
        if box_data['box_init_method'] == "None" : 
            init_method = lambda box, scheduler_params : ...
        else :
            init_method = getattr(foo, box_data['box_init_method'])

        # Si la fonction n'éxiste, pas création de celle-ci
        if box_data['box_function'] == "None" : 
            box_function = lambda box, event : ...
        else :
            box_function = getattr(foo, box_data['box_function'])

        # Si la méthode end n'éxiste, pas création de celle-ci
        if box_data['box_end_method'] == "None" : 
            end_method = lambda box : ...
        else :
            end_method = getattr(foo, box_data['box_end_method'])

        if box_data['inputs'] == 'None':
            inputs = []
        else :
            inputs = box_data['inputs']

        if box_data['outputs'] == 'None':
            outputs = []
        else :
            outputs = box_data['outputs']

        if box_data['params'] == 'None' :
            params = {}
        else :
            params = box_data['params']

        if "icon" not in box_data :
            icon = None
        else:
            icon = box_data['icon']

        # Retour de la nouvelle box de code.
        return CodeBoxData(
            box_name = box_data['name'],
            box_library = box_data['library'],
            wait_for_event = box_data['wait_for_events'],
            wait_for_all_signal_events = box_data['wait_for_all_signal_events'],
            params = params,
            box_init_method_ = init_method, 
            box_function_ = box_function,
            box_end_method_ = end_method, 
            creator = box_data['creator'],
            date_created = box_data['date_creation'],
            version = box_data['version'],
            inputs = inputs,
            outputs = outputs,
            icon = icon
        )