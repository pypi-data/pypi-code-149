# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing ZscoreChecker class"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.window_statistics.zscore_checker import ZscoreChecker

class TestZscoreChecker(unittest.TestCase):
    """Test methods in ZscoreChecker class"""

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
        zsc = ZscoreChecker()
        fitted_zsc = zsc.fit(test_class.train_data)
        self.assertEqual(id(zsc), id(fitted_zsc))

    def test_threshold_method(self):
        """Test threshold related methods"""
        zsc = ZscoreChecker()
        self.assertEqual(3, zsc.get_threshold())
        zsc.set_threshold(5)
        self.assertEqual(5, zsc.get_threshold())

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        zsc = ZscoreChecker(-0.05)
        zsc.fit(test_class.train_data_1d)
        prediction = zsc.predict(test_class.test_data_1d)
        self.assertEqual(1, prediction)

    def test_anomaly_score_method(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        zsc = ZscoreChecker(-0.05)
        zsc.fit(test_class.train_data_1d)
        score = zsc.anomaly_score(test_class.test_data_1d)
        self.assertEqual(-0.035, round(score, 3))

    def test_get_stats_method(self):
        """Test get_stats method"""
        test_class = self.__class__
        zsc = ZscoreChecker(-0.05)
        self.assertIsNone(zsc.get_stats()['z_score'])
        zsc.fit(test_class.train_data_1d)
        score = zsc.anomaly_score(test_class.test_data_1d)
        self.assertEqual(round(zsc.get_stats()['z_score'], 3), round(score, 3))
        self.assertEqual(-0.035, round(zsc.get_stats()['z_score'], 3))

    def test_predict_exceptions(self):
        """Test predict exceptions"""
        test_class = self.__class__
        zsc = ZscoreChecker()
        self.assertRaises(RuntimeError, zsc.predict, test_class.test_data_1d)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
