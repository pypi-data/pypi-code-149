import sys
import typing

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QPointF, QRectF, QSizeF, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsObject, QGraphicsRectItem, QGraphicsScene, QGraphicsSceneMouseEvent, QGraphicsView
from muphyn.packages.interface.models.graphical_models.resizers.abstract_resizer import AbstractResizer

from muphyn.packages.interface.models.event_signal_data import EventSignalData
from muphyn.packages.interface.models.graphical_models.resizers.horizontal_resizer import HorizontalResizer
from muphyn.packages.interface.models.graphical_models.resizers.oblique_resizer import ObliqueResizer
from muphyn.packages.interface.models.graphical_models.resizers.vertical_resizer import VerticalResizer

from muphyn.packages.interface.models.graphical_models.box_model import BoxModel

if __name__ == "__main__":

    app = QApplication(sys.argv)

    view = QGraphicsView()
    scene = QGraphicsScene()
    scene.setSceneRect(0, 0, 1024, 768)
    view.setScene(scene)

    margin = (1024 - 400) / 5
    box000 = BoxModel('BoxLibrary', 'box 000°', QPointF((1 * margin) + 000, -50 + 384), QSizeF(100, 100), 0)
    box090 = BoxModel('BoxLibrary', 'box 090°', QPointF((2 * margin) + 100, -50 + 384), QSizeF(100, 100), 90)
    box180 = BoxModel('BoxLibrary', 'box 180°', QPointF((3 * margin) + 200, -50 + 384), QSizeF(100, 100), 180)
    box270 = BoxModel('BoxLibrary', 'box 270°', QPointF((4 * margin) + 300, -50 + 384), QSizeF(100, 100), 270)

    scene.addItem(box000)
    scene.addItem(box090)
    scene.addItem(box180)
    scene.addItem(box270)

    view.show()

    sys.exit(app.exec_())