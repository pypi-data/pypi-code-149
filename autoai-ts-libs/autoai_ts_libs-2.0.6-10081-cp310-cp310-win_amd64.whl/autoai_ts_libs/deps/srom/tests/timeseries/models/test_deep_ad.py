""" Test DeepAD """
import unittest

import numpy as np
from sklearn.linear_model import LinearRegression
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_robust_pca import AnomalyRobustPCA
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.time_series.pipeline import DeepAD, PredAD


class TestDeepAD(unittest.TestCase):
    """class for testing DeepAD"""

    @classmethod
    def setUp(cls):
        x = np.arange(50)
        cls.target_columns = [0]
        cls.X = x.reshape(-1, 1)

    def test_fit(self):
        """method for testing the fit method of DeepAD"""
        test_class = self.__class__
        model = DeepAD(
            steps=[
                PredAD(
                    steps=[
                        ("flatten", Flatten()),
                        ("linearregression", LinearRegression()),
                    ],

                    lookback_win=5,
                    feature_columns=[0],
                    target_columns=[0],
                    pred_win=1,
                ),
                PredAD(
                    steps=[
                        ("flatten", Flatten()),
                        ("linearregression", AnomalyRobustPCA()),
                    ],
                    lookback_win=5,
                    feature_columns=[0],
                    target_columns=[0],
                    pred_win=1,
                ),
            ]
        )
        fitted_model = model.fit(test_class.X)
        self.assertEqual(fitted_model, model)

    def test_prediction_error(self):
        """method for testing the predict method of DeepAD"""
        test_class = self.__class__
        # Test Multivariate
        model = DeepAD(
            steps=[
                PredAD(
                    steps=[
                        ("flatten", Flatten()),
                        ("linearregression", LinearRegression()),
                    ],
                    lookback_win=5,
                    feature_columns=[0],
                    target_columns=[0],
                    pred_win=1,
                ),
                PredAD(
                    steps=[
                        ("flatten", Flatten()),
                        ("linearregression", AnomalyRobustPCA()),
                    ],
                    lookback_win=5,
                    feature_columns=[0],
                    target_columns=[0],
                    pred_win=1,
                ),
            ]
        )
        fitted_model = model.fit(test_class.X)
        pred_x = fitted_model.prediction_error(test_class.X)
        self.assertIsNotNone(pred_x)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
