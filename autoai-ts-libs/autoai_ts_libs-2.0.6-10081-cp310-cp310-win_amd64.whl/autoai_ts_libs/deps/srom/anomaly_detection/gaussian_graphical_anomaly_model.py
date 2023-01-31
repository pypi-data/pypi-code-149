# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: gaussian_graphical_anomaly_model
   :platform: Python, R
   :synopsis: Gaussian Graphical Model.

.. moduleauthor:: SROM Team
"""

import copy
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing
from sklearn.exceptions import NotFittedError
from sklearn.utils.metaestimators import _BaseComposition
import autoai_ts_libs.deps.srom.utils.distance_metric_utils as dmu
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_graph_lasso import AnomalyGraphLasso
from .anomaly_score_evaluation import AnomalyScoreEvaluator


class GaussianGraphicalModel(_BaseComposition, BaseEstimator, TransformerMixin):
    """
    We use this as a estimators for anomaly detection.

    
    """

    def __init__(
        self,
        base_learner=AnomalyGraphLasso(alpha=0.5),
        distance_metric="KL_Divergence",
        sliding_window_size=50,
        sliding_window_data_cutoff=15,
        scale=True,
    ):
        """
        Parameters:
        base_learner (object,optional): Covariance model instance to be used. Defaults to AnomalyGraphLasso.
        distance_metric (String, optional): Supported values -'KL_Divergence', 'Frobenius_Norm', \
                            'Likelihood', 'Spectral', 'Mahalanobis_Distance'. Defaults to KL_Divergence.
        sliding_window_size (Integer, optional): Should be greater than 0. Defaults to 50.
        sliding_window_data_cutoff (Integer, optional): 0 < sliding_window_data_cutoff < sliding_window_size. \
            Defaults to 15.
        scale (Boolean, optional): True/False. Defaults to True.
        """

        # sliding_window_size > 0
        self.sliding_window_size = sliding_window_size
        # 'KL_Divergence', 'Frobenius_Norm', 'Likelihood', 'Spectral', 'Mahalanobis_Distance'
        self.distance_metric = distance_metric
        # sliding_window_data_cutoff: > 0 and less than self.sliding_window_size
        self.sliding_window_data_cutoff = sliding_window_data_cutoff
        self.base_learner = base_learner
        self.scale = scale

        # internal variables
        self.best_thresholds = None  # ?
        self.model_train = None  # ?
        self.anomaly_scorer = None

        self.mean_train = None
        self.location_ = None
        self.train_sample_cov_ = None
        self.scores = None

    # set param
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

    def fit(self, X, y=None):
        """
        Fit the estimator.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of \
                shape:(n_samples, n_features) \
                Set of samples, where n_samples is the number of samples \
                and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Mix of normal and abnormal data. \
                y is passed in the fit stage, it has to be labelled, label_prefix indicates \
                the prefix of the label column/s. "l" is the default value.

        Returns:
            self: Trained instance of GaussianGraphicalModel.
        """
        # The method which trains the model on normal data set (in most cases).
        # Should have named "train",
        # but continuing with "training" to be consistent with other pipelines
        if self.base_learner is None:
            raise RuntimeError("You must have base learner for training!")

        model_train = copy.deepcopy(self.base_learner)

        if isinstance(X, pd.DataFrame):
            training_data = X.values
            training_data = training_data.astype(float)
        else:
            training_data = X.astype(float)

        # _, n_features = training_data.shape
        self.mean_train = np.mean(training_data, axis=0)
        self.location_ = training_data.mean(0)
        # added for snn (distance function)
        self.train_sample_cov_ = np.cov(training_data.T)
        self.model_train = None

        try:
            if self.scale is True:
                # scaling is done as a default
                model_train.fit(preprocessing.scale(training_data))
            else:
                # no scaling
                model_train.fit(training_data)

            self.model_train = model_train
        except Exception as ex:
            print(str(ex))
            raise Exception("Error while fitting covariance instance.")

        return self

    def predict(self, X):
        """
        Predict anomaly target for X.

        Parameters:
            X (pandas dataframe or numpy array): Input Samples.

        Returns:
            anomaly_scores (numpy.ndarray): `per sample score` or \
                `attribute wise per sample scores`.
        """
        if self.model_train is None:
            raise NotFittedError(
                "This %(name)s instance is not fitted "
                "yet" % {"name": type(self).__name__}
            )

        if isinstance(X, list):
            X = np.array(X)

        test_data = X

        if isinstance(test_data, pd.DataFrame):
            test_data = test_data.values
            test_data = test_data.astype(float)
        else:
            test_data = test_data.astype(float)

        # If sliding window size is -1 or None, the setting corresponds to "outlier analysis"
        if self.sliding_window_size > 0:
            scores = self.attribute_wise_anomaly_score(test_data)
        else:
            scores = self.anomaly_score(test_data)

        if isinstance(scores, pd.DataFrame):
            anomaly_scores = scores.values
            anomaly_scores = anomaly_scores.astype(float)
        else:
            anomaly_scores = scores.astype(float)

        return anomaly_scores

    # calling an internal score method
    def score(self, X, y=None):
        """
        Score function is used for model evaluation.

        Parameters:
            X (pandas dataframe or numpy array): Input Samples.
            y (pandas dataframe or numpy array, optional): Mix of normal and abnormal data.
        Returns:
            numpy.ndarray : Score of given test labels.
        """
        return self._score(self.predict(X), y)

    # score function
    def _score(self, anomaly_scores, test_data_labels):
        """
        Internal function which contains logic for scoring.
        """
        if self.anomaly_scorer:
            self.best_thresholds = None
            anomaly_score = self.anomaly_scorer.score(anomaly_scores, test_data_labels)
            self.best_thresholds = self.anomaly_scorer.get_best_thresholds()
            return anomaly_score
        else:
            raise Exception(
                "You need to call set_scoring to initialize anomaly scorer."
            )

    def get_best_thresholds(self):
        """
        Returns:
            best_thresholds (float): Best thresholds.
        """
        return self.best_thresholds

    def attribute_wise_anomaly_score(self, test_data):
        """
        This method does sliding window based anomaly score calculation.

        Parameters:
            test_data (pandas dataframe or numpy array) : Test data for scoring.

        Returns:
            numpy.ndarray : Attribute wise anomaly scores.
        """
        slide_window = self.sliding_window_size
        n_samples, n_features = test_data.shape
        # if model_train does not have covariance_ and/or precision_ matrix then?
        train_covariance = self.model_train.covariance_
        train_precision = self.model_train.precision_
        train_sample_cov = self.train_sample_cov_
        slide_window = int(slide_window)

        if slide_window > n_samples:
            raise Exception("Sliding Window should be less than the number of samples")
        else:
            n_windows = n_samples - slide_window + 1

        self.scores = np.zeros([n_samples, n_features])
        self.scores[:] = np.NAN  # added a NAN to check
        start_scores = n_samples - n_windows

        for win_index in range(n_windows):
            tmp_X = test_data[win_index : win_index + slide_window, :]
            tmp_X = pd.DataFrame(tmp_X).dropna().values  # remove NULL
            if tmp_X.shape[0] < self.sliding_window_data_cutoff:
                continue

            # mean value of the sample
            tmp_X_location_ = np.mean(tmp_X)

            # create the copy of model
            model_test = copy.deepcopy(self.base_learner)
            try:
                if self.scale is True:
                    # remove preprocessing
                    model_test.fit(preprocessing.scale(tmp_X))
                else:
                    model_test.fit(tmp_X)  # remove preprocessing
            except Exception as ex:
                print(str(ex))
                continue

            test_covariance = model_test.covariance_
            test_precision = model_test.precision_
            score_index = start_scores + win_index
            test_sample_cov = np.cov(tmp_X.T)

            if test_covariance is None or test_precision is None:
                continue

            for i in range(n_features):
                if self.distance_metric == "KL_Divergence":
                    self.scores[score_index, i] = dmu.compute_KL_divergence(
                        train_covariance,
                        train_precision,
                        test_covariance,
                        test_precision,
                        i,
                    )
                elif (
                    self.distance_metric == "Stochastic_Nearest_Neighbors"
                ):  # added for snn
                    self.scores[
                        score_index, i
                    ] = dmu.compute_stochstic_nearest_neighbors(
                        train_covariance,
                        train_precision,
                        test_covariance,
                        test_precision,
                        i,
                        train_sample_cov,
                        test_sample_cov,
                    )  # added for snn
                elif self.distance_metric == "KL_Divergence_Dist":
                    self.scores[
                        score_index, i
                    ] = dmu.compute_KL_divergence_between_distribution(
                        train_covariance,
                        train_precision,
                        test_covariance,
                        test_precision,
                        self.mean_train,
                        np.mean(tmp_X, axis=0),
                    )
                elif self.distance_metric == "Frobenius_Norm":
                    self.scores[score_index, i] = dmu.compute_error_norm(
                        test_covariance, self.model_train.covariance_, norm="frobenius"
                    )
                elif self.distance_metric == "Likelihood":
                    self.scores[score_index, i] = dmu.compute_score(
                        preprocessing.scale(tmp_X),
                        self.model_train.precision_,
                        self.location_,
                    )
                elif self.distance_metric == "Spectral":
                    self.scores[score_index, i] = dmu.compute_error_norm(
                        test_covariance, self.model_train.covariance_, norm="spectral"
                    )
                elif self.distance_metric == "Mahalanobis_Distance":
                    self.scores[score_index, i] = dmu.compute_mahalanobis(
                        tmp_X_location_.reshape(1, -1),
                        self.model_train.precision_,
                        self.location_,
                    )  # last observation in the test dataset for finding the distance
                else:
                    raise NotImplementedError("This distance metric is not implemented")
        return self.scores

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
            scoring_method (String, optional): Scoring method to select from [average, topk]. Defaults to average.
            scoring_metric (String, optional): Scoring metric on of the ['roc_auc', 'anomaly_f1', 'anomaly_acc', 'pr_auc']. \
                                               Defaults to anomaly_f1.
            scoring_topk_param (Integer, optional): positive, > 0 when score_method is 'top-k'. Defaults to 5.
            score_validation (Float, optional): Between 0 and 1. Defaults to 0.5.
        """
        self.anomaly_scorer = AnomalyScoreEvaluator(
            scoring_method, scoring_metric, scoring_topk_param, score_validation
        )

    def anomaly_score(self, test_data):
        """
        Computes the probability score.

        Parameters:
            test_data (pandas dataframe or numpy array): Test data.

        Returns:
            numpy.ndarray: Anomaly scores.
        """
        n_rows, n_features = test_data.shape
        # train_covariance = self.model_train.covariance_
        train_precision = self.model_train.precision_
        if self.scale is True:
            # no effect??to be asked-corrected at this point
            test_data = preprocessing.scale(test_data)
        self.scores = np.zeros([n_rows, n_features])
        self.scores[:] = np.NAN
        y0 = 0.5 * np.log(2.0 * np.pi / np.diag(train_precision))
        for i in range(n_rows):
            self.scores[i, :] = y0 + 0.5 * np.diag(
                np.mat(train_precision)
                * np.mat(test_data[i, :]).T
                * np.mat(test_data[i, :])
                * np.mat(train_precision)
                * np.diag(np.power(1.0 / np.diag(train_precision), 2))
            )

        return self.scores
