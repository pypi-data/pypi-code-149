from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from os.path import dirname
from muphyn.utils.paths import ROOT_DIR

class StartAction(QAction):
    def __init__(self, text: str = "Start", parent=None):
        super().__init__(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/start.svg"), text, parent)

class StopAction(QAction):
    def __init__(self, text: str = "Stop", parent=None):
        super().__init__(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/stop.svg"), text, parent)

class RotateLeftAction(QAction):
    def __init__(self, text: str = "Rotate 90° Left", parent=None):
        super().__init__(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/rotate_left.svg"), text, parent)

class RotateRightAction(QAction):
    def __init__(self, text: str = "Rotate 90° Right", parent=None):
        super().__init__(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/rotate_right.svg"), text, parent)

class UndoAction(QAction):
    def __init__(self, text: str = "Rotate 90° Right", parent=None):
        super().__init__(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/undo.svg"), text, parent)

class RedoAction(QAction):
    def __init__(self, text: str = "Rotate 90° Right", parent=None):
        super().__init__(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/redo.svg"), text, parent)

class DeleteAction(QAction):
    def __init__(self, text: str = "Delete", parent=None):
        super().__init__(QIcon(ROOT_DIR + "/" + "packages/interface/assets/GeneralIcons/delete.svg"), text, parent)