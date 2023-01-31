"""
Block implementation that wraps srom.anomaly_detection.algorithms.anomaly_ensembler.AnomalyEnsembler
"""

# First Party
from srom.anomaly_detection.algorithms.anomaly_ensembler import (
    AnomalyEnsembler as WrappedEstimator,
)
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import SKLearnAnomalyDetectorMixin


@block(
    "711e4fa0-bbf5-4069-91df-9a7a9a25d228",
    "Block wrapper for srom.anomaly_detection.algorithms.anomaly_ensembler.AnomalyEnsembler",
    "0.0.1",
)
class AnomalyEnsembler(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
