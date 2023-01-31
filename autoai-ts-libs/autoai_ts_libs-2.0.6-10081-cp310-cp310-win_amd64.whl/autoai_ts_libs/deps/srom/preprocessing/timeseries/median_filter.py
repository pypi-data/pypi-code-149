# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: median_filter
   :synopsis: MedianFilter.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class MedianFilter(BaseEstimator, TransformerMixin):
    """
    Performs outlier detection on time series data \
    using Median Filter
    """

    def __init__(self, columns_to_be_ignored=None, sliding_window_size=10, median_threshold=3):
        """
        Parameters:
            columns_to_be_ignored: Outlier will not be detected from the column present \
                in this list.
            sliding_window_size: The size of window used for outlier detection.
            median_threshold: The median threshold used to detect the outlier.
        """
        if columns_to_be_ignored:
            self.columns_to_be_ignored = columns_to_be_ignored
        else:
            self.columns_to_be_ignored = []
        self.sliding_window_size = sliding_window_size
        self.median_threshold = median_threshold

    def set_params(self, **kwarg):
        """
        Used to set params.
        """
        if 'columns_to_be_ignored' in kwarg:
            self.columns_to_be_ignored = kwarg['columns_to_be_ignored']
        if 'sliding_window_size' in kwarg:
            self.sliding_window_size = kwarg['sliding_window_size']
        if 'median_threshold' in kwarg:
            self.iqr_threshold = kwarg['median_threshold']    

    # an internal method - evaluate whether the observation is outlier
    def _find_outlier_index_in_window(self, Xwin):
        """
        Parameters:
            Xwin: Pandas Series or single dimensional numpy array.
            median_threshold: Threshold used to detect the outlier \
                in the given window.

        Returns:
            None or a list of integer value between 0 to len(Xwin)
        """
        non_nan_idx = []
        tmp_Xwin = []

        for i, val in enumerate(Xwin):
            if not np.isnan(val):
                non_nan_idx.append(i)
                tmp_Xwin.append(val)

        non_nan_idx = np.array(non_nan_idx)

        #TODO : raise error len(tmp_Xwin) == 0
        if not tmp_Xwin:
            return None

        difference = np.abs(tmp_Xwin - np.median(tmp_Xwin))
        median_difference = np.median(difference)

        if abs(median_difference) > 0:
            deviation = difference / float(median_difference)
            mask = list(deviation > self.median_threshold)
            outlier_index = []
            for i, _ in enumerate(tmp_Xwin):
                if mask[i]:
                    outlier_index.append(i)
            return non_nan_idx[outlier_index]
        return None

    def _find_outliers(self, Xclm):
        """
        Parameters:
            Xclm: Pandas Series or single dimensional numpy array.
            win: A size of sliding window for outlier detection.

        Returns:
            Position at which outliers are observed for input column Xclm.
        """
        win = self.sliding_window_size
        outlier_idx = []
        for k in range(win, Xclm.size, win):
            idx = self._find_outlier_index_in_window(Xclm[k-win:k+win])
            if idx is not None:
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
