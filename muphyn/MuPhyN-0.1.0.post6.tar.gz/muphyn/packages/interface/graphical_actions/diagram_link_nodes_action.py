#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from muphyn.packages.interface.graphical_actions.abstract_diagram_action import AbstractDiagramAction
from muphyn.packages.interface.models.links_model.abstract_node_model import AbstractNodeModel
from muphyn.packages.interface.models.signals_model.abstract_signal_model import AbstractSignalModel
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel

#-----------------------------------
# Class
#-----------------------------------

class DiagramLinkNodesAction (AbstractDiagramAction) :
    """Est le type d'action qui permet de lier des noeuds entre eux."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, input_node : AbstractNodeModel, output_node : AbstractNodeModel) :

        AbstractDiagramAction.__init__(self, input_node.diagram_model)
        
        self._input_box_index = input_node.box_model.graphical_index
        self._output_box_index = output_node.box_model.graphical_index
        self._input_index = input_node.graphical_index
        self._output_index = output_node.graphical_index

        self._link_index = -1

    # -------------
    # Methods
    # -------------

    def get_input (self) -> Any :
        """Permet de récuperer l'entrée à lier."""

        box_element = self.diagram_model.get_element_by_graphical_index(self._input_box_index)

        if box_element is None : 
            return None 

        if hasattr(box_element, 'inputs_groups'):
            for inputs_group in box_element.inputs_groups.values():
                for input_ in inputs_group.inputs:
                    if input_.graphical_index == self._input_index:
                        return input_

        return None

    def get_output (self) -> Any :
        """Permet de récuperr la sortie à lier."""

        box_element = self.diagram_model.get_element_by_graphical_index(self._output_box_index)

        if box_element is None : 
            return None 

        if hasattr(box_element, 'outputs') :
            for output in box_element.outputs :
                if output.graphical_index == self._output_index :
                    return output

        return None

    def do (self) :
        input_ = self.get_input()
        output = self.get_output()

        # Set input_ as connected
        input_.is_connected = True

        link = self.diagram_model.link_nodes(input_, output)

        if self._link_index == -1 :
            self._link_index = link.graphical_index
        
        else :
            link.graphical_index = self._link_index

    def undo (self) :
        link : SignalLinkModel = self.diagram_model.get_element_by_graphical_index(self._link_index)
        if not(link is None) :
            
            # Get Input/Output BoxModel Graphical Index
            self._input_box_index = link.input.box_model.graphical_index
            self._output_box_index = link.output.box_model.graphical_index

            # Get Input/Output Graphical Index
            self._input_index = link.input.graphical_index
            self._output_index = link.output.graphical_index

            link.unbind()
            self.diagram_model.remove_element(link)
