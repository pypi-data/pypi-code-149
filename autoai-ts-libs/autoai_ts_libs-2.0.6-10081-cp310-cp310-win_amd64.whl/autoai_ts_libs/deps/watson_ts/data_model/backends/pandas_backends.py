"""
Core data model backends backed by pandas
"""

# Standard
from typing import Any, Iterable, Optional, Tuple, Type, Union
import json

# Third Party
# TODO: make pandas and numpy non-optional elsewhere!
from pandas import RangeIndex
import numpy as np
import pandas as pd

# First Party
from watson_core.data_model import ProducerId
from watson_core.toolkit import error_handler
import alog

# Local
from .. import time_types
from .base import StrictFieldBackendMixin, TimeSeriesBackendBase, UncachedBackendMixin

log = alog.use_channel("PDBCK")
error = error_handler.get(log)


class PandasTimeSeriesBackend(TimeSeriesBackendBase):
    """The PandasTimeSeriesBackend is responsible for managing the standard
    in-memory representation of a TimeSeries
    """

    def __init__(
        self,
        data_frame: pd.DataFrame,
        timestamp_column: str = None,
        value_columns: Optional[Iterable[str]] = None,
        ids: Optional[Iterable[int]] = None,
        producer_id: Optional[Union[Tuple[str, str], ProducerId]] = None,
    ):
        """At init time, hold onto the data frame as well as the arguments that
        tell where the time and values live

        Args:
            data_frame:  pd.DataFrame
                The raw data frame
            timestamp_column:  Optional[str]
                The name of the column holding the timestamps. If set to None, timestamps will be assigned based on the
                rows index (default is None)
            value_columns:  Optional[Iterable[str]]
                A sequence of names of columns to hold as values
            ids:  Optional[iterable[int]]
                A sequence of numeric IDs associated with this TimeSeries
            producer_id:  Optional[Union[Tuple[str, str], ProducerId]]
                The id for the producer of this TimeSeries
        """
        # Validate the types and column names
        error.type_check("<WTS81128380E>", pd.DataFrame, data_frame=data_frame)
        error.type_check(
            "<WTS32030920E>", str, int, type(None), timestamp_column=timestamp_column
        )
        error.type_check_all(
            "<WTS81128382E>",
            str,
            int,
            allow_none=True,
            value_columns=value_columns,
        )
        error.type_check_all(
            "<WTS81128383E>",
            str,
            allow_none=True,
            ids=ids,
        )
        error.type_check(
            "<WTS81128384E>",
            tuple,
            ProducerId,
            allow_none=True,
            producer_id=producer_id,
        )

        # Validate the column names

        error.value_check(
            "<WTS81128385E>",
            (timestamp_column is None or (timestamp_column in data_frame.columns)),
            "Invalid timestamp column/index: {}",
            timestamp_column,
        )
        value_columns = value_columns or [
            col for col in data_frame.columns if col != timestamp_column
        ]
        error.value_check(
            "<WTS81128386E>",
            # TODO: Support lambdas!
            all(value_col in data_frame.columns for value_col in value_columns),
            "Invalid value columns: {}",
            value_columns,
        )

        self._df = data_frame
        self._timestamp_column = timestamp_column
        self._value_columns = value_columns
        self._ids = [] if ids is None else ids
        self._producer_id = (
            producer_id
            if isinstance(producer_id, ProducerId)
            else (ProducerId(*producer_id) if producer_id is not None else None)
        )

    def get_attribute(
        self,
        data_model_class: Type["TimeSeries"],
        name: str,
        external_df: pd.DataFrame = None,
    ) -> Any:
        """When fetching a data attribute from the timeseries, this aliases to
        the appropriate set of packend wrappers for the various fields.
        """

        # use the external definition of our pandas-like dataframe if
        # requested
        pandas_impl = external_df if external_df is not None else self._df

        # If requesting producer_id or ids, just return the stored value
        if name == "producer":
            return self._producer_id
        if name == "ids":
            return self._ids

        # If requesting the value_labels, this is the value column names
        if name == "value_labels":
            return [str(val) for val in self._value_columns]

        # If requesting the "time_sequence" or one of the oneof fields, extract
        # the timestamps from the dataframe
        if name in ["time_period", "time_points"]:
            if self._timestamp_column is None:
                time_sequence = RangeIndex(start=0, stop=pandas_impl.shape[0], step=1)
            else:
                time_sequence = pandas_impl[self._timestamp_column]

            # If the sequence is periodic, use the PeriodicTimeSequence backend
            is_periodic = isinstance(time_sequence.dtype, pd.PeriodDtype) or isinstance(
                time_sequence, RangeIndex
            )
            if name == "time_period":
                if is_periodic:
                    return time_types.PeriodicTimeSequence.from_backend(
                        PandasPeriodicTimeSequenceBackend(time_sequence)
                    )

            # Otherwise, use the PointTimeSequence backend
            elif not is_periodic:
                return time_types.PointTimeSequence.from_backend(
                    PandasPointTimeSequenceBackend(time_sequence)
                )
            return None

        # If requesting the value sequences, return the wrapped value columns
        if name == "values":

            return [
                time_types.ValueSequence.from_backend(
                    PandasValueSequenceBackend(pandas_impl, col_name)
                )
                for col_name in self._value_columns
            ]

        # Delegate to common parent logic
        # this seems unreachable???
        # return super().get_attribute(data_model_class, name)

    def as_pandas(self) -> pd.DataFrame:
        """Return the underlying data frame"""
        return self._df, self._timestamp_column, self._value_columns


def _iteritems_workaround(series: Any, force_list: bool = False) -> Iterable:
    """pyspark.pandas.Series objects do not support
    iteration. For native pandas.Series objects this
    function will be a no-op.

    For pyspark.pandas.Series or other iterable objects
    we try to_numpy() (unless force_list
    is true) and if that fails we resort to a to_list()

    """
    if isinstance(series, pd.Series):
        return series

    # note that we're forcing a list only if we're not
    # a native pandas series
    if force_list:
        return series.to_list()

    try:
        return series.to_numpy()
    except:
        return series.to_list()


class PandasValueSequenceBackend(UncachedBackendMixin, StrictFieldBackendMixin):
    """Backend for ValueSequence backed by a set of columns in a Pandas
    DataFrame
    """

    @staticmethod
    def _serialize_any(any_val):
        try:
            json_str = json.dumps(any_val)
            return json_str
        except:
            raise TypeError("could not serialize the given value")

    # This dtype is what shows up for non-periodic date ranges
    _TIMESTAMP_DTYPE = np.dtype("datetime64[ns]")

    def __init__(self, data_frame: pd.Series, col_name: str):
        """Initialize with the data frame and the value column name"""
        self._df = data_frame
        self._col_name = col_name
        # Determine which of the oneof types is valid for this sequence
        self._dtype = self._df[self._col_name].dtype
        self._converter = lambda x: x
        if self._dtype == self.__class__._TIMESTAMP_DTYPE or isinstance(
            self._dtype, pd.PeriodDtype
        ):
            # what do we want to do here, are we just assuming it will convert forever?
            self._sequence_type = time_types.ValueSequence.TimePointSequence
            self._valid_oneof = "val_timepoint"
        # todo not sur why np.issubdtype is running into issue if this is run after, but will look into
        elif self._dtype == "string":
            self._sequence_type = time_types.ValueSequence.StrValueSequence
            self._valid_oneof = "val_str"
        elif np.issubdtype(self._dtype, np.integer):
            self._sequence_type = time_types.ValueSequence.IntValueSequence
            self._valid_oneof = "val_int"
        elif np.issubdtype(self._dtype, np.floating):
            self._sequence_type = time_types.ValueSequence.FloatValueSequence
            self._valid_oneof = "val_float"
        else:
            self._sequence_type = time_types.ValueSequence.AnyValueSequence
            self._valid_oneof = "val_any"

    def get_attribute(
        self,
        data_model_class: Type[time_types.ValueSequence],
        name: str,
    ) -> Any:
        """Get the known attributes from the underlying DataFrame columns"""
        if name in ["val_int", "val_float", "val_str"]:
            if name == self._valid_oneof:
                return self._sequence_type(
                    values=[
                        self._converter(val)
                        for val in _iteritems_workaround(
                            self._df[self._col_name], force_list=True
                        )
                    ],
                )
            return None
        if name == self._valid_oneof == "val_any":
            return self._sequence_type(
                values=[
                    self._serialize_any(val)
                    for val in _iteritems_workaround(
                        self._df[self._col_name], force_list=False
                    )
                ]
            )

        if name == self._valid_oneof == "val_timepoint":
            return self._sequence_type(
                values=[
                    str(val)
                    for val in _iteritems_workaround(
                        self._df[self._col_name], force_list=False
                    )
                ]
            )

        # Delegate to common parent logic
        return super().get_attribute(data_model_class, name)


class PandasPeriodicTimeSequenceBackend(UncachedBackendMixin, StrictFieldBackendMixin):
    """Backend for PeriodicTimeSequence backed by a Pandas Time Span"""

    def __init__(self, time_sequence):
        """Initialize with a periodic time sequence"""
        self._is_range_index = isinstance(time_sequence, RangeIndex)
        if self._is_range_index:
            self._start_time = time_sequence.start
            self._period_length = time_sequence.step
        else:
            self._start_time = (
                None if time_sequence.empty else time_sequence[0].start_time
            )
            self._period_length = time_sequence.dtype.freq.name

    def get_attribute(
        self,
        data_model_class: Type[time_types.PeriodicTimeSequence],
        name: str,
    ) -> Any:
        """Get the known attributes from the backend data"""
        if name == "start_time" and self._start_time is not None:
            return time_types.TimePoint.from_backend(
                PandasTimePointBackend(self._start_time)
            )
        if name == "period_length":
            if self._is_range_index:
                return time_types.TimeDuration(dt_int=self._period_length)
            else:
                return time_types.TimeDuration(dt_str=self._period_length)

        # Delegate to common parent logic
        # This seems unreachable???
        # return super().get_attribute(data_model_class, name)


class PandasPointTimeSequenceBackend(
    UncachedBackendMixin,
    StrictFieldBackendMixin,
):  # TODO: Should we cache this one???
    """Backend for PointTimeSequence backed by a Pandas Series"""

    def __init__(self, time_sequence: pd.Series):
        """Initialize with a series based time sequence"""
        self._time_sequence = time_sequence

    def get_attribute(
        self,
        data_model_class: Type[time_types.PointTimeSequence],
        name: str,
    ) -> Any:
        """Get the known attributes from the backend data"""
        if name == "points":
            # TODO: a user may have ints/floats stored as objects in their dataframe, should we handle that or throw an
            #  exception
            return [
                time_types.TimePoint.from_backend(PandasTimePointBackend(point_data))
                for point_data in _iteritems_workaround(
                    self._time_sequence, force_list=True
                )
            ]

        # Delegate to common parent logic
        # This seems unreachable???
        # return super().get_attribute(data_model_class, name)


class PandasTimePointBackend(UncachedBackendMixin, StrictFieldBackendMixin):
    """Backend for time point data held by Pandas"""

    def __init__(self, point_data: Any):
        """Initialize with the raw pandas value"""
        self._point_data = point_data

    def get_attribute(
        self,
        data_model_class: Type[time_types.TimePoint],
        name: str,
    ) -> Any:
        """Get the appropriate fields based on the data type of the point"""
        int_ok = name in ["time", "ts_int"]
        float_ok = name in ["time", "ts_float"]
        epoch_ok = name in ["time", "ts_epoch"]
        any_ok = any((int_ok, float_ok, epoch_ok))

        if epoch_ok and isinstance(self._point_data, pd.Timestamp):
            return time_types.Seconds(seconds=pd_timestamp_to_seconds(self._point_data))
        dtype = getattr(self._point_data, "dtype", None)
        if int_ok and (
            isinstance(self._point_data, int) or np.issubdtype(dtype, np.integer)
        ):
            return self._point_data
        if float_ok and (
            isinstance(self._point_data, float)
            or (dtype is not None and np.issubdtype(dtype, np.floating))
        ):
            return self._point_data
        if any_ok:
            return None
        # This seems unreachable???
        # return super().get_attribute(data_model_class, name)


## Shared Utils ################################################################


def pd_timestamp_to_seconds(ts: Union[pd.Timestamp, pd.Period]) -> float:
    """Extract the seconds-since-epoch representation of the timestamp

    NOTE: The pandas Timestamp.timestamp() function returns a different value
        than Timestamp.to_pydatetime().timestamp()! Since we want this to
        round-trip with python datetime, we want the later. They both claim to
        be POSIX, so something is missing leap-something!
    """
    if isinstance(ts, pd.Period):
        ts = ts.to_timestamp()
    if isinstance(ts, np.datetime64):
        return ts.astype(float) / 1e9
    return ts.to_pydatetime().timestamp()
