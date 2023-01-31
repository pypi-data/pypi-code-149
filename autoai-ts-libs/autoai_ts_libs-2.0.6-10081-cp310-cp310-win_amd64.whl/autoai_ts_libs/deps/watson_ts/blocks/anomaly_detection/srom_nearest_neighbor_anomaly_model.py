"""
Block implementation that wraps srom.anomaly_detection.algorithms.NearestNeighborAnomalyModel
"""

# First Party
from srom.anomaly_detection.algorithms import (
    NearestNeighborAnomalyModel as WrappedEstimator,
)
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import SKLearnAnomalyDetectorMixin


@block(
    "91b5f2f9-439a-4364-9fa4-b71bc457102d",
    "Block wrapper for srom.anomaly_detection.algorithms.NearestNeighborAnomalyModel",
    "0.0.1",
)
class NearestNeighborAnomalyModel(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
