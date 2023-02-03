from PyQt5 import QtCore, QtGui, QtWidgets


class Diedrico (QtWidgets.QWidget) :
    
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        pen = QtGui.QPen(QtGui.QColor(QtCore.Qt.black), 5)
        qp.setPen(pen)
        qp.drawRect(500, 500, 1000, 1000)
        qp.drawRect(100, 100, 10, 20)
        qp.drawText(100, 100, "Test")


class UiVentana(QtWidgets.QMainWindow):
    factor = 1.5

    def __init__(self, parent=None):
        super(UiVentana, self).__init__(parent)

        self._scene = QtWidgets.QGraphicsScene(self)
        self._view = QtWidgets.QGraphicsView(self._scene)

        self._diedrico = Diedrico()
        self._diedrico.setFixedSize(2000, 2000)
        self._scene.addWidget(self._diedrico)

        self.setCentralWidget(self._view)

        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.Key_Plus), # <---
            self._view,
            context=QtCore.Qt.WidgetShortcut,
            activated=self.zoom_in,
        )

        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.Key_Minus), # <---
            self._view,
            context=QtCore.Qt.WidgetShortcut,
            activated=self.zoom_out,
        )

    @QtCore.pyqtSlot()
    def zoom_in (self):
        scale_tr = QtGui.QTransform()
        scale_tr.scale(UiVentana.factor, UiVentana.factor)

        tr = self._view.transform() * scale_tr
        self._view.setTransform(tr)

    @QtCore.pyqtSlot()
    def zoom_out (self):
        scale_tr = QtGui.QTransform()
        scale_tr.scale(UiVentana.factor, UiVentana.factor)

        scale_inverted, invertible = scale_tr.inverted()

        if invertible:
            tr = self._view.transform() * scale_inverted
            self._view.setTransform(tr)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = UiVentana()
    ui.show()
    sys.exit(app.exec_())