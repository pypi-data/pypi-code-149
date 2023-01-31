# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: grubbstest_filter
   :synopsis: Grubb Test Filter
        external dependency on https://pypi.org/project/outlier_utils/

.. moduleauthor:: SROM Team
"""

from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from outliers import smirnov_grubbs as grubbs


class GrubbsTestFilter(BaseEstimator, TransformerMixin):
    """
    Performs outlier detection on time series data using Grubbs Test.
    """

    def __init__(
        self,
        columns_to_be_ignored=None,
        sliding_window_size=10,
        test_type="two-sided",
        alpha=0.05,
    ):
        """
        Parameters:
            columns_to_be_ignored: Outlier will not be detected from the \
                column present in this list.
            sliding_window_size: The size of window used for outlier detection.
            test_type: One sided or two sided, if one sided then min or max: two-sided, \
                one-sided-min, one-sided-max.
            alpha: Significance value.
        """
        if columns_to_be_ignored:
            self.columns_to_be_ignored = columns_to_be_ignored
        else:
            self.columns_to_be_ignored = []
        self.sliding_window_size = sliding_window_size
        self.test_type = test_type
        self.alpha = alpha

    def set_params(self, **kwarg):
        """
        Used to set params.
        """
        if "columns_to_be_ignored" in kwarg:
            self.columns_to_be_ignored = kwarg["columns_to_be_ignored"]
        if "sliding_window_size" in kwarg:
            self.sliding_window_size = kwarg["sliding_window_size"]
        if "test_type" in kwarg:
            self.test_type = kwarg["test_type"]
        if "alpha" in kwarg:
            self.alpha = kwarg["alpha"]

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

        outlier_index = []
        if self.test_type == "two-sided":
            outlier_index = grubbs.two_sided_test_indices(tmp_Xwin, self.alpha)
        elif self.test_type == "one-sided-min":
            outlier_index = grubbs.min_test_indices(tmp_Xwin, self.alpha)
        elif self.test_type == "one-sided-max":
            outlier_index = grubbs.max_test_indices(tmp_Xwin, self.alpha)
        else:
            raise Exception("Test type is not supported")

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
            idx = self._find_outlier_index_in_window(Xclm[k - win : k + win])
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
                raise Exception( 
                    "Sliding Window should be less than the number of samples"
                )
            outlier_mask = np.empty(X.shape)
            outlier_mask.fill(False)
            columns = X.columns
            for i, column in enumerate(columns):
                if column not in self.columns_to_be_ignored:
                    outlier_index = self._find_outliers(X[column])
                    outlier_mask[outlier_index, i] = True
            return outlier_mask
        else:
            raise Exception(
                "Training set must be either pandas dataframe or numpy ndarray."
            )

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
            array of outlier Flag, with length = number of elements in X.

        Raises:
            Exception: If number of samples in X is less than sliding_window_size. \
                If training set is not either pandas dataframe or numpy ndarray.
        """
        return self._transform(X)
