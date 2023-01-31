# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: srom_robustPCA
   :synopsis: Implementation of Robust PCA based Anomaly/Outlier Detection algorithm.
   
.. moduleauthor:: SROM Team
"""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.preprocessing import StandardScaler
from autoai_ts_libs.deps.srom.preprocessing.robust_pca import RobustPCA


class AnomalyRobustPCA(BaseEstimator):
    """
    Robust PCA based Anomaly
    """

    def __init__(
        self,
        scale=False,
        base_learner=RobustPCA(),
        error_order=1,
        anomaly_threshold=2.0,
    ):
        """
        Parameters:
            scale (boolean, optional): Enable scaling. Defaults to False.
            base_learner (object, optional): Defaults to RobustPCA.
            error_order (integer, optional): Error Calculation : 1=l1, 2=l2 Defaults to 1.
            anomaly_threshold (float, optional): User defined threshold to generate labels. 
                                                Defaults to 2.0.
        """
        self.scale = scale
        self.base_learner = base_learner
        self.error_order = error_order
        self.anomaly_threshold = anomaly_threshold

        self.scaler = None
        self.trainX = None

        self.train_mean = None
        self.train_std = None

    def set_params(self, **kwarg):
        """
        Set the parameters of this estimator.

        Paramters:
            kwargs : Keyword arguments, set of params and its values.
        """
        if "scale" in kwarg:
            self.scale = kwarg["scale"]
        return self

    def fit(self, X, y=None):
        """
        Fit estimator.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of AnomalyRobustPCA.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values
        X = X.astype(np.float64)

        # scaling
        if self.scale:
            self.scaler = StandardScaler()
            X = self.scaler.fit_transform(X)

        # fit pca
        self.base_learner.fit(X)

        # store the training samples
        self.trainX = X

        return self

    def predict(self, X):
        """
        Predicts on given input samples.

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            tmp_score (numpy.ndarray): Predicted data.
        """

        tmp_score = self.anomaly_score(X)
        tmp_score = (tmp_score - self.train_mean) / self.train_std
        tmp_score[abs(tmp_score) < self.anomaly_threshold] = 0
        tmp_score[abs(tmp_score) > 0] = 1
        tmp_score[tmp_score == 1] = -1
        tmp_score[tmp_score == 0] = 1

        return tmp_score

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.

        Returns:
            numpy.ndarray : Anomaly scores.
        
        Raises:
            Exception: When the fit method is not called.
        """
        # Must call fit
        if self.trainX is None:
            raise Exception("Please call fit method first.")

        if isinstance(X, pd.DataFrame):
            X = X.values

        # get the projected space if required
        if self.scale:
            X = self.scaler.transform(X)

        # merge train and test data
        evaluate_X = np.concatenate((self.trainX, X), axis=0)
        evaluate_X = evaluate_X.astype(np.float64)

        tx_X = self.base_learner.transform(evaluate_X)
        attribute_wise_residual_error = evaluate_X - tx_X
        tmp_score = np.sum(
            np.abs(attribute_wise_residual_error) ** self.error_order, axis=1
        )
        self.train_mean = np.mean(tmp_score[: len(tmp_score) - len(X)])
        self.train_std = np.std(tmp_score[: len(tmp_score) - len(X)])
        if self.train_std <= 3.093042293287924e-16:
            self.train_std = 1.0
        return tmp_score[len(tmp_score) - len(X) :]

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector.
        """
        return self.anomaly_score(X)
