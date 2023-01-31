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


class RobustGGM(BaseEstimator, TransformerMixin):
    """[summary]

    Args:
        BaseEstimator ([type]): [description]
        TransformerMixin ([type]): [description]
    """

    def __init__(self, pho, lambda_, maxIteration=1000, epsilon=None):
        """[summary]

        Args:
            pho ([type]): [description]
            lambda ([type]): [description]
            maxIteration (int, optional): [description]. Defaults to 1000.
            epsilon ([type], optional): [description]. Defaults to None.
        """
        self.pho = pho
        self.lambda_ = lambda_
        self.maxIteration = maxIteration
        self.epsilon = epsilon

    def _solve_theta(self, decomp, mu_1):
        eigval, eigvec = np.linalg.eigh(decomp)
        Q = np.matrix(eigvec)
        D = eigval + np.sqrt(np.square(eigval) + 4 * mu_1)
        xdiag = np.matrix(np.diag(D))
        return 1.0 / (2 * mu_1) * Q * xdiag * Q.T

    def _solve_L(self, theta_, M, S, mu_2, U_2):
        return M - S + 1.0 / mu_2 * (U_2 - theta_)

    def _soft_threshold(self, data, value, substitute=0):
        data = np.asarray(data)
        magnitude = np.absolute(data)

        thresholded = 1 - value / magnitude
        thresholded.clip(min=0, max=None, out=thresholded)
        thresholded = data * thresholded

        if substitute == 0:
            return thresholded

        cond = np.less(magnitude, value)
        return np.where(cond, substitute, thresholded)

    def _projectSPD(self, A):
        eigval, eigvec = np.linalg.eigh(A)
        Q = np.matrix(eigvec)
        xdiag = np.matrix(np.diag(np.maximum(eigval, 0)))
        return Q * xdiag * Q.T

    def _Robust_glasso_S_first(self, M, pho_, lambda_, maxIteration=1000, epsilon=None):

        if epsilon is None:
            epsilon = 1e-7

        U_1 = M * 0.0
        U_2 = M * 0.0
        Z = M * 0.0
        theta_ = M * 0.0
        theta_temp = M * 0.0
        L = M * 0.0
        S = M - L

        mu_1 = 0.2
        mu_2 = 0.2

        iteration = 0

        while True:
            # Break if we use too many interations
            iteration += 1
            if iteration > maxIteration:
                break

            # step4 soft thresholding S
            threshold_S = lambda_ * 1.0 / mu_2
            soft_target_S = M - L + (1.0 / mu_2) * U_2

            # print 'soft_target_S',  soft_target_S
            # print "threshold_S", threshold_S
            S = self._soft_threshold(soft_target_S, threshold_S)
            S = np.matrix(S)
            # print 'after soft', S

            # step3 sovle and project L
            L_temp = self._solve_L(theta_, M, S, mu_2, U_2)
            L = self._projectSPD(L_temp)

            # update U_2
            U_2 = U_2 + mu_2 * (M - L - S)

            # step1 solve theta
            decomp = mu_1 * (Z - U_1) - L
            theta_ = self._solve_theta(decomp, mu_1)

            # step2 soft thresholding Z
            threshold_Z = pho_ * 1.0 / mu_1
            soft_target_Z = theta_ + U_1

            Z = self._soft_threshold(soft_target_Z, threshold_Z)
            Z = np.matrix(Z)

            # update U_1
            U_1 = U_1 + theta_ - Z

            if iteration > 1:
                criterion1 = (np.linalg.norm((theta_ - theta_temp), "fro") ** 2) / (
                    np.linalg.norm(theta_temp, "fro") ** 2
                )
                criterion2 = (np.linalg.norm((M - L - S), "fro") ** 2) / (
                    np.linalg.norm(M, "fro") ** 2
                )

                if criterion1 < epsilon and criterion2 < epsilon:
                    break

            mu_1 *= 1.2
            mu_2 *= 1.2
            theta_temp = theta_.copy()

        return theta_, S, L, iteration, criterion1, criterion2

    def fit(self, X, y=None):
        """
        Fit model
        """
        return self

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

    def _transform(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        return self._Robust_glasso_S_first(
            X, self.pho, self.lambda_, self.maxIteration, self.epsilon
        )[2]

