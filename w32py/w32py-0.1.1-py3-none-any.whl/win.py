from sys import argv as _argv
from typing import Any

from psutil import process_iter as _process_iter
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QApplication
from pythoncom import CoInitialize as _CoInitialize
from pythoncom import CoUninitialize as _CoUninitialize
from pythoncom import PumpWaitingMessages as _PumpWaitingMessages
from pywinauto import Application
from win32com.client import DispatchWithEvents as _DispatchWithEvents
from win32com.client import EventsProxy


def coInitialize() -> None:
    _CoInitialize()


def coUninitialize() -> None:
    _CoUninitialize()


def pumpWaitingMessages() -> bool:
    return int(_PumpWaitingMessages()) != 1


def dispatchWithEvents(clsid: Any, user_event_class: Any) -> EventsProxy:
    return _DispatchWithEvents(clsid, user_event_class)


def startApplication(cmd: str, *, backend: str = "win32") -> Application:
    return Application(backend=backend).start(cmd)


def isRunning(names: set[str]) -> bool:
    for proc in _process_iter():
        if proc.name() in names:
            return True
    return False


def qAxWidget(control: str) -> QAxWidget:
    return QAxWidget(control)


def qApplication() -> QApplication:
    return QApplication(_argv)


def qEventLoop() -> QEventLoop:
    return QEventLoop()
