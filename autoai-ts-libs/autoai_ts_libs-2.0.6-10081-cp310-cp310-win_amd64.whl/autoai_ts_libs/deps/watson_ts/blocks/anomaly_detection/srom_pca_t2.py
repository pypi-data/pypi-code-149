"""
Block implementation that wraps srom.anomaly_detection.algorithms.pca_t2.AnomalyPCA_T2
"""

# First Party
from srom.anomaly_detection.algorithms.pca_t2 import AnomalyPCA_T2 as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "81c7f05d-390d-43ea-95ba-4273e815f8f2",
    "Block wrapper for srom.anomaly_detection.algorithms.pca_t2.AnomalyPCA_T2",
    "0.0.1",
)
class AnomalyPCA_T2(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
