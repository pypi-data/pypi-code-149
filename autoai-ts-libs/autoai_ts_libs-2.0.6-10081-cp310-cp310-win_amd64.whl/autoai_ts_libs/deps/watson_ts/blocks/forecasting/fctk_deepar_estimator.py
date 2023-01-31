"""
Implementation of DeepAR estimator method from FCTK.
"""

# First Party
from fctk.methods.deepar.deepar_estimator import DeepAREstimator as WrappedEstimator
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import ForecasterBase


@block("bbe45e15-ece7-451d-93fb-8df3b8792ba8", "DeepAR Estimator", "0.0.1")
class DeepAREstimator(ForecasterBase, SKLearnEstimatorMixin, SKLearnPredictorMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
    _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns
