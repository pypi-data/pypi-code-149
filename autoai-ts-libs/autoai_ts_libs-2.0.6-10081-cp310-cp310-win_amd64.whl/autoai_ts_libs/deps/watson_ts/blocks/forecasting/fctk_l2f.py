"""
Implementation of a forecaster block for the L2F method from FCTK.
"""

# First Party
from fctk.methods.l2f.l2f_scalable import NormedL2F as WrappedEstimator
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import ForecasterBase


@block("a73fa4e8-5c41-11ec-8cef-acde48001122", "L2F Forecaster", "0.0.1")
class NormedL2F(ForecasterBase, SKLearnEstimatorMixin, SKLearnPredictorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns
