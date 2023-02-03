#-----------------------------------
# Imports
#-----------------------------------

from typing import Iterable
from PyQt5.QtCore import pyqtSignal  
from PyQt5.QtWidgets import QTabWidget, QWidget
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder

from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class AbstractEditor (QWidget) : 
    """Est la classe abstraite commune aux éditeurs de contenus."""
    
    # -------------
    # Static Element
    # -------------

    TAB_ID : int = 0

    # -------------
    # Signals
    # -------------
    
    elements_selected_changed = pyqtSignal(object)
    """Est la signal appelé lorsque la sélection contenu dans le modèle est modifié."""

    name_changed = pyqtSignal(object, str)
    """Est le signal appelé lorsque le nom du modèle est modifié."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, tab_holder : QTabWidget, editable_model : AbstractEditableModel, actions_holder : ActionsHolder) :
        QWidget.__init__(self)

        self._tab_holder = tab_holder
        self._editable_model = editable_model
        self._editable_model.name_changed.connect(self.editable_model_name_changed)
        self._editable_model.selection_changed.connect(self.elements_selected_changed)
        self._actions_holder = actions_holder

        # Set Tab ID
        self._id = AbstractEditor.TAB_ID

        # Increment Global Tab ID value
        AbstractEditor.TAB_ID += 1


    # -------------
    # Properties
    # -------------

    @property
    def editable_model (self) -> AbstractEditableModel :
        """Permet de récuperer le model en cours d'édition."""
        return self._editable_model

    @property
    def tab_text (self) -> str :
        """Permet de récuperer le texte à afficher dans le nom de l'onglet."""
        return self._editable_model.name

    @property
    def actions_holder (self) -> ActionsHolder :
        """Permet de récuperer l'action holder de l'éditeur."""
        return self._actions_holder

    
    @property
    def id(self) -> int :
        """ 
        Get the tab ID 

        Returns :
        ---------
        id: int
            ID of the tab
        """
        return self._id

    # -------------
    # Properties
    # -------------

    def editable_model_name_changed (self, kwargs) :
        """Est la méthode appelée lorsque le nom du modèle est modifié."""
        LogManager().set_project_name(self._id, kwargs['name'])
        self.name_changed.emit(self, kwargs['name'])

    def copy (self) -> None :
        """Permet de copier la séléction actuelle dans le presse papier."""
        raise Exception('AbstractEditor.copy is an abstract method and should be overloaded.')

    def cut (self) -> None :
        """Permet de couper la séléction actuelle dans le presse papier."""
        raise Exception('AbstractEditor.cut is an abstract method and should be overloaded.')

    def paste (self) -> None :
        """Permet de coller le contenu du presse papier dans l'éditeur actuel."""
        raise Exception('AbstractEditor.paste is an abstract method and should be overloaded.')

    def selected_elements (self) -> Iterable :
        """Permet de récuperer les éléments sélectionnés dans l'interface."""
        raise Exception('AbstractEditor.selected_elements is an abstract method and should be overloaded.')

    def unslect_elements (self) -> None :
        """Permet de déselectionner les éléments acutellements sélectionnés dans l'interface."""
        raise Exception('AbstractEditor.unslect_elements is an abstract method and should be overloaded.')

    def elements (self) -> Iterable :
        """Permet de récuperer tous les éléments de l'interface."""
        raise Exception('AbstractEditor.elements is an abstract method and should be overloaded.')

    def zoom (self, value : int) -> None :
        """Permet de changer le zoom de l'éditeur."""
        raise Exception('AbstractEditor.zoom is an abstract method and should be overloaded.')
        
    def add_item (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet d'ajouter un élément graphique à l'interface."""
        raise Exception('AbstractEditor.add_item is an abstract method and should be overloaded.')
        
    def rem_item (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet de supprimer un élément graphique de l'interface."""
        raise Exception('AbstractEditor.rem_item is an abstract method and should be overloaded.')

    def delete_selection (self) -> None :
        """Permet de supprimer tous les éléments présent dans l'interface."""
        raise Exception('AbstractEditor.delete_selection is an abstract method and should be overloaded.')

    def clear (self) -> None :
        """Permet de supprimer tous les éléments présent dans l'interface."""
        raise Exception('AbstractEditor.clear is an abstract method and should be overloaded.')

