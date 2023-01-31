# *****************************************************************#
# (C) Copyright IBM Corporation 2022.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

# Standard
import inspect
from enum import Enum

# First party
import alog
from .errors import error_handler


log = alog.use_channel("WIPDC")
error = error_handler.get(log)

################ Constants ##########################################

message_format = "{} is still in the {} phase and subject to change!"

_ENABLE_DECORATOR = True


class WipCategory(Enum):
    WIP = 1
    BETA = 2


class Action(Enum):
    ERROR = 1
    WARNING = 2


################ Implementation #####################################


def disable_wip():
    """Utility function to disable decorator functionality.
    Mainly designed for testing
    """
    global _ENABLE_DECORATOR
    _ENABLE_DECORATOR = False


def enable_wip():
    """Utility function to enable decorator functionality.
    Mainly designed for testing
    """
    global _ENABLE_DECORATOR
    _ENABLE_DECORATOR = True


def work_in_progress(*args, **kwargs):
    """Decorator that can be used to mark a function
    or a class as "work in progress". It will result in a warning being emitted
    when the function / class is used.

    Args:
        category: WipCategory
            Enum specifying what category of message you want to throw
        action: Action
            Enum specifying what type of action you want to take.
            Example: ERROR or WARNING

    Example Usage:

    ### Decorating class

    1. No configuration:
        @work_in_progress
        class Foo:
            pass

    2. Action and category configuration:
        @work_in_progress(action=Action.WARNING, category=WipCategory.BETA)
        class Foo:
            pass

    ### Decorating Function:

    1. No configuration:
        @work_in_progress
        def foo(*args, **kwargs):
            pass

    2. Action and category configuration:
        @work_in_progress(action=Action.WARNING, category=WipCategory.BETA)
         def foo(*args, **kwargs):
            pass

    ### Sample message:

    foo is still in the BETA phase and subject to change!

    """
    if args:
        wrapped_obj = args[0]
    else:
        wrapped_obj = None

    # Set defaults
    category = kwargs.get("category", WipCategory.WIP)
    action = kwargs.get("action", Action.WARNING)

    # Type checks
    error.type_check("<TRU92076783E>", WipCategory, category=category)
    error.type_check("<TRU87572165E>", Action, action=action)

    if inspect.isclass(wrapped_obj) or inspect.isfunction(wrapped_obj):

        # TODO: if a class, add this decorator to all the functions of this class
        return _decorator_handler(wrapped_obj, category, action)

    elif len(kwargs) > 0:

        def decorator(wrapped_obj):
            return _decorator_handler(wrapped_obj, category, action)

        return decorator
    else:
        raise ValueError(
            "Invalid usage of wip decorator. {} argument not supported!".format(
                type(wrapped_obj)
            )
        )


def _decorator_handler(wrapped_obj, category, action):
    """Utility function to cover common decorator handling
    logic.
    Args:
        wrapped_obj: Callable
            Class or function to be decorated
        category: Enum(WipCategory)
            Enum specifying the category of the message
        Action: Enum(Action)
            Enum specifying the action to be taken with the decorator
    Returns:
        function:
            Decorator function
    """

    if inspect.isclass(wrapped_obj):
        # Replace __new__ function of wrapped class
        # with wrapped_cls function that includes
        # warning message
        new_class = wrapped_obj.__new__

        def wrapped_cls(cls, *args, **kwargs):
            _get_message(wrapped_obj, category, action)

            # if class __new__ is empty
            if new_class is object.__new__:
                return new_class(cls)

            return new_class(cls, *args, **kwargs)

        wrapped_obj.__new__ = staticmethod(wrapped_cls)

        return wrapped_obj
    else:

        def wip_decorator(*args, **kwargs):

            # function specific handling
            _get_message(wrapped_obj, category, action)
            return wrapped_obj(*args, **kwargs)

    return wip_decorator


def _get_message(wrapped_obj, category, action):
    """Utility function to run action"""
    if _ENABLE_DECORATOR:
        message = message_format.format(wrapped_obj, category.name)
        if action == Action.ERROR:
            raise RuntimeError(message)
        if action == Action.WARNING:
            log.warning(message)
