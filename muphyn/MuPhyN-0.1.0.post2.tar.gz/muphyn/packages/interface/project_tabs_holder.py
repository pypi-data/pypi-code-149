#-----------------------------------
# Imports
#-----------------------------------

from typing import Iterable, overload
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QTabWidget, QWidget

from muphyn.packages.interface.editors.abstract_editor import AbstractEditor
from muphyn.packages.interface.editors.diagram_editor import DiagramEditor
from muphyn.packages.core.utils.log_manager import LogManager

#-----------------------------------
# Class
#-----------------------------------

class ProjectTabsHolder (QTabWidget) :
    """Est le widget qui affiche les différents onglets des projets du programme."""
    

    # -------------
    # Signals
    # -------------
    
    elements_selected_changed = pyqtSignal(object)
    """Est le signal appelé quand l'onglet sélectionné est changé."""

    tab_close_request = pyqtSignal(object)
    """Est le signal appelée quand un des onglet reçoit une requête de fermeture."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, parent : QWidget) :
        
        QTabWidget.__init__(self, parent)

        self.setTabsClosable(True)
        self.setMovable(True)
        self.currentChanged.connect(self.current_tab_changed)
        self._current_editor = None 

    # -------------
    # Properties
    # -------------

    @property
    def current_editor (self) -> AbstractEditor : 
        """Permet de récuperer l'éditeur actuel."""
        return self._current_editor

    @current_editor.setter
    def current_editor (self, current_editor_ : AbstractEditor) -> None :
        """Permet de modifier l'éditeur actuel."""

        if not(self._current_editor is None) : 
            self._current_editor.elements_selected_changed.disconnect(self.current_editor_selected_elements_changed)

        self._current_editor = current_editor_

        if self._current_editor is None :
            self.elements_selected_changed.emit(None)
            
        else : 
            self.elements_selected_changed.emit(self._current_editor.selected_elements)
            self._current_editor.elements_selected_changed.connect(self.current_editor_selected_elements_changed) 

    # -------------
    # Methods
    # -------------
    def __iter__(self) -> Iterable[DiagramEditor]:
        return iter([self.widget(childIndex) for childIndex in range(self.count())])

    def current_tab_changed (self, index: int) -> None :
        """Est la méthode appelée lorsque l'utilisateur modifie l'onglet selectionné."""

        if self.currentWidget() == None :
            self.current_editor = None 

        elif isinstance(self.currentWidget(), AbstractEditor) :
            # Change the current editor
            self.current_editor = self.currentWidget()

            # Update in the LOG Manager the current editor
            LogManager().set_current_project_id(self.currentWidget().id)

    def current_editor_selected_elements_changed (self, elements) -> None :
        """Est la méthode appelée lorsque la sélection de l'utilisateur est modifiée."""
        self.elements_selected_changed.emit(elements)

    def addEditor (self, model : AbstractEditor) -> int :
        model.name_changed.connect(self.tab_name_changed)
        return super().addTab(model, model.tab_text)

    def removeTab (self, index : int) -> None :
        editor = self.widget(index)
        if hasattr(editor, 'name_changed') :
            editor.name_changed.disconnect(self.tab_name_changed)

        super().removeTab(index)
    
    def tab_name_changed (self, tab_ : AbstractEditor, title_ : str) -> None :
        """Est la méthode appelée lorsque le nom du modèle est modifié."""
        LogManager().debug('tab name changed')
        self.setTabText(self.indexOf(tab_), title_)