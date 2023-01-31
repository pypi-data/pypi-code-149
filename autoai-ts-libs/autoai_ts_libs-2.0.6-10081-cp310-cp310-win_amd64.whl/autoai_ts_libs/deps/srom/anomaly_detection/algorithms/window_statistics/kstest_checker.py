# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: kstest_checker
   :synopsis: Contains KSTestChecker class.

.. moduleauthor:: SROM Team
"""
from scipy.stats import ks_2samp
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np
#from sm.tsa.stattools import adfuller

class KSTestChecker(BaseEstimator, ClassifierMixin):
    """
    An example of Kolgo Test Checker Comparison.
    """

    def __init__(self, threshold=1):
        """
        Initializing the KS test checker.

        Parameters:
            threshold (float, optional): Threshold for checking the test statistics.
        """
        self.train_X = None
        self.threshold = threshold
        self.ks_d = None
        self.ks_p_value = None

    def set_threshold(self, threshold):
        """
        Setter function for threshold.
        """
        self.threshold = threshold

    def get_threshold(self):
        """
        Getter function for threshold.
        """
        return self.threshold

    def fit(self, X):
        """
        This should fit classifier for TTestChecker function.
        """
        self.train_X = X
        return self

    def predict(self, X):
        """
        Predict function for classifying anomaly as 1 or 0.
        """
        tmp_z_score = self._generate_statistic(X)
        if tmp_z_score >= 1:
            return 1
        return 0

    def _generate_statistic(self, X):
        """
        Generate the raw scores.
        """
        if self.train_X is None:
            raise RuntimeError("You must fit checker before predicting data!")

        X = X[~np.isnan(np.array(X))]
        if len(X) <= 0:
            return 0

        tmp_list = np.array(list(self.train_X))
        tmp_list = tmp_list[~np.isnan(np.array(tmp_list))]

        if len(tmp_list) < 2 or len(X) < 2:
            return 0

        self.ks_d, self.ks_p_value = ks_2samp(tmp_list, X)
        if self.ks_p_value < 0.05 and self.ks_d > 0.5:
            return 1
            '''
            # pending
            adf = sm.tsa.stattools.adfuller(tmp_list, 10)
            if adf[1] < 0.05:
                return 1
            '''
        return 0

    def anomaly_score(self, X):
        """
        Predict function for classifying anomaly as 1 or 0.
        """
        self._generate_statistic(X)
        return self.ks_d

    def get_stats(self):
        """
        Return all the statistics generated in the Cost Discrepancy function.
        """
        return {'ks_d':self.ks_d, 'ks_p_value':self.ks_p_value}
