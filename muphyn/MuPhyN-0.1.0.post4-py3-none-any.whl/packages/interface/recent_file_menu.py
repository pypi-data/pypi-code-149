#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtWidgets import QWidget, QAction
from PyQt5.QtCore import pyqtSlot

#-----------------------------------
# Class
#-----------------------------------

class RecentFileMenu (QAction) :
    """Est le menu qui permet d'afficher et de gérer les fichiers récents."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, parent : QWidget, path : str, open_method : callable) :

        QAction.__init__(self, parent)
        self.setText(path)
        self.triggered.connect(self.click)
        self._path = path
        self._open_method = open_method

    # -------------
    # Properties
    # -------------

    @property
    def path (self) -> str :
        """Permet de récuperer le chemin pointé par le menu de fichier récent."""
        return self._path 

    @property
    def open_method (self) -> callable :
        """Permet de récuperer la méthode appelée pour ouvrir un fichier."""
        return self._open_method

    # -------------
    # Methods
    # -------------

    @pyqtSlot()
    def click (self) :
        """Est la méthode appelée lorsque l'utilisateur clique sur l'élément de fichier récent."""
        self._open_method(self._path)
