import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.utils.validation import check_array, check_is_fitted, column_or_1d as c1d
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator
import copy


class SARIMAModel(StateSpaceEstimator, BaseEstimator):
    """
    A base line prediction model : predict training using ARIMA
    See description
    https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_model.ARIMA.fit.html

    Parameters:
        target_columns (numpy array): Target indices.
        p (int, optional):  The order (number of time lags) of the autoregressive model. Default is 2.
        d (int, optional): The degree of differencing (the number of times the data have had past values subtracted). model. Default is 0.
        q (int, optional): The order of the moving-average model. model. Default is 1.
        P (int, optional):  The order (number of time lags) of the autoregressive model. Default is 2.
        D (int, optional): The degree of differencing (the number of times the data have had past values subtracted). model. Default is 0.
        Q (int, optional): The order of the moving-average model. model. Default is 1.
        s (int, optional): The seasonal frequency
        trend (string, optional): Whether to include a constant or not. 'c' includes constant, 'nc' no constant.
        method (string, optional): This is the loglikelihood to maximize. Default is 'css-mle'.
        transparams (boolean, optional): Whether or not to transform the parameters to ensure stationarity. Default is True.
        maxiter (int, optional): The maximum number of function evaluations. Default is 35.
        start_params(array, optional): Starting parameters for ARMA(p,q). If None, the default is given by ARMA._fit_start_params.
        auto_search(bool, optional): Automated discovery of parameters.
    """

    def __init__(
        self,
        time_column=[0],
        feature_columns=[0],
        target_columns=[0],
        pred_win=1,
        p=2,
        d=0,
        q=1,
        P=0,
        D=0,
        Q=0,
        s=0,
        trend="c",
        method="lbfgs",
        transparams=True,
        maxiter=35,
    ):
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.pred_win = pred_win
        self.p = p
        self.d = d
        self.q = q
        self.P = P
        self.D = D
        self.Q = Q
        self.s = s
        self.trend = trend
        self.method = method
        self.transparams = transparams
        self.maxiter = maxiter

    def fit(self, X, y=None):
        """
        No learning, return the object as it is.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        if len(self.target_columns) > 1:
            raise Exception("Only supported univariate prediction")

        X = X[:, self.target_columns].astype(float)

        self.model_ = SARIMAX(
            X,
            order=(self.p, self.d, self.q),
            seasonal_order=(self.P, self.D, self.Q, self.s),
        )
        self.fitted_model_ = self.model_.fit(
            method=self.method,
            trend=self.trend,
            transparams=self.transparams,
            maxiter=self.maxiter,
            full_output=0,
            disp=0,
        )
        return self

    def predict(self, X, prediction_type="forecast"):
        """
        Predict the output using fitted model and input array.
        Args:
            X (numpy array or time tensor) - input array.
        """
        if self.fitted_model_ is None:
            raise Exception("model is not fitted")

        if isinstance(X, pd.DataFrame):
            X = X.values

        if X is not None:
            X = X[:, self.target_columns].astype(float)

        if prediction_type == "training":
            return self.fitted_model_.predict(dynamic=False)

        if prediction_type == "sliding":
            mdl_fitted_ = copy.deepcopy(self.fitted_model_)
            pred_ans = []
            for item_index in range(len(X) - self.pred_win + 1):
                yhat = mdl_fitted_.forecast(self.pred_win)
                pred_ans.append(yhat)
                mdl_fitted_ = mdl_fitted_.extend(
                    X[item_index, :].reshape(-1, len(self.target_columns))
                )
            return np.array(pred_ans)

        if X is None or X.shape[0] == 0:
            yhat = self.fitted_model_.forecast(self.pred_win)
            return np.array(yhat)

        mdl_fitted_ = copy.deepcopy(self.fitted_model_)
        mdl_fitted_ = mdl_fitted_.extend(X)
        yhat = mdl_fitted_.forecast(self.pred_win)
        return np.array(yhat)
