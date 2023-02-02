import typing

from PyQt5.QtCore import QPoint, QPointF
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsObject

def findMainWindow() -> typing.Union[QMainWindow, None]:
    # Global function to find the (open) QMainWindow in application
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if isinstance(widget, QMainWindow):
            return widget
    return None