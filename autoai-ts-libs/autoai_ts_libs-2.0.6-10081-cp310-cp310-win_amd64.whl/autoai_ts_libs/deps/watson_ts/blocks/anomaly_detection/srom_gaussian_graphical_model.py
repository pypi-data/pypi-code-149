"""
Block implementation that wraps srom.anomaly_detection.gaussian_graphical_anomaly_model.GaussianGraphicalModel
"""

# First Party
from srom.anomaly_detection.gaussian_graphical_anomaly_model import (
    GaussianGraphicalModel as WrappedEstimator,
)
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import SKLearnAnomalyDetectorMixin


@block(
    "a2bfbd2e-25be-4836-b3cf-473ba48722ae",
    "Block wrapper for srom.anomaly_detection.gaussian_graphical_anomaly_model.GaussianGraphicalModel",
    "0.0.1",
)
class GaussianGraphicalModel(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
