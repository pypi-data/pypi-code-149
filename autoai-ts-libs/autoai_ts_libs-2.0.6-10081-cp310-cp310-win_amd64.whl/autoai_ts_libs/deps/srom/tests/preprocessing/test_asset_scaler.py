# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing TestAssetScaler class"""
import unittest
import pandas as pd
from autoai_ts_libs.deps.srom.preprocessing.asset_scaler import AssetScaler

class TestAssetScaler(unittest.TestCase):
    """Test class for TestRobustPCA"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        data = [[0, 0], [0, 0], [1, 1], [1, 1], [0, 0], [0, 0], [1, 1], [1, 1]]
        cls.dataframe = pd.DataFrame(data)
        cls.dataframe.columns = ['x', 'y']
        cls.dataframe['id'] = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b']
        cls.numpy_array = cls.dataframe.values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """ Test fit method"""
        test_class = self.__class__
        asset_scaler = AssetScaler(asset_id='id')
        fitted_as = asset_scaler.fit(test_class.dataframe)
        self.assertEqual(len(fitted_as._fitted_scalers),2)
        for scaler in fitted_as._fitted_scalers :
            self.assertEqual(list(scaler.var_),[0.25,0.25])
            self.assertEqual(list(scaler.mean_),[0.5,0.5])
        asset_scaler = AssetScaler(asset_id='id', columns_to_be_ignored=['x'])
        fitted_as = asset_scaler.fit(test_class.dataframe)
        self.assertEqual(len(fitted_as._scale_clms),1)

    def test_fit_exceptions(self):
        """ Exception test cases for test_fit """
        test_class = self.__class__
        asset_scaler = AssetScaler(asset_id='id')
        self.assertRaises(AttributeError,getattr,asset_scaler._scaler,"mean_")
        fitted_as = asset_scaler.fit(test_class.dataframe)
        self.assertRaises(AttributeError, asset_scaler.fit, test_class.numpy_array)
        
    def test_transform(self):
        """ Test transform"""
        test_class = self.__class__
        asset_scaler = AssetScaler(asset_id='id')
        asset_scaler.fit(test_class.dataframe)
        transformed_as = asset_scaler.transform(test_class.dataframe)
        self.assertEqual(transformed_as.iloc[:, 0].tolist(),
                         [-1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0])
        self.assertEqual(transformed_as.iloc[:, 1].tolist(),
                         [-1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0])

        asset_scaler = AssetScaler(asset_id='id', columns_to_be_ignored=['x'])
        asset_scaler.fit(test_class.dataframe)
        transformed_as = asset_scaler.transform(test_class.dataframe)
        self.assertEqual(transformed_as.iloc[:, 0].tolist(),
                         [-1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0])

    def test_transform_exceptions(self):
        """ Exception test cases for test_transform """
        test_class = self.__class__
        asset_scaler = AssetScaler(asset_id='id')
        self.assertRaises(Exception, asset_scaler.transform, test_class.dataframe)




if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
