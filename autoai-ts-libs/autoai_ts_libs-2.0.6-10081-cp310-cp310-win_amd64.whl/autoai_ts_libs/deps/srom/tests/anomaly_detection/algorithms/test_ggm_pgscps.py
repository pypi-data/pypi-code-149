# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing GraphPgscps class"""

import unittest
import numpy as np
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms import GraphPgscps

class TestGraphPgscps(unittest.TestCase):
    """Test methods in GraphPgscps class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.samples = [[-2, -1], [-1, -1], [-1, -2], [1, 1], [1, 2], [2, 1], [5, 3], [-4, 2]]

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        samples = test_class.samples
        pgscps = GraphPgscps()
        fitted_model = pgscps.fit(samples)
        self.assertEqual(id(fitted_model), id(pgscps))

        self.assertEqual(round(pgscps.objective_function_value, 3), 4.631)
        self.assertEqual(np.around(pgscps.precision_, 4).tolist(),
                         [[0.1966, -0.1451], [-0.1451, 0.472]])
        self.assertEqual(np.around(pgscps.covariance_, 4).tolist(),
                         [[6.5778, 2.0215], [2.0215, 2.7399]])

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
