#-----------------------------------
# Imports
#-----------------------------------
import re
from typing import List, Dict

from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager
from muphyn.packages.core.plci_core_box import Box
from muphyn.packages.core.plci_core_diagram import Diagram
from muphyn.packages.core.plci_core_scheduler import Scheduler
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.core.plci_core_signal import Signal
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.interface.models.editable_models.scheduler_model import SchedulerModel
from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.signals_model.abstract_signal_model import AbstractSignalModel
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.core.utils.global_env_variables_manager import GlobalEnvVariablesManager
from muphyn.packages.core.utils.regexes import *
from muphyn.packages.core.plci_core_data_type import get_data_type

#-----------------------------------
# Class
#-----------------------------------

class Parser : 

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        ...
    
    # -------------
    # Methods
    # -------------      

    def parse (self, element : object, schedulers_libraries : SchedulersLibraries) -> Scheduler :
        """Est la méthode pour convertir/traduire un objet en un scheduler prêt à être simuler."""
        
        if isinstance(element, SimulationModel) :
            
            return self.__parse_simulation__(element, BoxesLibrariesManager(), schedulers_libraries)

        elif isinstance(element, str) :
            ...

        return None

    def __parse_simulation__ (self, simulation_model : SimulationModel, boxes_libraries : BoxesLibrariesManager, schedulers_libraries : SchedulersLibraries) -> Scheduler :
        """Est la méthode pour convertir/traduire une simulation en un scheduler prêt à être simuler."""

        if simulation_model.scheduler_model is None :
            return None

        else :
            if simulation_model.scheduler_model.params is None :
                return None 

            else :

                scheduler = schedulers_libraries.construct_scheduler(simulation_model.scheduler_model.library, simulation_model.scheduler_model.name)

                # Si pas de scheduler sélectionné.
                if scheduler is None : 
                    
                    scheduler_library = None 

                    # On prend le premier.
                    for lib in schedulers_libraries.schedulers :
                        if not(lib is None) :
                            scheduler_library = lib
                            break

                    if scheduler_library is None :
                        return None

                    else :
                        simulation_model.scheduler_model = SchedulerModel(scheduler_library.scheduler_library, scheduler_library.scheduler_name, simulation_model.scheduler_model.params)
                        scheduler = scheduler_library.construct_scheduler()

                scheduler.params = SchedulerParams(simulation_model.scheduler_model.params.stop_time, simulation_model.scheduler_model.params.step_time)
                scheduler.diagram = Diagram()
                
                last_signal_index = 0
                signals_dict : Dict[AbstractSignalModel, Signal] = {} 
                diagrams : List[Diagram] = []

                for box_model in simulation_model.box :

                    if isinstance(box_model, BoxModel) :

                        params = {}
                        for param in box_model.get_parameters() :
                            params[param] = box_model.get_parameter(param)['value']

                        box = boxes_libraries.construct_box(box_model.library, box_model.name, **params)
                        scheduler.diagram.append(box)

                        if isinstance(box, Box) :

                            # Handle Inputs
                            for input in box_model.inputs :

                                if len(input._links) > 0 :
                                    link = input._links[0]

                                    if link in signals_dict :
                                        scheduler.diagram.add_box_inputs(box, signals_dict[link])
                                        signals_dict[link].input_name = input.text

                                    else :
                                        signal : Signal = Signal(last_signal_index, link.data_type, link.data_type.default_value(), input_name=input.text)
                                        scheduler.diagram.append(signal)
                                        signals_dict[link] = signal
                                        scheduler.diagram.add_box_inputs(box, signal)
                                        last_signal_index += 1
                                        
                            # Handle Outputs
                            for output in box_model.outputs :
                                
                                for link in output.links : 
                                    
                                    if link in signals_dict :
                                        scheduler.diagram.add_box_outputs(box, signals_dict[link])
                                        signals_dict[link].ouput_name = output.text

                                    else :
                                        signal : Signal = Signal(last_signal_index, link.data_type, link.data_type.default_value(), output_name=output.text)
                                        scheduler.diagram.append(signal)
                                        signals_dict[link] = signal
                                        scheduler.diagram.add_box_outputs(box, signal)
                                        last_signal_index += 1

                            # Handle Parameters
                            for param in box.params:
                                # Get param value from Box
                                param_value = box.get_parameter(param)
                                if type(param_value) == str:
                                
                                    # Test if scientific notation number
                                    if re.match(DotScientificNumberRegex, param_value):
                                        # Valid Value
                                        box[param] = float(param_value)

                                    # Test if value exists as global variable
                                    elif str(param_value) in GlobalEnvVariablesManager().global_vars:
                                        # Get global variable value
                                        global_var = GlobalEnvVariablesManager().global_vars[param_value]

                                        # Get parameter type
                                        param_type = get_data_type(box_model.get_parameter(param)["type"])
                                        
                                        # Compare types
                                        if str(param_type) == "float" and str(type(global_var).__name__) in ['float', 'int']:
                                            box[param] = float(global_var)
                                        elif str(param_type) == "int" and str(type(global_var).__name__) in ['float', 'int']:
                                            box[param] = int(global_var)
                                        else:
                                            box[param] = param_type.default_value()
                                            

                        elif isinstance(box, Diagram) : 
                            diagrams.append(box)
                            

                return scheduler

                        