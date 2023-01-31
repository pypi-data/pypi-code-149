"""
This is a utility that automates the process of hoisting module classes from a
colleciton of sub-modules within a block/workflow type.
"""

# Standard
from types import ModuleType

# First Party
from watson_core.module import ModuleBase


def hoist_module_imports(current_globals: dict):
    """This function will inspect all modules within the current globals for any
    ModuleBase types that live in them and will hoist those classes directly
    into the current globals.

    Args:
        current_globals:  dict
            The globals() dict for the block/workflow type module
    """
    new_globals = {}
    for attr in current_globals.values():
        if isinstance(attr, ModuleType):
            for submod_attr_name, submod_attr_val in vars(attr).items():
                if isinstance(submod_attr_val, type) and issubclass(
                    submod_attr_val, ModuleBase
                ):
                    new_globals[submod_attr_name] = submod_attr_val
    current_globals.update(new_globals)
