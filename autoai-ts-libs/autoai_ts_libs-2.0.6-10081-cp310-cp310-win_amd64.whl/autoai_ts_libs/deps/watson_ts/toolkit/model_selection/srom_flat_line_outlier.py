"""
Block implementation that wraps srom.anomaly_detection.pipeline_utils.FlatLineOutlier
"""
# First Party
from srom.anomaly_detection.pipeline_utils import FlatLineOutlier as WrappedEstimator

# Local
from autoai_ts_libs.deps.watson_ts.toolkit.model_selection.base import CrossValidator


class FlatLineOutlier(CrossValidator):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
