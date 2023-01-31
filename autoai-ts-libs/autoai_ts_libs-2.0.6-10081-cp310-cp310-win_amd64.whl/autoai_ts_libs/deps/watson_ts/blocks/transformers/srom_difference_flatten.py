"""
Block implementation that wraps srom.preprocessing.ts_transformer.DifferenceFlatten
"""

# First Party
from srom.preprocessing.ts_transformer import DifferenceFlatten as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "713830bd-789d-4ebe-8461-c55b993fc12a",
    "Block wrapper for srom.preprocessing.ts_transformer.DifferenceFlatten",
    "0.0.1",
)
class DifferenceFlatten(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
