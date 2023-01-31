# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


""""""
"""
.. module:: percentile_sampler
   :synopsis: PercentileApproximator
.. moduleauthor:: SROM Team
"""

from autoai_ts_libs.deps.srom.preprocessing.timeseries.sampler import Sampler
import numpy as np


class PercentileApproximator(Sampler):
    """
    Transforms the data into a percentile representation.

    Parameters
    ----------
    n_bins : number of bins to split into percentiles in
    """

    def __init__(self, n_bins=5, inverse=False):
        """

        """
        self.n_bins = n_bins
        self.inverse = inverse

    def fit(self, X, y=None):
        """
        Fit the Percentile Approximator transformer
        Parameters
        ----------
        X : array-like of input
            Time series dataset

        Returns
        -------
        self
        """
        n, d = X.shape
        X_ = X.copy()
        sz_segment = 100.0 // self.n_bins
        buckets = np.zeros((d, self.n_bins + 1))
        for dim in range(d):
            for i_seg in range(self.n_bins):
                start = i_seg * sz_segment
                end = start + sz_segment
                p_s = np.nanpercentile(X_[:, dim], start)
                p_e = np.nanpercentile(X_[:, dim], end)
                if i_seg == 0:
                    buckets[dim][i_seg] = p_s
                buckets[dim][i_seg + 1] = p_e
        self.segments = list(range(self.n_bins))
        self.buckets = buckets
        return self

    def transform(self, X, y=None):
        """
        Transform the data to percentile transformed form

        Parameters
        ----------
        X : array-like of input
            Time series dataset

        Returns
        -------
        numpy.ndarray
            Transformed dataset
        """

        n, d = X.shape
        X_transformed = X.copy()
        for dim in range(d):
            for i_val in range(n):
                X_transformed[i_val, dim] = min(
                    self.buckets[dim], key=lambda x: abs(x - X[i_val, dim])
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
        return X
