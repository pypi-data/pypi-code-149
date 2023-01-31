"""
Block implementation that wraps srom.preprocessing.ts_transformer.LocalizedFlatten
"""

# First Party
from srom.preprocessing.ts_transformer import LocalizedFlatten as WrappedEstimator
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnTransformerMixin,
)


@block(
    "b0be605d-6682-4744-b2e4-16eb9171d9da",
    "Block wrapper for srom.preprocessing.ts_transformer.LocalizedFlatten",
    "0.0.1",
)
class LocalizedFlatten(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
