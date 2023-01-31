"""
Workflow implementation that wraps srom.time_series.pipeline._relationship_ad.RelationshipAD
"""

# First Party
from srom.time_series.pipeline._relationship_ad import (
    RelationshipAD as WrappedEstimator,
)
from watson_core import workflow

# Local
from ..sklearn_mixins import SKLearnWorkflowMixin
from .base import SKLearnAnomalyDetectorWorkflowMixin, SROMPredictionTypeMixin


@workflow(
    "39ff44fb-5d2b-4769-87dd-e5837d3f51ba",
    "Block wrapper for srom.time_series.pipeline._relationship_ad.RelationshipAD",
    "0.0.1",
)
class RelationshipAD(
    SROMPredictionTypeMixin, SKLearnWorkflowMixin, SKLearnAnomalyDetectorWorkflowMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
