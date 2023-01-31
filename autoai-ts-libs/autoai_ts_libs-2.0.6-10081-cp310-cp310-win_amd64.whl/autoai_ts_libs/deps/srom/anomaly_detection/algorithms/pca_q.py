# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: srom_pca_Q
   :synopsis: Implementation of PCA based algorithm with Q statistics.
   
.. moduleauthor:: SROM Team
"""

import math
from sklearn.base import BaseEstimator
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from scipy.stats import norm


class AnomalyPCA_Q(BaseEstimator):
    """
    PCA based Anomaly
    """

    def __init__(self, scale=True, variance_threshold=0.7, alpha=0.05):
        """
        Parameters:
            scale (boolean, optional): Enable scaling. Defaults to True.
            variance_threshold (float, optional): Defaults to 0.7.
            alpha (float, optional): Defaults to 0.05.
        """
        self.scale = scale
        self.variance_threshold = variance_threshold
        self.alpha = alpha

        self.pca = None
        self.scaler = None
        self.ucl = 0

    def set_params(self, **kwarg):
        """
        Set the parameters of this estimator.

        Parameters:
            kwargs : Keyword arguments, set of params and its values.
        """
        if "scale" in kwarg:
            self.scale = kwarg["scale"]
        if "variance_threshold" in kwarg:
            self.variance_threshold = kwarg["variance_threshold"]
        if "alpha" in kwarg:
            self.alpha = kwarg["alpha"]
        return self

    def fit(self, X, y=None):
        """
        Fit estimator.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of AnomalyPCA_Q.

        Raises:
            Exception : When variance_threshold is greater than number of columns.
        """
        X = X.astype(np.float64)

        # scaling
        if self.scale:
            self.scaler = StandardScaler()
            X = self.scaler.fit_transform(X)

        # fit pca
        self.pca = PCA()
        self.pca.fit(X)

        # select number of component to choose using variance_threshold
        cpv = np.cumsum(self.pca.explained_variance_ratio_)
        num_selected_com = np.min(np.where(cpv >= self.variance_threshold)[0]) + 1

        if num_selected_com == X.shape[1]:
            raise Exception("variance_threshold should be reduced")

        # derive (upper) control limits, assuming n is not very big or else use chi2
        q1 = np.sum(self.pca.singular_values_[num_selected_com:])
        q2 = np.sum(np.power(self.pca.singular_values_[num_selected_com:], 2))
        q3 = np.sum(np.power(self.pca.singular_values_[(num_selected_com):], 3))

        h0 = 1.0
        if np.abs(q2) > 0:
            h0 = 1.0 - ((2 * q1 * q3) / (3 * q2 * q2))
        alpha_val = norm.ppf(1 - self.alpha)
        self.ucl = 0
        if np.abs(q1) > 0:
            self.ucl = (
                1.0
                + ((q2 * h0 * (h0 - 1)) / (q1 * q1))
                + ((alpha_val * h0 * math.sqrt(2 * q2)) / q1)
            ) * q1

        # update pca
        self.pca = PCA(n_components=num_selected_com)
        self.pca.fit(X)

        return self

    def predict(self, X):
        """
        Calls anomaly_score() which returns anomaly scores.

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.

        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """
        tmp_score = self.anomaly_score(X)
        ind1 = np.where(tmp_score >= self.ucl)[0]
        ind0 = np.where(tmp_score < self.ucl)[0]
        if ind1.size > 0:
            tmp_score[ind1] = -1
        if ind0.size > 0:
            tmp_score[ind0] = 1
        return tmp_score

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.

        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.

        Raises:
            Exception : When the model is not trained.
        """
        if not self.pca:
            raise Exception("Please train the model.")

        # each sample will be scored separately
        X = X.astype(np.float64)

        # get the projected space if required
        if self.scale and self.scaler:
            X = self.scaler.transform(X)

        # get the projected data
        A = np.dot(X, np.transpose(self.pca.components_))
        reg_X = np.dot(A, self.pca.components_)

        # set the selected component to zero
        # get the per sample score
        res_error = X - reg_X
        s_res_X = np.square(res_error)
        tmp_score = np.sqrt(np.sum(s_res_X, axis=1))
        return tmp_score

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector.
        """
        return self.anomaly_score(X)
