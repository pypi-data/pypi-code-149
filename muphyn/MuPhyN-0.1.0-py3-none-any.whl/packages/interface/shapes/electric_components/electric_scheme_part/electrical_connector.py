from enum import Enum
from PyQt5.QtCore import QLineF, QPointF, QSizeF
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QColor

from basic_shape.shapes import Square, Line
from basic_shape.grouped_shapes import GroupedShapes



class ElectricalConnector(GroupedShapes):

    # Elecrtical node type
    class ElectricalConnectorType(Enum):
        Positive = 1
        Neutral = 0
        Negative = -1

    # Node Size
    node_side_size = 10
    connector_line_length = 10
    connector_size = QSizeF(node_side_size + connector_line_length, node_side_size)

    # Node Color    
    border_node_color = QColor(0, 0, 255)
    positive_node_color = border_node_color
    negative_node_color = QColor(255, 255, 255)

    def __init__(self, type: ElectricalConnectorType, position: QPointF = QPointF(0, 0), parent: QGraphicsItem = None) -> None:

        super().__init__(position, parent=parent)

        # Select Color
        border_color = ElectricalConnector.border_node_color
        background_color = ElectricalConnector.get_color_by_type(type)

        # Shapes
        offset = position + QPointF(0, -ElectricalConnector.node_side_size/2)

        # Square
        square = Square(
            QPointF(0, 0) + offset, 
            ElectricalConnector.node_side_size, 
            border_color=border_color, border_width=2, fill_color=background_color,
            parent=self
        )

        # Line
        start_point = QPointF(ElectricalConnector.node_side_size, ElectricalConnector.node_side_size/2) + offset
        end_point = QPointF(ElectricalConnector.node_side_size + ElectricalConnector.connector_line_length, ElectricalConnector.node_side_size/2) + offset
        line = Line(
            QLineF(start_point, end_point),
            line_color=border_color, line_width=2,
            parent=self
        )

        # self.add_shapes([square, line])


    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def get_color_by_type(type: ElectricalConnectorType) -> QColor:
        color_switcher = {
            ElectricalConnector.ElectricalConnectorType.Positive: ElectricalConnector.positive_node_color,
            ElectricalConnector.ElectricalConnectorType.Neutral: ElectricalConnector.positive_node_color,
            ElectricalConnector.ElectricalConnectorType.Negative: ElectricalConnector.negative_node_color
        }

        return color_switcher[type]