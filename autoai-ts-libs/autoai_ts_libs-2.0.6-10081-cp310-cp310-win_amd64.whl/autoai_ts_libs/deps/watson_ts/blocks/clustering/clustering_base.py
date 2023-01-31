# Standard
import abc

# Third Party
import numpy as np

# First Party
from watson_core.toolkit.errors import error_handler
import alog

# Local
from autoai_ts_libs.deps.watson_ts.base import PredictorBase

log = alog.use_channel("WatsonCore Clustering Base Mixin")
error = error_handler.get(log)


class ClusteringBase(PredictorBase):
    """
    Base class for Time-Series Clustering Models
    """

    @property
    @abc.abstractmethod
    def cluster_centers_(self):
        """
        get the cluster centers
        """

    @property
    @abc.abstractmethod
    def labels_(self) -> np.ndarray:
        """
        get the cluster labels
        """

    @property
    @abc.abstractmethod
    def n_iter_(self):
        """
        get number of iterations
        """

    @property
    @abc.abstractmethod
    def intra_cluster_distances(self) -> np.ndarray:
        """
        returns the intra cluster distances
        """

    @property
    @abc.abstractmethod
    def inter_cluster_distances(self) -> np.ndarray:
        """
        returns the inter cluster distances
        """

    @property
    @abc.abstractmethod
    def silhouette_coefficients(self) -> np.ndarray:
        """
        returns the silhouette coefficients for this model
        """
