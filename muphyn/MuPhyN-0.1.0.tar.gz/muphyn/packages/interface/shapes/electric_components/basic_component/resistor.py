
from PyQt5.QtCore import QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QColor

from basic_shape.shapes import Text
from basic_shape.image_shapes import ImageShapeFactory
from basic_shape.grouped_shapes import GroupedShapes
from electric_components.electric_scheme_part.electrical_connector import ElectricalConnector

class Resistor(GroupedShapes):

    # Image 
    border_color = QColor(0, 0, 0)

    background_color = QColor(255, 255, 255)

    rectangle_size = QSizeF(100, 100)

    def __init__(self, group_position: QPointF = QPointF(0, 0), parent: QGraphicsItem = None) -> None:

        super().__init__(group_position, parent=parent)

        # Init Positive Node
        self.positive_node = ElectricalConnector(
            ElectricalConnector.ElectricalConnectorType.Positive,
            position=QPointF(0, Resistor.rectangle_size.height()/2),
            parent=self
        )
        
        # Init Negative Node
        self.negative_node = ElectricalConnector(
            ElectricalConnector.ElectricalConnectorType.Negative,
            QPointF(Resistor.rectangle_size.width() + ElectricalConnector.connector_size.width(), Resistor.rectangle_size.height()/2),
            parent=self
        )
        self.negative_node.setRotation(180)
        
        # Init Resistor Icon
        self.resistor_icon = ImageShapeFactory(
            "packages/interface/assets/ec-Resistor_US.svg", 
            QPointF(ElectricalConnector.connector_size.width(), 0), Resistor.rectangle_size, 
            border_color=QColor(255, 0, 0),
            aspect_ratio_mode=Qt.AspectRatioMode.KeepAspectRatio,
            parent=self
        )
        self.resistor_icon.setRotation(90)

        # Text 
        self.text = Text(
            "R", 
            QPointF(60, 10), 60,
            parent=self)

        self.setFlag(QGraphicsItem.ItemIsMovable)