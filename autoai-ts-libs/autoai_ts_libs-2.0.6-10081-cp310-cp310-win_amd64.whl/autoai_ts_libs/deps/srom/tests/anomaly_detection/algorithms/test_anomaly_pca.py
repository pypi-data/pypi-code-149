# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing AnomalyPCA class"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_pca import AnomalyPCA


class TestAnomalyPCA(unittest.TestCase):
    """Test methods in AnomalyPCA class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        x_array = np.zeros(100)  # Numpy array containins 100 0's
        y_array = np.ones(100)  # Numpy array containins 100 1's
        z_array = np.ones(100)
        # Add random outliers to below index's
        index = [35, 45, 55, 75, 95]
        values = [25, 17, 23, 2.5, 20]
        for i, value in enumerate(index):
            y_array[value] = values[i]
        # Add single outlier in z
        z_array[50] = 10
        z_array[80] = 39
        cls.dataframe = pd.DataFrame({"x": x_array, "y": y_array, "z": z_array})
        cls.numpy_array = cls.dataframe.values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        ar_pca = AnomalyPCA(n_components=2)
        fitted_ar_pca = ar_pca.fit(test_class.dataframe)
        self.assertEqual(id(ar_pca), id(fitted_ar_pca))

    def test_anomaly_score_method(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        ar_pca = AnomalyPCA(n_components=2)
        ar_pca.fit(test_class.dataframe)
        anomaly_scores = ar_pca.anomaly_score(test_class.dataframe)
        anomaly_scores = pd.DataFrame(anomaly_scores).apply(round)
        outlier = np.where(anomaly_scores > 0.0)[0].tolist()
        self.assertIsNotNone(ar_pca.decision_function(test_class.dataframe))
        
        ar_pca.anomaly_score_option = 'reconstruction'
        ar_pca.anomaly_score(test_class.dataframe)
        
        try:
            ar_pca.anomaly_score_option = 'log-likelihood'
            ar_pca.anomaly_score(test_class.dataframe)
        except:
            pass

        try:
            ar_pca.anomaly_score_option = 'log-likelihood-1'
            ar_pca.anomaly_score(test_class.dataframe)
        except:
            pass


    def test_with_numpy_dataset(self):
        """Test numpy dataset"""
        test_class = self.__class__
        ar_pca = AnomalyPCA(n_components=2)
        ar_pca.fit(test_class.numpy_array)
        prediction = ar_pca.decision_function(test_class.numpy_array)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertIsNotNone(outlier)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
