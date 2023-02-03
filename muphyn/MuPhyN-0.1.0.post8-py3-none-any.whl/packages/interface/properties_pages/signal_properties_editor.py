#-----------------------------------
# Imports
#-----------------------------------

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from PyQt5.QtWidgets import QComboBox, QLabel, QLineEdit, QSlider
from muphyn.packages.interface.models.dbl_spin_box import DblSpinBox
from muphyn.packages.interface.models.signals_model.signal_link_model import SignalLinkModel
from muphyn.packages.interface.models.links_model.link_type import LinkType
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor
from muphyn.packages.interface.widgets.BaseWidgets.Label import PropertyLabel

#-----------------------------------
# Class
#-----------------------------------

sldr_factor = 100.0

class SignalPropertiesEditor (AbstractPropertiesEditor) : 
    """Est la classe qui affiche une page capable de modifier les propriétés d'un lien."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, signal_model : SignalLinkModel) :
        
        AbstractPropertiesEditor.__init__(self, signal_model)

        self._value_semaphore : bool = True
        self._link_value_semaphore : bool = False
        self._signal_model : SignalLinkModel = None
        self.signal_model = signal_model
        self._value_semaphore : bool = False
        
    # -------------
    # Properties
    # -------------
    
    @property
    def signal_model (self) -> SignalLinkModel :
        """Permet de récuperer le signal modifié par la fenêtre de propriétés."""
        return self._signal_model
    
    @signal_model.setter
    def signal_model (self, signal_model_ : SignalLinkModel) -> None :
        """Permet de modifier le signal modifié par la fenêtre de propriétés."""

        if not(self._signal_model is None) :
            self._signal_model.param_changed.disconnect(self.signal_model_param_changed)

        self._signal_model = signal_model_
        self._model = signal_model_

        if self._signal_model == None :
            self._fld_texte.setEnabled(False)
            self._fld_texte.setText('')
            self._cmb_color.setEnabled(False)
            self._cmb_color.setCurrentIndex(0)
            self._cmb_link_type.setEnabled(False)
            self._cmb_link_type.setCurrentIndex(0)
            self._spn_link_value.setEnabled(False)
            self._spn_link_value.setValue(0)
            self._sldr_link_value.setEnabled(False)
            self._sldr_link_value.setValue(0)
            self._lbl_data_type_value.setText('')

        else :
            self._fld_texte.setEnabled(True)
            self._fld_texte.setText(self._signal_model.text)
            
            self._cmb_color.setEnabled(False)
            self._cmb_color.setCurrentIndex(0)

            self._cmb_link_type.setEnabled(True)
            if self._signal_model.link_type == LinkType.SQUARE :
                self._cmb_link_type.setCurrentIndex(0)
            elif self._signal_model.link_type == LinkType.CURVED :
                self._cmb_link_type.setCurrentIndex(1)

            self._link_value_semaphore : bool = True
            self._spn_link_value.setEnabled(True)
            self._spn_link_value.setValue(self._signal_model.link_value)
            
            self._sldr_link_value.setEnabled(True)
            self._sldr_link_value.setValue(int(self._signal_model.link_value * sldr_factor))
            self._link_value_semaphore : bool = False

            self._lbl_data_type_value.setText(self._signal_model.data_type.__str__())
            
            self._signal_model.param_changed.connect(self.signal_model_param_changed)

    # -------------
    # Methods
    # -------------

    def signal_model_param_changed (self, signal_model, param_name, old_value, new_value) -> None :
        """Est la méthode appelée lorsqu'un des paramètres du lien est modifié."""

        if not(signal_model == self.signal_model) :
            return

        if not(param_name == 'link_value' or param_name == 'link_type' or param_name == 'text' or param_name == 'color') :
            return

        self._value_semaphore = True

        if param_name == 'link_value' :
            self._sldr_link_value.setValue(int(new_value * sldr_factor))
            self._spn_link_value.setValue(new_value)

        elif param_name == 'link_type' :
            if new_value == LinkType.SQUARE : 
                self._cmb_link_type.setCurrentIndex(0)
            elif new_value == LinkType.CURVED :
                self._cmb_link_type.setCurrentIndex(1)

        elif param_name == 'text' :
            self._fld_texte.setText(new_value)

        elif param_name == 'color' :
            ...

        self._value_semaphore = False

    @pyqtSlot()
    def sldr_link_value_changed (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur modifie la valeur du lien via le slider."""

        if self._value_semaphore :
            return

        if self._link_value_semaphore :
            return

        if self._signal_model is None : 
            return

        self._link_value_semaphore = True
        self._signal_model.action_param_semaphore = True

        new_value = float(self._sldr_link_value.value()) / sldr_factor
        old_value = self.signal_model.link_value
        param_name = 'link_value'

        self.actions_generator(old_value, new_value, param_name)

        self._signal_model.link_value = new_value
        self._spn_link_value.setValue(self._signal_model.link_value)
        self._signal_model.self_update()

        self._signal_model.action_param_semaphore = False
        self._link_value_semaphore = False

    @pyqtSlot()
    def spn_link_value_changed (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur modifie la valeur du lien via le spinner."""

        if self._value_semaphore :
            return

        if self._link_value_semaphore :
            return

        if self._signal_model is None : 
            return

        self._link_value_semaphore = True
        self._signal_model.action_param_semaphore = True

        new_value = self._spn_link_value.value()
        old_value = self.signal_model.link_value
        param_name = 'link_value'

        self.actions_generator(old_value, new_value, param_name)

        self._signal_model.link_value = new_value
        self._sldr_link_value.setValue(int(new_value * sldr_factor))
        self._signal_model.self_update()

        self._signal_model.action_param_semaphore = False
        self._link_value_semaphore = False

    def cmb_link_type_value_changed (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur modifie le type de lien du signal."""

        if self._value_semaphore :
            return

        if self._cmb_link_type.currentIndex() == 0 :
            new_value = LinkType.SQUARE

        elif self._cmb_link_type.currentIndex() == 1 :
            new_value = LinkType.CURVED

        self._signal_model.action_param_semaphore = True
        
        old_value = self.signal_model.link_type
        param_name = 'link_type'

        self.actions_generator(old_value, new_value, param_name)

        self._signal_model.link_type = new_value
        self._signal_model.self_update()

        self._signal_model.action_param_semaphore = False

    def fld_texte_text_changed (self) -> None : 
        """Est la méthode appelée lorsque l'utilisateur modifie le texte du signal."""

        if self._value_semaphore :
            return

        self._signal_model.action_param_semaphore = True

        new_value = self._fld_texte.text()
        old_value = self._signal_model.text
        param_name = 'text'

        self.actions_generator(old_value, new_value, param_name)

        self._signal_model.text = new_value

        self._signal_model.action_param_semaphore = False

    def init_ui (self) :

        if not self.objectName():
            self.setObjectName(u"pnl_signal_properties")
        
        # Texte
        self._lbl_texte = PropertyLabel()
        self._lbl_texte.setObjectName(u"_lbl_texte")

        self._fld_texte = QLineEdit()
        self._fld_texte.setObjectName(u"_fld_texte")
        self._fld_texte.textChanged.connect(self.fld_texte_text_changed)

        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_texte, row, 0)
        self.layout().addWidget(self._fld_texte, row, 1)

        # Color picker
        self._lbl_color = PropertyLabel()
        self._lbl_color.setObjectName(u"_lbl_color")

        self._cmb_color = QComboBox()
        self._cmb_color.setObjectName(u"_cmb_color")
        self._cmb_color.addItem('black')
        
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_color, row, 0)
        self.layout().addWidget(self._cmb_color, row, 1)

        # Link type
        self._lbl_type_of_link = PropertyLabel()
        self._lbl_type_of_link.setObjectName(u"_lbl_type_of_link")

        self._cmb_link_type = QComboBox()
        self._cmb_link_type.setObjectName(u"_cmb_link_type")
        self._cmb_link_type.addItem('Square')
        self._cmb_link_type.addItem('Curved')
        self._cmb_link_type.currentIndexChanged.connect(self.cmb_link_type_value_changed)
        
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_type_of_link, row, 0)
        self.layout().addWidget(self._cmb_link_type, row, 1)

        # Link value
        self._lbl_link_value = PropertyLabel()
        self._lbl_link_value.setObjectName(u"_lbl_link_value")

        self._sldr_link_value = QSlider()
        self._sldr_link_value.setObjectName(u"_sldr_link_values")
        self._sldr_link_value.setOrientation(Qt.Horizontal)
        self._sldr_link_value.setMinimum(0)
        self._sldr_link_value.setMaximum(int(sldr_factor))
        self._sldr_link_value.valueChanged.connect(self.sldr_link_value_changed)

        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_link_value, row, 0)
        self.layout().addWidget(self._sldr_link_value, row, 1)

        self._spn_link_value = DblSpinBox()
        self._spn_link_value.setObjectName(u"_spn_link_value")
        self._spn_link_value.setMinimum(0)
        self._spn_link_value.setMaximum(1)
        self._spn_link_value.setDecimals(2)
        self._spn_link_value.valueChanged.connect(self.spn_link_value_changed)

        row = self.layout().rowCount()
        self.layout().addWidget(PropertyLabel(), row, 0)
        self.layout().addWidget(self._spn_link_value, row, 1)

        # Data type 
        self._lbl_data_type = PropertyLabel()
        self._lbl_data_type.setObjectName(u"_lbl_data_type")

        self._lbl_data_type_value = PropertyLabel()
        self._lbl_data_type_value.setObjectName(u"_lbl_data_type_value")
        
        row = self.layout().rowCount()
        self.layout().addWidget(self._lbl_data_type, row, 0)
        self.layout().addWidget(self._lbl_data_type_value, row, 1)

    def translate_ui (self) -> None :
        self._lbl_texte.setText(QCoreApplication.translate(self.objectName(), u"Texte : ", None))
        self._lbl_color.setText(QCoreApplication.translate(self.objectName(), u"Couleur : ", None))
        self._lbl_type_of_link.setText(QCoreApplication.translate(self.objectName(), u"Type :", None))
        self._lbl_link_value.setText(QCoreApplication.translate(self.objectName(), u"Link value : ", None))
        self._lbl_data_type.setText(QCoreApplication.translate(self.objectName(), u"Data Type : ", None))