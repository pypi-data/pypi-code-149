# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: localhistogram_filter
   :synopsis: Local Histogram Based Filter.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class LocalHistogramFilter(BaseEstimator, TransformerMixin):
    """
    Performs outlier detection on time series data using \
    Local Histogram Filter.
    """

    def __init__(self, columns_to_be_ignored=None, sliding_window_size=10,
                 threshold=5.e-3, no_histogram_bins='auto'):
        """
        Parameters:
            columns_to_be_ignored: Outlier will not be detected from the \
                column present in this list.
            sliding_window_size: The size of window used for outlier detection.
            threshold: Probability threshold for marking outliers.
            no_histogram_bins: Number of bins for histogram construction.
        """
        if columns_to_be_ignored:
            self.columns_to_be_ignored = columns_to_be_ignored
        else:
            self.columns_to_be_ignored = []
        self.sliding_window_size = sliding_window_size
        self.threshold = threshold
        self.no_histogram_bins = no_histogram_bins
    
    def set_params(self, **kwarg):
        """
        Used to set params.
        """
        if 'columns_to_be_ignored' in kwarg:
            self.columns_to_be_ignored = kwarg['columns_to_be_ignored']
        if 'sliding_window_size' in kwarg:
            self.sliding_window_size = kwarg['sliding_window_size']
        if 'threshold' in kwarg:
            self.threshold = kwarg['threshold']        
        if 'no_histogram_bins' in kwarg:
            self.no_histogram_bins = kwarg['no_histogram_bins']   


    # an internal method - evaluate whether the observation is outlier
    def _find_outlier_index_in_window(self, Xwin):
        """
        Parameters:
            Xwin: Pandas Series or single dimensional numpy array.

        Returns:
            None or a list of integer value between 0 to len(Xwin).
        """
        non_nan_idx = []
        tmp_Xwin = []

        for i, val in enumerate(Xwin):
            if not np.isnan(val):
                non_nan_idx.append(i)
                tmp_Xwin.append(val)

        non_nan_idx = np.array(non_nan_idx)

        if not tmp_Xwin:
            return None

        ans1, ans2 = np.histogram(tmp_Xwin, bins=self.no_histogram_bins)
        a1 = ans2
        a2 = ans2
        a1 = np.delete(a1, len(a1) - 1, 0)
        a2 = np.delete(a2, 0, 0)
        diff = np.delete(ans2, len(ans2) - 1, 0) + ((a2 - a1) / 2.0)
        df = (a2[0] - a1[0])
        threshold = self.threshold
        point_in = diff[(ans1 / (1.0 * ans1.sum())) > threshold]
        flag = np.zeros((len(tmp_Xwin)), dtype=bool)

        for i, _ in enumerate(point_in):
            flag1 = tmp_Xwin >= (point_in[i] - 0.5 * df)
            flag2 = tmp_Xwin <= (point_in[i] + 0.5 * df)
            flag = np.logical_or(flag, (np.logical_and(flag1, flag2)))

        outlier_index = []
        for i, outlier_flag in enumerate(flag):
            if not outlier_flag:
                outlier_index.append(i)

        if outlier_index:
            return non_nan_idx[list(outlier_index)]

        return None

    def _find_outliers(self, Xclm):
        """
        Parameters:
            Xclm: Pandas Series or single dimensional numpy array.

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
