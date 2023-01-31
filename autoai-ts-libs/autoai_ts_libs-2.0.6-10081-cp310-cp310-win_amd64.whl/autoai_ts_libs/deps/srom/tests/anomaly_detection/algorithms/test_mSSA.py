# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2022 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.mSSA import Mssa
# srom.tests.anomaly_detection.
from autoai_ts_libs.deps.srom.tests.anomaly_detection.algorithms.data_generation.timeseries_generator import \
    analyze_change_points, generate_seasonal_sawtooth_series, generate_change_in_periodicity, generate_outlier_series,\
    generate_change_in_mean_series

import numpy as np
import unittest


class TestMssa(unittest.TestCase):

    def test_simple_synthetic(self) -> None:
        # Create the model
        model = Mssa(distance_threshold=5, rows=5)

        # Create synthetic time series data
        ts = np.ones([4000, 3]) * [1, 2, 3]
        ts[:1000, :] = ts[:1000, :] / 0.5
        # print(ts)

        # Detection
        cp = model.fit_predict(ts)

        # Print detected output
        # print("change point vector = ", cp)
        # print("change point (t) = ", np.where(cp == -1)[0][0])

        true_cp_t = [1005]
        self.assertListEqual(np.where(cp == -1)[0].tolist(), true_cp_t)

    def test_sawtooth(self) -> None:
        # Best not to reseed BitGenerator => use numpy.random.default_rng() instead of numpy.random.seed()
        # See https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html
        rng = np.random.default_rng(1337)
        ts = generate_seasonal_sawtooth_series(rng=rng)
        model = Mssa(distance_threshold=5, rows=5)
        change_points = model.fit_predict(ts)
        cpt = analyze_change_points(change_points)

        # Using threshold to be robust against randomness, even though seeding (P)RNG should also take care of this
        self.assertLess(np.sum(np.abs(np.asarray([265]) - np.asarray(cpt))), 10)

    def test_change_in_mean(self) -> None:
        rng = np.random.default_rng(1337)
        ts = generate_change_in_mean_series(simple=True, rng=rng)
        model = Mssa(distance_threshold=5, rows=5)
        change_points = model.fit_predict(ts)
        cpt = analyze_change_points(change_points)

        self.assertLess(np.sum(np.abs(np.asarray([205, 415]) - np.asarray(cpt))), 25)

    def test_change_in_periodicity(self) -> None:
        rng = np.random.default_rng(1337)
        ts = generate_change_in_periodicity(rng=rng)
        model = Mssa(distance_threshold=5, rows=5)
        change_points = model.fit_predict(ts)
        cpt = analyze_change_points(change_points)

        self.assertLess(np.sum(np.abs(np.asarray([485, 805]) - np.asarray(cpt))), 25)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
