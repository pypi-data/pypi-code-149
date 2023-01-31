"""
Block implementation that wraps srom.anomaly_detection.algorithms.anomaly_robust_pca.AnomalyRobustPCA
"""

# First Party
from srom.anomaly_detection.algorithms.anomaly_robust_pca import (
    AnomalyRobustPCA as WrappedEstimator,
)
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "5fb6e57e-9790-409a-a2fb-11998abd59a6",
    "Block wrapper for srom.anomaly_detection.algorithms.anomaly_robust_pca.AnomalyRobustPCA",
    "0.0.1",
)
class AnomalyRobustPCA(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
