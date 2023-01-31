# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing NearestNeighborAnomalyModel class"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.nearest_neighbor import NearestNeighborAnomalyModel

class TestNearestNeighborAnomalyModel(unittest.TestCase):
    """Test methods in NearestNeighborAnomalyModel class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        rng = np.random.RandomState(42)
        # Generate train data
        X = 0.3 * rng.randn(100, 2)
        cls.x_train = np.r_[X + 2, X - 2]
        # Generate some regular novel observations
        X = 0.3 * rng.randn(20, 2)
        cls.x_test = np.r_[X + 2, X - 2]
        # Generate some abnormal novel observations
        cls.x_outliers = rng.uniform(low=-4, high=4, size=(20, 2))

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        ...

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        x_train = test_class.x_train
        nn_am = NearestNeighborAnomalyModel(n_neighbors=10)
        fitted_model = nn_am.fit(x_train)
        self.assertEqual(id(fitted_model), id(nn_am))
        self.assertTrue(-3.0 < fitted_model.train_mean < -1.5)
        self.assertTrue(0.25 < fitted_model.train_std < 0.5)

    def test_predict(self):
        """Test predict method"""
        test_class = self.__class__
        x_train = test_class.x_train
        x_test = test_class.x_test
        x_outliers = test_class.x_outliers
        nn_am = NearestNeighborAnomalyModel(n_neighbors=10)
        nn_am.fit(x_train)
        # Normal data must be predicted as non outlier - 0
        self.assertTrue(np.array_equal(nn_am.predict(x_test[:3]), np.array([1., 1., 1.])))
        # Outlier must be predicted as 1
        self.assertTrue(np.array_equal(nn_am.predict(x_outliers[:3]), np.array([-1.0, -1.0, -1.0])))

    def test_predict_exceptions(self):
        """Test predict exceptions"""
        # If model is not fitted then exception is raise
        nn_am = NearestNeighborAnomalyModel()
        self.assertRaises(RuntimeError, nn_am.predict, self.x_train)

    def test_anomaly_score(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        x_train = test_class.x_train
        x_test = test_class.x_test
        x_outliers = test_class.x_outliers
        nn_am = NearestNeighborAnomalyModel(n_neighbors=10)
        nn_am.fit(x_train)
        # Mean of scores for outlier data will be higher than that of normal data
        self.assertGreater(nn_am.anomaly_score(x_outliers).mean(),
                           nn_am.anomaly_score(x_test).mean())

    def test_set_params(self):
        """Test set_params method"""
        nn_am = NearestNeighborAnomalyModel()
        nn_am.set_params(n_neighbors=5)
        self.assertEqual(nn_am.n_neighbors, 5)
        self.assertEqual(nn_am.model.get_params()['n_neighbors'], 5)
        nn_am.set_params(anomaly_threshold=5)
        self.assertEqual(nn_am.anomaly_threshold, 5)
        nn_am.set_params(n_neighbors=10, anomaly_threshold=10)
        self.assertEqual(nn_am.n_neighbors, 10)
        self.assertEqual(nn_am.anomaly_threshold, 10)

    def test_using_pandas_data(self):
        """Test using pandas data as an input"""
        test_class = self.__class__
        x_train = pd.DataFrame(test_class.x_train)
        x_test = pd.DataFrame(test_class.x_test)
        x_outliers = pd.DataFrame(test_class.x_outliers)
        nn_am = NearestNeighborAnomalyModel(n_neighbors=10)
        nn_am.fit(x_train)
        # Normal data must be predicted as non outlier - 0
        self.assertTrue(np.array_equal(nn_am.predict(x_test[:3]), np.array([1.0, 1.0, 1.0])))
        # Outlier must be predicted as 1
        self.assertTrue(np.array_equal(nn_am.predict(x_outliers[:3]), np.array([-1.0, -1.0, -1.0])))
        # Mean of scores for outlier data will be higher than that of normal data
        self.assertGreater(nn_am.anomaly_score(x_outliers).mean(),
                           nn_am.anomaly_score(x_test).mean())

    def test_init_combinations(self):
        """Test using different combinations of init parameters"""
        test_class = self.__class__
        x_train = test_class.x_train
        x_outliers = test_class.x_outliers
        nn_am1 = NearestNeighborAnomalyModel(n_neighbors=10, anomaly_threshold=2.0)
        nn_am2 = NearestNeighborAnomalyModel(n_neighbors=10, anomaly_threshold=7)
        nn_am1.fit(x_train)
        nn_am2.fit(x_train)
        # nn_am1 should predict more outlier than nn_am2, because of less strict threshold
        self.assertGreater(nn_am2.predict(x_outliers).sum(),nn_am1.predict(x_outliers).sum())

        nn_am1 = NearestNeighborAnomalyModel(n_neighbors=10, anomaly_threshold=7)
        nn_am2 = NearestNeighborAnomalyModel(n_neighbors=3, anomaly_threshold=7)
        nn_am1.fit(x_train)
        nn_am2.fit(x_train)
        # Larger value of n_neighbors should reduces effect of the noise
        self.assertGreater(nn_am2.predict(x_outliers).sum(),nn_am1.predict(x_outliers).sum())

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
