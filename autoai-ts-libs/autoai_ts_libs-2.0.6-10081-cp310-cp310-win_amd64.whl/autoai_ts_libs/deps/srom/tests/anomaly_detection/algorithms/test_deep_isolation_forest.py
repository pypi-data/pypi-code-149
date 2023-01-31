import numpy as np
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.deep_isolation_forest import DeepIsolationForest
from sklearn import datasets


import os
import sys
import unittest

class TestDeepIsolationForest(unittest.TestCase):
    """Test class for testing DeepIsolationForest"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        iris = datasets.load_iris()
        X = iris.data[:, :2]  
        y = iris.target
        cls.testX, cls.testy = X, y
 
        cls.n_ensemble=50
        cls.n_estimators=6
        cls.max_samples=256
        cls.n_jobs=1
        cls.random_state=42
        cls.n_processes=15
        cls.batch_size=10000
        cls.device="cuda"
        cls.verbose=1
        # cls.network_args

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        deep_isolator = DeepIsolationForest(n_ensemble=test_class.n_ensemble,n_estimators=test_class.n_estimators,max_samples=test_class.max_samples,n_jobs=test_class.n_jobs,random_state=test_class.random_state,n_processes=test_class.n_processes,batch_size=test_class.batch_size,device=test_class.device)
        fitted_deep_isolator = deep_isolator.fit(test_class.testX)
        self.assertEqual(id(fitted_deep_isolator), id(deep_isolator))

    def test_predict(self):
        """Test Decision Function"""
        test_class = self.__class__
        deep_isolator = DeepIsolationForest(n_ensemble=test_class.n_ensemble,n_estimators=test_class.n_estimators,max_samples=test_class.max_samples,n_jobs=test_class.n_jobs,random_state=test_class.random_state,n_processes=test_class.n_processes,batch_size=test_class.batch_size,device=test_class.device)
        deep_isolator.fit(test_class.testX)
        score=deep_isolator.predict(test_class.testX)
        self.assertIsNotNone(score)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
