# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: srom_lof
   :synopsis: srom_lof.
   
.. moduleauthor:: SROM Team
"""

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.neighbors import LocalOutlierFactor
import numpy as np


class LOFNearestNeighborAnomalyModel(BaseEstimator, ClassifierMixin):
    """
    An example of Nearest Neighbor based Algorithm.
    """

    # knn function gets the dataset and calculates K-Nearest neighbors and distances
    # reachDist calculates the reach distance of each point to MinPts around it

    def __init__(self, n_neighbors=10, anomaly_threshold=2.0):
        """
        Parameters:
            n_neighbors (integer, optional): Number of neighbors to use. Defaults to 10.
        """
        self.n_neighbors = n_neighbors
        self.anomaly_threshold = anomaly_threshold
        self.model = LocalOutlierFactor(n_neighbors=self.n_neighbors, novelty=True)

    def set_params(self, **kwarg):
        """
        Set the parameters of the estimator.

        Parameters:
            kwargs: keyword arguments, set of params and its values.
        """
        if "n_neighbors" in kwarg:
            self.n_neighbors = kwarg["n_neighbors"]
            self.model.set_params(n_neighbors=self.n_neighbors)
        return self

    def fit(self, X, y=None):
        """
        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of \
                shape:(n_samples, n_features) \
                Set of samples, where n_samples is the number of samples \
                and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of LOFNearestNeighborAnomalyModel.

        Raises:
            RuntimeError : When model is None.
        """
        if self.model is None:
            raise RuntimeError("You must have classifier for training!")

        self.model.fit(X)

        # derive some parameter to be used for generating class label
        train_score = self.anomaly_score(X)
        self.train_mean = np.mean(train_score)
        self.train_std = np.std(train_score)

        return self

    def predict(self, X, y=None):
        """
        Calls anomaly_score() which returns anomaly scores.

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
            y (pandas dataframe or numpy array, optional): Mix of normal and abnormal data. \
                Defaults to None.

        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.

        Raises:
            RuntimeError : When model is None.
        """
        if not self.model:
            raise RuntimeError("You must have trained model!")

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

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.

        Returns:
            numpy.ndarray : Anomaly scores.
        """
        if not self.model:
            raise RuntimeError("You must have classifier.")
        return -1 * self.model.decision_function(X)

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector.
        """
        return self.anomaly_score(X)
