"""
Block implementation that wraps srom.anomaly_detection.algorithms.extended_isolation_forest.ExtendedIsolationForest
"""

# First Party
from srom.anomaly_detection.algorithms.extended_isolation_forest import (
    ExtendedIsolationForest as WrappedEstimator,
)
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "0373b6d5-45fb-45c8-b6a1-a470747ea7b5",
    "Block wrapper for srom.anomaly_detection.algorithms.extended_isolation_forest.ExtendedIsolationForest",
    "0.0.1",
)
class ExtendedIsolationForest(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
