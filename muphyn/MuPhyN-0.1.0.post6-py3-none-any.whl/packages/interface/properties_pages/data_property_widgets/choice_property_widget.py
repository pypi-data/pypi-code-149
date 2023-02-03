
from typing import Any
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QComboBox

from muphyn.packages.interface.properties_pages.data_property_widgets.abstract_property_widget import AbstractPropertyWidget
from muphyn.packages.core.utils.log_manager import LogManager

class ChoicePropertyWidget(AbstractPropertyWidget):
    def __init__(self, parameter_to_edit: dict, parent=None, flags=Qt.Widget) -> None:
        super().__init__(parent, flags)

        # Choices
        self._choices: list | dict = parameter_to_edit["choices"] if "choices" in parameter_to_edit else []

        # Init VBoxLayout
        layout = QHBoxLayout()

        # Index
        self._index = -1
        if "value" in parameter_to_edit:
            self._value = parameter_to_edit["value"]
            if type(self._choices) == list and self._value in self._choices:
                self._index = self._choices.index(self._value)
            elif type(self._choices) == dict and self._value in self._choices.values():
                self._index = list(self._choices.values()).index(self._value)

        # Double Spin
        self.combo_box = QComboBox()
        self.combo_box.addItems(self._choices)
        self.combo_box.setCurrentIndex(self._index)
        self.combo_box.currentIndexChanged.connect(self.onNewIndex)

        # Set Layout
        layout.addWidget(self.combo_box, 1)
        self.setLayout(layout)

    def onNewIndex(self, newIndex: int):
        if self._index != newIndex:
            self._index = newIndex
            if type(self._choices) == list:
                self.setValue(self._choices[newIndex])
            elif type(self._choices) == dict:
                key = list(self._choices.keys())[newIndex]

                self.setValue(self._choices[key])

    def setValue(self, new_value: Any):
        if self._value != new_value:
            # Get new value
            self._value = new_value

            # Emit value changed
            self.valueChanged.emit()