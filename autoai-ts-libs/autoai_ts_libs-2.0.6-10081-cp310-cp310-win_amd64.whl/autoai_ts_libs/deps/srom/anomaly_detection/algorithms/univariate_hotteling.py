# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: UnivariateHotteling
   :synopsis: UnivariateHotteling.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from scipy import stats


class UnivariateHotteling(BaseEstimator, TransformerMixin):
    """
    Univariate Anomaly Detection Model based on Hotteling.

    """

    def __init__(self, threshold):
        """
            Parameters:
                threshold: Threshold for percent of the distribution for normal
        """
        self.threshold = threshold
        self.avg = None
        self.var = None
        self.anomaly_score_threshold = None

    def fit(self, X, y=None):
        """
        Fit the model with the provided data.

        Parameters:
            X (pandas dataframe or numpy array, required): Univariate data \
                shape:(n_samples, ) \
                Set of samples, where n_samples is the number of samples \
        """
        # checking if univariate data
        if len(X.shape)> 1 and X.shape[1]>1:
            raise TypeError('Number of columns in the data should be less than 1.')

        if not isinstance(X, np.ndarray):
            X = np.array(X)

        self.anomaly_score_threshold = stats.chi2.interval(1 - self.threshold, 1)[1]
        self.avg = np.average(X)
        self.var = np.var(X)

        return self

    def predict(self, X):
        """
        Calls anomaly_score() which returns anomaly scores.

        Paramters:
            X (pandas dataframe or numpy array, required): Input Samples.
            
        Returns:
            scores (numpy.ndarray): Anomaly scores.

        Raises:
            Exception : When instance is not trained.
        """
        if self.avg is None or self.var is None:
            raise Exception("You must call fit method")
        
        scores = self.anomaly_score(X)
        result = []
        for (_, x) in enumerate(scores):
            if x > self.anomaly_score_threshold:
                result.append(1)
            elif np.isnan(x):
                result.append(x)
            else:
                result.append(0)
        return np.array(result)

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.

        Paramters:
            X (pandas dataframe or numpy array, required): Input samples.
            
        Returns:
            normalized score (numpy.ndarray): Anomaly scores.
        """
        if self.avg is None or self.var is None:
            raise Exception("You must call fit method")

        if isinstance(X, pd.DataFrame):
            X = X.values
        elif not isinstance(X, np.ndarray):
            X = np.array(X)
        else:
            pass

        # checking if univariate data
        if len(X.shape)> 1 and X.shape[1]>1:
            raise TypeError('Number of columns in the data should be less than 1.')

        return [(x - self.avg) ** 2 / self.var for x in X]

    def decision_function(self, X):
        """
        Predict raw anomaly score of X using the fitted detector.

        """
        return self.anomaly_score(X)
