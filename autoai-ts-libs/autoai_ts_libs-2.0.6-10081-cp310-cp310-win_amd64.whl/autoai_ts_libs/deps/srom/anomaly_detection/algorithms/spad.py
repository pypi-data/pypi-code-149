# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: spad
   :synopsis: Implementation of SPAD.
   
.. moduleauthor:: SROM Team
"""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.utils import check_array


class SPAD(BaseEstimator):
    """
    SPAD based Anomaly.           
    """

    def __init__(self, bins="auto"):
        """
            Parameters:
                bins (str or int) : number of bins. 
        """
        self.bins = bins
        self.hist_ = []
        self.bin_edges_ = []

    def fit(self, X, y=None):
        """
        Fit estimator.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of SPAD.
        """
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()
        X = check_array(X)
        n_samples, n_features = X.shape[0], X.shape[1]
        self.n_samples = n_samples
        for i in range(n_features):
            hist, bin_edges = np.histogram(X[:, i], bins=self.bins, density=False)
            self.hist_.append(hist)
            self.bin_edges_.append(bin_edges)
        return self

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.

        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()
        if not self.hist_:
            raise RuntimeError("You must have trained model!")
        X = check_array(X)
        n_samples, n_features = X.shape[0], X.shape[1]
        intermediate_scores = np.zeros([n_samples, n_features])
        for i in range(n_samples):
            for j in range(n_features):
                x = X[i, j]
                bin_edges = self.bin_edges_[j]
                no_bins = len(self.hist_[j])
                for k in range(no_bins):
                    if k != (no_bins - 1):
                        if bin_edges[k] <= x < bin_edges[k + 1]:
                            hist_cnt = self.hist_[j][k]
                            break
                    else:
                        if bin_edges[k] <= x <= bin_edges[k + 1]:
                            hist_cnt = self.hist_[j][k]
                        else:
                            hist_cnt = 0
                score = np.log((hist_cnt + 1) / (self.n_samples + no_bins))
                intermediate_scores[i][j] = score
        anomaly_score = np.sum(intermediate_scores, axis=1)
        return anomaly_score

    def decision_function(self, X):
        """
        Predict raw anomaly score of X using the fitted detector.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        """
        return self.anomaly_score(X)
