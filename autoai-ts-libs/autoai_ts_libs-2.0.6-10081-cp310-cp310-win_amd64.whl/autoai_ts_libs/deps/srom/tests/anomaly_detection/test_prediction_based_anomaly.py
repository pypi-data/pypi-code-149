# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Unit test cases for testing gaussian graphical model
"""
import unittest
import copy
import numpy as np
import pandas as pd
from time import time

from autoai_ts_libs.deps.srom.anomaly_detection.prediction_based_anomaly import (
    PredictionAnomaly,
    models_for_predad,
)
from autoai_ts_libs.deps.srom.time_series.pipeline import Forecaster
from sklearn.linear_model import LinearRegression
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import TimeTensorTransformer


class TestPredictionBasedAnomaly(unittest.TestCase):
    """Test class for Prediction based anomaly detection"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""

        X = np.arange(196)
        XwoNan = X.copy()
        cls.XwoNan = XwoNan.reshape(-1, 1)
        X = np.append(X, [np.nan, 1000, 2000, 10000])
        cls.X = X.reshape(-1, 1)
        cls.sample_model = (
            Forecaster(
                feature_columns=[0],
                lookback_win=20,
                pred_win=1,
                steps=[("TimeTensorTransformer", TimeTensorTransformer())],
                store_lookback_history=True,
                target_columns=[0],
            ),
        )

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_models_for_predad(self):
        """method to test models for predad method."""
        test_class = self.__class__
        models = models_for_predad(
            test_class.X, [0], [0], lookback_win=20, total_execution_time=2, mode="auto"
        )
        self.assertIsNotNone(models)
        models2 = models_for_predad(
            test_class.X,
            [0],
            [0],
            lookback_win=20,
            total_execution_time=2,
            mode="default",
        )
        self.assertIsNotNone(models2)

    def test_set_models(self):
        test_class = self.__class__
        model = PredictionAnomaly([0], [1])
        model.set_models(test_class.sample_model)
        model.set_models([LinearRegression()])
        self.assertIsNotNone(model)

    def test_mask_unmask(self):
        test_class = self.__class__
        model = PredictionAnomaly([0], [1])
        self.assertIsNotNone(model.mask_missing_values(test_class.X))
        self.assertIsNotNone(model.unmask_missing_values(test_class.X))

    def test_getXY_data(self):
        test_class = self.__class__
        model = PredictionAnomaly([0], [1])
        self.assertIsNotNone(model.get_Xy_Data(test_class.X))

    def test_fit(self):
        """test the fit method."""
        test_class = self.__class__
        model = PredictionAnomaly([0], [1])
        model.set_models(test_class.sample_model)
        fitted_model = model.fit(test_class.X)
        self.assertEqual(id(model), id(fitted_model))

    def test_predict(self):
        test_class = self.__class__
        model = PredictionAnomaly([0], [1])
        model.set_models(test_class.sample_model)
        fitted_model = model.fit(test_class.XwoNan)
        predicted_X = fitted_model.predict(test_class.XwoNan)
        self.assertIsNotNone(predicted_X)

    def test_predict_proba(self):
        test_class = self.__class__
        model = PredictionAnomaly([0], [1], anomaly_threshold_method="chiscore")
        model.set_models(test_class.sample_model)
        fitted_model = model.fit(test_class.XwoNan)
        predicted_X = fitted_model.predict_proba(test_class.XwoNan)
        self.assertIsNotNone(predicted_X)
        model = PredictionAnomaly([0], [1], anomaly_threshold_method="qscore")
        model.set_models(test_class.sample_model)
        fitted_model = model.fit(test_class.XwoNan)
        predicted_X = fitted_model.predict_proba(test_class.XwoNan)
        self.assertIsNotNone(predicted_X)

    def test_get_model_prediction(self):
        test_class = self.__class__
        model = PredictionAnomaly([0], [1], anomaly_threshold_method="chiscore")
        model.set_models(test_class.sample_model)
        fitted_model = model.fit(test_class.XwoNan)
        model_prediction = fitted_model.get_model_prediction(test_class.X)
        self.assertIsNotNone(model_prediction)

    def test_get_prediction_score(self):
        test_class = self.__class__
        model = PredictionAnomaly([0], [1], anomaly_threshold_method="chiscore")
        model.set_models(test_class.sample_model)
        fitted_model = model.fit(test_class.XwoNan)
        self.assertIsNotNone(fitted_model.get_model_prediction(test_class.XwoNan))


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
