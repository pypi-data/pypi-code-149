# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""wml test suite"""

import unittest
import sys
from test_pipeline_skeleton import TestPipelineSkeleton
from test_anomaly_service import TestAnomalyWMLTrainer
from test_wml_scorer import TestWMLScorer
from test_wml_trainer import TestWMLtrainer


if __name__ == "__main__":
    TEST_CLASSES = [
        TestPipelineSkeleton,
        # TestWMLScorer,
        TestWMLtrainer,
        TestAnomalyWMLTrainer,
    ]

    LOADER = unittest.TestLoader()

    SUITES_LIST = []
    for test_class in TEST_CLASSES:
        SUITE = LOADER.loadTestsFromTestCase(test_class)
        SUITES_LIST.append(SUITE)

    TEST_SUITE = unittest.TestSuite(SUITES_LIST)

    RUNNER = unittest.TextTestRunner(verbosity=2, failfast=True)
    RESULTS = RUNNER.run(TEST_SUITE)
    print("*" * 80)
    if RESULTS.wasSuccessful():
        print("Status for execution of 'wml' test suite: SUCCESS")
        print("*" * 80)
        sys.exit(0)
    else:
        print("Status for execution of 'wml' test suite: FAILURE")
        print("*" * 80)
        sys.exit(1)
