# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing methods in dataframe_scaler file"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.dataframe_scaler import standard_scaler, min_max_scaler

class TestDataframeScaler(unittest.TestCase):
    """Test methods in dataframe_scaler file"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.sample_data = [[0, 0], [0, 0], [1, 1], [1, 1]]
        cls.sample_df = pd.DataFrame(cls.sample_data)

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_standard_scaler(self):
        """Test standard_scaler method"""
        test_class = self.__class__
        sample_data = test_class.sample_data
        sample_df = test_class.sample_df
        expected_std_scaler = [[-1.0, -1.0], [-1.0, -1.0], [1.0, 1.0], [1.0, 1.0]]
        output_df = standard_scaler(sample_df)
        self.assertTrue(np.array_equal(expected_std_scaler, output_df))

    def test_standard_scaler_exceptions(self):
        """Test standard_scaler method for exceptions"""
        test_class = self.__class__
        sample_data = test_class.sample_data
        # With empty dataframe
        empty_df = pd.DataFrame([])
        self.assertRaises(ValueError, standard_scaler, empty_df)
        # With numpy array
        self.assertRaises(AttributeError, standard_scaler, sample_data)

    def test_min_max_scaler(self):
        """Test min_max_scaler method"""
        test_class = self.__class__
        sample_data = test_class.sample_data
        sample_df = test_class.sample_df
        expected_min_max_scaler = [[0.0, 0.0], [0.0, 0.0], [1.0, 1.0], [1.0, 1.0]]
        output_df = min_max_scaler(sample_df)
        self.assertTrue(np.array_equal(expected_min_max_scaler, output_df))

    def test_min_max_scaler_exceptions(self):
        """Test min_max_scaler method for exceptions"""
        test_class = self.__class__
        sample_data = test_class.sample_data
        # With empty dataframe
        empty_df = pd.DataFrame([])
        self.assertRaises(ValueError, min_max_scaler, empty_df)
        # With numpy array
        self.assertRaises(AttributeError, min_max_scaler, sample_data)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
