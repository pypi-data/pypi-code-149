"""
Block implementation that wraps srom.anomaly_detection.algorithms.LOFNearestNeighborAnomalyModel
"""

# First Party
from srom.anomaly_detection.algorithms import (
    LOFNearestNeighborAnomalyModel as WrappedEstimator,
)
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "6649b473-0e5a-40cd-be0c-ff7370a2ef35",
    "Block wrapper for srom.anomaly_detection.algorithms.LOFNearestNeighborAnomalyModel",
    "0.0.1",
)
class LOFNearestNeighborAnomalyModel(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
