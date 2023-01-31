import unittest
from autoai_ts_libs.deps.srom.preprocessing.timeseries.sax_sampler import SymbolicAggregateApproximation
from autoai_ts_libs.deps.srom.tests.datasets.sample_data import ts_2dim

class TestSAXSampler(unittest.TestCase):
    """Test class for SAX Sampler"""

    @classmethod
    def setUpClass(cls):
        """Setup class"""
        cls.sax_sampler = SymbolicAggregateApproximation(n_bins=5, encode="ordinal")

    def testSAXSamplerSetup(self):
        """Test init method"""
        class_obj = self.__class__
        sax_sampler = class_obj.sax_sampler
        self.assertIsNotNone(sax_sampler)

    def testSAXSamplerFitTransform(self):
        """Test fit_transform method"""
        class_obj = self.__class__
        sax_sampler = class_obj.sax_sampler
        sampled_data = sax_sampler.fit_transform(ts_2dim)
        self.assertIsNotNone(sampled_data)
        self.assertEqual(sampled_data.shape, ts_2dim.shape)

    def testSAXSamplerInverseTransform(self):
        """Test inverse_transform method"""
        class_obj = self.__class__
        sax_sampler = class_obj.sax_sampler
        inverse_transformed_data = sax_sampler.inverse_transform(
            sax_sampler.fit_transform(ts_2dim)
        )
        self.assertIsNotNone(inverse_transformed_data)
        self.assertEqual(inverse_transformed_data.shape, ts_2dim.shape)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
