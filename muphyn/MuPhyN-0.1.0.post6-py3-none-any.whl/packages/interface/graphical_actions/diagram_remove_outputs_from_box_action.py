#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Dict

from muphyn.packages.interface.graphical_actions.abstract_unique_element_diagram_action import AbstractUniqueElementDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel
from muphyn.packages.interface.graphical_actions import parser_decode as parser_decode
from muphyn.packages.interface.graphical_actions import parser_encode as parser_encode

#-----------------------------------
# Class
#-----------------------------------

class DiagramRemoveOutputsFromBoxAction (AbstractUniqueElementDiagramAction) :
    """Est l'action permettant de supprimer les sorties d'une box."""

    # -------------
    # Constructors
    # -------------
    
    def __init__ (self, box_element : AbstractBoxModel, output_group_name: str, outputs : List[OutputConnectionModel]) :

        AbstractUniqueElementDiagramAction.__init__(self, box_element)

        self._reconstructors : List[Dict] = []
        self._output_group_name: str = output_group_name
        self._outputs: list[OutputConnectionModel] = outputs
        
    # -------------
    # Methods
    # -------------
    def do (self):

        box_model: AbstractBoxModel = self.graphical_element

        if box_model is None : 
            return

        for output in self._outputs:
            output_dict : Dict = {"graphical_index": output.graphical_index}
            current_output : Dict = parser_encode.box_output(output, output_dict)
            current_output['signals'] = []

            for signal in output.links :
                current_output['signals'].append(parser_encode.link(signal))
                signal.unbind()
                self.diagram_model.remove_element(signal)

            output._links.clear()
            
            box_model.remove_output(self._output_group_name, output)

            self._reconstructors.append(output_dict)

    def undo (self) :
        
        box_model : AbstractBoxModel = self.graphical_element 

        if box_model is None : 
            return

        self._reconstructors.reverse()
        for output_dict in self._reconstructors :
            parser_decode.box_output(output_dict, box_model)

            for signal_dict in output_dict['signals'] : 
                parser_decode.link(signal_dict, self.diagram_model)