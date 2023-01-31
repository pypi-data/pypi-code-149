# Standard
from typing import Dict

# Third Party
import numpy as np

# First Party
from tspy.ml.clustering import kshape
from watson_core import block
import tspy

# Local
from autoai_ts_libs.deps.watson_ts.blocks.clustering.clustering_base import ClusteringBase
from autoai_ts_libs.deps.watson_ts.blocks.watson_core_mixins import (
    WatsonCoreEstimatorMixin,
    WatsonCorePredictorMixin,
)
from autoai_ts_libs.deps.watson_ts.toolkit import tspy_unbound_arg
from autoai_ts_libs.deps.watson_ts.toolkit.timeseries_conversions import TimeseriesType


@block(
    "99f002b3-9a6d-4fbf-b89f-be276d2364bf",
    "K-Shape clustering model",
    "0.0.1",
)
class KShape(WatsonCoreEstimatorMixin, WatsonCorePredictorMixin, ClusteringBase):
    """
    Implementation of K-Shape Clustering on Time-Series
    """

    _ARTIFACTS_DIR = "artifacts"
    _MODEL_FILE = "model.bin"
    _MODEL_BIN_KEY = "model_binary"
    _PARAMS_KEY = "params"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # first check if this is coming from a loaded model or if this is a new model
        if "_params" in kwargs:
            self._model = kwargs["_model"]
            self._params = kwargs["_params"]
        else:
            self._model = kwargs.pop("_model", None)
            self._params = kwargs

    def _save_artifacts(self, path):
        # Standard
        import pickle

        with open(path, "wb") as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def _load_artifacts(cls, path: str) -> Dict:
        # Standard
        import pickle

        with open(path, "rb") as f:
            return pickle.load(f).__dict__

    def get_params(self, deep=True):
        return self._params

    def set_params(self, **params):
        self._params = params

    @property
    def cluster_centers_(self):
        return self._model._centroids

    @property
    def labels_(self):
        return np.array(self._model._centroids.keys())

    @property
    def n_iter_(self):
        return self._params["num_runs"]

    @property
    def intra_cluster_distances(self):
        return np.array([float(x) for x in self._model.intra_cluster_distances])

    @property
    def inter_cluster_distances(self):
        return np.array([float(x) for x in self._model.inter_cluster_distances])

    @property
    def silhouette_coefficients(self):
        return np.array([float(x) for x in self._model.silhouette_coefficients])

    # todo add multi-time-series
    @tspy_unbound_arg(arg_name="timeseries")
    def run(self, timeseries, with_silhouette=False):
        result = self._model.score(timeseries.materialize(), with_silhouette)
        if with_silhouette:
            return int(result[0]), float(result[1])
        else:
            return int(result)

    # todo add multi-time-series
    @classmethod
    @tspy_unbound_arg(arg_name="timeseries")
    def train(
        cls,
        timeseries: TimeseriesType,
        k_clusters,
        num_runs,
        use_eigen=True,
        init_strategy="plusplus",
        *_,
        **kwargs
    ) -> "WatsonCoreClusteringBase":

        # don't care about timestamps here, so just create numpy array to transpose
        time_ticks, values = timeseries.to_numpy()

        mts = tspy.multi_time_series(values.transpose())
        model = kshape.fit(mts, k_clusters, num_runs, use_eigen, init_strategy)
        return cls(
            k_clusters=k_clusters,
            num_runs=num_runs,
            use_eigen=use_eigen,
            init_strategy=init_strategy,
            _model=model,
        )
