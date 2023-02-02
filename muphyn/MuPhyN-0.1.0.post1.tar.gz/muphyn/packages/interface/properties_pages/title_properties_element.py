#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor
from muphyn.packages.interface.widgets.BaseWidgets.Label import TitlePropertyLabel

#-----------------------------------
# Imports
#-----------------------------------

class TitlePropertiesElement (AbstractPropertiesEditor) :
    """Est la classe qui permet d'afficher un titre dans la liste des propriétées."""

    # -------------
    # Constructors
    # -------------
    
    def __init__ (self, title : str, parent : QWidget = None) :

        self._title = title

        AbstractPropertiesEditor.__init__(self, None)
        
    # -------------
    # Properties
    # -------------

    @property
    def title (self) -> str :
        """Permet de récuperer le titre affiché."""
        return self._title 

    # -------------
    # Methods
    # -------------

    def init_ui (self) -> None : 

        self._lbl_title: TitlePropertyLabel = TitlePropertyLabel()
        self.layout().addWidget(self._lbl_title)

    def translate_ui (self) -> None :
        
        self._lbl_title.setText(QCoreApplication.translate(self.objectName(), self.title, None))

    def create_layout(self) -> None:
        return QHBoxLayout()