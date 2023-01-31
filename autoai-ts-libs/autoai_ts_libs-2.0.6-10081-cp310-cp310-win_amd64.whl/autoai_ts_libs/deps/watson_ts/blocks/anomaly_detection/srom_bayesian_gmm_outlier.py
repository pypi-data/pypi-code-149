"""
Block implementation that wraps srom.anomaly_detection.algorithms.bayesian_gmm_outlier.BayesianGMMOutlier
"""

# First Party
from srom.anomaly_detection.algorithms.bayesian_gmm_outlier import (
    BayesianGMMOutlier as WrappedEstimator,
)
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "be48c8f9-02ab-4c3d-bfe6-438bcbe8670f",
    "Block wrapper for srom.anomaly_detection.algorithms.bayesian_gmm_outlier.BayesianGMMOutlier",
    "0.0.1",
)
class BayesianGMMOutlier(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
