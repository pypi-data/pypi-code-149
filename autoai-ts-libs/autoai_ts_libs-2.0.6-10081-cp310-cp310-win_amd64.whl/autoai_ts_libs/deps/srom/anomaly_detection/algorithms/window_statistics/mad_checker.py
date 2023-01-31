# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: mad_checker
   :synopsis: Contains MedianAbsoluteDeviationChecker class.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class MedianAbsoluteDeviationChecker(BaseEstimator, ClassifierMixin):
    """
    An example of Median Absolute Deviation Checker Comparison
    """

    def __init__(self, threshold=6):
        """
        Initializing the Median Absolute Deviation checker.

        Parameters:
            threshold (float, optional): Threshold for checking the test statistics.
        """
        self.train_X = None
        self.threshold = threshold
        self.test_statistic = None

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
        tmp_val = self._generate_statistic(X)
        if tmp_val > self.threshold:
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
            self.test_statistic = 0
            return self.test_statistic

        self.train_X = [i[0] for i in self.train_X]
        tmp_list = np.array(list(self.train_X) + list(X))
        tmp_list = tmp_list[~np.isnan(np.array(tmp_list))]
        median = np.median(tmp_list)
        demedianed = np.abs(tmp_list - median)
        median_deviation = np.median(demedianed)

        if median_deviation == 0:
            self.test_statistic = 0
        else:
            self.test_statistic = np.mean(X) / median_deviation

        return self.test_statistic

    def anomaly_score(self, X):
        """
        Predict function for classifying anomaly as 1 or 0.
        """
        tmp_val = self._generate_statistic(X)
        return tmp_val

    def get_stats(self):
        """
        Return all the statistics generated in the Cost Discrepancy function.
        """
        return {'mean_abs_deviation':self.test_statistic}
        
