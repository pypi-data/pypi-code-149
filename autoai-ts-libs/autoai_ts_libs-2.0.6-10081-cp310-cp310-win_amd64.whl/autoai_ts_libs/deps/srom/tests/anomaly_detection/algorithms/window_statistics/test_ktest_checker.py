# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing ktest checker class"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.window_statistics.kstest_checker import KSTestChecker

class TestKSTestChecker(unittest.TestCase):
    """Test methods in KSTestChecker class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        x_array = np.zeros(100)  # Numpy array containins 100 0's
        y_array = np.ones(100)    # Numpy array containins 100 1's
        z_array = np.ones(100)
        # Add random outliers to below index's
        index = [35, 45, 55, 75, 95]
        values = [25, 17, 23, 2.5, 20]
        for i, value in enumerate(index):
            y_array[value] = values[i]
        # Add single outlier in z
        z_array[50] = 10
        z_array[80] = 39
        cls.dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'z': z_array})
        numpy_array = cls.dataframe.values

        # Multi-dimensional
        cls.train_data = pd.DataFrame(numpy_array[0:70, :]).values
        cls.test_data = pd.DataFrame(numpy_array[70:, :]).values
        # 1-D
        cls.train_data_1d = pd.DataFrame(y_array[0:70]).values
        cls.test_data_1d = pd.DataFrame(y_array[70:]).values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        ktc = KSTestChecker()
        fitted_ktc = ktc.fit(test_class.train_data)
        self.assertEqual(id(ktc), id(fitted_ktc))

    def test_threshold_method(self):
        """Test threshold related methods"""
        ktc = KSTestChecker()
        self.assertEqual(1, ktc.get_threshold())
        ktc.set_threshold(5)
        self.assertEqual(5, ktc.get_threshold())

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        ktc = KSTestChecker(threshold=1000000)
        ktc.fit(test_class.train_data_1d)
        prediction = ktc.predict(test_class.test_data_1d)
        self.assertEqual(0, prediction)

        prediction = ktc.predict(np.array([]))
        self.assertEqual(0, prediction)

        # length of train data equal to 1
        ktc.fit(np.array([1]))
        prediction = ktc.predict(np.array([1, 2]))
        self.assertEqual(0, prediction)

    def test_anomaly_score_method(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        ktc = KSTestChecker(threshold=-0.05)
        ktc.fit(test_class.train_data_1d)
        score = ktc.anomaly_score(test_class.test_data_1d)
        self.assertEqual(0.029, round(score, 3))

    def test_get_stats_method(self):
        """Test get_stats method"""
        test_class = self.__class__
        ktc = KSTestChecker(threshold=-0.05)
        self.assertIsNone(ktc.get_stats()['ks_d'])
        self.assertIsNone(ktc.get_stats()['ks_p_value'])
        ktc.fit(test_class.train_data)
        score = ktc.anomaly_score(test_class.test_data)
        self.assertEqual(round(ktc.get_stats()['ks_d'], 3), 0.014)
        self.assertEqual(1.0, round(ktc.get_stats()['ks_p_value'], 3))

    def test_predict_exceptions(self):
        """Test predict exceptions"""
        test_class = self.__class__
        ktc = KSTestChecker()
        self.assertRaises(RuntimeError, ktc.predict, test_class.test_data_1d)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
