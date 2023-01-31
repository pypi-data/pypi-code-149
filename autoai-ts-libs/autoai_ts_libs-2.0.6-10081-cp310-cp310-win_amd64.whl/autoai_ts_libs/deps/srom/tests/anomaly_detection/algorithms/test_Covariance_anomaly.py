# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing CovarianceAnomaly class"""
import unittest
import numpy as np
import pandas as pd

np.random.seed(0)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.covariance_anomaly import CovarianceAnomaly
from sklearn.covariance import EllipticEnvelope


class TestCovarianceAnomaly(unittest.TestCase):
    """Test methods in CovarianceAnomaly class"""

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
        cov_anomaly = CovarianceAnomaly()
        fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
        self.assertEqual(id(fitted_cov_anomaly), id(cov_anomaly))
        slide_cov_anomaly = CovarianceAnomaly(base_learner="slide_covariance")
        fitted_slide_cov_anomaly = slide_cov_anomaly.fit(test_class.dataframe)
        self.assertEqual(id(fitted_slide_cov_anomaly), id(slide_cov_anomaly))
        cov_anomaly = CovarianceAnomaly(base_learner="slide_covariance")
        with self.assertRaises(Exception):
            cov_anomaly.fit(test_class.dataframe[10:14])
        cov_anomaly = CovarianceAnomaly(base_learner=EllipticEnvelope())
        fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
        self.assertEqual(id(fitted_cov_anomaly), id(cov_anomaly))

    def test_wrong_base_learner(self):
        """Test wrong base method"""
        test_class = self.__class__
        cov_anomaly = CovarianceAnomaly(base_learner="pn")
        try:
            fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
        except Exception as ex:
            print (ex)
            pass
        


    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        cov_anomaly = CovarianceAnomaly(lookback_win=10)
        fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
        prediction = fitted_cov_anomaly.predict(test_class.dataframe)
        self.assertEqual(prediction.shape, test_class.dataframe.shape)

    def test_with_numpy_dataset(self):
        """Test numpy dataset"""
        test_class = self.__class__
        cov_anomaly = CovarianceAnomaly()
        fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
        prediction = fitted_cov_anomaly.predict(test_class.dataframe.values)
        self.assertEqual(prediction.shape, test_class.dataframe.shape)
        
        cov_anomaly = CovarianceAnomaly(distance_metric="logdet")
        fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
        prediction = fitted_cov_anomaly.predict(test_class.dataframe.values)
        self.assertEqual(prediction.shape, test_class.dataframe.shape)

        try:
            cov_anomaly = CovarianceAnomaly(distance_metric="riemannian",lookback_win=10)
            fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
            prediction = fitted_cov_anomaly.predict(test_class.dataframe.values)
        except:
            pass


        try:
            cov_anomaly = CovarianceAnomaly(distance_metric="kullback",lookback_win=10)
            fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
            prediction = fitted_cov_anomaly.predict(test_class.dataframe.values)
        except:
            pass

        try:
            cov_anomaly = CovarianceAnomaly(distance_metric="kullback1")
            fitted_cov_anomaly = cov_anomaly.fit(test_class.dataframe)
            prediction = fitted_cov_anomaly.predict(test_class.dataframe.values)
        except:
            pass


    def test_predict_without_fit(self):
        """Test predict method without calling fit method"""
        test_class = self.__class__
        cov_anomaly = CovarianceAnomaly()
        self.assertRaises(Exception, cov_anomaly.predict, test_class.dataframe)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
