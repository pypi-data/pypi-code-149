"""
Block implementation that wraps srom.anomaly_detection.algorithms.kde.KDE
"""

# First Party
from srom.anomaly_detection.algorithms.kde import KDE as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "24b2407e-0d21-474b-9582-87a57daf5f9a",
    "Block wrapper for srom.anomaly_detection.algorithms.kde.KDE",
    "0.0.1",
)
class KDE(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X)
