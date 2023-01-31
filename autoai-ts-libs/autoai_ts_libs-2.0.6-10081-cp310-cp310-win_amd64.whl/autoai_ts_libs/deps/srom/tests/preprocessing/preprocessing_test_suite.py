# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""preprocessing test suite"""

import unittest
import sys

from timeseries.test_fft_filter import TestFFTFilter
from timeseries.test_guassianprocess_filter import TestGaussianProcessFilter
from timeseries.test_median_filter import TestMedianFilter
from timeseries.test_iqr_filter import TestIQRFilter
from timeseries.test_guassianwindow_filter import TestGaussianWindowFilter
from timeseries.test_grubbstest_filter import TestGrubbsTestFilter
from timeseries.test_localhistogram_filter import TestLocalHistogramFilter
from test_outlier_removal import TestOutlierRemoval
from test_robust_pca import TestRobustPCA
from test_asset_scaler import TestAssetScaler
from test_dataframe_scaler import TestDataframeScaler
from test_ts_transformer import TestTsTransformer
from timeseries.test_paa_sampler import TestPAASampler
from timeseries.test_sampler import TestSampler
from timeseries.test_sax_sampler import TestSAXSampler
from timeseries.test_percentile_sampler import TestPercentileSampler
from test_transformer import TestTransformer
from test_robust_gmm import TestRobustGGM

if __name__ == "__main__":
    TEST_CLASSES = [
        TestFFTFilter,
        TestGaussianProcessFilter,
        TestMedianFilter,
        TestIQRFilter,
        TestGaussianWindowFilter,
        TestGrubbsTestFilter,
        TestOutlierRemoval,
        TestLocalHistogramFilter,
        TestRobustPCA,
        TestAssetScaler,
        TestDataframeScaler,
        TestPAASampler,
        TestSampler,
        TestSAXSampler,
        TestPercentileSampler,
        TestTsTransformer,
        TestTransformer,
        TestRobustGGM,
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
        print("Status for execution of 'preprocessing' test suite: SUCCESS")
        print("*" * 80)
        sys.exit(0)
    else:
        print("Status for execution of 'preprocessing' test suite: FAILURE")
        print("*" * 80)
        sys.exit(1)
