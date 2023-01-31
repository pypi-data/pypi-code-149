# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing NSA class"""
import unittest
import numpy as np
import pandas as pd
import copy
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.negative_sample_anomaly import NSA
from sklearn.ensemble import RandomForestClassifier


class TestNSA(unittest.TestCase):
    """Test methods in NSA class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        np.random.seed(0)
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
        # Add single outlier in z
        z_array[50] = 2500
        z_array[80] = 2700
        cls.dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'z': z_array})
        cls.numpy_array = cls.dataframe.values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        np.random.seed(0)
        nsa = NSA(scale=True,sample_ratio=0.4,sample_delta=0.05)
        fitted_nsa = nsa.fit(test_class.dataframe)
        self.assertEqual(id(nsa), id(fitted_nsa))

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        np.random.seed(0)
        nsa = NSA(base_model=RandomForestClassifier(random_state=1),scale=True,sample_ratio=0.95,sample_delta=0.005,anomaly_threshold=0.08)
        nsa = nsa.fit(test_class.dataframe)
        prediction = nsa.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual( [20, 33, 50, 55, 80, 95], outlier)

    def test_anomaly_score_method(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        np.random.seed(0)
        nsa = NSA(base_model=RandomForestClassifier(random_state=1),scale=True,sample_ratio=0.95,sample_delta=0.005,anomaly_threshold=0.1)
        nsa = nsa.fit(test_class.dataframe)
        anomaly_scores = nsa.anomaly_score(test_class.dataframe)
        outlier = np.where(anomaly_scores >= 0.08)[0].tolist()
        self.assertEqual([20, 33, 50, 55, 80, 95], outlier)

    def test_without_scaling(self):
        """Test without scaling"""
        test_class = self.__class__
        np.random.seed(0)
        nsa = NSA(base_model=RandomForestClassifier(random_state=1),scale=False,sample_ratio=0.95,sample_delta=0.005,anomaly_threshold=0.1)
        nsa = nsa.fit(test_class.dataframe)
        prediction = nsa.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual( [20, 33, 95], outlier)

    def test_with_numpy_dataset(self):
        """Test numpy dataset"""
        test_class = self.__class__
        np.random.seed(0)
        nsa = NSA(base_model=RandomForestClassifier(random_state=1),scale=True,sample_ratio=0.95,sample_delta=0.005,anomaly_threshold=0.09)
        nsa = nsa.fit(test_class.dataframe)
        prediction = nsa.predict(test_class.dataframe.values)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual( [20, 33, 80, 95], outlier)

    def test_predict_without_fit(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        nsa = NSA(base_model=RandomForestClassifier(random_state=1),scale=False,sample_ratio=0.8,sample_delta=0.005,anomaly_threshold=0.04)
        self.assertRaises(Exception, nsa.predict, test_class.dataframe)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
