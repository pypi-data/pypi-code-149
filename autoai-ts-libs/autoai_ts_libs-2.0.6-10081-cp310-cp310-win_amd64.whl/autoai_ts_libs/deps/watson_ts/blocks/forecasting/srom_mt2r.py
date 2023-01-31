"""
Forecaster block implementation that wraps
srom.time_series.models.MT2RForecaster
"""

# First Party
from srom.time_series.models.MT2RForecaster import MT2RForecaster as SROMMT2RForecaster
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import ForecasterBase


@block(
    "99f002b3-9a6d-4fbf-b89f-be276d2364be",
    "Trend-to-Residual Multi-Step Multi-Variate Singal Predictor.",
    "0.0.1",
)
class MT2RForecaster(
    ForecasterBase,
    SKLearnEstimatorMixin,
    SKLearnPredictorMixin,
):
    __doc__ = __doc__
    _WRAPPED_CLASS = SROMMT2RForecaster
    _TS_COL_PARAM = "time_column"
    _VAL_COLS_PARAM = "feature_columns"
