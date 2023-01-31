"""
Implementation of a forecasting workflow for the FCTK pipeline.
"""

# First Party
from fctk.pipeline import FCTKPipeline as wrappedpipeline
from watson_core import workflow

# Local
from ..sklearn_mixins import SKLearnWorkflowMixin
from .base import ForecasterWorkflowBase


@workflow("2bea46a5-0989-4dc6-95d7-05278ab64295", "FCTK Pipeline", "0.0.1")
class FCTKPipeline(ForecasterWorkflowBase, SKLearnWorkflowMixin):
    __doc__ = __doc__
    _WRAPPED_CLASS = wrappedpipeline
    _INTERNAL_TIMESERIES_TYPE = "spark"
