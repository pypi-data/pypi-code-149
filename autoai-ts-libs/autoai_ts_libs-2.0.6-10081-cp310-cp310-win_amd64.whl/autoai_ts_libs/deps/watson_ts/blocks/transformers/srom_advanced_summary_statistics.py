"""
Block implementation that wraps srom.preprocessing.ts_transformer.AdvancedSummaryStatistics
"""

# First Party
from srom.preprocessing.ts_transformer import (
    AdvancedSummaryStatistics as WrappedEstimator,
)
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "45b1e6bb-8a62-4f32-8d4d-7f519686e6e4",
    "Block wrapper for srom.preprocessing.ts_transformer.AdvancedSummaryStatistics",
    "0.0.1",
)
class AdvancedSummaryStatistics(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
