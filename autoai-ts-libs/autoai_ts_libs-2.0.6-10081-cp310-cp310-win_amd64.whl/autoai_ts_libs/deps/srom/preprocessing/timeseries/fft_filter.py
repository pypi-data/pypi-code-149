# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: fft_filter
   :synopsis: FFTFilter.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from numpy.fft import fft, ifft
import pandas as pd
from sklearn.preprocessing import StandardScaler

class FFTFilter(BaseEstimator, TransformerMixin):
    """
    Performs outlier detection on time series \
    data using FFT.
    """

    def __init__(self, columns_to_be_ignored=None, sliding_window_size=10,
                 max_frequency_component=1, scale=False):
        """
        Parameters:
            columns_to_be_ignored: Outlier will not be detected from the \
                column present in this list.
            sliding_window_size: The size of window used for outlier detection.
            max_frequency_component: Number of fft components that will be removed.
            scale: True or False, apply StandardScaler.
        """
        if columns_to_be_ignored:
            self.columns_to_be_ignored = columns_to_be_ignored
        else:
            self.columns_to_be_ignored = []
        self.sliding_window_size = sliding_window_size
        self.max_frequency_component = max_frequency_component
        self.scale = scale

    def set_params(self, **kwarg):
        """
        Set parameters for the function.
        """
        if 'columns_to_be_ignored' in kwarg:
            self.columns_to_be_ignored = kwarg['columns_to_be_ignored']
        if 'sliding_window_size' in kwarg:
            self.sliding_window_size = kwarg['sliding_window_size']
        if 'max_frequency_component' in kwarg:
            self.max_frequency_component = kwarg['max_frequency_component']
        if 'scale' in kwarg:
            self.scale = kwarg['scale']

    def _find_outlier_index_in_window(self, Xwin):
        """
        Parameters:
            Xwin: Pandas Series or single dimensional numpy array.

        Returns:
            None or a list of integer value between 0 to len(Xwin).
        """
        if self.max_frequency_component <= 0:
            return None

        non_nan_idx = []
        tmp_Xwin = []

        for i, val in enumerate(Xwin):
            if not np.isnan(val):
                non_nan_idx.append(i)
                tmp_Xwin.append(val)
        non_nan_idx = np.array(non_nan_idx)

        if not tmp_Xwin or np.std(tmp_Xwin) == 0:
            return None

        if self.scale:
            tmp_Xwin = list(StandardScaler().fit_transform(np.array(tmp_Xwin).reshape(-1, 1)))

        # find the value of fft energy that need to be removed
        fft_tmp_Xwin = fft(tmp_Xwin)

        bVal = np.zeros(len(fft_tmp_Xwin))
        for i, _ in enumerate(fft_tmp_Xwin):
            bVal[i] = fft_tmp_Xwin[i].real
        bVal = sorted(np.abs(bVal))
        bValmax = bVal[0]
        if self.max_frequency_component < len(bVal):
            bValmax = bVal[-self.max_frequency_component]

        # reinitialized the fft component
        for i, _ in enumerate(fft_tmp_Xwin):
            if np.abs(fft_tmp_Xwin[i].real) >= bValmax:
                fft_tmp_Xwin[i] = 0

        # apply the inverse fft
        filtered_signal = list(ifft(fft_tmp_Xwin))
        bVal = np.zeros(len(filtered_signal))
        for i, _ in enumerate(filtered_signal):
            bVal[i] = filtered_signal[i].real

        # find the value that is outliers
        outlier_index = np.where(np.abs(tmp_Xwin) > np.max(np.abs(bVal)))[0]
        return non_nan_idx[outlier_index]

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
