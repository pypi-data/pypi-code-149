"""Unit test cases for testing extended_emcd class"""
import unittest
import numpy as np
import pandas as pd
import copy

np.random.seed(0)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.extended_mincovdet import ExtendedMinCovDet


class TestExtendedMinCovDet(unittest.TestCase):
    """Test methods in ExtendedMinCovDet class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
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
        emcd = ExtendedMinCovDet()
        fitted_emcd = emcd.fit(test_class.numpy_array)
        self.assertEqual(id(fitted_emcd), id(emcd))

        emcd = ExtendedMinCovDet(num_rows=10, num_cols=2)
        fitted_emcd = emcd.fit(test_class.numpy_array, test_class.numpy_array[:,1].reshape(-1,1))

    def test_score_method(self):
        """Test score method"""
        np.random.seed(0)
        test_class = self.__class__
        emcd = ExtendedMinCovDet()
        fitted_emcd = emcd.fit(test_class.numpy_array)
        score = fitted_emcd.score(test_class.numpy_array)
        #self.assertAlmostEqual(score, float('-inf'))

    def test_mahalanobis(self):
        """Test mahalanobis method"""
        test_class = self.__class__
        np.random.seed(0)
        test_class = self.__class__
        emcd = ExtendedMinCovDet()
        fitted_emcd = emcd.fit(test_class.numpy_array)
        prediction = fitted_emcd.mahalanobis(test_class.numpy_array)
        outlier = np.where(prediction > 1.0e+08)[0].tolist()
        self.assertEqual([35, 55, 75, 95],outlier)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)

TestExtendedMinCovDet()
