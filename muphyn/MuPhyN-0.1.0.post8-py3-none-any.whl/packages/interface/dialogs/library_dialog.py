#-----------------------------------
# Imports
#-----------------------------------


import os
from typing import List, Any

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QAbstractItemView, QFileDialog, QListWidgetItem, QVBoxLayout, QGridLayout

from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder
from muphyn.packages.interface.dialogs.abstract_dialog import AbstractDialog
from muphyn.packages.interface.graphical_actions.library_dialog_add_action import LibraryDialogAddAction, _lst_contains_element
from muphyn.packages.interface.graphical_actions.library_dialog_remove_action import LibraryDialogRemoveAction
from muphyn.packages.interface.widgets.BaseWidgets.Button import PlainButton
from muphyn.packages.interface.utils.interface_constants import ApplicationWindowTitle
from muphyn.packages.interface.widgets.BaseWidgets.Label import TitlePropertyLabel

from muphyn.utils.paths import ROOT_DIR

#-----------------------------------
# Class
#-----------------------------------

class LibraryDialog (AbstractDialog) :
    """Est la classe permettant d'afficher une boîte de dialogue capable de modifier les bibliothèques des boxes et des solveurs."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, schedulers_libraries = SchedulersLibraries) :
        AbstractDialog.__init__(self, dialog_holder, 'library', f'{ApplicationWindowTitle} - Libraries')
        
        self._actions_holder = ActionsHolder()
        self.setMinimumSize(480, 360)
        self.resize(640, 480)
        self._init_ui()
        self._lst_libraries_selection_changed_event()
        self._fld_folder_text_edited_event()

        self._boxes_at_start : List[str] = []
        self._schedulers_libraries : SchedulersLibraries = schedulers_libraries
        self._solvers_at_start : List[str] = []

        for library_element in BoxesLibrariesManager().libraries :
            self._boxes_at_start.append(library_element.path)
            if not _lst_contains_element(self._lst_libraries, library_element.path) :
                QListWidgetItem(library_element.path, self._lst_libraries)

        for library_element in self._schedulers_libraries.libraries :
            self._solvers_at_start.append(library_element.path)
            if not _lst_contains_element(self._lst_libraries, library_element.path) :
                QListWidgetItem(library_element.path, self._lst_libraries)

        
    # -------------
    # Methods
    # -------------

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(event)

        if event.modifiers() == QtCore.Qt.ControlModifier:

            if event.key() == QtCore.Qt.Key_Z :
                self._actions_holder.undo()

            elif event.key() == QtCore.Qt.Key_Y :
                self._actions_holder.redo()

        elif event.modifiers() == QtCore.Qt.NoModifier :

            if event.key() == QtCore.Qt.Key_Delete :

                if self._lst_libraries.hasFocus():
                    self._remove_method()

    def _init_ui (self) -> None :
        """
        Est la méthode appelée pour déssiner l'interface de la boîte de dialogue
        capable d'afficher l'interface de la boîte de dialogue.
        """

        # Init main Layout
        mainLayout = QVBoxLayout()

        # Init Options Layout
        optionsLayout = QGridLayout()
        optionsLayout.setColumnMinimumWidth(1, 45)
        optionsLayout.setColumnMinimumWidth(2, 45)
        optionsLayout.setSpacing(5)

        # Init Buttons Layout
        buttonsLayout = QGridLayout()
        buttonsLayout.setColumnMinimumWidth(1, 90)
        buttonsLayout.setColumnMinimumWidth(2, 90)
        buttonsLayout.setHorizontalSpacing(5)

        # Folder Path Field Text
        self._fld_folder = QtWidgets.QLineEdit(self)
        self._fld_folder.setObjectName("_fld_folder")
        self._fld_folder.textEdited.connect(self._fld_folder_text_edited_event)

        # Search Button (Open a Folder Dialog)
        self._search_button = QtWidgets.QPushButton(self)
        self._search_button.setObjectName("_search_button")
        self._search_button.clicked.connect(self._search_method)

        # Library list title
        self._lbl_libraries = TitlePropertyLabel(self)
        self._lbl_libraries.setObjectName("_lbl_libraries")

        # Add Path Field Text Content to list as Item
        self._add_button = PlainButton(self)
        self._add_button.setObjectName("_add_button")
        self._add_button.clicked.connect(self._add_method)

        # Remove Item From List Button
        self._remove_button = QtWidgets.QPushButton(self)
        self._remove_button.setObjectName("_remove_button")
        self._remove_button.clicked.connect(self._remove_method)

        # List of all library pathes
        self._lst_libraries = QtWidgets.QListWidget()
        self._lst_libraries.setObjectName("_lst_libraries")
        self._lst_libraries.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self._lst_libraries.itemSelectionChanged.connect(self._lst_libraries_selection_changed_event)

        # Confirm Button (Update Boxes List)
        self._accept_button = PlainButton()
        self._accept_button.setObjectName("_accept_button")
        self._accept_button.clicked.connect(self._accept_method)

        # Cancel button (just close the library dialog and restore old library list)
        self._cancel_button = QtWidgets.QPushButton()
        self._cancel_button.setObjectName("_cancel_button")
        self._cancel_button.clicked.connect(self._cancel_method)

        # Adding options widget to layout
        optionsLayout.addWidget(self._fld_folder, 0, 0)
        optionsLayout.addWidget(self._search_button, 0, 1, 1, 2)
        optionsLayout.addWidget(self._lbl_libraries, 1, 0)
        optionsLayout.addWidget(self._add_button, 1, 1)
        optionsLayout.addWidget(self._remove_button, 1, 2)
        optionsLayout.addWidget(self._lst_libraries, 2, 0, 1, 3)
        optionsLayout.setRowStretch(2, 1)
        optionsLayout.setColumnStretch(0, 1)

        # Closing action layout
        buttonsLayout.addWidget(self._accept_button, 0, 1)
        buttonsLayout.addWidget(self._cancel_button, 0, 2)
        buttonsLayout.setColumnStretch(0, 1)

        # Main Layout
        mainLayout.addItem(optionsLayout)
        mainLayout.addItem(buttonsLayout)
        mainLayout.setSpacing(10)

        # Add Layout to file dialog
        self.setLayout(mainLayout)

        self._retranslate_ui(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslate_ui (self, Dialog) -> None :
        _translate = QtCore.QCoreApplication.translate
        
        self._search_button.setText(_translate("Dialog", "Select Folder"))
        self._add_button.setText(_translate("Dialog", "+"))
        self._remove_button.setText(_translate("Dialog", "-"))
        self._accept_button.setText(_translate("Dialog", "Apply"))
        self._cancel_button.setText(_translate("Dialog", "Cancel"))
        self._lbl_libraries.setText(_translate("Dialog", "Libraries"))

    @pyqtSlot()
    def _search_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur veut faire une recherche."""
        path = QFileDialog.getExistingDirectory(self, f"{ApplicationWindowTitle} - Select Libraries Folder", ROOT_DIR)

        if path is None or path == '':
            return

        self._fld_folder.setText(path)
        self._fld_folder_text_edited_event()

    @pyqtSlot()
    def _add_method (self) -> None :
        """Est la méthode appelée pour ajouter un élément dans la liste."""

        if _lst_contains_element(self._lst_libraries, self._fld_folder.text()):
            return

        library_action = LibraryDialogAddAction(self._lst_libraries, self._fld_folder.text())
        library_action.do()
        self._actions_holder.append(library_action)

    @pyqtSlot()
    def _remove_method (self) -> None :
        """Est la méthode appelée pour supprimer un élément de la liste."""
        
        selected_items : List[str] = []

        for selected_item in self._lst_libraries.selectedItems() :
            selected_items.append(selected_item.text())

        library_action = LibraryDialogRemoveAction(self._lst_libraries, selected_items)
        library_action.do()
        self._actions_holder.append(library_action)

    @pyqtSlot()
    def _accept_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur accepte les modifications apportées."""
        
        BoxesLibrariesManager().clear()
        self._schedulers_libraries.clear()

        for i in range(self._lst_libraries.__len__()) :
            path : str = self._lst_libraries.item(i).text()

            LogManager().debug(f"Adding \"{path}\"...")

            BoxesLibrariesManager().add_library(path)
            self._schedulers_libraries.add_library(path)

        BoxesLibrariesManager().load_libraries()
        self._schedulers_libraries.load_libraries()

        self.close()

    @pyqtSlot()
    def _cancel_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur annulle les modifications apportées."""
        self.close()

    @pyqtSlot()
    def _lst_libraries_selection_changed_event (self) -> None :
        """Est la méthode appelée lorsque la sélection des bibliothèque change."""
        self._remove_button.setEnabled(self._lst_libraries.selectedItems().__len__() > 0)
    
    @pyqtSlot()
    def _fld_folder_text_edited_event (self) -> None :
        """Est la méthode appelée lorsque le texte dans le champ de sélection de dossier est modifié."""
        if self._fld_folder.text().__len__() > 0:
            self._add_button.setEnabled(os.path.isdir(self._fld_folder.text()))

        else:
            self._add_button.setEnabled(False)