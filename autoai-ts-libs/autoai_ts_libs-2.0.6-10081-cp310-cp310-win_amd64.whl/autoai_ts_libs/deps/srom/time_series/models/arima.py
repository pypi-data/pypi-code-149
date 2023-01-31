import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator
from statsmodels.tsa.arima.model import ARIMA
from sklearn.utils.validation import check_array, check_is_fitted, column_or_1d as c1d
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator
import copy


class ARIMAModel(StateSpaceEstimator, BaseEstimator):
    """
    A base line prediction model : predict training using ARIMA
    See description
    https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_model.ARIMA.fit.html

    Parameters:
        target_columns (numpy array): Target indices.
        p (int, optional):  The order (number of time lags) of the autoregressive model. Default is 2.
        d (int, optional): The degree of differencing (the number of times the data have had past values subtracted). model. Default is 0.
        q (int, optional): The order of the moving-average model. model. Default is 1.
        trend (string, optional): Whether to include a constant or not. 'c' includes constant, 'nc' no constant.
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
        trend="c",
    ):
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.pred_win = pred_win
        self.p = p
        self.d = d
        self.q = q
        self.trend = trend

    def fit(self, X, y=None):
        """
        full fledge training with proper estimation of the parameters
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        if len(self.target_columns) > 1:
            raise Exception("Only supported univariate prediction")

        X = X[:, self.target_columns].astype(float)

        self.model_ = ARIMA(X, order=(self.p, self.d, self.q), trend=self.trend)
        self.fitted_model_ = self.model_.fit()
        return self

    def predict(self, X=None, prediction_type="forecast"):
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
