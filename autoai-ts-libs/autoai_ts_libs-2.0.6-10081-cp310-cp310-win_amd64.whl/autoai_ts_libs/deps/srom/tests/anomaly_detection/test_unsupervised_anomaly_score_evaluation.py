# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Unit test cases for testing unsupervised anomaly score evaluation
"""
import unittest
import numpy as np
import pandas as pd

from sklearn.svm import OneClassSVM
from autoai_ts_libs.deps.srom.anomaly_detection.unsupervised_anomaly_score_evaluation import (
    unsupervised_anomaly_cross_val_score,
    EM_score_parameter,
    MV_score_parameter,
    AL_score_parameter,
)


class TestUnsupervisedAnomalyScoreEvaluation(unittest.TestCase):
    """Test class for UnsupervisedAnomalyScoreEvaluation"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        pass

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_unsupervised_anomaly_cross_val_score(self):
        """Test unsupervised_anomaly_cross_val_score"""
        test_class = self.__class__
        clf = OneClassSVM()
        X = np.linspace(0, 3, num=20)
        X = X.reshape(-1, 1)
        mv_score_val = unsupervised_anomaly_cross_val_score(clf, X, scoring="em_score")
        self.assertIsNotNone(mv_score_val)
        em_score_val = unsupervised_anomaly_cross_val_score(clf, X, scoring="mv_score")
        self.assertIsNotNone(em_score_val)
        al_score_val = unsupervised_anomaly_cross_val_score(clf, X, scoring="al_score")
        self.assertIsNotNone(al_score_val)

    def test_EM_score_parameter(self):
        """test EM_score_parameter function."""
        x = np.linspace(0, 3, num=20)
        x = x.reshape(-1, 1)
        clf = OneClassSVM().fit(x)
        n_generated = 10000
        t_max = 0.9
        alpha_min = np.min(x)
        alpha_max = np.max(x)
        scorer = EM_score_parameter(alpha_min, alpha_max, 1, n_generated, t_max)
        self.assertIsNotNone(scorer(clf, x))

    def test_MV_score_parameter(self):
        """test MV_score_parameter function."""
        x = np.linspace(0, 3, num=20)
        x = x.reshape(-1, 1)
        clf = OneClassSVM().fit(x)
        n_generated = 10000
        t_max = 0.9
        alpha_min = np.min(x)
        alpha_max = np.max(x)
        scorer = MV_score_parameter(
            alpha_min, alpha_max, x.shape[1], n_generated, 0.9, 0.999
        )
        self.assertIsNotNone(scorer(clf, x))

    def test_AL_score_parameter(self):
        """test AL_score_parameter function."""
        x = np.linspace(0, 3, num=20)
        x = x.reshape(-1, 1)
        clf = OneClassSVM().fit(x)
        scorer = AL_score_parameter(x, 1, 10000, 0.9, 0.999)
        self.assertIsNotNone(scorer(clf, x))


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
