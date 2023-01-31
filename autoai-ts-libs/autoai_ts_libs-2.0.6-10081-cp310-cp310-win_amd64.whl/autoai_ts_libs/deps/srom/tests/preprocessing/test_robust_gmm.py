# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing TestRobustGMM class"""
import unittest
import copy
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.robust_GGM import RobustGGM


class TestRobustGGM(unittest.TestCase):
    """Test class for RobustGGM"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.X = np.arange(100, 109)

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        test_class = self.__class__
        gmm = RobustGGM(pho=0.1, lambda_=2)
        fitted_robust_gmm = gmm.fit(test_class.X.reshape(-1, 1))
        self.assertEqual(id(gmm), id(fitted_robust_gmm))

    def test_transform(self):
        test_class = self.__class__
        gmm = RobustGGM(pho=0.1, lambda_=2)
        fitted_robust_gmm = gmm.fit(test_class.X.reshape(-1, 3))
        self.assertIsNotNone(fitted_robust_gmm.transform(test_class.X.reshape(-1, 3)))

    def test_fit_transform(self):
        test_class = self.__class__
        gmm = RobustGGM(pho=0.1, lambda_=2)
        self.assertIsNotNone(gmm.fit_transform(test_class.X.reshape(-1, 3)))


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
