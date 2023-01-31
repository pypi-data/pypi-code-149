# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing NMT_Anomaly class"""
import unittest
import numpy as np
import pandas as pd

np.random.seed(0)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.NMT_anomaly import NMT_anomaly


class TestNMTAnomaly(unittest.TestCase):
    """Test methods in NMT_Anomaly class"""

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
        nmt_anomaly = NMT_anomaly(feature_columns=[0,1,2],target_columns=[0,1,2])
        fitted_nmt_anomaly = nmt_anomaly.fit(test_class.dataframe.values)
        self.assertEqual(id(fitted_nmt_anomaly), id(nmt_anomaly))

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        nmt_anomaly = NMT_anomaly(feature_columns=[0,1,2],target_columns=[0,1,2])
        fitted_nmt_anomaly = nmt_anomaly.fit(test_class.dataframe.values)
        prediction = fitted_nmt_anomaly.predict(test_class.dataframe.values)
        fitted_nmt_anomaly.anomaly_score(test_class.dataframe.values)
        self.assertEqual(prediction.shape[0], test_class.dataframe.values.shape[0])

    def test_exception(self):
        """Test exception"""
        test_class = self.__class__
        nmt_anomaly = NMT_anomaly(feature_columns=[0,1,2],target_columns=[0,1,2])
        try:
            nmt_anomaly._covariate_model(None, None)
        except:
            pass

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
