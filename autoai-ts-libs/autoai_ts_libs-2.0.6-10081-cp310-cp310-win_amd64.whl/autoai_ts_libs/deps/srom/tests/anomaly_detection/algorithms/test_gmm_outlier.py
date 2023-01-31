# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing GMMOutlier class"""
import unittest
import numpy as np
import pandas as pd

np.random.seed(0)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.gmm_outlier import GMMOutlier


class TestGMMOutlier(unittest.TestCase):
    """Test methods in GMMOutlier class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        mu, sigma = 0.5, 0.1
        s = np.random.normal(mu, sigma, 100)
        x_array = s
        y_array = s
        z_array = s
        # Add random outliers to below index's
        index = [35, 55, 75, 95]
        values = [2500, 2300, 2700, 2000]
        for i, value in enumerate(index):
            y_array[value] = values[i]
        # Add single outlier in z
        z_array[50] = 2000
        z_array[80] = 3900
        cls.dataframe = pd.DataFrame({"x": x_array, "y": y_array, "z": z_array})
        cls.numpy_array = cls.dataframe.values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        gmm_outlier = GMMOutlier()
        fitted_bayesian_gmm_outlier = gmm_outlier.fit(test_class.dataframe)
        self.assertEqual(id(fitted_bayesian_gmm_outlier), id(gmm_outlier))

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        gmm_outlier = GMMOutlier(threshold=0.95)
        gmm_outlier = gmm_outlier.fit(test_class.dataframe)
        prediction = gmm_outlier.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual([35, 50, 55, 75, 80, 95], outlier)

    def test_score_samples_method(self):
        """Test score_samples method"""
        test_class = self.__class__
        gmm_outlier = GMMOutlier(threshold=0.95)
        gmm_outlier = gmm_outlier.fit(test_class.dataframe)
        scores = gmm_outlier.score_samples(test_class.dataframe)
        outlier = np.where(scores > 0.0)[0].tolist()
        self.assertEqual([35, 50, 55, 75, 80, 95], outlier)

    def test_with_numpy_dataset(self):
        """Test numpy dataset"""
        test_class = self.__class__
        gmm_outlier = GMMOutlier(threshold=0.95)
        gmm_outlier = gmm_outlier.fit(test_class.dataframe)
        prediction = gmm_outlier.predict(test_class.dataframe.values)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual([35, 50, 55, 75, 80, 95], outlier)

    def test_predict_without_fit(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        gmm_outlier = GMMOutlier(threshold=0.95)
        self.assertRaises(Exception, gmm_outlier.predict, test_class.dataframe)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
