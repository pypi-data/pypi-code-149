# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: gaussianprocess_filter
   :synopsis: GaussianProcessFilter.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np
import pandas as pd
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

class GaussianProcessFilter(BaseEstimator, TransformerMixin):
    """
    Performs outlier detection on time series data \
    using GaussianProcess Filter.
    """

    def __init__(self, columns_to_be_ignored=None, sliding_window_size=10,
                 confidence_threshold=2.3):
        """
        Parameters:
            columns_to_be_ignored: Outlier will not be detected from the \
                column present in this list.
            sliding_window_size: The size of window used for outlier detection.
            confidence_threshold: Confidence threshold used to detect the outlier.
        """
        if columns_to_be_ignored:
            self.columns_to_be_ignored = columns_to_be_ignored
        else:
            self.columns_to_be_ignored = []
        self.sliding_window_size = sliding_window_size
        self.confidence_threshold = confidence_threshold

    def set_params(self, **kwarg):
        """
        Used to set params.
        """
        if 'columns_to_be_ignored' in kwarg:
            self.columns_to_be_ignored = kwarg['columns_to_be_ignored']
        if 'sliding_window_size' in kwarg:
            self.sliding_window_size = kwarg['sliding_window_size']
        if 'confidence_threshold' in kwarg:
            self.confidence_threshold = kwarg['confidence_threshold']

    # an internal method - evaluate wether the observation is outlier
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

        #TODO : raise error len(tmp_Xwin) == 0
        if not tmp_Xwin:
            return None

        time_x = np.arange(0, len(tmp_Xwin), 1)
        X = np.atleast_2d(time_x).T
        y = np.atleast_2d(tmp_Xwin).T
        x_pred = np.atleast_2d(np.linspace(X.min(), X.max(), len(tmp_Xwin))).T
        rw_kernel = 0.64**2 * RBF(length_scale=0.365) + WhiteKernel(noise_level=0.29)
        gp = GaussianProcessRegressor(kernel=rw_kernel)
        gp.fit(X, y)
        y_pred, sigma = gp.predict(x_pred, return_std=True)
        if y_pred.ndim == 1:
            y_pred = y_pred.reshape(-1,1)
        confidence_interval = self.confidence_threshold * sigma

        tmp_Xwin = list(tmp_Xwin)
        y_pred = list(np.concatenate(y_pred, axis=0))
        confidence_interval = list(confidence_interval)

        outlier_index = []
        for i, _ in enumerate(confidence_interval):
            num1 = (y_pred[i] - confidence_interval[i])
            num2 = (y_pred[i] + confidence_interval[i])
            min_num = num1
            max_num = num2
            if min_num > num2:
                min_num = num2
            if max_num < num1:
                max_num = num1

            if ((tmp_Xwin[i]) >= min_num) and ((tmp_Xwin[i]) <= max_num):
                pass
            else:
                outlier_index.append(i)
        return non_nan_idx[outlier_index]

    def _find_outliers(self, Xclm):
        """
        Parameters:
            Xclm: Pandas Series or single dimensional numpy array.
        
        Returns:
            Position at which outliers are observed for \
            input column Xclm.
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

        Fits transformer to X and y and returns a transformed version of X

        Parameters:
            X: Training set(Pandas dataframe or numpy ndarray).
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
            Exception: If number of samples in X is less than sliding_window_sizes. \
                If training set is not either pandas dataframe or numpy ndarray.
        """
        return self._transform(X)
