# *****************************************************************#
# (C) Copyright IBM Corporation 2022.                              #
#                                                                  #
# The source code for this program is not published or otherwise   #
# divested of its trade secrets, irrespective of what has been     #
# deposited with the U.S. Copyright Office.                        #
# *****************************************************************#
"""
This module holds utilities for determining the set of modules that are held as
extras sets for the library and for giving useful errors when dependencies are
missing.
"""

# Standard
from typing import Set
import sys

# First Party
from watson_core.model_manager import MODULE_REGISTRY

## Globals #####################################################################

# The name of this library's top-level module
_THIS_PACKAGE = sys.modules[__name__].__package__.partition(".")[0]


## Utilities ###################################################################


def get_extras_modules() -> Set[str]:
    """Get the list of module names that should be managed as extra dependency
    sets
    NOTE: This must be called after all @block, @workflow, and @resource Modules
        have been registered with the the MODULE_REGISTRY, so it should be used
        lazily to create the extras modules _after_ the rest of the library is
        imported.
    Returns:
        extras_modules:  Set[str]
            The set of unique module names that should be managed as extras
    """
    return {
        module.__module__
        for module in MODULE_REGISTRY.values()
        if module.__module__.partition(".")[0] == _THIS_PACKAGE
    }
