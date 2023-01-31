# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing AnomalyRobustPCA class"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_robust_pca import AnomalyRobustPCA


class TestAnomalyRobustPCA(unittest.TestCase):
    """Test methods in AnomalyRobustPCA class"""

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

        x_array = np.zeros(100)  # Numpy array containins 100 0's
        y_array = np.ones(100)  # Numpy array containins 100 1's
        z_array = np.ones(100)
        cls.dataframe1 = pd.DataFrame({"x": x_array, "y": y_array, "z": z_array})
        cls.numpy_array1 = cls.dataframe.values


    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        ar_pca = AnomalyRobustPCA()
        fitted_ar_pca = ar_pca.fit(test_class.dataframe)
        self.assertEqual(id(ar_pca), id(fitted_ar_pca))

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        ar_pca = AnomalyRobustPCA()
        ar_pca.fit(test_class.dataframe)
        prediction = ar_pca.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        # Outliers on index 50 and 75 are not flagged, we will try to tune parameters
        self.assertEqual([35, 45, 55, 80, 95], outlier)

        ar_pca = AnomalyRobustPCA(error_order=0.5)
        ar_pca.fit(test_class.dataframe)
        prediction = ar_pca.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        # Outlier on index 75 is not flagged, we will try to tune parameters further
        self.assertEqual([35, 45, 50, 55, 80, 95], outlier)

        ar_pca = AnomalyRobustPCA(error_order=0.5, anomaly_threshold=0.5)
        ar_pca.fit(test_class.dataframe)
        prediction = ar_pca.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        # Now all of the outliers are properly detected
        self.assertEqual([35, 45, 50, 55, 75, 80, 95], outlier)

    def test_anomaly_score_method(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        ar_pca = AnomalyRobustPCA()
        ar_pca.fit(test_class.dataframe)
        anomaly_scores = ar_pca.anomaly_score(test_class.dataframe)
        anomaly_scores = pd.DataFrame(anomaly_scores).apply(round)
        outlier = np.where(anomaly_scores > 0.0)[0].tolist()
        self.assertEqual([35, 45, 50, 55, 75, 80, 95], outlier)
        self.assertIsNotNone(ar_pca.decision_function(test_class.dataframe))
        
        ar_pca = AnomalyRobustPCA()
        ar_pca.fit(test_class.dataframe1)
        ar_pca.anomaly_score(test_class.dataframe1)

    def test_with_scaling(self):
        """Test with scaling"""
        test_class = self.__class__
        ar_pca = AnomalyRobustPCA(scale=True)
        ar_pca.fit(test_class.dataframe)
        prediction = ar_pca.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual([35, 45, 55, 80, 95], outlier)

    def test_with_numpy_dataset(self):
        """Test numpy dataset"""
        test_class = self.__class__
        ar_pca = AnomalyRobustPCA()
        ar_pca.fit(test_class.numpy_array)
        prediction = ar_pca.predict(test_class.numpy_array)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual([35, 45, 55, 80, 95], outlier)

    def test_predict_without_fit(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        ar_pca = AnomalyRobustPCA()
        self.assertRaises(Exception, ar_pca.predict, test_class.dataframe)

        # But if scale=True, fit call is required.
        ar_pca = AnomalyRobustPCA(scale=True)
        self.assertRaises(Exception, ar_pca.predict, test_class.dataframe)

    def test_set_params_method(self):
        """Test set_params method"""
        test_class = self.__class__
        ar_pca = AnomalyRobustPCA()
        ar_pca.set_params(scale=True, something_not_there=True)
        ar_pca.fit(test_class.dataframe)
        prediction = ar_pca.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual([35, 45, 55, 80, 95], outlier)

        ar_pca = AnomalyRobustPCA()
        ar_pca.set_params(something_not_there=True)
        ar_pca.fit(test_class.dataframe)
        prediction = ar_pca.predict(test_class.dataframe)
        outlier = np.where(prediction < 0.0)[0].tolist()
        self.assertEqual([35, 45, 55, 80, 95], outlier)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
