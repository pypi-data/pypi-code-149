# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Platform related utilities"""

from functools import wraps
import sys
import os
import tempfile

from autoai_ts_libs.deps.srom.utils.file_utils import possibly_unsafe_join, gettempdir


def memoize(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


@memoize
def is_windows():
    """Return true if process is running under win32 or win64"""
    return sys.platform.startswith("win")


@memoize
def get_username():
    return os.getenv(
        "USER", os.getenv("USERNAME", os.getenv("NB_USER", "UNKNOWN_USER"))
    )


@memoize
def get_user_tempdir():
    return possibly_unsafe_join(gettempdir(), get_username())

