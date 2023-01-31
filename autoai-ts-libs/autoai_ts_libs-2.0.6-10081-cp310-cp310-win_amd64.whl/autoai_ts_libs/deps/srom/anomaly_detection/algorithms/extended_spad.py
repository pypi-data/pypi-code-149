# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: extended_spad
   :synopsis: Implementation of ExtendedSPAD.
   
.. moduleauthor:: SROM Team
"""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.utils import check_array
from sklearn.decomposition import PCA
from sklearn.utils.validation import check_is_fitted


class ExtendedSPAD(BaseEstimator):
    """
    SPAD and PCA based Anomaly.            
    """

    def __init__(
        self,
        bins="auto",
        pca_model=PCA(
            n_components=2,
            whiten=False,
            svd_solver="auto",
            tol=0.0,
            iterated_power="auto",
            random_state=42,
        ),
    ):
        """
        Parameters:
        bins (str or int) : number of bins.
        n_components (int or none) : number of components.
        whiten (boolean) : wheather to whiten. 
        svd_solver (str), : svd solver.
        tol (float) : tolerance
        iterated_power (int or str) : number of iterations for the power method.
        random_state (int) : random state.
        """
        self.bins = bins
        self.pca_model = pca_model

    def set_params(self, **kwarg):
        """
        Set the parameters of the estimator.

        Parameters:
            kwargs: keyword arguments, set of params and its values.
        """
        if "bins" in kwarg:
            self.bins = kwarg["bins"]
            del kwarg["bins"]
        self.pca_model.set_params(**kwarg)
        return self

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
        X_tf = self.pca_model.fit_transform(X)
        self.n_samples, self.hist_, self.bin_edges_ = self.__train_x(X)
        self.n_samples_tf, self.hist_tf_, self.bin_edges_tf_ = self.__train_x(X_tf)
        return self

    def __train_x(self, X):
        """
        Internal helper function.
        """
        hist_ = []
        bin_edges_ = []
        n_samples, n_features = X.shape[0], X.shape[1]
        for i in range(n_features):
            hist, bin_edges = np.histogram(X[:, i], bins=self.bins, density=False)
            hist_.append(hist)
            bin_edges_.append(bin_edges)
        return n_samples, hist_, bin_edges_

    def __compute_scores(self, X, hist_, bin_edges_, n_samples):
        """
        Internal helper function.
        """
        n_samples, n_features = X.shape[0], X.shape[1]
        intermediate_scores = np.zeros([n_samples, n_features])
        for i in range(n_samples):
            for j in range(n_features):
                x = X[i, j]
                bin_edges = bin_edges_[j]
                no_bins = len(hist_[j])
                for k in range(no_bins):
                    if k != (no_bins - 1):
                        if bin_edges[k] <= x < bin_edges[k + 1]:
                            hist_cnt = hist_[j][k]
                            break
                    else:
                        if bin_edges[k] <= x <= bin_edges[k + 1]:
                            hist_cnt = hist_[j][k]
                        else:
                            hist_cnt = 0
                score = np.log((hist_cnt + 1) / (n_samples + no_bins))
                intermediate_scores[i][j] = score
        anomaly_score = np.sum(intermediate_scores, axis=1)
        return anomaly_score

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.

        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """
        check_is_fitted(self)
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()
        X = check_array(X)
        X_tf = self.pca_model.transform(X)
        anomaly_score = self.__compute_scores(
            X, self.hist_, self.bin_edges_, self.n_samples
        )
        anomaly_score_tf = self.__compute_scores(
            X_tf, self.hist_tf_, self.bin_edges_tf_, self.n_samples_tf
        )
        anomaly_score = anomaly_score + anomaly_score_tf
        return anomaly_score

    def decision_function(self, X):
        """
        Predict raw anomaly score of X using the fitted detector.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        """
        return self.anomaly_score(X)
