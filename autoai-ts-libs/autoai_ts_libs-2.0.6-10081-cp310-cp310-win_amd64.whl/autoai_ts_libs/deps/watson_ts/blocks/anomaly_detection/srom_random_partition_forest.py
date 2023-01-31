"""
Block implementation that wraps srom.anomaly_detection.algorithms.random_partition_forest.RandomPartitionForest
"""

# First Party
from srom.anomaly_detection.algorithms.random_partition_forest import (
    RandomPartitionForest as WrappedEstimator,
)
from watson_core import block

# Local
from .base import SKLearnAnomalyDetectorMixin
from autoai_ts_libs.deps.watson_ts.blocks.sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin


@block(
    "b95ba0a1-b4ea-40d1-9a8c-5b7b38bdf09d",
    "Block wrapper for srom.anomaly_detection.algorithms.random_partition_forest.RandomPartitionForest",
    "0.0.1",
)
class RandomPartitionForest(
    SKLearnEstimatorMixin, SKLearnPredictorMixin, SKLearnAnomalyDetectorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    def fit(self, X, y=None) -> "SKLearnEstimatorMixin":
        return super().fit(X, y)
