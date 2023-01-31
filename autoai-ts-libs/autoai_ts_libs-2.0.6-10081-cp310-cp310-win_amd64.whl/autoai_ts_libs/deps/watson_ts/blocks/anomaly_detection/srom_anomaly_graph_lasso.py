"""
Block implementation that wraps srom.anomaly_detection.algorithms.AnomalyGraphLasso
"""

# First Party
from srom.anomaly_detection.algorithms import AnomalyGraphLasso as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "68f60957-1ea9-41d0-bb47-e72a25b95c0d",
    "Block wrapper for srom.anomaly_detection.algorithms.AnomalyGraphLasso",
    "0.0.1",
)
class AnomalyGraphLasso(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X)
