# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Unit test cases for testing sliding window anomaly model
"""
import unittest
import copy
import numpy as np
import pandas as pd

from sklearn.exceptions import NotFittedError
from autoai_ts_libs.deps.srom.anomaly_detection.sliding_window_anomaly_model import (
    SlidingWindowAnomalyModel
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.window_statistics.cost_discrepancy_checker import (
    CostDiscrepancyChecker
)
from sklearn.base import TransformerMixin


class TestSlidingWindowAnomalyModel(unittest.TestCase):
    """Test class for TestSlidingWindowAnomalyModel"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.base_learner = CostDiscrepancyChecker(order=2, threshold=0.5)
        cls.train_window_size = 10
        cls.buffer_window_size = 0
        cls.test_window_size = 10
        cls.jump = 5
        cls.min_size = 5
        cls.n_jobs = -1
        cls.prediction_score = True

        x_array = np.zeros(100)  # Numpy array containins 100 0's
        y_array = np.ones(100)  # Numpy array containins 100 1's
        z_array = np.ones(100)
        # Add random outliers to below index's
        index = [5, 25, 55, 75, 95]
        values = [25, 17, 23, 2.5, 20]
        for i, value in enumerate(index):
            y_array[value] = values[i]
        # Add single outlier in z
        z_array[50] = 10
        z_array[80] = 39
        cls.dataframe = pd.DataFrame({"x": x_array, "y": y_array, "z": z_array})
        numpy_array = cls.dataframe.values

        # Multi-dimensional
        cls.train_data = pd.DataFrame(numpy_array[0:70, :]).values
        cls.test_data = pd.DataFrame(numpy_array[70:, :]).values
        # 1-D
        cls.train_data_1d = pd.DataFrame(y_array[0:70]).values
        cls.test_data_1d = pd.DataFrame(y_array[70:]).values

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_fit(self):
        """ Test fit """
        test_class = self.__class__
        swm = SlidingWindowAnomalyModel(
            base_learner=test_class.base_learner,
            train_window_size=test_class.train_window_size,
            buffer_window_size=test_class.buffer_window_size,
            test_window_size=test_class.test_window_size,
            jump=test_class.jump,
            min_size=test_class.min_size,
        )
        swm_model = swm.fit(test_class.train_data)
        self.assertEqual(id(swm_model), id(swm))

    def test_fit_exceptions(self):
        """ Test fit for exceptions"""
        test_class = self.__class__
        # no base learner
        swm = SlidingWindowAnomalyModel()
        swm.base_learner = None
        self.assertRaises(RuntimeError, swm.fit, test_class.train_data)

    def test_predict_exceptions(self):
        """ Test predict for exceptions"""
        test_class = self.__class__
        swm = SlidingWindowAnomalyModel()
        # no base learner
        swm.base_learner = None
        self.assertRaises(RuntimeError, swm.predict, test_class.train_data)

    def test_predict_with_prediction_score(self):
        """ Test predict with no prediction score"""
        test_class = self.__class__
        swm = SlidingWindowAnomalyModel(
            base_learner=test_class.base_learner,
            train_window_size=test_class.train_window_size,
            buffer_window_size=test_class.buffer_window_size,
            test_window_size=test_class.test_window_size,
            jump=test_class.jump,
            min_size=test_class.min_size,
            prediction_score=True,
        )
        predicted_data = swm.predict(test_class.train_data)
        self.assertEqual(
            predicted_data,
            [
                np.nan,
                np.nan,
                np.nan,
                np.nan,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0,
                1.0,
                1.0,
                1.0,
            ],
        )

        swm.prediction_score = False
        predicted_data = swm.predict(test_class.train_data)
        average_anomaly_score = np.nanmean(predicted_data)
        self.assertGreaterEqual(average_anomaly_score, 5.64)
        predicted_data = swm.predict([1, 1, 1, 1, 6, 10, 20, 1, 1])
        self.assertEqual(predicted_data, [np.nan, np.nan, np.nan, np.nan])

    def test_predict_with_prediction_score_and_1d_data(self):
        """ Test predict with no prediction score and 1 dimentional data"""
        test_class = self.__class__
        swm = SlidingWindowAnomalyModel(
            base_learner=test_class.base_learner,
            train_window_size=test_class.train_window_size,
            buffer_window_size=test_class.buffer_window_size,
            test_window_size=test_class.test_window_size,
            jump=test_class.jump,
            min_size=test_class.min_size,
            prediction_score=True,
        )
        predicted_data = swm.predict(test_class.train_data_1d)
        self.assertEqual(
            predicted_data,
            [
                np.nan,
                np.nan,
                np.nan,
                np.nan,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0,
                0.0,
                1.0,
                1.0,
            ],
        )
        swm.prediction_score = False
        predicted_data = swm.predict(test_class.train_data_1d)
        average_anomaly_score = np.nanmean(predicted_data)
        self.assertGreaterEqual(average_anomaly_score, 15.71)

    def test_predict_with_with_min_size_greater_than_samples(self):
        """ Test predict with min_size greater than samples"""
        test_class = self.__class__
        swm = SlidingWindowAnomalyModel(
            base_learner=test_class.base_learner,
            train_window_size=test_class.train_window_size,
            buffer_window_size=test_class.buffer_window_size,
            test_window_size=test_class.test_window_size,
            jump=test_class.jump,
            min_size=30,
            prediction_score=True,
        )
        predicted_data = swm.predict(test_class.train_data_1d)
        self.assertEqual(
            predicted_data,
            [
                np.nan,
                np.nan,
                np.nan,
                np.nan,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
        )

    def test_set_params(self):
        """ Test set params """
        test_class = self.__class__
        swm = SlidingWindowAnomalyModel(
            base_learner=test_class.base_learner,
            train_window_size=test_class.train_window_size,
            buffer_window_size=test_class.buffer_window_size,
            test_window_size=test_class.test_window_size,
            jump=test_class.jump,
            min_size=test_class.min_size,
            prediction_score=True,
        )
        # empty set_params
        swm.set_params()
        predicted_data = swm.predict(test_class.train_data)
        self.assertEqual(
            predicted_data,
            [
                np.nan,
                np.nan,
                np.nan,
                np.nan,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0,
                1.0,
                1.0,
                1.0,
            ],
        )

        # set_params with threshold
        swm.set_params(base_learner__threshold=5)
        predicted_data = swm.predict(test_class.train_data)
        self.assertEqual(
            predicted_data,
            [
                np.nan,
                np.nan,
                np.nan,
                np.nan,
                1.0,
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
                0.0,
            ],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
