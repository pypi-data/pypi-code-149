# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing ExtendedIsolationForest class"""
import unittest
import numpy as np
import pandas as pd
import copy

np.random.seed(0)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.extended_isolation_forest import (
    ExtendedIsolationForest,
)


class TestExtendedIsolationForest(unittest.TestCase):
    """Test methods in ExtendedIsolationForest class"""

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

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        e_isolation_forest = ExtendedIsolationForest(max_samples=10000000, max_features=1000)
        fitted_e_isolation_forest = e_isolation_forest.fit(test_class.dataframe)
        self.assertEqual(id(fitted_e_isolation_forest), id(e_isolation_forest))
        e_isolation_forest = ExtendedIsolationForest(max_samples=0.2, max_features=0)
        fitted_e_isolation_forest = e_isolation_forest.fit(test_class.numpy_array)
        self.assertEqual(id(fitted_e_isolation_forest), id(e_isolation_forest))
        e_isolation_forest = ExtendedIsolationForest(max_samples=10, max_features=2)
        fitted_e_isolation_forest = e_isolation_forest.fit(test_class.numpy_array)
        e_isolation_forest = ExtendedIsolationForest(max_samples=1.2)
        self.assertRaises(ValueError, e_isolation_forest.fit, test_class.numpy_array)

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        e_isolation_forest = ExtendedIsolationForest()
        e_isolation_forest.fit(test_class.dataframe)
        prediction = e_isolation_forest.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual([35, 50, 55, 75, 80, 95], outlier)
        prediction = e_isolation_forest.predict(test_class.numpy_array)

    def test_decision_function_method(self):
        """Test decision_function method"""
        test_class = self.__class__
        e_isolation_forest = ExtendedIsolationForest()
        e_isolation_forest = e_isolation_forest.fit(test_class.dataframe)
        scores = e_isolation_forest.decision_function(test_class.dataframe)
        outlier = np.where(scores > 0.7)[0].tolist()
        common_element = list(set([35, 50, 55, 75, 80, 95]) & set(outlier))
        self.assertGreater(len(common_element), 2)

    def test_with_numpy_dataset(self):
        """Test numpy dataset"""
        test_class = self.__class__
        e_isolation_forest = ExtendedIsolationForest(max_features=0.00001)
        e_isolation_forest = e_isolation_forest.fit(test_class.dataframe)
        prediction = e_isolation_forest.predict(test_class.dataframe.values)
        outlier = np.where(prediction < 0.0)[0].tolist()
        common_element = list(set([35, 50, 55, 75, 80, 95]) & set(outlier))
        self.assertGreater(len(common_element), 2)

    def test_predict_without_fit(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        e_isolation_forest = ExtendedIsolationForest()
        self.assertRaises(Exception, e_isolation_forest.predict, test_class.dataframe)
        test_class = self.__class__
        e_isolation_forest = ExtendedIsolationForest(max_samples="test")
        self.assertRaises(Exception, e_isolation_forest.fit, test_class.dataframe)
        test_class = self.__class__
        e_isolation_forest = ExtendedIsolationForest(
            max_samples="auto", max_features=2.2
        )
        self.assertRaises(Exception, e_isolation_forest.fit, test_class.dataframe)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
