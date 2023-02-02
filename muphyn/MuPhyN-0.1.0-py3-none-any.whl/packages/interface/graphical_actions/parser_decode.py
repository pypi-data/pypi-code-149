#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from typing import Dict

# PyQt5 Imports
from PyQt5.QtCore import QPointF, QSizeF
from PyQt5.QtGui import QColor
from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager

# Project Imports
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.graphical_models.box_input_model import BoxInputModel
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.graphical_models.box_output_model import BoxOutputModel
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel
from muphyn.packages.interface.models.editable_models.abstract_diagram_model import AbstractDiagramModel

#-----------------------------------
# Functions
#-----------------------------------

def color (color_dict : Dict) -> QColor :
    """Permet de reconstruire une couleur sur base d'un dictionnaire."""
    return QColor(color_dict['red'], color_dict['green'], color_dict['blue'])
    
def link (link_reconstructor : Dict, diagram_model : AbstractDiagramModel) -> SignalLinkModel :
    """Permet de reconstruire un lien suivant son reconstructeur."""
    input_box = diagram_model.get_element_by_graphical_index(link_reconstructor['input_box_index'])
    output_box = diagram_model.get_element_by_graphical_index(link_reconstructor['output_box_index'])

    if input_box is None : 
        LogManager().error('reconstruct link : input box = None')
        return None

    if not(hasattr(input_box, '_inputs')) :
        LogManager().error('reconstruct link : input box has no inputs')
        return None

    if output_box is None : 
        LogManager().error('reconstruct link : output box = None')
        return None

    if not(hasattr(output_box, '_outputs')) :
        LogManager().error('reconstruct link : output box has no inputs')
        return None

    input = None
    output = None

    for i in input_box.inputs : 
        if i.graphical_index == link_reconstructor['input_index'] :
            input = i
            break

    for o in output_box.outputs :
        if o.graphical_index == link_reconstructor['output_index'] : 
            output = o
            break

    if input is None :
        LogManager().error('reconstruct link : no input found')
        return None
        
    if output is None : 
        LogManager().error('reconstruct link : no output found')
        return None


    link_model = diagram_model.link_nodes(input, output, link_value = link_reconstructor['link_value'], link_type = link_reconstructor['link_type'], link_text = link_reconstructor['link_text']) 
    link_model.graphical_index = link_reconstructor['graphical_index']

    return link_model

def box (box_reconstructor : Dict) -> BoxModel :
    """Permet de reconstruire une box suivant son reconstructeur."""

    # Box data
    library = box_reconstructor['library']
    name = box_reconstructor['name']

    # Get box data
    box_data = BoxesLibrariesManager().get_box_data(library, name)

    # Init new box
    box_model = BoxModel(
        library,
        name,
        QPointF(box_reconstructor['geometry']['x'], box_reconstructor['geometry']['y']),
        QSizeF(box_reconstructor['geometry']['width'], box_reconstructor['geometry']['height']),
        box_reconstructor['geometry']['rotation'],
        True,
        box_reconstructor['text'],
        box_data.icon
    )

    # Build inputs groups
    box_model.add_inputs_groups(box_data.inputs, infinite_groups_reset=True)

    # Build outputs groups
    box_model.add_outputs_groups(box_data.outputs, infinite_groups_reset=True)

    for param_name in box_reconstructor['params']:
        box_model.create_parameter(param_name, box_reconstructor['params'][param_name]['type'], box_reconstructor['params'][param_name]['value'])

    # Common box informations (inputs, outputs)
    abstract_box_model(box_model, box_reconstructor)

    return box_model

def composite_box_input (input_reconstructor : Dict) -> BoxInputModel:
    """Permet de reconstruire une entrée de box composite suivant son reconstructeur."""
    raise Exception('No reconstructor created yet for the composite box input !!!')

def composite_box_output (output_reconstructor : Dict) -> BoxOutputModel:
    """Permet de reconstruire une sortie de box composite suivant son reconstructeur."""
    raise Exception('No reconstructor created yet for the composite box output !!!')

def abstract_box_model (box : AbstractBoxModel, box_reconstructor : Dict) -> AbstractBoxModel :
    """Permet de repeupler les données contenues dans le reconstructeur dans l'abstract box model."""

    # Inputs
    for inputs_group_dict in box_reconstructor['inputs_groups']:
        for input_index, input_dict in enumerate(inputs_group_dict['inputs']) :
            if inputs_group_dict["isInfinite"]:
                # Add input to group
                input_ = box.append_input(inputs_group_dict["name"])
            else:
                # Get input
                input_ = box.inputs_groups[inputs_group_dict["name"]].inputs[input_index]

            # Set input values
            input_.graphical_index = input_dict['graphical_index']
            input_.text = input_dict['text']

    # Outputs
    for outputs_group_dict in box_reconstructor['outputs_groups']:
        for output_index, output_dict in enumerate(outputs_group_dict['outputs']) :
            if outputs_group_dict["isInfinite"]:
                # Add output to group
                output = box.append_output(outputs_group_dict["name"])
            else:
                # Get output
                output = box.outputs_groups[outputs_group_dict["name"]].outputs[output_index]

            # Set output values
            output.graphical_index = output_dict['graphical_index']
            output.text = output_dict['text']

    abstract_graphical_element(box, box_reconstructor)
    return box

def abstract_graphical_element (graphical_element : AbstractGraphicalElement, element_reconstructor : Dict) -> AbstractGraphicalElement :
    """Permet de repeupler les données contenues dans le reconstructeur dans l'objet graphique."""
    graphical_element.graphical_index = element_reconstructor['graphical_index']
    return graphical_element

def decode (element_reconstructor : Dict) -> AbstractGraphicalElement :
    """Permet de retourner un l'élément contenu dans le dictionnaire."""

    if element_reconstructor is None :
        return

    if element_reconstructor['type'] == 'box' :
        return box(element_reconstructor)

    elif element_reconstructor['type'] == 'box-composite-input' :
        return composite_box_input(element_reconstructor)

    elif element_reconstructor['type'] == 'box-composite-output' :
        return composite_box_output(element_reconstructor)
