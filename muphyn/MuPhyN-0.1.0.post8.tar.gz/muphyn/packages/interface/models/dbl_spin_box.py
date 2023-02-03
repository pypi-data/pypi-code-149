#-----------------------------------
# Imports
#-----------------------------------

import sys
import math as m
from PyQt5 import QtGui

from PyQt5.QtWidgets import QDoubleSpinBox, QWidget

#-----------------------------------
# Class
#-----------------------------------

class DblSpinBox (QDoubleSpinBox) :
    """Est la classe qui décrit une spin box gérant des doubles dont le nombre de zéro est variable."""

    # -------------
    # Contructors
    # -------------

    def __init__ (self, parent : QWidget = None) :

        QDoubleSpinBox.__init__(self, parent)
    
        self.setMinimum(-sys.float_info.max)
        self.setMaximum(sys.float_info.max)
        self.setValue(0)
        self.setDecimals(10) 
    
    # -------------
    # Methods
    # -------------

    def keyPressEvent(self, event : QtGui.QKeyEvent) -> None :
        return super().keyPressEvent(event)

    def setValue (self, value : float) -> None :
        return super().setValue(value)

    def setSingleStep (self, val : float) -> None :
        ...

    def setDecimals (self, precision : int) -> None :

        if precision < 0 :
            precision = 0

        super().setSingleStep(10 * m.pow(10, -precision))
        return super().setDecimals(precision) 
