"""
Common data model containing all data structures that are passed in and out of
blocks.
"""

# ordering is important here to permit protobuf loading and dynamic
# `watson_core` setup
# pylint: disable=wrong-import-order,wrong-import-position

# First Party
# Import core enums and add in from this data model
from watson_core.data_model import default_wrap_protobufs, enums

# Local
# Import the protobufs
from . import protobufs

enums.import_enums(globals())

# First Party
# Import producer and data streams from the core
from watson_core.data_model import *

# Local
from .time_types import (
    PeriodicTimeSequence,
    PointTimeSequence,
    Seconds,
    TimeDuration,
    TimePoint,
    ValueSequence,
)
from .timeseries import TimeSeries

default_wrap_protobufs(protobufs, globals())
