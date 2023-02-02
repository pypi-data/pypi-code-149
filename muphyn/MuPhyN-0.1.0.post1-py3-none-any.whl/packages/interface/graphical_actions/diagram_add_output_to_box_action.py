#-----------------------------------
# Imports
#-----------------------------------

# PyQt5 Imports
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

# Project Imports
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.interface.graphical_actions.abstract_unique_element_diagram_action import AbstractUniqueElementDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class DiagramAddOutputToBoxAction (AbstractUniqueElementDiagramAction) :
    """Est la classe d'action permettant d'ajouter une sortie à une box."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, graphical_element : AbstractGraphicalElement, output_group_name : str, output_index: int = -1) :

        AbstractUniqueElementDiagramAction.__init__(self, graphical_element)

        self._output_added_graphical_index = None
        self._output_group_name = output_group_name
        self._output_index = output_index

    # -------------
    # Methods
    # -------------

    def do (self) :
        
        # Append output
        if self._output_index == -1:
            output_model = self.graphical_element.append_output(self._output_group_name)
        else:
            output_model = self.graphical_element.insert_output(self._output_group_name, self._output_index)
        
        if self._output_added_graphical_index is None :
            # Get the output graphical index if not already added before
            self._output_added_graphical_index = output_model.graphical_index

        else :
            # Set the output graphical index if already added before
            output_model.graphical_index = self._output_added_graphical_index


    def undo (self) :
        
        box = self.graphical_element

        if box is None : 
            return

        for output_index in range(box.output_len - 1, -1, -1) :

            output = box.get_output(output_index)
            if output.graphical_index == self._output_added_graphical_index :             
                box.remove_output(output)