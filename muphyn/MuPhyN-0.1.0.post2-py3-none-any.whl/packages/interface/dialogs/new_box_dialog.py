#-----------------------------------
# Imports
#-----------------------------------


import os
from datetime import date
from typing import List, Any

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QMetaObject, QPointF, QRect, QSizeF, pyqtSlot
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QWidget
from PyQt5.QtWidgets import QAbstractItemView, QComboBox, QFileDialog, QFrame

from muphyn.packages.core.plci_core_data_type import get_data_type
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.graphical_actions.actions_holder import ActionsHolder
from muphyn.packages.interface.graphical_actions.new_box_dialog_add_action import NewBoxDialogAddAction
from muphyn.packages.interface.graphical_actions.new_box_dialog_remove_action import NewBoxDialogRemoveAction
from muphyn.packages.interface.models.graphical_models.box_input_model import BoxInputModel
from muphyn.packages.interface.models.graphical_models.box_output_model import BoxOutputModel
from muphyn.packages.interface.user_data.user_data import UserData
from .abstract_dialog import AbstractDialog

from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.editable_models.box_composite_model import BoxCompositeModel
from muphyn.packages.interface.models.editable_models.box_code_model import BoxCodeModel

#-----------------------------------
# Class
#-----------------------------------

class NewBoxDialog (AbstractDialog) : 
    """Est la classe permettant d'afficher une boîte de dialogue capable de créer une nouvelle box."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, user_data : UserData) :
        AbstractDialog.__init__(self, dialog_holder, 'new_simulation', 'Nouvelle Simulation')
        
        self.setFixedSize(630, 480)

        self._user_data = user_data
        self._actions_holder = ActionsHolder()

        self._init_ui()

        self._test_data_accept_button()
        self._tbl_inputs_selection_changed()
        self._tbl_outputs_selection_changed()

    # -------------
    # Properties
    # -------------

    @property
    def user_data (self) -> UserData :
        """Permet de récuperer les données utilisateurs."""
        return self._user_data
    
    # -------------
    # Methods
    # -------------

    def _init_ui (self) :
        """Est la méthode pour remplire l'interface graphique aves les widgets nécessaires."""
        if not self.objectName():
            self.setObjectName("_new_box_dialog")

        self._btn_cancel = QPushButton(self)
        self._btn_cancel.setObjectName("_btn_cancel")
        self._btn_cancel.setGeometry(QRect(540, 440, 81, 24))
        self._btn_cancel.clicked.connect(self._btn_cancel_clicked)

        self._btn_accept = QPushButton(self)
        self._btn_accept.setObjectName("_btn_accept")
        self._btn_accept.setGeometry(QRect(450, 440, 81, 24))
        self._btn_accept.clicked.connect(self._btn_accept_clicked)

        self._btn_box_path = QPushButton(self)
        self._btn_box_path.setObjectName("_btn_box_path")
        self._btn_box_path.setGeometry(QRect(550, 50, 75, 24))
        self._btn_box_path.clicked.connect(self._btn_box_path_clicked)

        self._btn_input_remove = QPushButton(self)
        self._btn_input_remove.setObjectName("_btn_input_remove")
        self._btn_input_remove.setGeometry(QRect(200, 190, 51, 24))
        self._btn_input_remove.clicked.connect(self._btn_input_remove_clicked)

        self._btn_input_add = QPushButton(self)
        self._btn_input_add.setObjectName("_btn_input_add")
        self._btn_input_add.setGeometry(QRect(260, 190, 51, 24))
        self._btn_input_add.clicked.connect(self._btn_input_add_clicked)

        self._btn_output_remove = QPushButton(self)
        self._btn_output_remove.setObjectName("_btn_output_remove")
        self._btn_output_remove.setGeometry(QRect(510, 190, 51, 24))
        self._btn_output_remove.clicked.connect(self._btn_output_remove_clicked)

        self._btn_output_add = QPushButton(self)
        self._btn_output_add.setObjectName("_btn_output_add")
        self._btn_output_add.setGeometry(QRect(570, 190, 51, 24))
        self._btn_output_add.clicked.connect(self._btn_output_add_clicked)

        self._fld_box_name = QLineEdit(self)
        self._fld_box_name.setObjectName("_fld_box_name")
        self._fld_box_name.setGeometry(QRect(130, 20, 411, 22))
        self._fld_box_name.textEdited.connect(self._test_data_accept_button)

        self._fld_box_path = QLineEdit(self)
        self._fld_box_path.setObjectName("_fld_box_path")
        self._fld_box_path.setGeometry(QRect(130, 50, 411, 22))
        self._fld_box_path.textEdited.connect(self._test_data_accept_button)

        self._fld_library = QLineEdit(self)
        self._fld_library.setObjectName("_fld_library")
        self._fld_library.setGeometry(QRect(130, 110, 411, 22))
        self._fld_library.textEdited.connect(self._test_data_accept_button)

        self._fld_creator = QLineEdit(self)
        self._fld_creator.setObjectName("_fld_creator")
        self._fld_creator.setGeometry(QRect(130, 140, 411, 22))
        self._fld_creator.textEdited.connect(self._test_data_accept_button)
        self._fld_creator.setText(self._user_data.user_name)

        self._cmb_box_type = QComboBox(self)
        self._cmb_box_type.setObjectName("_cmb_box_type")
        self._cmb_box_type.setGeometry(QRect(130, 80, 411, 22))
        self._cmb_box_type.currentIndexChanged.connect(self._test_data_accept_button)
        self._cmb_box_type.addItem('Composite', 0)
        self._cmb_box_type.addItem('Code', 1)

        self._tbl_inputs = QTableWidget(self)
        self._tbl_inputs.setObjectName("_tbl_inputs")
        self._tbl_inputs.setGeometry(QRect(10, 219, 300, 211))
        self._tbl_inputs.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self._tbl_inputs.selectionModel().selectionChanged.connect(self._tbl_inputs_selection_changed)
        self._tbl_inputs.setColumnCount(4)
        self._tbl_inputs.setHorizontalHeaderLabels(['Nom', 'Type', 'Nombre', 'Valeur'])
        self._tbl_inputs.currentCellChanged.connect(self._tbl_inputs_current_cell_changed)

        self._tbl_outputs = QTableWidget(self)
        self._tbl_outputs.setObjectName("_tbl_outputs")
        self._tbl_outputs.setGeometry(QRect(320, 220, 300, 211))
        self._tbl_outputs.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self._tbl_outputs.selectionModel().selectionChanged.connect(self._tbl_outputs_selection_changed)
        self._tbl_outputs.setColumnCount(4)
        self._tbl_outputs.setHorizontalHeaderLabels(['Nom', 'Type', 'Nombre', 'Valeur'])
        self._tbl_outputs.currentCellChanged.connect(self._tbl_outputs_current_cell_changed)

        self._lbl_box_name = QLabel(self)
        self._lbl_box_name.setObjectName("_lbl_box_name")
        self._lbl_box_name.setGeometry(QRect(10, 25, 111, 16))

        self._lbl_box_path = QLabel(self)
        self._lbl_box_path.setObjectName("_lbl_box_path")
        self._lbl_box_path.setGeometry(QRect(10, 55, 111, 16))

        self._lbl_box_type = QLabel(self)
        self._lbl_box_type.setObjectName("_lbl_box_type")
        self._lbl_box_type.setGeometry(QRect(10, 85, 111, 16))

        self._lbl_library = QLabel(self)
        self._lbl_library.setObjectName("_lbl_library")
        self._lbl_library.setGeometry(QRect(10, 115, 111, 16))

        self._lbl_creator = QLabel(self)
        self._lbl_creator.setObjectName("_lbl_creator")
        self._lbl_creator.setGeometry(QRect(10, 145, 111, 16))

        self._lbl_inputs = QLabel(self)
        self._lbl_inputs.setObjectName("_lbl_inputs")
        self._lbl_inputs.setGeometry(QRect(10, 195, 49, 16))

        self._lbl_outputs = QLabel(self)
        self._lbl_outputs.setObjectName("_lbl_outputs")
        self._lbl_outputs.setGeometry(QRect(320, 195, 49, 16))

        self._ln_separator = QFrame(self)
        self._ln_separator.setObjectName("_ln_separator")
        self._ln_separator.setGeometry(QRect(10, 170, 611, 21))
        self._ln_separator.setFrameShape(QFrame.HLine)
        self._ln_separator.setFrameShadow(QFrame.Sunken)

        QWidget.setTabOrder(self._fld_box_name, self._fld_box_path)
        QWidget.setTabOrder(self._fld_box_path, self._btn_box_path)
        QWidget.setTabOrder(self._btn_box_path, self._cmb_box_type)
        QWidget.setTabOrder(self._cmb_box_type, self._fld_library)
        QWidget.setTabOrder(self._fld_library, self._fld_creator)
        QWidget.setTabOrder(self._fld_creator, self._btn_accept)
        QWidget.setTabOrder(self._btn_accept, self._btn_cancel)
        QWidget.setTabOrder(self._btn_cancel, self._btn_input_remove)
        QWidget.setTabOrder(self._btn_input_remove, self._btn_input_add)
        QWidget.setTabOrder(self._btn_input_add, self._btn_output_remove)
        QWidget.setTabOrder(self._btn_output_remove, self._btn_output_add)
        QWidget.setTabOrder(self._btn_output_add, self._tbl_inputs)
        QWidget.setTabOrder(self._tbl_inputs, self._tbl_outputs)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog) -> None :
        self.setWindowTitle(QCoreApplication.translate("_new_box_dialog", "Dialog", None))
        self._btn_cancel.setText(QCoreApplication.translate("_new_box_dialog", "Annuler", None))
        self._btn_accept.setText(QCoreApplication.translate("_new_box_dialog", "Accepter", None))
        self._btn_box_path.setText(QCoreApplication.translate("_new_box_dialog", "Rechercher", None))
        self._btn_input_remove.setText(QCoreApplication.translate("_new_box_dialog", "-", None))
        self._btn_input_add.setText(QCoreApplication.translate("_new_box_dialog", "+", None))
        self._btn_output_remove.setText(QCoreApplication.translate("_new_box_dialog", "-", None))
        self._btn_output_add.setText(QCoreApplication.translate("_new_box_dialogg", "+", None))
        self._lbl_inputs.setText(QCoreApplication.translate("n_new_box_dialog", "Entrées :", None))
        self._lbl_outputs.setText(QCoreApplication.translate("_new_box_dialog", "Sorties :", None))
        self._lbl_box_name.setText(QCoreApplication.translate("_new_box_dialog", "Nom de la box :", None))
        self._lbl_box_path.setText(QCoreApplication.translate("_new_box_dialog", "Chemin vers la box :", None))
        self._lbl_box_type.setText(QCoreApplication.translate("_new_box_dialog", "Type de box :", None))
        self._lbl_library.setText(QCoreApplication.translate("_new_box_dialog", "Bibliothèque :", None))
        self._lbl_creator.setText(QCoreApplication.translate("_new_box_dialog", "Créateur :", None))

    @pyqtSlot()
    def _test_data_accept_button (self) -> None :
        """Est la méthode pour activer/désactiver le bouton accept en fonction des champs d'édition."""
        
        if self._fld_box_name.text().strip().__len__() == 0 :
            self._btn_accept.setEnabled(False)
            return
        
        if self._fld_box_path.text().strip().__len__() == 0 :
            self._btn_accept.setEnabled(False)
            return

        if not os.path.isdir(self._fld_box_path.text()) :
            self._btn_accept.setEnabled(False)
            return

        if self._fld_library.text().strip().__len__() == 0 :
            self._btn_accept.setEnabled(False)
            return

        if self._fld_creator.text().strip().__len__() == 0 :
            self._btn_accept.setEnabled(False)
            return

        if self._tbl_inputs.rowCount() == 0 and self._tbl_outputs.rowCount() == 0 :
            self._btn_accept.setEnabled(False)
            return

        self._btn_accept.setEnabled(True)

    @pyqtSlot()
    def _btn_cancel_clicked (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton annuler."""
        self.close()

    @pyqtSlot()
    def _btn_box_path_clicked (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton pour rechercher un chemin."""
        path = QFileDialog.getExistingDirectory(self, "Recherche d'un dossier", os.getcwd())

        if path is None or path == '':
            return

        if not path.endswith('/') :
            path = path + '/'

        self._fld_box_path.setText(path)

    @pyqtSlot()
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(event)

        if event.modifiers() == QtCore.Qt.ControlModifier:

            if event.key() == QtCore.Qt.Key_Z :
                self._actions_holder.undo()
                self._test_data_accept_button()

            elif event.key() == QtCore.Qt.Key_Y :
                self._actions_holder.redo()
                self._test_data_accept_button()

        elif event.modifiers() == QtCore.Qt.NoModifier :

            if event.key() == QtCore.Qt.Key_Delete :

                if self._tbl_inputs.hasFocus():
                    self._btn_input_remove_clicked()

                elif self._tbl_outputs.hasFocus():
                    self._btn_output_remove_clicked()

    @pyqtSlot()
    def _btn_input_add_clicked (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton pour ajouter une entrée."""

        addAction = NewBoxDialogAddAction(self._btn_input_add, 'Entrée', self._tbl_inputs)
        addAction.do()
        self._actions_holder.append(addAction)

        self._test_data_accept_button()
        self._btn_input_remove.setEnabled(self._tbl_inputs.selectedIndexes().__len__() > 0)

    @pyqtSlot()
    def _btn_input_remove_clicked (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton pour supprimer une entrée."""

        if self._tbl_inputs.selectedIndexes().__len__() == 0 :
            return

        removeAction = NewBoxDialogRemoveAction(self._btn_input_remove, self._tbl_inputs)
        removeAction.do()
        self._actions_holder.append(removeAction)
        self._btn_input_remove.setEnabled(self._tbl_inputs.selectedIndexes().__len__() > 0)

        self._test_data_accept_button()

    @pyqtSlot()
    def _btn_output_add_clicked (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton pour ajouter une sortie."""

        addAction = NewBoxDialogAddAction(self._btn_output_add, 'Sortie', self._tbl_outputs)
        addAction.do()
        self._actions_holder.append(addAction)

        self._test_data_accept_button()
        self._btn_output_remove.setEnabled(self._tbl_outputs.selectedIndexes().__len__() > 0)

    @pyqtSlot()
    def _btn_output_remove_clicked (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton pour supprimer une sortie."""

        if self._tbl_outputs.selectedIndexes().__len__() == 0 :
            return

        removeAction = NewBoxDialogRemoveAction(self._btn_output_remove, self._tbl_outputs)
        removeAction.do()
        self._actions_holder.append(removeAction)

        self._test_data_accept_button()
        self._btn_output_remove.setEnabled(self._tbl_outputs.selectedIndexes().__len__() > 0)
        
    @pyqtSlot()
    def _tbl_inputs_selection_changed (self) -> None :
        """Est la méthode appelée lorsque la sélection du tableau des entrée est modifiée."""

        self._btn_input_remove.setEnabled(self._tbl_inputs.selectedIndexes().__len__() > 0)

    @pyqtSlot()
    def _tbl_outputs_selection_changed (self) -> None :
        """Est la méthode appelée lorsque la sélection du tableau des entrée est modifiée."""

        self._btn_output_remove.setEnabled(self._tbl_outputs.selectedIndexes().__len__() > 0)
        
    @pyqtSlot()
    def _tbl_inputs_current_cell_changed (self) -> None :
        """Est la méthode appelée lorsqu'une valeur est modifiée dans le tableau de entrées."""
        LogManager().debug('_tbl_inputs_current_cell_changed')

    @pyqtSlot()
    def _tbl_outputs_current_cell_changed (self) -> None :
        """Est la méthode appelée lorsqu'une valeur est modifiée dans le tableau de sorties."""
        LogManager().debug('_tbl_outputs_current_cell_changed')

    @pyqtSlot()
    def _btn_accept_clicked (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton accepter."""

        boxModel : AbstractBoxModel = None

        lst_inputs : List[BoxInputModel] = []

        for row_index in range(self._tbl_inputs.rowCount()) :

            # ['Nom', 'Type', 'Nombre', 'Valeur']
            index : str =  self._tbl_inputs.item(row_index, 0).text()
            type : str =  self._tbl_inputs.cellWidget(row_index, 1).currentText()
            nbr : str =  self._tbl_inputs.cellWidget(row_index, 2).currentText()
            value : str =  self._tbl_inputs.item(row_index, 3).text()

            lst_inputs.append(BoxInputModel(index, get_data_type(type), QPointF(10, 10 + 40 * row_index), QSizeF(150, 30), 0))


        lst_outputs : List[BoxOutputModel] = []

        for row_index in range(self._tbl_outputs.rowCount()) :
            index : str =  self._tbl_outputs.item(row_index, 0).text()
            type : str =  self._tbl_outputs.cellWidget(row_index, 1).currentText()
            nbr : str =  self._tbl_outputs.cellWidget(row_index, 2).currentText()
            value : str =  self._tbl_outputs.item(row_index, 3).text()

            lst_inputs.append(BoxInputModel(index, get_data_type(type), QPointF(170, 10 + 40 * row_index), QSizeF(150, 30), 0))

        if self._cmb_box_type.currentData() == 0 :
            
            boxModel = BoxCompositeModel(
                self._fld_box_name.text(), 
                self._fld_box_path.text(), 
                self._fld_creator.text(),
                date.today(),
                0.1,
                lst_inputs,
                lst_outputs
            )

        else :

            boxModel = BoxCodeModel(
                self._fld_box_name.text(), 
                self._fld_box_path.text(), 
                self._fld_creator.text(),
                date.today(),
                0.1,
                '',
                lst_inputs,
                lst_outputs
            )

        self._value = boxModel
        self.close()