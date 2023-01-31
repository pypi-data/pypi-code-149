# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Test Runner for optimization test suite
"""
import unittest
import sys

from test_optimization import TestOptimization
from test_optimization_parallel import TestOptimizationParallel
#from test_optimization_spark import TestOptimizationSpark
from test_non_linear_optimizer import TestNonLinearOptimizer
from nlopt.test_constraints import TestMaxBoundFunctor, TestMinBoundFunctor
from nlopt.test_utils import TestUtils
from nlopt.test_nlopt import TestNLOptimizer
from test_optimization_wml_adapters import TestOptimizersWithWMLAdapter

if __name__ == "__main__":
    TEST_CLASSES = [
        TestOptimizersWithWMLAdapter,
        TestOptimization,
        TestOptimizationParallel,
        #TestOptimizationSpark,
        TestNonLinearOptimizer,
        TestMinBoundFunctor,
        TestMaxBoundFunctor,
        TestUtils,
        TestNLOptimizer,
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
        print("Status for execution of 'optimization' test suite: SUCCESS")
        print("*" * 80)
        sys.exit(0)
    else:
        print("Status for execution of 'optimization' test suite: FAILURE")
        print("*" * 80)
        sys.exit(1)
