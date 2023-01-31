import sys
from typing import Optional, Union

import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QAction, QFileDialog, QLabel, \
    QActionGroup
from numpy.typing import ArrayLike

from primawera import lut
from primawera.canvas2d import Canvas2D
from primawera.canvas3d import Canvas3D
from primawera.canvascomplex import CanvasComplex
from primawera.loading import load_data


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, filepath: Optional[str] = None,
                 data: Optional[ArrayLike] = None, bitdepth: int = -1,
                 mode: str = ""):
        super(MainWindow, self).__init__()

        if data is not None and (bitdepth == -1 or mode == ""):
            print(
                "Error: Provided raw data but bitdepth and mode is not specified!")
            self.close()

        self.setWindowTitle("Primawera")
        # self.setMinimumSize(300, 300)

        # Set up fonts
        self.font = QFont("Noto Sans", 12)
        self.setFont(self.font)

        # Set up LUTs
        lut.fill_luts()

        # Get the size of the desktop
        desktop = QApplication.desktop()
        screen_geometry = desktop.screenGeometry(0)
        self.desktop_width = screen_geometry.width()
        self.desktop_height = screen_geometry.height()

        self.canvas = None

        # Create menu
        self._create_actions()
        self._connect_actions()
        self._create_menu_bar()

        # Help window
        self._help_window = None

        # Layout
        if filepath is not None:
            data, bitdepth, mode = load_data(filepath)
            self._start_visualiser(data, bitdepth, mode)
        elif data is not None:
            self._start_visualiser(data, bitdepth,
                                   mode)  # TODO: figure out mode
        else:
            self.setCentralWidget(QLabel("Please open an image."))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_PageDown:
            self.canvas.previous_frame()
        elif event.key() == QtCore.Qt.Key_PageUp:
            self.canvas.next_frame()

    def _start_visualiser(self, data, bitdepth, mode):
        if mode == "C":
            # Complex data
            self.canvas = CanvasComplex(data, bitdepth, mode,
                                        self.desktop_height,
                                        self.desktop_width, {}, {})
        elif data.shape[0] == 1:
            # 2D data
            self.canvas = Canvas2D(data, bitdepth, mode, self.desktop_height,
                                   self.desktop_width, {}, {})
        else:
            self.canvas = Canvas3D(data, bitdepth, mode,
                                   self.desktop_height,
                                   self.desktop_width, {},
                                   {})
        self.canvas.menus_changed_signal.connect(self._refresh_menu_bar)
        self.setCentralWidget(self.canvas)
        self._refresh_menu_bar()

    @pyqtSlot()
    def _refresh_menu_bar(self):
        # Clear menubar
        self._create_menu_bar()

        # Update menu with available filters
        menubar = self.menuBar()
        canvas_menus = self.canvas.get_menus()
        for menu_title, actions in canvas_menus:
            # Add the menu
            new_menu = menubar.addMenu(menu_title)

            # Set exclusivity
            action_group = QActionGroup(self)
            for idx, action in enumerate(actions):
                action_group.addAction(action)
                new_menu.addAction(action)

    def _create_menu_bar(self):
        menubar = self.menuBar()
        menubar.clear()

        # File menu
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(self.open_file_action)
        file_menu.addAction(self.open_folder_action)
        file_menu.addAction(self.exit_action)

        # Help menu
        help_menu = menubar.addMenu("&Help")
        help_menu.addAction(self.about_action)
        help_menu.addAction(self.help_commands_action)

    def _create_actions(self):
        self.open_file_action = QAction("Open file...")
        self.open_folder_action = QAction("Open folder...")
        self.exit_action = QAction("Exit")
        self.about_action = QAction("About")
        self.help_commands_action = QAction("Commands")

    def _connect_actions(self):
        self.exit_action.triggered.connect(self.close)
        self.open_file_action.triggered.connect(self.open_file)
        self.open_folder_action.triggered.connect(self.open_folder)
        self.help_commands_action.triggered.connect(self.help_commands)

    def resizeEvent(self, event):
        desktop = QApplication.desktop()
        screen_geometry = desktop.screenGeometry(0)
        self.desktop_width = screen_geometry.width()
        self.desktop_height = screen_geometry.height()
        if self.canvas is not None:
            self.canvas.update_desktop_size(width=self.desktop_width,
                                            height=self.desktop_height)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open file", ".",
                                                   "Image file (*.jpg *.png"
                                                   " *.h5 *.tif *.tiff)")
        if file_name == "":
            # User does not select a file
            return
        data, bitdepth, mode = load_data(file_name)
        self._start_visualiser(data, bitdepth, mode)

    def open_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Open folder",
                                                       ".",
                                                       QFileDialog.ShowDirsOnly
                                                       )
        if folder_name == "":
            # No folder was selected
            return
        data, bitdepth, mode = load_data(folder_name)
        self._start_visualiser(data, bitdepth, mode)

    def help_commands(self):
        self._help_window = QLabel(
            "--- Scaling ---\n"
            "+\tTo scale up the image size by 2\n"
            "-\tTo scale down the image size by 2\n"
            "--- Frames ---\n"
            "n\tSwitch to next frame\n"
            "p\tSwitch to previous frame\n"
        )
        self._help_window.show()


def print_help(name: str) -> None:
    print(f"Usage: {name} FILEPATH\n"
          f"-----\n"
          f"Filepath specifies path to an image file. It is optional.\n\n")


def run_app(data: Union[str, ArrayLike], bitdepth: int = -1, mode: str = ""):
    app = QtCore.QCoreApplication.instance()
    app_created = False
    if app is None:
        print("Creating app")
        app = QtWidgets.QApplication(sys.argv)
        app_created = True

    if type(data) == str:
        _window = MainWindow(filepath=data)
    elif isinstance(data, np.ndarray):
        if len(data.shape) == 2:
            data = np.array([data])
        _window = MainWindow(data=data, bitdepth=bitdepth, mode=mode)
    else:
        print("Error: Invalid input data. Cannot run the app.")
        return False
    _window.show()

    if app_created:
        app.exec_()
    return _window


# Inspired by:
# https://cyrille.rossant.net/making-pyqt4-pyside-and-ipython-work-together/
def create_window(filepath: str = None):
    app_created = False
    app = QtCore.QCoreApplication.instance()
    if app is None:
        print("Creating app")
        app = QtWidgets.QApplication(sys.argv)
        app_created = True
    app.references = set()
    if filepath is not None:
        _window = MainWindow(filepath=filepath)
    else:
        _window = MainWindow()
    app.references.add(_window)
    _window.show()

    if app_created:
        app.exec_()
    return _window


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error: Wrong number of arguments!")
        print_help(sys.argv[0])
        exit(1)

    if len(sys.argv) == 2:
        if type(sys.argv[1]) == str and sys.argv[1] == "--help":
            print_help(sys.argv[0])
            exit(0)

        window = create_window(filepath=sys.argv[1])
    else:
        window = create_window()
