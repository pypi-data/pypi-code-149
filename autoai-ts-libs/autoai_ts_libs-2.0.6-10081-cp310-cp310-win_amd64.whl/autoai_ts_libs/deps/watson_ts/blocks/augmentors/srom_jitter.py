"""
Block implementation that wraps srom.time_series.augmentor.Jitter
"""

# First Party
from srom.time_series.augmentor import Jitter as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "d31a1082-f9b4-42c9-9367-d9b4d76224d2",
    "Block wrapper for srom.time_series.augmentor.Jitter",
    "0.0.1",
)
class Jitter(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
