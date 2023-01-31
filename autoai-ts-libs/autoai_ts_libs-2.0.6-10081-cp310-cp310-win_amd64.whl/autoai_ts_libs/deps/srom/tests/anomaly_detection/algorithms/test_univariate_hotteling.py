# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing UnivariateHotteling class"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.univariate_hotteling import UnivariateHotteling

class TestUnivariateHotteling(unittest.TestCase):
    """Test methods in UnivariateHotteling class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.samples = np.array([-1, -2, -3, 1, 2, 3])
        cls.samples_diff_col = np.array([[-1, -1, 1], [-2, -1, 1], [-3, -2, 0], [1, 1, 0]])
        cls.predict_samples = np.array([0, -1, 3, 1,  2])
        cls.invalid_samples = np.array([1, 1])
        # converting to pandas dataframes
        cls.samples_df = pd.DataFrame(cls.samples)
        cls.predict_samples_df = pd.DataFrame(cls.predict_samples)
        cls.expected_res = [0, 0, 1, 0, 1]
        cls.expected_anomaly_scores = [0.0, 0.21428571428571427, 1.9285714285714284, 0.21428571428571427, 0.8571428571428571]
        
    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        samples = test_class.samples
        samples_df = test_class.samples_df
        univariate_hotelling = UnivariateHotteling(0.8)

        # numpy array
        univariate_hotelling.fit(samples)
        self.assertEqual(univariate_hotelling.anomaly_score_threshold, 0.7083263008007934)
        self.assertEqual(univariate_hotelling.avg, 0.0)
        self.assertEqual(univariate_hotelling.var, 4.666666666666667)
        self.assertRaises(TypeError, univariate_hotelling.fit, samples.reshape(-1,2))

        # pandas dataframe
        univariate_hotelling = UnivariateHotteling(0.8)
        univariate_hotelling.fit(samples_df)
        self.assertEqual(univariate_hotelling.anomaly_score_threshold, 0.7083263008007934)
        self.assertEqual(univariate_hotelling.avg, 0.0)
        self.assertEqual(univariate_hotelling.var, 4.666666666666667)

    def test_predict(self):
        """Test predict method"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        samples_df = test_class.samples_df
        predict_samples_df = test_class.predict_samples_df
        expected_res = test_class.expected_res

        # using numpy array as input
        univariate_hotelling = UnivariateHotteling(0.8)
        univariate_hotelling.fit(samples)
        univariate_hotelling.anomaly_score([1])
        univariate_hotelling.decision_function([1])
        res = univariate_hotelling.predict(predict_samples)
        self.assertListEqual(list(res), expected_res)

        # try using pandas dataframe as input
        univariate_hotelling = UnivariateHotteling(0.8)
        univariate_hotelling.fit(samples_df)
        res = univariate_hotelling.predict(predict_samples_df)
        self.assertListEqual(list(res), expected_res)

    def test_predict_exceptions(self):
        """Test predict exceptions"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        samples_diff_col = test_class.samples_diff_col
        # predict without fit
        univariate_hotelling = UnivariateHotteling(0.8)
        self.assertRaises(Exception, univariate_hotelling.predict, predict_samples)
        # predict with data with different number of columns
        univariate_hotelling.fit(samples)
        self.assertRaises(Exception, univariate_hotelling.predict, samples_diff_col)

    def test_anomaly_score(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        samples_df = test_class.samples_df
        predict_samples_df = test_class.predict_samples_df
        expected_anomaly_scores = test_class.expected_anomaly_scores

        # using numpy array as input
        univariate_hotelling = UnivariateHotteling(0.8)
        univariate_hotelling.fit(samples)
        score = univariate_hotelling.anomaly_score(predict_samples)
        self.assertIsNotNone(score)
        self.assertListEqual(score, expected_anomaly_scores)

        # try using pandas dataframe as input
        univariate_hotelling = UnivariateHotteling(0.8)
        univariate_hotelling.fit(samples_df)
        score = univariate_hotelling.anomaly_score(predict_samples_df)
        self.assertIsNotNone(score)
        self.assertListEqual(score, expected_anomaly_scores)

    def test_anomaly_score_exceptions(self):
        """Test anomaly_score exceptions"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        samples_diff_col = test_class.samples_diff_col
        # anomaly score without fit
        univariate_hotelling = UnivariateHotteling(0.8)
        self.assertRaises(Exception, univariate_hotelling.anomaly_score, predict_samples)
        # anomaly score with data with different number of columns
        univariate_hotelling.fit(samples)
        self.assertRaises(Exception, univariate_hotelling.anomaly_score, samples_diff_col)

    def test_invalid_input_data(self):
        """Test predict and anomaly_score with invalid data"""
        test_class = self.__class__
        invalid_samples = test_class.invalid_samples

        # test anomaly_score with invalid data
        univariate_hotelling = UnivariateHotteling(0.8)
        univariate_hotelling.fit(invalid_samples)
        score = univariate_hotelling.anomaly_score(invalid_samples)
        self.assertTrue(all([np.isnan(s) for s in score]))

        # test predict with invalid data
        score = univariate_hotelling.predict(invalid_samples)
        self.assertTrue(all([np.isnan(s) for s in score]))

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
