"""
Block implementation that wraps srom.preprocessing.transformer.Log
"""

# First Party
from srom.preprocessing.transformer import Log as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "f91c42fb-c1b1-40b7-b8d3-f723fca95e47",
    "Block wrapper for srom.preprocessing.transformer.Log",
    "0.0.1",
)
class Log(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
