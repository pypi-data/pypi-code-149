# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Unit test cases for testing anomaly score evaluation
"""
import unittest
import numpy as np
import pandas as pd

from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms import LOFNearestNeighborAnomalyModel
from autoai_ts_libs.deps.srom.anomaly_detection.anomaly_score_evaluation import AnomalyScoreEvaluator


class TestAnomalyScoreEvaluation(unittest.TestCase):
    """Test class for TestAnomalyScoreEvaluation"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.scoring_method = "average"
        cls.scoring_metric = "anomaly_f1"
        cls.scoring_topk_param = 5
        cls.score_validation = 0.5

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

    def test_score(self):
        """ Test score """
        test_class = self.__class__
        ase = AnomalyScoreEvaluator(
            test_class.scoring_method,
            test_class.scoring_metric,
            test_class.scoring_topk_param,
            test_class.score_validation,
        )
        gam = GeneralizedAnomalyModel(
            base_learner=LOFNearestNeighborAnomalyModel(n_neighbors=2),
            predict_function="predict",
            score_sign=1,
        )
        gam.fit(test_class.n_samples)
        best_score = ase.score(gam.predict(np.array([[5, 4]])), np.array([[1, 0]]))
        self.assertEqual(best_score, 1)

        # With None anomaly scores
        best_score = ase.score(None, np.array([[1, 0]]))
        self.assertEqual(best_score, 0)

        # With anomaly scores shape less than 1 or equal to 1
        best_score = ase.score(np.array([5, 4]), np.array([1, 0]))
        self.assertEqual(best_score, 1)

        # With pandas series
        best_score = ase.score(pd.Series([5, 4]), np.array([[1, 0]]))
        self.assertEqual(best_score, 1)

        # With pandas dataframe
        best_score = ase.score(pd.DataFrame([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(best_score, 0.5)

        # With numpy array
        best_score = ase.score(np.array([[5, 4]]), np.array([[1, 0]]))
        self.assertEqual(best_score, 0.5)

    def test_score_with_diff_scoring_metric(self):
        """ Test score with different scoring metric"""
        test_class = self.__class__
        scoring_metric_list = ["roc_auc", "anomaly_f1", "anomaly_acc", "pr_auc"]
        best_score_list = []
        gam = GeneralizedAnomalyModel(
            base_learner=LOFNearestNeighborAnomalyModel(n_neighbors=2),
            predict_function="predict",
            score_sign=-1,
        )

        for _, metric in enumerate(scoring_metric_list):
            ase = AnomalyScoreEvaluator(
                test_class.scoring_method,
                metric,
                test_class.scoring_topk_param,
                test_class.score_validation,
            )
            gam.fit(test_class.n_samples)
            best_score = ase.score(gam.predict(np.array([[5, 4]])), np.array([[1, 0]]))
            best_score_list.append(best_score)
        self.assertEqual(len(set(best_score_list)), 1)

        ase = AnomalyScoreEvaluator(
            "topk", "anomaly_f1", 0, test_class.score_validation
        )
        gam.fit(test_class.n_samples)
        self.assertRaises(
            Exception, ase.score, gam.predict(np.array([[5, 4]])), np.array([[1, 0]])
        )

        best_score_list = []
        for _, metric in enumerate(scoring_metric_list):
            ase = AnomalyScoreEvaluator(
                "topk",
                metric,
                test_class.scoring_topk_param,
                test_class.score_validation,
            )
            gam.fit(test_class.n_samples)
            best_score = ase.score(gam.predict(np.array([[5, 4]])), np.array([[1, 0]]))
            best_score_list.append(best_score)
        self.assertEqual(len(set(best_score_list)), 1)

        ase = AnomalyScoreEvaluator(
            "dummy", "anomaly_f1", 0, test_class.score_validation
        )
        gam.fit(test_class.n_samples)
        best_score = ase.score(gam.predict(np.array([[5, 4]])), np.array([[1, 0]]))
        self.assertEqual(best_score, 0)

    def test_get_best_thresholds(self):
        """ Test get best thresholds """
        test_class = self.__class__
        scoring_metric_list = ["roc_auc", "pr_auc"]
        for _, metric in enumerate(scoring_metric_list):
            ase = AnomalyScoreEvaluator(
                test_class.scoring_method,
                metric,
                test_class.scoring_topk_param,
                test_class.score_validation,
            )
            self.assertRaises(Exception, ase.get_best_thresholds)

        scoring_metric_list = ["anomaly_f1", "anomaly_acc"]
        for _, metric in enumerate(scoring_metric_list):
            ase = AnomalyScoreEvaluator(
                test_class.scoring_method,
                metric,
                test_class.scoring_topk_param,
                test_class.score_validation,
            )
            gam = GeneralizedAnomalyModel(
                base_learner=LOFNearestNeighborAnomalyModel(n_neighbors=2),
                predict_function="predict",
                score_sign=-1,
            )
            gam.fit(test_class.n_samples)
            ase.score(gam.predict(np.array([[5, 4]])), np.array([[1, 0]]))
            best_thresholds = ase.get_best_thresholds()
            self.assertEqual(round(best_thresholds[0], 3), 1.0)

        # With dummy scoring metric
        ase = AnomalyScoreEvaluator(
            test_class.scoring_method,
            "dummy",
            test_class.scoring_topk_param,
            test_class.score_validation,
        )
        self.assertRaises(Exception, ase.get_best_thresholds)

    def test_score_with_diff_topk_param(self):
        """ Test score with different topk param"""
        test_class = self.__class__
        ase = AnomalyScoreEvaluator(
            "topk", test_class.scoring_metric, 500, test_class.score_validation
        )
        gam = GeneralizedAnomalyModel(
            base_learner=LOFNearestNeighborAnomalyModel(n_neighbors=2),
            predict_function="predict",
            score_sign=1,
        )
        gam.fit(test_class.n_samples)
        best_score = ase.score(gam.predict(np.array([[5, 4]])), np.array([[1, 0]]))
        self.assertEqual(best_score, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
