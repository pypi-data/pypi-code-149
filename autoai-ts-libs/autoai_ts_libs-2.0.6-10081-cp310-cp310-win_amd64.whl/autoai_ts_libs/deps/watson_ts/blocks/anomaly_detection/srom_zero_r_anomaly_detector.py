"""
Block implementation that wraps srom.time_series.models.zero_r_anomaly_detector.ZeroRAnomalyDetector
"""

# First Party
from srom.time_series.models.zero_r_anomaly_detector import (
    ZeroRAnomalyDetector as WrappedEstimator,
)
from watson_core import block

# Local
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "d31d5b2a-89b2-4a81-ae34-323a49b3bb6a",
    "Block wrapper for srom.time_series.models.zero_r_anomaly_detector.ZeroRAnomalyDetector",
    "0.0.1",
)
class ZeroRAnomalyDetector(SKLearnEstimatorMixin, SKLearnPredictorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X)
