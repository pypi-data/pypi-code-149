"""
Block implementation that wraps srom.time_series.pipeline._reconstruct_ad.ReconstructAD
"""

# First Party
from srom.time_series.pipeline._reconstruct_ad import ReconstructAD as WrappedEstimator
from watson_core import workflow

# Local
from ..sklearn_mixins import SKLearnWorkflowMixin
from .base import SKLearnAnomalyDetectorWorkflowMixin, SROMPredictionTypeMixin


@workflow(
    "cc2f109a-420e-4262-8b80-5dd99f8b370b",
    "Block wrapper for srom.time_series.pipeline._reconstruct_ad.ReconstructAD",
    "0.0.1",
)
class ReconstructAD(
    SROMPredictionTypeMixin, SKLearnWorkflowMixin, SKLearnAnomalyDetectorWorkflowMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
