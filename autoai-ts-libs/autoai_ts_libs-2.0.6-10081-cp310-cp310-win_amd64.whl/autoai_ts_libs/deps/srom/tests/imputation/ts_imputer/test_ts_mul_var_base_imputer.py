# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM DQLearn : 20201159
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.
#

"""
Unit test cases for testing imputation scikit-like classes. We have tested for two datasets
"""

import unittest

import numpy as np
from autoai_ts_libs.deps.srom.imputation.ts_imputer.ts_mul_var_base_imputer import TSMulVarBaseImputer

from autoai_ts_libs.deps.srom.tests.imputation.ts_imputer.test_imputation_datasets import (
    initialize_air_gap_data_set,
    initialize_data_set,
    initialize_multivariate_data_set,
    initialize_timestamped_data_set,
)


class TestTSMulVarBaseImputer(unittest.TestCase):
    """Class for testing imputation."""

    @classmethod
    def setUpClass(cls):
        """Setup class for imputation checks."""
        # df = pd.read_csv("../../test_data/missing_mackey_glass.csv", index_col=[0])
        # cls.integer_series = df["Variable"]
        # df = pd.read_csv(
        #     "../../../test_data/missing_sample_data_with_timestamp.csv",
        #     parse_dates=["Date"],
        #     index_col=[0],
        # )
        # cls.timestamp_series2 = df["Variable"]
        df2 = initialize_data_set()
        cls.integer_series = df2["Variable"]
        df3 = initialize_timestamped_data_set()
        cls.timestamp_series = df3["Variable"]
        df4 = initialize_air_gap_data_set()
        cls.air_gap_series = df4["Variable"]
        X = initialize_multivariate_data_set()
        cls.multivariate_time_series = X

    @classmethod
    def tearDownClass(cls):
        """Teardown class for imputation checks."""
        pass

    def test_univariate_simple_base_imputer(self):
        """Tests univariate impute_base_imputer (forward)."""
        testclass = self.__class__
        X = testclass.integer_series
        X = X.to_numpy()
        X = np.reshape(X, (-1, 1))
        si = TSMulVarBaseImputer()
        result2 = si.fit_transform(X)
        self.assertTrue(result2.shape[0] == 10)
        self.assertTrue(result2[1] > 0.1)

        X = testclass.timestamp_series
        X = X.to_numpy()
        X = np.reshape(X, (-1, 1))
        base = TSMulVarBaseImputer()
        result3 = base.fit_transform(X)
        self.assertTrue(result3[2] > 0.1)

    def test_multivariate_time_series_base_imputer(self):
        """Tests multi-variate TSMulVarBaseImputer ((forward))"""
        testclass = self.__class__
        X = testclass.multivariate_time_series
        base = TSMulVarBaseImputer()
        result = base.fit_transform(X)
        self.assertTrue(result.shape[0] == 51)
        self.assertTrue(result[49, 1] > 100.0)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
