""" Test ReconstructAD """
import unittest

import numpy as np
from autoai_ts_libs.deps.srom.deep_learning.anomaly_detector import CNNAutoEncoder
from autoai_ts_libs.deps.srom.time_series.pipeline import ReconstructAD


class TestReconstructAD(unittest.TestCase):
    """class for testing ReconstructAD"""

    @classmethod
    def setUp(cls):
        x = np.arange(99)
        x = x.reshape(1, -1, 3)
        cls.X = x
        cls.feature_columns = [0,1,2]
        cls.target_columns = [0,1,2]
        cls.lookback_win = 5
        cls.pred_win = 1

    def test_fit(self):
        """method for testing the fit method of ReconstructAD"""
        test_class = self.__class__
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        self.assertEqual(fitted_model, model)

    def test_predict_anomaly_score(self):
        """method for testing the score method of ReconstructAD with batch prediction type and with iid scoring method"""
        test_class = self.__class__
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X, test_class.X)
        score = fitted_model.anomaly_score(test_class.X)
        pred_x = fitted_model.predict(test_class.X)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        prediction_type='batch'
        pred_x = fitted_model.predict(test_class.X, prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_anomaly_score_context(self):
        """method for testing the score method of ReconstructAD with contextual-Anomaly scoring method and batch prediction type"""
        test_class = self.__class__
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X, test_class.X)
        score = fitted_model.anomaly_score(test_class.X)
        pred_x = fitted_model.predict(test_class.X)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        prediction_type='batch'
        pred_x = fitted_model.predict(test_class.X, prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_anomaly_score_context_with_none_x(self):
        """method for testing the score method of ReconstructAD with none x"""
        test_class = self.__class__
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X, test_class.X)
        score = fitted_model.anomaly_score(None)
        #pred_x = fitted_model.predict(test_class.X)
        #self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        prediction_type='batch'
        pred_x = fitted_model.predict(None, prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_anomaly_score_sliding(self):
        """method for testing the score method of ReconstructAD with sliding-window scoring method and batch prediction type"""
        test_class = self.__class__
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X, test_class.X)
        score = fitted_model.anomaly_score(test_class.X)
        pred_x = fitted_model.predict(test_class.X)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        prediction_type='batch'
        pred_x = fitted_model.predict(test_class.X, prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_anomaly_score_sliding_with_none_x(self):
        """method for testing the score method of ReconstructAD with none x"""
        test_class = self.__class__
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X, test_class.X)
        score = fitted_model.anomaly_score(None)
        #pred_x = fitted_model.predict(test_class.X)
        #self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        prediction_type='batch'
        pred_x = fitted_model.predict(None, prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

        
    def test_predict_sliding_and_anomaly_scores(self):
        """method for testing the score method of ReconstructAD with iid scoring method and sliding prediction type"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="sliding"
        pred_x_sliding = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_sliding)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_sliding_and_anomaly_scores_context(self):
        """method for testing the score method of ReconstructAD with contextual-anomaly scoring method and sliding prediction type"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="sliding"
        pred_x_sliding = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_sliding)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_sliding_and_anomaly_scores_sliding(self):
        """method for testing the score method of ReconstructAD with sliding-window scoring method and sliding prediction type"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="sliding"
        pred_x_sliding = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_sliding)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score(self):
        """method for testing the score method of ReconstructAD with iid scoring method and recent prediction type"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score_wtih_none_x(self):
        """method for testing the score method of ReconstructAD with iid scoring method and recent prediction type"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="iid",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(None,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(None)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score_context(self):
        """method for testing the score method of ReconstructAD with contextual-anomaly scoring method and recent prediction type"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score_context_with_none_x(self):
        """method for testing the score method of ReconstructAD with none x"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Contextual-Anomaly",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(None,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(None)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score_sliding(self):
        """method for testing the score method of ReconstructAD with sliding-window scoring method and recent prediction type"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(test_class.X,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)

    def test_predict_recent_and_anomaly_score_sliding_with_none_x(self):
        """method for testing the score method of ReconstructAD with none x"""
        test_class = self.__class__
        # Test Multivariate
        model = ReconstructAD(
            steps=[
                (
                    "CNN_AutoEncoder",
                    CNNAutoEncoder(
                        input_dimension=(20, 2)
                    ),
                )
            ],
            lookback_win=5,
            target_columns=[0,1,2],
            scoring_method="Sliding-Window",
        )
        fitted_model = model.fit(test_class.X)
        prediction_type="recent"
        pred_x_recent = fitted_model.predict(None,prediction_type)
        self.assertIsNotNone(pred_x_recent)
        score = fitted_model.anomaly_score(None)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Chi-Square', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Q-Score', scoring_threshold=10)
        post_process_score,threshold=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        fitted_model.set_anomaly_scoring_params(scoring_method='Contextual-Anomaly', scoring_threshold=10)
        post_process_score=fitted_model._post_process_anomaly(score, return_threshold=True)
        self.assertIsNotNone(post_process_score)
        
if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
