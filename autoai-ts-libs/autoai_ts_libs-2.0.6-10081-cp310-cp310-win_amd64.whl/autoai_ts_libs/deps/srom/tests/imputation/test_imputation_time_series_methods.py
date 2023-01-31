# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import unittest
from pandas import read_csv
import pandas as pd
import numpy as np
from warnings import simplefilter

from autoai_ts_libs.deps.srom.imputation.imputation_time_series import ImputationTimeSeries as imp


class TestImputationTimeSeries(unittest.TestCase):
    """Test methods for data imputation"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        simplefilter(action="ignore", category=FutureWarning)
        simplefilter(action="ignore", category=DeprecationWarning)
        simplefilter(action="ignore", category=UserWarning)
        simplefilter(action="ignore", category=RuntimeWarning)
        simplefilter(action="ignore", category=UserWarning)
        cls.input_df = get_input_data()  # read in data

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_imputer_linear(self):
        test_imputer(self, imp.linear, "linear")

    def test_imputer_time(self):
        test_imputer(self, imp.time, "time")

    def test_imputer_index(self):
        test_imputer(self, imp.index, "index")

    def test_interpolator_quadratic(self):
        test_interpolator(self, "quadratic")

    def test_interpolator_nearest(self):
        test_interpolator(self, "nearest")

    def test_interpolator_spline(self):
        test_interpolator(self, "spline", order=4)


def get_input_data():
    input_file = "./datasets/assetAD_time_series.csv"
    df = read_csv(input_file)
    datetime_label = list(df)[0]
    df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], format="%Y-%m-%d")
    return df.set_index(datetime_label)


def verify_values(test_imputer_ts, df_output, type):
    test_imputer_ts.assertTrue(np.isnan(test_imputer_ts.input_df.iloc[74, 0]))
    test_imputer_ts.assertTrue(np.isnan(test_imputer_ts.input_df.iloc[74, 1]))
    test_imputer_ts.assertTrue(np.isnan(test_imputer_ts.input_df.iloc[74, 2]))
    test_imputer_ts.assertGreater(df_output.iloc[74, 0], 0)
    test_imputer_ts.assertGreater(df_output.iloc[74, 1], 0)
    test_imputer_ts.assertGreater(df_output.iloc[74, 2], 0)


def test_imputer(test_imputer_ts, imputer, description):
    df_output = imputer(test_imputer_ts.input_df)
    verify_values(test_imputer_ts, df_output, description)


def test_interpolator(test_imputer_ts, description, **kwargs):
    df_output = test_imputer_ts.input_df.interpolate(description, **kwargs)
    verify_values(test_imputer_ts, df_output, description)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
