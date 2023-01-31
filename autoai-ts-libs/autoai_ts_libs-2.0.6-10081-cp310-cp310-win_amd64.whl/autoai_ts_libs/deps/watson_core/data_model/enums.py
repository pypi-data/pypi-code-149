# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Enumeration data structures map from strings to integers and back.
"""

import json
import munch

from autoai_ts_libs.deps.watson_core.toolkit import alog
from ..toolkit.errors import error_handler

from autoai_ts_libs.deps.watson_core import toolkit
from . import protobufs


log = alog.use_channel("DATAM")
error = error_handler.get(log)


class EnumBase(munch.Munch):
    """Enumerations maps from string to integer."""

    def __init__(self, name):
        proto_enum = getattr(protobufs, name, None)
        if proto_enum is None:
            error(
                "<COR71783952E>",
                AttributeError("could not locate protobuf enum `{}`".format(name)),
            )

        if not toolkit.isprotobufenum(proto_enum):
            error(
                "<COR71783964E>",
                AttributeError("`{}` is not a valid protobuf enumeration"),
            )

        super().__init__(proto_enum.items())

    def __repr__(self):
        return json.dumps(self, indent=2)


class _EnumRevInject(munch.Munch, dict):
    """Use multiple inheritance dependency injection to reverse the order
    of the enum map before passing to dict parent.  In order to understand
    this consider the method resolution order (MRO) for __init__ in this
    class hierarchy:

    EnumRevBase -> EnumBase -> Munch -> _EnumRevInject -> Munch -> dict -> object
    """

    def __init__(self, forward_map):
        # reverse keys and values and call munch constructor
        super().__init__({value: key for key, value in forward_map})


class EnumRevBase(EnumBase, _EnumRevInject):
    """Reverse enumeration maps from integer to string."""


__all__ = ["import_enums"]


def import_enums(current_globals):
    """Add all enums and their reverse enum mappings a module's global symbol table. Note that
    we also update __all__. In general, __all__ controls the stuff that comes with a wild (*)
    import.

    Examples tend to make stuff like this easier to understand. Let's say the first name we hit
    is the Entity Mention Type. Then, after the first cycle through the loop below, you'll see
    something like:

        '__all__': ['import_enums', 'EntityMentionType', 'EntityMentionTypeRev']
        'EntityMentionType': { "MENTT_UNSET": 0, "MENTT_NAM": 1, ... , "MENTT_NONE": 4}
        'EntityMentionTypeRev': { "0": "MENTT_UNSET", "1": "MENTT_NAM", ... , "4": "MENTT_NONE"}

    since this is called explicitly below, you can thank this function for automagically syncing
    your enums (as importable from this file) with the data model.

    Args:
        current_globals: dict
            global dictionary from your data model package __init__ file.
    """
    # Like the proto imports, we'd one day like to do this with introspection using something
    # like below, but can't because our wheel is compiled. If you can think of a cleaner way
    # to do this, open a PR!
    # caller = inspect.stack()[1]
    # caller_module = inspect.getmodule(caller[0])
    # current_globals = caller_module.__dict__

    # Add the str->int (EnumBase) and int->str (EnumRevBase) mapping for each enum
    # to the calling module's symbol table, then update __all__ to include the names
    # for the added objects.
    for name in current_globals["protobufs"].all_enum_names:
        globals()[name] = EnumBase(name)
        current_globals[name] = globals()[name]
        rev_name = name + "Rev"
        globals()[rev_name] = EnumRevBase(name)
        current_globals[rev_name] = globals()[rev_name]
        __all__.append(name)
        __all__.append(rev_name)


import_enums(globals())
