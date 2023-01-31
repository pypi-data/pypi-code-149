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

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.sparse_structure_learning import SparseStructureLearning


class TestSparseStructureLearning(unittest.TestCase):
    """Test methods in AnomalyPCA class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        x_array = np.random.uniform(size=(50,2))
        cls.dataframe = pd.DataFrame({"x": x_array[:,0],'x_1':x_array[:,1]})

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        ssl = SparseStructureLearning()
        fitted_ssl = ssl.fit(test_class.dataframe)
        self.assertEqual(id(ssl), id(fitted_ssl))

    def test_anomaly_score_method(self):
        """Test anomaly_score method"""
        test_class = self.__class__
        ssl = SparseStructureLearning()
        ssl.fit(test_class.dataframe)
        anomaly_scores = ssl.anomaly_score(test_class.dataframe)
        anomaly_scores = pd.DataFrame(anomaly_scores).apply(round)
        self.assertIsNotNone(anomaly_scores)



if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
