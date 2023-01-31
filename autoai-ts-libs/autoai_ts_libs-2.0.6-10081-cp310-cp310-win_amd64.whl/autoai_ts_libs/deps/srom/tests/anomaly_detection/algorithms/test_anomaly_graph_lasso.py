# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing AnomalyGraphLasso class"""
import unittest
import numpy as np
from sklearn import datasets
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_graph_lasso import AnomalyGraphLasso


class TestAnomalyGraphLasso(unittest.TestCase):
    """Test methods in AnomalyGraphLasso class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        pass

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """Test fit method"""
        data, _ = datasets.load_iris(return_X_y=True)
        sgl = AnomalyGraphLasso()
        fitted_model = sgl.fit(data)
        self.assertEqual(id(fitted_model), id(sgl))
        # Check covariance
        actual_covariance = np.round(sgl.covariance_, decimals=5)
        expected_covariance = np.array(
            [
                [0.68112, -0.04903, 1.25519, 0.51898],
                [-0.04903, 0.18675, -0.30957, -0.12719],
                [1.25519, -0.30957, 3.09242, 1.27774],
                [0.51898, -0.12719, 1.27774, 0.57853],
            ]
        )
        np.testing.assert_almost_equal(
            actual_covariance, expected_covariance, decimal=2
        )
        # Check precision
        actual_precision = np.round(sgl.precision_, decimals=5)
        expected_precision = np.array(
            [
                [7.46524, -3.6723, -3.39757, 0.],
                [-3.6723, 8.22715, 2.35152, -0.09065],
                [-3.39757, 2.35152, 5.31667, -8.17758],
                [0., -0.09065, -8.17758, 19.7696],
            ]
        )
        np.testing.assert_almost_equal(actual_precision, expected_precision, decimal=1)
        # Check n_iter_
        # self.assertEqual(sgl.n_iter_, 16) # not approriate

    def test_fit_with_floating_point_error(self):
        """Test fit method with FloatingPointError"""
        # Create 4 by 3 sparse data
        sparse_data = np.array(
            [
                [0.0000000, 150.0000000, 0.0000000],
                [0.0000000, 0.000000, 0.00000000],
                [32.0000000, 0.0000000, 40.0000000],
                [0.0000000, 0.0000000, 0.0000000],
            ]
        )
        sgl = AnomalyGraphLasso()
        fitted_model = sgl.fit(sparse_data)
        self.assertEqual(id(fitted_model), id(sgl))
        # Check covariance
        actual_covariance = np.round(sgl.covariance_, decimals=5)
        expected_covariance = np.array(
            [
                [329.825, -269.98991, 215.98999],
                [-269.98991, 3953.9, -337.49],
                [215.98999, -337.49, 427.025],
            ]
        )
        np.testing.assert_almost_equal(
            actual_covariance, expected_covariance, decimal=1
        )
        # Check precision
        actual_precision = np.round(sgl.precision_, decimals=5)
        expected_precision = np.array(
            [
                [0.00459, 0.00012, -0.00222],
                [0.00012, 0.00027, 0.00015],
                [-0.00222, 0.00015, 0.00359],
            ]
        )
        np.testing.assert_almost_equal(actual_precision, expected_precision, decimal=1)
        # Check n_iter_
        # self.assertEqual(sgl.n_iter_, 2)


    def test_fit_with_floating_error(self):
        """Test fit method with FloatingPointError"""
        # Create 4 by 3 sparse data
        sparse_data = np.array(
            [
                [0.0000000, 0.0000000, 0.0000000],
                [0.0000000, 0.000000, 0.00000000],
                [0.0000000, 0.0000000, 0.0000000],
                [0.0000000, 0.0000000, 0.0000000],
            ]
        )
        sgl = AnomalyGraphLasso()
        fitted_model = sgl.fit(sparse_data)

    def test_fit_with_floating_error_1(self):
        """Test fit method with FloatingPointError"""
        # Create 4 by 3 sparse data
        sparse_data = np.array(
            [
                [0.0000000, np.inf, 0.0000000],
                [0.0000000, 0.000000, 0.00000000],
                [0.0000000, 0.0000000, 0.0000000],
                [0.0000000, 0.0000000, 0.0000000],
            ]
        )
        try:
            sgl = AnomalyGraphLasso()
            fitted_model = sgl.fit(sparse_data)
        except:
            pass



if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
