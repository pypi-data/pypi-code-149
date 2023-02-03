#-----------------------------------
# Imports
#-----------------------------------

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, QRect, Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout

from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor

#-----------------------------------
# Class
#-----------------------------------

class UnknownPropertiesEditor (AbstractPropertiesEditor) :
    """Est la page affichées quand aucune autre page de propriétés ne peut être affichées."""
        
    # -------------
    # Constructors
    # -------------
    
    def __init__ (self) :

        AbstractPropertiesEditor.__init__(self, None)

    # -------------
    # Methods
    # -------------

    def resizeEvent (self, event : QtGui.QResizeEvent) -> None :
        self.redraw_ui()
        return super().resizeEvent(event)

    def init_ui (self) :

        if not self.objectName():
            self.setObjectName(u"pnl_unknown_properties")

        self._lbl_unknown : QLabel = QLabel(self)
        self._lbl_unknown.setAlignment(Qt.AlignCenter)
    
        self.redraw_ui()

    def translate_ui (self) -> None :

        self._lbl_unknown.setText(QCoreApplication.translate(self.objectName(), u"No selected item", None))

    def redraw_ui (self) -> None :

        self._lbl_unknown.setGeometry(QRect(0, 10, self.width(), 35))

        self._height = 40

    def create_layout (self) -> None : 
        """Permet de créer le layout pour l'affichage actuel."""
        return QVBoxLayout(self)