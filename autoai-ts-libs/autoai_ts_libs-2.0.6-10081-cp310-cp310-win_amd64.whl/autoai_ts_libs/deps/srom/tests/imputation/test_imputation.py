# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import unittest
import numpy as np
import pandas as pd
from warnings import simplefilter
from math import ceil

from sklearn.impute import SimpleImputer
from autoai_ts_libs.deps.srom.imputation.pipeline_utils import ImputationKFold


class TestImputation(unittest.TestCase):
    """Test methods for data imputation"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        simplefilter(action="ignore", category=FutureWarning)
        simplefilter(action="ignore", category=DeprecationWarning)
        simplefilter(action="ignore", category=UserWarning)
        simplefilter(action="ignore", category=RuntimeWarning)
        simplefilter(action="ignore", category=UserWarning)
        X = pd.read_csv("./datasets/banana.csv")
        cls.features, cls.labels = (
            X[["c1", "c2"]].values,
            X[["label"]].values.reshape(-1, 1),
        )  # read in data

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_data(self):
        np_features = self.features
        x, y = np_features.shape
        self.assertTrue(x > 1 and y > 1)
        test_missing_data(self)

    def test_simple_imputers_fit(self):
        test_missing_data(self, imputer=SimpleImputer(strategy="mean"))
        test_missing_data(self, imputer=SimpleImputer(strategy="median"))
        test_missing_data(self, imputer=SimpleImputer(strategy="most_frequent"))

    def test_simple_imputers_fit_transform(self):
        test_missing_data(self, imputer=SimpleImputer(strategy="mean"), transform=True)
        test_missing_data(
            self, imputer=SimpleImputer(strategy="median"), transform=True
        )
        test_missing_data(
            self, imputer=SimpleImputer(strategy="most_frequent"), transform=True
        )


def test_missing_data(test_imputation, imputer=None, transform=False):
    impute_size = 0.1  # proportion of data points to delete to test imputers
    imputation_kfold = ImputationKFold(
        n_iteration=5, impute_size=impute_size, random_state=7
    )
    gen = imputation_kfold.split(test_imputation.features)
    for array1, array2 in gen:
        expected_deleted = ceil(impute_size * array1.size)
        num_deleted = np.count_nonzero(np.isnan(array1))
        num_missing_original = np.count_nonzero(np.isnan(array2))
        test_imputation.assertEqual(num_deleted, expected_deleted)
        test_imputation.assertEqual(num_missing_original, 0)
        if imputer is not None:
            if transform:
                imputed_array = imputer.fit_transform(array1)
                num_missing_imputed = np.count_nonzero(np.isnan(imputed_array))
                test_imputation.assertEqual(num_missing_imputed, 0)
            else:
                imputer2 = imputer.fit(array1)
                test_imputation.assertEqual(imputer, imputer2)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
