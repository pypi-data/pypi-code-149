"""
Block implementation that wraps srom.anomaly_detection.algorithms.GraphPgscps
"""

# First Party
from srom.anomaly_detection.algorithms import GraphPgscps as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "bfdea3ee-b837-4a06-a165-ffeacdac6c8b",
    "Block wrapper for srom.anomaly_detection.algorithms.GraphPgscps",
    "0.0.1",
)
class GraphPgscps(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X)
