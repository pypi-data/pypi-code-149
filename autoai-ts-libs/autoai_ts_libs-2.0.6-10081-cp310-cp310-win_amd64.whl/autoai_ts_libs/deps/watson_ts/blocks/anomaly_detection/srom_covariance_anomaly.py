"""
Block implementation that wraps srom.anomaly_detection.algorithms.covariance_anomaly.CovarianceAnomaly
"""

# First Party
from srom.anomaly_detection.algorithms.covariance_anomaly import (
    CovarianceAnomaly as WrappedEstimator,
)
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import AnomalyDetectorBase, SKLearnAnomalyDetectorMixin


@block(
    "926d83e9-1971-4a1b-a723-04b8d47eec12",
    "Block wrapper for srom.anomaly_detection.algorithms.covariance_anomaly.CovarianceAnomaly",
    "0.0.1",
)
class CovarianceAnomaly(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
