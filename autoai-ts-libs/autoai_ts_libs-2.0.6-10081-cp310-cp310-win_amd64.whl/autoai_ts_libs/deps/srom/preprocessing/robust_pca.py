# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: robust_pca
   :synopsis: RobustPCA
        This algorithm takes data and apply robust PCA iteratively \
        and tranform the original data into new data such that the 
        noise and anomaly in the data is eliminated.

.. moduleauthor:: SROM Team
"""
from __future__ import division
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class RobustPCA(BaseEstimator, TransformerMixin):
    """
    Performs Data Cleansing of the input multivariate signal \
    on dataset using Robust PCA.
    """

    def __init__(self, tolerance=None, max_iter=1000, mu=None, Lambda=None):
        """
        Parameters:
            tolerance: Outlier threshold (initialized internally). Defaults to None.
            max_iter (int): Number of iteration to apply. Defaults to 1000.
            mu: A kind of parameter to control the output (initialized internally).
                Defaults to None.
            Lambda: A kind of parameter to control the output (initialized internally).
                Defaults to None.
        """
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.mu = mu
        self.Lambda = Lambda
        self.S = None
        self.L = None

    def _initialize_var(self, X_shape):
        self.S = np.zeros(X_shape)
        if not self.mu:
            self.mu = np.prod(X_shape) / (4 * self._norm_p(X_shape, 2))

        if not self.Lambda:
            self.Lambda = 1 / np.sqrt(np.max(X_shape))

    def _norm_p(self, M, p):
        return np.sum(np.power(M, p))

    def _shrink(self, M, tau):
        return np.sign(M) * np.maximum((np.abs(M) - tau), np.zeros(M.shape))

    def _svd_threshold(self, M, tau):
        U, S, V = np.linalg.svd(M, full_matrices=False)
        return np.dot(U, np.dot(np.diag(self._shrink(S, tau)), V))

    def fit(self, X, y=None):
        """
        Fit model
        """
        return self

    def _transform(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        self._initialize_var(X.shape)
        iteration = 0
        err = np.Inf
        Sk = self.S
        Yk = np.zeros(X.shape)
        Lk = np.zeros(X.shape)
        mu_inv = 1 / self.mu

        if self.tolerance:
            _tol = self.tolerance
        else:
            _tol = 1e-7 * self._norm_p(np.abs(X), 2)

        while err > _tol and iteration < self.max_iter:
            Lk = self._svd_threshold(X - Sk + mu_inv * Yk, mu_inv)
            Sk = self._shrink(X - Lk + (mu_inv * Yk), mu_inv * self.Lambda)
            Yk = Yk + self.mu * (X - Lk - Sk)
            err = self._norm_p(np.abs(X - Lk - Sk), 2)
            iteration += 1

        self.L = Lk
        self.S = Sk
        return self.L

    def fit_transform(self, X, y=None, **fit_params):
        """
        Fit to data, then transform it. 
        Takes data and apply robust PCA iteratively and fit-tranform \
        the original data into new data such that the noise and anomaly \
        in the data is eliminated.

        Parameters:
            X: Training set (Pandas dataframe or numpy ndarray).
            y: Target values.

        Returns:
            (numpy ndarray): Outlier flags, with length = number of elements in X.
        """
        return self._transform(X)

    def transform(self, X):
        """
        Transform data.
        Takes data and apply robust PCA iteratively and tranform the original \
        data into new data such that the noise and anomaly in the data is eliminated.

        Parameters:
            X: Training set(Pandas dataframe or numpy ndarray).

        Returns:
            (numpy ndarray): Outlier flags, with length = number of elements in X.
        """
        return self._transform(X)
