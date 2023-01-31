""" Test the Mean model. """
import unittest
import pandas as pd
import numpy as np
from sklearn import datasets
from autoai_ts_libs.deps.srom.time_series.models import mean


class TestMeanModel(unittest.TestCase):
    """class for testing the Mean model."""

    @classmethod
    def setUp(cls):
        diabetes = datasets.load_diabetes()
        cls.X_train = diabetes.data[:-20]
        cls.X_test = diabetes.data[-20:]
        cls.y_train = diabetes.target[:-20]
        cls.y_test = diabetes.target[-20:]
        cls.target_col = np.array([0])

    def test_fit(self):
        """method for testing the fit method of Mean."""
        test_class = self.__class__
        model1 = mean.MeanModel(target_columns=test_class.target_col)
        self.assertIsNotNone(model1.fit(test_class.X_train))
        self.assertIsNotNone(model1.fit(test_class.X_train, test_class.y_train))
        self.assertIsNotNone(model1.fit(test_class.X_train, test_class.y_train))

    def test_predict_sliding_window(self):
        """Tests the predict_sliding_window method of Mean."""
        test_class = self.__class__
        model1 = mean.MeanModel(target_columns=test_class.target_col)
        model1.fit(test_class.X_train)
        pred = model1.predict(test_class.X_test, prediction_type="sliding")
        self.assertIsNotNone(pred)
        self.assertIsInstance(pred, np.ndarray)
        pred = model1.predict(test_class.X_test, prediction_type="training")
        self.assertIsNotNone(pred)
        self.assertIsInstance(pred, np.ndarray)
        


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
