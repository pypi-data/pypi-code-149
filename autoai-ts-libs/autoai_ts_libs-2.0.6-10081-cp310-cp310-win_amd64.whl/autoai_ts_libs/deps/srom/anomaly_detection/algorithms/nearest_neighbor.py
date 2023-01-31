# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: nearest_neighbor
   :synopsis: Nearest neighbor anomaly model.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.neighbors import NearestNeighbors
import numpy as np


class NearestNeighborAnomalyModel(BaseEstimator, ClassifierMixin):
    """Nearest Neighbor based Algorithm"""

    def __init__(self, n_neighbors=10, anomaly_threshold=2.0):
        """
        Parameters:
            n_neighbors (integer, optional): Number of neighbors to use. Defaults to 10.
            anomaly_threshold (float, optional): Generate Class Label. Defaults to 2.0.
        """
        self.n_neighbors = n_neighbors
        self.anomaly_threshold = anomaly_threshold
        self.model = NearestNeighbors(n_neighbors=self.n_neighbors)
        self.train_mean = None
        self.train_std = None

    def set_params(self, **kwarg):
        """
        Set the parameters of the estimator.

        Parameters:
            kwargs : Keyword arguments, set of params and its values.

        Returns:
            self: Returns the set of params and its values.
        """
        if "n_neighbors" in kwarg:
            self.n_neighbors = kwarg["n_neighbors"]
            self.model.set_params(n_neighbors=self.n_neighbors)
        if "anomaly_threshold" in kwarg:
            self.anomaly_threshold = kwarg["anomaly_threshold"]
        return self

    def fit(self, X, y=None):
        """
        Parameters:
            X (pandas dataframe or numpy array, required): Training data.If array or matrix, \
                shape [n_samples, n_features] or [n_samples, n_samples].
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of NearestNeighborAnomalyModel.
        """
        self.model.fit(X)
        # derive some parameter to be used for generating class label
        train_score = self.anomaly_score(X)
        self.train_mean = np.mean(train_score)
        self.train_std = np.std(train_score)
        return self

    def predict(self, X, y=None):
        """
        Returns prediction.

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            tmp_score (numpy.ndarray): Predictions.

        Raises Exception:
            RuntimeError : When model is not fitted.
        """
        if not self.train_mean or not self.train_std:
            raise RuntimeError("You must train the model!")

        tmp_score = self.anomaly_score(X)
        tmp_score = (tmp_score - self.train_mean) / self.train_std
        tmp_score[abs(tmp_score) < self.anomaly_threshold] = 0
        tmp_score[abs(tmp_score) > 0] = 1
        tmp_score[tmp_score == 1] = -1
        tmp_score[tmp_score == 0] = 1

        return tmp_score

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.

        Paramters:
            X (pandas dataframe or numpy array, required): Input Samples.

        Returns:
            scores (numpy.ndarray): Anomaly scores.
        """
        dist, _ = self.model.kneighbors(X)
        scores = np.log(np.mean(np.array(dist), axis=1))
        scores[np.isneginf(scores)] = 0
        return scores

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector.
        """
        return self.anomaly_score(X)
