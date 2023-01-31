"""
Workflow implementation that wraps srom.time_series.pipeline._pred_ad.PredAD
"""

# First Party
from srom.time_series.pipeline._pred_ad import PredAD as WrappedEstimator
from watson_core import workflow

# Local
from ..sklearn_mixins import SKLearnWorkflowMixin
from .base import SKLearnAnomalyDetectorWorkflowMixin, SROMPredictionTypeMixin


@workflow(
    "88ade8d9-4657-4c09-8e45-722df2eccd2d",
    "Workflow wrapper for srom.time_series.pipeline._pred_ad.PredAD",
    "0.0.1",
)
class PredAD(
    SROMPredictionTypeMixin, SKLearnWorkflowMixin, SKLearnAnomalyDetectorWorkflowMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
