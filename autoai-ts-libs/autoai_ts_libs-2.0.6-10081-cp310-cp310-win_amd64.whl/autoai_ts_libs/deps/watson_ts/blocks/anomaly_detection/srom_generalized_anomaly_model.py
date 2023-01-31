"""
Block implementation that wraps srom.anomaly_detection.generalized_anomaly_model.GeneralizedAnomalyModel
"""

# First Party
from srom.anomaly_detection.generalized_anomaly_model import (
    GeneralizedAnomalyModel as WrappedEstimator,
)
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import AnomalyDetectorBase, SKLearnAnomalyDetectorMixin


@block(
    "e77f2f64-6254-4720-9458-ec3bf7bea1c4",
    "Block wrapper for srom.anomaly_detection.generalized_anomaly_model.GeneralizedAnomalyModel",
    "0.0.1",
)
class GeneralizedAnomalyModel(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
