import os
import unittest
import numpy as np
import pandas as pd
from sklearn import datasets
from autoai_ts_libs.deps.srom.time_series.models import zero


class TestZeroModel(unittest.TestCase):
    """Test methods in ZeroModel class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        diabetes = datasets.load_diabetes()
        cls.X_train = diabetes.data[:-20]
        cls.X_test = diabetes.data[-20:]
        cls.y_train = diabetes.target[:-20]
        cls.y_test = diabetes.target[-20:]
        cls.target_col = np.array([0])

    @classmethod
    def tearDownClass(test_class):
        pass

    def test_fit(self):
        """
        Test fit method
        """
        test_class = self.__class__
        lookback_win = 1
        regressor = zero.ZeroModel(
            target_columns=test_class.target_col, lookback_win=lookback_win, pred_win=1
        )
        fitted = regressor.fit(test_class.X_train, test_class.y_train)
        self.assertEqual(fitted, regressor)

    def test_predict(self):
        """
        Test predict method
        """
        test_class = self.__class__
        lookback_win = 1
        regressor = zero.ZeroModel(
            target_columns=test_class.target_col, lookback_win=lookback_win, pred_win=1
        )
        regressor = regressor.fit(test_class.X_train, test_class.y_train)
        pred = regressor.predict(
            test_class.X_train[-3:],
        )
        mean = np.mean(pred)
        self.assertAlmostEqual(mean, 0.0380759064334241,4)

    def test_predict_sliding_window(self):
        """
        Test predict_sliding_window method
        """
        test_class = self.__class__
        lookback_win = 1
        regressor = zero.ZeroModel(
            target_columns=test_class.target_col, lookback_win=lookback_win, pred_win=1
        )
        regressor = regressor.fit(test_class.X_train, test_class.y_train)
        pred = regressor.predict(test_class.X_train[-3:], "sliding")
        mean = np.mean(pred)
        self.assertAlmostEqual(mean, 0.0380759064334241,4)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
