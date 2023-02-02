#-----------------------------------
# Imports
#-----------------------------------
# PyQt Imports
from PyQt5.QtWidgets import QWidget, QFormLayout, QLayout, QGridLayout
from PyQt5.QtCore import Qt

# Project Imports
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder
from muphyn.packages.interface.graphical_actions.diagram_change_element_params_action import DiagramChangeElementParamsAction
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class AbstractPropertiesEditor (QWidget) :
    """Est la classe abstraite communes aux éléments permettant de modifier un model graphique."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, model : AbstractGraphicalElement) : 

        QWidget.__init__(self, None)
        self._model = model

        self.setLayout(self.create_layout())

        self.init_ui()
        self.translate_ui()

    # -------------
    # Properties
    # -------------

    @property
    def model (self) -> AbstractGraphicalElement :
        """Permet de récuperer le modèle édité par la page de propriétés."""
        return self._model

    @property
    def actions_holder (self) -> ActionsHolder :
        """Permet de récuperer le conteneur des actions."""
        return self._actions_holder

    @actions_holder.setter
    def actions_holder (self, actions_holder_ : ActionsHolder) -> None :
        """Permet de modifier le conteneur des actions."""
        self._actions_holder = actions_holder_


    def actions_generator (self, old_value, new_value, param_name) -> None :
        """Est la méthode appelée pour générer une """

        last_action = self.actions_holder.last_action

        if not(last_action is None) :
            if isinstance(last_action, DiagramChangeElementParamsAction) :
                if last_action.param_name == param_name : 
                    if type(old_value) != bool and type(new_value) != bool:

                        last_action.new_param_value = new_value
                        return

        action = DiagramChangeElementParamsAction(self.model, param_name, new_value, old_value)
        self.actions_holder.append(action)
        
    # -------------
    # Methods
    # -------------

    def init_ui (self) -> None :
        """Permet de créer les éléments graphiques de la page de propriétés."""
        raise Exception('AbstractPropertiesElement init_ui is an abstract method and should be overridden.')

    def translate_ui (self) -> None : 
        """Permet de traduire les éléments graphiques de la page de propriétés."""
        raise Exception('AbstractPropertiesElement translate_ui is an abstract method and should be overridden.')

    def create_layout (self) -> QLayout : 
        """Permet de créer le layout pour l'affichage actuel."""
        grid_layout = QGridLayout()
        grid_layout.setColumnMinimumWidth(0, 60)
        # grid_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        return grid_layout

    def unload (self) -> None :
        """Est la méthode appelée lorsque le page de propriété est supprimée de l'écran.""" 