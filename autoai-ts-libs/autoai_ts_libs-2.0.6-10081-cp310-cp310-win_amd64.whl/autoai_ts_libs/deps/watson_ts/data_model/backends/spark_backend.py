"""
Core data model backends backed by pandas
"""

# Standard
from typing import Any, Iterable, Optional, Tuple, Type, Union

# Third Party
# TODO: make pandas and numpy non-optional elsewhere!
# from google.protobuf import any_pb2
# import numpy as np
import pandas
import pyspark

# First Party
from watson_core.data_model import ProducerId

# from watson_core.data_model.data_backends import DataModelBackendBase
from watson_core.toolkit import error_handler
import alog

# Local
# from ...toolkit.timeseries_conversions import DEFAULT_TIMESTAMP_TARGET_NAME
from .base import TimeSeriesBackendBase
from .dfcache import EnsureCached
from .pandas_backends import PandasTimeSeriesBackend
from autoai_ts_libs.deps.watson_ts.data_model.timeseries import TimeSeries


log = alog.use_channel("SPBCK")
error = error_handler.get(log)


class SparkTimeSeriesBackend(TimeSeriesBackendBase):
    """The SparkTimeSeries is responsible for managing the standard
    in-memory representation of a TimeSeries using a spark backend compute engine.
    """

    def __init__(
        self,
        data_frame: pyspark.sql.DataFrame,
        timestamp_column: str = None,
        value_columns: Optional[Iterable[str]] = None,
        ids: Optional[Iterable[int]] = None,
        producer_id: Optional[Union[Tuple[str, str], ProducerId]] = None,
    ):
        """At init time, hold onto the data frame as well as the arguments that
        tell where the time and values live

        Args:
            data_frame:  pyspark.DataFrame
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

        self._pyspark_df: pyspark.sql.DataFrame = data_frame

        # for tapping into pandas api call when needed
        self._pyspark_pandas_df = self._pyspark_df.pandas_api()

        # this will give us basic parameter validation
        self._pdbackend_helper = PandasTimeSeriesBackend(
            data_frame=pandas.DataFrame(columns=data_frame.columns),
            value_columns=value_columns,
            timestamp_column=str(timestamp_column)
            if timestamp_column is not None
            else timestamp_column,
            ids=ids,
            producer_id=producer_id,
        )

        # Validators special to this class
        error.type_check("<WTS11947329E>", pyspark.sql.DataFrame, data_frame=data_frame)
        error.type_check(
            "<WTS81128381E>", str, int, type(None), timestamp_column=timestamp_column
        )

    def get_attribute(self, data_model_class: Type["TimeSeries"], name: str) -> Any:
        """When fetching a data attribute from the timeseries, this aliases to
        the appropriate set of backend wrappers for the various fields.
        """

        with EnsureCached(self._pyspark_df) as _:
            return self._pdbackend_helper.get_attribute(
                data_model_class=data_model_class,
                name=name,
                external_df=self._pyspark_pandas_df,
            )

    def as_pandas(self) -> pandas.DataFrame:
        """Return the underlying data frame"""
        # @todo fix the copy here
        return (
            self._pyspark_df.toPandas(),
            self._pdbackend_helper._timestamp_column,
            self._pdbackend_helper._value_columns,
        )
