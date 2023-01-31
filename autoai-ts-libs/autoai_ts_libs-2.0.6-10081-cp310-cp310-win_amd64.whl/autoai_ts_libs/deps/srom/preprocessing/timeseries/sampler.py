# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


""""""
"""
.. module:: sampler
   :synopsis: Sampler
.. moduleauthor:: SROM Team
"""

from sklearn.base import TransformerMixin


class Sampler(TransformerMixin):
    """
    Sampler reduces/increases the size of the input through transformations/ \
    inverse transformations
    """

    def __init__(self,):
        """

        """
        pass

    def fit(self, X, y=None):
        """
        Fit the sampler transformer
        """
        return self

    def transform(self, X, y=None):
        """
        Transform the data to sampled form

        Parameters
        ----------
        X : array-like of input
            Time series dataset

        Returns
        -------
        numpy.ndarray
            Transformed dataset
        """
        return X

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
