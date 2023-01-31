"""
Block implementation that wraps srom.anomaly_detection.algorithms.HotellingT2
"""

# First Party
from srom.anomaly_detection.algorithms import HotellingT2 as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "5bf022bf-4369-45d6-a846-037181d6dcd8",
    "Block wrapper for srom.anomaly_detection.algorithms.HotellingT2",
    "0.0.1",
)
class HotellingT2(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
