"""
Implementation of lightgbm_ray method from FCTK.
"""

# Third Party
import pandas as pd  # to make missing deps tests pass

# First Party
from fctk.methods.ensemble.lightgbm_ray import (
    RayDistributedLightGBM as WrappedRayDistributedLightGBM,
)
from watson_core import block

# Local
from ..sklearn_mixins import SKLearnEstimatorMixin, SKLearnPredictorMixin
from .base import ForecasterBase


@block("e1652219-f4fb-4c19-b5e2-0bada1039a06", "Lightgbm Ray", "0.0.1")
class RayDistributedLightGBM(
    ForecasterBase, SKLearnEstimatorMixin, SKLearnPredictorMixin
):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedRayDistributedLightGBM
    _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns
