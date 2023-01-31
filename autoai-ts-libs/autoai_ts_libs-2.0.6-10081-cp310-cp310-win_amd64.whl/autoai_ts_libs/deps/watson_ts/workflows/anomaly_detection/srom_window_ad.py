"""
Workflow implementation that wraps srom.time_series.pipeline._window_ad.WindowAD
"""

# First Party
from srom.time_series.pipeline._window_ad import WindowAD as WrappedEstimator
from watson_core import workflow

# Local
from ...toolkit.timeseries_conversions import TimeseriesType
from ..sklearn_mixins import SKLearnWorkflowMixin
from .base import SKLearnAnomalyDetectorWorkflowMixin, SROMPredictionTypeMixin


@workflow(
    "2621e121-16d9-4384-82c8-3228a165bb9e",
    "Workflow wrapper for srom.time_series.pipeline._window_ad.WindowAD",
    "0.0.1",
)
class WindowAD(
    SROMPredictionTypeMixin,
    SKLearnWorkflowMixin,
    SKLearnAnomalyDetectorWorkflowMixin,
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    # TODO: Determine if this estimator supports time/val column params
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"
