""" Test the arima model. """
import unittest
import pandas as pd
from sklearn import datasets
import numpy as np
from autoai_ts_libs.deps.srom.time_series.models.arima import ARIMAModel


class TestARIMAModel(unittest.TestCase):
    """ class for testing the ARIMA model. """

    @classmethod
    def setUp(cls):
        diabetes = datasets.load_diabetes()
        cls.X_train = diabetes.data[:-20]
        cls.X_test = diabetes.data[-20:]
        cls.y_train = diabetes.target[:-20]
        cls.y_test = diabetes.target[-20:]
        cls.target_col = np.array([0])

    def test_fit(self):
        """ method for testing the fit method of ARIMA."""
        test_class = self.__class__
        model1 = ARIMAModel(target_columns=test_class.target_col)
        self.assertIsNotNone(model1.fit(test_class.X_train))
        self.assertIsNotNone(model1.fit(test_class.X_train, test_class.y_train))
        model3 = ARIMAModel(target_columns=[0, 1])
        self.assertRaises(Exception, model3.fit, test_class.X_train)

    def test_predict(self):
        """ Tests the predict method of ARIMA. """
        test_class = self.__class__
        model1 = ARIMAModel(target_columns=test_class.target_col)
        model1.fit(test_class.X_train)
        pred = model1.predict(test_class.X_test)
        self.assertIsNotNone(pred)
        self.assertIsInstance(pred, np.ndarray)

    def test_predict_sliding_window(self):
        """ Tests the predict sliding window of ARIMA."""
        test_class = self.__class__
        model1 = ARIMAModel(target_columns=test_class.target_col)
        model1.fit(test_class.X_train)
        predict = model1.predict(test_class.X_test,prediction_type="sliding")
        self.assertIsNotNone(predict)
        self.assertIsInstance(predict, np.ndarray)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
