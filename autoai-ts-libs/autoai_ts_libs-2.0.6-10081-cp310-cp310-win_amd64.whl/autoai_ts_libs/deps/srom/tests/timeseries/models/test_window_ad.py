""" Test WindowAD """
import unittest

import numpy as np
from sklearn.covariance import MinCovDet
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_robust_pca import AnomalyRobustPCA
from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
from autoai_ts_libs.deps.srom.time_series.pipeline import WindowAD


class TestWindowAD(unittest.TestCase):
    """class for testing WindowAD"""

    @classmethod
    def setUp(cls):
        x = np.arange(100)
        x = x.reshape(-1, 1)
        cls.target_columns = [0]
        cls.X = x
        cls.feature_columns = [0]
        cls.target_columns = [0]
        cls.lookback_win = 5
        cls.pred_win = 1

    def test_fit(self):
        """method for testing the fit method of PredAD"""
        test_class = self.__class__
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        self.assertEqual(fitted_model, model)

    def test_predict_and_anomaly_scores(self):
        """method for testing the predict method of PredAD"""
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        pred_x = fitted_model.predict(test_class.X)
        score = fitted_model.anomaly_score(test_class.X)
#       Checking for predict in batch
        prediction_type='batch'
        pred_x = fitted_model.predict(test_class.X, prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_and_anomaly_scores_context(self):
        """method for testing the predict method of PredAD"""
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X)
        pred_x = fitted_model.predict(test_class.X)
        score = fitted_model.anomaly_score(test_class.X)
#       Checking for predict in batch
        prediction_type='batch'
        pred_x = fitted_model.predict(test_class.X, prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_sliding_and_anomaly_scores(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="sliding"
        pred_x_sliding = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_sliding)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_sliding_and_anomaly_scores_context(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="sliding"
        pred_x_sliding = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_sliding)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score_sliding(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_batch_and_anomaly_score_sliding(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="batch"
        pred_x_recent = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_batch_and_anomaly_score_sliding_with_none_x(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="batch"
        pred_x_recent = fitted_model.predict(None,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(None)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_sliding_and_anomaly_score_sliding(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="sliding"
        pred_x_recent = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_training_and_anomaly_score_sliding(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="training"
        pred_x_recent = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_training_and_anomaly_score_sliding_with_none_x(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="training"
        pred_x_recent = fitted_model.predict(None,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(None)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score_with_none_x(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(None,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(None)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_training_and_anomaly_scores(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="training"
        pred_x_training = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_training)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score =fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_training_and_anomaly_scores_context(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="training"
        pred_x_training = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_training)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score =fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_training_and_anomaly_scores_with_none_x(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="training"
        pred_x_training = fitted_model.predict(None,prediction_type)
        self.assertIsNotNone(pred_x_training)
        score = fitted_model.anomaly_score(None)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score, threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score =fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_training_and_anomaly_scores_idd_false_threshold(self):
        test_class = self.__class__
        # Test Multivariate
        model = WindowAD(
            steps=[
                (
                    "anomaly_robust_pca",
                    GeneralizedAnomalyModel(
                        base_learner=AnomalyRobustPCA(),
                        predict_function="anomaly_score",
                        score_sign=1,
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="training"
        pred_x_training = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_training)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=False)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=False)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=False)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=False)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=False)
        self.assertIsNotNone(post_process_score)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
