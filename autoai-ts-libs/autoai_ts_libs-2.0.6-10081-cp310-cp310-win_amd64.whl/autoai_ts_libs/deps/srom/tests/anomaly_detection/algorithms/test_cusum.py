# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing CUSUM class"""
import unittest
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.cusum import CUSUM

class TestCUSUM(unittest.TestCase):
    """Test methods in CUSUM class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        x_array = np.zeros(100)  # Numpy array containins 100 0's
        y_array = np.ones(100)    # Numpy array containins 100 1's
        z_array = np.ones(100)
        # Add random outliers to below index's
        index = [35, 45, 55, 75, 95]
        values = [25, 17, 23, 2.5, 20]
        for i, value in enumerate(index):
            y_array[value] = values[i]
        # Add single outlier in z
        z_array[50] = 10
        z_array[80] = 39
        cls.dataframe = pd.DataFrame({'x': x_array, 'y': y_array, 'z': z_array})
        cls.numpy_array = cls.dataframe.values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """Test fit method"""
        cusum = CUSUM()
        fitted_cusum = cusum.fit(None)
        self.assertEqual(id(fitted_cusum), id(cusum))

    def test_predict(self):
        """Test predict method"""
        test_class = self.__class__
        cusum = CUSUM()
        cusum.fit(None)
        prediction = cusum.predict(test_class.dataframe.y)
        outlier = np.where(prediction > 0.0)[0].tolist()
        # Predict is also providing unexpected outlier, need to confirm if this is expected
        self.assertEqual([35, 36, 45, 46, 55, 56, 75, 76, 95, 96], outlier)

        # Check with negative drift
        cusum = CUSUM(drift=-1, threshold=0)
        cusum.fit(None)
        prediction = cusum.predict(test_class.dataframe.y)
        outlier = np.where(prediction > 0.0)[0].tolist()
        # Need to confirm below
        self.assertEqual([1, 36, 46, 56, 76, 96], outlier)

        # Check with numpy array
        cusum = CUSUM()
        cusum.fit(None)
        prediction = cusum.predict(test_class.numpy_array[:, 1])
        outlier = np.where(prediction > 0.0)[0].tolist()
        self.assertEqual([35, 36, 45, 46, 55, 56, 75, 76, 95, 96], outlier)
        prediction = cusum.predict(test_class.numpy_array[:, 0])
        outlier = np.where(prediction > 0.0)[0].tolist()
        self.assertEqual([], outlier)
        prediction = cusum.predict(test_class.numpy_array[:, 2])
        outlier = np.where(prediction > 0.0)[0].tolist()
        self.assertEqual([50, 51, 80, 81], outlier)

    def test_get_information(self):
        """Test get_information method"""
        test_class = self.__class__
        cusum = CUSUM()
        alarm_index, change_start, change_end, change_magnitude = cusum.get_information()
        self.assertIsNone(alarm_index)
        self.assertIsNone(change_start)
        self.assertIsNone(change_end)
        self.assertIsNone(change_magnitude)
        cusum.fit(None)
        cusum.predict(test_class.dataframe.y)
        alarm_index, change_start, change_end, change_magnitude = cusum.get_information()
        self.assertEqual(alarm_index.tolist(), [35, 36, 45, 46, 55, 56, 75, 76, 95, 96])
        self.assertEqual(change_start.tolist(), [0, 35, 36, 45, 46, 55, 56, 75, 76, 95])
        self.assertEqual(change_end.tolist(), [35, 44, 45, 54, 55, 74, 75, 94, 95, 99])
        self.assertEqual(change_magnitude.tolist(),
                         [24.0, -24.0, 16.0, -16.0, 22., -22., 1.5, -1.5, 19.0, -19.0])
        cusum.fit(None)
        alarm_index, change_start, change_end, change_magnitude = cusum.get_information()
        self.assertIsNone(alarm_index)
        self.assertIsNone(change_start)
        self.assertIsNone(change_end)
        self.assertIsNone(change_magnitude)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
