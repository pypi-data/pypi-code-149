from enum import Enum


class EnumBase(Enum):
    @classmethod
    def list(cls) -> list:
        return [[key.name, key.value] for key in cls]

    @classmethod
    def tuple(cls) -> tuple:
        """ Return a tuple with name and value of enumerate.

        (('AB', 'AB desc value'), ('AC', 'AC desc value'))

        :return: tuple
        """
        return tuple(((key.name, key.value) for key in cls))

    @classmethod
    def names(cls) -> tuple:
        return tuple(key.name for key in cls)

    @classmethod
    def values(cls) -> tuple:
        return tuple(key.value for key in cls)

    @classmethod
    def tuple_enumerated(cls, start=0, name: bool = False, value: bool = True):
        if name and value is True:
            return tuple(((enum, key.name, key.value) for enum, key in enumerate(cls, start=start)))
        elif name is True:
            return tuple(((enum, key.name) for enum, key in enumerate(cls, start=start)))
        elif value is True:
            return tuple(((enum, key.value) for enum, key in enumerate(cls, start=start)))

    @classmethod
    def dict(cls) -> dict:
        return dict([(key.name, key.value) for key in cls])
