#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Dict

from muphyn.packages.interface.graphical_actions.abstract_unique_element_diagram_action import AbstractUniqueElementDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel
from muphyn.packages.interface.graphical_actions import parser_decode as parser_decode
from muphyn.packages.interface.graphical_actions import parser_encode as parser_encode

#-----------------------------------
# Class
#-----------------------------------

class DiagramRemoveInputsFromBoxAction (AbstractUniqueElementDiagramAction) :
    """Est l'action permettant de supprimer les entrées d'une box."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_element : AbstractBoxModel, input_group_name: str, inputs : list[InputConnectionModel]) :

        AbstractUniqueElementDiagramAction.__init__(self, box_element)

        self._reconstructors : List[Dict] = []
        self._input_group_name: str = input_group_name
        self._inputs: list[InputConnectionModel] = inputs


    # -------------
    # Methods
    # -------------
    def do (self):

        box_model: AbstractBoxModel = self.graphical_element

        if box_model is None : 
            return

        for input_ in self._inputs:
            input_dict : Dict = {"graphical_index": input_.graphical_index}
            current_input : Dict = parser_encode.box_input(input_, input_dict)

            for signal in input_.links : 
                current_input['signals'].append(parser_encode.link(signal))
                signal.unbind()
                self.diagram_model.remove_element(signal)

            input_._links.clear()
            
            box_model.remove_input(self._input_group_name, input_)

            self._reconstructors.append(input_dict)

 
    def undo (self) :
        
        box_model : AbstractBoxModel = self.graphical_element 

        if box_model is None : 
            return

        self._reconstructors.reverse()
        for input_dict in self._reconstructors :
            parser_decode.box_input(input_dict, box_model)

            for signal_dict in input_dict['signals'] : 
                parser_decode.link(signal_dict, self.diagram_model)