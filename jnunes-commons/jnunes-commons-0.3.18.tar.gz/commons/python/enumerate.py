from enum import Enum
from deprecated import deprecated


@deprecated(version='0.3.17', reason='use commons.enumerate.enum_base.EnumBase')
class EnumBase(Enum):
    @classmethod
    def list(cls) -> list:
        return [[key.name, key.value] for key in cls]

    @classmethod
    def tuple(cls) -> tuple:
        return tuple(((key.name, key.value) for key in cls))

    @classmethod
    def dict(cls) -> dict:
        return dict([(key.name, key.value) for key in cls])
