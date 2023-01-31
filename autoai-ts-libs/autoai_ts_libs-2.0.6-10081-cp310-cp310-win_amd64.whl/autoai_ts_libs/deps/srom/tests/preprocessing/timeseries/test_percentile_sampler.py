import unittest
from autoai_ts_libs.deps.srom.preprocessing.timeseries.percentile_sampler import PercentileApproximator
from autoai_ts_libs.deps.srom.tests.datasets.sample_data import ts_2dim

class TestPercentileSampler(unittest.TestCase):
    """Test class for Percentile Sampler"""

    @classmethod
    def setUpClass(cls):
        """Setup class"""
        cls.percentile_sampler = PercentileApproximator(n_bins=6)

    def testPercentileSamplerSetup(self):
        """Test init method"""
        class_obj = self.__class__
        percentile_sampler = class_obj.percentile_sampler
        self.assertIsNotNone(percentile_sampler)

    def testPercentileSamplerFitTransform(self):
        """Test fit_transform method"""
        class_obj = self.__class__
        percentile_sampler = class_obj.percentile_sampler
        sampled_data = percentile_sampler.fit_transform(ts_2dim)
        self.assertIsNotNone(sampled_data)
        self.assertEqual(sampled_data.shape, ts_2dim.shape)

    def testPercentileSamplerInverseTransform(self):
        """Test inverse_transform method"""
        class_obj = self.__class__
        percentile_sampler = class_obj.percentile_sampler
        inverse_transformed_data = percentile_sampler.inverse_transform(
            percentile_sampler.fit_transform(ts_2dim)
        )
        self.assertIsNotNone(inverse_transformed_data)
        self.assertEqual(inverse_transformed_data.shape, ts_2dim.shape)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
