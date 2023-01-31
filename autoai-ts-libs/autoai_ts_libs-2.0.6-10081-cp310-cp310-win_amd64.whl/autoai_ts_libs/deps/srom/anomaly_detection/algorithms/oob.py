# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: srom_oob
   :synopsis: srom_oob.
   
.. moduleauthor:: SROM Team
"""

from sklearn.base import BaseEstimator
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble._forest import _generate_unsampled_indices
import pandas as pd
from sklearn.base import clone
from sklearn.preprocessing import MinMaxScaler


class OOB(BaseEstimator):
    """
    Anomaly detection using out-of-box estimators.
    """

    def __init__(
        self,
        base_model=RandomForestRegressor(
            random_state=42,
            oob_score=True,
            n_estimators=10,
            criterion="squared_error",
            max_features=0.333333,
            min_samples_leaf=30,
        ),
        anomaly_threshold=0.3,
    ):
        """
        Parameters:
            base_model (object): Model to be used for anomaly detection.
            anomaly_threshold (number) : Threshold for classifying anomaly.
        """
        self.base_model = base_model
        self.anomaly_threshold = anomaly_threshold

    def _get_per_sample_oob_error(self, feature_index, X, y):
        """
            Internal method work as a helper method.
        """
        X = np.array(X, dtype=np.float32)
        n_samples = y.shape[0]
        predictions = [[] for _ in range(n_samples)]

        for estimator in self._internal_trained_model[feature_index]:
            unsampled_indices = _generate_unsampled_indices(
                estimator.random_state, n_samples, n_samples
            )
            p_estimator = estimator.predict(X[unsampled_indices, :], check_input=False)
            p_estimator = p_estimator[:, np.newaxis]
            for idx, value in enumerate(unsampled_indices):
                predictions[value].append(p_estimator[idx])

        oob_errors = np.array(
            [
                np.sum(((values - y[idx]) ** 2) / len(values))
                for idx, values in enumerate(predictions)
            ]
        )

        return oob_errors

    def fit(self, X, y=None):
        """
        Fit estimator.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of NSA.
        """
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()

        self._internal_trained_model = []
        self._internal_minmax_scaler_error = []
        for i in range(X.shape[1]):
            # build model, one for each i
            f_index = list(range(X.shape[1]))
            f_index.remove(i)
            X_i = X[:, f_index].copy()
            y_i = X[:, i].copy()
            self._internal_trained_model.append(clone(self.base_model))
            self._internal_trained_model[i].fit(X_i, y_i)
            tmp_oob_error = self._get_per_sample_oob_error(i, X_i, y_i)
            tmp_minmax_scaler = MinMaxScaler()
            self._internal_minmax_scaler_error.append(tmp_minmax_scaler)
            self._internal_minmax_scaler_error[i].fit(tmp_oob_error.reshape(-1, 1))
        return self

    def predict(self, X):
        """
        Return wheather given data point is anomaly or not. -1 for anomaly and 1 for non anomaly.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            anomaly values
        """
        tmp_score = self.anomaly_score(X)
        tmp_score[tmp_score > self.anomaly_threshold] = -1
        tmp_score[tmp_score != -1] = 1
        return tmp_score

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """

        # each sample will be scored separately
        X = X.astype(np.float64)

        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()

        results_all_features = []

        for i in range(X.shape[1]):
            # build model, one for each i
            f_index = list(range(X.shape[1]))
            f_index.remove(i)
            X_i = X[:, f_index]
            y_i = X[:, i]
            tmp_oob_error = self._get_per_sample_oob_error(i, X_i, y_i)
            scaled_tmp_oob_error = list(
                self._internal_minmax_scaler_error[i].transform(
                    tmp_oob_error.reshape(-1, 1)
                )
            )
            results_all_features.append(scaled_tmp_oob_error)
        metric_sum = np.array(results_all_features).sum(axis=0) / X.shape[1]
        return metric_sum

    def decision_function(self, X):
        """
        Predict raw anomaly score of X using the fitted detector.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        """
        return self.anomaly_score(X)
