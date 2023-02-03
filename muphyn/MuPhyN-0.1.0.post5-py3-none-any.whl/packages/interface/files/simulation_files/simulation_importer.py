#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import copy
from typing import Dict

# PyQt5 Imports
from PyQt5.QtCore import QSizeF, QPointF

# Project Imports
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager
from muphyn.packages.core.plci_core_data_type import get_data_type
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.interface.files.abstract_importer import AbstractImporter
from muphyn.packages.interface.models.editable_models.scheduler_model import SchedulerModel
from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.links_model.link_type import get_link_type
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel

#-----------------------------------
# Functions
#-----------------------------------

def construct_box (box_dict : Dict) -> BoxModel :
    """Est la méthode appelée pour produire un modèle de box suivant un dictionnaire d'import."""

    # Get genral box informations
    library = box_dict['library']
    name = box_dict['name']

    #
    text = box_dict['text']

    # Get geometry
    position = QPointF(float(box_dict['geometry']['x']), float(box_dict['geometry']['y']))
    size = QSizeF(float(box_dict['geometry']['width']), float(box_dict['geometry']['height']))
    rotation = float(box_dict['geometry']['rotation'])

    # Build Box from BoxData
    box_data = BoxesLibrariesManager().get_box_data(library, name)
    
    # Handle Geometry value
    ## Size
    if size.width() < AbstractBoxModel.MinimunBoxWidth:
        size.setWidth(AbstractBoxModel.MinimunBoxWidth)
    if size.height() < AbstractBoxModel.MinimunBoxHeight:
        size.setHeight(AbstractBoxModel.MinimunBoxHeight)
    
    ## Rotation
    rotation = ((rotation // 90) % 4) * 90

    # Build Box Model
    box_model = BoxModel(
        library=box_data.box_library,
        name=box_data.box_name,
        position=position,
        size=size,
        rotation=rotation, can_be_loaded=True, text=text, icon=box_data.icon
    )
    
    # Add default params value
    if hasattr(box_data, 'params') :
        for parameter, attributes in box_data.params.items() :
            # Copy parameter
            box_model._parameters[parameter] = copy.deepcopy(attributes)

    return box_model


def construct_input (input_dict : Dict, current_input_index : int, box_model : BoxModel) -> InputConnectionModel :
    """Est la méthode appelée pour produire un modèle d'entrée d'une box suivant un dictionnaire d'import."""

    input_name = input_dict['name']
    input_type = get_data_type(input_dict['data_type'])
    input_text = input_dict['text']
    input_is_infinite = input_dict['isInfinite']

    return box_model.insert_input(current_input_index, input_name)

    return box_model.insert_input(current_input_index, input_name, input_type, input_text, input_is_infinite)

def construct_output (output_dict : Dict, current_output_index : int, box_model : BoxModel) -> OutputConnectionModel : 
    """Est la méthode appelée pour produire un modèle de sortie d'une box suivant un dictionnaire d'import."""

    output_name = output_dict['name']
    output_type = get_data_type(output_dict['data_type'])
    output_text = output_dict['text']
    output_is_infinite = output_dict['isInfinite']

    return box_model.insert_output(current_output_index, output_name)
    # return box_model.insert_output(current_output_index, output_name, output_type, output_text, output_is_infinite)

#-----------------------------------
# Class
#-----------------------------------

class SimulationsImporter (AbstractImporter) :
    """Est la classe qui permet d'importer une simulation."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        
        AbstractImporter.__init__(self)

    # -------------
    # Methods
    # -------------

    def open (self, simulation_data : Dict, path : str, name : str) -> SimulationModel :
    
        if simulation_data['export_version'] == '1.0.0' :
            return self.v_1_0_0(simulation_data, path, name)
        elif simulation_data['export_version'] == '1.1.0' :
            return self.v_1_1_0(simulation_data, path, name)

        return None

    def v_1_0_0 (self, simulation_data : Dict, path : str, name : str) -> SimulationModel : 
        
        # General Project informations
        date_creation = simulation_data['date_creation']
        version = float(simulation_data['version'])
        creator = simulation_data['creator']

        # Simulation informations
        stop_time = float(simulation_data['stop_time'])
        step_time = float(simulation_data['step_time'])
        scheduler_library = simulation_data['scheduler']['library']
        scheduler_name = simulation_data['scheduler']['name']

        # Build Scehduler & Simulation Models
        scheduler_params = SchedulerParams(stop_time, step_time)
        scheduler_model = SchedulerModel(scheduler_library, scheduler_name, scheduler_params)
        simulation_model = SimulationModel(name, path, creator, date_creation, version, scheduler_model)

        # Get list of all boxes & signals
        boxes = simulation_data['diagram']['boxes']
        signals = simulation_data['diagram']['signals']

        #Ajout de input et ouput au dictionnaire importé dans le but de connecter correctement les noeuds.
        #Plus rapide que de copier l'éxistant et d'ajotuer les "input" et "output". 
        
        for signal in signals : 
            signal['input'] = None
            signal['output'] = None

        for box_data in boxes :

            box_model = construct_box(box_data)
            
            current_input_index = 0
            for input_data in box_data['inputs'] : 

                input = construct_input(input_data, current_input_index, box_model)
                
                input_signal_index = int(input_data['signal_index'])
                if input_signal_index < len(signals) and input_signal_index >= 0 : 

                    signal_data = signals[input_signal_index]
                    if signal_data['input'] is None : 
                        signal_data['input'] = input
                        if not(signal_data['output'] is None) : 
                            simulation_model.link_nodes(input, signal_data['output'], -1, -1,
                                float(signal_data['link_value']), get_link_type(signal_data['link_type']), '')

                current_input_index += 1

            current_output_index = 0
            for output_data in box_data['outputs'] :

                output = construct_output(output_data, current_output_index, box_model)
                
                for output_signal_index in output_data['signal_indices'] : 
                    if output_signal_index < len(signals) and output_signal_index >= 0 : 
                        
                        signal_data = signals[output_signal_index]
                        if signal_data['output'] is None : 
                            signal_data['output'] = output
                            if not(signal_data['input'] is None) : 
                                simulation_model.link_nodes(signal_data['input'], output, -1, -1,
                                    float(signal_data['link_value']), get_link_type(signal_data['link_type']), '')
                
                current_output_index += 1


            # Set parameters
            for parameter_data in box_data['params'] :
                box_model.set_parameter(parameter_data, box_data['params'][parameter_data]['value'])

            # Append Box Model
            simulation_model.add_element(box_model)

        return simulation_model

    def v_1_1_0 (self, simulation_data : Dict, path : str, name : str) -> SimulationModel : 
        
        # General Project informations
        date_creation = simulation_data['date_creation']
        version = float(simulation_data['version'])
        creator = simulation_data['creator']

        # Simulation informations
        stop_time = float(simulation_data['stop_time'])
        step_time = float(simulation_data['step_time'])
        scheduler_library = simulation_data['scheduler']['library']
        scheduler_name = simulation_data['scheduler']['name']

        # Build Scehduler & Simulation Models
        scheduler_params = SchedulerParams(stop_time, step_time)
        scheduler_model = SchedulerModel(scheduler_library, scheduler_name, scheduler_params)
        simulation_model = SimulationModel(name, path, creator, date_creation, version, scheduler_model)

        # Get list of all boxes & signals
        boxes = simulation_data['diagram']['boxes']
        signals = simulation_data['diagram']['signals']

        #Ajout de input et ouput au dictionnaire importé dans le but de connecter correctement les noeuds.
        #Plus rapide que de copier l'éxistant et d'ajotuer les "input" et "output". 
        
        for signal in signals : 
            signal['input'] = None
            signal['output'] = None

        for box_dict in boxes :

            # Get default box data from dict informations
            box_model = BoxModel.fromDict(box_dict)

            # Build infinite inputs groups
            for inputs_group in box_dict["inputs_groups"]:

                # Get group data
                is_infinite = inputs_group["isInfinite"]
                inputs_group_name = inputs_group["name"]

                if is_infinite:
                    # Add inputs
                    for input_data in inputs_group['inputs'] : 
                        # Input data
                        input_signal_index = int(input_data["signal_index"])
                        input_text = input_data["text"]

                        # Append input to box model
                        input_ = box_model.append_input(inputs_group_name)

                        # Set input parameter
                        input_.text = input_text

                        if input_signal_index < len(signals) and input_signal_index >= 0 : 
                            # Get signal data
                            signal_data = signals[input_signal_index]

                            # Add input to signal data
                            if signal_data['input'] is None : 
                                signal_data['input'] = input_

                else:
                    # Set inputs
                    for input_index, input_data in enumerate(inputs_group['inputs']): 
                        # Input data
                        input_signal_index = int(input_data["signal_index"])
                        input_text = input_data["text"]

                        # Get input from box model
                        input_ = box_model.inputs_groups[inputs_group_name].inputs[input_index]

                        # Set input parameter
                        input_.text = input_text

                        if input_signal_index < len(signals) and input_signal_index >= 0 : 
                            # Get signal data
                            signal_data = signals[input_signal_index]

                            # Add input to signal data
                            if signal_data['input'] is None : 
                                signal_data['input'] = input_

            
            # Build infinite outputs groups
            for outputs_group in box_dict["outputs_groups"]:

                # Get group data
                is_infinite = outputs_group["isInfinite"]
                outputs_group_name = outputs_group["name"]

                if is_infinite:
                    # Add outputs
                    for output_data in outputs_group['outputs'] : 
                        # Input data
                        output_signal_indices = output_data["signal_indices"]
                        output_text = output_data["text"]

                        # Append output to box model
                        output_ = box_model.append_output(outputs_group_name)

                        # Set output parameter
                        output_.text = output_text

                        for output_signal_index in output_signal_indices:

                            if output_signal_index < len(signals) and output_signal_index >= 0 : 
                                # Get signal data
                                signal_data = signals[output_signal_index]

                                # Add output to signal data
                                if signal_data['output'] is None : 
                                    signal_data['output'] = output_

                else:
                    # Set outputs
                    for output_index, output_data in enumerate(outputs_group['outputs']): 
                        # Input data
                        output_signal_indices = output_data["signal_indices"]
                        output_text = output_data["text"]

                        # Get output from box model
                        output_ = box_model.outputs_groups[outputs_group_name].outputs[output_index]

                        # Set output parameter
                        output_.text = output_text

                        for output_signal_index in output_signal_indices:
                            if output_signal_index >= 0 : 
                                # Get signal data
                                signal_data = signals[output_signal_index]

                                # Add output to signal data
                                if signal_data['output'] is None :
                                    signal_data['output'] = output_

            # Set parameters
            for parameter_data in box_dict['params'] :
                box_model.set_parameter(parameter_data, box_dict['params'][parameter_data])

            # Append Box Model
            simulation_model.add_element(box_model)

            
        # Signals
        for signal_data in signals:
            # Get signal data
            input_ = signal_data["input"]
            output = signal_data["output"]
            
            # Create link
            if input_ is not None and output is not None:
                simulation_model.link_nodes(input_, output, -1, -1,
                    float(signal_data['link_value']), get_link_type(signal_data['link_type']), '')

        return simulation_model