# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: srom_hotelling_T2
   :synopsis: srom_hotelling_T2.
   
.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

# class need to adjusted yet...
class HotellingT2(BaseEstimator, TransformerMixin):
    """
    HotellingT2
    """

    def __init__(self):
        """ 
            Init method
        """
        self.train_mean = None
        self.train_cov = None
        self.train_num_col = None
        self.train_num_rows = None

    def fit(self, X, y=None):
        """
        Fit estimator.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of \
                shape:(n_samples, n_features) \
                Set of samples, where n_samples is the number of samples \
                and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.
        """
        self.train_num_col = X.shape[1]
        self.train_num_rows = X.shape[0]

        if isinstance(X, pd.DataFrame):
            train = X.values
        else:
            train = X

        self.train_mean = train.mean(0)
        self.train_cov = np.cov(train.T)

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
        if self.train_cov is None or self.train_mean is None:
            raise Exception("You must call fit method")

        if isinstance(X, pd.DataFrame):
            X = X.values

        scores = self.anomaly_score(X)
        return scores

    # sliding window based
    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.

        Paramters:
            X (pandas dataframe or numpy array, required): Input samples.
            
        Returns:
            t2 (numpy.ndarray): Anomaly scores.
        """
        if self.train_num_col != X.shape[1]:
            raise Exception("Column does not match")

        X = pd.DataFrame(X).dropna().values
        n2 = X.shape[0]
        difbar = self.train_mean - X.mean(0)
        v = ((self.train_num_rows - 1) * self.train_cov + ((n2 - 1) * np.cov(X.T))) / (
            self.train_num_rows + n2 - 1.0
        )
        try:
            t2 = (
                self.train_num_rows
                * n2
                * np.dot(np.dot(difbar, np.linalg.inv(v)), difbar)
                / (self.train_num_rows + n2)
            )
        except np.linalg.linalg.LinAlgError as _:
            return None
        return t2

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector.
        """
        return self.anomaly_score(X)
