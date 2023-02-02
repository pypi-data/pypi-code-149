#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtCore import QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QApplication, QGraphicsSceneHoverEvent
from muphyn.packages.interface.models.graphical_models.resizers.abstract_resizer import AbstractResizer

#-----------------------------------
# Class
#-----------------------------------

class ObliqueResizer (AbstractResizer) :
    """Est le resizer qui permet de modifier la hauteur et la longueur des boxes."""

    # -------------
    # Constructers
    # -------------

    def __init__ (self, parent) :
        
        AbstractResizer.__init__(self, parent, QSizeF(10, 10))

        self.setAcceptHoverEvents(True)

    # -------------
    # Methods
    # -------------

    def changeValue (self, value_: QPointF) -> QPointF :
        return value_ - self.pos()

    def hoverEnterEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
        return super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        while QApplication.overrideCursor() is not None:
            QApplication.restoreOverrideCursor()
        return super().hoverLeaveEvent(event)