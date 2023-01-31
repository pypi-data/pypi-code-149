"""
Block implementation that wraps srom.anomaly_detection.algorithms.extended_spad.ExtendedSPAD
"""

# First Party
from srom.anomaly_detection.algorithms.extended_spad import (
    ExtendedSPAD as WrappedEstimator,
)
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "aba408f0-bf9e-41fa-8ebd-e2742008db32",
    "Block wrapper for srom.anomaly_detection.algorithms.extended_spad.ExtendedSPAD",
    "0.0.1",
)
class ExtendedSPAD(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
