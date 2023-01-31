# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Utility functions for testing if an object is an instance of a given type.
"""

import collections
import google
import semver

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer,
)


def isprotobuf(obj):
    """Returns True if obj is a protobuf message, otherwise False."""
    return isinstance(obj, google.protobuf.message.Message)


def isprotobufclass(obj):
    """Returns True if obj is a protobuf message class.
    If you want to test for a protobuf message instance, not a class, use isprotobuf instead.
    """
    return isinstance(
        obj, google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType
    )


def isprotobufenum(obj):
    """Returns True if obj is a protobuf enum."""
    return isinstance(obj, google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper)


def isprotobufrepeated(obj):
    """Returns true if obj is a repeated Message or repeated primitive"""
    return isinstance(obj, RepeatedCompositeFieldContainer) or isinstance(
        obj, RepeatedScalarFieldContainer
    )


def isprimitive(obj):
    """Returns True if obj is a python primitive (bool, int, float, str), otherwise False."""
    return (obj is None) or isinstance(obj, (bool, int, float, str))


def isiterable(obj):
    """Returns True if obj can be iterated over, otherwise False."""
    return isinstance(obj, collections.abc.Iterable)


def isvalidversion(obj):
    """Returns True if obj is a valid parseable semantic version (https://semver.org/)"""
    try:
        semver.VersionInfo.parse(obj)  # Parse doesn't fail on valid object
        return True
    except (TypeError, ValueError):
        return False
