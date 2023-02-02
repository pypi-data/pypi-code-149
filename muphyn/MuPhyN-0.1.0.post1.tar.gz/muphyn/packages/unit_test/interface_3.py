
from typing import List, Any

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QDialog, QGraphicsItem, QGraphicsScene, QGraphicsView, QStyleOptionGraphicsItem, QWidget

from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.interface.models.editable_models.abstract_diagram_model import AbstractDiagramModel
from muphyn.packages.interface.models.graphical_models.abstract_box_model import AbstractBoxModel
from muphyn.packages.interface.models.graphical_models.abstract_graphical_element import AbstractGraphicalElement
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel

class SelectableBox (AbstractGraphicalElement) :

    def __init__ (self, name : str, position : QPointF, size : QSizeF, parent : QGraphicsItem = None) :
        
        AbstractGraphicalElement.__init__(self, name, position, size, 0, name, parent)
        
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)

        self._font_metrics_used : QtGui.QFontMetrics = None
        self._text_point : QPointF = QPointF(0, 0)

    def itemChange(self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any :

        if change == QGraphicsItem.ItemSelectedChange :
            self.setZValue(value)

        elif change == QGraphicsItem.ItemPositionHasChanged :
            print('item changed ', self.name, ' position : ', value.x(), '; ', value.y())

        elif change == QGraphicsItem.ItemPositionChange :
            print('item changed ', self.name, ' position : ', value.x(), '; ', value.y())

        return super().itemChange(change, value)


    def recompute_name_position (self) :
        """Permet de recalculer la taille du texte affiché et le recentrer dans la box."""
        
        if self._font_metrics_used is None :
            return

        point_x = (self.size.width() - self._font_metrics_used.width(self.rendered_text)) / 2
        point_y = ((self.size.height() - self._font_metrics_used.height()) / 2) + self._font_metrics_used.height()
        self._text_point = QPointF(point_x, point_y)

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem, widget) -> None :

        if self._font_metrics_used is None :
            self._font_metrics_used = QtGui.QFontMetrics(painter.font())

        self.recompute_name_position()

        if self.isSelected() :
            painter.setPen(self.selected_black_pen)
        
        else :
            painter.setPen(self.unselected_black_pen)
        
        painter.fillRect(self._bound, self.white_brush)
        painter.drawRect(self._bound)
        painter.drawText(int(self._text_point.x()), int(self._text_point.y()), self.rendered_text)


class Scenery (QGraphicsScene) :

    def __init__ (self, parent : QWidget = None, graphical_scenery = None) :
        QGraphicsScene.__init__(self, parent)
        self._graphical_scenery = graphical_scenery
        self._start_sliding_point = None
        self._boxes : List[AbstractGraphicalElement] = []

    def append_element (self, box : AbstractBoxModel) -> None :
        self.addItem(box)
        self._boxes.append(box)

    def new_selection_item (self, selectable) -> None :
        self.setFocusItem(selectable)
        selectable.setZValue(self.items().__len__())

class GraphicalScenery (QGraphicsView) :

    def __init__ (self, parent : QWidget) :

        QGraphicsView.__init__(self, parent)

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setDragMode(QGraphicsView.RubberBandDrag)

    def mousePressEvent(self, event):
        if event.button() == Qt.MidButton: # or Qt.MiddleButton
            self.__prevMousePos = event.pos()
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent (self, event) :
        if event.buttons() == Qt.MidButton: # or Qt.MiddleButton
            offset = self.__prevMousePos - event.pos()
            self.__prevMousePos = event.pos()

            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + offset.y())
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + offset.x())
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:

        if event.modifiers() == Qt.ControlModifier :

            if event.angleDelta().y() > 0 :
                self.scale(1.125, 1.125)

            elif event.angleDelta().y() < 0 :
                self.scale(0.825, 0.825)

            event.accept()
        else :
            super().wheelEvent(event) 

class UI (QDialog) :

    def __init__ (self, parent : QWidget = None) :

        QDialog.__init__(self, parent)
        self.setFixedSize(630, 480)
        self.setWindowTitle('Test graphics')


        self._red_brush : QtGui.QBrush = QtGui.QBrush(Qt.red)
        self._blue_brush : QtGui.QBrush = QtGui.QBrush(Qt.blue)
        self._black_pen : QtGui.QPen = QtGui.QPen(Qt.black)
        self._black_pen.setWidth(6)

        
        self._graphics_view : QGraphicsView = AbstractDiagramModel(self)
        self._graphics_view.setGeometry(QtCore.QRect(10, 10, 610, 460))
        
        width = 100
        height = 150

        box1 = BoxModel('sources', 'box 1', QPointF(10, 10), QSizeF(width, height), 0, True, parent = None)
        box1.insert_input(0, 'Test', DataType.FLOAT, 'Test')
        box1.insert_input(1, 'Test', DataType.FLOAT, 'Test')
        box1.insert_output(0, 'Test', DataType.FLOAT, 'test')
        box1.insert_output(2, 'Test', DataType.FLOAT, 'test')

        box2 = BoxModel('sources', 'box 2', QPointF(20 + width + width, 10), QSizeF(width, height), 0, True, parent = None)
        box2.insert_input(0, 'Test', DataType.FLOAT, 'Test')
        box2.insert_output(0, 'Test', DataType.FLOAT, 'test')

        box6 = BoxModel('sources', 'box 6', QPointF(20 + width + width, 20 + height), QSizeF(width, height), 0, True, parent = None)
        box6.insert_input(0, 'Test', DataType.FLOAT, 'Test')
        box6.insert_output(0, 'Test', DataType.FLOAT, 'test')

        box3 = BoxModel('sources', 'box 3', QPointF(10, 20 + height), QSizeF(width, height), 90, True, parent = None)
        box4 = BoxModel('sources', 'box 4', QPointF(10, 30 + height + height), QSizeF(width, height), 180, True, parent = None)
        box5 = BoxModel('sources', 'box 5', QPointF(10, 40 + height + height + height), QSizeF(width, height), 270, True, parent = None)

        box3.insert_input(0, 'Test', DataType.FLOAT, 'Test')
        box3.insert_output(0, 'Test', DataType.FLOAT, 'test')

        box4.insert_input(0, 'Test', DataType.FLOAT, 'Test')
        box4.insert_output(0, 'Test', DataType.FLOAT, 'test')

        box5.insert_input(0, 'Test', DataType.FLOAT, 'Test')
        box5.insert_output(0, 'Test', DataType.FLOAT, 'test')

        self._graphics_view.add_graphical_element(box1)
        self._graphics_view.add_graphical_element(box2)
        #self._graphics_view.add_graphical_element(box3)
        #self._graphics_view.add_graphical_element(box4)
        #self._graphics_view.add_graphical_element(box5)
        self._graphics_view.add_graphical_element(box6)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())