"""
Implementation of random forest regressor method from FCTK.
"""

# First Party
from fctk.methods.ensemble.random_forest_spark import (
    RandomForestRegressor as WrappedRandomForestRegressor,
)
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import ForecasterBase


@block("27757ceb-876b-42ae-8976-bc16a1a7f658", "Random Forest Regressor", "0.0.1")
class RandomForestRegressor(
    ForecasterBase, SKLearnEstimatorMixin, SKLearnPredictorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedRandomForestRegressor
    _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns
