# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing LocalHistogramFilter class"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.timeseries.localhistogram_filter import LocalHistogramFilter

class TestLocalHistogramFilter(unittest.TestCase):
    """Test class for LocalHistogramFilter"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        # Samples from a normal distribution.
        x_array = [-6.56710551e-02, 5.55957684e-02, 2.71371400e-01, 1.25716976e-01, 1.42302468e-01,
                   -3.77753833e-02, -1.07457176e-01, -4.61041380e-02, 1.77357238e-01,
                   -9.81085625e-02, -1.22173575e-01, -1.08495346e-01, -3.69485060e-02,
                   3.83447146e-02, -5.14401581e-02, 1.11368359e-01, 1.02186861e-01,
                   -1.45493563e-01, 1.06967250e-01, 1.88921632e-03, 1.29276466e-01,
                   -6.61571155e-02, 3.04332412e-02, -8.19763634e-02, 1.64243250e-01,
                   2.00000000e+00, 1.53177058e-01, 1.28808242e-01, 7.50495256e-03,
                   -1.22822287e-02, -5.08531950e-02, 1.03298774e-03, 1.50208320e-01,
                   4.09017708e-02, 2.62526548e-01, 3.50000000e+01, -6.92284800e-02,
                   -1.45483203e-01, -1.32561652e-01, -1.13780506e-02, 7.15968954e-02,
                   2.14845622e-01, -1.02389484e-01, 3.40417818e-02, -8.36860219e-02,
                   -2.13528004e-01, -7.97585690e-02, 1.41669732e-02, -6.93437207e-02,
                   -8.87474156e-02, -1.25760699e-01, 2.60835190e-02, -1.31526975e-01,
                   1.31647335e-01, 5.61963687e-02, 6.81039861e-03, 1.83692074e-01, 3.23019869e-02,
                   1.13353687e-01, 9.48726329e-03, -1.17250750e-01, 1.43720717e-01,
                   -6.48920342e-02, 7.81205926e-02, 7.71782487e-02, -3.72084018e-02,
                   4.67309849e-02, 7.83475917e-02, 5.93447372e-02, -3.50214513e-03, 7.00000000e+01,
                   2.81233950e-02, -6.52499460e-02, -7.57309384e-02, 9.72720088e-02,
                   2.66389357e-02, 6.69376724e-02, -1.10145057e-01, 1.50805784e-01, 5.60285566e-02,
                   -7.56471329e-02, -8.95086897e-02, -1.99779242e-01, 5.49086855e-02,
                   -2.47287486e-02, -2.85870980e-02, 5.23866338e-02, -3.15978585e-02,
                   6.93988143e-02, -3.82139889e-02, -1.28858741e-01, -2.03791925e-01,
                   -1.32520511e-01, 9.81451509e-03, -2.00100198e-02, 1.47056716e-01,
                   1.73539795e-04, 2.86994051e-02, 5.83170625e-02, 1.12103030e-02]
        # Add outliers
        x_array[25] = 2
        x_array[35] = 35
        x_array[70] = 70
        y_array = np.ones(100)    # Numpy array containins 100 1's
        y_array[39:45] = np.nan     # Introducing some nan values
        z_array = np.ones(100)    # Numpy array containins 100 1's
        z_array[45] = 45
        cls.dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'z': z_array})
        cls.threshold = 0.05
        cls.ignore_features = ['z']
        cls.no_histogram_bins = 51
        cls.sliding_window_size = 50

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
        no_histogram_bins = test_class.no_histogram_bins
        threshold = test_class.threshold
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.transform(dataframe)

        # 3 outlier for 'x'
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertEqual([25, 35, 70], outlier_indexes.tolist())

        # No outlier for 'y'
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())

        # No Outlier for ignored columns
        outlier_indexes = np.where(transformed_df[:, 2] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())

    def test_fit_transform(self):
        """Test fit_transform method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        no_histogram_bins = test_class.no_histogram_bins
        threshold = test_class.threshold
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)

        transformed_df = localhistogramfilter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertEqual([25, 35, 70], outlier_indexes.tolist())

    def test_fit(self):
        """Test fit method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        localhistogramfilter = LocalHistogramFilter()
        fitted_localhistogramfilter = localhistogramfilter.fit(dataframe)
        self.assertEqual(localhistogramfilter, fitted_localhistogramfilter)

    def test_fit_transform_exceptions(self):
        """Test fit_transform method for exceptions"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        # Using sliding_window_size = number of observations
        localhistogramfilter = LocalHistogramFilter(sliding_window_size=dataframe.shape[0])
        self.assertRaises(Exception, localhistogramfilter.fit_transform, dataframe)
        # Using sliding_window_size = number of observations + 5
        localhistogramfilter = LocalHistogramFilter(sliding_window_size=dataframe.shape[0] + 2)
        self.assertRaises(Exception, localhistogramfilter.fit_transform, dataframe)
        # non pandas and non numpy array data type
        localhistogramfilter = LocalHistogramFilter()
        dataframe = []
        self.assertRaises(Exception, localhistogramfilter.fit_transform, dataframe)
        # random value no_histogram_binss
        dataframe = test_class.dataframe
        no_histogram_bins = "some_random_value"
        sliding_window_size = test_class.sliding_window_size
        threshold = test_class.threshold
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    no_histogram_bins=no_histogram_bins)
        self.assertRaises(ValueError, localhistogramfilter.fit_transform, dataframe)
        # sliding_window_size 0
        sliding_window_size = 0
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        self.assertRaises(ValueError, localhistogramfilter.fit_transform, dataframe)
        # sliding_window_size 1.5
        sliding_window_size = 1.5
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        self.assertRaises(TypeError, localhistogramfilter.fit_transform, dataframe)
        
    def test_transform_exceptions(self):
        """Test transform method for exceptions"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        # Using sliding_window_size = number of observations
        localhistogramfilter = LocalHistogramFilter(sliding_window_size=dataframe.shape[0])
        self.assertRaises(Exception, localhistogramfilter.transform, dataframe)
        # Using sliding_window_size = number of observations + 5
        localhistogramfilter = LocalHistogramFilter(sliding_window_size=dataframe.shape[0] + 2)
        self.assertRaises(Exception, localhistogramfilter.transform, dataframe)
        # non pandas and non numpy array data type
        localhistogramfilter = LocalHistogramFilter()
        dataframe = []
        self.assertRaises(Exception, localhistogramfilter.transform, dataframe)
        
    def test_numpy_dataset(self):
        """Check numpy dataset as input"""
        test_class = self.__class__
        dataframe = test_class.dataframe.values
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        no_histogram_bins = test_class.no_histogram_bins
        threshold = test_class.threshold
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)

        transformed_df = localhistogramfilter.fit_transform(dataframe)

        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertEqual([25, 35, 70], outlier_indexes.tolist())

        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())

    def test_when_no_columns_to_be_ignored(self):
        """Test with empty columns_to_be_ignored flag"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = []
        sliding_window_size = test_class.sliding_window_size
        no_histogram_bins = test_class.no_histogram_bins
        threshold = test_class.threshold
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.transform(dataframe)

        # 3 outlier for 'x' feature
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertEqual([25, 35, 70], outlier_indexes.tolist())
        # No outliers for 'y' feature
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())
        # 1 outlier for 'z' feature
        outlier_indexes = np.where(transformed_df[:, 2] == 1)[0]
        self.assertEqual([45], outlier_indexes.tolist())

    def test_with_different_histogram_bins(self):
        """Test with different no_histogram_bins values"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        threshold = test_class.threshold

        outliers = [25, 35, 70]

        no_histogram_bins = 'doane'
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        doane_outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        result1 =  any(elem in list(doane_outlier_indexes)  for elem in outliers)
        self.assertTrue(result1)

        no_histogram_bins = 'sturges'
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        sturges_outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        result2 =  any(elem in list(sturges_outlier_indexes)  for elem in outliers)
        self.assertTrue(result2)

        no_histogram_bins = 'auto'
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        auto_outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        result3 =  any(elem in list(auto_outlier_indexes)  for elem in outliers)
        self.assertTrue(result3)

        no_histogram_bins = 10
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        ten_bin_outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        result4 =  any(elem in list(ten_bin_outlier_indexes )  for elem in outliers)
        self.assertTrue(result4)

        no_histogram_bins = 5
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        five_bin_outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        result5 =  any(elem in list(five_bin_outlier_indexes )  for elem in outliers)
        self.assertTrue(result5)


    def test_with_different_sliding_window_size(self):
        """Test with different sliding_window_size values"""
        test_class = self.__class__
        outliers = [25, 35, 70]
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        no_histogram_bins = test_class.no_histogram_bins
        threshold = test_class.threshold
        sliding_window_size = 20
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        win_20_outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        result1 =  any(elem in list(win_20_outlier_indexes )  for elem in outliers)
        self.assertTrue(result1)

        sliding_window_size = 90
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        win_90_outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        result2 =  any(elem in list(win_90_outlier_indexes )  for elem in outliers)
        self.assertTrue(result2)

    def test_with_different_threshold(self):
        """Test with different threshold values"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        no_histogram_bins = test_class.no_histogram_bins
        sliding_window_size = test_class.sliding_window_size

        threshold = 0.005
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertLessEqual(len(list(outlier_indexes)),3)

        threshold = 0.01
        localhistogramfilter = LocalHistogramFilter(columns_to_be_ignored=ignore_features,
                                                    sliding_window_size=sliding_window_size,
                                                    threshold=threshold,
                                                    no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.fit_transform(dataframe)
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertGreaterEqual(len(list(outlier_indexes)),3)

    def test_set_params(self):
        """Test set_params method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        ignore_features = test_class.ignore_features
        sliding_window_size = test_class.sliding_window_size
        no_histogram_bins = test_class.no_histogram_bins
        threshold = test_class.threshold
        localhistogramfilter = LocalHistogramFilter()
        localhistogramfilter.set_params(columns_to_be_ignored=ignore_features,
                                        sliding_window_size=sliding_window_size,
                                        threshold=threshold,
                                        no_histogram_bins=no_histogram_bins)
        transformed_df = localhistogramfilter.transform(dataframe)

        # 3 outlier for 'x'
        outlier_indexes = np.where(transformed_df[:, 0] == 1)[0]
        self.assertEqual([25, 35, 70], outlier_indexes.tolist())

        # No outlier for 'y'
        outlier_indexes = np.where(transformed_df[:, 1] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())

        # No Outlier for ignored columns
        outlier_indexes = np.where(transformed_df[:, 2] == 1)[0]
        self.assertEqual([], outlier_indexes.tolist())

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
