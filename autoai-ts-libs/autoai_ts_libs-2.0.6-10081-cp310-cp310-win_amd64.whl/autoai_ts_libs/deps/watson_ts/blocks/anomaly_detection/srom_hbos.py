"""
Block implementation that wraps srom.anomaly_detection.algorithms.hbos.HBOS
"""

# First Party
from srom.anomaly_detection.algorithms.hbos import HBOS as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "830254ea-3c99-498b-a2ca-ffe2924dbde1",
    "Block wrapper for srom.anomaly_detection.algorithms.hbos.HBOS",
    "0.0.1",
)
class HBOS(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
