from typing import Iterable
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLineEdit

from muphyn.packages.interface.properties_pages.data_property_widgets.abstract_property_widget import AbstractPropertyWidget
from muphyn.packages.interface.utils.graphical_items.file_selector_button import file_selector_button, ExistingFilesSelectorButton

class AbstractPathPropertyWidget(AbstractPropertyWidget):

    def __init__(self, file_mode: QFileDialog.FileMode, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)
        
        # Init VBoxLayout
        layout = QHBoxLayout()

        # Add text field
        self.textfield = QLineEdit()
        self.textfield.editingFinished.connect(self.on_textfield_path_edited)

        # Add button to explore file
        self.select_path_button = file_selector_button(file_mode)
        self.select_path_button.accepted.connect(self.on_path_selector_accepted)

        # Set Layout
        layout.addWidget(self.textfield, 1)
        layout.addWidget(self.select_path_button)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def on_path_selector_accepted(self):
        # Change path value
        self.setValue(self.select_path_button.path)

    def on_textfield_path_edited(self):
        # change path value
        self.setValue(self.textfield.text())

    def setValue(self, new_value: str):
        self._value = new_value

        # Update LineEdit
        if self.textfield.text() != new_value:
            self.textfield.setText(new_value)

        # Emit path changed
        self.valueChanged.emit()
        

class AnyFilePropertyWidget(AbstractPathPropertyWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(QFileDialog.FileMode.AnyFile, parent)        

class DirectoryPropertyWidget(AbstractPathPropertyWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(QFileDialog.FileMode.Directory, parent)

class ExistingFilePropertyWidget(AbstractPathPropertyWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(QFileDialog.FileMode.ExistingFile, parent)


class ExistingFilesPropertyWidget(AbstractPropertyWidget):

    def __init__(self, parent = None, flags = Qt.Widget) -> None:
        super().__init__(parent, flags)

        # Path
        self._value = ""

        # Init VBoxLayout
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Add button to explore file
        self.select_path_button = ExistingFilesSelectorButton()
        self.select_path_button.accepted.connect(self.on_path_selector_accepted)

        # Set Layout
        layout.addWidget(self.select_path_button)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def on_path_selector_accepted(self):
        # Change path value
        self.setValue(self.select_path_button.path)

    def setValue(self, new_value: Iterable[str]):
        self._value = new_value

        # Emit path changed
        self.valueChanged.emit()
