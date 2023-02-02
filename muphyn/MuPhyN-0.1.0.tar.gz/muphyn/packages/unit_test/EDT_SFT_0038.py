
from typing import List

from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRectF, QSizeF, QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGraphicsObject, QGraphicsScene, QWidget, QGraphicsView, QDialog, QStyleOptionGraphicsItem, QGraphicsItem

class FakeBox (QGraphicsObject) :

    def __init__ (self) :
        
        self._size : QSizeF = QSizeF(0, 0)
        QGraphicsObject.__init__(self, parent = None)

        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)
        self._rect = QRectF(QPointF(0, 0), self._size)

    def boundingRect(self) -> QRectF :
        return self._rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        painter.drawRect(self.boundingRect())

    def size (self) -> QSizeF :
        return self._size

    def setSize (self, size_ : QSizeF) :
        self._size = size_

class FakeLink (QGraphicsObject) :

    def __init__ (self, parent : FakeBox, connected_to : FakeBox) :
         
        QGraphicsObject.__init__(self, parent)
        self.setParent(parent)

        self._connected_to = connected_to
        self._parent = parent
        
    def boundingRect(self) -> QRectF :
        
        self._p1 = self._parent.scenePos()
        self._p2 = self._connected_to.scenePos()
        self._line = self._p2 - self._p1

        print(self.print_values('parent', self._parent))
        print(self.print_values('connected', self._connected_to))
        print('starting point :', self.print_point(self._p1))
        print('stop point :', self.print_point(self._p2))
        print('==========================================================================')

        return QRectF(QPointF(0, 0), QSizeF(self._line.x(), self._line.y()))

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        self.setRotation(-self._parent.rotation())
        path = QtGui.QPainterPath(QPointF(0, 0))
        path.lineTo(self._line)
        painter.drawPath(path)

    def print_values (self, name : str, box : FakeBox) -> None : 
        return name + ' : ' + self.print_point(box.pos()) + ' ' + self.print_size(box.size())

    def print_rect (self, rect : QRectF) -> str : 
        return '[' +  str(rect.x()) + '; ' + str(rect.y()) + '] [' + str(rect.width()) + '; ' + str(rect.height()) + ']' 

    def print_point (self, point : QPointF) -> str :
        return '[' +  str(point.x()) + '; ' + str(point.y()) + ']'

    def print_size (self, size : QSizeF) -> str :
        return '[' + str(size.width()) + '; ' + str(size.height()) + ']'


class Scenery (QGraphicsScene) :

    def __init__ (self, parent : QWidget = None, graphical_scenery = None) :
        QGraphicsScene.__init__(self, parent)
        self._graphical_scenery = graphical_scenery
        self._start_sliding_point = None
        self._boxes : List[FakeBox] = []

    def append_element (self, box : FakeBox) -> None :
        self.addItem(box)
        self._boxes.append(box)

class GraphicalScenery (QGraphicsView) :

    def __init__ (self, parent : QWidget) :

        QGraphicsView.__init__(self, parent)
        self.setScene(Scenery(self, self))

    def scenery (self) -> Scenery :
        return self.scene()

class UI (QDialog) :

    def __init__ (self, parent : QWidget = None) :

        QDialog.__init__(self, parent)
        self.setFixedSize(630, 480)
        self.setWindowTitle('Test graphics')

        self._red_brush : QtGui.QBrush = QtGui.QBrush(Qt.red)
        self._blue_brush : QtGui.QBrush = QtGui.QBrush(Qt.blue)
        self._black_pen : QtGui.QPen = QtGui.QPen(Qt.black)
        self._black_pen.setWidth(6)

        
        self._graphics_view : QGraphicsView = GraphicalScenery(self)
        self._graphics_view.setGeometry(QtCore.QRect(10, 10, 610, 460))

        box1 = FakeBox()
        box1.setPos(QPointF(10, 10))
        box1.setSize(QSizeF(100, 150))
        box1.setRotation(180)
        self._graphics_view.scenery().append_element(box1)

        box2 = FakeBox()
        box2.setPos(QPointF(300, 10))
        box2.setSize(QSizeF(100, 150))
        self._graphics_view.scenery().append_element(box2)
        
        output = FakeLink(box1, box2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())