
# PyQt5 imports
from itertools import count
from PyQt5.QtCore import QPointF, QRectF, QSizeF, QSize
from PyQt5.QtWidgets import QGraphicsObject

# Project imports
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.shapes.basic_shape import GroupedShapes

class VerticalLayout(GroupedShapes):
    def __init__(self, group_position: QPointF = QPointF(0, 0), parent = None) -> None:
        super().__init__(group_position, parent)

        # Init child items
        self.childConfigs: dict[QGraphicsObject, dict] = {}

        # Maximum size
        self._maximumWidth: int = 0
        self._maximumHeight: int = 0

        # Spacing
        self._spacing: int = 0
    
    # -------------
    # Properties
    # -------------
    @property
    def count(self) -> int:
        return len(list(self.childConfigs))

    @property
    def maximumWidth(self) -> int:
        return self._maximumWidth

    @maximumWidth.setter
    def maximumWidth(self, newMaximumWidth: int) -> None:
        if newMaximumWidth != self._maximumWidth:
            self.setMaximumWidth(newMaximumWidth)

    @property
    def maximumHeight(self) -> int:
        return self._maximumHeight

    @maximumHeight.setter
    def maximumHeight(self, newMaximumHeight: int) -> None:
        if newMaximumHeight != self._maximumHeight:
            self.setMaximumHeight(newMaximumHeight)

    @property
    def spacing(self) -> int:
        return self._spacing

    @spacing.setter
    def spacing(self, newSpacing: int) -> None:
        if newSpacing != self._spacing:
            self.setSpacing(newSpacing)

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return QRectF(QPointF(), QSizeF(self.maximumWidth, self.maximumHeight))

    def addItem(self, newItem: QGraphicsObject, height: int = 0):
        # Create config parameters dictionnary
        self.childConfigs[newItem] = {
            "height": height if height > 0 else 0
        }

        # Set parent item
        newItem.setParentItem(self)

        # Handle children positions
        self.recomputeChildrenPosition()

    def removeItem(self, item: QGraphicsObject):
        # Remove item from child list
        del self.childConfigs[item]

        # Remove parent Item
        item.setParentItem(None)

        # Handle children positions
        self.recomputeChildrenPosition()

    def recomputeChildrenPosition(self):
        heightNotSetItems = [item for item, config in self.childConfigs.items() if config["height"] < 1]

        # Calculate total height
        totalMinimumSize = sum([config["height"] for config in self.childConfigs.values()])

        # Calculate total spacing height
        totalSpacingHeight = self._spacing * (self.count - 1) 

        # Calculate exceed height space
        exceedHeightSpace = self._maximumHeight - totalMinimumSize - totalSpacingHeight
        
        if exceedHeightSpace >= 0:
            # Calculate shared height space
            if len(heightNotSetItems) > 0:
                exceedHeightShared = exceedHeightSpace / len(heightNotSetItems)
            else:
                exceedHeightShared = 0

            # Place all items
            y_axis_position = 0
            for item, config in self.childConfigs.items():
                # Move Item
                item.setPos(QPointF(0, y_axis_position))

                # Set height
                if config["height"] == 0:
                    height = exceedHeightShared
                else:
                    height = config["height"]
                item.setSize(QSize(int(self.maximumWidth), int(height)))

                # Update next item y-axis position
                y_axis_position += height + self._spacing

        else:
            pass

    def setMaximumWidth(self, newMaximumWidth: int):
        if newMaximumWidth < 0:
            LogManager().error(f"VerticalLayout.setMaximumWidth(): Maximum width value is negative {newMaximumWidth}")
            return

        self._maximumWidth = newMaximumWidth

    def setMaximumHeight(self, newMaximumHeight: int):
        if newMaximumHeight < 0:
            LogManager().error(f"VerticalLayout.setMaximumHeight(): Maximum width value is negative {newMaximumHeight}")

        self._maximumHeight = newMaximumHeight

    def setSpacing(self, newSpacing: int):
        if newSpacing < 0:
            LogManager().error(f"VerticalLayout.setSpacing(): Spacing value is negative {newSpacing}")

        self._spacing = newSpacing
