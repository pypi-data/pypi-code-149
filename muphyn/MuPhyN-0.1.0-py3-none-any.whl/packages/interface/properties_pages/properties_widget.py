#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Any

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLayout

from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor
from muphyn.packages.interface.properties_pages.properties_page_builder import get_properties_page

#-----------------------------------
# Class
#-----------------------------------

class PropertiesWidget (QWidget) :
    """Est le widget qui affiche les propriétés des éléments sélectionnés."""
        
    # -------------
    # Constructors
    # -------------

    def __init__(self, parent : QWidget = None) :
        
        QWidget.__init__(self, parent)

        # Init VBox Layout
        vBoxLayout = QVBoxLayout()
        vBoxLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.setLayout(vBoxLayout)

        self._properties_editors : List[AbstractPropertiesEditor] = []
        self._actions_holder = None
        self._current_model = None
        
    # -------------
    # Properties
    # -------------

    @property
    def actions_holder (self) -> ActionsHolder :
        """Permet de récuperer l'actions holder à utiliser pour les widgets de propriétés."""
        return self._actions_holder

    @actions_holder.setter
    def actions_holder (self, actions_holder_ : ActionsHolder) -> None :
        """Permet de modifier l'actions holder à utiliser pour les widgets de propriétés."""

        self._actions_holder = actions_holder_

        for property_editor in self._properties_editors :
            property_editor.actions_holder = self._actions_holder

    @property
    def current_model (self) -> Any :
        """Permet de récuperer le modèle actuellement en cours d'édition."""
        return self._current_model

    @current_model.setter
    def current_model (self, current_model_ : Any) -> None :
        """Permet de modifier le modèle actuellement en cours d'édition."""
        for editor in self._properties_editors : 

            # Remove all items from layout
            if self.layout() is not None:
                self.layout().removeWidget(editor)

            # Disable update from property editor
            editor.setUpdatesEnabled(False)
            editor.actions_holder = None
            editor.unload()
            editor.deleteLater()

        # Clear list of property editors
        self._properties_editors.clear()

        self._current_model = current_model_

        # Build List of Property Editors
        for rowIndex, editor in enumerate(get_properties_page(self._current_model)):
            editor.actions_holder = self.actions_holder
            self._properties_editors.append(editor)
            self.layout().addWidget(editor)