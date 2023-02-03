#-----------------------------------
# Imports
#-----------------------------------

# Project Imports
from muphyn.packages.interface.graphical_actions.abstract_unique_element_diagram_action import AbstractUniqueElementDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class DiagramAddInputToBoxAction (AbstractUniqueElementDiagramAction) :
    """Est la classe d'action permettant d'ajouter une entrée à une box."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, graphical_element : AbstractGraphicalElement, input_group_name : str, input_index: int = -1) :

        AbstractUniqueElementDiagramAction.__init__(self, graphical_element)

        self._input_added_graphical_index = None
        self._input_group_name = input_group_name
        self._input_index = input_index

    # -------------
    # Methods
    # -------------

    def do (self) :
        
        # Append input
        if self._input_index == -1:
            input_model = self.graphical_element.append_input(self._input_group_name)
        else:
            input_model = self.graphical_element.insert_input(self._input_group_name, self._input_index)
        
        if self._input_added_graphical_index is None :
            # Get the input graphical index if not already added before
            self._input_added_graphical_index = input_model.graphical_index

        else :
            # Set the input graphical index if already added before
            input_model.graphical_index = self._input_added_graphical_index


    def undo (self) :
        
        box = self.graphical_element

        if box is None : 
            return

        for input_index in range(box.input_len - 1, -1, -1) :

            input = box.get_input(self._input_group_name, input_index)
            if input.graphical_index == self._input_added_graphical_index :             
                box.remove_input(self._input_group_name, input)