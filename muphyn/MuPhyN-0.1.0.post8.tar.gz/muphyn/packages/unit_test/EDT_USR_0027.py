
from PyQt5.QtWidgets import QApplication
import sys

from ..interface.main_window import MainWindow 

app = QApplication(sys.argv)
win = MainWindow()

win.show()
sys.exit(app.exec_())