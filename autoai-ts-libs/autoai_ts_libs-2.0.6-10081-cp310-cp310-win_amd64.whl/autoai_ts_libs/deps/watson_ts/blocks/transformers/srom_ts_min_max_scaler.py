"""
Block implementation that wraps srom.preprocessing.transformer.TSMinMaxScaler
"""

# First Party
from srom.preprocessing.transformer import TSMinMaxScaler as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "7c633854-a064-4099-9590-ea8e2f565900",
    "Block wrapper for srom.preprocessing.transformer.TSMinMaxScaler",
    "0.0.1",
)
class TSMinMaxScaler(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
