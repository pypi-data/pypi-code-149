"""
Block implementation that wraps srom.anomaly_detection.algorithms.oob.OOB
"""

# First Party
from srom.anomaly_detection.algorithms.oob import OOB as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "899d75f8-f096-4fc5-9da5-f0e53dd838c7",
    "Block wrapper for srom.anomaly_detection.algorithms.oob.OOB",
    "0.0.1",
)
class OOB(SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
