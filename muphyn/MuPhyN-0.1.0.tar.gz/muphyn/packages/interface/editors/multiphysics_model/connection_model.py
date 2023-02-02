# General import
from typing import Iterable

# PyQt import
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsItem

# Project import
from muphyn.packages.interface.shapes.basic_shape import GroupedShapes, Path

class ConnectionModel(GroupedShapes):

    def __init__(self, points: Iterable[QPointF], parent: QGraphicsItem = None) -> None:
        minX = min([point.x() for point in points])
        minY = min([point.y() for point in points])
        topLeft = QPointF(minX, minY)

        points = [point - topLeft for point in points]

        super().__init__(topLeft, parent)

        # Buidl steps
        steps = [Path.Step(point) for point in points]

        # Build path
        self.path = Path(steps, parent=self)