# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing GrubbsTestFilter class"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.timeseries.grubbstest_filter import GrubbsTestFilter

class TestGrubbsTestFilter(unittest.TestCase):
    """Test class for GrubbsTestFilter"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        x = np.zeros(100)  # Numpy array containins 100 0's
        y = np.ones(100)    # Numpy array containins 100 1's
        z = np.ones(100)
        # Add random outliers to below index's
        index = [10, 20, 30, 35, 45, 55, 75, 95]
        values = [-25, -17, -10, 25, 17, 10, 2.5, 20]
        for i, value in enumerate(index):
            y[value] = values[i]
        # Add outliers in z
        z[50] = 10
        z[60] = -10
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
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=sliding_window_size,
                                             columns_to_be_ignored=ignore_features)
        transformed_df = grubbstest_filter.transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([10, 20, 30, 35, 45, 55, 75, 95], outlier_indexes.tolist())

    def test_fit_transform(self):
        """Test fit_transform method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=sliding_window_size,
                                             columns_to_be_ignored=ignore_features)
        transformed_df = grubbstest_filter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([10, 20, 30, 35, 45, 55, 75, 95], outlier_indexes.tolist())

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        grubbstest_filter = GrubbsTestFilter()
        fitted_grubbstest_filter = grubbstest_filter.fit(dataframe)
        self.assertEqual(grubbstest_filter, fitted_grubbstest_filter)

    def test_fit_transform_exceptions(self):
        """Test fit_transform method for exceptions"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        # Using sliding_window_size = number of observations
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=dataframe.shape[0])
        self.assertRaises(Exception, grubbstest_filter.fit_transform, dataframe)
        # Using sliding_window_size = number of observations + 5
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=dataframe.shape[0] + 5)
        self.assertRaises(Exception, grubbstest_filter.fit_transform, dataframe)
        # with non pandas and non numpy array data type
        self.assertRaises(Exception, grubbstest_filter.fit_transform, dataframe)
        # with wrong test_type value
        wrong_test_type = 'wrong-test-type'
        grubbstest_filter = GrubbsTestFilter(test_type=wrong_test_type)
        self.assertRaises(Exception, grubbstest_filter.fit_transform, dataframe)

    def test_transform_exceptions(self):
        """Test transform method for exceptions"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        # Using sliding_window_size = number of observations
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=dataframe.shape[0])
        self.assertRaises(Exception, grubbstest_filter.transform, dataframe)
        # Using sliding_window_size = number of observations + 5
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=dataframe.shape[0] + 5)
        self.assertRaises(Exception, grubbstest_filter.transform, dataframe)
        # with non pandas and non numpy array data type
        self.assertRaises(Exception, grubbstest_filter.transform, dataframe)

    def test_numpy_dataset(self):
        """Check numpy dataset as input"""
        test_class = self.__class__
        dataframe = test_class.dataframe.values
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=sliding_window_size,
                                             columns_to_be_ignored=ignore_features)
        transformed_df = grubbstest_filter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([10, 20, 30, 35, 45, 55, 75, 95], outlier_indexes.tolist())

    def test_nan_values_dataset(self):
        """Test with NaN values dataset"""
        test_class = self.__class__
        sliding_window_size = test_class.sliding_window_size
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=sliding_window_size)
        nan_array = np.full(10, np.nan)
        transformed_df = grubbstest_filter.fit_transform(nan_array)
        outlier_indexes = np.where(transformed_df[:] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())

    def test_when_no_columns_to_be_ignored(self):
        """Test with empty columns_to_be_ignored flag"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = []
        sliding_window_size = test_class.sliding_window_size
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=sliding_window_size,
                                             columns_to_be_ignored=ignore_features)
        transformed_df = grubbstest_filter.transform(dataframe)
        # No outlier for 1st feature
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())
        # 5 outliers for 2nd feature
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([10, 20, 30, 35, 45, 55, 75, 95], outlier_indexes.tolist())
        # 1 outlier for 3rd feature
        outlier_indexes = np.where(transformed_df[:, 2] == 1)[0]
        self.assertEqual([50, 60], outlier_indexes.tolist())

    def test_with_different_test_type(self):
        """Test with different test_type values"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        #default two-sided-test
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=sliding_window_size,
                                             columns_to_be_ignored=ignore_features)
        transformed_df = grubbstest_filter.transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        # with test type one-sided-min
        test_type_min = 'one-sided-min'
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=sliding_window_size,
                                             columns_to_be_ignored=ignore_features,
                                             test_type=test_type_min)
        transformed_df = grubbstest_filter.fit_transform(dataframe)
        min_outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        result_min =  all(elem in list(outlier_indexes)  for elem in list(min_outlier_indexes))
        self.assertTrue(result_min)
        # with test type one-sided-max
        test_type_max = 'one-sided-max'
        grubbstest_filter = GrubbsTestFilter(sliding_window_size=sliding_window_size,
                                             columns_to_be_ignored=ignore_features,
                                             test_type=test_type_max)
        transformed_df = grubbstest_filter.fit_transform(dataframe)
        max_outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        result_max =  all(elem in list(outlier_indexes)  for elem in list(max_outlier_indexes))
        self.assertTrue(result_max)

    def test_set_params(self):
        """Test set_params method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        grubbstest_filter = GrubbsTestFilter()
        grubbstest_filter.set_params(sliding_window_size=sliding_window_size,
                                     columns_to_be_ignored=ignore_features,
                                     test_type="two-sided",
                                     alpha=0.05)
        transformed_df = grubbstest_filter.transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([10, 20, 30, 35, 45, 55, 75, 95], outlier_indexes.tolist())

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
