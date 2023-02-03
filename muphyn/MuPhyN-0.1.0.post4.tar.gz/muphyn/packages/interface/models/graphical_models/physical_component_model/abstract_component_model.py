

# PyQt5 Imports
from PyQt5.QtCore import QPointF, QSizeF
from PyQt5.QtWidgets import QGraphicsItem

# Project Imports
from muphyn.packages.interface.models.graphical_models.abstract_moveable_graphical_element import AbstractMoveableGraphicalElement

class AbstractComponentModel(AbstractMoveableGraphicalElement):

    def __init__(self, name: str, position: QPointF, size: QSizeF, rotation: float = 0.0, 
        text: str = '', parent: QGraphicsItem = None, symbol_path: str = None):

        AbstractMoveableGraphicalElement.__init__(name, position, size, rotation, text, parent)

        self._should_recompute = False
