""" Test PredAD """
import unittest

import numpy as np
from sklearn.linear_model import LinearRegression
from autoai_ts_libs.deps.srom.preprocessing.transformer import Log
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.time_series.pipeline import PredAD
from sklearn.pipeline import FeatureUnion
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import NormalizedFlattenX


class TestPredAD(unittest.TestCase):
    """class for testing PredAD"""

    @classmethod
    def setUp(cls):
        x = np.arange(100)
        cls.target_columns = [0]
        cls.X = x.reshape(-1, 2)
        log = Log()
        tt = NormalizedFlattenX(feature_columns=[0, 1], target_columns=[0])
        flatten = Flatten()
        lr = LinearRegression()
        featun = FeatureUnion([("log", log)])
        cls.steps = [
            ("featun", featun),
            ("flatten", flatten),
            ("targettransformer", tt),
            ("lr", lr),
        ]
        cls.feature_columns = [0, 1]
        cls.target_columns = [0]
        cls.lookback_win = 5
        cls.observation_window=10
        cls.pred_win = 1

    def test_fit(self):
        """method for testing the fit method of PredAD"""
        test_class = self.__class__
        model = PredAD(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=False,
        )
        fitted_model = model.fit(test_class.X)
        self.assertEqual(id(fitted_model), id(model))

    def test_anomaly_score_and_predict(self):
        """method for testing the score method of PredAD"""
        test_class = self.__class__
        model = PredAD(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=False,
        )
        fitted_model = model.fit(test_class.X)
        score = fitted_model.anomaly_score(test_class.X)
        prediction_type="recent"
        predicts = fitted_model.predict(test_class.X,prediction_type=prediction_type)
        self.assertIsNotNone(predicts)
        self.assertIsNotNone(score)
        fitted_model.set_anomaly_scoring_params(observation_window=test_class.observation_window, scoring_method='Sliding-Window', scoring_threshold=10)
        score_sliding=fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score_sliding)
        fitted_model.set_anomaly_scoring_params(observation_window=test_class.observation_window,scoring_method='Adaptive-Sliding-Window', scoring_threshold=10)
        score_adaptive=fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score_adaptive)
        fitted_model.set_anomaly_scoring_params(observation_window=test_class.observation_window,scoring_method='Chi-Square', scoring_threshold=10)
        score_chi_square=fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score_chi_square)
        fitted_model.set_anomaly_scoring_params(observation_window=test_class.observation_window,scoring_method='Q-Score', scoring_threshold=10)
        score_q_score=fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score_q_score)
        fitted_model.set_anomaly_scoring_params(observation_window=test_class.observation_window,scoring_method='Contextual-Anomaly', scoring_threshold=10)
        score_contextual=fitted_model.anomaly_score(test_class.X)
        self.assertIsNotNone(score_contextual)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
