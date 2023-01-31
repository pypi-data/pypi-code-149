# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing methods in outlier_removal file"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.outlier_removal import prob_density_based_outlier_removal

class TestOutlierRemoval(unittest.TestCase):
    """Test methods in outlier_removal file"""

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
        z_array = np.ones(100)    # Numpy array containins 100 1's
        cls.dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'z': z_array})
        cls.threshold = 0.05
        cls.columns_to_be_ignored = ['z']

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_prob_density_based_outlier_removal(self):
        """Test prob_density_based_outlier_removal method"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        threshold = test_class.threshold
        columns_to_be_ignored = test_class.columns_to_be_ignored
        result = prob_density_based_outlier_removal(X=dataframe,
                                                    threshold=threshold,
                                                    columns_to_be_ignored=columns_to_be_ignored)
        # Since 3 outliers are removed, shape will be reduced by 3
        self.assertEqual(97, result.shape[0])
        # Since 3 outliers are removed, index will not have those records which are removed
        self.assertNotIn(25, result.index)
        self.assertNotIn(35, result.index)
        self.assertNotIn(70, result.index)
        # Result should be same to input after removing outlier containing records
        self.assertTrue(result.equals(dataframe.drop(dataframe.index[[25, 35, 70]])))

    def test_columns_to_be_ignored_as_none(self):
        """Test prob_density_based_outlier_removal method with columns_to_be_ignored as None"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        threshold = test_class.threshold
        columns_to_be_ignored = None
        result = prob_density_based_outlier_removal(X=dataframe,
                                                    threshold=threshold,
                                                    columns_to_be_ignored=columns_to_be_ignored)
        # Since 3 outliers are removed, shape will be reduced by 3
        self.assertEqual(97, result.shape[0])
        # Since 3 outliers are removed, index will not have those records which are removed
        self.assertNotIn(25, result.index)
        self.assertNotIn(35, result.index)
        self.assertNotIn(70, result.index)
        # Result should be same to input after removing outlier containing records
        self.assertTrue(result.equals(dataframe.drop(dataframe.index[[25, 35, 70]])))

    def test_outlier_columns_is_ignored(self):
        """Test prob_density_based_outlier_removal method with a columns_to_be_ignored
        containing outlier producing column name"""
        test_class = self.__class__
        dataframe = test_class.dataframe
        threshold = test_class.threshold
        columns_to_be_ignored = ['x']
        result = prob_density_based_outlier_removal(X=dataframe,
                                                    threshold=threshold,
                                                    columns_to_be_ignored=columns_to_be_ignored)
        # Since no outliers are removed, shape will be same
        self.assertEqual(100, result.shape[0])
        # Result should be same to input
        self.assertTrue(result.equals(dataframe))

    def test_non_pandas_dataset(self):
        """Test prob_density_based_outlier_removal method with a non pandas dataset"""
        test_class = self.__class__
        dataframe = np.ones(100)
        threshold = test_class.threshold
        columns_to_be_ignored = []
        result = prob_density_based_outlier_removal(X=dataframe,
                                                    threshold=threshold,
                                                    columns_to_be_ignored=columns_to_be_ignored)
        # Result should be same to input
        self.assertTrue(np.array_equal(result, dataframe))

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
