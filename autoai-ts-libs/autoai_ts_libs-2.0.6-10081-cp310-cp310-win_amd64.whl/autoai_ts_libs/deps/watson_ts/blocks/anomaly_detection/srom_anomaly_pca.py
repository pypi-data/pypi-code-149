"""
Block implementation that wraps srom.anomaly_detection.algorithms.anomaly_pca.AnomalyPCA
"""

# First Party
from srom.anomaly_detection.algorithms.anomaly_pca import AnomalyPCA as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "4dd2346e-cfbf-4f32-bf19-72dd64e5797f",
    "Block wrapper for srom.anomaly_detection.algorithms.anomaly_pca.AnomalyPCA",
    "0.0.1",
)
class AnomalyPCA(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
