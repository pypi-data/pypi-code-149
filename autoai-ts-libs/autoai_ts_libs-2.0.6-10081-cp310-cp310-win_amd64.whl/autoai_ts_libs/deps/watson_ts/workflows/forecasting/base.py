"""
Shared baseclass for forecasting pipelines. Forecaster pipelines support fit, predict.
"""

# Local
from ..base import TSWorkflowBase


class ForecasterWorkflowBase(TSWorkflowBase):
    __doc__ = __doc__
