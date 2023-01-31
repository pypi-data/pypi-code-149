# Standard
from typing import Any, Dict

# First Party
from watson_core import block
import tspy

# Local
from autoai_ts_libs.deps.watson_ts.blocks.watson_core_mixins import WatsonCoreTransformerMixin
from autoai_ts_libs.deps.watson_ts.toolkit import tspy_unbound_arg
from autoai_ts_libs.deps.watson_ts.toolkit.timeseries_conversions import TimeseriesType


@block(
    "713830bd-789d-4ebe-8461-c55b993fc12d",
    "Block wrapper for performing a generic segmentation operation and reducing each segment",
    "0.0.1",
)
class SegmentAndReduce(WatsonCoreTransformerMixin):
    """
    Block which will take in any tspy segmentation transform and segment the data and perform the given reduction
    operation on each segment
    """

    _ARTIFACTS_DIR = "artifacts"
    _MODEL_FILE = "model.bin"
    _MODEL_BIN_KEY = "model_binary"
    _PARAMS_KEY = "params"

    def __init__(self, segment_transform, reduce_transform):
        super().__init__()
        self._segment_transform = segment_transform
        self._reduce_transform = reduce_transform

    def _save_artifacts(self, path):
        to_save = tspy.ts_context.packages.java.util.HashMap()
        to_save.put("segment_transform", self._segment_transform)
        to_save.put("reduce_transform", self._reduce_transform)
        tspy.ts_context.packages.time_series.core.utils.PythonConnector.serializeObject(
            to_save, path
        )

    @classmethod
    def _load_artifacts(cls, path: str) -> Dict:
        loaded = tspy.ts_context.packages.time_series.core.utils.PythonConnector.deserializeObject(
            path
        )
        return {
            "segment_transform": loaded.get("segment_transform"),
            "reduce_transform": loaded.get("reduce_transform"),
        }

    def get_params(self, deep=True):
        return {
            "segment_transform": self._segment_transform,
            "reduce_trasnform": self._reduce_transform,
        }

    @tspy_unbound_arg(arg_name="timeseries")
    def run(
        self, timeseries: TimeseriesType, *_, **kwargs: Dict[str, Any]
    ) -> TimeseriesType:
        """
        This method will take in a time-series of any type and segment the time-series, then reduce the segments and
        return a new time-series
        """
        return timeseries.to_segments(self._segment_transform).transform(
            self._reduce_transform
        )
