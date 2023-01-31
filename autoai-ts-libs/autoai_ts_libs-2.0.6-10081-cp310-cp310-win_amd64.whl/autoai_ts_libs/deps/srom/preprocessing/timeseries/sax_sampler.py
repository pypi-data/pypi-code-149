# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


""""""
"""
.. module:: sax_sampler
   :synopsis: SymbolicAggregateApproximation
.. moduleauthor:: SROM Team
"""
import numpy as np
from autoai_ts_libs.deps.srom.preprocessing.timeseries.sampler import Sampler
from autoai_ts_libs.deps.srom.feature_engineering.timeseries.functions import get_symbolicaggregation
from sklearn.preprocessing import KBinsDiscretizer


class SymbolicAggregateApproximation(Sampler):
    """
    Transforms the data into a Symbolic Aggregate Approximation (SAX) transformation.

    Parameters
    ----------
    n_bins : int or array-like, shape (n_features,) (default=5)
        The number of bins to produce. Raises ValueError if ``n_bins < 2``.
    encode : {'onehot', 'onehot-dense', 'ordinal'}, (default='onehot')
        Method used to encode the transformed result.

        onehot
            Encode the transformed result with one-hot encoding
            and return a sparse matrix. Ignored features are always
            stacked to the right.
        onehot-dense
            Encode the transformed result with one-hot encoding
            and return a dense array. Ignored features are always
            stacked to the right.
        ordinal
            Return the bin identifier encoded as an integer value.
    """

    def __init__(self, n_bins=5, encode="ordinal", inverse=False):
        """

        """
        super().__init__()
        self.n_bins = n_bins
        self.encode = encode
        self.inverse = inverse

    def fit(self, X, y=None):
        """
        Fit the Symbolic Approximator transformer
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
        Transform the data to SAX transformed form

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
        if len(X_) < 1:
            return float(np.NaN)
        X_ = X.copy()
        self.bins = {}
        X_transformed = np.zeros(X.shape)
        for dim in range(X.shape[1]):
            X_transformed[:, dim], tmpMdl = get_symbolicaggregation(
                X_[:, dim], n_bins=self.n_bins, encode=self.encode, return_trained_bins=True
            )
            self.bins[dim] = tmpMdl
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
        X_inverse = np.zeros(X.shape)
        for dim in self.bins.keys():
            X_inverse[:,dim] = (self.bins[dim].inverse_transform(X[:,dim].reshape(-1,1))).reshape(-1)
        return X_inverse
