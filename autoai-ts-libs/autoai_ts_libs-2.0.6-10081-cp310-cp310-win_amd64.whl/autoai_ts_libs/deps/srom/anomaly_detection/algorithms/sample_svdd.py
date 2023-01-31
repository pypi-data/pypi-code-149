# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: sample_svdd
   :synopsis: sample_svdd.
   
.. moduleauthor:: SROM Team
"""

import numpy as np
from numpy.random import choice
from sklearn import svm
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.base import BaseEstimator
import pandas as pd


class SampleSVDD(BaseEstimator):
    """
    Sample SVDD : Extension to One Class SVM to build Support Vector Data Description
    """

    def __init__(
        self,
        outlier_fraction=0.001,
        kernel_s=2,
        maxiter=1000,
        sample_size=10,
        resample_n=3,
        stop_tol=1e-6,
        n_iter=30,
        seed=2513646,
    ):
        """
        Parameters:
            outlier_fraction (number) : outlier fraction.
            kernel_s (number) : kernel,
            maxite (number) : maximum iterations,
            sample_size (number) : sample size,
            resample_n (number) : resample size,
            stop_tol (number) : tolerance for stopping criterion.,
            n_iter (number) : no of iterations,
            seed (numver) : seed,

        """
        self.outlier_fraction = outlier_fraction
        self.kernel_s = kernel_s
        self.maxiter = maxiter
        self.sample_size = sample_size
        self.resample_n = resample_n
        self.stop_tol = stop_tol
        self.n_iter = n_iter
        self.seed = seed
        self.clf_ = None

    def _compute_radius_center(self, clf, method=1):
        """
        clf is one class svm object.
        """
        sv, coef = clf.support_vectors_, clf.dual_coef_
        sv_pos = np.where((coef < 1)[0, ...])[0]
        coef.shape = (coef.shape[1],)
        coef = coef / np.sum(coef)
        center = np.dot(coef, sv)
        if method == 0:
            m = rbf_kernel(sv, sv, gamma=clf.gamma)
            radius = (
                1 - 2 * np.dot(m[sv_pos[0], ...], coef) + np.dot(coef, np.dot(m, coef))
            )
        elif method == 1:
            v = sv[sv_pos[0], ...].reshape(1, sv.shape[1])
            m = rbf_kernel(v, sv, gamma=clf.gamma)
            radius = 1 - np.dot(m, coef)
        else:
            raise Exception("wrong method value")
        return radius, center

    def _do_one_class_svm_sample(self, gamma, nu, X, sample_indices, compute_rc=True):
        """
        build one class svm.
        """
        x_train_sample = X[sample_indices, ...]
        nsample = x_train_sample.shape[0]
        nu_1 = nu if nu * nsample > 1 else 1 / nsample
        clf = svm.OneClassSVM(gamma=gamma, nu=nu_1)
        clf.fit(x_train_sample)
        if compute_rc:
            radius, center = self._compute_radius_center(clf)
            return sample_indices[clf.support_], radius, center
        else:
            return sample_indices[clf.support_]

    def _do_one_class_svm_random(
        self, gamma, nu, x_train, sample_size, compute_rc=True
    ):
        """
            build one class svm.
        """
        sample = choice(x_train.shape[0], sample_size)
        return self._do_one_class_svm_sample(
            gamma, nu, x_train, sample, compute_rc=compute_rc
        )

    def fit(self, X, y=None):
        """
        Fit estimator.
        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.
        Returns:
            self: Trained instance of SampleSVDD.
        """
        X = X.astype(np.float64)

        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()

        if len(X.shape) != 2:
            raise ValueError("X must be 2d array.")

        if self.maxiter < 0:
            raise ValueError("maxiter cannot be less than zero.")

        nobs = X.shape[0]

        if nobs <= self.sample_size:
            raise ValueError("nobs is less than the sample size.")

        gamma, nu = 0.5 / (self.kernel_s * self.kernel_s), self.outlier_fraction

        if (
            np.isfinite(gamma) != True
            or np.isfinite(nu) != True
            or (nu < 0)
            or (nu > 1)
        ):
            raise ValueError("parameter to SVM has issues. Check value of nu and gamma")

        np.random.seed(seed=self.seed if self.seed >= 0 else None)

        # iteration 1
        sv_ind_prev, radius_prev, _ = self._do_one_class_svm_random(
            gamma, nu, X, self.sample_size
        )

        i = 0
        converged = 0
        iter_n = 0

        while i < self.maxiter:
            if converged:
                break

            sv_ind_local = self._do_one_class_svm_random(
                gamma, nu, X, self.sample_size, compute_rc=False
            )

            for _ in range(self.resample_n - 1):
                sv_ind_locals = self._do_one_class_svm_random(
                    gamma, nu, X, self.sample_size, compute_rc=False
                )
                sv_ind_local = np.union1d(sv_ind_locals, sv_ind_local)

            sv_ind_merge = np.union1d(sv_ind_local, sv_ind_prev)
            sv_ind_master, radius_master, center_master = self._do_one_class_svm_sample(
                gamma, nu, X, sv_ind_merge
            )
            iter_n = (
                iter_n + 1
                if np.fabs(radius_master - radius_prev)
                <= self.stop_tol * np.fabs(radius_prev)
                else 0
            )
            if iter_n >= self.n_iter:
                converged = 1
            else:
                sv_ind_prev, _, radius_prev = (
                    sv_ind_master,
                    center_master,
                    radius_master,
                )
            i += 1

        nsv = sv_ind_master.shape[0]
        self.clf_ = svm.OneClassSVM(gamma=gamma, nu=nu if nu * nsv > 1 else 1.0 / nsv)
        self.clf_.fit(X[sv_ind_master, ...])

        return self

    def predict(self, X):
        """
        Calls anomaly_score() which returns anomaly scores. -1 as anomaly and 1 as non anomaly.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """
        return self.clf_.predict(X)

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """

        # each sample will be scored separately
        return self.clf_.decision_function(X)

    def decision_function(self, X):
        """
        Predict raw anomaly score of X using the fitted detector.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """
        return self.anomaly_score(X)
