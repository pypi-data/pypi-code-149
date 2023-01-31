"""
Block implementation that wraps srom.anomaly_detection.algorithms.GraphQUIC
"""

# First Party
from srom.anomaly_detection.algorithms import GraphQUIC as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "610226b3-b633-4a9c-956b-715d075dda92",
    "Block wrapper for srom.anomaly_detection.algorithms.GraphQUIC",
    "0.0.1",
)
class GraphQUIC(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X)
