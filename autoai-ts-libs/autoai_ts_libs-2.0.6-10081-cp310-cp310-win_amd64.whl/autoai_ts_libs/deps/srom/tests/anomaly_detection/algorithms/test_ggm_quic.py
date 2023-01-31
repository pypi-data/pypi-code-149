# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing GraphQUIC class"""
import unittest
import numpy as np

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.ggm_quic import GraphQUIC

class TestGraphQUIC(unittest.TestCase):
    """Test methods in GraphQUIC class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.samples = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        samples = test_class.samples
        graph_quic = GraphQUIC()
        fitted_graph_quic = graph_quic.fit(samples)
        self.assertEqual(id(fitted_graph_quic), id(graph_quic))
        self.assertEqual(np.around(fitted_graph_quic.precision_, 4).tolist(),
                         [[1.3132, -1.8135], [-1.8135, 2.9806]])
        self.assertEqual(np.around(fitted_graph_quic.covariance_, 4).tolist(),
                         [[4.7665, 2.9001], [2.9001, 2.1001]])

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
