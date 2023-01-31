# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing classes under utils.py"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.optimization.nlopt.utils import todf, concatbyrow


class TestUtils(unittest.TestCase):
    """Test class for methods under utils.py"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        pass

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_todf_method(self):
        """test todf method"""
        df = todf(np.array([0, 1]), ["a", "b"])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.columns.tolist(), ["a", "b"])
        self.assertEqual(df.a.tolist(), [0])
        self.assertEqual(df.b.tolist(), [1])

    def test_concatbyrow_method(self):
        """test concatbyrow method"""
        df1 = pd.DataFrame({"a": [0], "b": [1]})
        df2 = pd.DataFrame({"c": [3], "d": [4]})
        df = concatbyrow(df1, df2, df1.columns.tolist(), df2.columns.tolist())
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.columns.tolist(), ["a", "b", "c", "d"])
        self.assertEqual(df.a.tolist(), [0])
        self.assertEqual(df.b.tolist(), [1])
        self.assertEqual(df.c.tolist(), [3])
        self.assertEqual(df.d.tolist(), [4])
