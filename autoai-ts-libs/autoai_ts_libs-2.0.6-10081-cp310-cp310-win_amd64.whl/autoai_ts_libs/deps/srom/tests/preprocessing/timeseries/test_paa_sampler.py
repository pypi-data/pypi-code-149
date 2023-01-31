import unittest
from autoai_ts_libs.deps.srom.preprocessing.timeseries.paa_sampler import PiecewiseAggregateApproximation
from autoai_ts_libs.deps.srom.tests.datasets.sample_data import ts_2dim


class TestPAASampler(unittest.TestCase):
    """Test class for PAA Sampler"""

    @classmethod
    def setUpClass(cls):
        """Setup class"""
        cls.paa_sampler = PiecewiseAggregateApproximation(n_segments=6)

    def testPAASamplerSetup(self):
        """Test init method"""
        class_obj = self.__class__
        paa_sampler = class_obj.paa_sampler
        self.assertIsNotNone(paa_sampler)

    def testPAASamplerFitTransform(self):
        """Test fit_transform method"""
        class_obj = self.__class__
        paa_sampler = class_obj.paa_sampler
        sampled_data = paa_sampler.fit_transform(ts_2dim)
        self.assertIsNotNone(sampled_data)
        self.assertEqual(sampled_data.shape[0], paa_sampler.n_segments)

    def testPAASamplerInverseTransform(self):
        """Test inverse_transform method"""
        class_obj = self.__class__
        paa_sampler = class_obj.paa_sampler
        inverse_transformed_data = paa_sampler.inverse_transform(
            paa_sampler.fit_transform(ts_2dim)
        )
        self.assertIsNotNone(inverse_transformed_data)
        self.assertEqual(inverse_transformed_data.shape, ts_2dim.shape)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
