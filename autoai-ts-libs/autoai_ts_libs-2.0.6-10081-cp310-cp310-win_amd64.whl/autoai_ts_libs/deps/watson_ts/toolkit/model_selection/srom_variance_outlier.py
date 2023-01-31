"""
Block implementation that wraps srom.anomaly_detection.pipeline_utils.VarianceOutlier
"""
# First Party
from srom.anomaly_detection.pipeline_utils import VarianceOutlier as WrappedEstimator

# Local
from autoai_ts_libs.deps.watson_ts.toolkit.model_selection.base import CrossValidator


class VarianceOutlier(CrossValidator):
    __doc__ = __doc__
    _WRAPPED_CLASS = WrappedEstimator
