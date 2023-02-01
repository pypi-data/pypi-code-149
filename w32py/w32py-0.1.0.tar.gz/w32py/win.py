from typing import Any

from pythoncom import CoInitialize as _CoInitialize
from pythoncom import CoUninitialize as _CoUninitialize
from pythoncom import PumpWaitingMessages as _PumpWaitingMessages
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
