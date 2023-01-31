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
from sklearn.exceptions import NotFittedError
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.lof_nearest_neighbor import LOFNearestNeighborAnomalyModel

class TestLOFNearestNeighborAnomalyModel(unittest.TestCase):
    """Test methods in LOFNearestNeighborAnomalyModel class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.samples = [[-2, -1], [-1, -1], [-1, -2], [1, 1], [1, 2], [2, 1], [5, 3], [-4, 2]]
        cls.n_neighbors = 5

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        samples = test_class.samples
        n_neighbors = test_class.n_neighbors
        lofnn_am = LOFNearestNeighborAnomalyModel(n_neighbors=n_neighbors)
        fitted_model = lofnn_am.fit(samples)
        self.assertEqual(id(fitted_model), id(lofnn_am))

    def test_fit_exceptions(self):
        """Test fit exceptions"""
        # If model is None then exception is raise
        test_class = self.__class__
        samples = test_class.samples
        n_neighbors = test_class.n_neighbors
        lofnn_am = LOFNearestNeighborAnomalyModel(n_neighbors=n_neighbors)
        lofnn_am.model = None
        self.assertRaises(RuntimeError, lofnn_am.fit, samples)

    def test_predict_exceptions(self):
        """Test predict exceptions"""
        # If model is None then exception is raise
        test_class = self.__class__
        samples = test_class.samples
        n_neighbors = test_class.n_neighbors
        lofnn_am = LOFNearestNeighborAnomalyModel(n_neighbors=n_neighbors)
        self.assertRaises(NotFittedError, lofnn_am.predict, samples)
        lofnn_am.model = None
        self.assertRaises(RuntimeError, lofnn_am.predict, samples)

    def test_anomaly_score_exceptions(self):
        """Test anomaly_score exceptions"""
        # If model is None then exception is raise
        test_class = self.__class__
        samples = test_class.samples
        n_neighbors = test_class.n_neighbors
        lofnn_am = LOFNearestNeighborAnomalyModel(n_neighbors=n_neighbors)
        self.assertRaises(NotFittedError, lofnn_am.anomaly_score, samples)
        lofnn_am.model = None
        self.assertRaises(RuntimeError, lofnn_am.anomaly_score, samples)

    def test_predict(self):
        """Test predict method"""
        test_class = self.__class__
        samples = test_class.samples
        n_neighbors = test_class.n_neighbors
        lofnn_am = LOFNearestNeighborAnomalyModel(n_neighbors=n_neighbors)
        lofnn_am.fit(samples)
        prediction = lofnn_am.predict([[3, 5]])
        self.assertEqual(round(prediction.tolist()[0], 3), -1.0)
        prediction = lofnn_am.predict([[1, -2]])
        self.assertEqual(round(prediction.tolist()[0], 3), 1.0)

    def test_anomaly_score(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        samples = test_class.samples
        n_neighbors = test_class.n_neighbors
        lofnn_am = LOFNearestNeighborAnomalyModel(n_neighbors=n_neighbors)
        lofnn_am.fit(samples)

        anomaly_score = lofnn_am.anomaly_score([[3, 6]])
        self.assertAlmostEqual(round(anomaly_score.tolist()[0], 3), 0.135, delta=1.0)

        anomaly_score = lofnn_am.anomaly_score([[1, -2]])
        self.assertAlmostEqual(round(anomaly_score.tolist()[0], 3), -0.216, delta=1.0)

    def test_set_params(self):
        """Test set_params method"""
        test_class = self.__class__
        samples = test_class.samples
        lofnn_am = LOFNearestNeighborAnomalyModel()
        lofnn_am.set_params(n_neighbors=5, algorithm='auto', leaf_size=30, metric='minkowski',
                            p=2, metric_params=None, contamination=0.1, n_jobs=1)
        lofnn_am.fit(samples)

        prediction = lofnn_am.predict([[3, 5]])
        self.assertEqual(round(prediction.tolist()[0], 3), -1.0)

        prediction = lofnn_am.predict([[1, -2]])
        self.assertEqual(round(prediction.tolist()[0], 3), 1.0)

        #Set no params i.e. default params
        lofnn_am = LOFNearestNeighborAnomalyModel()
        samples = np.eye(10, 2)
        lofnn_am.set_params()
        lofnn_am.fit(samples)
        prediction = lofnn_am.predict([[1, 1]])
        self.assertEqual(round(prediction.tolist()[0], 3), -1.0)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
