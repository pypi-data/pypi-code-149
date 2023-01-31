# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing IQRFilter class"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.timeseries.iqr_filter import IQRFilter

class TestIQRFilter(unittest.TestCase):
    """Test class for IQRFilter"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        x_array = np.array([np.nan] * 10)
        y_array = np.array([1, 2, 6, 6, 7, 12, 12, 17, 25, 55])
        z_array = np.array([1, 2, 55, 4, 5, 6, 7, 8, 9, 10], dtype=float)
        # Add np.nan in z
        z_array[7] = np.nan
        cls.dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'z': z_array})
        cls.ignore_features = ['x', 'z']
        cls.sliding_window_size = 5
        cls.iqr_threshold = 1.5

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
        iqr_threshold = test_class.iqr_threshold
        median_filter = IQRFilter(sliding_window_size=sliding_window_size,
                                  columns_to_be_ignored=ignore_features,
                                  iqr_threshold=iqr_threshold)
        transformed_df = median_filter.transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([9], outlier_indexes.tolist())

    def test_fit_transform(self):
        """Test fit_transform method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        iqr_threshold = test_class.iqr_threshold
        median_filter = IQRFilter(sliding_window_size=sliding_window_size,
                                  columns_to_be_ignored=ignore_features,
                                  iqr_threshold=iqr_threshold)
        transformed_df = median_filter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([9], outlier_indexes.tolist())

    def test_fit_transform_exceptions(self):
        """Test fit_transform method for exceptions"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        # Using sliding_window_size = number of observations
        median_filter = IQRFilter(sliding_window_size=dataframe.shape[0])
        self.assertRaises(Exception, median_filter.fit_transform, dataframe)
        # Using sliding_window_size = number of observations + 5
        median_filter = IQRFilter(sliding_window_size=dataframe.shape[0] + 5)
        self.assertRaises(Exception, median_filter.fit_transform, dataframe)
        # with non pandas and non numpy array data type
        median_filter = IQRFilter()
        dataframe = []
        self.assertRaises(Exception, median_filter.fit_transform, dataframe)

    def test_transform_exceptions(self):
        """Test transform method for exceptions"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        # Using sliding_window_size = number of observations
        median_filter = IQRFilter(sliding_window_size=dataframe.shape[0])
        self.assertRaises(Exception, median_filter.transform, dataframe)
        # Using sliding_window_size = number of observations + 5
        median_filter = IQRFilter(sliding_window_size=dataframe.shape[0] + 5)
        self.assertRaises(Exception, median_filter.transform, dataframe)
        # with non pandas and non numpy array data type
        median_filter = IQRFilter()
        dataframe = []
        self.assertRaises(Exception, median_filter.transform, dataframe)
        
    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        median_filter = IQRFilter()
        fitted_median_filter = median_filter.fit(dataframe)
        self.assertEqual(median_filter, fitted_median_filter)

    def test_numpy_dataset(self):
        """Check numpy dataset as input"""
        test_class = self.__class__
        dataframe = test_class.dataframe.values
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        iqr_threshold = test_class.iqr_threshold
        median_filter = IQRFilter(sliding_window_size=sliding_window_size,
                                  columns_to_be_ignored=ignore_features,
                                  iqr_threshold=iqr_threshold)
        transformed_df = median_filter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([9], outlier_indexes.tolist())

    def test_when_no_columns_to_be_ignored(self):
        """Test with empty columns_to_be_ignored flag"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = []
        sliding_window_size = test_class.sliding_window_size
        iqr_threshold = test_class.iqr_threshold
        median_filter = IQRFilter(sliding_window_size=sliding_window_size,
                                  columns_to_be_ignored=ignore_features,
                                  iqr_threshold=iqr_threshold)
        transformed_df = median_filter.transform(dataframe)
        # No outlier for 1st feature
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())
        # 1 outliers for 2nd feature
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([9], outlier_indexes.tolist())
        # 1 outlier for 3rd feature
        outlier_indexes = np.where(transformed_df[:, 2] == 1)[0]
        self.assertEqual([2], outlier_indexes.tolist())

    def test_with_different_iqr_threshold(self):
        """Test with different iqr_threshold values"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        #Test default threshold
        iqr_threshold = test_class.iqr_threshold
        median_filter = IQRFilter(sliding_window_size=sliding_window_size,
                                  columns_to_be_ignored=ignore_features,
                                  iqr_threshold=iqr_threshold)
        transformed_df = median_filter.transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]

        # iqr_threshold value is very low: Almost all are outliers
        iqr_threshold = 0
        median_filter = IQRFilter(sliding_window_size=sliding_window_size,
                                  columns_to_be_ignored=ignore_features,
                                  iqr_threshold=iqr_threshold)
        transformed_df = median_filter.fit_transform(dataframe)
        zero_thre_outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertGreaterEqual(len(list(zero_thre_outlier_indexes)),len(list(outlier_indexes)))

        # iqr_threshold value is very high: Almost none is outlier
        iqr_threshold = 100
        median_filter = IQRFilter(sliding_window_size=sliding_window_size,
                                  columns_to_be_ignored=ignore_features,
                                  iqr_threshold=iqr_threshold)
        transformed_df = median_filter.fit_transform(dataframe)
        high_thre_outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertLessEqual(len(list(high_thre_outlier_indexes)),len(list(outlier_indexes)))

    def test_set_params(self):
        """Test set_params method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        iqr_threshold = test_class.iqr_threshold
        median_filter = IQRFilter()
        median_filter.set_params(sliding_window_size=sliding_window_size,
                                 columns_to_be_ignored=ignore_features,
                                 iqr_threshold=iqr_threshold)
        transformed_df = median_filter.transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([9], outlier_indexes.tolist())

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
