# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

from autoai_ts_libs.deps.watson_core.toolkit import alog
from ..toolkit.errors import error_handler

from . import base


log = alog.use_channel("DATAM")
error = error_handler.get(log)


class ProducerId(base.DataBase):
    """Information about a data structure and the block that produced it."""

    def __init__(self, name, version):
        """Construct a new producer id.

        Args:
            name:  str
                The name of the producing block.
            version:  str
                The version of the producing block.
        """
        error.type_check("<COR99428011E>", str, name=name, version=version)

        super().__init__()
        self.name = name
        self.version = version

    def __add__(self, other):
        """Add two producer ids."""
        return ProducerId(name=" & ".join([self.name, other.name]), version="0.0.0")

    @classmethod
    def from_proto(cls, proto):
        return cls(proto.name, proto.version)

    def fill_proto(self, proto):
        proto.name = self.name
        proto.version = self.version
        return proto


class ProducerPriority(base.DataBase):
    """An ordered list of ProducerId structures in descending order of priority.
    This is used when handling conflicts between multiple producers of the same
    data structure.
    """

    def __init__(self, producers):
        """Construct a new ProducerPriority

        Args:
            producers:  list(ProducerId)
        """
        error.type_check_all("<COR01353088E>", ProducerId, producers=producers)

        super().__init__()
        self.producers = producers
