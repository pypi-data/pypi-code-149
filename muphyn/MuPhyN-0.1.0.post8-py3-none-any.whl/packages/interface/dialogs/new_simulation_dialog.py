#-----------------------------------
# Imports
#-----------------------------------

import os
from datetime import date
from typing import Any

from PyQt5.QtCore import QCoreApplication, QRect, pyqtSlot
from PyQt5.QtWidgets import QComboBox, QFileDialog, QFrame, QLabel, QLineEdit, QGridLayout, QVBoxLayout, QPushButton, QWidget
from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams

from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.core.scheduler_library.scheduler_library_data import SchedulerData
from muphyn.packages.interface.models.dbl_spin_box import DblSpinBox
from muphyn.packages.interface.models.editable_models.scheduler_model import SchedulerModel
from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from .abstract_dialog import AbstractDialog
from muphyn.packages.interface.widgets.BaseWidgets.Button import PlainButton
from muphyn.packages.interface.widgets.BaseWidgets.Label import PropertyLabel
from muphyn.packages.interface.utils.interface_constants import ApplicationWindowTitle

#-----------------------------------
# Class
#-----------------------------------

class NewSimulationDialog (AbstractDialog) :
    """Est la classe permettant d'afficher une boîte de dialogue capable de créer une simulation."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, schedulers_libraries : SchedulersLibraries) :
        AbstractDialog.__init__(self, dialog_holder, 'new_simulation', 'Nouvelle Simulation')

        self.setFixedSize(480, 240)
        self._init_ui()
        self._test_data_accept_button()
        
        self._schedulers_libraries = schedulers_libraries

        for scheduler_data in self._schedulers_libraries.schedulers :
            self._cmb_scheduler.addItem(scheduler_data.__str__(), scheduler_data)


    # -------------
    # Methods
    # -------------

    @pyqtSlot()
    def _btn_cancel_click (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton annuler."""
        self.close()
        
    @pyqtSlot()
    def _btn_simulation_path_click (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton rechercher."""
        path = QFileDialog.getExistingDirectory(self, f"{ApplicationWindowTitle} - Select folder", os.getcwd())

        if path is None or path == '':
            return

        if not path.endswith('/') :
            path = path + '/'

        self._fld_simulation_path.setText(path)

    @pyqtSlot()
    def _test_data_accept_button (self) -> None :
        """Permet de vérifier si les données entrées sont correctes dans le but de débloquer le bouton accepter."""
        
        if self._fld_simulation_name.text().strip().__len__() == 0 :
            self._btn_accept.setEnabled(False)
            return

        if not os.path.isdir(self._fld_simulation_path.text()) :
            self._btn_accept.setEnabled(False)
            return

        if self._cmb_scheduler.currentIndex() == -1 :
            self._btn_accept.setEnabled(False)
            return
        
        if self._spn_simulation_timing.value() == 0 :
            self._btn_accept.setEnabled(False)
            return

        if self._spn_simulation_step.value() == 0 :
            self._btn_accept.setEnabled(False)
            return
            
        self._btn_accept.setEnabled(True)


    def _init_ui (self) :

        # Base Layout
        baseLayout = QVBoxLayout()

        # Options Layout
        optionsLayout = QGridLayout()
        optionsLayout.setColumnMinimumWidth(2, 90)
        optionsLayout.setSpacing(5)

        # Buttons Layout
        buttonsLayout = QGridLayout()
        buttonsLayout.setColumnMinimumWidth(1, 90)
        buttonsLayout.setColumnMinimumWidth(2, 90)
        buttonsLayout.setHorizontalSpacing(5)

        # Simulation Name
        self._lbl_simulation_name = PropertyLabel()
        self._lbl_simulation_name.setObjectName("_lbl_simulation_name")

        self._fld_simulation_name = QLineEdit()
        self._fld_simulation_name.setObjectName("_fld_simulation_name")
        self._fld_simulation_name.textChanged.connect(self._test_data_accept_button)

        # Simulation Path
        self._lbl_simulation_path = PropertyLabel()
        self._lbl_simulation_path.setObjectName("_lbl_simulation_path")
        
        self._fld_simulation_path = QLineEdit()
        self._fld_simulation_path.setObjectName("_fld_simulation_path")
        self._fld_simulation_path.textChanged.connect(self._test_data_accept_button)

        self._btn_simulation_path = QPushButton()
        self._btn_simulation_path.setObjectName("_btn_simulation_path")
        self._btn_simulation_path.clicked.connect(self._btn_simulation_path_click)

        # Separator
        self._ln_separator = QFrame()
        self._ln_separator.setObjectName("_ln_separator")
        self._ln_separator.setFrameShape(QFrame.HLine)
        self._ln_separator.setFrameShadow(QFrame.Sunken)

        # Scheduler
        self._lbl_scheduler = PropertyLabel()
        self._lbl_scheduler.setObjectName("_lbl_scheduler")

        self._cmb_scheduler = QComboBox()
        self._cmb_scheduler.setObjectName("_cmb_scheduler")
        self._cmb_scheduler.currentIndexChanged.connect(self._test_data_accept_button)

        # Simulation Time
        self._lbl_simulation_timing = PropertyLabel()
        self._lbl_simulation_timing.setObjectName("_lbl_simulation_timing")

        self._spn_simulation_timing = DblSpinBox()
        self._spn_simulation_timing.setObjectName("_spn_simulation_timing")
        self._spn_simulation_timing.setMinimum(0)
        self._spn_simulation_timing.setValue(5.0)
        self._spn_simulation_timing.valueChanged.connect(self._test_data_accept_button)

        # Step Time
        self._lbl_simulation_step = PropertyLabel()
        self._lbl_simulation_step.setObjectName("_lbl_simulation_step")

        self._spn_simulation_step = DblSpinBox()
        self._spn_simulation_step.setObjectName("_spn_simulation_step")
        self._spn_simulation_step.setMinimum(0)
        self._spn_simulation_step.setValue(0.001)
        self._spn_simulation_step.setSingleStep(self._spn_simulation_step.value())
        self._spn_simulation_step.valueChanged.connect(self._test_data_accept_button)

        # Confirm Button
        self._btn_accept = PlainButton()
        self._btn_accept.setObjectName("_btn_accept")
        self._btn_accept.clicked.connect(self._btn_accept_click)

        # Cancel Button
        self._btn_cancel = QPushButton()
        self._btn_cancel.setObjectName("_btn_cancel")
        self._btn_cancel.clicked.connect(self._btn_cancel_click)

        # Add option widgets to layout
        optionsLayout.addWidget(self._lbl_simulation_name, 0, 0)
        optionsLayout.addWidget(self._fld_simulation_name, 0, 1)
        optionsLayout.addWidget(self._lbl_simulation_path, 1, 0)
        optionsLayout.addWidget(self._fld_simulation_path, 1, 1)
        optionsLayout.addWidget(self._btn_simulation_path, 1, 2)
        optionsLayout.addWidget(self._ln_separator, 2, 0, 1, 3)
        optionsLayout.addWidget(self._lbl_scheduler, 3, 0)
        optionsLayout.addWidget(self._cmb_scheduler, 3, 1)
        optionsLayout.addWidget(self._lbl_simulation_timing, 4, 0)
        optionsLayout.addWidget(self._spn_simulation_timing, 4, 1)
        optionsLayout.addWidget(self._lbl_simulation_step, 5, 0)
        optionsLayout.addWidget(self._spn_simulation_step, 5, 1)

        # Add buttons to layout
        buttonsLayout.addWidget(self._btn_accept, 0, 1)
        buttonsLayout.addWidget(self._btn_cancel, 0, 2)
        buttonsLayout.setColumnStretch(0, 1)

        # Add layouts to main layout
        baseLayout.addLayout(optionsLayout)
        baseLayout.addLayout(buttonsLayout)
        
        # Set Base Layout of page
        self.setLayout(baseLayout)

        self.retranslateUi(self)

    def retranslateUi (self, Dialog) -> None :
        self.setWindowTitle(QCoreApplication.translate(self.objectName(), f"{ApplicationWindowTitle} - New Simulation", None))
        self._btn_accept.setText(QCoreApplication.translate("_dlg_new_simulation", "Accept", None))
        self._btn_cancel.setText(QCoreApplication.translate("_dlg_new_simulation", "Cancel", None))
        self._btn_simulation_path.setText(QCoreApplication.translate("_dlg_new_simulation", "Select Folder", None))
        self._lbl_simulation_name.setText(QCoreApplication.translate("_dlg_new_simulation", "Projet name :", None))
        self._lbl_simulation_path.setText(QCoreApplication.translate("_dlg_new_simulation", "Project folder :", None))
        self._lbl_scheduler.setText(QCoreApplication.translate("_dlg_new_simulation", "Scheduler :", None))
        self._lbl_simulation_timing.setText(QCoreApplication.translate("_dlg_new_simulation", "Duration time [s] :", None))
        self._lbl_simulation_step.setText(QCoreApplication.translate("_dlg_new_simulation", "Step time [s] :", None))

    @pyqtSlot()
    def _btn_accept_click (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur clique sur le bouton accepter."""

        scheduler_data : SchedulerData = self._cmb_scheduler.currentData()  
        scheduler_params : SchedulerParams = SchedulerParams(self._spn_simulation_timing.value(), self._spn_simulation_step.value())
        scheduler_model : SchedulerModel = SchedulerModel(scheduler_data.scheduler_library, scheduler_data.scheduler_name, scheduler_params)
        self._value = SimulationModel(self._fld_simulation_name.text(), self._fld_simulation_path.text(), '', date.today(), 0.1, scheduler_model, [])
        self.close()