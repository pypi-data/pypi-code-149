"""
The core data model objects for primitive time types
"""

# Standard
import json
from datetime import datetime, timedelta
from typing import Any, Iterable, Union

# First Party
import dateutil.parser

from watson_core.data_model.base import DataBase
import alog

# Local
from .protobufs import timeseries_types_pb2

log = alog.use_channel("TSDM")


class Seconds(DataBase):
    """A nanosecond value that can be interpreted as either a datetime or a
    timedelta
    """

    def as_datetime(self) -> datetime:
        """Interperet these nanoseconds as time since epoch"""
        return datetime.fromtimestamp(self.seconds)

    def as_timedelta(self) -> timedelta:
        """Interpret these nanoseconds as a duration"""
        return timedelta(seconds=self.seconds)

    @classmethod
    def from_datetime(cls, time_point: datetime) -> "Seconds":
        """Create a Seconds from a datetime"""
        return cls(seconds=time_point.timestamp())

    @classmethod
    def from_timedelta(cls, time_delta: timedelta) -> "Seconds":
        """Create a Seconds from a timedelta"""
        return cls(seconds=time_delta.total_seconds())

    def to_dict(self) -> str:
        return {"seconds": self.seconds}


class TimePoint(DataBase):
    """
    The core data model object for a TimePoint
    """

    _private_slots = ("_which_one_of",)

    @property
    def which_one_of(self):
        """"""
        which_one_of = getattr(self, "_which_one_of", None)
        if which_one_of is not None:
            return which_one_of

        backend = getattr(self, "_backend", None)
        if backend is not None:
            data_val = backend.get_attribute(self._proto_class, "time")
            if isinstance(data_val, int):
                return "ts_int"
            if isinstance(data_val, float):
                return "ts_float"
            if isinstance(data_val, (datetime, Seconds)):
                return "ts_epoch"

            # todo This seems unreachable as when we call setattr, it checks if the type is in
            #  the given fields.
            # log.warning("No known data point field for data of type %s", type(data_val))

    def to_dict(self) -> str:
        """Override to_dict to handle the oneof cleanly"""
        valid_field = self.which_one_of
        if valid_field is not None:
            field_val = getattr(self, valid_field)
            if valid_field == "ts_epoch":
                field_val = field_val.to_dict()
            return {valid_field: field_val}
        # todo This seems unreachable as we at least will end up with a ts_int if empty is created, if not
        #  empty, we will end up using setattr which checks if the types in the given field. Should never return
        #  None from which one of???
        # return {}

    def __setattr__(self, name: str, value: Any):
        """Custom setattr for 'time' that will dispatch to the correct type
        under the hood
        """
        if name == "time":
            name = f"ts_{type(value).__name__}"
            if name == "ts_Seconds":
                name = "ts_epoch"
            if name not in self.fields:
                raise AttributeError(f"No oneof for 'time' and type {type(value)}")
        # this here seems to be setting a defaul
        if name.startswith("ts_") and (self.which_one_of is None or bool(value)):
            self._which_one_of = name
        super().__setattr__(name, value)

    @property
    def time(self) -> Union[int, float, Seconds]:
        """Time is an alias to the set oneof value"""
        if self.which_one_of is not None:
            return getattr(self, self.which_one_of)

        # return None

    @classmethod
    def from_proto(cls, proto):
        which_field = proto.WhichOneof("time")

        field_value = getattr(proto, which_field)
        if which_field == "ts_epoch":
            field_value = Seconds.from_proto(field_value)

        return cls(**{which_field: field_value})


class TimeDuration(DataBase):
    """
    The core data model object for a TimeDuration
    """

    _private_slots = ("_which_one_of",)

    # @property
    # def which_one_of(self):
    #     """"""
    #     which_one_of = getattr(self, "_which_one_of", None)
    #     if which_one_of is not None:
    #         return which_one_of
    #
    #     backend = getattr(self, "_backend", None)
    #     if backend is not None:
    #         data_val = backend.get_attribute(self._proto_class, "time")
    #         if isinstance(data_val, int):
    #             return "dt_int"
    #         if isinstance(data_val, float):
    #             return "dt_float"
    #         if isinstance(data_val, str):
    #             return "dt_str"
    #         if isinstance(data_val, (datetime, Seconds)):
    #             return "dt_sec"
    #         log.warning("No known data point field for data of type %s", type(data_val))

    # def to_dict(self) -> str:
    #     """Override to_dict to handle the oneof cleanly"""
    #     valid_field = self.which_one_of
    #     if valid_field is not None:
    #         field_val = getattr(self, valid_field)
    #         if valid_field == "dt_sec":
    #             field_val = field_val.to_dict()
    #         return {valid_field: field_val}
    #     return {}

    # def __setattr__(self, name: str, value: Any):
    #     """Custom setattr for 'time' that will dispatch to the correct type
    #     under the hood
    #     """
    #     if name == "time":
    #         name = f"dt_{type(value).__name__}"
    #         if name == "dt_Seconds":
    #             name = "dt_sec"
    #         if name not in self.fields:
    #             raise AttributeError(f"No oneof for 'time' and type {type(value)}")
    #     if name.startswith("ts_") and (self.which_one_of is None or bool(value)):
    #         self._which_one_of = name
    #     super().__setattr__(name, value)

    # @property
    # def time(self) -> Union[int, float, str, Seconds]:
    #     """Time is an alias to the set oneof value"""
    #     if self.which_one_of is not None:
    #         return getattr(self, self.which_one_of)
    #     return None

    @classmethod
    def from_proto(cls, proto):
        which_field = proto.WhichOneof("time")

        field_value = getattr(proto, which_field)
        if which_field == "dt_sec":
            field_value = Seconds.from_proto(field_value)

        return cls(**{which_field: field_value})

    def __setattr__(self, name: str, value: Any):
        """Custom setattr for 'time' that will dispatch to the correct type
        under the hood
        """
        if name == "time":
            name = f"dt_{type(value).__name__}"
            if name == "dt_Seconds":
                name = "dt_sec"
            if name not in self.fields:
                raise AttributeError(f"No oneof for 'time' and type {type(value)}")
        super().__setattr__(name, value)

    # def fill_proto(self, proto):
    #     subproto = getattr(proto, 'values')
    #     subproto.extend([json.loads(v) for v in self.values])

    @property
    def time(self) -> Union[str, int, float, Seconds]:
        """Time is an alias to the set oneof value"""
        # todo find first non-zero, they default to 0
        if self.dt_str is not None and self.dt_str != "":
            return self.dt_str
        elif self.dt_sec is not None:
            return self.dt_sec
        elif self.dt_int is not None and self.dt_int != 0:
            return self.dt_int
        elif self.dt_float is not None and self.dt_float != 0.0:
            return self.dt_float
        else:
            return None


class PeriodicTimeSequence(DataBase):
    """A PeriodicTimeSequence represents an indefinite time sequence where ticks
    occur at a regular period
    """


class PointTimeSequence(DataBase):
    """A PointTimeSequence represents a finite sequence of time points that may
    or may not be evenly distributed in time
    """


class ValueSequence(DataBase):
    """A ValueSequence is a finite list of contiguous values, each representing
    the value of a given attribute for a specific observation within a
    TimeSeries
    """

    class IntValueSequence(DataBase):
        """Nested value sequence of integers"""

        _proto_class = timeseries_types_pb2.ValueSequence.IntValueSequence

    class FloatValueSequence(DataBase):
        """Nested value sequence of floats"""

        _proto_class = timeseries_types_pb2.ValueSequence.FloatValueSequence

    class StrValueSequence(DataBase):
        """Nested value sequence of strings"""

        _proto_class = timeseries_types_pb2.ValueSequence.StrValueSequence

    # todo we can have a constuct for sequences that require serialization
    class TimePointSequence(DataBase):
        """Nested value sequence of TimePoints"""

        _proto_class = timeseries_types_pb2.ValueSequence.TimePointSequence

        def to_dict(self):
            result = []
            for v in self.values:
                result.append(v)
            return {"values": result}

        def fill_proto(self, proto):
            subproto = getattr(proto, "values")
            subproto.extend([v for v in self.values])

        @classmethod
        def from_proto(cls, proto):
            return cls(**{"values": [str(v) for v in proto.values]})

    # todo we can have a construct for sequences that require serialization
    class AnyValueSequence(DataBase):
        """Nested value sequence of Any objects"""

        _proto_class = timeseries_types_pb2.ValueSequence.AnyValueSequence

        def to_dict(self):
            result = []
            for v in self.values:
                json_v = json.loads(v)
                result.append(json_v)
            return {"values": result}

        def fill_proto(self, proto):
            subproto = getattr(proto, "values")
            subproto.extend([json.loads(v) for v in self.values])

        @classmethod
        def from_proto(cls, proto):
            return cls(**{"values": [json.dumps(v) for v in proto.values]})

    @property
    def sequence(
        self,
    ) -> Union[Iterable[int], Iterable[float], Iterable[str], Iterable[Any]]:
        """sequence is an alias to the value sequence oneof"""
        for attr in ("val_int", "val_float", "val_str", "val_timepoint", "val_any"):
            attr_val = getattr(self, attr, None)
            if attr_val is not None:
                return attr_val
        return None
