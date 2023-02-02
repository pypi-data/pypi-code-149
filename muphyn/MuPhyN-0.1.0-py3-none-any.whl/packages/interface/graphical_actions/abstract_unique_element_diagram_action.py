#-----------------------------------
# Imports
#-----------------------------------

# Project Imports
from muphyn.packages.interface.graphical_actions.abstract_diagram_action import AbstractDiagramAction
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class AbstractUniqueElementDiagramAction (AbstractDiagramAction) :
    """Est la classe abstraite commune aux actions modifiant les informations contenus dans un modèle unique d'un diagrame."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, graphical_element : AbstractGraphicalElement) :

        AbstractDiagramAction.__init__(self, graphical_element.diagram_model)
        self._graphical_index = graphical_element.graphical_index
        
    # -------------
    # Properties
    # -------------
    
    @property
    def graphical_element (self) :
        """Permet de récuperer l'élément graphique qui doit être modifiée."""
        return self._diagram_model.get_element_by_graphical_index(self._graphical_index)

    @property
    def graphical_index (self) :
        """Permet de récuperer l'index de l'élément graphique qui doit être modifié."""
        return self._graphical_index