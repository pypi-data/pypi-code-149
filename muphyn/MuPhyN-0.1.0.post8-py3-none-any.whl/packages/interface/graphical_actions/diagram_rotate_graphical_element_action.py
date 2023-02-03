#-----------------------------------
# Imports
#-----------------------------------

# PyQt5 Imports
from PyQt5.QtCore import QSizeF

# Project Imports
from muphyn.packages.interface.graphical_actions.abstract_unique_element_diagram_action import AbstractUniqueElementDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class DiagramRotateGraphicalElementAction (AbstractUniqueElementDiagramAction) :
    """Est l'action qui permet de modifier la rotation des léments graphiques."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, graphical_element : AbstractGraphicalElement, old_rotate : int, new_rotate : int) :
        
        AbstractUniqueElementDiagramAction.__init__(self, graphical_element)

        self._old_rotate = old_rotate
        self._new_rotate = new_rotate

    # -------------
    # Properties
    # -------------

    @property
    def old_rotate (self) -> QSizeF :
        """Permet de récuperer la rotation avant la modification."""
        return self._old_rotate

    @property
    def new_rotate (self) -> QSizeF :
        """Permet de récuperer la rotation après modification."""
        return self._new_rotate

    @new_rotate.setter
    def new_rotate (self, new_rotate_ : QSizeF) -> None :
        """Permet de modifier la rotation qui doit être appliqué pour la modification."""
        self._new_rotate = new_rotate_
        
    # -------------
    # Methods
    # -------------

    def do (self) :
        
        graphical_element = self.graphical_element

        if graphical_element is None : 
            return

        graphical_element.action_rot_semaphore = True
        graphical_element.setRotation(self._new_rotate)
        graphical_element.action_rot_semaphore = False

    def undo (self) :
        
        graphical_element = self.graphical_element

        if graphical_element is None : 
            return

        graphical_element.action_rot_semaphore = True
        graphical_element.setRotation(self._old_rotate)
        graphical_element.action_rot_semaphore = False