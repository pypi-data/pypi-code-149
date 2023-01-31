# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: grubbs_checker
   :synopsis: Contains GrubbsTestChecker class.

.. moduleauthor:: SROM Team
"""
from scipy.stats import t
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np


class GrubbsTestChecker(BaseEstimator, ClassifierMixin):
    """
    An example of Grubb Test Checker Comparison.
    """

    def __init__(self, threshold=1):
        """
        Initializing the Grubbs test score.

        Parameters:
            threshold (float, optional): Threshold for checking the test statistics.
        """
        self.train_X = None
        self.grubbs_score = None
        self.z_score = None
        self.threshold = threshold

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
        This should fit classifier for Grubbs test Checker function.
        """
        self.train_X = X
        return self

    def predict(self, X):
        """
        Predict function for classifying anomaly as 1 or 0.
        """
        tmp_z_score, tmp_grubbs_score = self._generate_statistic(X)
        if tmp_z_score is not None and tmp_grubbs_score is not None:
            if tmp_z_score > (self.threshold * tmp_grubbs_score):
                return 1
        return 0

    def _generate_statistic(self, X):

        if self.train_X is None:
            raise RuntimeError("You must fit checker before predicting data!")

        X = X[~np.isnan(np.array(X))]

        if len(X) <= 0:
            self.z_score = None
            self.grubbs_score = None
            return self.z_score, self.grubbs_score

        # converting self.train_X from arrays of arrays to array of ints
        self.tmp_train_X = [i[0] for i in self.train_X]
        tmp_list = np.array(list(self.tmp_train_X) + list(X))
        tmp_list = tmp_list[np.logical_not(np.isnan(np.array(tmp_list)))]

        mean = np.mean(tmp_list)
        std_dev = np.mean(tmp_list)
        x_avg = np.mean(X)
        self.z_score = (x_avg - mean) / std_dev
        len_series = len(tmp_list)

        threshold = t.isf(0.05 / (2 * len_series), len_series - 2)
        threshold_squared = threshold * threshold
        self.grubbs_score = ((len_series - 1) / np.sqrt(len_series)) * np.sqrt(
            threshold_squared / (len_series - 2 + threshold_squared)
        )
        return self.z_score, self.grubbs_score

    def anomaly_score(self, X):
        """
        Return the anomaly value as a score.
        """
        _, tmp_grubbs_score = self._generate_statistic(X)
        return tmp_grubbs_score

    def get_stats(self):
        """
        Return all the statistics generated in the Cost Discrepancy function.
        """
        return {"grubb_test": self.grubbs_score, "z-score": self.z_score}

