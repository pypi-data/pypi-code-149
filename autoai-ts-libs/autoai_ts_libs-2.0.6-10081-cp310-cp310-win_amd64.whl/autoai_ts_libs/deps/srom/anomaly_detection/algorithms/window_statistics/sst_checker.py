# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: sst_checker
   :synopsis: Contains SSTChecker class.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np


class SSTChecker(BaseEstimator, ClassifierMixin):
    """
    An example of Singular Spectral Transfrom Comparison
    """

    def __init__(self, num_vectors=2, threshold=3):
        """
        Parameters:
            num_vectors (int, optional): number of vectors after applying SVD.
            threshold (float, optional): Threshold for checking the test statistics.
        """
        self.num_vectors = None
        self.train_X = None
        self.change_score = None
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
        Generate the change score.

        Paramters:
            X: matrix like.
        """
        if self.train_X is None:
            raise RuntimeError("You must fit checker before predicting data!")

        tra_U, _, _ = np.linalg.svd(self.train_X, full_matrices=False)
        test_U, _, _ = np.linalg.svd(X, full_matrices=False)
        tra_Um = tra_U[:, : self.num_vectors]
        test_Um = test_U[:, : self.num_vectors]
        s = np.linalg.svd(
            np.dot(tra_Um.T, test_Um), full_matrices=False, compute_uv=False
        )
        self.change_score = 1 - s[0]
        return 1 - s[0]

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
        return {"change_score": self.change_score}

