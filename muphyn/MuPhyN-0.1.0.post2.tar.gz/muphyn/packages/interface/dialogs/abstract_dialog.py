#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog

#-----------------------------------
# Class
#-----------------------------------

class AbstractDialog (QDialog) :
    """Est la classe abstraite commune aux dialogues affichés par dessus la fenêtre principale."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, name : str, title : str) :
        QDialog.__init__(self)

        self.setWindowTitle(title)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        if not self.objectName():
            self.setObjectName('_dlg_' + name)
        
        self._name : str = name
        self._dialog_holder : Any = dialog_holder
        self._value : Any = None

    # -------------
    # Properties
    # -------------

    @property
    def name (self) -> str:
        """Permet de récuperer le nom de la boîte de dialogue."""
        return self._name

    @property
    def value (self) -> Any:
        """Permet de récuperer la valeur de la boite de dialogue."""
        return self._value

    # -------------
    # Methods
    # -------------

    def hideEvent (self, event: QtGui.QHideEvent) -> None:
        """Est la méthode appelée lorsque la boite de dialogue est fermée."""
        super().hideEvent(event)

        if not self.isModal():
            self._dialog_holder._dialog_closed(self, None)