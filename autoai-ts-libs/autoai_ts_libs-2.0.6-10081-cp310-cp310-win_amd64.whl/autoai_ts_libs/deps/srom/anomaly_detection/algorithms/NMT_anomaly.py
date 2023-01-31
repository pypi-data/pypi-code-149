# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: NMT_anomaly
   :synopsis: srom_NMT_anomaly.
   
.. moduleauthor:: SROM Team
"""

from sklearn.base import BaseEstimator
from sklearn.neural_network import MLPRegressor
import numpy as np

class NMT_anomaly(BaseEstimator):
    """
    Covariate Prediction Model inputs a time tensor of multi variate
    time series over a window, to predict each variable with
    all other variables, in order to reconstruct the time tensor.
    """

    def __init__(self, feature_columns=None, target_columns=None):
        """init method"""
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """
        Fits the covariate prediction model to store one deep learning
        lstm regressor for each feature column
        Args:
            X: (required) Time tensor of dimension (2 x samples x
                    input_dim x feature_dims)
            y: optional
        Returns: elf
        """

        graph = {}
        for _, item in enumerate(self.target_columns):
            tmp_x_clm = self.target_columns.copy()
            tmp_x_clm.remove(item)
            Xt_ = X[:, tmp_x_clm]
            yt_ = X[:, item].reshape(-1, 1)
            graph[item] = self._covariate_model(Xt_, yt_,)
        self.graph = graph
        return self

    def _covariate_model(self, src, tgt):
        """
        Initializes and fits a deep learning lstm regressor for the
         source(all other features) and target(one feature)
        Args:
            src: TimeTensor of shape (samples x input_dims x
                    feature_columns -1)
            tgt: TimeTensor of shape (samples x input_dims x 1)
        Returns: (regressor, history) where the regressor is the fit
                model, and history is the training history of a
                tensorflow history type
        """
        """
        regressor = DeepLSTMRegressor(
            input_dimension=(self.input_dimension_, self.target_columns_len_ - 1),
            output_dimension=(self.input_dimension_),
            epochs=10,
        )
        """
        regressor = MLPRegressor()
        try:
            from autoai_ts_libs.deps.srom.deep_learning.regressor import DNNRegressor
            regressor = DNNRegressor(input_dimension=(src.shape[1],), output_dimension=1)
        except Exception as e:
            print(e)
            pass
        history = regressor.fit(src, tgt)
        return (regressor, history)

    def predict(self, X):
        """
        Predicts or reconstructs the input using other feature columns
        Args:
            X: TimeTensor of shape (2 x samples x
                    input_dim x feature_dims)
        Returns: y: TimeTensor of shape (samples x
                    input_dim x feature_dims)
        """
        y_ = np.zeros((X.shape[0], len(self.target_columns)))

        for i, item in enumerate(self.target_columns):
            tmp_x_clm = self.target_columns.copy()
            tmp_x_clm.remove(item)
            Xt_ = X[:, tmp_x_clm]
            preds = self.graph[item][0].predict(Xt_)
            if len(preds.shape)>1:
                if preds.shape[1] == 1:
                    preds = preds.reshape(-1)
            y_[:, i] = preds

        Xt = X[:, self.target_columns]
        anomaly_score = ((Xt - y_) ** 2).mean(axis=1)
        return anomaly_score

    def anomaly_score(self, X):
        """
        Get the anomaly score
        Args:
            X: TimeTensor of shape (2 x samples x
                    input_dim x feature_dims)
        Returns: y: TimeTensor of shape (samples x
                    input_dim x feature_dims)
        """
        return self.predict(X)
