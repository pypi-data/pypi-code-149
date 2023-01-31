"""
Block implementation that wraps srom.anomaly_detection.algorithms.extended_mincovdet.MinCovDet
"""

# First Party
from srom.anomaly_detection.algorithms.extended_mincovdet import (
    MinCovDet as WrappedEstimator,
)
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin


@block(
    "86b57fe7-082b-4bc0-8255-26320c9b3528",
    "Block wrapper for srom.anomaly_detection.algorithms.extended_mincovdet.MinCovDet",
    "0.0.1",
)
class MinCovDet(SKLearnEstimatorMixin, SKLearnAnomalyDetectorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
