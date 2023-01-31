# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Unit test cases for testing generalized anomaly model
"""
import os
import unittest
import copy
import numpy as np
import pandas as pd
import tempfile

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

from sklearn.exceptions import NotFittedError

from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms import LOFNearestNeighborAnomalyModel
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms import AnomalyGraphLasso


class TestGeneralizedAnomalyModel(unittest.TestCase):
    """Test class for TestGeneralizedAnomalyModel"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.base_learner = LOFNearestNeighborAnomalyModel(n_neighbors=2)
        cls.fit_function = "fit"
        cls.predict_function = "predict"
        cls.score_function = None
        cls.score_sign = -1
        cls.n_samples = np.array(
            [[-2, -1], [-1, -1], [-1, -2], [1, 1], [1, 2], [2, 1], [5, 3], [-4, 2]]
        )
        cls.testX = np.array([[-1, 0]])

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        files = os.listdir(".")
        for file in files:
            if file.endswith(".hdf5"):
                os.remove(file)

    def test_fit(self):
        """ Test fit method"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        fitted_model = gam.fit(test_class.n_samples)
        self.assertEqual(id(fitted_model), id(gam))

    def test_fit_with_none_base_learner(self):
        """ Test fit method with none base learner"""
        test_class = self.__class__
        gam = GeneralizedAnomalyModel(
            base_learner=None,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        self.assertRaises(RuntimeError, gam.fit, test_class.n_samples)

    def test_fit_with_dummy_fit_function(self):
        """ Test fit with dummy fit function"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            fit_function="dummy",
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        self.assertRaises(AttributeError, gam.fit, test_class.n_samples)

    def test_predict(self):
        """ Test predict method"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        gam.fit(test_class.n_samples)

        prediction = gam.predict(np.array([[5, 4]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 3), 1.0)

        prediction = gam.predict(np.array([[-1, 0]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 3), -1.0)

        # With pandas dataframe
        prediction = gam.predict(pd.DataFrame([[-1, 0]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 3), -1.0)

    def test_predict_without_training(self):
        """ Test predict method without training"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )

        self.assertRaises(NotFittedError, gam.predict, np.array([[5, 4]]))

    def test_predict_with_none_base_learner(self):
        """ Test predict method"""
        test_class = self.__class__
        gam = GeneralizedAnomalyModel(
            base_learner=None,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        self.assertRaises(RuntimeError, gam.predict, test_class.testX)

    def test_anomaly_scores(self):
        """ Test anomaly_scores """
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        gam.fit(test_class.n_samples)
        anomaly_scores = gam.anomaly_score(test_class.testX, np.array([[1, 0]]))
        self.assertIsNotNone(anomaly_scores)
        self.assertEqual(round(anomaly_scores[0], 3), -1.0)

    def test_anomaly_scores_with_nan_samples(self):
        """ Test anomaly_scores """
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        gam.fit(test_class.n_samples)
        anomaly_scores = gam.anomaly_score(np.array([[1, np.nan]]), np.array([[1, 0]]))
        self.assertIsNotNone(anomaly_scores)
        self.assertTrue(np.isnan(anomaly_scores[0]))

    def test_anomaly_scores_with_mixed_samples(self):
        """ Test anomaly_scores """
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        gam.fit(test_class.n_samples)
        anomaly_scores = gam.anomaly_score(
            np.array([[np.nan, np.nan], [-1, 1], [0, 1]]), np.array([[1, 0]])
        )
        self.assertIsNotNone(anomaly_scores)
        self.assertTrue(np.isnan(anomaly_scores[0]))
        self.assertEqual(round(anomaly_scores[1], 3), -1)
        self.assertEqual(round(anomaly_scores[2], 3), -1)

    def test_predict_with_diff_predict_function(self):
        """ Test predict with different predict function srom_log_liklihood"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function="srom_log_liklihood",
            score_sign=test_class.score_sign,
        )
        gam.fit(test_class.n_samples)
        self.assertRaises(
            AttributeError, gam.predict, np.array([[np.nan, np.nan], [-1, 1], [0, 1]])
        )

    def test_predict_with_diff_dummy_predict_function(self):
        """ Test predict with different dummy predict function"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function="dummy",
            score_sign=test_class.score_sign,
        )
        gam.fit(test_class.n_samples)
        prediction = gam.predict(np.array([[np.nan, np.nan], [-1, 1], [0, 1]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(len(prediction), 3)
        self.assertTrue(np.isnan(prediction).all())

    """
    def test_predict_with_diff_base_learner(self):
        Test predict with different predict function and base learner
        test_class = self.__class__
        gam = GeneralizedAnomalyModel(base_learner=AnomalyGraphLasso(),
                                      predict_function="srom_log_liklihood",
                                      score_sign=test_class.score_sign)
        gam.fit(test_class.n_samples)
        anomaly_scores = gam.predict(np.array([[np.nan, np.nan], [-1, 1], [0, 1]]))
    """

    def test_score(self):
        """ Test Score"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        gam.fit(test_class.n_samples)
        gam.set_scoring()
        score_value = gam.score(np.array([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(score_value, 1)

        score_value = gam.score(np.array([[1, -1]]), np.array([[1, 1]]))
        self.assertEqual(score_value, 1)

    def test_score_without_set_scoring(self):
        """ Test Score withot set_scoring"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        gam.fit(test_class.n_samples)
        self.assertRaises(Exception, gam.score, np.array([[5, 4]]), np.array([[1, 0]]))

    def test_set_params(self):
        """Test set_params method"""
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )

        gam.set_params(
            base_learner__n_neighbors=5,
            base_learner__algorithm="auto",
            base_learner__leaf_size=30,
            base_learner__metric="minkowski",
            base_learner__metric_params=None,
            base_learner__n_jobs=1,
        )
        gam.fit(test_class.n_samples)

        prediction = gam.predict(np.array([[-1, 0]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 2), -1.0)

        gam.base_learner = copy.deepcopy(test_class.base_learner)
        # base_learner__ not appened with parameters hence base learner is executed
        # with default parameters
        gam.set_params(
            neighbors=5,
            algorithm="auto",
            leaf_size=30,
            metric="minkowski",
            metric_params=None,
            n_jobs=1,
        )
        gam.fit(test_class.n_samples)
        prediction = gam.predict(np.array([[-1, 0]]))
        self.assertIsNotNone(prediction)
        self.assertEqual(round(prediction[0][0], 3), -1.0)

    def test_set_scoring_with_different_params_combination(self):
        """ Test set scoring """
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        gam.set_scoring(
            scoring_method="topk",
            scoring_metric="roc_auc",
            scoring_topk_param=5,
            score_validation=0.5,
        )
        gam.fit(test_class.n_samples)
        self.assertRaises(Exception, gam.score, np.array([[5, 4]]), np.array([[1, 0]]))

        gam.set_scoring(
            scoring_method="topk",
            scoring_metric="pr_auc",
            scoring_topk_param=5,
            score_validation=0.5,
        )
        gam.fit(test_class.n_samples)
        self.assertRaises(Exception, gam.score, np.array([[5, 4]]), np.array([[1, 0]]))

        gam.set_scoring(
            scoring_method="topk",
            scoring_metric="dummy",
            scoring_topk_param=5,
            score_validation=0.5,
        )
        gam.fit(test_class.n_samples)
        self.assertRaises(Exception, gam.score, np.array([[5, 4]]), np.array([[1, 0]]))

        gam.set_scoring(
            scoring_method="topk",
            scoring_metric="anomaly_f1",
            scoring_topk_param=5,
            score_validation=0.5,
        )
        gam.fit(test_class.n_samples)
        score_value = gam.score(np.array([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(score_value, 1)

        gam.set_scoring(
            scoring_method="topk",
            scoring_metric="anomaly_acc",
            scoring_topk_param=5,
            score_validation=0.7,
        )
        gam.fit(test_class.n_samples)
        score_value = gam.score(np.array([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(score_value, 1)

        gam.set_scoring(
            scoring_method="topk",
            scoring_metric="anomaly_acc",
            scoring_topk_param=0,
            score_validation=0.5,
        )
        gam.fit(test_class.n_samples)
        self.assertRaises(Exception, gam.score, np.array([[5, 4]]), np.array([[1, 0]]))

        gam.set_scoring(
            scoring_method="average",
            scoring_metric="anomaly_acc",
            scoring_topk_param=5,
            score_validation=0.5,
        )
        gam.fit(test_class.n_samples)
        score_value = gam.score(np.array([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(score_value, 1)

        gam.set_scoring(
            scoring_method="average",
            scoring_metric="anomaly_f1",
            scoring_topk_param=5,
            score_validation=0.5,
        )
        gam.fit(test_class.n_samples)
        score_value = gam.score(np.array([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(score_value, 1)

    def test_get_score(self):
        """ Test get score """
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        gam.set_scoring()
        gam.fit(test_class.n_samples)
        score_value = gam.score(np.array([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(score_value, gam.get_best_score())

    def test_get_score_without_scoring(self):
        """ Test get score """
        test_class = self.__class__
        base_learner = copy.deepcopy(test_class.base_learner)
        gam = GeneralizedAnomalyModel(
            base_learner=base_learner,
            predict_function=test_class.predict_function,
            score_sign=test_class.score_sign,
        )
        self.assertIsNone(gam.get_best_score())


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
