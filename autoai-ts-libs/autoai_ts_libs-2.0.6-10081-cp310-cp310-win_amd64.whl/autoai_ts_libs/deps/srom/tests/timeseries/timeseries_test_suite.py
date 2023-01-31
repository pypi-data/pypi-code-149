"""Timeseries test suite"""

import unittest
import sys

from models.test_arima_model import TestARIMAModel
from models.test_m_t_2_r_forecaster import TestMT2RForecaster
from models.test_reservoir_forecaster import TestReservoirForecaster
from models.test_mean_model import TestMeanModel
from models.test_sarima_model import TestSARIMAModel
from models.test_t_2_r_forecaster import T2RForecaster
from models.test_zero_model import TestZeroModel
from utils.test_lookback import TestLookback
from utils.test_tsp_pipeline_collection import TestTSPPipelineCollection
from models.test_pipeline import TestForecaster
from models.test_pred_ad import TestPredAD
from models.test_window_ad import TestWindowAD
from models.test_reconstruct_ad import TestReconstructAD
from models.test_relationship_ad import TestRelationshipAD
from models.test_deep_ad import TestDeepAD
from utils.test_types import TestTypes
from utils.test_windowad_pipeline_collection import TestWindowADPipelineCollection
from utils.test_reconstructad_pipeline_collection import (
    TestReconstructADPipelineCollection,
)
from utils.test_relationshipad_pipeline_collection import (
    TestRelationshipADPipelineCollection,
)
from test_run_timeseries_anomaly import TestRunTimeseriesAnomaly
from models.test_holtwinters import TestHoltWinters
from utils.test_period_detection import TestPeriodDetection
from models.test_classifier import TestClassifier

if __name__ == "__main__":
    TEST_CLASSES = [
        TestClassifier,
        TestARIMAModel,
        TestMT2RForecaster,
        TestSARIMAModel,
        T2RForecaster,
        TestMeanModel,
        TestZeroModel,
        TestLookback,
        TestForecaster,
        TestPredAD,
        TestDeepAD,
        TestWindowAD,
        TestRelationshipAD,
        TestReconstructAD,
        TestTypes,
        TestWindowADPipelineCollection,
        TestReconstructADPipelineCollection,
        TestRelationshipADPipelineCollection,
        TestTSPPipelineCollection,
        TestRunTimeseriesAnomaly,
        TestHoltWinters,
        TestPeriodDetection,
        TestReservoirForecaster
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
        print("Status for execution of 'timeseries' test suite: SUCCESS")
        print("*" * 80)
        sys.exit(0)
    else:
        print("Status for execution of 'timeseries' test suite: FAILURE")
        print("*" * 80)
        sys.exit(1)
