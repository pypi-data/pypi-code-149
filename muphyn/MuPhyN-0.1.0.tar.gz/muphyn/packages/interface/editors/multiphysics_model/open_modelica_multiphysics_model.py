# General import
from typing import Optional, Type

# PyQt import
from PyQt5.QtCore import QPoint, QPointF
from PyQt5.QtWidgets import QWidget

# Project import
from muphyn.packages.interface.editors.multiphysics_model import *
from muphyn.packages.core.simulation.model_parser import OpenModelicaModelParser, OpenModelicaComponent, OpenModelicaConnection

class OpenModelicaMultiphysicsModel(AbstractMultiPhysicsModel):

    # Component look up table
    ComponentLUT: dict = {
        "Modelica.Electrical.Analog.Basic.Ground": GroundModel,
        "Modelica.Electrical.Analog.Basic.Resistor": ResistorModel,
        "Modelica.Electrical.Analog.Basic.VariableResistor": VariableResistorModel,
        "Modelica.Electrical.Analog.Sources.SignalCurrent": SignalCurrentSourceModel
    }

    def __init__(self, omParser: OpenModelicaModelParser, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        # Add components to view
        for component in omParser.components:
            self.addComponent(component)

        # Add connections to view
        for connection in omParser.connections:
            self.addConnection(connection)

    def addComponent(self, newOpenModelicaComponent: OpenModelicaComponent):

        # Build component model
        componentModel: AbstractComponentModel = OpenModelicaMultiphysicsModel.componentModelFactory(newOpenModelicaComponent)

        # Place item above
        componentModel.setZValue(1)

        # Add component to scene
        return super().addItem(componentModel)

    def addConnection(self, newOpenModelicaConnection: OpenModelicaConnection):
        # Convert open modelica connection points
        points = [QPointF(point.x(), -point.y()+20) * 4 for point in newOpenModelicaConnection.points()]

        # Build connection model
        connectionModel = ConnectionModel(points)

        # Place item under
        connectionModel.setZValue(0)

        # Add connection to scene
        return super().addItem(connectionModel)

    @staticmethod
    def componentModelFactory(openModelicaComponent: OpenModelicaComponent):
        newComponentModelType: Type[AbstractComponentModel] = OpenModelicaMultiphysicsModel.ComponentLUT[openModelicaComponent.library]

        # Get component data
        componentPosition: QPoint = openModelicaComponent.topLeft() * 4
        componentPosition = QPointF(componentPosition.x(), -componentPosition.y())
        componentRotation = -openModelicaComponent.rotation()

        newComponentModel = newComponentModelType(group_position=componentPosition)
        newComponentModel.setRotation(componentRotation)

        return newComponentModel