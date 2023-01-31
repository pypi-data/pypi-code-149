# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: srom_cusum
   :synopsis: srom_cusum.
   
.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class CUSUM(BaseEstimator, TransformerMixin):
    """
    A cumulative sum based anomaly model.
    """

    def __init__(self, drift=0, threshold=1):
        """
        Parameters:
            drift (Numeric, required): Avoid the detection of a change in absence of an actual change.
            threshold (Numeric, required): Value higher than threshold will become an anomaly flag.
        """
        self.drift = drift
        self.threshold = threshold
        self.alarm_index = None
        self.change_start = None
        self.change_end = None
        self.change_magnitude = None

    def fit(self, X, y=None):
        """
        Fit estimator

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features) \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of CUSUM.
        """
        # reinitialized the variable
        self.alarm_index = None
        self.change_start = None
        self.change_end = None
        self.change_magnitude = None
        return self

    def _apply_cusum(self, X):
        """
        Internal function for apply cusum.
        Parameters:
            X: array-like, shape=(n_columns, n_samples,) training data.
        Return: 
            alarm_index and change_start
        """
        prev_s_hi_list, prev_s_lo_list = np.zeros(X.size), np.zeros(X.size)
        alarm_index, change_start = np.array([[], []], dtype=int)
        p_index, n_index = 0, 0

        # place where we need to find alarm
        for i in range(1, X.size):
            diff_s = X[i] - X[i-1]
            prev_s_hi_list[i] = prev_s_hi_list[i-1] + diff_s - self.drift
            prev_s_lo_list[i] = prev_s_lo_list[i-1] - diff_s - self.drift
            if prev_s_hi_list[i] < 0:
                prev_s_hi_list[i], p_index = 0, i
            if prev_s_lo_list[i] < 0:
                prev_s_lo_list[i], n_index = 0, i
            if prev_s_hi_list[i] > self.threshold or prev_s_lo_list[i] > self.threshold:
                alarm_index = np.append(alarm_index, i)
                change_start = np.append(change_start, p_index if prev_s_hi_list[i] > self.threshold else n_index)  # start
                prev_s_hi_list[i], prev_s_lo_list[i] = 0, 0      # reset alarm

        return alarm_index, change_start

    def _detect_change_interval(self, X):
        """
        Estimation of when the change ends (offline form).
        """
        _, change_start_2 = self._apply_cusum(X[::-1])
        change_end = X.size - change_start_2[::-1] - 1
        self.change_start, ind = np.unique(self.change_start, return_index=True)
        self.alarm_index = self.alarm_index[ind]
        if self.change_start.size != change_end.size:
            if self.change_start.size < change_end.size:
                change_end = change_end[[np.argmax(change_end >= i) for i in self.alarm_index]]
            else:
                ind = [np.argmax(i >= self.alarm_index[::-1])-1 for i in change_end]
                self.alarm_index = self.alarm_index[ind]
                self.change_start = self.change_start[ind]
            # Delete intercalated changes (the ending of the change is after
            # the beginning of the next change)
            ind = change_end[:-1] - self.change_start[1:] > 0
            if ind.any():
                #pylint: disable=invalid-unary-operand-type
                self.alarm_index = self.alarm_index[~np.append(False, ind)]
                self.change_start = self.change_start[~np.append(False, ind)]
                change_end = change_end[~np.append(ind, False)]
            # Amplitude of changes
        amp = X[change_end] - X[self.change_start]
        return change_end, amp

    def predict(self, X):
        """
        Predict anomaly target for X.

        Parameters:
            X (pandas dataframe or numpy array, required): 1 Dimensional Input Samples.

        Returns:
            anomaly_alert_index (numpy.ndarray): Anomaly scores.
        """
        X = np.atleast_1d(X).astype('float64')
        self.alarm_index, self.change_start = self._apply_cusum(X)

        if self.change_start.size:
            self.change_end, self.change_magnitude = self._detect_change_interval(X)

        anomaly_alert_index = np.zeros(X.shape)
        anomaly_alert_index[self.alarm_index] = 1
        return anomaly_alert_index

    def get_information(self):
        """
        Retrieves information about model.

        Returns:
            tuple: (alarm index, change start, change end, change magnitude).
        """
        return self.alarm_index, self.change_start, self.change_end, self.change_magnitude
