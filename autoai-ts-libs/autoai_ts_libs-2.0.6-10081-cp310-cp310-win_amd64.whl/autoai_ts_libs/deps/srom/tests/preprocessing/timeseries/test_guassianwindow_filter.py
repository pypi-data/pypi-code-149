# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing GaussianWindowFilter class"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.timeseries.gaussianwindow_filter import GaussianWindowFilter

class TestGaussianWindowFilter(unittest.TestCase):
    """Test class for TestGaussianWindowFilter"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        x = np.zeros(100)  # Numpy array containins 100 0's
        y = np.ones(100)    # Numpy array containins 100 1's
        z = np.ones(100)
        # Add random outliers to below index's
        index = [35, 45, 55, 75, 95]
        values = [25, 17, 10, 2.5, 20]
        for i, value in enumerate(index):
            y[value] = values[i]
        # Add single outlier in z
        z[50] = 10
        # Add np.nan in z
        z[80] = np.nan
        cls.dataframe = pd.DataFrame({'x': x, 'y': y, 'z': z})
        cls.ignore_features = ['x', 'z']
        cls.sliding_window_size = 5

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_transform(self):
        """Test transform method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=0.01)
        transformed_df = gaussianwindow_filter.transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([35, 45, 55, 75, 95], outlier_indexes.tolist())

    def test_fit_transform(self):
        """Test fit_transform method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=0.01)
        transformed_df = gaussianwindow_filter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([35, 45, 55, 75, 95], outlier_indexes.tolist())

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        gaussianwindow_filter = GaussianWindowFilter()
        fitted_gaussianwindow_filter = gaussianwindow_filter.fit(dataframe)
        self.assertEqual(gaussianwindow_filter, fitted_gaussianwindow_filter)

    def test_fit_transform_exceptions(self):
        """Test fit_transform method for exceptions"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        # Using sliding_window_size = number of observations
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=dataframe.shape[0])
        self.assertRaises(Exception, gaussianwindow_filter.fit_transform, dataframe)
        # Using sliding_window_size = number of observations + 5
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=dataframe.shape[0] + 5)
        self.assertRaises(Exception, gaussianwindow_filter.fit_transform, dataframe)
        # with non pandas and non numpy array data type
        gaussianwindow_filter = GaussianWindowFilter()
        dataframe = []
        self.assertRaises(Exception, gaussianwindow_filter.fit_transform, dataframe)

    def test_transform_exceptions(self):
        """Test transform method for exceptions"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        # Using sliding_window_size = number of observations
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=dataframe.shape[0])
        self.assertRaises(Exception, gaussianwindow_filter.transform, dataframe)
        # Using sliding_window_size = number of observations + 5
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=dataframe.shape[0] + 5)
        self.assertRaises(Exception, gaussianwindow_filter.transform, dataframe)
        # with non pandas and non numpy array data type
        gaussianwindow_filter = GaussianWindowFilter()
        dataframe = []
        self.assertRaises(Exception, gaussianwindow_filter.transform, dataframe)
        
    def test_numpy_dataset(self):
        """Check numpy dataset as input"""
        test_class = self.__class__
        dataframe = test_class.dataframe.values
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=0.01)
        transformed_df = gaussianwindow_filter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([35, 45, 55, 75, 95], outlier_indexes.tolist())

    def test_when_no_columns_to_be_ignored(self):
        """Test with empty columns_to_be_ignored flag"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = []
        sliding_window_size = test_class.sliding_window_size
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=0.01)
        transformed_df = gaussianwindow_filter.transform(dataframe)
        # No outlier for 1st feature
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())
        # 5 outliers for 2nd feature
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([35, 45, 55, 75, 95], outlier_indexes.tolist())
        # 1 outlier for 3rd feature
        outlier_indexes = np.where(transformed_df[:, 2] == 1)[0]
        self.assertEqual([50], outlier_indexes.tolist())

    def test_with_different_probability_threshold(self):
        """Test with different probability_threshold values"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        #Threshold 0.01
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=0.01)
        transformed_df = gaussianwindow_filter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]

        # Negative test: probability_threshold should be greater than 0
        probability_threshold = 0
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=probability_threshold)
        transformed_df = gaussianwindow_filter.fit_transform(dataframe)
        zero_thre_outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertLessEqual(len(list(zero_thre_outlier_indexes)),len(list(outlier_indexes)))
        probability_threshold = 0.05
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=probability_threshold)
        transformed_df = gaussianwindow_filter.fit_transform(dataframe)
        point_zero_five_thre_outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertGreaterEqual(len(list(point_zero_five_thre_outlier_indexes)),len(list(outlier_indexes)))

        # probability_threshold value is very high
        probability_threshold = 1
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=probability_threshold)
        transformed_df = gaussianwindow_filter.fit_transform(dataframe)
        high_thre_outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertGreaterEqual(len(list(high_thre_outlier_indexes)),len(list(outlier_indexes)))

    def test_with_nan_values_in_dataframe(self):
        """Test with nan values in dataframe"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = ['x']
        sliding_window_size = test_class.sliding_window_size
        dataframe = pd.DataFrame({'x': np.zeros(10), 'y': [np.nan for i in range(0, 10)]})
        gaussianwindow_filter = GaussianWindowFilter(sliding_window_size=sliding_window_size,
                                                     columns_to_be_ignored=ignore_features,
                                                     probability_threshold=0.01)
        transformed_df = gaussianwindow_filter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())

    def test_set_params(self):
        """Test set_params method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        gaussianwindow_filter = GaussianWindowFilter()
        gaussianwindow_filter.set_params(sliding_window_size=sliding_window_size,
                                         columns_to_be_ignored=ignore_features,
                                         probability_threshold=0.01)
        transformed_df = gaussianwindow_filter.transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([35, 45, 55, 75, 95], outlier_indexes.tolist())

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
