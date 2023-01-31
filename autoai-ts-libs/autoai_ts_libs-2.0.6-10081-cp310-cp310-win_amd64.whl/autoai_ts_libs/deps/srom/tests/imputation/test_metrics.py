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
from autoai_ts_libs.deps.srom.imputation.metrics import (
    mean_absolute_imputation_score,
    mean_squared_imputation_score,
    mean_squared_log_imputation_score,
    median_absolute_imputation_score,
    r2_imputation_score,
)


def initialize_dataset_with_missing():
    val = np.array(
        [
            [1.14e00, -1.14e-01],
            [-1.52e00, -1.15e00],
            [-1.05e00, 7.20e-01],
            [-9.16e-01, 3.97e-01],
            [np.nan, 4.37e-01],
            [-5.84e-01, np.nan],
            [1.83e00, 4.52e-01],
            [-1.25e00, -2.86e-01],
            [1.70e00, 1.21e00],
            [-4.82e-01, -4.85e-01],
            [np.nan, -4.59e-01],
            [-1.22e-01, -8.08e-01],
            [8.09e-02, 1.93e00],
            [-5.41e-01, -3.32e-01],
            [-1.02e00, np.nan],
            [-7.68e-01, -1.04e00],
            [-1.69e00, -4.61e-02],
            [1.26e00, 1.21e00],
            [7.24e-01, np.nan],
            [4.44e-01, 1.99e00],
            [-1.01e00, -1.36e00],
            [-8.63e-01, 4.96e-01],
            [np.nan, np.nan],
            [-5.95e-01, -6.51e-01],
            [-7.70e-01, 3.64e-01],
            [-8.71e-01, -8.25e-01],
            [9.96e-01, -1.70e00],
            [1.28e00, np.nan],
            [9.25e-01, 8.95e-01],
            [-6.87e-01, -1.29e00],
            [np.nan, 9.64e-01],
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
            [np.nan, 8.94e-01],
            [9.02e-03, -4.34e-01],
            [-2.14e00, -1.43e00],
            [np.nan, 1.25e00],
            [4.10e-02, -1.13e00],
            [4.83e-02, 8.66e-01],
            [-2.11e00, 1.93e-01],
            [5.22e-01, 1.46e00],
            [np.nan, 1.62e00],
            [3.96e-01, -6.06e-01],
            [5.36e-01, 9.21e-01],
            [3.15e-01, -1.82e-01],
            [-1.23e-01, -1.07e00],
            [5.26e-01, np.nan],
            [6.65e-03, 1.18e-02],
            [-3.52e-01, -4.90e-01],
            [-7.01e-02, -1.23e00],
            [-1.49e-01, -1.20e00],
            [7.85e-01, 4.81e-02],
            [np.nan, 5.93e-01],
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
            [np.nan, -2.13e-01],
            [-1.24e-01, -1.12e00],
            [-4.39e-01, -9.61e-01],
            [np.nan, 2.40e-03],
            [8.12e-01, 7.08e-01],
            [8.88e-01, 8.17e-01],
            [2.38e-02, 8.36e-02],
            [np.nan, -1.00e00],
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
            [np.nan, 6.54e-01],
            [4.31e-01, -1.33e00],
            [-5.83e-02, -1.15e00],
            [-2.09e-01, 3.45e-01],
            [1.26e00, -1.37e00],
            [-1.78e00, -3.78e-01],
            [np.nan, -4.39e-02],
            [-5.36e-02, 1.60e00],
            [-1.39e00, -4.51e-01],
            [1.22e00, np.nan],
            [1.22e00, 5.61e-01],
            [-8.38e-01, 3.56e-01],
            [-4.46e-01, -8.61e-01],
            [1.17e00, -1.39e00],
            [-8.68e-02, -1.33e00],
            [-1.12e00, 5.76e-01],
            [-2.80e-01, -1.30e00],
            [-2.69e-02, 9.58e-01],
            [np.nan, 1.35e00],
            [1.38e00, -1.74e00],
            [4.08e-01, 1.16e00],
            [1.20e00, np.nan],
            [2.07e00, 1.02e00],
            [-4.62e-01, -1.87e-01],
            [1.27e00, 5.89e-01],
            [-1.01e-01, -7.65e-01],
            [-8.19e-01, np.nan],
            [6.15e-01, -2.28e-02],
            [-1.79e00, -9.80e-01],
            [-1.79e00, -9.54e-01],
            [8.26e-01, 1.50e00],
            [8.45e-01, np.nan],
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
            [np.nan, 9.41e-01],
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
            [2.35e00, np.nan],
            [-9.82e-01, np.nan],
            [np.nan, 4.69e-01],
            [-1.74e00, 6.93e-01],
            [-1.10e00, 1.16e00],
            [1.79e-02, -7.00e-01],
            [-6.20e-01, -9.84e-01],
            [-1.52e00, 6.60e-01],
            [1.07e00, np.nan],
            [9.17e-01, 5.25e-01],
            [-4.82e-02, 1.52e00],
            [1.49e00, np.nan],
            [-5.84e-01, 1.01e00],
            [-6.25e-02, -1.20e-01],
            [np.nan, 1.08e00],
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
            [6.83e-01, np.nan],
            [-7.53e-01, -6.15e-02],
            [-6.74e-02, 1.85e00],
            [1.08e00, 6.83e-01],
            [1.15e00, 2.43e-01],
            [4.97e-01, -6.71e-01],
        ]
    )
    return val


def initialize_dataset_with_additional_missing():
    val = np.array(
        [
            [1.14, -0.114],
            [-1.52, -1.15],
            [-1.05, 0.72],
            [-0.916, 0.397],
            [np.nan, np.nan],
            [-0.584, np.nan],
            [1.83, np.nan],
            [-1.25, -0.286],
            [1.7, 1.21],
            [-0.482, -0.485],
            [np.nan, -0.459],
            [-0.122, np.nan],
            [0.0809, 1.93],
            [-0.541, -0.332],
            [-1.02, np.nan],
            [-0.768, -1.04],
            [-1.69, np.nan],
            [1.26, 1.21],
            [0.724, np.nan],
            [0.444, 1.99],
            [-1.01, -1.36],
            [np.nan, 0.496],
            [np.nan, np.nan],
            [-0.595, -0.651],
            [-0.77, 0.364],
            [-0.871, np.nan],
            [np.nan, -1.7],
            [1.28, np.nan],
            [0.925, 0.895],
            [-0.687, -1.29],
            [np.nan, 0.964],
            [1.18, -0.335],
            [np.nan, 1.43],
            [1.71, -0.044],
            [0.271, np.nan],
            [1.12, 0.626],
            [1.3, 0.196],
            [-1.59, -0.68],
            [0.408, 0.0673],
            [1.13, 1.48],
            [0.763, 0.921],
            [-1.41, 1.11],
            [-0.75, -0.881],
            [1.16, 0.978],
            [1.13, 0.405],
            [-0.522, -1.34],
            [np.nan, 0.894],
            [0.00902, -0.434],
            [-2.14, -1.43],
            [np.nan, 1.25],
            [0.041, -1.13],
            [0.0483, np.nan],
            [-2.11, 0.193],
            [0.522, 1.46],
            [np.nan, 1.62],
            [np.nan, -0.606],
            [0.536, 0.921],
            [0.315, -0.182],
            [-0.123, -1.07],
            [0.526, np.nan],
            [0.00665, np.nan],
            [-0.352, -0.49],
            [-0.0701, -1.23],
            [-0.149, -1.2],
            [0.785, 0.0481],
            [np.nan, 0.593],
            [-0.0314, np.nan],
            [-0.285, -1.1],
            [1.33, 1.51],
            [1.09, -1.37],
            [-0.223, -1.28],
            [-0.0341, -1.07],
            [np.nan, 1.13],
            [-1.67, -1.26],
            [1.97, -0.772],
            [-0.508, -0.715],
            [0.603, -0.108],
            [np.nan, -0.213],
            [-0.124, -1.12],
            [-0.439, -0.961],
            [np.nan, 0.0024],
            [0.812, 0.708],
            [0.888, 0.817],
            [0.0238, 0.0836],
            [np.nan, -1.0],
            [-0.308, np.nan],
            [0.767, -0.248],
            [1.23, -1.2],
            [1.33, np.nan],
            [0.27, 0.0491],
            [-1.69, -1.87],
            [0.495, -0.281],
            [-0.519, np.nan],
            [-1.99, 0.549],
            [1.36, -0.732],
            [np.nan, 0.654],
            [0.431, -1.33],
            [-0.0583, -1.15],
            [-0.209, 0.345],
            [1.26, -1.37],
            [-1.78, -0.378],
            [np.nan, -0.0439],
            [-0.0536, 1.6],
            [-1.39, -0.451],
            [1.22, np.nan],
            [np.nan, 0.561],
            [-0.838, 0.356],
            [-0.446, -0.861],
            [1.17, -1.39],
            [-0.0868, -1.33],
            [-1.12, 0.576],
            [np.nan, -1.3],
            [-0.0269, 0.958],
            [np.nan, 1.35],
            [1.38, -1.74],
            [np.nan, 1.16],
            [1.2, np.nan],
            [2.07, 1.02],
            [-0.462, -0.187],
            [1.27, 0.589],
            [-0.101, -0.765],
            [-0.819, np.nan],
            [0.615, -0.0228],
            [-1.79, -0.98],
            [-1.79, np.nan],
            [0.826, 1.5],
            [0.845, np.nan],
            [-0.476, -1.49],
            [1.01, np.nan],
            [1.39, -0.376],
            [0.357, -1.07],
            [0.77, 1.4],
            [-1.08, 0.114],
            [-0.795, np.nan],
            [0.706, 1.38],
            [-1.26, 0.23],
            [-0.833, -0.569],
            [-0.0303, 2.11],
            [-0.223, np.nan],
            [-0.562, -0.873],
            [0.926, 0.972],
            [-1.86, -1.57],
            [np.nan, 0.941],
            [-0.214, 0.38],
            [0.744, 1.42],
            [1.94, -0.65],
            [1.77, 1.35],
            [-0.903, 0.101],
            [-0.0418, -1.02],
            [0.309, -0.175],
            [-0.634, -0.969],
            [-1.62, 0.102],
            [-1.21, 1.27],
            [0.529, 0.133],
            [0.386, np.nan],
            [-0.0962, 0.19],
            [-0.536, 1.13],
            [1.02, -0.261],
            [-0.876, -1.0],
            [2.35, np.nan],
            [-0.982, np.nan],
            [np.nan, 0.469],
            [-1.74, 0.693],
            [-1.1, 1.16],
            [0.0179, -0.7],
            [-0.62, -0.984],
            [-1.52, 0.66],
            [1.07, np.nan],
            [0.917, 0.525],
            [-0.0482, 1.52],
            [1.49, np.nan],
            [-0.584, 1.01],
            [-0.0625, -0.12],
            [np.nan, 1.08],
            [-1.77, -0.923],
            [np.nan, 0.712],
            [np.nan, np.nan],
            [1.71, 1.1],
            [-1.7, 0.872],
            [1.86, 1.14],
            [-0.529, -0.357],
            [-0.411, -1.3],
            [0.666, 1.36],
            [np.nan, -0.791],
            [-0.296, 0.255],
            [-0.0347, 1.3],
            [np.nan, -1.5],
            [-0.52, -1.17],
            [0.741, np.nan],
            [-1.33, 1.08],
            [-0.0987, 0.966],
            [0.0131, -0.969],
            [0.896, 1.58],
            [-0.412, 0.492],
            [0.683, np.nan],
            [-0.753, -0.0615],
            [-0.0674, 1.85],
            [1.08, 0.683],
            [1.15, 0.243],
            [0.497, -0.671],
        ]
    )
    return val


class TestMetrics(unittest.TestCase):
    """Test methods for data imputation"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        simplefilter(action="ignore", category=FutureWarning)
        simplefilter(action="ignore", category=DeprecationWarning)
        simplefilter(action="ignore", category=UserWarning)
        simplefilter(action="ignore", category=RuntimeWarning)
        simplefilter(action="ignore", category=UserWarning)
        cls.X_missing = initialize_dataset_with_missing()
        cls.X_additional_missing = initialize_dataset_with_additional_missing()

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_mean_absolute_imputation_score(self):
        """ Test mean_absolute_imputation_score """
        test_class = self.__class__
        X_missing_master = test_class.X_missing
        X_additional_missing_master = test_class.X_additional_missing

        X_missing = copy.deepcopy(X_missing_master)
        X_additional_missing = copy.deepcopy(X_additional_missing_master)
        imputer = SimpleImputer(strategy="mean")
        imputer.fit(X_additional_missing)
        result = mean_absolute_imputation_score(
            imputer, X_additional_missing, X_missing
        )
        # print(result)
        self.assertAlmostEqual(result, -0.06998317286882082, 3)

    def test_mean_squared_imputation_score(self):
        """ Test mean_squared_imputation_score """
        test_class = self.__class__
        X_missing_master = test_class.X_missing
        X_additional_missing_master = test_class.X_additional_missing

        X_missing = copy.deepcopy(X_missing_master)
        X_additional_missing = copy.deepcopy(X_additional_missing_master)
        imputer = SimpleImputer(strategy="mean")
        imputer.fit(X_additional_missing)
        result = mean_squared_imputation_score(imputer, X_additional_missing, X_missing)
        # print(result)
        self.assertAlmostEqual(result, -0.08649727549431466, 3)

    def test_mean_squared_log_imputation_score(self):
        """ Test mean_squared_log_imputation_score """
        test_class = self.__class__
        X_missing_master = test_class.X_missing
        X_additional_missing_master = test_class.X_additional_missing

        X_missing = copy.deepcopy(X_missing_master)
        X_additional_missing = copy.deepcopy(X_additional_missing_master)
        imputer = SimpleImputer(strategy="mean")
        imputer.fit(X_additional_missing)
        result = mean_squared_log_imputation_score(
            imputer, X_additional_missing, X_missing
        )
        # print(result)
        self.assertAlmostEqual(result, -0.0016893120701838378, 3)

    def test_median_absolute_imputation_score(self):
        """ Test median_absolute_imputation_score """
        test_class = self.__class__
        X_missing_master = test_class.X_missing
        X_additional_missing_master = test_class.X_additional_missing

        X_missing = copy.deepcopy(X_missing_master)
        X_additional_missing = copy.deepcopy(X_additional_missing_master)
        imputer = SimpleImputer(strategy="mean")
        imputer.fit(X_additional_missing)
        result = median_absolute_imputation_score(
            imputer, X_additional_missing, X_missing
        )
        self.assertAlmostEqual(result, -0.0, 3)

    def test_r2_imputation_score(self):
        """ Test r2_imputation_score """
        test_class = self.__class__
        X_missing_master = test_class.X_missing
        X_additional_missing_master = test_class.X_additional_missing

        X_missing = copy.deepcopy(X_missing_master)
        X_additional_missing = copy.deepcopy(X_additional_missing_master)
        imputer = SimpleImputer(strategy="mean")
        imputer.fit(X_additional_missing)
        result = r2_imputation_score(imputer, X_additional_missing, X_missing)
        # print(result)
        self.assertAlmostEqual(result, 0.9141911058933627, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
