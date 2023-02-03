import numpy as np
import sys
import re
from typing import Any

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeyEvent
from PyQt5.QtWidgets import QCheckBox, QDoubleSpinBox, QHBoxLayout, QLabel, QLineEdit, QSpinBox, QAction

from muphyn.packages.core.plci_core_data_type import DataType
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.interface.properties_pages.data_property_widgets.abstract_property_widget import AbstractPropertyWidget
from muphyn.packages.interface.widgets.BaseWidgets.Button import ArrowButton
from muphyn.utils.paths import ROOT_DIR
from muphyn.packages.core.utils.global_env_variables_manager import GlobalEnvVariablesManager
from muphyn.packages.core.utils.regexes import *

class PropertyLineEdit(AbstractPropertyWidget):

    def __init__(self, parameter_to_edit, propertyType: DataType, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)

        # Init Layout
        layout = QHBoxLayout()

        # 
        self.parameter_to_edit = parameter_to_edit
        self.propertyType: DataType = propertyType

        # Init Line Edit
        self.line_edit = QLineEdit()
        self.line_edit.editingFinished.connect(self.line_edit_editing_finished)
        self.line_edit_tooltip = QAction(
            QIcon(ROOT_DIR + "/" +"packages/interface/assets/GeneralIcons/error.svg"), 
            ""
        )

        # Set Layout
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def line_edit_editing_finished(self):
        self.setValue(self.line_edit.text())

    def setError(self, isError: bool, message: str = None):
        if isError:
            # Test if Tool Tip Icon is in Line Edit
            if not self.line_edit_tooltip in self.line_edit.actions():
                self.line_edit.addAction(
                    self.line_edit_tooltip, 
                    QLineEdit.ActionPosition.TrailingPosition
                )

            # Set Tool Tip message
            if message is not None:
                self.line_edit_tooltip.setToolTip(message)
            
        else:
            # Remove tooltip Icon
            if self.line_edit_tooltip in self.line_edit.actions():                
                self.line_edit.removeAction(self.line_edit_tooltip)
        
    def setValue(self, new_value: str):
        # Remove leading and ending whitespaces
        new_value = str(new_value).strip()

        # Handle Comma decimal separator
        if re.match(CommaScientificNumberRegex, new_value) or re.match(CommaFloatRegex, new_value):
            new_value = new_value.replace(",", ".")

        if self.propertyType == DataType.INT:
            # Test if empty string
            if new_value == "" or new_value == "+" or new_value == "-":
                # Valid Value
                self.validValue(0)

            # Test if floating value
            elif re.match(DotFloatRegex, new_value):
                # Valid Value
                self.validValue(int(float(new_value)))
            
            elif re.match(DotScientificNumberRegex, new_value):
                # Valid Value
                self.validValue(new_value)

            # Test if variable name exists 
            elif new_value in GlobalEnvVariablesManager().global_vars:
                # Get global variable
                global_var = GlobalEnvVariablesManager().global_vars[new_value]

                if type(global_var) == int or type(global_var) == float:
                    # Valid Value
                    self.validValue(new_value)
                else:
                    self.setError(True, f"Integer object expected: {type(global_var)} instead")
                    LogManager().error(TypeError(f"Integer object expected: {type(global_var)} instead"))
            else:
                self.setError(True, f"Invalid input: Please set a int value or an existing variable name")
                LogManager().error(TypeError(f"Invalid input: Not a int neither an existing variable name"))

        elif self.propertyType == DataType.FLOAT:

            # Test if empty string
            if new_value == "" or new_value == "+" or new_value == "-":
                # Valid Value
                self.validValue(0.0)

            # Test if point floating value
            elif re.match(DotFloatRegex, new_value):
                # Valid Value
                self.validValue(float(new_value))
            
            elif re.match(DotScientificNumberRegex, new_value):
                # Valid Value
                self.validValue(new_value)

            elif new_value in GlobalEnvVariablesManager().global_vars:
                # Get global variable
                global_var = GlobalEnvVariablesManager().global_vars[new_value]

                if type(global_var) == float or type(global_var) == int:
                    # Set Checked
                    self.validValue(new_value)
                else:
                    self.setError(True, f"Float object expected: {type(global_var)} instead")
                    LogManager().error(TypeError(f"Float object expected: {type(global_var)} instead"))
            else:
                self.setError(True, f"Invalid input: Please set a float value or an existing variable name")
                LogManager().error(TypeError(f"Invalid input: Not a float neither an existing variable name"))

    def validValue(self, new_value: Any):
        # Save value
        self._value = new_value

        # Set Checked
        self.line_edit.setText(str(new_value))

        # Emit value changed
        self.valueChanged.emit()

        # Reset Error
        self.setError(False)



class BooleanPropertyWidget(AbstractPropertyWidget):

    def __init__(self, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)
        
        # Value
        self._value = False

        # Init VBoxLayout
        layout = QHBoxLayout()

        # Double Spin
        self.check_box = QCheckBox()
        self.check_box.toggled.connect(self.on_check_box_value_changed)

        # Set Layout
        layout.addWidget(self.check_box)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def on_check_box_value_changed(self, checked: bool):
        self.setValue(checked)

    def setValue(self, new_value: bool):
        if self._value != new_value:
            # Write new value
            self._value = new_value

            # Set Checked
            self.check_box.setCheckState(Qt.CheckState.Checked if new_value else Qt.CheckState.Unchecked)

            # Emit value changed
            self.valueChanged.emit()

class DoublePropertyWidget(AbstractPropertyWidget):

    # Constants
    DotFloatRegex = r"^[-+]?[0-9]*\.[0-9]*$"

    def __init__(self, parameter_to_edit: dict, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)

        # Value
        self._value = 0.0

        # Init VBoxLayout
        layout = QHBoxLayout()

        # Exponential value
        self.exp = 0

        # Get min/max values
        self.min_value = -sys.float_info.max
        if "min" in parameter_to_edit:
            min_value = parameter_to_edit["min"]
            try:
                self.min_value = max(float(min_value), self.min_value)
            except:
                LogManager().error(f"DoublePropertyWidget.__init__(): given 'min' value not a integer: {min_value}")


        self.max_value = sys.float_info.max
        if "max" in parameter_to_edit:
            max_value = parameter_to_edit["max"]
            try:
                self.max_value = min(float(max_value), self.max_value)
            except:
                LogManager().error(f"DoublePropertyWidget.__init__(): given 'max' value not a integer: {max_value}")


        # Double Spin
        self.double_spin_box = QDoubleSpinBox()
        self.double_spin_box.setRange(self.min_value, self.max_value)
        self.double_spin_box.valueChanged.connect(self.double_spin_box_value_changed)

        # Left arrow
        self.decrease_exp_button = ArrowButton(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/right_arrow.svg"), "")
        self.decrease_exp_button.clicked.connect(self.decrease_exp_button_clicked)

        # Right arrow
        self.increase_exp_button = ArrowButton(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/left_arrow.svg"), "")
        self.increase_exp_button.clicked.connect(self.increase_exp_button_clicked)

        # Text cursor event
        self.double_spin_box_line_edit = self.double_spin_box.lineEdit()
        self.double_spin_box_line_edit.editingFinished.connect(self.line_edit_editing_finished)
        self.double_spin_box_line_edit.returnPressed.connect(self.line_edit_editing_finished)

        # Set Layout
        layout.addWidget(self.double_spin_box, stretch=1)
        layout.addWidget(self.increase_exp_button)
        layout.addWidget(self.decrease_exp_button)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def update_step_value(self):
        # Add point in text if doesn't exists
        double_spin_box_text = self.double_spin_box.cleanText()

        # If empty
        if double_spin_box_text == "":
            self.double_spin_box.setValue(0.0)
        # If integer
        elif re.match(IntegerRegex, double_spin_box_text):
            self.double_spin_box.setValue(float(self.double_spin_box.value()))

        # Get number of digits interger & decimal parts
        # If comma decimal separator
        if re.match(CommaFloatRegex, double_spin_box_text):
            integer_digits, decimal_digits = [len(part) for part in self.double_spin_box.cleanText().split(",", maxsplit=2)]
        
        # If dot decimal separator
        elif re.match(DotFloatRegex, double_spin_box_text):
            integer_digits, decimal_digits = [len(part) for part in self.double_spin_box.cleanText().split(".", maxsplit=2)]

        if self.exp >= 0:
            # Change value in integers
            if  self.exp >= integer_digits:
                # Block increasement of exp if exceed number of interger part digits
                self.exp = integer_digits - 1

            # Calculate cursor position
            cursor_position = integer_digits - self.exp - 1

            # Set Cursor
            self.double_spin_box_line_edit.setSelection(cursor_position, 1)
        else:
            # Change value in decimals

            # Absolute value of exponential
            abs_exp = abs(self.exp)
            if decimal_digits < abs_exp:
                # Update number of decimals in the DoubleSpinBox
                self.double_spin_box.setDecimals(abs_exp)

            # Calculate cursor position
            cursor_position = integer_digits + abs_exp

            # Set Cursor
            self.double_spin_box_line_edit.setSelection(cursor_position, 1)

        # Update DoubleSpinBox step size
        self.double_spin_box.setSingleStep(10**self.exp)

    def decrease_exp_button_clicked(self):
        self.exp -= 1
        self.update_step_value()

    def increase_exp_button_clicked(self):
        self.exp += 1
        self.update_step_value()

    def line_edit_editing_finished(self):
        # Set exp
        if self.exp > len(self.double_spin_box_line_edit.text()):
            self.setExp(len(self.double_spin_box_line_edit.text()))

    def double_spin_box_value_changed(self, new_value: float):
        self.setValue(new_value)

    def setExp(self, new_exp: int):
        if self.exp != new_exp:
            self.exp = new_exp
            self.update_step_value()

    def setValue(self, new_value: float):
        if self._value != new_value:
            # Write new value
            self._value = new_value

            # Set value on graphical element
            if new_value != self.double_spin_box.value():
                self.double_spin_box.setValue(new_value)

            # Emit value changed
            self.valueChanged.emit()

    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        if self.double_spin_box_line_edit.hasFocus():
            if a0.key() == Qt.Key.Key_Left:
                self.increase_exp_button_clicked()
            elif a0.key() == Qt.Key.Key_Right:
                self.decrease_exp_button_clicked()

        return super().keyReleaseEvent(a0)
            

class IntegerPropertyWidget(AbstractPropertyWidget):

    def __init__(self, parameter_to_edit, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)

        # Value
        self._value = 0.0

        # Init VBoxLayout
        layout = QHBoxLayout()

        # Exponential value
        self.exp = 0

        # Get min/max values
        int32_info = np.iinfo(np.int32)
        self.min_value = int32_info.min
        if "min" in parameter_to_edit:
            min_value = parameter_to_edit["min"]
            try:
                self.min_value = max(int(float(min_value)), self.min_value)
            except:
                LogManager().error(f"IntegerPropertyWidget.__init__(): given 'min' value not a integer: {min_value}")


        self.max_value = int32_info.max
        if "max" in parameter_to_edit:
            max_value = parameter_to_edit["max"]
            try:
                self.max_value = min(int(float(max_value)), self.max_value)
            except:
                LogManager().error(f"IntegerPropertyWidget.__init__(): given 'max' value not a integer: {max_value}")


        # Integer Spin
        self.integer_spin_box = QSpinBox()
        self.integer_spin_box.setRange(self.min_value, self.max_value)
        self.integer_spin_box.valueChanged.connect(self.integer_spin_box_value_changed)

        # Left arrow
        self.decrease_exp_button = ArrowButton(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/right_arrow.svg"), "")
        self.decrease_exp_button.clicked.connect(self.decrease_exp_button_clicked)

        # Right arrow
        self.increase_exp_button = ArrowButton(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/left_arrow.svg"), "")
        self.increase_exp_button.clicked.connect(self.increase_exp_button_clicked)

        # Text cursor event
        self.integer_spin_box_line_edit = self.integer_spin_box.lineEdit()
        self.integer_spin_box_line_edit.editingFinished.connect(self.line_edit_editing_finished)
        self.integer_spin_box_line_edit.returnPressed.connect(self.line_edit_editing_finished)

        # Set Layout
        layout.addWidget(self.integer_spin_box, stretch=1)
        layout.addWidget(self.increase_exp_button)
        layout.addWidget(self.decrease_exp_button)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def update_step_value(self):
        # Get number of digits interger & decimal parts
        integer_digits = len(self.integer_spin_box.cleanText())

        # Change value in integers
        if  self.exp >= integer_digits:
            # Block increasement of exp if exceed number of interger part digits
            self.exp = integer_digits - 1

        # Calculate cursor position
        cursor_position = integer_digits - self.exp - 1

        # Set Cursor
        self.integer_spin_box_line_edit.setSelection(cursor_position, 1)

        # Update DoubleSpinBox step size
        self.integer_spin_box.setSingleStep(10**self.exp)

    def decrease_exp_button_clicked(self):
        self.setExp(self.exp - 1)

    def increase_exp_button_clicked(self):
        self.setExp(self.exp + 1)

    def integer_spin_box_value_changed(self, new_value: float):
        self.setValue(new_value)

    def line_edit_editing_finished(self):
        if self.exp > len(self.integer_spin_box_line_edit.text()):
            self.setExp(len(self.integer_spin_box_line_edit.text()))

    def setExp(self, new_exp: int):
        if new_exp < 0:
            new_exp = 0

        if self.exp != new_exp:
            self.exp = new_exp
            self.update_step_value()

    def setValue(self, new_value: str|int):
        if new_value == "":
            new_value = 0

        if type(new_value) == str:
            new_value = int(new_value)

        if self._value != new_value:
            # Write new value
            self._value = new_value

            # Set value on graphical element
            if new_value != self.integer_spin_box.value():
                self.integer_spin_box.setValue(new_value)

            # Emit value changed
            self.valueChanged.emit()

    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        if self.integer_spin_box_line_edit.hasFocus():
            if a0.key() == Qt.Key.Key_Left:
                self.increase_exp_button_clicked()
            elif a0.key() == Qt.Key.Key_Right:
                self.decrease_exp_button_clicked()

        return super().keyReleaseEvent(a0)
            
class StringPropertyWidget(AbstractPropertyWidget):

    def __init__(self, parameter_to_edit: dict, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)
        
        # Value
        self._value = False

        # Init VBoxLayout
        layout = QHBoxLayout()

        # Set limit characters
        self.limit_characters = -1
        if "maxLength" in parameter_to_edit:
            limit_characters = parameter_to_edit["maxLength"]
            try:
                self.limit_characters = max(int(limit_characters), self.limit_characters)
            except:
                LogManager().error(f"StringPropertyWidget.__init__(): given 'maxLength' value not a valid value: {limit_characters}")

        # Double Spin
        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(self.limit_characters)
        self.line_edit.editingFinished.connect(self.line_edit_editing_finished)

        # Set Layout
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def line_edit_editing_finished(self):
        self.setValue(self.line_edit.text())

    def setValue(self, new_value: str):
        if self._value != new_value:
            # Write new value
            self._value = new_value

            # Set Checked
            self.line_edit.setText(new_value)

            # Emit value changed
            self.valueChanged.emit()

class UnknownTypePropertyWidget(AbstractPropertyWidget):

    def __init__(self, type_name: str, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)
        
        # Value
        self._value = False

        # Type Name
        self._type_name = type_name

        # Init VBoxLayout
        layout = QHBoxLayout()

        # Double Spin
        self.label = QLabel(f"Uknown Type : {type_name}")

        # Set Layout
        layout.addWidget(self.label)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def setValue(self, new_value: str):
        LogManager().error(f"Can't set value of UnknownType : {self._type_name}")