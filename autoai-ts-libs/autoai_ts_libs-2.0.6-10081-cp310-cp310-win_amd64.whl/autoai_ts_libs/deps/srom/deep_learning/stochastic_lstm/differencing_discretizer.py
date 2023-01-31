# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import numpy as np

from autoai_ts_libs.deps.srom.feature_engineering.base import DataTransformer


class DifferencingDiscretizerTransformer(DataTransformer):
    def __init__(self, n_bins, col_index, bin_size_expansion=0.1):

        self.bin_size_expansion = bin_size_expansion

        if isinstance(n_bins, (list, np.ndarray)):
            self.n_bins = np.array(n_bins).astype(np.int)
        else:
            self.n_bins = np.array([n_bins] * len(col_index)).astype(np.int)
        self.col_index = col_index

    @staticmethod
    def _guess_bin_size(yhat, k, expansion_factor=0.1):
        """
        Guess a suitable value of bin size by dividing the range of the signal
        into k equal sized bins.
        """
        dyhat = np.diff(yhat, axis=0)
        min_dy = np.min(dyhat, axis=0)
        dy_range = np.ptp(dyhat, axis=0)
        delta_y = dy_range * (1.0 + expansion_factor) / k

        return delta_y, dy_range, min_dy

    @staticmethod
    def _difference_discretizer(yhat, bins):  # delta_y, n_bins):
        """
        Difference and then bin yhat using bins of size delta_y

        yhat (numpy array): data to differnce and bin
        delta_y (float, scalar): size of bins
        n_bins: number of bins

        """

        n_bins = len(bins) - 1
        dyhat = np.diff(yhat, axis=0)
        print("bins: min: {}, max: {}".format(bins[0], bins[-1]))

        # clip out of bound values
        mask = (dyhat < bins[-1]) & (dyhat >= bins[0])

        dyhat_d = np.zeros_like(dyhat)
        dyhat_d[mask] = np.digitize(dyhat[mask], bins) - 1

        if np.sum(dyhat >= bins[-1]) + np.sum(dyhat < bins[0]) > 0:
            print("Clipping values")

        dyhat_d[dyhat >= bins[-1]] = n_bins - 1
        dyhat_d[dyhat < bins[0]] = 0

        return dyhat_d

    def fit(self, X, y=None):

        bins_all = []
        bin_sizes = []
        for col, nb in zip(self.col_index, self.n_bins):
            bin_size, dy_range, min_dy = self._guess_bin_size(
                X[:, col], nb, expansion_factor=self.bin_size_expansion
            )
            # bins = bin_size*np.arange(-nb/2, nb/2+1)
            bins = (
                bin_size * np.arange(nb + 1)
                + min_dy
                - self.bin_size_expansion / 2 * dy_range
            )
            bin_sizes.append(bin_size)
            bins_all.append(bins)

        self.bin_sizes = np.array(bin_sizes)
        self.bins = np.array(bins_all)

        return self

    def transform(self, X, y=None):
        """
        Note that the difference computed is noncausal: d(t) = x(t+1) - x(t).
        Thus, to predict x(t+1) we should predict d(t) = x(t+1) - x(t) and
        add x(t)

        OLD
        Note that the difference computed is causal: d(t) = x(t) - x(t-1).
        Thus, to predict x(t+1) we should predict d(t+1) = x(t+1) - x(t) and
        add x(t)

        """
        # check if fitted

        """
        X_new = 0*np.ones((X.shape[0], len(self.col_index)))
        for i, (col, bins) in enumerate(zip(self.col_index, self.bins)):
            X_new[1:, i] = self._difference_discretizer(X[:, col], bins)
        """

        X_new = np.NaN * np.ones((X.shape[0], len(self.col_index)))
        for i, (col, bins) in enumerate(zip(self.col_index, self.bins)):
            X_new[:-1, i] = self._difference_discretizer(X[:, col], bins)

        return X_new
