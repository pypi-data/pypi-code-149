"""
This toolkit module holds routines for converting between the various types that
are used to represent timeseries data throughout the backend libraries. In
particular, it holds two-way conversion utilities between each pair of the
following types:

* RawTimeseries
* tspy.data_structures.Timeseries
* pd.DataFrame
* np.ndarray
* pyspark.sql.DataFrame
"""

# Standard
from datetime import datetime
from itertools import chain, islice
from typing import Any, Callable, Iterable, List, Optional, Tuple, Union
import collections

# Third Party
import numpy as np

# First Party
import alog

# Local
from .optional_dependencies import (
    HAVE_PANDAS,
    HAVE_PYSPARK,
    HAVE_TSPY,
    HAVE_NUMPY,
    pd,
    pyspark,
    tspy,
)

log = alog.use_channel("TLKT")


## Constants ###################################################################

# Shared definition of a unified "number" type
Number = Union[int, float]

# Shared definition of the types that can make up a timestamp
Timestamp = Union[Number, datetime]

# Shared definition of a RawTimesweries type
RawTimeseries = Iterable[Tuple[Timestamp, Any]]

# Shared definition of the union representing all valid timeseries
# representations
# NOTE: We use forward references for all optional data types to avoid enforcing
#   dependencies
# todo Data Model will replace this type
#  the code in this module will be moved to the DataModel for conversions
#  decorators will instead call the datamodel for conversions
TimeseriesType = Union[
    RawTimeseries,
    "pd.DataFrame",
    "np.ndarray",
    "pyspark.sql.DataFrame",
    "tspy.data_structures.TimeSeries.TimeSeries",
    "tspy.data_structures.BoundTimeSeries",
]

# The names for conversion arguments identifying the source of data when pulling
# from a tabular source (data frame or ndarray)
#
# NOTE: These intentionally match the argument names for each of the to_*
#   converters
TIMESTAMP_SOURCE_ARG = "timestamp_source"
VALUE_SOURCE_ARG = "value_source"

# The names for conversion arguments identifying the targets for data when
# converting to a tabular target (data frame or ndarray)
#
# NOTE: These intentionally match the argument names for each of the to_*
#   converters when converting to a data frame target with named columns
TIMESTAMP_TARGET_NAME_ARG = "timestamp_target"
VALUE_TARGET_NAME_ARG = "value_target"

# Defaults to use when deducing target column names if not given during a
# conversion to a data frame target
DEFAULT_TIMESTAMP_TARGET_NAME = "timestamp"
DEFAULT_VALUE_TARGET_PREFIX = "val"

## Public ######################################################################


def to_raw_timeseries(
    input_arg: TimeseriesType,
    *,
    timestamp_source: Optional[Union[str, int]] = None,
    value_source: Optional[Union[str, int]] = None,
    ignore_unused_col_args: bool = False,
) -> RawTimeseries:
    """Convert any of the available timeseries types to a RawTimeseries

    Args:
        input_arg:  TimeseriesType
            The raw input type

    Kwargs:
        timestamp_source:  Optional[Union[str, int]]
            The column name or index to use for the timeseries sequence
        value_source:  Optional[Iterable[Union[str, int]]]
            The column name(s) or indeces to use for the value sequence when
            the input is one of the data frame types
        ignore_unused_col_args:  bool
            Ignore column args passed to the conversion when the input does not
            require them. This can be useful when the conversion function is
            called without knowledge of the input type.

    Returns:
        timeseries:  RawTimeseries
            The converted RawTimeseries interable
    """

    # Make sure that the value columns are provided correctly
    if isinstance(value_source, (str, int)):
        value_source = [value_source]

    # Figure out which converter to call
    converter = None
    cols_required = False
    if HAVE_PANDAS and isinstance(input_arg, pd.DataFrame):
        cols_required = True
        converter = _pandas_to_raw_timeseries
    elif isinstance(input_arg, np.ndarray):
        cols_required = True
        converter = _numpy_to_raw_timeseries
    elif HAVE_PYSPARK and isinstance(input_arg, pyspark.sql.DataFrame):
        cols_required = True
        converter = _spark_to_raw_timeseries
    elif HAVE_TSPY and isinstance(input_arg, tspy.data_structures.BoundTimeSeries):
        converter = _tspy_bound_to_raw_timeseries
    elif HAVE_TSPY and isinstance(
        input_arg, tspy.data_structures.TimeSeries.TimeSeries
    ):
        converter = _tspy_unbound_to_raw_timeseries

    # Make sure col args are either given or not based on the type
    if cols_required:
        _validate_has_col_args(timestamp_source, value_source)
    elif not ignore_unused_col_args:
        _validate_no_col_args(timestamp_source, value_source)

    # If a valid converter is found, make sure the columns args are given
    # NOTE: The converters will handle type-specific validation errors
    result = (
        input_arg
        if converter is None
        else converter(input_arg, timestamp_source, value_source)
    )

    # We don't perform any additional validation to ensure that the result is a
    # RawTimeseries. Since Iterables encompass a wide range of types, including
    # custom types, the only way to fully validate it would be to iterate the
    # whole thing and validate each entry, then recreate the iterable from the
    # beginning. This would be wildly inefficient, so we leave it to the blocks
    # to ensure that the input types are correct. There may be a shared "best
    # effort" validator in the future, but it would be an opt-in validation step
    # implemented in the block body.
    return result


def to_ndarray(
    input_arg: TimeseriesType,
    *,
    timestamp_source: Optional[str] = None,
    value_source: Optional[str] = None,
    ignore_unused_col_args: bool = False,
    **kwargs,
) -> "np.ndarray":
    """Convert any of the available timeseries types to a np.ndarray

    Args:
        input_arg:  TimeseriesType
            The raw input type

    Kwargs:
        timestamp_source:  Optional[Union[str, int]]
            The column name or index to use for the timeseries sequence
        value_source:  Optional[Iterable[Union[str, int]]]
            The column name(s) or indeces to use for the value sequence when
            the input is one of the data frame types
        ignore_unused_col_args:  bool
            Ignore column args passed to the conversion when the input does not
            require them. This can be useful when the conversion function is
            called without knowledge of the input type.
        **kwargs:
            Additional keyword args to pass to the construction of the np.array.
            NOTE: The set of valid args may depend on whether np.array is called
                directly or df.to_numpy is called.

    Returns:
        timeseries:  np.ndarray
            The converted ndarray
    """
    if not HAVE_NUMPY:
        raise RuntimeError("Cannot run without 'numpy' installed")

    # Make sure that the value columns are provided correctly
    if isinstance(value_source, (str, int)):
        value_source = [value_source]

    # Figure out which converter to call
    converter = None
    cols_required = False
    if HAVE_PANDAS and isinstance(input_arg, pd.DataFrame):
        cols_required = True
        converter = _pandas_to_ndarray
    elif HAVE_PYSPARK and isinstance(input_arg, pyspark.sql.DataFrame):
        cols_required = True
        converter = _spark_to_ndarray
    elif HAVE_TSPY and isinstance(input_arg, tspy.data_structures.BoundTimeSeries):
        converter = _tspy_bound_to_ndarray
    elif HAVE_TSPY and isinstance(
        input_arg, tspy.data_structures.TimeSeries.TimeSeries
    ):
        converter = _tspy_unbound_to_ndarray
    elif not isinstance(input_arg, np.ndarray):
        converter = _raw_timeseries_to_ndarray

    # Make sure col args are either given or not based on the type
    if cols_required:
        _validate_has_col_args(timestamp_source, value_source)
    elif not ignore_unused_col_args:
        _validate_no_col_args(timestamp_source, value_source)

    # If a valid converter is found, make sure the columns args are given
    # NOTE: The converters will handle type-specific validation errors
    return (
        input_arg
        if converter is None
        else converter(input_arg, timestamp_source, value_source, **kwargs)
    )


def to_tspy_unbound(
    input_arg: TimeseriesType,
    *,
    timestamp_source: Optional[str] = None,
    value_source: Optional[str] = None,
    ignore_unused_col_args: bool = False,
    **kwargs,
) -> "tspy.data_structures.time_series.TimeSeries.TimeSeries":
    # todo add fixture?
    # if not HAVE_TSPY:
    #     raise RuntimeError("Cannot run without 'tspy' installed")

    # Make sure that the value columns are provided correctly
    if isinstance(value_source, (str, int)):
        value_source = [value_source]

    # Figure out which converter to call
    converter = None
    cols_required = False
    # First Party
    from tspy.data_structures.time_series.TimeSeries import TimeSeries

    if HAVE_PANDAS and isinstance(input_arg, pd.DataFrame):
        cols_required = True
        converter = _pandas_to_tspy_unbound
    elif HAVE_PYSPARK and isinstance(input_arg, pyspark.sql.DataFrame):
        cols_required = True
        converter = _spark_to_tspy_unbound
    elif HAVE_TSPY and isinstance(input_arg, tspy.data_structures.BoundTimeSeries):
        converter = _tspy_bound_to_tspy_unbound
    elif HAVE_NUMPY and isinstance(input_arg, np.ndarray):
        converter = _ndarray_to_tspy_unbound
    elif not isinstance(input_arg, TimeSeries):
        converter = _raw_timeseries_to_tspy_unbound

    # Make sure col args are either given or not based on the type
    if cols_required:
        _validate_has_col_args(timestamp_source, value_source)
    elif not ignore_unused_col_args:
        _validate_no_col_args(timestamp_source, value_source)

    # If a valid converter is found, make sure the columns args are given
    # NOTE: The converters will handle type-specific validation errors
    return (
        input_arg
        if converter is None
        else converter(input_arg, timestamp_source, value_source, **kwargs)
    )


def to_spark_df(
    input_arg: TimeseriesType,
    *,
    timestamp_source: Optional[str] = None,
    value_source: Optional[str] = None,
    timestamp_target: Optional[str] = None,
    value_target: Optional[Iterable[str]] = None,
    ignore_unused_col_args: bool = False,
    **kwargs,
) -> "pyspark.sql.DataFrame":
    """Convert any of the available timeseries types to a pyspark.sql.DataFrame

    Args:
        input_arg:  TimeseriesType
            The raw input type

    Kwargs:
        timestamp_source:  Optional[Union[str, int]]
            The column name or index to use for the timeseries sequence
        value_source:  Optional[Iterable[Union[str, int]]]
            The column name(s) or indeces to use for the value sequence when
            the input is one of the data frame types
        timestamp_target: Optional[str]
            The name of the timestamp column to use in the produced dataframe. Only applicable if
            timeseries does not have column names.
        value_target: Optional[Iterrable[str]]
            The column names to use in the resulting spark dataframe. Only applicable if timeseries
            does not have column names. If vall_col_names is provided, val_col_prefix will be ignored.
        ignore_unused_col_args:  bool
            Ignore column args passed to the conversion when the input does not
            require them. This can be useful when the conversion function is
            called without knowledge of the input type.
        **kwargs:
            Additional keyword args to pass to the construction of the pyspark.sql.DataFrame.
            NOTE: The set of valid args may depend on the precise type of input_arg.

    Returns:
        timeseries:  pyspark.sql.DataFrame
            The converted pyspark DataFrame
    """
    # Make sure we have pyspark
    if not HAVE_PYSPARK:
        raise RuntimeError("Cannot run without 'pyspark' installed")

    # Make sure that the value columns are provided correctly
    if isinstance(value_source, (str, int)):
        value_source = [value_source]

    # Figure out which converter to call
    converter = None
    cols_required = False
    input_is_dataframe = False
    if HAVE_PANDAS and isinstance(input_arg, pd.DataFrame):
        cols_required = True
        input_is_dataframe = True
        converter = _pandas_to_spark
    elif isinstance(input_arg, np.ndarray):
        cols_required = True
        converter = _ndarray_to_spark
    elif HAVE_TSPY and isinstance(input_arg, tspy.data_structures.BoundTimeSeries):
        converter = _tspy_bound_to_spark
    elif HAVE_TSPY and isinstance(
        input_arg, tspy.data_structures.TimeSeries.TimeSeries
    ):
        converter = _tspy_unbound_to_spark
    elif isinstance(input_arg, pyspark.sql.DataFrame):
        # for completeness
        input_is_dataframe = True
    elif not isinstance(input_arg, pyspark.sql.DataFrame):
        converter = _raw_timeseries_to_spark

    if converter is None:
        return input_arg

    # Make sure col args are either given or not based on the type
    if cols_required:
        _validate_has_col_args(timestamp_source, value_source)
    elif not ignore_unused_col_args:
        _validate_no_col_args(timestamp_source, value_source)

    converter_kwargs = kwargs
    # only specify ts col name and value column names for output if
    # we don't have an input dataframe (pyspark or pandas)
    if not input_is_dataframe:
        converter_kwargs[VALUE_TARGET_NAME_ARG] = value_target
        converter_kwargs[TIMESTAMP_TARGET_NAME_ARG] = (
            timestamp_target
            if timestamp_target is not None
            else DEFAULT_TIMESTAMP_TARGET_NAME
        )
    elif any(val is not None for val in [timestamp_target, value_target]):
        raise ValueError(
            "Changing column names is not supportred when the source is a data frame type"
        )

    # If a valid converter is found, make sure the columns args are given
    # NOTE: The converters will handle type-specific validation errors
    return converter(
        input_arg,
        timestamp_source,
        value_source,
        **converter_kwargs,
    )


def get_val_col_names_for_df(num_vals: int) -> List[str]:
    """Get a list of column names for use in a dataframe. Resulting names
    will have the form: "{prefix}0", "{prefix}1", ... "{prefix}{num_vals-1}"

    Args:
        num_vals:  Integer
            The number of value columns to generate names for
    Returns:
        List[str]:  List of strings to use as column names.
    """
    return [f"{DEFAULT_VALUE_TARGET_PREFIX}{i}" for i in range(num_vals)]


## -> RawTimeseries ############################################################


def _pandas_to_raw_timeseries(
    data_frame: "pd.DataFrame",
    timestamp_source: str,
    value_source: Iterable[str],
) -> RawTimeseries:
    """Converter for pd.DataFrame -> RawTimeseries"""
    _validate_pandas_cols(data_frame, timestamp_source, value_source)

    # The columns were found, so extract them lazily
    if len(value_source) == 1:
        return zip(data_frame[timestamp_source], data_frame[value_source[0]])
    else:
        return zip(
            data_frame[timestamp_source],
            (
                tuple(vals)
                for vals in zip(
                    *[data_frame[val_col_name] for val_col_name in value_source]
                )
            ),
        )


def _numpy_to_raw_timeseries(
    array: "np.ndarray",
    ts_col_idx: int,
    val_col_idxs: int,
) -> RawTimeseries:
    """Converter for np.ndarray"""
    dims = len(array.shape)
    if dims != 2:
        raise ValueError(
            f"Cannot convert non-2D ndarray with dimension {dims} to timeseries"
        )
    num_cols = array.shape[1]
    invalid_cols = [
        entry[0]
        for entry in filter(
            lambda entry: entry[1],
            [
                (col_idx, not isinstance(col_idx, int) or col_idx >= num_cols)
                for col_idx in [ts_col_idx] + list(val_col_idxs)
            ],
        )
    ]
    if invalid_cols:
        invalid_cols_str = ", ".join([str(col_idx) for col_idx in invalid_cols])
        raise IndexError(f"Invalid column values: {invalid_cols_str}")

    # Return a zipped representation of the two columns
    if len(val_col_idxs) == 1:
        return zip(array[:, ts_col_idx], array[:, val_col_idxs[0]])
    else:
        return zip(
            array[:, ts_col_idx],
            (
                tuple(vals)
                for vals in zip(
                    *[array[:, val_col_idx] for val_col_idx in val_col_idxs]
                )
            ),
        )


def _spark_to_raw_timeseries(
    data_frame: "pyspark.sql.DataFrame",
    timestamp_source: str,
    value_source: Iterable[str],
) -> RawTimeseries:
    """Converter for spark.sql.DataFrame"""
    # Convert to pandas and run the pandas converter
    return _pandas_to_raw_timeseries(
        data_frame.toPandas(),
        timestamp_source,
        value_source,
    )


def _tspy_bound_to_raw_timeseries(
    timeseries: "tspy.data_structures.BoundTimeSeries",
    *_,
) -> RawTimeseries:
    """Converter for tspy.data_structures.BoundTimeSeries"""

    # to_numpy will use byte buffer implementation if backed by DirectByteBuffer
    time_ticks, values = timeseries.to_numpy()
    return (
        (
            time_ticks[i],
            tuple(values[i]) if isinstance(values[i], np.ndarray) else values[i],
        )
        for i in range(len(time_ticks))
    )


def _tspy_unbound_to_raw_timeseries(
    timeseries: "tspy.data_structures.TimeSeries.TimeSeries",
    *_,
) -> RawTimeseries:
    """Converter for tspy.data_structures.TimeSeries.TimeSeries"""
    return _tspy_bound_to_raw_timeseries(timeseries[:])


## -> ndarray ##################################################################


def _pandas_to_ndarray(
    data_frame: "pd.DataFrame",
    timestamp_source: str,
    value_source: Iterable[str],
    **kwargs,
) -> "np.ndarray":
    """pd.DataFrame -> np.ndarray"""
    _validate_pandas_cols(data_frame, timestamp_source, value_source)
    all_cols = [timestamp_source] + value_source
    return data_frame[all_cols].to_numpy(**kwargs)


def _spark_to_ndarray(
    data_frame: "pyspark.sql.DataFrame",
    timestamp_source: str,
    value_source: Iterable[str],
    **kwargs,
) -> "np.ndarray":
    """pyspark.DataFrame -> np.array"""
    return _pandas_to_ndarray(
        data_frame.toPandas(),
        timestamp_source,
        value_source,
        **kwargs,
    )


def _tspy_bound_to_ndarray(
    timeseries: "tspy.data_structures.BoundTimeSeries",
    *_,
    **kwargs,
) -> "np.ndarray":
    """tspy.data_structures.BoundTimeSeries -> np.ndarray"""

    # to_numpy will use byte buffer implementation if backed by DirectByteBuffer
    time_ticks, values = timeseries.to_numpy()
    return np.column_stack([time_ticks, values])


def _tspy_unbound_to_ndarray(
    timeseries: "tspy.data_structures.TimeSeries.TimeSeries",
    *_,
    **kwargs,
):
    """tspy.data_structures.TimeSeries.TimeSeries -> np.ndarray"""
    return _tspy_bound_to_ndarray(timeseries[:], **kwargs)


def _raw_timeseries_to_ndarray(
    timeseries: RawTimeseries,
    *_,
    **kwargs,
):
    """RawTimeseries -> np.ndarray"""
    # If this is single-variate, just create the array directly, otherwise
    # flatten the values to create rows
    return np.array(
        [
            [ts] + (list(val) if isinstance(val, tuple) else [val])
            for ts, val in timeseries
        ],
        **kwargs,
    )


## -> tspy unbound ##########################################################


def _raw_timeseries_to_tspy_unbound(
    timeseries: RawTimeseries,
    *_,
    **kwargs,
) -> "tspy.data_structures.time_series.TimeSeries.TimeSeries":
    return _ndarray_to_tspy_unbound(_raw_timeseries_to_ndarray(timeseries))
    # todo we should be using builder but its still using java backend here, will address in tspy
    # ts_builder = tspy.builder()
    # for ts, val in timeseries:
    #     ts_builder.add(ts, val)
    # return ts_builder.result().to_time_series()


def _pandas_to_tspy_unbound(
    data_frame: "pd.DataFrame",
    timestamp_source: str,
    value_source: Iterable[str],
    **kwargs,
) -> "tspy.data_structures.time_series.TimeSeries.TimeSeries":
    if sum(1 for _ in value_source) == 1:  # is this a list?
        value_source = value_source[0]
    return tspy.time_series(
        data_frame, ts_column=timestamp_source, value_column=value_source
    )


def _spark_to_tspy_unbound(
    data_frame: "pyspark.sql.DataFrame",
    timestamp_source: str,
    value_source: Iterable[str],
    **kwargs,
):
    if sum(1 for _ in value_source) == 1:  # is this a list?
        value_source = value_source[0]
    return tspy.time_series(
        data_frame.toPandas(), ts_column=timestamp_source, value_column=value_source
    )


def _tspy_bound_to_tspy_unbound(
    bts: "tspy.data_structures.observations.BoundTimeSeries.BoundTimeSeries",
    *_,
    **kwargs,
):
    return bts.to_time_series()


def _ndarray_to_tspy_unbound(nd_array, *_, **kwargs):
    nd_array_transpose = nd_array.transpose()

    if len(nd_array_transpose) > 2:
        values = np.column_stack(
            [nd_array_transpose[i] for i in range(1, len(nd_array_transpose))]
        )
    else:
        values = nd_array_transpose[1]

    return tspy.observations(nd_array_transpose[0], values).to_time_series()


## -> spark DataFrame ##########################################################


def _pandas_to_spark(
    data_frame: "pd.DataFrame",
    timestamp_source: str,
    value_source: Iterable[str],
    **kwargs,
) -> "pyspark.sql.DataFrame":
    """pd.DataFrame -> pyspark.sql.DataFrame
    uses pyspark-native capability to ingest pandas dataframes
    """
    _validate_pandas_cols(data_frame, timestamp_source, value_source)
    all_cols = [timestamp_source] + value_source
    session = pyspark.sql.SparkSession.builder.getOrCreate()
    df = session.createDataFrame(data_frame[all_cols], **kwargs)

    # Attach the timestamp and value column names as additional attributes on
    # the data frame. This is a local attribute that allows auto-deduced column
    # names to be programmatically accessed in the local python session.
    setattr(df, TIMESTAMP_TARGET_NAME_ARG, timestamp_source)
    setattr(df, VALUE_TARGET_NAME_ARG, value_source)

    return df


def _ndarray_to_spark(
    array: "np.ndarray",
    ts_col_idx: int,
    val_col_idxs: int,
    timestamp_target: str,
    value_target: Optional[Iterable[str]],
    **kwargs,
) -> "pyspark.sql.DataFrame":
    """np.ndarray -> pyspark.sql.DataFrame"""
    raw = _numpy_to_raw_timeseries(array, ts_col_idx, val_col_idxs)
    return _raw_timeseries_to_spark(
        raw,
        timestamp_target=timestamp_target,
        value_target=value_target,
        **kwargs,
    )


def _raw_timeseries_to_spark(
    timeseries: RawTimeseries,
    *_,
    timestamp_target: str,
    value_target: Optional[Iterable[str]],
    **kwargs,
) -> "pyspark.sql.DataFrame":
    """RawTimeseries -> pyspark.sql.DataFrame"""

    session = pyspark.sql.SparkSession.builder.getOrCreate()

    # Determine the target column names for the value columns
    if value_target is None:

        # Get first element to create column labels for template
        try:
            first_ts, first_val = list(islice(timeseries, 1))[0]
        except IndexError:
            raise ValueError(
                "Provided time series should contain at least one time point."
            )

        # Figure out the number of columns needed
        # NOTE: This assumes all elements have the same width
        num_vals = len(first_val) if isinstance(first_val, tuple) else 1
        value_target = get_val_col_names_for_df(num_vals)

        # Depending on input iterable, we may have consumed an element, so put it back
        if isinstance(timeseries, collections.abc.Iterator):
            timeseries = chain([(first_ts, first_val)], timeseries)

    names = (timestamp_target,) + tuple(value_target)
    row_helper = _make_row_helper(names)
    rows = (row_helper(ts, val) for ts, val in timeseries)

    df = session.createDataFrame(rows, **kwargs)

    # Attach the timestamp and value column names as additional attributes on
    # the data frame. This is a local attribute that allows auto-deduced column
    # names to be programmatically accessed in the local python session.
    setattr(df, TIMESTAMP_TARGET_NAME_ARG, timestamp_target)
    setattr(df, VALUE_TARGET_NAME_ARG, value_target)

    return df


def _make_row_helper(names: List[str]) -> Callable:
    """Function to create a helper function for formatting rows.

    The helper function produces appropriate Rows for the spark dataframe
    1. Formats timestamp and values appropriately so that they can be ingested by spark.
    2. Creates a tuple of information needed for the row
    3. Converts the tuple to a Row

    Args:
        names ([List[str]]): names of columns to create row template

    Returns:
        Callable: Function to create formatted rows. The returned function will return
            pyspark.sql.Row: Row object containing ts information at a paritcular time
    """

    row_template = pyspark.sql.Row(*names)

    # create function to format rows appropriately usiing above template
    # ts: Timestamp, val: Any

    return lambda ts, val: row_template(
        *(
            (_spark_type_conversion(ts),)
            + (
                tuple([_spark_type_conversion(v) for v in val])
                if isinstance(val, tuple)
                else (_spark_type_conversion(val),)
            )
        )
    )


def _tspy_bound_to_spark(
    timeseries: "tspy.data_structures.BoundTimeSeries",
    *_,
    timestamp_target: str,
    value_target: Optional[Iterable[str]],
    **kwargs,
) -> "pyspark.sql.DataFrame":
    """tspy.data_structures.BoundTimeSeries -> pyspark.sql.DataFrame"""
    raw = _tspy_bound_to_raw_timeseries(timeseries, **kwargs)
    return _raw_timeseries_to_spark(
        raw,
        timestamp_target=timestamp_target,
        value_target=value_target,
        **kwargs,
    )


def _tspy_unbound_to_spark(
    timeseries: "tspy.data_structures.TimeSeries.TimeSeries",
    *_,
    timestamp_target: str,
    value_target: Optional[Iterable[str]],
    **kwargs,
) -> "pyspark.sql.DataFrame":
    """tspy.data_structures.TimeSeries.TimeSeries -> pyspark.sql.DataFrame"""

    raw = _tspy_unbound_to_raw_timeseries(timeseries, **kwargs)
    return _raw_timeseries_to_spark(
        raw,
        timestamp_target=timestamp_target,
        value_target=value_target,
        **kwargs,
    )


def _spark_type_conversion(x: Any) -> Any:
    """use tolist to convert to native types, this might not be very robust
    numpy objects support tolist to produce native python types, instead of numpy types

    More complex conversion logic can go here as the need arises
    """
    if hasattr(x, "tolist"):
        return x.tolist()
    else:
        return x


## Implementation Helpers ######################################################


def _validate_has_col_args(
    timestamp_source: Union[str, int],
    value_source: Iterable[Union[str, int]],
):
    """Make sure that the column args are provided"""
    if None in [timestamp_source, value_source]:
        missing_cols = [
            entry[0]
            for entry in filter(
                lambda entry: entry[1] is None,
                [
                    ("timestamp_source", timestamp_source),
                    ("value_source", value_source),
                ],
            )
        ]
        raise ValueError(f"Missing required conversion columns: {missing_cols}")


def _validate_no_col_args(
    timestamp_source: Union[str, int],
    value_source: Iterable[Union[str, int]],
):
    """Make sure conversion arguments were not given when no conversion is being
    performed
    """
    provided_cols = [
        entry[0]
        for entry in filter(
            lambda entry: entry[1],
            [
                (col_label, col is not None)
                for col, col_label in [
                    (timestamp_source, TIMESTAMP_SOURCE_ARG),
                    (value_source, VALUE_SOURCE_ARG),
                ]
            ],
        )
    ]
    if provided_cols:
        raise ValueError(
            f"Received conversion arguments {provided_cols} but no conversion needed"
        )


def _validate_pandas_cols(
    data_frame: "pd.DataFrame",
    timestamp_source: str,
    val_col_names: Iterable[str],
):
    """Shared source column validation for all pandas converters"""
    # Get the names of the columns to use for the timestamps and the
    # values. If either is missing, no conversion is applied, so the
    # function will receive the raw DataFrame.
    unknown_cols = [
        entry[0]
        for entry in filter(
            lambda entry: entry[1],
            [
                (col, col not in data_frame.columns)
                for col in [timestamp_source] + list(val_col_names)
            ],
        )
    ]
    if unknown_cols:
        raise KeyError(f"Unknown data frame column(s): {unknown_cols}")
