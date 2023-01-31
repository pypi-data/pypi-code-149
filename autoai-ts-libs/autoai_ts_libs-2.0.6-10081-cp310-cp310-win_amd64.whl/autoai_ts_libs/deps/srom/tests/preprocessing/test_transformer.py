import unittest
import pandas as pd
import numpy as np
import copy
from autoai_ts_libs.deps.srom.preprocessing.transformer import (
    Log,
    Sqrt,
    Reciprocal,
    MeanDivision,
    MeanSubtraction,
    MeanDivisionLog,
    MeanSubtractionLog,
    Anscombe,
    Fisher,
    TSMinMaxScaler,
    MinMaxScaler,
    StandardScaler,
)


class TestTransformer(unittest.TestCase):
    """Test various tranformer classes"""

    @classmethod
    def setUpClass(test_class):
        r = np.random.RandomState(1234)
        test_class.data = r.randint(1000, size=(100, 2))
        test_class.data = test_class.data.astype("float64")
        test_class.state_less_transformers = [Log, Sqrt, Reciprocal, Anscombe, Fisher]
        test_class.state_full_transformers = [
            MeanDivision,
            MeanSubtraction,
            MeanDivisionLog,
            MeanSubtractionLog,
            TSMinMaxScaler,
        ]
        test_class.XY_Scalers = [MinMaxScaler, StandardScaler]

    @classmethod
    def tearDownClass(test_class):
        pass

    def test_fit_transform_inverse_transform_state_less(self):
        """
        check fit,transform,inverse_transform for state_less transformers.
        """
        test_class = self.__class__
        for transformer in test_class.state_less_transformers:
            data = copy.copy(test_class.data)
            tf = transformer(feature_columns=[0, 1], target_columns=[0, 1])
            fitted_tf = tf.fit(data)
            self.assertEqual(id(tf), id(fitted_tf))
            tf_data = fitted_tf.transform(data)
            self.assertEqual((100, 2), tf_data.shape)
            inv_tf_data = fitted_tf.inverse_transform(tf_data)
            self.assertEqual((100, 2), inv_tf_data.shape)
            if not isinstance(tf, Fisher):
                np.testing.assert_array_almost_equal(data, inv_tf_data, decimal=6)

    def test_fit_transform_inverse_transform_few_cols(self):
        """
        check fit,transform,inverse_transform for few cols.
        """
        test_class = self.__class__
        for transformer in test_class.state_less_transformers:
            data = copy.copy(test_class.data)
            tf = transformer(feature_columns=[1], target_columns=[1])
            fitted_tf = tf.fit(data)
            self.assertEqual(id(tf), id(fitted_tf))
            tf_data = fitted_tf.transform(data)
            self.assertEqual((100, 2), tf_data.shape)
            inv_tf_data = fitted_tf.inverse_transform(tf_data[:, [1]])
            self.assertEqual((100, 1), inv_tf_data.shape)
            if not isinstance(tf, Fisher):
                np.testing.assert_array_almost_equal(data[:, [1]], inv_tf_data, decimal=6)

    def test_fit_transform_inverse_transform_state_full_transformers(self):
        """
        check fit,transform,inverse_transform for state_full transformers.
        """
        test_class = self.__class__
        for transformer in test_class.state_full_transformers:
            data = copy.copy(test_class.data)
            tf = transformer(feature_columns=[0, 1], target_columns=[0, 1])
            fitted_tf = tf.fit(data)
            self.assertEqual(id(tf), id(fitted_tf))
            tf_data = fitted_tf.transform(data)
            self.assertEqual((100, 2), tf_data.shape)
            inv_tf_data = fitted_tf.inverse_transform(tf_data)
            self.assertEqual((100, 2), tf_data.shape)
            np.testing.assert_array_almost_equal(test_class.data, inv_tf_data, decimal=6)

    def test_xy_scalers(self):
        test_class = self.__class__
        for transformer in test_class.XY_Scalers:
            data = copy.copy(test_class.data)
            tf = transformer()
            fitted_tf = tf.fit(data)
            self.assertEqual(id(tf), id(fitted_tf))
            tf_data = fitted_tf.transform(data)
            self.assertEqual((100, 2), tf_data.shape)
            inv_tf_data = fitted_tf.inverse_transform(tf_data)
            self.assertEqual((100, 2), tf_data.shape)
            np.testing.assert_array_almost_equal(test_class.data, inv_tf_data, decimal=6)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
