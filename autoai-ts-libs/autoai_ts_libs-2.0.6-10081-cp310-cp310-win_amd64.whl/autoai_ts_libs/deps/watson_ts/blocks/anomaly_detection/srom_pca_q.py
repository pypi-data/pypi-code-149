"""
Block implementation that wraps srom.anomaly_detection.algorithms.pca_q.AnomalyPCA_Q
"""

# First Party
from srom.anomaly_detection.algorithms.pca_q import AnomalyPCA_Q as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "504efd4a-5ef3-4eef-98c3-0112a76d677a",
    "Block wrapper for srom.anomaly_detection.algorithms.pca_q.AnomalyPCA_Q",
    "0.0.1",
)
class AnomalyPCA_Q(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
