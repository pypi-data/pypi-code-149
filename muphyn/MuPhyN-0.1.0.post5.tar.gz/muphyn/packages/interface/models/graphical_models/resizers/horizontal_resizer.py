#-----------------------------------
# Imports
#-----------------------------------

from PyQt5.QtCore import QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QApplication, QGraphicsSceneHoverEvent
from muphyn.packages.interface.models.graphical_models.resizers.abstract_resizer import AbstractResizer

#-----------------------------------
# Class
#-----------------------------------

class HorizontalResizer (AbstractResizer) :
    """Est le resizer qui permet de modifier la longueur des boxes."""

    # -------------
    # Constructers
    # -------------

    def __init__ (self, parent) :
        
        AbstractResizer.__init__(self, parent, QSizeF(10, 20))

        self.setAcceptHoverEvents(True)

    # -------------
    # Methods
    # -------------

    def changeValue (self, value_: QPointF) -> QPointF :
        v : QPointF = value_ - self.pos()
        v.setY(0)
        return v

    def hoverEnterEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        QApplication.setOverrideCursor(Qt.SizeHorCursor)
        return super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        while QApplication.overrideCursor() is not None:
            QApplication.restoreOverrideCursor()
        return super().hoverLeaveEvent(event)
        