import sys

from .display import Display
from .keyboard import Keyboard
from .keyboard.key import Keys
from .mouse import Mouse

__all__ = ['sm', 'keys']

keys = Keys()


class Simulant(Keyboard, Mouse, Display):
    def __init__(self):
        self.os = sys.platform

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<Simulant: {self.os}>"


sm = Simulant()
