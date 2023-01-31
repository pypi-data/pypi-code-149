# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: generalized_anomaly_model
   :platform: Python
.. moduleauthor:: SROM Team
"""

from inspect import getfullargspec
import math

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.ensemble import IsolationForest
from sklearn.utils.metaestimators import _BaseComposition

import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.anomaly_detection.anomaly_score_evaluation import AnomalyScoreEvaluator


class GeneralizedAnomalyModel(_BaseComposition, BaseEstimator, ClassifierMixin):
    """ 
    An example of generalized anomaly class.

    """

    def __init__(
        self,
        base_learner=IsolationForest(),
        fit_function="fit",
        predict_function="predict",
        score_sign=-1,
    ):
        """
        Parameters:
        base_learner (object,optional): Base learning model instance to be used. \
            Defaults to IsolationForest.
        fit_function (String, optional): Fit function to be used while training. \
            Defaults to 'fit'.
        predict_function (String, optional): Predict function to be used while prediction. \
            Defaults to 'predict'.
        score_sign (Integer, optional): 1 or -1. Defaults to -1.
        """

        self.base_learner = base_learner
        self.fit_function = fit_function
        self.predict_function = predict_function
        self.score_sign = score_sign

        # internal method
        self.best_score = None
        self.anomaly_scorer = None
        self.best_thresholds = None

    def fit(self, X, y=None):
        """
        Fit the model.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of \
                shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples \
                and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Mix of normal and abnormal data. \
                Defaults to None.

        Returns:
            self: Trained instance of GeneralizedAnomalyModel.

        Raises:
            RuntimeError : When base_learner is None.
        """
        if self.base_learner is None:
            raise RuntimeError("You must have model for training!")
        self.location_ = np.mean(X, axis=0)
        sig = getfullargspec(self.base_learner.__getattribute__(self.fit_function))
        if "X" in sig.args and "y" in sig.args:
            self.base_learner.__getattribute__(self.fit_function)(X, y)
        elif "X" in sig.args:
            self.base_learner.__getattribute__(self.fit_function)(X)
        else:
            raise Exception("Fit error: check the method name of fit")
        return self

    def predict(self, X, y=None):
        """

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
            y (pandas dataframe or numpy array, optional): Mix of normal and abnormal data. \
                Defaults to None.
        Returns:
            numpy.ndarray

        Raises:
            RuntimeError: when base_learner is None.
        """
        if self.base_learner is None:
            raise RuntimeError("You must have trained base learner for prediction!")
        if isinstance(X, list):
            X = np.array(X)
        anomaly_scores = self.anomaly_score(X, y)
        anomaly_scores = pd.DataFrame(anomaly_scores)
        anomaly_scores = anomaly_scores
        return anomaly_scores.values

    def anomaly_score(self, X, y=None):
        """

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
            y (pandas dataframe or numpy array, optional): Mix of normal and abnormal data. \
                Defaults to None.
        Returns:
            numpy.ndarray
        """
        is_result = np.ones(X.shape[0], dtype=float)
        is_result.fill(np.nan)
        sig = None

        if self.predict_function in dir(self.base_learner):
            sig = getfullargspec(
                self.base_learner.__getattribute__(self.predict_function)
            )

        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)

        # improved version - in python avoid loop as much as you can
        copy_X = X.copy().reset_index(drop=True)
        copy_X = copy_X.dropna()

        ret_res = None
        if copy_X.shape[0] > 0:
            if sig is not None and "X" in sig.args and "y" in sig.args:
                ret_res = self.base_learner.__getattribute__(self.predict_function)(
                    copy_X.values, y
                )
            elif sig is not None and ("X" in sig.args or "observations" in sig.args):
                ret_res = self.base_learner.__getattribute__(self.predict_function)(
                    copy_X.values
                )
            elif self.predict_function == "srom_log_liklihood":
                ret_res = self.srom_log_liklihood(copy_X.values)
            else:
                pass
            if "ret_res" in dir():
                if (ret_res is not None) and (ret_res.ndim > 1):
                    ret_res = ret_res[:, 0]
                is_result[copy_X.index] = ret_res
        else:
            pass

        return is_result * self.score_sign

    def set_params(self, **kwargs):
        """
        Set the parameters of this estimator.

        Parameters:
            kwargs : Keyword arguments, set of params and its values.
        """
        base_learner_params = {}
        for d_item in kwargs:
            if "base_learner__" in d_item:
                base_learner_params[d_item.split("base_learner__")[1]] = kwargs[d_item]
        # sending parameter to base_learner
        self.base_learner.set_params(**base_learner_params)
        return self

    def srom_log_liklihood(self, X):
        """
        Internal method for log likelihood.
        """
        if not hasattr(self.base_learner, "covariance_") or not hasattr(
            self.base_learner, "precision_"
        ):
            raise AttributeError(
                "Either covariance or precision is not present in base_learner. \
                                 Try some other base_learner."
            )

        part1 = math.log(np.linalg.det(self.base_learner.covariance_))
        location = self.location_
        if isinstance(self.location_, np.ndarray):
            location = pd.DataFrame(self.location_)
        part12 = X - location.values
        part12_T = np.transpose(part12)
        partm = np.dot(np.dot(part12, self.base_learner.precision_), part12_T)
        part2 = X.shape[1] * math.log(2 * math.pi)
        score_value = (-0.5) * (part1 + part2 + partm)
        return score_value

    def score(self, X, y):
        """
        Score function is used for model evaluation.

        Parameters:
            X (pandas dataframe or numpy array): Input Samples.
            y (pandas dataframe or numpy array, optional): Mix of normal and abnormal data.

        Returns:
            numpy.ndarray: Score of given test labels.
        """
        return self._score(self.predict(X), y)

    def set_scoring(
        self,
        scoring_method="average",
        scoring_metric="anomaly_f1",
        scoring_topk_param=5,
        score_validation=0.5,
    ):
        """
        Method to set scoring related configurations.

        Parameters:
            scoring_method (String, optional): Scoring method to select from [average, topk]. \
                Defaults to average.
            scoring_metric (String, optional): Scoring metric on of the ['roc_auc', 'anomaly_f1', \
                'anomaly_acc', 'pr_auc']. Defaults to anomaly_f1.
            scoring_topk_param (Integer, optional): positive, > 0 when score_method is 'top-k'. \
                Defaults to 5.
            score_validation (Float, optional): between 0 and 1. Defaults to 0.5.
        """
        self.anomaly_scorer = AnomalyScoreEvaluator(
            scoring_method, scoring_metric, scoring_topk_param, score_validation
        )

    def _score(self, anomaly_scores, test_data_labels):
        """
        Internal function which contains logic for scoring.
        """
        self.best_score = None
        self.best_thresholds = None
        if self.anomaly_scorer:
            self.best_score = self.anomaly_scorer.score(
                anomaly_scores, test_data_labels
            )
            self.best_thresholds = self.anomaly_scorer.get_best_thresholds()
            return self.best_score
        else:
            raise Exception(
                "You need to call set_scoring to initialize anomaly scorer."
            )

    # best score method (do not know what is importance)
    def get_best_score(self):
        """
        Return the score corresponding to the best performing pipeline.

        Returns:
            float: Best score.
        """
        return self.best_score

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector."""
        return self.anomaly_score(X, None)
