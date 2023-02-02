#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import os

# PyQt5 Imports
from PyQt5.QtCore import QPointF, QSize, QSizeF, Qt
from PyQt5.QtWidgets import QGraphicsItem

# Project Imports
from muphyn.packages.interface.shapes.basic_shape import GroupedShapes, Text, ImageShapeFactory, AbstractImage
from muphyn.packages.interface.utils.interface_constants import MuphynFonts

class Icon(GroupedShapes):
    def __init__(self, iconPath: str, description: str = None, position: QPointF = QPointF(), 
            size: QSizeF = None, parent: QGraphicsItem = None) -> None:

        # Init parent class
        super().__init__(position, parent)

        # Icon path
        self.iconPath = iconPath

        # Test if path exists
        if os.path.exists(iconPath):
            # Build icon shape
            self.imageShape: AbstractImage = ImageShapeFactory(image_path=iconPath, position=position, size=size, parent=self)

        else:
            # Handle description
            if description is None : 
                self.description = os.path.basename(iconPath)

            # Build text flag
            alignementFlag = Qt.AlignmentFlag.AlignVCenter

            # Build Text shape
            self.textShape = Text(self.description, position=QPointF(), 
                font=MuphynFonts.BoxModelDetailsFont, alignment=alignementFlag, parent=self)

    def setWidth(self, new_width: int) -> None:
        if hasattr(self, "imageShape"):
            self.imageShape.setWidth(new_width)
        else:
            # Resize text area
            pass

    def setHeight(self, new_height: QSizeF) -> None:
        if hasattr(self, "imageShape"):
            self.imageShape.setHeight(new_height)
        else:
            # Resize text area
            pass

    def setSize(self, new_size: QSize | QSizeF) -> None:
        if hasattr(self, "imageShape"):
            self.imageShape.setSize(new_size)
        else:
            # Resize text area
            pass


