#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from typing import Iterable, Any

# PyQt5 Imports
from PyQt5.QtCore import QCoreApplication

# Project Imports
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor
from muphyn.packages.interface.properties_pages.box_properties import BoxProperties
from muphyn.packages.interface.properties_pages.moveable_graphical_element_properties_editor import MoveableGraphicalElementPropertiesEditor
from muphyn.packages.interface.properties_pages.parameter_properties_editor import ParameterPropertiesEditor
from muphyn.packages.interface.properties_pages.signal_properties_editor import SignalPropertiesEditor
from muphyn.packages.interface.properties_pages.title_properties_element import TitlePropertiesElement
from muphyn.packages.interface.properties_pages.unknown_properties_editor import UnknownPropertiesEditor
from muphyn.packages.interface.models.graphical_models.abstract_moveable_graphical_element import AbstractMoveableGraphicalElement
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.models.graphical_models.box_input_model import BoxInputModel
from muphyn.packages.interface.models.graphical_models.box_output_model import BoxOutputModel
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel
from muphyn.packages.interface.properties_pages.infinite_input_properties_editor import InfiniteInputPropertiesEditor
from muphyn.packages.interface.properties_pages.infinite_output_properties_editor import InfiniteOutputPropertiesEditor

#-----------------------------------
# Function
#-----------------------------------

def get_properties_page (element : Any) -> Iterable[AbstractPropertiesEditor] :
    
    based_editor_loaded = False

    if isinstance(element, SignalLinkModel) : 
        yield SignalPropertiesEditor(element)
        return
    
    if isinstance(element, BoxOutputModel) :
        properties_page = None

    elif isinstance(element, BoxInputModel) : 
        properties_page = None

    elif isinstance(element, BoxModel) :
        box_model : BoxModel = element
        yield BoxProperties(box_model)

        # Inputs
        already_added_name_input = []
        for input_group in box_model.inputs_groups.values(): 
            if input_group.is_infinite and not(input_group.name in already_added_name_input):
                already_added_name_input.append(input_group.name)
                yield InfiniteInputPropertiesEditor(box_model, input_group)

        # Outputs
        already_added_name_output = []
        for output_group in box_model.outputs_groups.values(): 
            if output_group.is_infinite and not(output_group.name in already_added_name_output):
                    already_added_name_output.append(output_group.name)
                    yield InfiniteOutputPropertiesEditor(box_model, output_group)

        if box_model.get_parameters_len() > 0 :
            yield TitlePropertiesElement(QCoreApplication.translate('properties_page_builder', u"Parameters : ", None))
            for parameter in box_model.get_parameters() :
                yield ParameterPropertiesEditor(box_model, parameter)

        based_editor_loaded = True


    if based_editor_loaded == False :
        yield UnknownPropertiesEditor()
        return

    else :

        if isinstance(element, AbstractMoveableGraphicalElement) :
            yield MoveableGraphicalElementPropertiesEditor(element)
            