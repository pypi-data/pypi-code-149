""" Test Augments. """
import unittest
import numpy as np
from autoai_ts_libs.deps.srom.time_series.augmentor import (
    Jitter,
    TrendOutlier,
    Noise,
    ExtremeOutlier,
    VarianceOutlier,
)


class TestAugmentors(unittest.TestCase):
    """class for testing augmentors"""

    @classmethod
    def setUp(cls):
        cls.augmentors = [
            Jitter(),
            TrendOutlier(outlier_factor=30),
            Noise(),
            ExtremeOutlier(),
            VarianceOutlier(),
        ]
        mu, sigma = 0, 0.1  # mean and standard deviation
        rs = np.random.RandomState(32)
        cls.X = rs.normal(mu, sigma, 50)
        cls.X = cls.X.reshape(-1, 1)

    def test_fit(self):
        """Tests fit method"""
        test_class = self.__class__
        augmentors = test_class.augmentors
        for augmentor in augmentors:
            fitted_aug = augmentor.fit(test_class.X)
            self.assertEqual(augmentor, fitted_aug)

    def test_transform(self):
        """Tests transform method"""
        test_class = self.__class__
        augmentors = test_class.augmentors
        scores = [0.016945, 27.017710, 0.016378, 0.000005, -0.000658]
        for idx, augmentor in enumerate(augmentors):
            fitted_aug = augmentor.fit(test_class.X)
            tf_x = fitted_aug.transform(test_class.X)
            self.assertEqual(tf_x.shape, test_class.X.shape)
            self.assertFalse((tf_x == test_class.X).all())
            self.assertAlmostEqual(scores[idx], np.mean(tf_x), places=6)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
