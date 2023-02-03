#-----------------------------------
# Imports
#-----------------------------------

# PyQt5 imports
from typing import Any
from PyQt5.QtCore import QCoreApplication 
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout

# Project imports
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.models.signals_model.abstract_connection_model import AbstractConnectionModel
from muphyn.packages.interface.widgets.BaseWidgets.Label import PropertyLabel

#-----------------------------------
# Class
#-----------------------------------

class InifiniteIOPropertiesItem (QWidget) :
    """Est l'item qui permet d'afficher des éléments visuels pour modifier une entrée/sortie dans la liste des entrées/sorites infinies."""

    # -------------
    # Constants
    # -------------
    ItemHeight: int = 40

    # -------------
    # Constructors
    # -------------

    def __init__ (self, number : int, connection_model : AbstractConnectionModel, parent : QWidget = None) :

        QWidget.__init__(self, parent)

        self._connection_model = connection_model

        self.init_ui()
        self.translate_ui()

        # Set field text
        self._fld_text.setText(connection_model.text)
        self.number = number

        # Connect text change
        self.connection_model.param_changed.connect(self.on_text_changed)

    # -------------
    # Methods
    # -------------

    @property
    def number (self) -> int :
        """Permet de récuperer le nombre de l'item."""
        return self._number

    @number.setter
    def number (self, number_ : int) -> None :
        """Permet de modifier le nombre de l'item."""
        self._number = number_
        self._lbl_index.setText(str(self._number) + ' : ')

    @property
    def connection_model (self) -> AbstractConnectionModel :
        """Permet de récuperer le modèle de la connexion."""
        return self._connection_model

    # -------------
    # Methods
    # -------------

    def init_ui (self) -> None :
        """Permet de créer et dessinier l'interface graphique."""

        self._lyt_ui : QHBoxLayout = QHBoxLayout()

        self._lbl_index : PropertyLabel = PropertyLabel()

        self._fld_text : QLineEdit = QLineEdit()
        self._fld_text.editingFinished.connect(self.text_field_edited)

        self._lyt_ui.addWidget(self._lbl_index)
        self._lyt_ui.addWidget(self._fld_text)

        self.setLayout(self._lyt_ui)

    def translate_ui (self) -> None :
        """Permet de traduire les éléments de l'interface graphique."""

        self._fld_text.setPlaceholderText(QCoreApplication.translate(self.objectName(), u"Texte", None))

    def text_field_edited (self) -> None : 
        """Est la méthode appelée lorsque l'utilisateur termine de modifier le champ d'étition du texte de l'entrée."""
        LogManager().debug(f'text field edited {self.number} new text : {self._fld_text.text()}')
        self._connection_model.text = self._fld_text.text()
        self._connection_model.name = self._fld_text.text()

    def on_text_changed(self, connection_model: AbstractConnectionModel, param_name: str, old_value: Any, new_value: Any) -> None:
        if param_name == "text":
            self._fld_text.setText(new_value)