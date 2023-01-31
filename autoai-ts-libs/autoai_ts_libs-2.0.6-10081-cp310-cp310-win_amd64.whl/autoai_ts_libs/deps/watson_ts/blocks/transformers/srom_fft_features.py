"""
Block implementation that wraps srom.preprocessing.ts_transformer.FFTFeatures
"""

# First Party
from srom.preprocessing.ts_transformer import FFTFeatures as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "a02072fb-55d3-4ce6-9b56-f0f7d23d28eb",
    "Block wrapper for srom.preprocessing.ts_transformer.FFTFeatures",
    "0.0.1",
)
class FFTFeatures(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
