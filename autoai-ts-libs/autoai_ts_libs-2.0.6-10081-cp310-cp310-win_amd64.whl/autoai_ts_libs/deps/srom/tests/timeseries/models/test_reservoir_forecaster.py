""" Test the ReservoirForecaster model. """
import unittest

# import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from autoai_ts_libs.deps.srom.time_series.models.ReservoirForecaster import ReservoirForecaster


class TestReservoirForecaster(unittest.TestCase):
    """class for testing the ReservoirForecaster model."""

    @classmethod
    def setUp(cls):
        x1 = np.arange(0,20)
        # x2 = np.arange(200,220)
        x1 = x1.reshape(-1,1)
        # x2 = x2.reshape(-1,1)
        #cls.X = np.hstack([x1,x2])
        cls.X = x1

    def test_fit(self):
        """method for testing the fit method"""
        test_class = self.__class__
        model1 = ReservoirForecaster(
            target_columns=[0],
            feature_columns=[0]
        )
        self.assertIsNotNone(model1.fit(test_class.X))

    def test_predict(self):
        """Tests the predict method"""
        test_class = self.__class__
        model1 = ReservoirForecaster(
            target_columns=[0],
            feature_columns=[0]
        )
        model1.fit(test_class.X[:15])
        pred = model1.predict(test_class.X[15:,],prediction_type="forecast")
        self.assertEqual(pred.shape,(5,1))


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
