"""
Block implementation that wraps srom.time_series.augmentor.Noise
"""

# First Party
from srom.time_series.augmentor import Noise as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "03005fc0-121a-4941-a248-029aad92b142",
    "Block wrapper for srom.time_series.augmentor.Noise",
    "0.0.1",
)
class Noise(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
