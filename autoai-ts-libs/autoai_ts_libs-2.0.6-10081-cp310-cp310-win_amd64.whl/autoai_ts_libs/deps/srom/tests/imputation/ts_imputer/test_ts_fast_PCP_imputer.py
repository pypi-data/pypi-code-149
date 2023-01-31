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
from autoai_ts_libs.deps.srom.imputation.ts_imputer.ts_fast_PCP_imputer import TSFastPCPImputer

from autoai_ts_libs.deps.srom.tests.imputation.ts_imputer.test_imputation_datasets import (
    initialize_air_gap_data_set,
    initialize_data_set,
    initialize_timestamped_data_set,
)


class TestTSFastPCPImputer(unittest.TestCase):
    """Class for testing imputation."""

    @classmethod
    def setUpClass(cls):
        """Setup class for imputation checks."""
        df2 = initialize_data_set()
        cls.integer_series = df2["Variable"]
        df3 = initialize_timestamped_data_set()
        cls.timestamp_series = df3["Variable"]
        df4 = initialize_air_gap_data_set()
        cls.air_gap_series = df4["Variable"]

    @classmethod
    def tearDownClass(cls):
        """Teardown class for imputation checks."""
        pass

    def test_impute_fastpcp(self):
        """Tests impute_fastpcp."""
        testclass = self.__class__
        X = testclass.integer_series
        X = X.to_numpy()
        X = np.reshape(X, (-1, 1))
        fast = TSFastPCPImputer()
        result2 = fast.fit_transform(X)
        self.assertTrue(result2.shape[0] == 10)
        self.assertTrue(result2[1] > 0.1)

        X = testclass.timestamp_series
        X = X.to_numpy()
        X = np.reshape(X, (-1, 1))
        fast = TSFastPCPImputer()
        result3 = fast.fit_transform(X)
        self.assertTrue(result3[2] > 0.1)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
