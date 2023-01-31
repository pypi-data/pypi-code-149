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
    "713830bd-789d-4ebe-8461-c55b993fc12c",
    "Block wrapper for tspy unary transforms",
    "0.0.1",
)
class UnaryTransform(WatsonCoreTransformerMixin):
    """
    Block which will take in any tspy UnaryTransform and transform the entirety of the data returning a RawTimeSeries
    """

    _ARTIFACTS_DIR = "artifacts"
    _MODEL_FILE = "model.bin"
    _MODEL_BIN_KEY = "model_binary"
    _PARAMS_KEY = "params"

    def __init__(self, unary_transform):
        super().__init__()
        self._unary_transform = unary_transform

    def _save_artifacts(self, path):
        tspy.ts_context.packages.time_series.core.utils.PythonConnector.serializeObject(
            self._unary_transform, path
        )

    @classmethod
    def _load_artifacts(cls, path: str) -> Dict:
        unary_transform = tspy.ts_context.packages.time_series.core.utils.PythonConnector.deserializeObject(
            path
        )
        return {"unary_transform": unary_transform}

    def get_params(self, deep=True):
        return {"unary_transform": self._unary_transform}

    @tspy_unbound_arg(arg_name="timeseries")
    def run(
        self, timeseries: TimeseriesType, *_, **kwargs: Dict[str, Any]
    ) -> TimeseriesType:
        """
        This method will take in a time-series of any type and return a raw-time series which has been transformed using
        a tspy UnaryTransform
        """
        return timeseries.transform(self._unary_transform)
