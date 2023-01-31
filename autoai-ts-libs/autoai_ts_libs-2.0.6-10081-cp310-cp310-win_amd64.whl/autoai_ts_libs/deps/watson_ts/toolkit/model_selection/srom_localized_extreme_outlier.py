"""
Block implementation that wraps srom.anomaly_detection.pipeline_utils.LocalizedExtremeOutlier
"""
# First Party
from srom.anomaly_detection.pipeline_utils import (
    LocalizedExtremeOutlier as WrappedEstimator,
)

# Local
from autoai_ts_libs.deps.watson_ts.toolkit.model_selection.base import CrossValidator


class LocalizedExtremeOutlier(CrossValidator):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
