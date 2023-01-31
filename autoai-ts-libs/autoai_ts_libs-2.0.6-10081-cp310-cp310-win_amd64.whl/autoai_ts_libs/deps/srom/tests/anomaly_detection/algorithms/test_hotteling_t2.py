# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing HotellingT2 class"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.hotteling_t2 import HotellingT2

class TestHotellingT2(unittest.TestCase):
    """Test methods in HotellingT2 class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.samples = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
        cls.samples_diff_col = np.array([[-1, -1, 1], [-2, -1, 1], [-3, -2, 0], [1, 1, 0]])
        cls.predict_samples = np.array([[-1, 0], [-1, 1], [3, 0], [1, 1], [1, -1], [1, 2]])
        cls.invalid_samples = np.array([[1, 1], [1, 1]])
        # converting to pandas dataframes
        cls.samples_df = pd.DataFrame(cls.samples)
        cls.predict_samples_df = pd.DataFrame(cls.predict_samples)
        # expected score
        cls.expected_score = 0.518781

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        samples = test_class.samples
        samples_df = test_class.samples_df
        hotelling_t2 = HotellingT2()

        # numpy array
        hotelling_t2.fit(samples)
        self.assertEqual(hotelling_t2.train_num_col, 2)
        self.assertEqual(hotelling_t2.train_num_rows, 6)
        self.assertTrue(np.array_equal(hotelling_t2.train_mean, np.array([0., 0.])))
        self.assertIsNotNone(hotelling_t2.train_cov)

        # pandas dataframe
        hotelling_t2 = HotellingT2()
        hotelling_t2.fit(samples_df)
        self.assertEqual(hotelling_t2.train_num_col, 2)
        self.assertEqual(hotelling_t2.train_num_rows, 6)
        self.assertTrue(np.array_equal(hotelling_t2.train_mean, np.array([0., 0.])))
        self.assertIsNotNone(hotelling_t2.train_cov)

    def test_predict(self):
        """Test predict method"""
        test_class = self.__class__
        samples = test_class.samples
        samples_diff_col = test_class.samples_diff_col
        predict_samples = test_class.predict_samples
        samples_df = test_class.samples_df
        predict_samples_df = test_class.predict_samples_df
        expected_score = test_class.expected_score

        # using numpy array as input
        hotelling_t2 = HotellingT2()
        hotelling_t2.fit(samples)
        score = hotelling_t2.predict(predict_samples)
        self.assertIsNotNone(score)
        self.assertAlmostEqual(score, expected_score, places=4)

        # try using pandas dataframe as input
        hotelling_t2 = HotellingT2()
        hotelling_t2.fit(samples_df)
        score = hotelling_t2.predict(predict_samples_df)
        self.assertIsNotNone(score)
        self.assertAlmostEqual(score, expected_score, places=4)

    def test_predict_exceptions(self):
        """Test predict exceptions"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        samples_diff_col = test_class.samples_diff_col
        # predict without fit
        hotelling_t2 = HotellingT2()
        self.assertRaises(Exception, hotelling_t2.predict, predict_samples)
        # predict with data with different number of columns
        hotelling_t2.fit(samples)
        self.assertRaises(Exception, hotelling_t2.predict, samples_diff_col)

    def test_anomaly_score(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        samples_df = test_class.samples_df
        predict_samples_df = test_class.predict_samples_df
        expected_score = test_class.expected_score
        # using numpy array as input
        hotelling_t2 = HotellingT2()
        hotelling_t2.fit(samples)
        score = hotelling_t2.anomaly_score(predict_samples)
        self.assertIsNotNone(score)
        self.assertAlmostEqual(score, expected_score, places=4)
        # try using pandas dataframe as input
        hotelling_t2 = HotellingT2()
        hotelling_t2.fit(samples_df)
        score = hotelling_t2.anomaly_score(predict_samples_df)
        self.assertIsNotNone(score)
        self.assertAlmostEqual(score, expected_score, places=4)

    def test_anomaly_score_exceptions(self):
        """Test anomaly_score exceptions"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        samples_diff_col = test_class.samples_diff_col
        # anomaly score without fit
        hotelling_t2 = HotellingT2()
        self.assertRaises(Exception, hotelling_t2.anomaly_score, predict_samples)
        # anomaly score with data with different number of columns
        hotelling_t2.fit(samples)
        self.assertRaises(Exception, hotelling_t2.anomaly_score, samples_diff_col)

    def test_invalid_input_data(self):
        """Test predict and anomaly_score with invalid data"""
        test_class = self.__class__
        invalid_samples = test_class.invalid_samples

        # test anomaly_score with invalid data
        hotelling_t2 = HotellingT2()
        hotelling_t2.fit(invalid_samples)
        score = hotelling_t2.anomaly_score(invalid_samples)
        self.assertIsNone(score)

        # test predict with invalid data
        score = hotelling_t2.predict(invalid_samples)
        self.assertIsNone(score)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
