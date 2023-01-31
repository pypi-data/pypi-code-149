"""
Block implementation that wraps srom.anomaly_detection.algorithms.spad.SPAD
"""

# First Party
from srom.anomaly_detection.algorithms.spad import SPAD as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "21a5ee6b-b96c-4d8d-a800-70013f3cc76d",
    "Block wrapper for srom.anomaly_detection.algorithms.spad.SPAD",
    "0.0.1",
)
class SPAD(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
