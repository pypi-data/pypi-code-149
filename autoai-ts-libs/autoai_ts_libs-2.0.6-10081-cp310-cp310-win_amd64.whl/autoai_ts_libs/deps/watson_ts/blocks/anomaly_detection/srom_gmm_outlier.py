"""
Block implementation that wraps srom.anomaly_detection.algorithms.gmm_outlier.GMMOutlier
"""

# First Party
from srom.anomaly_detection.algorithms.gmm_outlier import GMMOutlier as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "3f1c2848-a2b5-4a3f-9b37-0ce16adc9cc8",
    "Block wrapper for srom.anomaly_detection.algorithms.gmm_outlier.GMMOutlier",
    "0.0.1",
)
class GMMOutlier(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
