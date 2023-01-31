import unittest
from autoai_ts_libs.deps.srom.preprocessing.timeseries.sampler import Sampler
from autoai_ts_libs.deps.srom.tests.datasets.sample_data import ts_2dim

class TestSampler(unittest.TestCase):
    """Test class for Sampler"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.sampler = Sampler()

    def testSamplerSetup(self):
        """Test init method"""
        class_obj = self.__class__
        sampler = class_obj.sampler
        self.assertIsNotNone(sampler)

    def testSamplerFitTransform(self):
        """Test fit_transform method"""
        class_obj = self.__class__
        sampler = class_obj.sampler
        sampled_data = sampler.fit_transform(ts_2dim)
        self.assertIsNotNone(sampled_data)

    def testSamplerInverseTransform(self):
        """Test inverse_transform method"""
        class_obj = self.__class__
        sampler = class_obj.sampler
        inverse_transformed_data = sampler.inverse_transform(
            sampler.fit_transform(ts_2dim)
        )
        self.assertIsNotNone(inverse_transformed_data)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
