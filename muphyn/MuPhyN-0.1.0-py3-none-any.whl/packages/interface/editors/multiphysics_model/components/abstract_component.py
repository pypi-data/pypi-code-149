# General import
import os

# PyQt import
from PyQt5.QtCore import QPointF, QRectF, QSizeF
from PyQt5.QtWidgets import QGraphicsItem

# Project import
from muphyn.packages.interface.shapes.basic_shape import GroupedShapes, ImageShapeFactory

class ComponentConnector(GroupedShapes):

    # Constants
    ItemSideSize = 8

    def __init__(self, group_position: QPointF = QPointF, parent: QGraphicsItem = None) -> None:
        super().__init__(group_position, parent)

    def absoluteCenter(self) -> QPointF:
        return self.scenePos() + self.boundingRect().center()

class AbstractComponentModel(GroupedShapes):

    # -------------
    # Constants
    # -------------
    DefaultSize: QSizeF = QSizeF(80, 80)
    DefaultRect: QRectF = QRectF(
        -ComponentConnector.ItemSideSize, 
        -ComponentConnector.ItemSideSize,
        DefaultSize.width() + 2*ComponentConnector.ItemSideSize,
        DefaultSize.height() + 2*ComponentConnector.ItemSideSize
    )

    def __init__(self, iconPath: str = None, group_position = QPointF(), parent = None) -> None:

        if iconPath is None or not os.path.exists(iconPath):
            raise(FileExistsError(f"AbstractComponentModel.__init__(): Given Icon path doesn't exists {iconPath}"))

        super().__init__(group_position, parent)

        # Icon
        self.icon = ImageShapeFactory(iconPath, size=AbstractComponentModel.DefaultSize, parent=self)

        # Set transform origin point to the center of this item
        self.setTransformOriginPoint(AbstractComponentModel.DefaultRect.center())

    # -------------
    # Properties
    # -------------

    

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return AbstractComponentModel.DefaultRect