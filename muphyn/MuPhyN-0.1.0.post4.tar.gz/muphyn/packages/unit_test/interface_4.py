import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.interface.models.signals_model.input_connection_model import InputConnectionModel
from muphyn.packages.interface.models.signals_model.output_connection_model import OutputConnectionModel


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    
    view = QtWidgets.QGraphicsView()
    scene = QtWidgets.QGraphicsScene()
    scene.setSceneRect(0, 0, 1024, 768)
    view.setScene(scene)
    
    startPoint = OutputConnectionModel('t', DataType.FLOAT, QtCore.QPointF(100, 100))
    endPoint = InputConnectionModel('t', DataType.FLOAT, QtCore.QPointF(340, 340))
    
    scene.addItem(startPoint)
    scene.addItem(endPoint)

    view.show()

    sys.exit(app.exec_())