# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: gaussianwindow_filter
   :synopsis: Gaussian Window Filter.

.. moduleauthor:: SROM Team
"""
from math import erfc, sqrt
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class GaussianWindowFilter(BaseEstimator, TransformerMixin):
    """
    Performs outlier detection on time series data \
    using Gaussian Window.
    """

    def __init__(self, columns_to_be_ignored=None, sliding_window_size=10,
                 probability_threshold=0.01):
        """
        Parameters:
            columns_to_be_ignored: Outlier will not be detected from the \
                column present in this list.
            sliding_window_size: The size of window used for outlier detection.
            probability_threshold: Value higher than threshold is labeled as outliers.
        """
        if columns_to_be_ignored:
            self.columns_to_be_ignored = columns_to_be_ignored
        else:
            self.columns_to_be_ignored = []
        self.sliding_window_size = sliding_window_size
        self.probability_threshold = probability_threshold

    def set_params(self, **kwarg):
        """
        Used to set params.
        """
        if 'columns_to_be_ignored' in kwarg:
            self.columns_to_be_ignored = kwarg['columns_to_be_ignored']
        if 'sliding_window_size' in kwarg:
            self.sliding_window_size = kwarg['sliding_window_size']
        if 'probability_threshold' in kwarg:
            self.probability_threshold = kwarg['probability_threshold']        

    def _normalProbability(self, x, mean, std):
        """
        Gives the normal distribution specified by the mean and standard \
        deviation args, return the probability of getting samples > x. \

        Q-function: The tail probability of the normal distribution.
        """
        if x < mean:
            xp = 2 * mean - x
            return self._normalProbability(xp, mean, std)

        z = (x - mean) / std
        return 0.5 * erfc(z / sqrt(2))

    # an internal method - evaluate whether the observation is outlier
    def _find_outlier_index_in_window(self, Xwin):
        """
        Parameters:
            Xwin: Pandas Series or single dimensional numpy array.

        Returns:
            None or a list of integer value between 0 to len(Xwin).
        """
        outlier_idx = []
        w_mean = np.nanmean(Xwin)
        w_std = np.nanstd(Xwin)

        if w_std:
            for i, val in enumerate(Xwin):
                if not np.isnan(val):
                    p_score = self._normalProbability(val, w_mean, w_std)
                    if p_score <= self.probability_threshold:
                        outlier_idx.append(i)
        return outlier_idx

    def _find_outliers(self, Xclm):
        """
        Parameters:
            Xclm: Pandas Series or single dimensional numpy array.

        Returns:
            outlier_idx: Position at which outliers are observed \
                for input column Xclm.
        """
        win = self.sliding_window_size
        outlier_idx = []
        for k in range(win, Xclm.size, win):
            idx = self._find_outlier_index_in_window(Xclm[k-win:k+win])
            if idx:
                for item in idx:
                    outlier_idx.append(k + item - win)
        outlier_idx = list(set(outlier_idx))
        return outlier_idx

    def fit(self, X, y=None):
        """
        Fit model.
        """
        return self

    def _transform(self, X):
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)
        if isinstance(X, pd.DataFrame):
            n_samples, _ = X.shape
            if self.sliding_window_size >= n_samples:
                raise Exception('Sliding Window should be less than the number of samples')
            outlier_mask = np.empty(X.shape)
            outlier_mask.fill(False)
            columns = X.columns
            for i, column in enumerate(columns):
                if column not in self.columns_to_be_ignored:
                    outlier_index = self._find_outliers(X[column])
                    outlier_mask[outlier_index, i] = True
            return outlier_mask
        else:
            raise Exception("Training set must be either pandas dataframe or numpy ndarray.")

    def fit_transform(self, X, y=None, **fit_params):
        """
        Fit to data, then transform it.

        Fits transformer to X and y and returns a transformed \
        version of X.

        Parameters:
            X: Training set (Pandas dataframe or numpy ndarray).
            y: Target values.

        Returns:
            Array of outlier Flag, with length = number of elements in X.

        Raises:
            Exception: If number of samples in X is less than sliding_window_size. \
                If training set is not either pandas dataframe or numpy ndarray.
        """
        return self._transform(X)

    def transform(self, X):
        """
        Transform data.

        Parameters:
            X: Training set (Pandas dataframe or numpy ndarray).

        Returns:
            Array of outlier Flag, with length = number of elements in X.

        Raises:
            Exception: If number of samples in X is less than sliding_window_size. \
                If training set is not either pandas dataframe or numpy ndarray.
        """
        return self._transform(X)
