#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QLabel

#-----------------------------------
# Class
#-----------------------------------

class LibraryElement (QStandardItem) :

    # -------------
    # Constructors
    # -------------

    def __init__ (self, label_name: str) :

        QStandardItem.__init__(self)

        self.setText(label_name)
        self.setEditable(False)