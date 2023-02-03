#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import yaml
from datetime import date
from typing import Dict

# Project Imports
from muphyn.packages.interface.files.abstract_exporter import AbstractExporter
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from muphyn.packages.interface.models.signals_model.abstract_signal_model import AbstractSignalModel
from muphyn.packages.interface.models.links_model.abstract_link_model import AbstractLinkModel
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel

def export_box (box : BoxModel) -> Dict :
    """Est la méthode appelée pour créer un dictionnaire contenant les données d'une box."""

    box_dict = {}

    box_dict['name'] = box.name
    box_dict['library'] = box.library
    box_dict['text'] = box.text

    box_dict['geometry'] = {}
    box_dict['geometry']['x'] = box.x()
    box_dict['geometry']['y'] = box.y()
    box_dict['geometry']['width'] = box.size.width()
    box_dict['geometry']['height'] = box.size.height()
    box_dict['geometry']['rotation'] = box.rotation()

    params = {}
    for param in box.get_parameters() :
        current_params = {}
        current_params['type'] = box.get_parameter(param)['type'].__str__()
        current_params['value'] = box.get_parameter(param)['value']

        params[param] = current_params

    box_dict['params'] = params

    return box_dict

def export_input (input : InputConnectionModel) -> Dict :
    """Est la méthode appelée pour créer un dictionnaire contenant les données d'une entrée de box."""

    input_dict = {}

    input_dict['name'] = input.name
    input_dict['isInfinite'] = input.is_infinite
    input_dict['data_type'] = input.data_type.__str__()
    input_dict['text'] = input.text

    # input_dict['color'] = {}
    # input_dict['color']['red'] = input.color.red
    # input_dict['color']['green'] = input.color.green
    # input_dict['color']['blue'] = input.color.blue

    input_dict['signal_index'] = -1

    return input_dict

def export_output (output : OutputConnectionModel) -> Dict : 
    """Est la méthode appelée pour créer un dictionnaire contenant les données d'une sortie de box."""

    output_dict = {}

    output_dict['name'] = output.name
    output_dict['isInfinite'] = output.is_infinite
    # output_dict['count'] = output
    output_dict['data_type'] = output.data_type.__str__()
    output_dict['text'] = output.text

    # output_dict['color'] = {}
    # output_dict['color']['red'] = output.color.red
    # output_dict['color']['green'] = output.color.green
    # output_dict['color']['blue'] = output.color.blue

    output_dict['signal_indices'] = []

    return output_dict

def export_signal (signal_index : int, link_model : AbstractLinkModel) -> Dict :
    """Est la méthode appelée pour créer un dictionnaire contenant les données d'un lien entre des entrées/sorties."""

    signal_dict = {}

    signal_dict['value'] = 0.0
    signal_dict['data_type'] = link_model.data_type.__str__()
    signal_dict['index'] = signal_index
    signal_dict['link_type'] = link_model.link_type.__str__()
    signal_dict['link_value'] = link_model.link_value
    signal_dict['text'] = link_model.text
    # signal_dict['color'] = {}
    # signal_dict['color']['red'] = link_model.color.red
    # signal_dict['color']['green'] = link_model.color.green
    # signal_dict['color']['blue'] = link_model.color.blue
 
    return signal_dict

#-----------------------------------
# Class
#-----------------------------------

class SimulationExporter (AbstractExporter) :
    """Est la classe qui permet d'exporter des fichiers de simulation."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        
        AbstractExporter.__init__(self)

    # -------------
    # Methods
    # -------------
    def save (self, model: SimulationModel, path : str) -> bool :
        # General informations
        simulation = {}
        simulation['export_version'] = '1.1.0'
        simulation['date_creation'] = model.date_creation
        simulation['date_edition'] = date.today() 
        simulation['version'] = model.version
        simulation['creator'] = model.creator

        # Scheduler parameters
        scheduler = {}
        if model.scheduler_model is None :
            # Set default parameters
            simulation['stop_time'] = 10
            simulation['step_time'] = 0.1
            scheduler['library'] = ''
            scheduler['name'] = ''
        else :
            scheduler['library'] = model.scheduler_model._library
            scheduler['name'] = model.scheduler_model._name

            if model.scheduler_model.params is None : 
                simulation['stop_time'] = 10
                simulation['step_time'] = 0.1
            else :
                simulation['stop_time'] = model.scheduler_model.params.stop_time
                simulation['step_time'] = model.scheduler_model.params.step_time
        simulation['scheduler'] = scheduler
        
        diagram = {}
        boxes = []        
        signals = []

        last_signal_index = 0
        signals_dict : Dict[AbstractSignalModel, int] = {} 

        # Filtering Graphics element
        box_models = [graphic_element for graphic_element in model.graphical_elements if isinstance(graphic_element, BoxModel)]

        # Box Models
        for box_model in box_models:
            # Get dict of box model
            current_box = box_model.to_dict()

            # Inputs
            for inputs_group in box_model.inputs_groups.values(): 
                # Build input dict
                input_group_dict = inputs_group.to_dict()

                for input_index, input_model in enumerate(inputs_group.inputs):
                    # Get input dict
                    input_dict = input_group_dict["inputs"][input_index]

                    # Handle signal
                    if input_model.has_link():
                        # Get link (only one possible)
                        link = input_model._links[0]
                        
                        # If Link already exists
                        if link in signals_dict:
                            input_dict['signal_index'] = signals_dict[link]

                        # If doesn't already exist
                        else: 
                            current_signal = link.to_dict()
                            current_signal['index'] = last_signal_index
                            signals.append(current_signal)

                            signals_dict[link] = last_signal_index
                            input_dict['signal_index'] = last_signal_index
                            last_signal_index += 1

                current_box['inputs_groups'].append(input_group_dict)

            # Outputs
            for outputs_group in box_model.outputs_groups.values(): 
                # Build output dict
                output_group_dict = outputs_group.to_dict()

                for output_index, output_model in enumerate(outputs_group.outputs):
                    # Get output dict
                    output_dict = output_group_dict["outputs"][output_index]
                    output_dict['signal_indices'] = []

                    # Handle signal
                    if output_model.has_link():

                        for link in output_model.links:
                            # If Link already exists
                            if link in signals_dict:
                                output_dict['signal_indices'].append(signals_dict[link])

                            # If doesn't already exist
                            else: 
                                current_signal = link.to_dict()
                                current_signal['index'] = last_signal_index
                                signals.append(current_signal)

                                signals_dict[link] = last_signal_index
                                output_dict['signal_indices'].append(last_signal_index)
                                last_signal_index += 1

                current_box['outputs_groups'].append(output_group_dict)

            # Append box
            boxes.append(current_box)

        diagram['boxes'] = boxes
        diagram['signals'] = signals
        
        simulation['diagram'] = diagram

        serialization = {}
        serialization['simulation'] =  simulation

        with open(path, 'w') as file : 
            yaml.dump(serialization, file)
            return True

