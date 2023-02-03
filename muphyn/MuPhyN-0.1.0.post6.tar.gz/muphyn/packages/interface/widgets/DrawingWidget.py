# General import
from enum import Enum
from typing import Optional

# General imports
import numpy as np

# PyQt imports
from PyQt5.QtCore import QRect,QSize, Qt
from PyQt5.QtGui import QColor, QImage, QPainter, QPixmap, QWheelEvent, QBrush
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QWidget, QApplication

# Project imports
from muphyn.packages.core.utils.log_manager import LogManager

class DrawingScene(QGraphicsScene):

    def __init__(self, parent):
        super().__init__(parent)

class DrawingView(QGraphicsView):

    def __init__(self, scene: QGraphicsScene, parent):

        super().__init__(scene, parent)

        # General View Parameters
        self.setGeometry(self.geometry())
        self.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        # Init zoom
        self.zoomLevel = 5

    def setSize(self, newSize: QSize) -> None:
        # Update geometry
        self.setGeometry(QRect(self.pos(), newSize))

    def wheelEvent(self, event: QWheelEvent):
        if Qt.KeyboardModifier.ControlModifier == QApplication.keyboardModifiers():
            if  event.angleDelta().y() > 0:
                factor = 1.25
                self.zoomLevel += 1
            else:
                if self.zoomLevel > 0:
                    factor = 0.8
                    self.zoomLevel -= 1

            if self.zoomLevel > 0:
                self.scale(factor, factor)

class PatternBuilder:

    class PatternType(Enum):
        CrossPattern = 0
        SquarePattern = 1

    # -------------
    # Constants
    # -------------
    DefaultGridColor = QColor(200, 200, 200)

    @staticmethod
    def buildPixmap(gridSize: int, patternType: PatternType, color: QColor = DefaultGridColor) -> QPixmap:
        if patternType == PatternBuilder.PatternType.CrossPattern:
            return PatternBuilder.buildCrossPattern(gridSize, color)
        elif patternType == PatternBuilder.PatternType.SquarePattern:
            return PatternBuilder.buildSquarePattern(gridSize, color)
        else:
            LogManager().error(f"PatternBuilder.buildPixmap(): Pattern type not supported {patternType}")
            return QPixmap(gridSize, gridSize)

    @staticmethod
    def buildCrossPattern(gridSize: int, color: QColor = DefaultGridColor) -> QPixmap:
        # Convetr color to list
        colorList = [color.red(), color.green(), color.blue()]

        # Init numpy array
        npPattern = np.full((gridSize, gridSize, 3), 255, np.uint8)

        # Change numpy array pattern
        ## Top left corner
        npPattern[0,:3] = colorList
        npPattern[:3,0] = colorList

        ## Top right corner
        npPattern[0,-2:] = colorList

        ## Bottom left corner
        npPattern[-2:,0] = colorList

        bytesPerLine = 3 * gridSize
        return QImage(npPattern.data, gridSize, gridSize, bytesPerLine, QImage.Format_RGB888)

    @staticmethod
    def buildSquarePattern(gridSize: int, color: QColor = DefaultGridColor) -> QPixmap:
        # Convetr color to list
        colorList = [color.red(), color.green(), color.blue()]

        # Init numpy array
        npPattern = np.full((gridSize, gridSize, 3), 255, np.uint8)

        # Change numpy array pattern
        ## Replace first row
        npPattern[0,:] = colorList
        ## Replace first column
        npPattern[1:,0] = colorList

        bytesPerLine = 3 * gridSize
        return QImage(npPattern.data, gridSize, gridSize, bytesPerLine, QImage.Format_RGB888)

class DrawingWidget(QWidget):

    def __init__(self, parent: Optional[QWidget] = None) -> None:

        # Widget flag
        super().__init__(parent)

        # Create board scene
        self.scene = DrawingScene(self)

        # Create Board View
        self.view = DrawingView(self.scene, self)

        # Draw background
        self.view.setBackgroundBrush(QBrush(PatternBuilder.buildPixmap(50, PatternBuilder.PatternType.CrossPattern)))

    def setSize(self, newSize: QSize):
        # Set this item size
        self.setGeometry(QRect(self.pos(), newSize))

        # Update view size
        self.view.setSize(newSize)