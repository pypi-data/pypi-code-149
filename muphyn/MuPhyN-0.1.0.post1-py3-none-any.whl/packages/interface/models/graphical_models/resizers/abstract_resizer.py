#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from PyQt5.QtCore import QPointF, QRectF, QSizeF, Qt, pyqtSignal
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsObject
from numpy import minimum

from muphyn.packages.interface.models.event_signal_data import EventSignalData

#-----------------------------------
# Class
#-----------------------------------

class AbstractResizer (QGraphicsObject) :
    """Est la classe abstraite commune des éléments capable de redimensionner les boxes."""

    # -------------
    # Signals
    # -------------

    resizeSignal = pyqtSignal(EventSignalData)
    selectedSignal = pyqtSignal(EventSignalData)

    # -------------
    # Constructors
    # -------------

    def __init__ (self, parent, size : QSizeF) :

        QGraphicsObject.__init__(self, parent)

        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)

        self.setZValue(5)

        self._rect = QRectF(0, 0, size.width(), size.height())
        self._parent = parent

    # -------------
    # Methods
    # -------------

    def boundingRect (self) :
        return self._rect

    def paint (self, painter : QPainter, option, widget = None) :

        if self.isSelected() :
            painter.drawRect(self._rect)

        else :
            painter.fillRect(self._rect, Qt.black)

    def itemChange (self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any :
        
        if change == QGraphicsItem.ItemSelectedChange :
            self.selectedSignal.emit(EventSignalData(self, value))

        elif change == QGraphicsItem.ItemPositionChange :
            if self.isSelected() :
                
                value : QPointF = self.changeValue(value)

                if not(self._parent == None) : 

                    new_width = self._parent._bound.width() + value.x()
                    new_height = self._parent._bound.height() + value.y()

                    minimum_size = self._parent.minimum_size

                    if new_width < minimum_size.width() :
                        value.setX(minimum_size.width() - self._parent._bound.width())

                    if new_height < minimum_size.height() :
                        value.setY(minimum_size.height() - self._parent._bound.height())
                    

                if not(value.x() == 0 and value.y() == 0) :
                    self.resizeSignal.emit(EventSignalData(self, value))
            
                return QPointF(self.pos().x() + (value.x() / 2), self.pos().y() + (value.y() / 2))

        return super().itemChange(change, value)

    def changeValue (self, value_ : QPointF) -> QPointF :
        raise Exception('AbstractResizer.changeValue is an abstract method and must be overhidden.')