"""
Block implementation that wraps srom.anomaly_detection.pipeline_utils.TrendOutlier
"""
# First Party
from srom.anomaly_detection.pipeline_utils import TrendOutlier as WrappedEstimator

# Local
from autoai_ts_libs.deps.watson_ts.toolkit.model_selection.base import CrossValidator


class TrendOutlier(CrossValidator):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
