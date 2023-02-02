from typing import Any
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget

class AbstractPropertyWidget(QWidget):

    valueChanged = pyqtSignal()

    def __init__(self, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)

        self._value = None

    
    # -------------
    # Properties
    # -------------
    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, new_value: Any):
        # Set new value
        self.setValue(new_value)


    # -------------
    # Methods
    # -------------
    def setValue(self, new_value: Any):
        raise(NotImplementedError(f"{type(self).__name__}.setValue() not yet implemented"))