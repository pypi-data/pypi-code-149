#-----------------------------------
# Imports
#-----------------------------------

from typing import Dict
import importlib
import yaml

from muphyn.packages.core.scheduler_library.scheduler_library_data import SchedulerData
from muphyn.packages.core.utils.log_manager import LogManager
from .abstract_scheduler_library_importer import AbstractSchedulerLibraryImporter

#-----------------------------------
# Class
#-----------------------------------

class SchedulerLibraryImporter_1_0_0 (AbstractSchedulerLibraryImporter) : 
    """Est la V 1.0.0 de classes capable d'importer des planificateurs."""

    # -------------
    # Constructors
    # -------------
    
    def __init__ (self) :
        super().__init__()

    # -------------
    # Methods
    # -------------

    def import_scheduler_data (self, path : str, file_name : str, absolute_yaml_file : str, schedulers : Dict[str, SchedulerData]) -> Dict[str, SchedulerData] :
        
        absolute_py_file = path + '/' + file_name + '.py'

        with open(absolute_yaml_file) as yaml_file_data :
            
            file_data = yaml.load(yaml_file_data, Loader = yaml.FullLoader)

            if 'scheduler' in file_data:
                
                scheduler_data = file_data['scheduler']

                if scheduler_data['library'].startswith('Schedulers') :
                    
                    library_name = scheduler_data['library'] + "." + scheduler_data['name']
                    spec = importlib.util.spec_from_file_location(library_name, absolute_py_file)
                    foo = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(foo)

                    if scheduler_data['scheduler_method'] == "None" : 
                        scheduler_method = lambda box : LogManager().error("No scheduler method")
                    else :
                        scheduler_method = getattr(foo, scheduler_data['scheduler_method'])

                    return {'library_name' : library_name, 'scheduler_data' : SchedulerData(
                        scheduler_name = scheduler_data['name'],
                        scheduler_library = scheduler_data['library'],
                        scheduler_method = scheduler_method,
                        creator = scheduler_data['creator'],
                        date_created = scheduler_data['date_creation'],
                        version = scheduler_data['version']
                    )}