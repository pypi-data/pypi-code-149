import tomllib
import os
import re
import inspect
"""
Author: Levi Schanding

"""


def _add_init_args_and_annotations_to_cls(cls: object) -> object:
    
    clsargspec = inspect.getfullargspec(cls)
    cls.__init_args = clsargspec.args[1:]
    cls.__init_annotations = clsargspec.annotations
    return cls



def _load_arguments(params: list, annotations: dict[str], arguments: dict[str]) -> list:
    return [
        annotations[param](
            *_load_arguments(
                annotations[param].__init_args,
                annotations[param].__init_annotations,
                arguments[param]
            )
        )
        if param in annotations.keys() and hasattr(annotations[param], 'load_from_toml') 
        else arguments[param]
        for param in params
    ]



def toml_init(cls: object):
    if cls is None:
        raise ValueError("A class must be passed! None is not allowed!")
    toml_dict: dict[str]
    cls = _add_init_args_and_annotations_to_cls(cls)

    @classmethod
    def load_from_toml(cls: object, filename: str) -> object:

        if not os.path.exists(filename):
            raise FileNotFoundError(f"Could not locate TOML '{filename}'")

        if not re.search("\.toml$", filename):
            raise tomllib.TOMLDecodeError(f"Expecting file ending in '.toml', received '{filename}'")

        with open(filename, "rb") as toml_handle:
            toml: dict[str] = tomllib.load(toml_handle)

        return cls(*_load_arguments(
            cls.__init_args, 
            cls.__init_annotations,
            toml
        ))

    @classmethod
    def load_from_toml_string(cls: object, toml_string: str):
        if not isinstance(toml_string, str):
            raise TypeError("'toml_string' must be of type 'str'!")

        toml: dict[str] = tomllib.loads(toml_string)

        return cls(*_load_arguments(
            cls.__init_args, 
            cls.__init_annotations,
            toml
        ))
    



    # Add functions to class
    cls.load_from_toml = load_from_toml
    cls.load_from_toml_string = load_from_toml_string
    return cls