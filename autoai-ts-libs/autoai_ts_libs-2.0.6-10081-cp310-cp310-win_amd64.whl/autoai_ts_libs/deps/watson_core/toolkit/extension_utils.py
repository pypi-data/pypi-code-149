# *****************************************************************#
# (C) Copyright IBM Corporation 2022.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
from types import ModuleType

from imp import new_module
from importlib import import_module

from . import alog
from .errors import error_handler

log = alog.use_channel("TLKIT")
error = error_handler.get(log)

EXTENSIONS_ATTR_NAME = "extensions"


def enable_extension_binding(lib_handle):
    """Idempotent initialization of extensions subpackage under a provided package. Assuming
    one doesn't exist, binds an empty "extensions" subpackage to the lib_handle. We can then
    bind individual extensions to the library.

    This should be called in the top level package initialization of the library being extended
    to enable extension module support by attribute binding.

    Args:
        lib_handle: Module
            Watson * library on which we would like to create an empty extensions subpackage,
            accessible by <lib_handle>.extensions
    """
    error.type_check("<COR64728193E>", ModuleType, lib_handle=lib_handle)
    # Ensure that we have a watson * like module to start with, and that
    # it's initialized dynamic extension package binding.
    error.value_check(
        "<COR10841029E>",
        is_extension_like(lib_handle),
        "lib_handle must be a Watson * like Module",
    )
    if not hasattr(lib_handle, EXTENSIONS_ATTR_NAME):
        extension_pkg = new_module(EXTENSIONS_ATTR_NAME)
        setattr(lib_handle, EXTENSIONS_ATTR_NAME, extension_pkg)


def is_extension_like(lib_handle):
    """Given a handle to a module, determine if it is Watson * like. Currently, this is checked
    to see if <lib_handle>.lib_config.library_version is a string type.

    Args:
        lib_handle: Module
            Watson * library on which we would like to create an empty extensions subpackage,
            accessible by <lib_handle>.extensions

    Returns:
        bool
            True if the library handle is Watson * like.
    """
    error.type_check("<COR64748191E>", ModuleType, lib_handle=lib_handle)
    lib_version = getattr(
        getattr(lib_handle, "lib_config", None), "library_version", None
    )
    return isinstance(lib_version, str)


def bind_extensions(extension_names, lib_handle):
    """Given an iterable of extension names and a handle to a watson library, consider each
    extension name. For each, import it & ensure it looks like a Watson library by checking to
    see if it have a lib_config attribute with a defined library version.

    For all Watson * like libraries, bind them to an extensions package on the library.

    Ex)
        Say we provide inputs:
            extension_names = ["sample_module"], a Watson NLP extension
            lib_handle = watson_nlp

        Register sample_module onto watson_nlp.extensions.sample_module.

    Args:
        extension_names: list | tuple | set
            Iterable of (string) module names to be imported and bound. Objects are presumed
            to be unique & will be cast to a set for consideration. If an existing extension
            of the same name is already registered, the extension will be skipped.
        lib_handle: Module
            Watson * library on which we would like to create an empty extensions subpackage,
            accessible by <lib_handle>.extensions
    """
    error.type_check(
        "<COR64140091E>", set, list, tuple, extension_names=extension_names
    )
    error.type_check_all("<COR34341191E>", str, extension_names=extension_names)
    error.type_check("<COR64748191E>", ModuleType, lib_handle=lib_handle)
    error.value_check(
        "<COR12831731E>",
        hasattr(lib_handle, EXTENSIONS_ATTR_NAME),
        "Library {} has not enabled extension binding",
        lib_handle.__name__,
    )

    ext_subpkg = getattr(lib_handle, EXTENSIONS_ATTR_NAME)
    for ext_name in set(extension_names):
        # Skip any extension package name that's already registered
        if hasattr(ext_subpkg, ext_name):
            log.debug("Extension [{}] is already bound".format(ext_name))
            continue
        # Dynamically import each extension module; skip if we can't import
        try:
            ext_lib = import_module(ext_name)
        except ImportError:
            log.warning(
                "<COR81130101W>",
                "Module [{}] is not importable and could not be bound".format(ext_name),
            )
            continue
        # If this is a watson * like library, bind it to the extensions property
        if is_extension_like(ext_lib):
            setattr(ext_subpkg, ext_name, ext_lib)
            log.debug("Bound extension [{}] successfully".format(ext_name))
        else:
            log.warning(
                "<COR81130101W>",
                "Skipping binding for [{}]; module is not Watson Library like".format(
                    ext_name
                ),
            )
