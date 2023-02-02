from typing import Optional, Union

from PyQt5.QtCore import Qt, QEvent, QRect
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QDialog, QWidget, QApplication

from muphyn.packages.core.simulation.model_parser.open_modelica_model_parser import OpenModelicaModelParser
from muphyn.packages.interface.editors.multiphysics_model.open_modelica_multiphysics_model import OpenModelicaMultiphysicsModel

class MultiphysicsModelPreviewer(QDialog):

    # Constants
    DefaultRect = QRect(0, 0, 640, 480)

    def __init__(self, multiphysics_parser: OpenModelicaModelParser, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent, Qt.WindowType.Dialog)
        
        # Get screen 
        globalCursorPosition = QCursor.pos()
        screenNumber = QApplication.desktop().screenNumber(globalCursorPosition)

        # Get current screen 
        screenRect = QApplication.desktop().availableGeometry(screenNumber)
        appRect = MultiphysicsModelPreviewer.DefaultRect

        # Calculate centered geometry
        offset = screenRect.center() - appRect.center()
        appRect.translate(offset)

        # General Parameters
        self.setMinimumSize(appRect.size())
        self.setGeometry(appRect)

        self.openModelicaModelPreviewer = OpenModelicaMultiphysicsModel(multiphysics_parser, parent=self)

    def event(self, a0: QEvent) -> bool:
        if a0.type() == QEvent.Type.Resize:
            self.openModelicaModelPreviewer.setSize(self.size())
        return super().event(a0)