#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from typing import List

# PyQt5 Imports
from PyQt5.QtCore import QPointF

# Project Imports
from muphyn.packages.interface.graphical_actions.abstract_diagram_action import AbstractDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class DiagramMoveGraphicalElementAction (AbstractDiagramAction) :
    """Est l'action qui permet de déplacer des éléments graphiques."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, graphical_element : AbstractGraphicalElement, selection_elements : List[AbstractGraphicalElement], old_position : QPointF, new_position : QPointF) :
        
        AbstractDiagramAction.__init__(self, graphical_element.diagram_model)

        self._graphical_element_index = graphical_element.graphical_index
        self._selection_indices : List[int] = []

        for selected_element in selection_elements : 

            element_type = type(selected_element).__name__
            if element_type == 'BoxModel' or element_type == 'BoxInputModel' or element_type == 'BoxOutputModel' :
            
                if selected_element.graphical_index in self._selection_indices :
                    continue
            
                self._selection_indices.append(selected_element.graphical_index)


        self._old_position = old_position
        self._new_position = new_position

    # -------------
    # Properties
    # -------------

    def graphical_index (self) -> int : 
        """Permet de récuperer le graphical index de l'élément qui a créé l'action."""
        return self._graphical_element_index

    @property
    def old_position (self) -> QPointF :
        """Permet de récuperer la position avant modification."""
        return self._old_position

    @property
    def new_position (self) -> QPointF :
        """Permet de récuperer la position après modification."""
        return self._new_position

    @new_position.setter
    def new_position (self, new_position_ : QPointF) -> None :
        """Permet de modifier la position qui doit être appliqué à la modification."""

        if new_position_ is None : 
            return

        self._new_position = new_position_
        
    # -------------
    # Methods
    # -------------

    def contains_index (self, graphical_index_ : int) -> bool :
        """Permet de savoir si le grpahical index passé en paramètre est contenu dans la liste."""

        for selection_index in self._selection_indices : 
            if graphical_index_ == selection_index :
                return True

        return False

    def do (self) :
        
        diffrence = self._new_position - self._old_position
        for element_index in self._selection_indices :
            
            graphical_element : AbstractGraphicalElement = self.diagram_model.get_element_by_graphical_index(element_index)

            if graphical_element is None : 
                return

            graphical_element.action_pos_semaphore = True
            graphical_element.setPos(graphical_element.pos() + diffrence)
            graphical_element.action_pos_semaphore = False

    def undo (self) :
        
        diffrence = self._new_position - self._old_position
        for element_index in self._selection_indices :
            
            graphical_element : AbstractGraphicalElement = self.diagram_model.get_element_by_graphical_index(element_index)

            if graphical_element is None : 
                return

            graphical_element.action_pos_semaphore = True
            graphical_element.setPos(graphical_element.pos() - diffrence)
            graphical_element.action_pos_semaphore = False
