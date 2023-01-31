"""Unit test cases for testing SSTChecker class"""
import unittest
import numpy as np
import pandas as pd
import copy

np.random.seed(0)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.window_statistics.sst_checker import SSTChecker


class TestSSTChecker(unittest.TestCase):
    """Test methods in SSTChecker class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        mu, sigma = 0.5, 0.1
        s1 = np.random.normal(0.5, 0.1, 100)
        s2 = np.random.normal(0.49, 0.3, 100)
        x_array = s1
        y_array = copy.copy(s1)
        z_array = s2
        # Add random outliers to below index's
        index = [35, 55, 75, 95]
        values = [2500, 2300, 2700, 2000]
        for i, value in enumerate(index):
            y_array[value] = values[i]
        cls.dataframe = pd.DataFrame({"x": x_array, "y": y_array, "z": z_array})
        cls.numpy_array = cls.dataframe.values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        sst_instance = SSTChecker()
        fitted_sst = sst_instance.fit(test_class.dataframe)
        self.assertEqual(id(fitted_sst), id(fitted_sst))

    def test_anomaly_score_method(self):
        """Test anomaly_score method"""
        np.random.seed(0)
        test_class = self.__class__
        sst_instance = SSTChecker()
        fitted_sst = sst_instance.fit(test_class.dataframe)
        anomaly_score = fitted_sst.anomaly_score(test_class.dataframe)
        outlier = np.where(anomaly_score < 0.0)[0].tolist()
        self.assertIsNotNone(outlier)

    def test_anomaly_score_without_fit(self):
        """Test anomaly_score method without calling fit method"""
        test_class = self.__class__
        sst_instance = SSTChecker()
        self.assertRaises(Exception, sst_instance.anomaly_score, test_class.dataframe)

    def test_predict(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        sst_instance = SSTChecker()
        fitted_sst = sst_instance.fit(test_class.dataframe)
        predict = fitted_sst.predict(test_class.dataframe)
        self.assertIsNotNone(predict)

    def test_get_stats(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        sst_instance = SSTChecker()
        fitted_sst = sst_instance.fit(test_class.dataframe)
        predict = fitted_sst.predict(test_class.dataframe)
        stats = fitted_sst.get_stats()
        self.assertIsNotNone(predict)
        self.assertIsNotNone(stats)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
