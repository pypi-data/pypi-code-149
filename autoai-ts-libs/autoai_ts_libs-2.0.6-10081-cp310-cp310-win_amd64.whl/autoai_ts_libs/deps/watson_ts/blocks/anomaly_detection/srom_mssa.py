"""
Block implementation that wraps srom.anomaly_detection.algorithms.mSSA.Mssa
"""

# First Party
from srom.anomaly_detection.algorithms.mSSA import Mssa as WrappedEstimator
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "e98ee944-01e8-4049-83e7-a5959a375062",
    "Block wrapper for srom.anomaly_detection.algorithms.mSSA.Mssa",
    "0.0.1",
)
class Mssa(SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X)
