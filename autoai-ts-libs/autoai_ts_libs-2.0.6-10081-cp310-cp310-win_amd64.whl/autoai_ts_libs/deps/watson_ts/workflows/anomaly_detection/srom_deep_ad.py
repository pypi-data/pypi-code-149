"""
Workflow implementation that wraps srom.time_series.pipeline._deeap_ad.DeepAD
"""

# First Party
from srom.time_series.pipeline._deep_ad import DeepAD as WrappedEstimator
from watson_core import workflow

# Local
from ..sklearn_mixins import SKLearnWorkflowMixin
from .base import SKLearnAnomalyDetectorWorkflowMixin, SROMPredictionTypeMixin


@workflow(
    "0f8b893f-f614-4652-bdc2-0d6bfc3a27aa",
    "Workflow wrapper for srom.time_series.pipeline._deep_ad.DeepAD",
    "0.0.1",
)
class DeepAD(
    SROMPredictionTypeMixin, SKLearnWorkflowMixin, SKLearnAnomalyDetectorWorkflowMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
