# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Test Runner for imputation test suite
"""
import sys
import unittest

from test_metrics import TestMetrics
from test_cv_scores import TestCVScores
from test_cv_scores_pipeline_utils import TestCVScoresPipelineUtils
from test_decomposition_imputers import TestDecompositionImputers
from test_flatten_imputers import TestFlattenImputers
from test_imputation import TestImputation
from test_imputation_time_series_methods import TestImputationTimeSeries
from test_interpolaters import TestInterpolators
from test_predictive_imputers import TestPredictiveImputers
from ts_imputer.test_ts_fast_PCP_imputer import TestTSFastPCPImputer
from ts_imputer.test_ts_local_reg_imputer import TestTSLocalRegImputer
from ts_imputer.test_ts_mul_var_base_imputer import TestTSMulVarBaseImputer
from ts_imputer.test_ts_mul_var_simple_imputer import TestMulVarSimpleImputer

if __name__ == "__main__":
    TEST_CLASSES = [
        TestMetrics,
        TestCVScores,
        TestCVScoresPipelineUtils,
        TestImputation,
        TestImputationTimeSeries,
        TestInterpolators,
        TestDecompositionImputers,
        TestPredictiveImputers,
        TestFlattenImputers,
        TestTSFastPCPImputer,
        TestTSLocalRegImputer,
        TestTSMulVarBaseImputer,
        TestMulVarSimpleImputer,
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
        print("Status for execution of 'imputation' test suite: SUCCESS")
        print("*" * 80)
        sys.exit(0)
    else:
        print("Status for execution of 'imputation' test suite: FAILURE")
        print("*" * 80)
        sys.exit(1)
