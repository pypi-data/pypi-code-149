"""
Block implementation that wraps srom.time_series.augmentor.TrendOutlier
"""

# First Party
from srom.time_series.augmentor import TrendOutlier as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "080ddfc7-d4da-44be-8aac-075ec4c2a575",
    "Block wrapper for srom.time_series.augmentor.TrendOutlier",
    "0.0.1",
)
class TrendOutlier(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
