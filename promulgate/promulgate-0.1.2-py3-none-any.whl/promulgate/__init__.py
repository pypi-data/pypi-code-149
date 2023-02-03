from __future__ import annotations
from typing import Callable, TypeVar, Type

T = TypeVar("T", bound="Promulgation")


class Promulgation:
    """
    Promulgation.
    """

    listeners: dict[str, list[Callable[[T], None]]] = {}

    @classmethod
    def subscribe(cls: Type[T], listener: Callable[[T], None]) -> None:
        """
        Register a function as handler for the given event.
        """
        if cls.__name__ not in cls.listeners:
            cls.listeners[cls.__name__] = []

        cls.listeners[cls.__name__].append(listener)

    @classmethod
    def unsubscribe(cls: Type[T], listener: Callable[[T], None]) -> None:
        """
        Unregisters a handler for the given event.
        """
        if cls.__name__ not in cls.listeners:
            cls.listeners[cls.__name__] = []
        cls.listeners[cls.__name__].remove(listener)

    def promulgate(self) -> None:
        """
        Causes the registered handler to be called.
        """
        for listener in self.listeners.get(self.__class__.__name__, []):
            listener(self)
