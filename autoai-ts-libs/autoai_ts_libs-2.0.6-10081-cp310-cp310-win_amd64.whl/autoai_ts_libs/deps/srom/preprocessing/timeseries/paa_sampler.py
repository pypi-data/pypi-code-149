# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


""""""
"""
.. module:: paa_sampler
   :synopsis: PiecewiseAggregateApproximation
.. moduleauthor:: SROM Team
"""
import numpy as np
from autoai_ts_libs.deps.srom.preprocessing.timeseries.sampler import Sampler
from autoai_ts_libs.deps.srom.feature_engineering.timeseries.functions import piecewise_aggregate_mean


class PiecewiseAggregateApproximation(Sampler):
    """
    Transforms the data into a Piecewise Aggregate Approximation (PAA) transformation.

    Parameters
    ----------
    n_segments : number of segments to divide the data into
    """

    def __init__(self, n_segments=5, inverse=False):
        super().__init__()
        self.n_segments = n_segments
        self.inverse = inverse

    def fit(self, X, y=None):
        """
        Fit the Piecewise Aggregate Approximator transformer
        Parameters
        ----------
        X : array-like of size (n,d) where d is the number of columns/features
            Time series dataset

        Returns
        -------
        self
        """
        self.X_shape = X.shape
        return self

    def transform(self, X, y=None):
        """
        Transform the data to piecewise aggregate transformed form

        Parameters
        ----------
        X : array-like of size (n,d) where d is the number of columns/features
            Time series dataset

        Returns
        -------
        numpy.ndarray
            Transformed dataset
        """
        X_ = X.copy()
        X_transformed = np.zeros((self.n_segments, X_.shape[1]))
        for dim in range(X.shape[1]):
            X_transformed[:, dim] = piecewise_aggregate_mean(
                X_[:, dim], n_segments=self.n_segments
            )
        if self.inverse:
            return self.inverse_transform(X_transformed)
        else:
            return X_transformed

    def fit_transform(self, X, y=None, **fit_params):
        """
        Fit a sampler representation and transform the data accordingly.

        Parameters
        ----------
        X : array-like of input
            Time series dataset

        Returns
        -------
        numpy.ndarray
            Transformed dataset
        """
        return self.fit(X).transform(X)

    def inverse_transform(self, X):
        """
        Compute time series corresponding to given sampled representations

        Parameters
        ----------
        X : array-like of input
            A sampled/transformed dataset

        Returns
        -------
        numpy.ndarray
            A dataset of time series corresponding to the provided representation.
        """
        X_inverse = np.zeros(self.X_shape)
        seg_sz = self.X_shape[0] // X.shape[0]
        for n in range(X.shape[0]):
            t_0 = int(n * seg_sz)
            for d in range(X.shape[1]):
                X_inverse[t_0 : t_0 + seg_sz, d] = X[n, d]
        return X_inverse
