# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import unittest
import numpy as np
from warnings import simplefilter
import copy

from sklearn.impute import SimpleImputer
from autoai_ts_libs.deps.srom.imputation.pipeline_utils import ImputationKFold
from autoai_ts_libs.deps.srom.imputation.metrics import r2_imputation_score

from autoai_ts_libs.deps.srom.imputation.pipeline_utils import cross_validate_impute
from autoai_ts_libs.deps.srom.imputation.pipeline_utils import cross_val_score_impute


def initialize_dataset():
    val = np.array(
        [
            [1.14e00, -1.14e-01],
            [-1.52e00, -1.15e00],
            [-1.05e00, 7.20e-01],
            [-9.16e-01, 3.97e-01],
            [-1.09e00, 4.37e-01],
            [-5.84e-01, 9.37e-02],
            [1.83e00, 4.52e-01],
            [-1.25e00, -2.86e-01],
            [1.70e00, 1.21e00],
            [-4.82e-01, -4.85e-01],
            [1.79e00, -4.59e-01],
            [-1.22e-01, -8.08e-01],
            [8.09e-02, 1.93e00],
            [-5.41e-01, -3.32e-01],
            [-1.02e00, 6.19e-01],
            [-7.68e-01, -1.04e00],
            [-1.69e00, -4.61e-02],
            [1.26e00, 1.21e00],
            [7.24e-01, 9.89e-01],
            [4.44e-01, 1.99e00],
            [-1.01e00, -1.36e00],
            [-8.63e-01, 4.96e-01],
            [1.16e00, -4.58e-01],
            [-5.95e-01, -6.51e-01],
            [-7.70e-01, 3.64e-01],
            [-8.71e-01, -8.25e-01],
            [9.96e-01, -1.70e00],
            [1.28e00, 6.91e-01],
            [9.25e-01, 8.95e-01],
            [-6.87e-01, -1.29e00],
            [1.74e00, 9.64e-01],
            [1.18e00, -3.35e-01],
            [2.52e00, 1.43e00],
            [1.71e00, -4.40e-02],
            [2.71e-01, -5.91e-01],
            [1.12e00, 6.26e-01],
            [1.30e00, 1.96e-01],
            [-1.59e00, -6.80e-01],
            [4.08e-01, 6.73e-02],
            [1.13e00, 1.48e00],
            [7.63e-01, 9.21e-01],
            [-1.41e00, 1.11e00],
            [-7.50e-01, -8.81e-01],
            [1.16e00, 9.78e-01],
            [1.13e00, 4.05e-01],
            [-5.22e-01, -1.34e00],
            [-1.41e00, 8.94e-01],
            [9.02e-03, -4.34e-01],
            [-2.14e00, -1.43e00],
            [-1.31e00, 1.25e00],
            [4.10e-02, -1.13e00],
            [4.83e-02, 8.66e-01],
            [-2.11e00, 1.93e-01],
            [5.22e-01, 1.46e00],
            [2.84e-02, 1.62e00],
            [3.96e-01, -6.06e-01],
            [5.36e-01, 9.21e-01],
            [3.15e-01, -1.82e-01],
            [-1.23e-01, -1.07e00],
            [5.26e-01, 1.48e00],
            [6.65e-03, 1.18e-02],
            [-3.52e-01, -4.90e-01],
            [-7.01e-02, -1.23e00],
            [-1.49e-01, -1.20e00],
            [7.85e-01, 4.81e-02],
            [-1.62e00, 5.93e-01],
            [-3.14e-02, -1.01e00],
            [-2.85e-01, -1.10e00],
            [1.33e00, 1.51e00],
            [1.09e00, -1.37e00],
            [-2.23e-01, -1.28e00],
            [-3.41e-02, -1.07e00],
            [1.22e00, 1.13e00],
            [-1.67e00, -1.26e00],
            [1.97e00, -7.72e-01],
            [-5.08e-01, -7.15e-01],
            [6.03e-01, -1.08e-01],
            [-3.23e-01, -2.13e-01],
            [-1.24e-01, -1.12e00],
            [-4.39e-01, -9.61e-01],
            [2.01e-01, 2.40e-03],
            [8.12e-01, 7.08e-01],
            [8.88e-01, 8.17e-01],
            [2.38e-02, 8.36e-02],
            [4.15e-01, -1.00e00],
            [-3.08e-01, 2.19e00],
            [7.67e-01, -2.48e-01],
            [1.23e00, -1.20e00],
            [1.33e00, 1.63e00],
            [2.70e-01, 4.91e-02],
            [-1.69e00, -1.87e00],
            [4.95e-01, -2.81e-01],
            [-5.19e-01, -7.99e-01],
            [-1.99e00, 5.49e-01],
            [1.36e00, -7.32e-01],
            [-1.03e00, 6.54e-01],
            [4.31e-01, -1.33e00],
            [-5.83e-02, -1.15e00],
            [-2.09e-01, 3.45e-01],
            [1.26e00, -1.37e00],
            [-1.78e00, -3.78e-01],
            [9.80e-01, -4.39e-02],
            [-5.36e-02, 1.60e00],
            [-1.39e00, -4.51e-01],
            [1.22e00, -3.61e-01],
            [1.22e00, 5.61e-01],
            [-8.38e-01, 3.56e-01],
            [-4.46e-01, -8.61e-01],
            [1.17e00, -1.39e00],
            [-8.68e-02, -1.33e00],
            [-1.12e00, 5.76e-01],
            [-2.80e-01, -1.30e00],
            [-2.69e-02, 9.58e-01],
            [-6.97e-01, 1.35e00],
            [1.38e00, -1.74e00],
            [4.08e-01, 1.16e00],
            [1.20e00, 1.54e00],
            [2.07e00, 1.02e00],
            [-4.62e-01, -1.87e-01],
            [1.27e00, 5.89e-01],
            [-1.01e-01, -7.65e-01],
            [-8.19e-01, 1.26e00],
            [6.15e-01, -2.28e-02],
            [-1.79e00, -9.80e-01],
            [-1.79e00, -9.54e-01],
            [8.26e-01, 1.50e00],
            [8.45e-01, 7.66e-01],
            [-4.76e-01, -1.49e00],
            [1.01e00, 4.80e-01],
            [1.39e00, -3.76e-01],
            [3.57e-01, -1.07e00],
            [7.70e-01, 1.40e00],
            [-1.08e00, 1.14e-01],
            [-7.95e-01, -1.43e00],
            [7.06e-01, 1.38e00],
            [-1.26e00, 2.30e-01],
            [-8.33e-01, -5.69e-01],
            [-3.03e-02, 2.11e00],
            [-2.23e-01, -4.19e-01],
            [-5.62e-01, -8.73e-01],
            [9.26e-01, 9.72e-01],
            [-1.86e00, -1.57e00],
            [-8.06e-01, 9.41e-01],
            [-2.14e-01, 3.80e-01],
            [7.44e-01, 1.42e00],
            [1.94e00, -6.50e-01],
            [1.77e00, 1.35e00],
            [-9.03e-01, 1.01e-01],
            [-4.18e-02, -1.02e00],
            [3.09e-01, -1.75e-01],
            [-6.34e-01, -9.69e-01],
            [-1.62e00, 1.02e-01],
            [-1.21e00, 1.27e00],
            [5.29e-01, 1.33e-01],
            [3.86e-01, 1.55e00],
            [-9.62e-02, 1.90e-01],
            [-5.36e-01, 1.13e00],
            [1.02e00, -2.61e-01],
            [-8.76e-01, -1.00e00],
            [2.35e00, 1.21e00],
            [-9.82e-01, -1.08e00],
            [-1.16e00, 4.69e-01],
            [-1.74e00, 6.93e-01],
            [-1.10e00, 1.16e00],
            [1.79e-02, -7.00e-01],
            [-6.20e-01, -9.84e-01],
            [-1.52e00, 6.60e-01],
            [1.07e00, -9.85e-01],
            [9.17e-01, 5.25e-01],
            [-4.82e-02, 1.52e00],
            [1.49e00, 1.55e00],
            [-5.84e-01, 1.01e00],
            [-6.25e-02, -1.20e-01],
            [-1.68e00, 1.08e00],
            [-1.77e00, -9.23e-01],
            [-2.02e-01, 7.12e-01],
            [1.06e00, -4.27e-01],
            [1.71e00, 1.10e00],
            [-1.70e00, 8.72e-01],
            [1.86e00, 1.14e00],
            [-5.29e-01, -3.57e-01],
            [-4.11e-01, -1.30e00],
            [6.66e-01, 1.36e00],
            [1.62e-01, -7.91e-01],
            [-2.96e-01, 2.55e-01],
            [-3.47e-02, 1.30e00],
            [2.94e-01, -1.50e00],
            [-5.20e-01, -1.17e00],
            [7.41e-01, -1.20e00],
            [-1.33e00, 1.08e00],
            [-9.87e-02, 9.66e-01],
            [1.31e-02, -9.69e-01],
            [8.96e-01, 1.58e00],
            [-4.12e-01, 4.92e-01],
            [6.83e-01, 1.07e00],
            [-7.53e-01, -6.15e-02],
            [-6.74e-02, 1.85e00],
            [1.08e00, 6.83e-01],
            [1.15e00, 2.43e-01],
            [4.97e-01, -6.71e-01],
        ]
    )
    return val


class TestCVScoresPipelineUtils(unittest.TestCase):
    """Test methods for data imputation"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        simplefilter(action="ignore", category=FutureWarning)
        simplefilter(action="ignore", category=DeprecationWarning)
        simplefilter(action="ignore", category=UserWarning)
        simplefilter(action="ignore", category=RuntimeWarning)
        simplefilter(action="ignore", category=UserWarning)
        cls.X = initialize_dataset()

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_cross_validate_impute(self):
        """ Test cross_validate_impute """
        test_class = self.__class__
        X_master = test_class.X

        X = copy.deepcopy(X_master)
        estimator = SimpleImputer(strategy="mean")

        iterations = 3
        missing_vals = 0.1
        RANDOM_STATE = 7

        cv = ImputationKFold(
            n_iteration=iterations, impute_size=missing_vals, random_state=RANDOM_STATE
        )

        result = cross_validate_impute(
            estimator=estimator, X=X, cv=cv, scoring=r2_imputation_score
        )
        # print(result["test_score"])
        self.assertAlmostEqual(result["test_score"][0], 0.9023196, 2)

    def test_cross_val_score_impute(self):
        """ Test cross_val_score_impute """
        test_class = self.__class__
        X_master = test_class.X

        X = copy.deepcopy(X_master)
        estimator = SimpleImputer(strategy="mean")

        iterations = 3
        missing_vals = 0.1
        RANDOM_STATE = 7

        cv = ImputationKFold(
            n_iteration=iterations, impute_size=missing_vals, random_state=RANDOM_STATE
        )

        result = cross_val_score_impute(
            estimator=estimator, X=X, cv=cv, scoring=r2_imputation_score
        )
        # print(result)
        self.assertAlmostEqual(result[1], 0.88228585, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
