# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2022 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.mSSA_moving_window import MssaMw
# srom.tests.anomaly_detection.
from autoai_ts_libs.deps.srom.tests.anomaly_detection.algorithms.data_generation.timeseries_generator import generate_seasonal_sawtooth_series, analyze_change_points

import numpy as np
import unittest


class TestMssaMw(unittest.TestCase):

    def test_sawtooth(self) -> None:
        """
        Tests moving window variant of mSSA against sawtooth time series. Should take under 0.4s to complete.
        :return:
        """
        # Best not to reseed BitGenerator => use numpy.random.default_rng() instead of numpy.random.seed()
        # See https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html
        rng = np.random.default_rng(1337)
        ts = generate_seasonal_sawtooth_series(number_of_cycles=120, jump_time_step=1250, noise_factor=0.1, rng=rng)
        model = MssaMw(distance_threshold=4, rows=10)
        change_points = model.fit_predict(ts)
        cpt = analyze_change_points(change_points)

        self.assertLess(np.sum(np.abs(np.asarray([1070, 1270]) - np.asarray(cpt))), 35)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
