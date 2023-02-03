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

class DiagramResizeGraphicalElementAction (AbstractUniqueElementDiagramAction) :
    """Est l'action qui permet de modifier la taille des léments graphiques."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, graphical_element : AbstractGraphicalElement, old_size : QSizeF, new_size : QSizeF) :
        
        AbstractUniqueElementDiagramAction.__init__(self, graphical_element)

        self._old_size = old_size
        self._new_size = new_size

    # -------------
    # Properties
    # -------------

    @property
    def old_size (self) -> QSizeF :
        """Permet de récuperer la taille avant la modification."""
        return self._old_size

    @property
    def new_size (self) -> QSizeF :
        """Permet de récuperer la taille après modification."""
        return self._new_size

    @new_size.setter
    def new_size (self, new_size_ : QSizeF) -> None :
        """Permet de modifier la taille qui doit être appliqué pour la modification."""
        self._new_size = new_size_
        
    # -------------
    # Methods
    # -------------

    def do (self) :
        
        graphical_element = self.graphical_element

        if graphical_element is None : 
            return

        graphical_element.action_size_semaphore = True
        graphical_element.size = self.new_size
        graphical_element.action_size_semaphore = False

    def undo (self) :
        
        graphical_element = self.graphical_element

        if graphical_element is None : 
            return

        graphical_element.action_size_semaphore = True
        graphical_element.size = self.old_size
        graphical_element.action_size_semaphore = False