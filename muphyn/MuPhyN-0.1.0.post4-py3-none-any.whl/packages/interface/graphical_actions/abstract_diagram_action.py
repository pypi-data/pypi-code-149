#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from muphyn.packages.interface.graphical_actions.abstract_graphical_action import AbstractGraphicalAction

#-----------------------------------
# Class
#-----------------------------------

class AbstractDiagramAction (AbstractGraphicalAction) :
    """Est la classe abstraite commune aux actions modifiant les informations contenus dans les modèles de diagram."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, diagram_model : Any) :

        AbstractGraphicalAction.__init__(self)
        self._diagram_model = diagram_model

    # -------------
    # Properties
    # -------------

    @property
    def diagram_model (self) -> Any :
        """Permet de récuperer le modèle diagram qu'il faut modifier avec les actions."""
        return self._diagram_model