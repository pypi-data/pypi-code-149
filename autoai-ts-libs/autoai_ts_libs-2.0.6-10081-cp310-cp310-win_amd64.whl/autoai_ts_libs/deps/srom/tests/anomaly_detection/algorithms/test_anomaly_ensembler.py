# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing AnomalyEnsembler class"""
import unittest
import numpy as np
import pandas as pd
import copy

np.random.seed(0)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_ensembler import AnomalyEnsembler


class TestAnomalyEnsembler(unittest.TestCase):
    """Test methods in AnomalyEnsembler class"""

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
        # Add single outlier in z
        z_array[50] = 2500
        z_array[80] = 2700
        cls.dataframe = pd.DataFrame({"x": x_array, "y": y_array, "z": z_array})
        cls.numpy_array = cls.dataframe.values
        cls.random_state = 1

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        anomaly_ensembler = AnomalyEnsembler(random_state=test_class.random_state)
        fitted_anomaly_ensembler = anomaly_ensembler.fit(test_class.dataframe)
        self.assertEqual(id(fitted_anomaly_ensembler), id(anomaly_ensembler))

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        anomaly_ensembler = AnomalyEnsembler(random_state=test_class.random_state)
        anomaly_ensembler.fit(test_class.dataframe)
        prediction = anomaly_ensembler.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertTrue(all(elem in outlier for elem in [35, 50, 55, 75, 80, 95]))

    def test_decision_function_method(self):
        """Test decision_function method"""
        test_class = self.__class__
        anomaly_ensembler = AnomalyEnsembler(random_state=test_class.random_state)
        anomaly_ensembler = anomaly_ensembler.fit(test_class.dataframe)
        scores = anomaly_ensembler.decision_function(test_class.dataframe)
        outlier = np.where(scores >= 0.0)[0].tolist()
        self.assertTrue(all(elem in outlier for elem in [35, 50, 55, 75, 80, 95]))

    def test_with_numpy_dataset(self):
        """Test numpy dataset"""
        test_class = self.__class__
        anomaly_ensembler = AnomalyEnsembler(random_state=test_class.random_state)
        anomaly_ensembler = anomaly_ensembler.fit(test_class.dataframe)
        prediction = anomaly_ensembler.predict(test_class.dataframe.values)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertTrue(all(elem in outlier for elem in [35, 50, 55, 75, 80, 95]))

    def test_predict_without_fit(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        anomaly_ensembler = AnomalyEnsembler(random_state=test_class.random_state)
        self.assertRaises(Exception, anomaly_ensembler.predict, test_class.dataframe)

    def test_extra(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        anomaly_ensembler = AnomalyEnsembler(random_state=test_class.random_state, predict_only=True)
        anomaly_ensembler = anomaly_ensembler.fit(test_class.dataframe)
        anomaly_ensembler.predict(test_class.dataframe.values)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
