# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Unit test cases for testing gaussian graphical model
"""
import unittest
import copy
import numpy as np
import pandas as pd

from sklearn.exceptions import NotFittedError
from autoai_ts_libs.deps.srom.anomaly_detection.gaussian_graphical_anomaly_model import (
    GaussianGraphicalModel
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms import AnomalyGraphLasso
from sklearn.base import TransformerMixin


class TestGaussianGraphicalModel(unittest.TestCase):
    """Test class for TestGaussianGraphicalModel"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.base_learner = AnomalyGraphLasso(alpha=0.5)
        cls.sliding_window_size = 2
        cls.distance_metric = "KL_Divergence"
        cls.sliding_window_data_cutoff = 0.5
        cls.scale = True
        cls.n_samples = np.array(
            [[-2, -1], [-1, -1], [-1, -2], [1, 1], [1, 2], [2, 1], [5, 3], [-4, 2]]
        )
        cls.n_samples_dataframe = pd.DataFrame(
            [[-2, -1], [-1, -1], [-1, -2], [1, 1], [1, 2], [2, 1], [5, 3], [-4, 2]]
        )
        cls.testX = np.array([[-1, 0]])

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """ Test fit method"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=test_class.sliding_window_size,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        fitted_model = ggm.fit(test_class.n_samples)
        self.assertEqual(id(fitted_model), id(ggm))

    def test_fit_with_none_base_learner(self):
        """ Test fit method with none base learner"""
        test_class = self.__class__
        ggm = GaussianGraphicalModel(
            base_learner=None,
            distance_metric=test_class.distance_metric,
            sliding_window_size=test_class.sliding_window_size,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        self.assertRaises(RuntimeError, ggm.fit, test_class.n_samples)

    def test_fit_with_pandas_dataframe(self):
        """ Test fit method with pandas dataframe"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=test_class.sliding_window_size,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        fitted_model = ggm.fit(test_class.n_samples_dataframe)
        self.assertEqual(id(fitted_model), id(ggm))

    def test_fit_with_bad_data(self):
        """ Test fit method with bad data"""
        test_class = self.__class__
        ggm = GaussianGraphicalModel(
            base_learner=TransformerMixin(),
            distance_metric=test_class.distance_metric,
            sliding_window_size=test_class.sliding_window_size,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        self.assertRaises(Exception, ggm.fit, np.array([[2, -1], [-1, -2]]))

    def test_fit_with_scale_equals_false(self):
        """ Test fit method with scale=False"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=test_class.sliding_window_size,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=False,
        )
        fitted_model = ggm.fit(test_class.n_samples_dataframe)
        self.assertEqual(id(fitted_model), id(ggm))

    def test_predict_with_n_samples_greater_than_window_size(self):
        """ Test predict method with n_samples greater than window size"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=10,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        self.assertRaises(Exception, ggm.predict, np.array([[-2, -1]]))

    def test_predict_without_training(self):
        """ Test predict method without training"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=test_class.sliding_window_size,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )

        self.assertRaises(NotFittedError, ggm.predict, np.array([[5, 4]]))

    def test_predict(self):
        """ Test predict method"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=0,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[5, 4]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 3), 0.919)

        # With pandas dataframe
        prediction = ggm.predict(pd.DataFrame([[-1, 0]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 3), 0.919)

        # With sliding window size 0 and scale False
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=0,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=False,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[5, 4]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 3), 5.538)
        self.assertEqual(round(prediction[0][1], 3), 5.355)

        # With sliding window size greater than 0
        # With default distance metric
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertEqual(round(prediction[1][0], 3), 0.189)
        self.assertEqual(round(prediction[1][1], 3), 0.189)

        # With default distance metric and scale False
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=False,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertEqual(round(prediction[1][0], 3), 11.152)
        self.assertEqual(round(prediction[1][1], 3), 3.844)

        # with different distance metric Stochastic_Nearest_Neighbors
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric="Stochastic_Nearest_Neighbors",
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertEqual(round(prediction[1][0], 3), 0.550)
        self.assertEqual(round(prediction[1][1], 3), 0.424)

        # with different distance metric KL_Divergence_Dist
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric="KL_Divergence_Dist",
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertEqual(round(prediction[1][0], 3), 3.150)
        self.assertEqual(round(prediction[1][1], 3), 3.150)

        # with different distance metric Frobenius_Norm
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric="Frobenius_Norm",
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertEqual(round(prediction[1][0], 3), 0.25)
        self.assertEqual(round(prediction[1][1], 3), 0.25)

        # with different distance metric Likelihood
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric="Likelihood",
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertEqual(round(prediction[1][0], 3), -3.041)
        self.assertEqual(round(prediction[1][1], 3), -3.041)

        # with different distance metric Spectral
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric="Spectral",
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertEqual(round(prediction[1][0], 3), 0.125)
        self.assertEqual(round(prediction[1][1], 3), 0.125)

        # with different distance metric Mahalanobis_Distance
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric="Mahalanobis_Distance",
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertGreaterEqual(round(prediction[1][0], 2), 3.90)
        self.assertGreaterEqual(round(prediction[1][1], 2), 3.90)

        # With dummy distance metric
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric="dummy",
            sliding_window_size=2,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        self.assertRaises(
            NotImplementedError, ggm.predict, np.array([[-1, 0], [-2, -1]])
        )

        # Minimum sliding window should be 2; else it throws error. Hence it gives nan as output
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=1,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertTrue(np.isnan(prediction[1][0]))
        self.assertTrue(np.isnan(prediction[1][1]))

        # With sliding_window_data_cutoff greater than test data shape, hence scores are nan
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=2,
            sliding_window_data_cutoff=10,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0], [-2, -1]]))
        self.assertTrue(np.isnan(prediction[1][0]))
        self.assertTrue(np.isnan(prediction[1][1]))

    def test_score(self):
        """ Test Score"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=0,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        ggm.set_scoring()
        score_value = ggm.score(np.array([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(score_value, 0.5)

        score_value = ggm.score(np.array([[1, -1]]), np.array([[1, 1]]))
        self.assertEqual(score_value, 1)

    def test_score_without_set_scoring(self):
        """ Test Score withot set_scoring"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=0,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        self.assertRaises(Exception, ggm.score, np.array([[5, 4]]), np.array([[1, 0]]))

    def test_set_params(self):
        """Test set_params method"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=0,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )

        ggm.set_params(
            base_learner__alpha=0.1,
            base_learner__mode="cd",
            base_learner__tol=0.0001,
            base_learner__enet_tol=0.0001,
            base_learner__max_iter=100,
        )
        ggm.fit(test_class.n_samples)

        prediction = ggm.predict(np.array([[-1, 0]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 2), 0.84)

        ggm.base_learner = copy.deepcopy(test_class.base_learner)
        # base_learner__ not appened with parameters hence base learner is executed
        # with default parameters
        ggm.set_params(alpha=0.1, mode="cd", tol=0.0001, enet_tol=0.0001, max_iter=100)
        ggm.fit(test_class.n_samples)
        prediction = ggm.predict(np.array([[-1, 0]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 3), 0.919)

    def test_get_best_thresholds(self):
        """ Test get best thresholds"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=0,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        ggm.fit(test_class.n_samples)
        ggm.set_scoring()
        ggm.score(np.array([[5, 4]]), np.array([[1, 0]]))
        best_thresholds = ggm.get_best_thresholds()
        self.assertEqual(round(best_thresholds[0], 1), 0.9)
        self.assertEqual(round(best_thresholds[1], 1), 0.9)

        # With out scoring get the best thresholds
        ggm = GaussianGraphicalModel(
            base_learner=base_learner,
            distance_metric=test_class.distance_metric,
            sliding_window_size=0,
            sliding_window_data_cutoff=test_class.sliding_window_data_cutoff,
            scale=test_class.scale,
        )
        self.assertIsNone(ggm.get_best_thresholds())


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
