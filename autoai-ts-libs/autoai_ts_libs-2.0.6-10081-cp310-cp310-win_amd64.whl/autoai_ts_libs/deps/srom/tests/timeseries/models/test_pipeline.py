""" Test Forecaster """
import unittest
import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.time_series.pipeline import Forecaster
from autoai_ts_libs.deps.srom.preprocessing.transformer import Log
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from autoai_ts_libs.deps.srom.time_series.utils.scorer import make_ts_scorer
from sklearn.pipeline import FeatureUnion
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import NormalizedFlatten


class TestForecaster(unittest.TestCase):
    """class for testing Forecaster"""

    @classmethod
    def setUp(cls):
        x = np.arange(30)
        y = np.arange(300, 330)
        X = np.array([x, y])
        X = np.transpose(X)
        cls.target_columns = [0, 1]
        cls.X = X
        log = Log()
        lr = LinearRegression()
#         lr.set_params(**{
#     'copy_X': False,
#     'fit_intercept': False,
#     'n_jobs': -1,
#     'normalize': True,
#     'positive': True
# })
     
        featun = FeatureUnion([("log", log)])
        cls.steps = [
            ("featun", featun), ("flatten", NormalizedFlatten()), ("lr", lr)]
        cls.feature_columns = [0, 1]
        cls.target_columns = [0, 1]
        cls.lookback_win = 5
        cls.store_lookback_history=True
        cls.pred_win = 5

    def test_fit(self):
        """method for testing the fit method of Forecaster"""
        test_class = self.__class__
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        self.assertEqual(fitted_model, model)

    def test_fit_with_false_store_lookback_history(self):
        """method for testing the fit method of Forecaster"""
        test_class = self.__class__
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=False,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        self.assertEqual(fitted_model, model)

    def test_predict_forecast(self):
        """method for testing the predict method of Forecaster"""
        test_class = self.__class__
        # Test Multivariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is forecast
        prediction_type="forecast"
        pred_x = fitted_model.predict(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertEqual((5, 2), pred_x.shape)
        # Test Univariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=[0],
            target_columns=[0],
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is forecast
        prediction_type="forecast"
        pred_x = fitted_model.predict(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertEqual((5, 1), pred_x.shape)

    def test_predict_forecast_with_none_x(self):
        """method for testing the predict method of Forecaster"""
        test_class = self.__class__
        # Test Multivariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(test_class.X)
        #predection type is forecast
        prediction_type="forecast"
        add_look_x=fitted_model._add_lookback_history_to_X(None)
        pred_x = fitted_model.predict(add_look_x,prediction_type=prediction_type)
        self.assertEqual((5, 2), pred_x.shape)
        # Test Univariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=[0],
            target_columns=[0],
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(test_class.X)
        #predection type is forecast
        prediction_type="forecast"
        add_look_x=fitted_model._add_lookback_history_to_X(None)
        pred_x = fitted_model.predict(add_look_x,prediction_type=prediction_type)
        self.assertEqual((5, 1), pred_x.shape)

    # def test_predcit_forecast_with_none_x(self):
    #     test_class = self.__class__
    #     # Test Multivariate
    #     model = Forecaster(
    #         steps=test_class.steps,
    #         feature_columns=test_class.feature_columns,
    #         target_columns=test_class.target_columns,
    #         lookback_win=test_class.lookback_win,
    #         pred_win=test_class.pred_win,
    #         store_lookback_history=True,
    #     )
    #     #checked_x=model._check_X(test_class.X)
    #     #prepared_xt=model._get_fit_X_y(checked_x)
    #     fitted_model = model.fit(test_class.X)
    #     #predection type is forecast
    #     prediction_type="forecast"
    #     pred_x = fitted_model.predict(None,prediction_type=prediction_type)
    #     self.assertEqual((5, 2), pred_x.shape)
    #     # Test Univariate
    #     model = Forecaster(
    #         steps=test_class.steps,
    #         feature_columns=[0],
    #         target_columns=[0],
    #         lookback_win=0,
    #         pred_win=test_class.pred_win,
    #         store_lookback_history=True,
    #     )
    #     #checked_x=model._check_X(test_class.X)
    #     #prepared_xt=model._get_fit_X_y(checked_x)
    #     fitted_model = model.fit(test_class.X)
    #     #predection type is forecast
    #     prediction_type="forecast"
    #     pred_x = fitted_model.predict(None,prediction_type=prediction_type)
    #     self.assertEqual((5, 1), pred_x.shape)

    def test_predict_rolling(self):
        """method for testing the predict method of Forecaster"""
        test_class = self.__class__
        # Test Multivariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is rolling
        prediction_type="rolling"
        pred_x = fitted_model.predict(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        # Test Univariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=[0],
            target_columns=[0],
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is rolling
        prediction_type="rolling"
        pred_x = fitted_model.predict(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)

    def test_get_predict_x_rolling(self):
        """method for testing the predict method of Forecaster"""
        test_class = self.__class__
        # Test Multivariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is rolling
        prediction_type="rolling"
        pred_x = fitted_model._get_predict_X(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        # Test Univariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=[0],
            target_columns=[0],
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is rolling
        prediction_type="rolling"
        pred_x = fitted_model._get_predict_X(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)

    def test_get_predict_x_forecast(self):
        """method for testing the predict method of Forecaster"""
        test_class = self.__class__
        # Test Multivariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is forecast
        prediction_type="forecast"
        pred_x = fitted_model._get_predict_X(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        # Test Univariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=[0],
            target_columns=[0],
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is forecast
        prediction_type="forecast"
        pred_x = fitted_model._get_predict_X(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)

    def test_get_predict_x_forecast_pred_win(self):
        """method for testing the predict method of Forecaster"""
        test_class = self.__class__
        # Test Multivariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=1,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is forecast
        prediction_type="forecast"
        pred_x = fitted_model._get_predict_X(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)
        # Test Univariate
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=[0],
            target_columns=[0],
            lookback_win=test_class.lookback_win,
            pred_win=1,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        #predection type is forecast
        prediction_type="forecast"
        pred_x = fitted_model._get_predict_X(prepared_xt[0][-test_class.lookback_win :],prediction_type=prediction_type)
        self.assertIsNotNone(pred_x)

    def test_score(self):
        """method for testing the score method of Forecaster"""
        test_class = self.__class__
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        score = fitted_model.score(prepared_xt[0])
        self.assertIsNotNone(score)

    def test_score_with_false_store_lookback_history(self):
        """method for testing the score method of Forecaster with false store loockback history"""
        test_class = self.__class__
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=False,
        )
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        score = fitted_model.score(prepared_xt[0])
        self.assertIsNotNone(score)

    def test_custom_scorer(self):
        """method for testing custom scorer of Forecaster"""
        test_class = self.__class__
        model = Forecaster(
            steps=test_class.steps,
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
            store_lookback_history=test_class.store_lookback_history,
        )
        scorer = make_ts_scorer(mean_squared_error)
        model.set_scoring(scorer)
        checked_x=model._check_X(test_class.X)
        prepared_xt=model._get_fit_X_y(checked_x)
        fitted_model = model.fit(prepared_xt[0])
        score = fitted_model.score(prepared_xt[0])
        self.assertIsNotNone(score)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
