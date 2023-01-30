"""
The version of the package can be returned as a single string or a dict.

When a string, it comes from the package __version__.
When a dict, it also has __version__,
as well as versions of other depdency packages.
"""

from typing import Optional

import zmq

from dls_pairstream_lib import __version__


# ----------------------------------------------------------
def version() -> str:
    """
    Version of the dls_pairstream package as a string.
    """

    return __version__


# ----------------------------------------------------------
def meta(given_meta: Optional[dict] = None) -> dict:
    """
    Returns version information from the dls_pairstream package
    and its dependencies as a dict.
    Adds version information to a given meta dict if it was provided.
    """

    meta = {}
    meta["dls_pairstream"] = version()

    meta["zmq_version"] = zmq.zmq_version()
    meta["pyzmq_version"] = zmq.pyzmq_version()

    try:
        import websockets

        meta["websockets"] = websockets.__version__
    except Exception as exception:
        meta["websockets"] = str(exception)

    if given_meta is not None:
        given_meta.update(meta)
    else:
        given_meta = meta
    return given_meta
