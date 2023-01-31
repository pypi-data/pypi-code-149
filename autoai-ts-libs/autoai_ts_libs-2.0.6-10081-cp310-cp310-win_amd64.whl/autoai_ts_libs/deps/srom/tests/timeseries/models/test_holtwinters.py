"""
Unit test cases for holtwinters.
"""
from datetime import time
import unittest
import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.time_series.models.holtwinters import HoltWinters


class TestHoltWinters(unittest.TestCase):
    """Test class for HoltWinters"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        import os

        day = 24 * 60 * 60
        year = 365.2425 * day

        def load_dataframe() -> pd.DataFrame:
            """ Create a time series x sin wave dataframe. """
            df = pd.DataFrame(columns=["date", "sin"])
            df.date = pd.date_range(start="2018-01-01", end="2021-03-01", freq="D")
            df.sin = 1 + np.sin(df.date.astype("int64") // 1e9 * (2 * np.pi / year))
            df.sin = (df.sin * 100).round(2)
            df.date = df.date.apply(lambda d: d.strftime("%Y-%m-%d"))
            return df

        cls.X = load_dataframe()
        cls.X = cls.X[["sin"]]

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        estm = HoltWinters(time_column=[0], feature_columns=[0], target_columns=[0])
        fitted_estm = estm.fit(self.X["sin"])
        self.assertEqual(id(fitted_estm), id(estm))

    def test_predict(self):
        estm = HoltWinters(time_column=[0], feature_columns=[0], target_columns=[0])
        estm.fit(self.X["sin"])
        self.assertIsNotNone(estm.predict())


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)

