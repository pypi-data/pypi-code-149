# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: cost_discrepancy_checker
   :synopsis: Contains CostDiscrepancyChecker class

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class CostDiscrepancyChecker(BaseEstimator, ClassifierMixin):
    """
    An example of mean based cost detection.
    """

    def __init__(self, threshold=0.05, order=2):
        """
        Initialization for cost discrepency checker.

        Parameters:
            threshold (float, optional): Value to flag anomaly.
            order (int, optional): Order of the cost function, e.g. 2=L2, 1=L1.
        """
        self.train_X = None
        self.threshold = threshold
        self.order = order
        self.cost_desc = None

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

    def set_order(self, order):
        """
        Setter function for order.
        """
        self.order = order

    def get_order(self):
        """
        Getter function for order.
        """
        return self.order

    def fit(self, X):
        """
        This should fit a classifier for change point detection similar to \
        ruptures package window method.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.

        Returns:
            self: Trained instance.
        """
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)
        self.train_X = X
        return self

    def _generate_discrepancy_score(self, X):
        """
        Generate the raw discrepancy scores.
        """
        if self.train_X is None:
            raise RuntimeError("You must train the checker before predicting data!")

        if len(X.shape) == 1:
            X = X.reshape(-1, 1)

        comb_x = np.vstack((self.train_X, X))
        comb_mean = np.mean(comb_x)
        x_mean = np.mean(X)
        train_x_mean = np.mean(self.train_X)

        comb_cost = np.sum(np.abs(comb_x-comb_mean)**self.order)
        x_cost = np.sum(np.abs(X-x_mean)**self.order)
        train_x_cost = np.sum(np.abs(self.train_X-train_x_mean)**self.order)

        self.cost_desc = comb_cost - x_cost - train_x_cost
        return self.cost_desc

    def predict(self, X):
        """
        Predict function for classifying anomaly as 1 or 0.
        """
        if self._generate_discrepancy_score(X) > self.threshold:
            return 1
        return 0

    def anomaly_score(self, X):
        """
        Return the anomaly value as a score.
        """
        self.cost_desc = self._generate_discrepancy_score(X)
        return self.cost_desc

    def get_stats(self):
        """
        Return all the statistics generated in the Cost Discrepancy function.
        """
        return {'cost_desc':self.cost_desc}
