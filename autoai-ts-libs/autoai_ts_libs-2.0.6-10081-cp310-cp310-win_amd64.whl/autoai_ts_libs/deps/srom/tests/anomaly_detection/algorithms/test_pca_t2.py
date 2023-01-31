# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing AnomalyPCA_T2 class"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.pca_t2 import AnomalyPCA_T2

class TestAnomalyPCA_T2(unittest.TestCase):
    """Test methods in AnomalyPCA_T2 class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.samples = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
        cls.predict_samples = np.array([[-1, 0], [-1, 1], [3, 0], [1, 1], [1, -1], [1, 2]])

        # converting to pandas dataframes
        cls.samples_df = pd.DataFrame(cls.samples)
        cls.predict_samples_df = pd.DataFrame(cls.predict_samples)

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_set_params(self):
        """Test set params method"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        anomaly_pca_t2 = AnomalyPCA_T2()
        # fit without set params
        fitted_model = anomaly_pca_t2.fit(samples)
        self.assertEqual(id(fitted_model), id(anomaly_pca_t2))
        # fit with few arguments
        anomaly_pca_t2.set_params(variance_threshold=0.80)
        fitted_model = anomaly_pca_t2.fit(samples)
        self.assertEqual(id(fitted_model), id(anomaly_pca_t2))
        # fit with extra arguments
        anomaly_pca_t2.set_params(scale=False, variance_threshold=0.9, alpha=0.5, dummy='dummy')
        fitted_model = anomaly_pca_t2.fit(samples)
        self.assertEqual(id(fitted_model), id(anomaly_pca_t2))

        # predict without set params
        anomaly_pca_t2 = AnomalyPCA_T2()
        anomaly_pca_t2.fit(samples)
        scores = anomaly_pca_t2.predict(predict_samples)
        self.assertIsNotNone(scores)
        # predict with few argument
        anomaly_pca_t2.set_params(scale=False, alpha=0.5)
        anomaly_pca_t2.fit(samples)
        scores = anomaly_pca_t2.predict(samples)
        self.assertIsNotNone(scores)
        # predict with extra arguments
        anomaly_pca_t2.set_params(scale=False, variance_threshold=0.9, alpha=0.5, dummy='dummy')
        scores = anomaly_pca_t2.predict(samples)
        self.assertIsNotNone(scores)

    def test_fit_numpy_array(self):
        """Test fit numpy array"""
        test_class = self.__class__
        samples = test_class.samples
        anomaly_pca_t2 = AnomalyPCA_T2()
        # with scale False
        anomaly_pca_t2.set_params(scale=False)
        fitted_model = anomaly_pca_t2.fit(samples)
        self.assertEqual(id(fitted_model), id(anomaly_pca_t2))
        # with scale True
        anomaly_pca_t2.set_params(scale=True)
        fitted_model = anomaly_pca_t2.fit(samples)
        self.assertEqual(id(fitted_model), id(anomaly_pca_t2))

    def test_fit_pandas_dataframe(self):
        """Test fit pandas dataframe"""
        test_class = self.__class__
        samples_df = test_class.samples_df
        anomaly_pca_t2 = AnomalyPCA_T2()
        # with scale False
        anomaly_pca_t2.set_params(scale=False)
        fitted_model = anomaly_pca_t2.fit(samples_df)
        self.assertEqual(id(fitted_model), id(anomaly_pca_t2))
        # with scale True
        anomaly_pca_t2.set_params(scale=True)
        fitted_model = anomaly_pca_t2.fit(samples_df)
        self.assertEqual(id(fitted_model), id(anomaly_pca_t2))

    def test_predict_numpy_array(self):
        """Test predict numpy array"""
        test_class = self.__class__
        samples = test_class.samples
        predict_samples = test_class.predict_samples
        anomaly_pca_t2 = AnomalyPCA_T2()
        # predict without fit
        self.assertRaises(Exception, anomaly_pca_t2.predict, predict_samples)
        # with scale False
        anomaly_pca_t2.set_params(scale=False)
        anomaly_pca_t2.fit(samples)
        scores = anomaly_pca_t2.predict(predict_samples)
        self.assertIsNotNone(scores)
        # with scale True
        anomaly_pca_t2.set_params(scale=True)
        anomaly_pca_t2.fit(samples)
        scores = anomaly_pca_t2.predict(predict_samples)
        self.assertIsNotNone(scores)

    def test_predict_pandas_dataframe(self):
        """Test predict pandas dataframe"""
        test_class = self.__class__
        samples_df = test_class.samples_df
        predict_samples_df = test_class.predict_samples_df
        anomaly_pca_t2 = AnomalyPCA_T2()
        # predict without fit
        self.assertRaises(Exception, anomaly_pca_t2.predict, predict_samples_df)
        # with scale False
        anomaly_pca_t2.set_params(scale=False)
        anomaly_pca_t2.fit(samples_df)
        scores = anomaly_pca_t2.predict(predict_samples_df)
        self.assertIsNotNone(scores)
        # with scale True
        anomaly_pca_t2.set_params(scale=True)
        anomaly_pca_t2.fit(samples_df)
        scores = anomaly_pca_t2.predict(predict_samples_df)
        self.assertIsNotNone(scores)

    def test_anomaly_score(self):
        """Test anomaly score"""
        test_class = self.__class__
        samples = test_class.samples
        anomaly_pca_t2 = AnomalyPCA_T2()
        # without fit
        self.assertRaises(Exception, anomaly_pca_t2.anomaly_score, samples)
        # with fit
        anomaly_pca_t2.fit(samples)
        scores = anomaly_pca_t2.anomaly_score(samples)
        self.assertIsNotNone(scores)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
