"""
The core data model object for a TimeSeries
"""

# Standard
from datetime import timedelta
from typing import Iterable, Tuple, Union

# Third Party
import numpy as np
import pandas as pd

# First Party
from pandas import RangeIndex

from watson_core.data_model.base import DataBase
from watson_core.toolkit import error_handler
import alog

# Local
from ..toolkit.optional_dependencies import HAVE_PYSPARK, HAVE_TSPY, pyspark, tspy
from . import time_types
from .backends.pandas_backends import PandasTimeSeriesBackend, pd_timestamp_to_seconds
from autoai_ts_libs.deps.watson_ts.data_model.backends.base import TimeSeriesBackendBase

log = alog.use_channel("TSDM")
error = error_handler.get(log)

## TimeSeries ##################################################################

# Shared constant for seconds -> milliseconds
S_TO_MS = 1000


class TimeSeries(DataBase):
    """The TimeSeries object is the central data container for the library. It
    wraps the tspy.TimeSeries container's functionality to bind it into the
    watson_core data model using a customized data backend.
    """

    _TEMP_TS_COL = "__ts"

    # TODO: We need to clean up the init semantics
    def __init__(self, *args, **kwargs):

        """Constructing a TimeSeries directly always delegates to the pandas
        backend
        """
        # todo check if this is possible???
        # if '_backend' in kwargs:
        #     self._backend = kwargs['_backend']
        if "values" in kwargs:
            self.time_period = None
            self.time_points = None
            self.producer = None

            for k, v in kwargs.items():
                setattr(self, k, v)
            self._get_pd_df()

        else:

            if isinstance(args[0], pd.DataFrame):
                self._backend = PandasTimeSeriesBackend(*args, **kwargs)
            elif HAVE_PYSPARK and isinstance(args[0], pyspark.sql.DataFrame):
                from .backends.spark_backend import SparkTimeSeriesBackend

                self._backend = SparkTimeSeriesBackend(*args, **kwargs)

            else:
                raise NotImplementedError("not implemented yet")

    @property
    def time_sequence(
        self,
    ) -> Union[time_types.PeriodicTimeSequence, time_types.PointTimeSequence]:
        """time_sequence is an alias for the two sequence types"""
        point_seq = self.time_points
        if point_seq is not None:
            return point_seq
        return self.time_period

    def _get_pd_df(self) -> Tuple[pd.DataFrame, str, Iterable[str]]:
        """Convert the data to a pandas DataFrame, efficiently if possible"""

        # If there is a backend that knows how to do the conversion, use that
        backend = getattr(self, "_backend", None)
        if backend is not None and isinstance(backend, TimeSeriesBackendBase):
            log.debug2("Using backend pandas conversion")
            return backend.as_pandas()

        # If not, convert the slow way from the proto representation
        df_kwargs = {}

        # Since all fields are optional, we need to ensure that the
        # time_sequence oneof has been set and that there are values
        error.value_check(
            "<WTS98388946E>",
            self.time_sequence is not None,
            "Cannot create pandas data frame without a time sequence",
        )
        error.value_check(
            "<WTS98388947E>",
            self.values is not None,
            "Cannot create pandas data frame without values",
        )

        # Determine the number of rows we'll expect
        col_lens = {len(col.sequence.values) for col in self.values}
        error.value_check(
            "<WTS24439736E>",
            len(col_lens) == 1,
            "Not all columns have matching lengths",
        )
        num_rows = list(col_lens)[0]
        log.debug2("Num rows: %d", num_rows)

        # If the time index is stored periodically, this can be represented as a
        # periodic index in pandas iff the start time and period are grounded in
        # real datetime space. If they are purely numerica, they can be
        # converted to a set of point values. The only invalid combination is a
        # numeric start time and a timedelta duration.
        #
        # (datetime, numeric) -> period w/ numeric seconds
        # (datetime, str) -> period w/ string freq
        # (datetime, timedelta) -> period w/ timedelta freq
        # (numeric, numeric) -> point sequence
        # (numeric, [str, timedelta]) -> INVALID
        if self.time_period is not None:
            start_time = self.time_period.start_time
            period_length = self.time_period.period_length
            error.value_check(
                "<WTS36718278E>",
                start_time.time is not None,
                "start_time must be set in time_period",
            )
            error.value_check(
                "<WTS36718279E>",
                period_length.time is not None,
                "period_length must be set in time_period",
            )

            numeric_start_time = start_time.ts_epoch is None
            numeric_period = period_length.dt_str is None and (
                period_length.dt_int is not None or period_length.dt_float is not None
            )
            error.value_check(
                "<WTS36962854E>",
                not (numeric_start_time and not numeric_period),
                "Time period cannot have a numeric start_time with a timedelta period_length",
            )

            if numeric_start_time:
                df_kwargs["index"] = np.arange(
                    start_time.time,
                    period_length.time * num_rows,
                    period_length.time,
                )
            elif numeric_period:
                df_kwargs["index"] = pd.period_range(
                    start_time.ts_epoch.as_datetime(),
                    freq=timedelta(seconds=period_length.time),
                    periods=num_rows,
                )
            else:
                df_kwargs["index"] = pd.period_range(
                    start_time.ts_epoch.as_datetime(),
                    freq=period_length.dt_str,
                    periods=num_rows,
                )

        # Otherwise, interpret the sequence of time values directly
        else:
            time_points = self.time_points.points
            error.value_check(
                "<WTS11757382E>",
                time_points is not None and len(time_points) == num_rows,
                "Number of time points {} doesn't match number of rows {}",
                -1 if time_points is None else len(time_points),
                num_rows,
            )
            if time_points:

                # Convert to a sequence of contiguous points
                time_point_values = [tp.time for tp in time_points]
                time_point_type = type(time_point_values[0])
                error.type_check_all(
                    "<WTS79828262E>",
                    time_point_type,
                    time_point_values=time_point_values,
                )

                # If the type needs conversion to datetimes, do so
                if time_point_type == time_types.Seconds:
                    time_point_values = [val.as_datetime() for val in time_point_values]

                df_kwargs["index"] = time_point_values

        # Make the columns dict
        value_labels = self.value_labels or range(len(self.values))
        error.value_check(
            "<WTS60320473E>",
            len(value_labels) == len(self.values),
            "Wrong number of value labels {} for {} value columns",
            len(value_labels),
            len(self.values),
        )
        df_kwargs["data"] = dict(
            zip(value_labels, (col.sequence.values for col in self.values))
        )

        # Make the data frame
        return pd.DataFrame(**df_kwargs)

    ## Views ##

    # TODO: Ensure that these are the correct zero-copy methods!!!

    def as_tspy(self) -> "tspy.data_structures.TimeSeries":
        """Get the view of this timeseries as a tspy series

        Returns:
            tspy_ts:  tspy.data_structures.TimeSeries
                The underlying tspy time series
        """
        if not HAVE_TSPY:
            raise EnvironmentError("Cannot view as tspy without tspy installed")

        # TODO: If the backend holds tspy natively, expose it directly

        # Use central pandas representation
        df, timestamp_source, value_source = self._get_pd_df()
        tspy_kwargs = {"value_column": value_source}

        # Get the timestamp sequence
        if timestamp_source is None:
            tspy_kwargs["ts_column"] = None
        else:
            timestamps = df[timestamp_source]
            freq_root = timestamps.dtype

            # If the sequence is periodic, use the periodic kwargs
            freq = getattr(freq_root, "freq", None)
            if freq is not None:
                # If the period does not have a fixed timedelta (e.g. "B" for
                # business day), we need to convert to a non-periodic column
                delta = getattr(freq, "delta", None)
                if delta is None:
                    log.debug3("Non-fixed period being treated as a sequence")
                    df = df.copy(deep=False)
                    df[self.__class__._TEMP_TS_COL] = [
                        int(pd_timestamp_to_seconds(ts) * S_TO_MS) for ts in timestamps
                    ]
                    tspy_kwargs["ts_column"] = self.__class__._TEMP_TS_COL
                else:
                    # If start_time is itself a Period of size 1, we need to extract
                    # the start_time attribute to get to a Timestamp
                    tspy_kwargs["granularity"] = delta
                    start_time = min(timestamps)
                    start_time = getattr(start_time, "start_time", start_time)
                    tspy_kwargs["start_time"] = start_time
            # Otherwise, it's just a column name!
            else:
                tspy_kwargs["ts_column"] = timestamp_source

        # tspy doesn't support floating point time points, so if we have a
        # floating point time sequence, we're out of luck!
        #
        # TODO: If this becomes required, talk to Josh about supporting it!
        ts_col = tspy_kwargs.get("ts_column")
        if (
            ts_col is not None
            and isinstance(df[ts_col].dtype, np.dtype)
            and np.issubdtype(df[ts_col].dtype, np.float_)
        ):
            raise ValueError(
                "Cannot convert to tspy with a floating-point time sequence"
            )

        log.debug3("tspy.time_series kwargs: %s", tspy_kwargs)
        log.debug4("tspy.time_series df: %s", df)
        return tspy.time_series(df, **tspy_kwargs)

    def as_pandas(self) -> "pd.DataFrame":
        """Get the view of this timeseries as a pandas DataFrame

        Returns:
            df:  pd.DataFrame
                The view of the data as a pandas DataFrame
        """
        return self._get_pd_df()[0]

    def as_numpy(self) -> "np.ndarray":
        """Get the view of this timeseries as a numpy array

        Returns:
            array:  np.ndarray
                The view of the data as a numpy array
        """
        df, timestamp_source, val_source = self._get_pd_df()
        all_cols = val_source if not isinstance(val_source, str) else [val_source]
        if timestamp_source is None:
            df = df.copy(deep=False)
            df[self.__class__._TEMP_TS_COL] = RangeIndex(
                start=0, stop=df.shape[0], step=1
            )
            all_cols = [self.__class__._TEMP_TS_COL] + all_cols
        else:
            all_cols = [timestamp_source] + all_cols
        return df[all_cols].to_numpy()
