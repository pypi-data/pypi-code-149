# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: sliding_window_anomaly_model
   :platform: Python
.. moduleauthor:: SROM Team
"""

import copy
import multiprocessing

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.ensemble import IsolationForest

# from sklearn.utils.metaestimators import _BaseComposition
import numpy as np
import pandas as pd


class SlidingWindowAnomalyModel(BaseEstimator, ClassifierMixin):
    """
    An example of sliding window anomaly class.
    """

    def __init__(
        self,
        base_learner=IsolationForest(),
        train_window_size=100,
        buffer_window_size=7,
        test_window_size=30,
        jump=1,
        min_size=10,
        n_jobs=-1,
        prediction_score=True,
        fit_once=False,
    ):
        """
        Parameters:
        base_learner (object,optional): Base anomaly model with fit and predict/predict_proba \
            method. Defaults to IsolationForest()
        train_window_size (Integer,optional): Size of training data. Defaults to 100.
        buffer_window_size (Integer,optional): Gap between training and testing data, these \
            data will not be used. Defaults to 7.
        test_window_size (Integer,optional): Size of test data (should be less than size of \
            train data). Defaults to 30.
        jump (Integer,optional): Jump number of observation for getting anomaly score from \
            the previously calculated anomaly score. Defaults to 1.
        min_size (Integer,optional): Size of minimum training data. Defaults to 10.
        n_jobs (Integer,optional): Parallelization we want. if value is -1, then infer \
            automatically. Defaults to -1.
        prediction_score (boolean, optional): True/False based on True/False we call predict \
            method or anomaly score method. Default True.
        """
        self.base_learner = base_learner
        self.train_window_size = train_window_size
        self.buffer_window_size = buffer_window_size
        self.test_window_size = test_window_size
        self.jump = jump
        self.min_size = min_size
        self.n_jobs = n_jobs
        self.prediction_score = prediction_score
        self.fit_once = fit_once

        # set the number of jobs
        if self.n_jobs < 0:
            self.n_jobs = multiprocessing.cpu_count()

    def train_and_get_anomaly_score(self, arg):
        """
        Used as a part of parallelization.
        """
        train_start = arg
        train_end = train_start + self.train_window_size
        test_start = train_end + self.buffer_window_size
        test_end = test_start + self.test_window_size

        if self.DataP.ndim > 1:
            train_data = self.DataP[train_start:train_end, :]
            test_data = self.DataP[test_start:test_end, :]
        elif self.DataP.ndim == 1:
            train_data = self.DataP[train_start:train_end].reshape(-1, 1)
            test_data = self.DataP[test_start:test_end].reshape(-1, 1)
        else:
            raise Exception("Error with number of column of Data")

        train_data = pd.DataFrame(train_data).dropna().values
        test_data = pd.DataFrame(test_data).dropna().values

        if (
            len(train_data) == 0
            or len(test_data) == 0
            or len(train_data) < self.min_size
        ):
            return None

        tmp_learner = copy.copy(self.base_learner)
        try:
            if not self.fit_once:
                tmp_learner.fit(train_data)

            score = []
            if self.prediction_score:
                score = tmp_learner.predict(
                    test_data
                )  # either call predict (return 0 ot -1) or
            else:
                if hasattr(self.base_learner, "anomaly_score"):
                    score = tmp_learner.anomaly_score(test_data)
                elif hasattr(self.base_learner, "decision_function"):
                    score = tmp_learner.decision_function(test_data)
                elif hasattr(self.base_learner, "predict_proba"):
                    score = tmp_learner.predict_proba(test_data)
                else:
                    return None
            return np.nanmean(score)
        except Exception:
            pass
        return None

    def fit(self, X, y=None):
        """
        Fit method.

        Parameters:
            X (pandas dataframe or numpy array): Input Samples.
            y (pandas dataframe or numpy array): Input labels.
        """
        if self.base_learner is None:
            raise RuntimeError("You must have model for training!")

        if self.fit_once:
            self.base_learner.fit(X, y)
        # nothing to fit in the SlidingWindowModel
        return self

    def predict(self, X):
        """
        Predict anomaly target for X.

        Parameters:
            X (pandas dataframe or numpy array): Input Samples.

        Returns:
            results : (numpy.ndarray)
                `per sample score` or \
                `attribute wise per sample scores`.
        """
        if self.base_learner is None:
            raise RuntimeError("You must have provided base learner for prediction!")

        if self.prediction_score:
            if not hasattr(self.base_learner, "predict"):
                raise Exception("Base learner does not have predict method")
        else:
            if (
                not hasattr(self.base_learner, "anomaly_score")
                and not hasattr(self.base_learner, "decision_function")
                and not hasattr(self.base_learner, "predict_proba")
            ):
                raise Exception(
                    "Base learner does not have required function for anomaly score"
                )

        from joblib import Parallel, delayed

        self.DataP = X
        arg_instances = list(
            range(
                0,
                len(X)
                - (
                    self.train_window_size
                    + self.buffer_window_size
                    + self.test_window_size
                ),
                self.jump,
            )
        )
        results = Parallel(n_jobs=self.n_jobs, verbose=1, backend="threading")(
            map(delayed(self.train_and_get_anomaly_score), arg_instances)
        )
        for _ in range(
            0,
            self.train_window_size + self.buffer_window_size + self.test_window_size,
            self.jump,
        ):
            results.insert(0, np.NaN)
        return results

    def set_params(self, **kwargs):
        """
        Set the parameters of this estimator.
        
        Parameters:
            kwargs: Keyword arguments, set of params and its values.
        """
        base_learner_params = {}
        for d_item in kwargs:
            if "base_learner__" in d_item:
                base_learner_params[d_item.split("base_learner__")[1]] = kwargs[d_item]
        # sending parameter to base_learner
        self.base_learner.set_params(**base_learner_params)
        return self
