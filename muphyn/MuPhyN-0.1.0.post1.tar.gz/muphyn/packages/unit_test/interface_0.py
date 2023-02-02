from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow (QMainWindow) :
    def __init__ (self) :
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self) :
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("PLCI")

        self._lbl_title = QtWidgets.QLabel(self)
        self._lbl_title.setText("PLCI")
        self._lbl_title.move(50, 50)

        self._btn_b1 = QtWidgets.QPushButton(self)
        self._btn_b1.setText("Button")
        self._btn_b1.clicked.connect(self.btn_b1_clicked)

    def btn_b1_clicked (self) :
        self._lbl_title.setText("Hello world lorem ipsum data Annalisa")
        self._lbl_title.adjustSize()
        print("Clicked !!")


def window() :
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
