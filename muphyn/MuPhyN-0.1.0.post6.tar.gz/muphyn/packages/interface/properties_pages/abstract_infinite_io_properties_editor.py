#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QListWidgetItem, QPushButton, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QFormLayout, QListWidget, QAbstractItemView
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor
from muphyn.packages.interface.properties_pages.infinite_io_properties_item import InifiniteIOPropertiesItem

#-----------------------------------
# Class
#-----------------------------------

class AbstractInfiniteIOPropertiesEditor (AbstractPropertiesEditor) :
    """Est la classe abstraite commune aux panneaux de propriétés qui permets d'afficher et modifier les entrées/sorties infinies."""

    # -------------
    # Constants
    # -------------
    ItemHeight: int = InifiniteIOPropertiesItem.ItemHeight * 3
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_model : BoxModel, group_name : str, data_type : DataType, minimum_count: int, maximum_count: int) :
        
        AbstractPropertiesEditor.__init__(self, box_model)

        # Box Model
        self._box_model = box_model

        # Get input group name
        self._group_name = group_name

        # Data Type
        self._data_type = data_type

        # Count
        self._minimum_count = minimum_count
        self._maximum_count = maximum_count

        self._lbl_connection_name_value.setText(group_name)
        self._lbl_data_type_value.setText(self._data_type.__str__())

    # -------------
    # Properties
    # -------------

    @property
    def box_model (self) -> BoxModel :
        """Permet de récuperer le modèle de box modifié par le pannel actuel."""
        return self._box_model
    
    @property
    def group_name (self) -> str :
        """Permet de récuperer le nom de la connexion."""
        return self._group_name

    @property 
    def data_type (self) -> DataType : 
        """Permet de récuperer le type de connexion."""
        return self._data_type

    @property 
    def minimum_count (self) -> int :
        return self._minimum_count

    @property 
    def maximum_count (self) -> int :
        return self._maximum_count

    # -------------
    # Methods
    # -------------

    def init_ui (self) -> None :
        
        self._pnl_form : QWidget = QWidget()
        self._lyt_form : QFormLayout = QFormLayout()
        self._lbl_connection_name : QLabel = QLabel()
        self._lbl_connection_name_value : QLabel = QLabel()
        self._lyt_form.addRow(self._lbl_connection_name, self._lbl_connection_name_value)

        self._lbl_data_type : QLabel = QLabel()
        self._lbl_data_type_value : QLabel = QLabel()
        self._lyt_form.addRow(self._lbl_data_type, self._lbl_data_type_value)

        self._lbl_connection_mode : QLabel = QLabel()
        self._lbl_connection_mode_value : QLabel = QLabel()
        self._lyt_form.addRow(self._lbl_connection_mode, self._lbl_connection_mode_value)

        self._pnl_button_holder : QWidget = QWidget()

        self._btn_add : QPushButton = QPushButton()
        self._btn_add.setBaseSize(100, 22)
        self._btn_add.clicked.connect(self.button_add_click)

        self._btn_remove : QPushButton = QPushButton()
        self._btn_remove.setBaseSize(100, 22)
        self._btn_remove.clicked.connect(self.button_remove_click)

        self._lyt_button_holder : QHBoxLayout = QHBoxLayout()
        self._lyt_button_holder.addWidget(self._btn_add)
        self._lyt_button_holder.addWidget(self._btn_remove)
        self._lyt_button_holder.setAlignment(Qt.AlignRight)

        self._pnl_button_holder.setLayout(self._lyt_button_holder)
        self._lyt_form.addRow(QLabel(), self._pnl_button_holder)

        self._pnl_form.setLayout(self._lyt_form)
        self.layout().addWidget(self._pnl_form)

        self._tbl_connection : QListWidget = QListWidget()
        self._tbl_connection.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.layout().addWidget(self._tbl_connection)
        self.layout().setContentsMargins(0, 0, 0, 0)


    def translate_ui (self) -> None :

        self._lbl_connection_name.setText(QCoreApplication.translate(self.objectName(), u'Name : ', None))
        self._lbl_data_type.setText(QCoreApplication.translate(self.objectName(), u'Data type : ', None))
        self._lbl_connection_mode.setText(QCoreApplication.translate(self.objectName(), u'Connexion mode : ', None))
        self._btn_add.setText(QCoreApplication.translate(self.objectName(), u"+", None))
        self._btn_remove.setText(QCoreApplication.translate(self.objectName(), u"-", None))

    def button_add_click (self) -> None : 
        """Est la méthode appelée lorsque l'utilisateur veut cliquer sur le bouton ajouter."""
        LogManager().debug('btn add clicked')
        
    def button_remove_click (self) -> None : 
        """Est la méthode appelée lorsque l'utilisateur veut cliquer sur le bouton ajouter."""
        LogManager().debug('btn remove clicked')

    def create_layout (self) -> None : 
        """Permet de créer le layout pour l'affichage actuel."""
        return QVBoxLayout(self)

        
    def recompute_connection_numbers (self) -> None : 
        
        for input_index in range(self._tbl_connection.count()) :
            item = self._tbl_connection.item(input_index)
            item_widget : InifiniteIOPropertiesItem = self._tbl_connection.itemWidget(item)
            item_widget.number = input_index + 1
