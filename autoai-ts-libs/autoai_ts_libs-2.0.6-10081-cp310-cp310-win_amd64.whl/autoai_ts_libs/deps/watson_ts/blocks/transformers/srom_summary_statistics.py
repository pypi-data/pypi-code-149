"""
Block implementation that wraps srom.preprocessing.ts_transformer.SummaryStatistics
"""

# First Party
from srom.preprocessing.ts_transformer import SummaryStatistics as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "4394d8c8-7f3b-4700-bae8-2f6f5e8cfeea",
    "Block wrapper for srom.preprocessing.ts_transformer.SummaryStatistics",
    "0.0.1",
)
class SummaryStatistics(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
