# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""anomaly_detection test suite"""

import unittest
import sys

from algorithms.test_nearest_neighbor import TestNearestNeighborAnomalyModel
from algorithms.test_lof_nearest_neighbor import TestLOFNearestNeighborAnomalyModel
from algorithms.test_anomaly_graph_lasso import TestAnomalyGraphLasso
from algorithms.test_spad import TestSPAD
from algorithms.test_pca_q import TestAnomalyPCA_Q
from algorithms.test_pca_t2 import TestAnomalyPCA_T2
from algorithms.test_hotteling_t2 import TestHotellingT2
from algorithms.test_anomaly_robust_pca import TestAnomalyRobustPCA
from algorithms.test_cusum import TestCUSUM
from algorithms.test_ggm_pgscps import TestGraphPgscps
from algorithms.test_ggm_quic import TestGraphQUIC
from algorithms.test_anomaly_ensembler import TestAnomalyEnsembler
from algorithms.test_mSSA import TestMssa
from algorithms.test_extended_mincovdet import TestExtendedMinCovDet
from algorithms.test_mSSA_moving_window import TestMssaMw
from test_generalized_anomaly_model import TestGeneralizedAnomalyModel
from test_gaussian_graphical_anomaly_model import TestGaussianGraphicalModel
from test_anomaly_score_evaluation import TestAnomalyScoreEvaluation
from test_sliding_window_anomaly_model import TestSlidingWindowAnomalyModel
from test_unsupervised_anomaly_score_evaluation import (
    TestUnsupervisedAnomalyScoreEvaluation,
)
from algorithms.test_anomaly_pca import TestAnomalyPCA
from algorithms.test_kde import TestKDE
# from test_prediction_based_anomaly import TestPredictionBasedAnomaly
from algorithms.window_statistics.test_cost_discrepancy_checker import (
    TestCostDiscrepancyChecker,
)
from algorithms.window_statistics.test_grubbs_checker import TestGrubbsTestChecker
from algorithms.window_statistics.test_ttest_checker import TestTTestChecker
from algorithms.window_statistics.test_ktest_checker import TestKSTestChecker
from algorithms.window_statistics.test_mad_checker import (
    TestMedianAbsoluteDeviationChecker,
)
from algorithms.window_statistics.test_zscore_checker import TestZscoreChecker
from algorithms.window_statistics.test_sst_checker import TestSSTChecker
from algorithms.test_negative_sample_anomaly import TestNSA
from algorithms.test_neural_network_nsa import TestNeuralNetworkNSA
from algorithms.test_univariate_hotteling import TestUnivariateHotteling
from algorithms.test_sample_svdd import TestSampleSVDD
from algorithms.test_random_partition_forest import TestRandomPartitionForest
from algorithms.test_extended_isolation_forest import TestExtendedIsolationForest
from algorithms.test_gmm_outlier import TestGMMOutlier
from algorithms.test_bayesian_gmm_outlier import TestBayesianGMMOutlier
from algorithms.test_extended_spad import TestExtendedSPAD
from algorithms.test_oob import TestOOB
from algorithms.test_Covariance_anomaly import TestCovarianceAnomaly
from algorithms.test_NMT_anomaly import TestNMTAnomaly
from algorithms.test_hbos import TestHBOS
from algorithms.test_sparse_structure_learning import TestSparseStructureLearning
from algorithms.test_deep_isolation_forest import TestDeepIsolationForest
from algorithms.test_timeseries_isolation_forest import TestTSIsolationForest
if __name__ == "__main__":
    TEST_CLASSES = [
        TestAnomalyEnsembler,
        TestHBOS,
        TestSparseStructureLearning,
        TestKDE,
        TestNearestNeighborAnomalyModel,
        TestLOFNearestNeighborAnomalyModel,
        TestAnomalyGraphLasso,
        TestAnomalyPCA,
        TestAnomalyPCA_Q,
        TestAnomalyPCA_T2,
        TestHotellingT2,
        TestGeneralizedAnomalyModel,
        TestAnomalyRobustPCA,
        TestCUSUM,
        TestGaussianGraphicalModel,
        TestAnomalyScoreEvaluation,
        TestGraphPgscps,
        TestGraphQUIC,
        TestMssa,
        TestMssaMw,
        TestSlidingWindowAnomalyModel,
        TestCostDiscrepancyChecker,
        TestGrubbsTestChecker,
        TestTTestChecker,
        TestKSTestChecker,
        TestZscoreChecker,
        TestMedianAbsoluteDeviationChecker,
        # TestPredictionBasedAnomaly,
        TestNSA,
        TestUnivariateHotteling,
        TestSampleSVDD,
        TestRandomPartitionForest,
        TestExtendedIsolationForest,
        TestGMMOutlier,
        TestBayesianGMMOutlier,
        TestSPAD,
        TestExtendedSPAD,
        TestOOB,
        TestSSTChecker,
        TestNeuralNetworkNSA,
        TestUnsupervisedAnomalyScoreEvaluation,
        TestCovarianceAnomaly,
        TestNMTAnomaly,
        TestExtendedMinCovDet,
        TestDeepIsolationForest,
        TestTSIsolationForest
    ]

    LOADER = unittest.TestLoader()

    SUITES_LIST = []
    for test_class in TEST_CLASSES:
        SUITE = LOADER.loadTestsFromTestCase(test_class)
        SUITES_LIST.append(SUITE)

    TEST_SUITE = unittest.TestSuite(SUITES_LIST)

    RUNNER = unittest.TextTestRunner(verbosity=2, failfast=True)
    RESULTS = RUNNER.run(TEST_SUITE)
    # Print execution status and exit with related code for Jenkins
    print("*" * 80)
    if RESULTS.wasSuccessful():
        print("Status for execution of 'anomaly_detection' test suite: SUCCESS")
        print("*" * 80)
        sys.exit(0)
    else:
        print("Status for execution of 'anomaly_detection' test suite: FAILURE")
        print("*" * 80)
        sys.exit(1)
