# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: zscore_checker
   :synopsis: Contains ZscoreChecker class.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np


class ZscoreChecker(BaseEstimator, ClassifierMixin):
    """
    An example of Median Absolute Deviation Checker Comparison
    """

    def __init__(self, threshold=3):
        """
        Parameters:
            threshold (float, optional): Threshold for checking the test statistics.
        """
        self.train_X = None
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
        This should fit classifier for TTestChecker function.
        """
        self.train_X = X
        return self

    def predict(self, X):
        """
        Predict function for classifying anomaly as 1 or 0.
        """
        tmp_z_score = self._generate_statistic(X)
        if tmp_z_score > self.threshold:
            return 1
        return 0

    def _generate_statistic(self, X):
        """
        Generate the raw z-scores.

        Paramters:
            X: matrix like.
        """
        if self.train_X is None:
            raise RuntimeError("You must fit checker before predicting data!")

        X = X[~np.isnan(np.array(X))]
        if len(X) <= 0:
            self.z_score = None
            return self.z_score

        self.tmp_train_X = [i[0] for i in self.train_X]
        tmp_list = np.array(list(self.tmp_train_X) + list(X))
        tmp_list = tmp_list[~np.isnan(np.array(tmp_list))]
        mean = np.mean(tmp_list)
        std_dev = np.std(tmp_list)
        x_avg = np.mean(X)
        self.z_score = (x_avg - mean) / std_dev
        return self.z_score

    def anomaly_score(self, X):
        """
        Return the anomaly value as a score.
        """
        tmp_z_score = self._generate_statistic(X)
        return tmp_z_score

    def get_stats(self):
        """
        Return all the statistics generated in the Cost Discrepancy function.
        """
        return {"z_score": self.z_score}

