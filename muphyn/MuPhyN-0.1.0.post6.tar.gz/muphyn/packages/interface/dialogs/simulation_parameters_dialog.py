#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from PyQt5.QtWidgets import QLabel, QFormLayout, QComboBox, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout

from muphyn.packages.core.plci_core_scheduler_params import SchedulerParams
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.core.scheduler_library.scheduler_library_data import SchedulerData
from muphyn.packages.interface.models.dbl_spin_box import DblSpinBox
from muphyn.packages.interface.dialogs.abstract_dialog import AbstractDialog
from muphyn.packages.interface.models.editable_models.scheduler_model import SchedulerModel
from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel
from muphyn.packages.interface.widgets.BaseWidgets.Button import PlainButton
from muphyn.packages.interface.widgets.BaseWidgets.Label import PropertyLabel
from muphyn.packages.interface.utils.interface_constants import ApplicationWindowTitle

#-----------------------------------
# Class
#-----------------------------------

class SimulationParametersDialog (AbstractDialog) :
    """Est la classe de dialogue qui permet de modifier les paramètres de la simulation."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, simulation_model : SimulationModel, schedulers_libraries : SchedulersLibraries) :

        AbstractDialog.__init__(self, dialog_holder, 'simulation_parameters_dialog', QCoreApplication.translate(u'dlg_simulation_parameter', f'{ApplicationWindowTitle} - Simulation parameters', None))

        self.setFixedSize(370, 160)
        self.init_ui()
        self.tranlsate_ui()

        self._simulation_model = None
        self._last_selected_index = -1
        self._schedulers_libraries = schedulers_libraries

        for scheduler_data in self._schedulers_libraries.schedulers :
            self._cmb_scheduler.addItem(scheduler_data.__str__(), scheduler_data)

        self.simulation_model = simulation_model

    # -------------
    # Properties
    # -------------

    @property 
    def simulation_model (self) -> SimulationModel :
        """Permet de récuperer le modèle de simulation."""
        return self._simulation_model

    @simulation_model.setter
    def simulation_model (self, simulation_model_ : SimulationModel) -> None :
        """Permet de modifier le modèle de simulation."""

        self._simulation_model = simulation_model_

        if self._simulation_model is None : 
            self._btn_accept.setEnabled(False)
            
            self._spn_simulation_tick.setEnabled(False)
            self._spn_simulation_tick.setValue(0)

            self._spn_simulation_time.setEnabled(False)
            self._spn_simulation_time.setValue(0)

            self._cmb_scheduler.setEnabled(False)
            if self._cmb_scheduler.count() > 0 :
                self._cmb_scheduler.setCurrentIndex(0)

        else : 
            
            self._spn_simulation_tick.setEnabled(True)
            self._spn_simulation_time.setEnabled(True)
            self._cmb_scheduler.setEnabled(True)
            
            if self._simulation_model.scheduler_model is None :
                self._spn_simulation_tick.setValue(10)
                self._spn_simulation_time.setValue(0.01)

            else : 
                if self._simulation_model.scheduler_model.params is None : 
                    self._spn_simulation_tick.setValue(10)
                    self._spn_simulation_time.setValue(0.01)
                    
                else :
                    self._spn_simulation_tick.setValue(self._simulation_model.scheduler_model.params.step_time)
                    self._spn_simulation_time.setValue(self._simulation_model.scheduler_model.params.stop_time)


            if self._cmb_scheduler.count() > 0 :

                self._cmb_scheduler.setCurrentIndex(0)

                if not(self._simulation_model.scheduler_model is None) :

                    for index in range(self._cmb_scheduler.count()) :
                        item_text = self._cmb_scheduler.itemText(index)
                        if  item_text == self._simulation_model.scheduler_model.__str__() :
                            self._last_selected_index = index
                            self._cmb_scheduler.setCurrentIndex(index)
                            break
        
        self.check_changed()

    # -------------
    # Methods
    # -------------

    @pyqtSlot()
    def button_accept_clicked (self) -> None :
        """Est la méthode appelée quand l'utilisateur clique sur le bouton accepter du dialogue."""
        
        scheduler_data : SchedulerData = self._cmb_scheduler.currentData() 
        scheduler_params = SchedulerParams(self._spn_simulation_time.value(), self._spn_simulation_tick.value())
        self._value = SchedulerModel(scheduler_data.scheduler_library, scheduler_data.scheduler_name, scheduler_params)
        self.close()

    @pyqtSlot()
    def button_cancel_clicked (self) -> None : 
        """Est la méthode appelée quand l'utilisateur clique sur le bouton annuler du dialogue."""
        self.close()

    @pyqtSlot()
    def check_changed (self) -> None : 
        """Est la méthode appelée quand l'utilisateur modifie un élément graphique. La méthode débloque alors le bouton accepter si il y a quelque chose de modifié."""

        if self.simulation_model is None or not(self._cmb_scheduler.count() > 0) :
            self._btn_accept.setEnabled(False)
            return

        if self.simulation_model.scheduler_model is None : 

            if not(self._cmb_scheduler.currentIndex() == -1) :
                self._btn_accept.setEnabled(True)
            
            else :
                self._btn_accept.setEnabled(False)

            return

        if self.simulation_model.scheduler_model.params is None : 
            self._btn_accept.setEnabled(True)
            return 

        # If Simulation Duration time is zero or Step time is zero → invalid value
        if self._spn_simulation_tick.value() == 0 or self._spn_simulation_time.value() == 0 :
            self._btn_accept.setEnabled(False)
            return

        # If Step time is greater than simulation time → invalid value
        if self._spn_simulation_time.value()  < self._spn_simulation_tick.value() : 
            self._btn_accept.setEnabled(False)
            return

        # If Scheduler is different from set parameters → enable button
        if self.simulation_model.scheduler_model.completeName != self._cmb_scheduler.currentText():
            self._btn_accept.setEnabled(True)
            return

        # If Step Time is different from set parameters → enable button
        if self.simulation_model.scheduler_model.params.step_time != self._spn_simulation_tick.value() :
            self._btn_accept.setEnabled(True)
            return

        # If Stop Time is different from set parameters → enable button
        if self.simulation_model.scheduler_model.params.stop_time != self._spn_simulation_time.value() :
            self._btn_accept.setEnabled(True)
            return

        # Disable accept button
        self._btn_accept.setEnabled(False)

    def init_ui (self) -> None :
        """Est la méthode appelée pour initialiser les éléments de l'interface graphique."""

        if self.objectName() is None : 
            self.setObjectName('dlg_simulation_parameter')

        mainLayout = QVBoxLayout()

        # Options Layout
        optionsLayout = QGridLayout()

        # Buttons Layout
        buttonsLayout = QGridLayout()
        buttonsLayout.setColumnMinimumWidth(1, 90)
        buttonsLayout.setColumnMinimumWidth(2, 90)
        buttonsLayout.setHorizontalSpacing(5)

        # Scheduler
        self._lbl_scheduler : PropertyLabel = PropertyLabel()
        self._cmb_scheduler : QComboBox = QComboBox()
        self._cmb_scheduler.currentIndexChanged.connect(self.check_changed)

        # Time Value
        self._lbl_simulation_time : PropertyLabel = PropertyLabel()
        self._spn_simulation_time : DblSpinBox = DblSpinBox()
        self._spn_simulation_time.setMinimum(0)
        self._spn_simulation_time.valueChanged.connect(self.check_changed)

        # Step Time Value
        self._lbl_simulation_tick : PropertyLabel = PropertyLabel()
        self._spn_simulation_tick : DblSpinBox = DblSpinBox()
        self._spn_simulation_tick.setMinimum(0)
        self._spn_simulation_tick.valueChanged.connect(self.check_changed)

        # Accept button
        self._btn_accept : QPushButton = PlainButton()
        self._btn_accept.clicked.connect(self.button_accept_clicked)

        # Cancel Button
        self._btn_cancel : QPushButton = QPushButton()
        self._btn_cancel.clicked.connect(self.button_cancel_clicked)
        
        # Add option widgets to layout
        optionsLayout.addWidget(self._lbl_scheduler, 0, 0)
        optionsLayout.addWidget(self._cmb_scheduler, 0, 1)
        optionsLayout.addWidget(self._lbl_simulation_time, 1, 0)
        optionsLayout.addWidget(self._spn_simulation_time, 1, 1)
        optionsLayout.addWidget(self._lbl_simulation_tick, 2, 0)
        optionsLayout.addWidget(self._spn_simulation_tick, 2, 1)
        optionsLayout.setColumnStretch(1, 1)

        # Add buttons to layout
        buttonsLayout.addWidget(self._btn_accept, 0, 1)
        buttonsLayout.addWidget(self._btn_cancel, 0, 2)
        buttonsLayout.setColumnStretch(0, 1)

        # Add Options Layout to Main Layout
        mainLayout.addLayout(optionsLayout, 1)

        # Add Buttons Layout to Main Layout
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

    def tranlsate_ui (self) -> None : 
        """Est la méthode pour traduire les éléments de l'interface graphique."""

        self._lbl_scheduler.setText(QCoreApplication.translate(self.objectName(), u'Scheduler : ', None))
        self._lbl_simulation_time.setText(QCoreApplication.translate(self.objectName(), u'Duration time [s] :', None))
        self._lbl_simulation_tick.setText(QCoreApplication.translate(self.objectName(), u'Step time [s] :', None))
        self._btn_accept.setText(QCoreApplication.translate(self.objectName(), u'Accept', None))
        self._btn_cancel.setText(QCoreApplication.translate(self.objectName(), u'Cancel', None))