""" Test T2RForecaster """
import unittest
import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.time_series.models.T2RForecaster import T2RForecaster,FourierTermEstimator


class TestT2RForecaster(unittest.TestCase):
    """ class for testing T2RForecaster """

    @classmethod
    def setUp(cls):
        X = np.arange(30)
        X = X.reshape(-1, 1)
        cls.X = X
        cls.lookback_win = "auto"

    def test_fit(self):
        """ method for testing the fit method of T2RForecaster"""
        test_class = self.__class__
        model = T2RForecaster(lookback_win=test_class.lookback_win)
        fitted_model = model.fit(test_class.X)
        self.assertEqual(fitted_model, model)
        model = T2RForecaster(lookback_win=test_class.lookback_win,trend="Mean")
        fitted_model = model.fit(test_class.X)
        self.assertEqual(fitted_model, model)
        model = T2RForecaster(lookback_win=test_class.lookback_win,trend="Poly")
        fitted_model = model.fit(test_class.X)
        self.assertEqual(fitted_model, model)
        model=T2RForecaster(lookback_win=test_class.lookback_win,residual="Difference")
        fitted_model=model.fit(test_class.X)
        self.assertEqual(fitted_model, model)
        model=T2RForecaster(lookback_win=test_class.lookback_win,residual="GeneralizedMean")
        fitted_model=model.fit(test_class.X)
        self.assertEqual(fitted_model, model)

    def test_predict_with_none(self):
        """ Tests the predict method of T2RForecaster"""
        test_class = self.__class__
        model = T2RForecaster(lookback_win=test_class.lookback_win,)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(pred_win=1)
        self.assertEqual(len(ypred), 1)
        model = T2RForecaster(lookback_win=test_class.lookback_win,)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)
        model = T2RForecaster(lookback_win=test_class.lookback_win,trend="Mean")
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)
        model = T2RForecaster(lookback_win=test_class.lookback_win,trend="Poly")
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)
        model=T2RForecaster(lookback_win=test_class.lookback_win,residual="Difference")
        fitted_model=model.fit(test_class.X)
        ypred=fitted_model.predict()
        self.assertEqual(len(ypred),12)
        model=T2RForecaster(lookback_win=test_class.lookback_win,residual="GeneralizedMean")
        fitted_model=model.fit(test_class.X)
        ypred=fitted_model.predict()
        self.assertEqual(len(ypred),12)

    def test_predict_with_data(self):
        test_class = self.__class__
        model = T2RForecaster(lookback_win=test_class.lookback_win,)
        #prepare_x=T2RForecaster._prepare_predict_X(test_class.X)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(pred_win=1)
        self.assertEqual(len(ypred), 1)
        model = T2RForecaster(lookback_win=test_class.lookback_win,)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(test_class.X)
        self.assertEqual(len(ypred), 12)
        model = T2RForecaster(lookback_win=test_class.lookback_win,trend="Mean")
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(test_class.X)
        self.assertEqual(len(ypred), 12)
        model = T2RForecaster(lookback_win=test_class.lookback_win,trend="Poly")
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(test_class.X)
        self.assertEqual(len(ypred), 12)
        model=T2RForecaster(lookback_win=test_class.lookback_win,residual="Difference")
        fitted_model=model.fit(test_class.X)
        ypred=fitted_model.predict(test_class.X)
        self.assertEqual(len(ypred),12)
        model=T2RForecaster(lookback_win=test_class.lookback_win,residual="GeneralizedMean")
        fitted_model=model.fit(test_class.X)
        ypred=fitted_model.predict(test_class.X)
        self.assertEqual(len(ypred),12)

    def test_predict_with_none_pred_win(self):
        test_class = self.__class__
        model = T2RForecaster(lookback_win=test_class.lookback_win)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(test_class.X,pred_win=None,prediction_type="sliding")
        self.assertEqual(len(ypred), 19)

    def test_predict_sliding_window(self):
        """ The tests the sliding window method of T2RForecaster"""
        test_class = self.__class__
        model = T2RForecaster(lookback_win=test_class.lookback_win,)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_sliding_window(
            test_class.X[test_class.X.shape[0] - 5 :]
        )
        self.assertEqual(len(ypred), 5)

    def test_predict_multi_step_sliding_window(self):
        """ The tests predict_multi_step_sliding_window method of T2RForecaster"""
        test_class = self.__class__
        model = T2RForecaster(lookback_win=test_class.lookback_win,)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_multi_step_sliding_window(
            test_class.X[test_class.X.shape[0] - 5 :], 3
        )
        self.assertEqual(len(ypred), 3)

    def test_predict_interval(self):
        test_class = self.__class__
        model = T2RForecaster(lookback_win=test_class.lookback_win,)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_interval(test_class.X)
        self.assertEqual(len(ypred), 12)
    
    def test_predict_interval_with_none_x(self):
        test_class = self.__class__
        model = T2RForecaster(lookback_win=test_class.lookback_win,)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_interval()
        self.assertEqual(len(ypred), 12)



if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
