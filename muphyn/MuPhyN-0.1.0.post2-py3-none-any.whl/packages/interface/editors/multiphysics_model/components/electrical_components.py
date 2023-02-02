# General import
from enum import Enum

# PyQt import
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsItem

# Project import
from muphyn.packages.interface.editors.multiphysics_model import AbstractComponentModel, ComponentConnector
from muphyn.packages.interface.shapes.basic_shape.shapes import Circle

class ElectricalComponentConnector(ComponentConnector):

    class ConnectorType(Enum):
        Positive = 1
        Negative = -1
        Neutral = 0

    # Constants
    Radius = ComponentConnector.ItemSideSize / 2

    ConnectorFillColorLUT = {
        ConnectorType.Positive: QColor(50, 50, 50),
        ConnectorType.Negative: QColor(255, 255, 255),
        ConnectorType.Neutral: QColor(128, 128, 128)
    }

    def __init__(self, connectorType: ConnectorType, group_position: QPointF = QPointF(), parent: QGraphicsItem = None) -> None:
        super().__init__(group_position, parent)

        # Select border & fill colors
        fillColor = ElectricalComponentConnector.ConnectorFillColorLUT[connectorType]

        # Circle
        center = group_position + QPointF(ElectricalComponentConnector.Radius, ElectricalComponentConnector.Radius)
        radius = ElectricalComponentConnector.Radius
        Circle(center, radius, fill_color=fillColor, border_width=2, parent=parent)

# 
class GroundModel(AbstractComponentModel):

    # Constants
    IconPath = "packages/interface/assets/Components/Electrics/ground.svg"

    def __init__(self, group_position = QPointF(), parent = None) -> None:
        super().__init__(__class__.IconPath, group_position, parent)

        # Calculate node position
        pos = QPointF((AbstractComponentModel.DefaultSize.width())/2, 0) - QPointF(ElectricalComponentConnector.Radius, ElectricalComponentConnector.Radius)

        self.p: ComponentConnector = ElectricalComponentConnector(
            ElectricalComponentConnector.ConnectorType.Neutral, 
            pos, 
            parent=self
        )

# Resistor Models
class ResistorModel(AbstractComponentModel):

    # Constants
    IconPath = "packages/interface/assets/Components/Electrics/resistor.svg"

    def __init__(self, group_position = QPointF(), parent = None) -> None:
        super().__init__(__class__.IconPath, group_position, parent)

        # Calculate point position
        leftX =  -ElectricalComponentConnector.Radius
        rightX = AbstractComponentModel.DefaultSize.width() - ElectricalComponentConnector.Radius
        y = AbstractComponentModel.DefaultSize.height()/2 - ElectricalComponentConnector.Radius

        # Add connectors
        self.p: ComponentConnector = ElectricalComponentConnector(
            ElectricalComponentConnector.ConnectorType.Positive, 
            QPointF(leftX, y), 
            parent=self
        )
        self.n: ComponentConnector = ElectricalComponentConnector(
            ElectricalComponentConnector.ConnectorType.Negative, 
            QPointF(rightX, y), 
            parent=self
        )

class VariableResistorModel(AbstractComponentModel):

    # Constants
    IconPath = "packages/interface/assets/Components/Electrics/variable_resistor.svg"

    def __init__(self, group_position = QPointF(), parent = None) -> None:
        super().__init__(__class__.IconPath, group_position, parent)

        # Calculate point position
        leftX =  -ElectricalComponentConnector.Radius
        rightX = AbstractComponentModel.DefaultSize.width() - ElectricalComponentConnector.Radius
        y = AbstractComponentModel.DefaultSize.height()/2 - ElectricalComponentConnector.Radius

        # Add connectors
        self.p: ComponentConnector = ElectricalComponentConnector(
            ElectricalComponentConnector.ConnectorType.Positive, 
            QPointF(leftX, y), 
            parent=self
        )
        self.n: ComponentConnector = ElectricalComponentConnector(
            ElectricalComponentConnector.ConnectorType.Negative, 
            QPointF(rightX, y), 
            parent=self
        )

class SignalCurrentSourceModel(AbstractComponentModel):

    # Constants
    IconPath = "packages/interface/assets/Components/Electrics/signal_current_source.svg"

    def __init__(self, group_position = QPointF(), parent = None) -> None:
        super().__init__(__class__.IconPath, group_position, parent)

        # Calculate point position
        leftX =  -ElectricalComponentConnector.Radius
        rightX = AbstractComponentModel.DefaultSize.width() - ElectricalComponentConnector.Radius
        y = AbstractComponentModel.DefaultSize.height()/2 - ElectricalComponentConnector.Radius

        # Add connectors
        self.p: ComponentConnector = ElectricalComponentConnector(
            ElectricalComponentConnector.ConnectorType.Positive, 
            QPointF(leftX, y), 
            parent=self
        )

        self.n: ComponentConnector = ElectricalComponentConnector(
            ElectricalComponentConnector.ConnectorType.Negative, 
            QPointF(rightX, y), 
            parent=self
        )
