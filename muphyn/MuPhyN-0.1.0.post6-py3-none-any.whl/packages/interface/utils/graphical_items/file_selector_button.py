from typing import Iterable
from PyQt5.QtCore import QEventLoop, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QPushButton

from muphyn.packages.core.utils.log_manager import LogManager

class AbstractFileDialogButton(QPushButton):

    accepted = pyqtSignal()
    rejected = pyqtSignal()

    SupportedFileModes = [
        QFileDialog.FileMode.AnyFile,
        QFileDialog.FileMode.Directory,
        QFileDialog.FileMode.ExistingFile,
        QFileDialog.FileMode.ExistingFiles,
    ]

    def __init__(self, file_mode: QFileDialog.FileMode, parent = None):
        super().__init__("Ouvrir", parent)

        # Init path value
        self.path = None

        # FileMode
        self.file_mode = file_mode

        # Connect button
        self.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        # Open a file dialog
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(self.file_mode)

        # Open file dialog
        self.file_dialog.open()

        # Create wait for file selector blocking loop
        wait_for_file_selected_loop = QEventLoop()
        # Accepted event
        self.file_dialog.accepted.connect(self.handle_accepted_event)
        self.file_dialog.accepted.connect(wait_for_file_selected_loop.exit)

        # Rejected event
        self.file_dialog.rejected.connect(self.handle_rejected_event)
        self.file_dialog.rejected.connect(wait_for_file_selected_loop.exit)
        wait_for_file_selected_loop.exec()

    def handle_accepted_event(self):
        self.handle_selected_files(self.file_dialog.selectedFiles())

    def handle_rejected_event(self):
        self.rejected.emit()

    def handle_selected_files(self, selected_files: Iterable[str]) -> None:
        raise(NotImplementedError(f"{type(self).__name__}.handle_selected_files() not implemented yet"))

class AnyFileSelectorButton(AbstractFileDialogButton):

    def __init__(self, parent = None):
        super().__init__(QFileDialog.FileMode.AnyFile, parent)

    def handle_selected_files(self, selected_files: Iterable[str]) -> None:
                
        # SelectedFiles must contain only one path
        if len(selected_files) == 1: 
            # Change path value
            self.path = selected_files[0]

            # Emit file path has changed
            self.accepted.emit()
        else:
            self.rejected.emit()

class DirectorySelectorButton(AbstractFileDialogButton):

    def __init__(self, parent = None):
        super().__init__(QFileDialog.FileMode.Directory, parent)

    def handle_selected_files(self, selected_files: Iterable[str]) -> None:
                
        # SelectedFiles must contain only one directory
        if len(selected_files) == 1: 
            # Change path value
            self.path = selected_files[0]

            # Emit file path has changed
            self.accepted.emit()
        else:
            self.rejected.emit()

class ExistingFileSelectorButton(AbstractFileDialogButton):

    def __init__(self, parent=None):
        super().__init__(QFileDialog.FileMode.ExistingFile, parent)

    def handle_selected_files(self, selected_files: Iterable[str]) -> None:

        # SelectedFiles must contain only one file
        if len(selected_files) == 1: 
            # Change path value
            self.path = selected_files[0]

            # Emit accepted
            self.accepted.emit()
        else:
            # Emit rejected
            self.rejected.emit()

class ExistingFilesSelectorButton(AbstractFileDialogButton):

    def __init__(self, parent=None):
        super().__init__(QFileDialog.FileMode.ExistingFiles, parent)

    def handle_selected_files(self, selected_files: Iterable[str]) -> None:

        # SelectedFiles must contain at least one file
        if len(selected_files) > 0: 
            # Change path value
            self.path = selected_files

            # Emit accepted
            self.accepted.emit()
        else:
            # Emit rejected
            self.rejected.emit()

# Factory
def file_selector_button(file_mode: QFileDialog.FileMode, parent=None) -> AbstractFileDialogButton:
    if file_mode == QFileDialog.FileMode.AnyFile:
        return AnyFileSelectorButton(parent)
    elif file_mode == QFileDialog.FileMode.Directory:
        return DirectorySelectorButton(parent)
    elif file_mode == QFileDialog.FileMode.ExistingFile:
        return ExistingFileSelectorButton(parent)
    elif file_mode == QFileDialog.FileMode.ExistingFiles:
        return ExistingFilesSelectorButton(parent)
    else:
        supported_file_modes = '\n - '.join(AbstractFileDialogButton.SupportedFileModes)
        LogManager().error(f"Unsupported QFileDialog.FileMode value given: {file_mode}.\nList of supported QFileDialog.FileMode:\n - {supported_file_modes}")