# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing TestRobustPCA class"""
import unittest
import copy
import numpy as np
from numpy.linalg.linalg import LinAlgError
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.robust_pca import RobustPCA

class TestRobustPCA(unittest.TestCase):
    """Test class for TestRobustPCA"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        x_array = np.zeros(100)  # Numpy array containins 100 0's
        y_array = np.ones(100)    # Numpy array containins 100 1's
        z_array = np.ones(100)
        # Add random outliers to below index's
        index = [35, 45, 55, 75, 95]
        values = [25, 17, 10, 2.5, 20]
        for i, value in enumerate(index):
            y_array[value] = values[i]
        # Add single outlier in z
        z_array[50] = 10
        z_array[80] = 39
        cls.dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'z': z_array})
        cls.numpy_array = cls.dataframe.values
        cls.max_iter = 1000

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_transform(self):
        """Test transform method"""
        test_class = self.__class__
        original_data = test_class.numpy_array
        max_iter = test_class.max_iter
        robust_pca = RobustPCA(None, max_iter)
        transformed_data = robust_pca.transform(original_data)
        residual_error = original_data - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        self.assertEqual([35, 45, 55, 75, 95],
                         np.where(function(residual_error[:100, 1]))[0].tolist())
        self.assertEqual([50, 80],
                         np.where(function(residual_error[:100, 2]))[0].tolist())

    def test_fit_transform(self):
        """Test fit_transform method"""
        test_class = self.__class__
        original_data = test_class.numpy_array
        max_iter = test_class.max_iter
        robust_pca = RobustPCA(None, max_iter)
        transformed_data = robust_pca.fit_transform(original_data)
        residual_error = original_data - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        self.assertEqual([35, 45, 55, 75, 95],
                         np.where(function(residual_error[:100, 1]))[0].tolist())
        self.assertEqual([50, 80],
                         np.where(function(residual_error[:100, 2]))[0].tolist())

    def test_transform_with_no_tolerance_and_nan_values_in_dataset(self):
        """Test transform method"""
        test_class = self.__class__
        original_data = copy.deepcopy(test_class.numpy_array)
        max_iter = test_class.max_iter
        original_data[80][2] = np.nan
        original_data[40][2] = np.nan
        robust_pca = RobustPCA(None, max_iter)
        transformed_data = robust_pca.transform(original_data)
        residual_error = original_data - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                          19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                          53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
                          70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                          87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
                         np.where(function(residual_error[:100, 1]))[0].tolist())

    def test_transform_exceptions(self):
        """Test transform method for exceptions"""
        #with tolerance and nan values in dataset
        test_class = self.__class__
        original_data = copy.deepcopy(test_class.numpy_array)
        max_iter = test_class.max_iter
        original_data[80][2] = np.nan
        original_data[40][2] = np.nan
        robust_pca = RobustPCA(2, max_iter)
        self.assertRaises(LinAlgError, robust_pca.transform, original_data)

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        robust_pca = RobustPCA()
        fitted_robust_pca = robust_pca.fit(dataframe)
        self.assertEqual(robust_pca, fitted_robust_pca)

    def test_transform_with_pandas_dataframe(self):
        """Test transform method with pandas dataframe"""
        test_class = self.__class__
        original_data = test_class.dataframe
        max_iter = test_class.max_iter
        robust_pca = RobustPCA(None, max_iter)
        transformed_data = robust_pca.transform(original_data)
        #convert numpy array to dataframe
        residual_error = test_class.numpy_array - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        self.assertEqual([35, 45, 55, 75, 95],
                         np.where(function(residual_error[:100, 1]))[0].tolist())
        self.assertEqual([50, 80],
                         np.where(function(residual_error[:100, 2]))[0].tolist())

    def test_transform_with_mu(self):
        """Test transform method with mu"""
        test_class = self.__class__
        original_data = test_class.numpy_array
        max_iter = test_class.max_iter
        #with mu value  = 0.1
        robust_pca = RobustPCA(None, max_iter, 0.1)
        transformed_data = robust_pca.transform(original_data)
        residual_error = original_data - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        outlier_indices = np.where(function(residual_error[:100, 1]))[0].tolist()
        #with mu value  = 10
        robust_pca = RobustPCA(None, max_iter, 10)
        transformed_data = robust_pca.transform(original_data)
        residual_error = original_data - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        self.assertLessEqual(len(np.where(function(residual_error[:100, 1]))[0].tolist()),len(outlier_indices))

    def test_transform_with_lambda(self):
        """Test transform method with lambda"""
        test_class = self.__class__
        original_data = test_class.numpy_array
        max_iter = test_class.max_iter
        #with lambda value  = 0.1
        robust_pca = RobustPCA(None, max_iter, None, 0.1)
        transformed_data = robust_pca.transform(original_data)
        residual_error = original_data - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        outlier_indices = np.where(function(residual_error[:100, 1]))[0].tolist() 
        #with lambda value  = 10
        robust_pca = RobustPCA(None, max_iter, None, 10)
        transformed_data = robust_pca.transform(original_data)
        residual_error = original_data - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        self.assertLessEqual(len(np.where(function(residual_error[:100, 1]))[0].tolist()),len(outlier_indices))
        
    def test_transform_with_all_parameters(self):
        """Test transform method with all parameters"""
        test_class = self.__class__
        original_data = test_class.numpy_array
        max_iter = test_class.max_iter
        robust_pca = RobustPCA(2, max_iter, 0.1, 0.1)
        transformed_data = robust_pca.transform(original_data)
        residual_error = original_data - transformed_data
        function = np.vectorize(lambda value: round(value) > 0)
        self.assertEqual([35, 45, 55, 95],
                         np.where(function(residual_error[:100, 1]))[0].tolist())
        self.assertEqual([50, 80],
                         np.where(function(residual_error[:100, 2]))[0].tolist())

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
