import sys
from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, \
                            QHBoxLayout, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # self.window_width, self.window_height = 1200, 800
        # self.setMinimumSize(self.window_width, self.window_height)
        self.setMinimumWidth(1200)
        self.setMaximumHeight(200)
        self.setWindowTitle('Copy to Clipboard Example')
        self.setStyleSheet('height: 65px; font-size: 35px')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.lineEdit = QLineEdit()
        self.btn_copy = QPushButton('Copy to clipboard', clicked=self.copyToClipboard)
        self.btn_paste = QPushButton('Paste from clipboard', clicked=self.pasteFromClipboard)
        self.lbl = QLabel()

        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.btn_copy)
        self.layout.addWidget(self.btn_paste)
        self.layout.addWidget(self.lbl)

    def copyToClipboard(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.lineEdit.text(), mode=cb.Clipboard)
        self.lbl.setText('Content is copied')

    def pasteFromClipboard (self) :
        cb = QApplication.clipboard()
        txt = cb.text(mode=cb.Clipboard)
        print('clipboard :', txt)

if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    
    app = QApplication(sys.argv)
    app.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')