"""
Block implementation that wraps srom.preprocessing.transformer.DataStationarizer
"""

# First Party
from srom.preprocessing.transformer import DataStationarizer as WrappedEstimator
from watson_core import block

# Local
from ...toolkit.timeseries_conversions import TimeseriesType
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "198a9dc2-f5d7-45f8-9ef3-26d6125d1fb8",
    "Block wrapper for srom.preprocessing.transformer.DataStationarizer",
    "0.0.1",
)
class DataStationarizer(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def transform(
        self,
        timeseries: TimeseriesType,
        is_lookback_appended=False,
        lookback_win=0,
        *args,
        **kwargs
    ) -> TimeseriesType:
        """Delegate transform to the wrapped model"""
        with self._convert_to_internal_timeseries_type(timeseries, **kwargs) as (
            timeseries,
            kwargs,
        ):
            return self._wrapped_model.transform(
                timeseries, is_lookback_appended, lookback_win, *args, **kwargs
            )
