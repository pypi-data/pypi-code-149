from PyQt5.QtCore import QPointF, QRectF, pyqtSignal
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsObject, QStyleOptionGraphicsItem

class GroupedShapes(QGraphicsObject):

    position_changed = pyqtSignal()

    def __init__(self, group_position: QPointF = QPointF(0, 0), parent: QGraphicsItem = None) -> None:
        QGraphicsObject.__init__(self, parent)        
        self.setPos(group_position)
    
    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return self.childrenBoundingRect()

    def paint (self, painter: QPainter, option: QStyleOptionGraphicsItem = QStyleOptionGraphicsItem.OptionType.SO_Frame, widget=None) -> None :
        return None

    def setRotation(self, angle: float) -> None:
        self.setTransformOriginPoint(self.boundingRect().center())
        return super().setRotation(angle)