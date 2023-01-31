# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing SampleSVDD class"""
import unittest
import numpy as np
import pandas as pd
import copy

np.random.seed(0)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.sample_svdd import SampleSVDD


class TestSampleSVDD(unittest.TestCase):
    """Test methods in SampleSVDD class"""

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
        sample_svdd = SampleSVDD()
        fitted_sample_svdd = sample_svdd.fit(test_class.dataframe)
        self.assertEqual(id(fitted_sample_svdd), id(sample_svdd))

    def test_predict_method(self):
        """Test predict method"""
        np.random.seed(0)
        test_class = self.__class__
        sample_svdd = SampleSVDD(outlier_fraction=0.001, kernel_s=5)
        sample_svdd = sample_svdd.fit(test_class.dataframe)
        prediction = sample_svdd.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertIsNotNone(outlier)

    def test_decision_function_method(self):
        """Test decision_function method"""
        test_class = self.__class__
        np.random.seed(0)
        sample_svdd = SampleSVDD(outlier_fraction=0.001, kernel_s=5)
        sample_svdd = sample_svdd.fit(test_class.dataframe)
        scores = sample_svdd.decision_function(test_class.dataframe)
        outlier = np.where(scores < 0.0)[0].tolist()
        self.assertIsNotNone(outlier)

    def test_with_numpy_dataset(self):
        """Test numpy dataset"""
        np.random.seed(0)
        test_class = self.__class__
        sample_svdd = SampleSVDD(outlier_fraction=0.001, kernel_s=5)
        sample_svdd = sample_svdd.fit(test_class.dataframe)
        prediction = sample_svdd.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertIsNotNone(outlier)

    def test_predict_without_fit(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        sample_svdd = SampleSVDD()
        self.assertRaises(Exception, sample_svdd.predict, test_class.dataframe)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
