# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing TTestChecker class"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.window_statistics.ttest_checker import TTestChecker

class TestTTestChecker(unittest.TestCase):
    """Test methods in TTestChecker class"""

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
        cls.test_data_1d = pd.DataFrame(y_array[50:]).values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        ttc = TTestChecker()
        fitted_ttc = ttc.fit(test_class.train_data)
        self.assertEqual(id(ttc), id(fitted_ttc))

    def test_threshold_method(self):
        """Test threshold related methods"""
        ttc = TTestChecker(threshold=0.05)
        self.assertEqual(0.05, ttc.get_threshold())
        ttc.set_threshold(5)
        self.assertEqual(5, ttc.get_threshold())

    def test_axis_method(self):
        """Test axis related methods"""
        ttc = TTestChecker(axis=0)
        self.assertEqual(0, ttc.get_axis())
        ttc.set_axis(1)
        self.assertEqual(1, ttc.get_axis())

    def test_equal_var_method(self):
        """Test equal_var related methods"""
        ttc = TTestChecker(equal_var=True)
        self.assertEqual(True, ttc.get_equal_var())
        ttc.set_equal_var(False)
        self.assertEqual(False, ttc.get_equal_var())

    def test_nan_policy_method(self):
        """Test nan policy related methods"""
        ttc = TTestChecker(nan_policy='omit')
        self.assertEqual('omit', ttc.get_nan_policy())
        ttc.set_nan_policy('propagate')
        self.assertEqual('propagate', ttc.get_nan_policy())

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        ttc = TTestChecker()
        ttc.fit(test_class.train_data_1d)
        prediction = ttc.predict(test_class.test_data_1d)
        self.assertEqual(0, prediction)

        ttc = TTestChecker(direction='negative', threshold=pow(10, -150), nan_policy='omit')
        ttc.fit(test_class.train_data_1d)
        prediction = ttc.predict(test_class.test_data_1d)
        self.assertEqual(-1, prediction)

        ttc = TTestChecker(direction='positive', threshold=1, nan_policy='propagate')
        ttc.fit(test_class.train_data_1d)
        prediction = ttc.predict(test_class.test_data_1d)
        self.assertEqual(1, prediction)

    def test_anomaly_score_method(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        ttc = TTestChecker(direction='positive', threshold=1, nan_policy='propagate')
        ttc.fit(test_class.train_data_1d)
        score = ttc.anomaly_score(test_class.test_data_1d)
        self.assertEqual( 0.046, round(score[0], 3))

    def test_get_stats_method(self):
        """Test get_stats method"""
        test_class = self.__class__
        gtc = TTestChecker(direction='positive', threshold=1, nan_policy='propagate')
        self.assertIsNone(gtc.get_stats()['ttest_score'])
        self.assertIsNone(gtc.get_stats()['p_value'])
        gtc.fit(test_class.train_data_1d)
        score = gtc.anomaly_score(test_class.test_data_1d)
        self.assertEqual(round(gtc.get_stats()['ttest_score'][0], 3), round(score[0], 3))
        self.assertEqual(0.046, round(gtc.get_stats()['ttest_score'][0], 3))
        self.assertEqual(0.963, round(gtc.get_stats()['p_value'][0], 3))

    def test_predict_exceptions(self):
        """Test predict exceptions"""
        test_class = self.__class__
        ttc = TTestChecker()
        self.assertRaises(RuntimeError, ttc.predict, test_class.test_data_1d)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
