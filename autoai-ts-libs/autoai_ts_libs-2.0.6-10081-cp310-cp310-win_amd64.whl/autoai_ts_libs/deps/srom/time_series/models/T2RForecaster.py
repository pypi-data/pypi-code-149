import pandas as pd
import numpy as np
import math
import scipy.stats as st
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from collections import namedtuple
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.base import BaseEstimator
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator


class MeanEstimator(BaseEstimator):
    """
    This class is to preserve the mean of signal.
    """

    def __init__(self, time_column=[0], feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            time_column (list, optional): [description]. Defaults to [0].
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, x, y=None):
        """
        This is to fit.
        """
        self.z = np.mean(x)
        return self

    def predict(self, x):
        """
        This is to predict.
        """
        return np.zeros(len(x)) + self.z


class PolyEstimator(BaseEstimator):
    """
    Poly line estimators.
    """

    def __init__(
        self, time_column=[0], feature_columns=[0], target_columns=[0], degree=2
    ):
        """[summary]

        Args:
            time_column (list, optional): [description]. Defaults to [0].
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
            degree (int, optional): [description]. Defaults to 2.
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.degree = degree

    def fit(self, x, y):
        """
        This is to fit.
        """
        self.base_model_ = np.poly1d(np.polyfit(x.flatten().tolist(), y, self.degree))
        return self

    def predict(self, x):
        """
        This is to predict.
        """
        return self.base_model_(x.flatten().tolist())


class TrendEstimator(BaseEstimator):
    """
    Trend line Estimator.
    """

    def __init__(
        self,
        time_column=[0],
        feature_columns=[0],
        target_columns=[0],
        base_model=LinearRegression(),
    ):
        """[summary]

        Args:
            time_column (list, optional): [description]. Defaults to [0].
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
            base_model ([type], optional): [description]. Defaults to LinearRegression().
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.base_model = base_model

    def fit(self, x, y):
        """
        This is to fit.
        """
        self.base_model.fit(x, y)
        return self

    def predict(self, x):
        """
        This is to predit.
        """
        return self.base_model.predict(x)


class FourierTermEstimator(BaseEstimator):
    """
    FourierTermEstimator Estimator.
    Parameters
    ----------
        base_model : (object, default = LinearRegression) Instance of base model to be used.
    """

    def __init__(
        self, period, time_column=[0], feature_columns=[0], target_columns=[0], terms=3
    ):
        """[summary]

        Args:
            period ([type]): [description]
            time_column (list, optional): [description]. Defaults to [0].
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
            terms (int, optional): [description]. Defaults to 3.
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.period = period
        self.terms = terms

    def _get_feature_names(self):
        return [
            "Four_%s%s-%s" % ("S" if i % 2 == 0 else "C", str(self.period), str(i // 2))
            for i in range(self.total_dims_)
        ]

    def fit(self, x=None, y=None):
        """
        This is to fit.
        """
        if self.terms > self.period:
            self.terms = self.period
        self.p_ = ((np.arange(self.terms) + 1) / self.period).astype(np.float64)
        self.total_dims_ = len(self.p_) * 2
        #print(self.total_dims_)
        self.feature_names_ = self._get_feature_names()
        return self

    def predict(self, x):
        """
        This is to predit.
        """
        _pred = []
        for e in self.p_:
            _pred.append(np.sin(np.pi * 2 * e * x))
            _pred.append(np.cos(np.pi * 2 * e * x))
        return np.asarray(_pred).T


class GeneralizedDifferenceRegressor(BaseEstimator):
    """
    GeneralizedDifferenceRegressor.
    Parameters
    ----------
        model : (object, default = LinearRegression) Instance of base model to be used.
    """

    def __init__(
        self,
        time_column=[0],
        feature_columns=[0],
        target_columns=[0],
        model=LinearRegression(),
    ):
        """[summary]

        Args:
            time_column (list, optional): [description]. Defaults to [0].
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
            model ([type], optional): [description]. Defaults to LinearRegression().
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.model = model

    def fit(self, x, y):
        """
        This is to fit.
        """
        y = y - x[:, 0]
        for item in range(1, x.shape[1]):
            x[:, item - 1] = x[:, item - 1] - x[:, item]
        self.model.fit(x[:, range(x.shape[1] - 1)], y)
        return self

    def predict(self, x):
        """
        This is to predict.
        """
        x1 = x.copy()
        for item in range(1, x1.shape[1]):
            x1[:, item - 1] = x1[:, item - 1] - x1[:, item]
        return self.model.predict(x1[:, range(x1.shape[1] - 1)]) + x[:, 0]


class GeneralizedMeanRegressor(BaseEstimator):
    """
    GeneralizedMeanRegressor.
    Parameters
    ----------
        model : (object, default = LinearRegression) Instance of base model to be used.
    """

    def __init__(
        self,
        time_column=[0],
        feature_columns=[0],
        target_columns=[0],
        model=LinearRegression(),
    ):
        """[summary]

        Args:
            time_column (list, optional): [description]. Defaults to [0].
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
            model ([type], optional): [description]. Defaults to LinearRegression().
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.model = model

    def fit(self, x, y):
        """
        This is to fit.
        """
        x = np.hstack((x, np.mean(x, axis=1).reshape(-1, 1)))
        self.model.fit(x, y)
        return self

    def predict(self, x):
        """
        This is to predict.
        """
        x = np.hstack((x, np.mean(x, axis=1).reshape(-1, 1)))
        return self.model.predict(x)


class T2RForecaster(BaseEstimator, StateSpaceEstimator):
    """
    Trend-to-Residual Multi-Step Singal Predictor.

    Parameters
    ----------
        trend : (string, default = Linear) It can be Linear, Mean, Poly.
        residual : (string, default = Linear) It can be Linear, Difference.
        lookback_win : (int or string, default = auto) Look-back window for the model.
        pred_win : (int, optional, default = 12) Look-ahead window for the model.
    """

    def __init__(
        self,
        time_column=[0],
        feature_columns=[0],
        target_columns=[0],
        trend="Linear",
        residual="Linear",
        lookback_win="auto",
        pred_win=12,
    ):
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.trend = trend
        self.residual = residual
        self.lookback_win = lookback_win
        self.pred_win = pred_win

    def _pre_fit_initialize(self):
        """
        """
        self.i_lookback_win_ = self.lookback_win

        # initialize the trend model
        if self.trend == "Linear":
            self.trend_model_ = TrendEstimator(base_model=LinearRegression())
        elif self.trend == "Poly":
            self.trend_model_ = PolyEstimator(degree=2)
        elif self.trend == "Mean":
            self.trend_model_ = MeanEstimator()
        else:
            raise Exception(
                "Unsupported trend model : only Linear, Poly and Mean supported."
            )

        # initialize the residual model
        if self.residual == "Linear":
            self.residual_model_ = LinearRegression()
        elif self.residual == "Difference":
            self.residual_model_ = GeneralizedDifferenceRegressor()
        elif self.residual == "GeneralizedMean":
            self.residual_model_ = GeneralizedMeanRegressor()
        else:
            raise Exception(
                "Unsupported residual model : only Linear, Difference and GeneralizedMean supported."
            )

    def _add_artifical_time_column(self):
        """
        This is utility function to store intermediate data.
        It add two new columns: row_number and artificial time
        also it store the min time, max time and deltaT.
        """
        self.X_["row_number"] = np.arange(0, self.X_.shape[0])
        self.X_["time"] = self.X_["row_number"]
        self.maxT_ = self.X_["time"].max()
        self.minT_ = self.X_["time"].min()
        self.deltaT_ = 1

    def fit(self, X, y=None):
        """
        Fit the model.
        Parameters
        ----------
            X : (numpy array) input data.
            y : None.
        Returns
        -------
            self : object
        """
        # automatically infer the lookback window for this model (only one time)
        self._pre_fit_initialize()
        if self.i_lookback_win_ == "auto":
            from autoai_ts_libs.deps.srom.time_series.utils.period_detection import guess_period

            self.i_lookback_win_ = guess_period(X.flatten())
            if self.i_lookback_win_ == 0:
                self.i_lookback_win_ = 5

        # this model store X for further processing
        # we use column signal
        self.X_ = pd.DataFrame(X[:, self.target_columns], columns=["Singal"])
        self.data_shape_ = self.X_.shape
        self._add_artifical_time_column()

        # add exogeneous
        self.eX_idx_ = list(set(self.feature_columns) - set(self.target_columns))
        self.eX_name_ = ["e_" + str(item) for item in self.eX_idx_]
        self.eX_ = pd.DataFrame(X[:, self.eX_idx_], columns=self.eX_name_)

        # fit a trend model that predict time --> singal value
        self.trend_model_.fit(self.X_["time"].values.reshape(-1, 1), self.X_["Singal"])

        # use trained model to fill Trend and Trend_Res
        self.X_["Trend"] = self.trend_model_.predict(
            self.X_["time"].values.reshape(-1, 1)
        )
        self.X_["Trend_Res"] = self.X_["Singal"] - self.X_["Trend"]

        # trend model residual stdev to be used in predict interval
        trend_res = self.X_["Trend_Res"].values
        sum_errs = np.sum((trend_res) ** 2)
        self.trend_res_stdev = np.sqrt(1 / (len(trend_res) - 2) * sum_errs)

        # prepare data to build second residual model using lookback window information
        self.X_col_ = ["Trend_Res"]
        for lag_i in range(1, self.i_lookback_win_):
            self.X_col_.append("Trend_Res_" + str(lag_i))
            self.X_["Trend_Res_" + str(lag_i)] = self.X_["Trend_Res"].shift(lag_i)
        # since this are recursive model, they take next
        self.X_["Trend_Res_y"] = self.X_["Trend_Res"].shift(-1)

        # scan back the series
        self.mdl_eX_name_ = []
        for ex_item in self.eX_name_:
            self.eX_[ex_item + "_xy"] = self.eX_[ex_item].shift(-1)
            self.mdl_eX_name_.append(ex_item + "_xy")
        self.jointX_eX = pd.concat([self.X_, self.eX_], axis=1)

        # training residual model
        # tmpData = self.X_[self.X_col_ + ["Trend_Res_y"]].dropna().copy()
        tmpData = (
            self.jointX_eX[self.X_col_ + self.mdl_eX_name_ + ["Trend_Res_y"]]
            .dropna()
            .copy()
        )
        close_to_zero = 0.0000000001
        if np.sum(tmpData.sum()) == 0.0:
            tmpData = tmpData.replace(0.0, close_to_zero)
        near_zero = np.sum(np.sum(np.abs(tmpData) < close_to_zero))
        if near_zero == tmpData.shape[0] * tmpData.shape[1]:
            tmpData[np.abs(tmpData) < close_to_zero] = close_to_zero
        self.residual_model_.fit(
            tmpData[self.X_col_ + self.mdl_eX_name_].values, tmpData["Trend_Res_y"]
        )
        #print(len(self.X_col_ + self.mdl_eX_name_))

        # residual model residual stdev to be used in predict interval
        ypred = self.residual_model_.predict(
            tmpData[self.X_col_ + self.mdl_eX_name_].values
        )
        ytrue = tmpData["Trend_Res_y"].values
        sum_errs = np.sum((ytrue - ypred) ** 2)

        self.res_res_stdev = np.sqrt(1 / (len(ytrue) - 2) * sum_errs)
        # trim the X, there are additional information that is not
        # used, so we trim it them
        # the following line failed so do not try
        self.predict_lookup = list(self.X_.loc[self.X_.index[-1], :][self.X_col_])
        self.X_ = self.X_[["Singal"]].copy()

        return self

    def update_multiple_observations(self, newX, pred_horizon=1):
        """
        This is a utility for speedup.
        It append multiple observations together and increase the speedup.
        """

        # temporary merge data of train and incoming
        _X = self.X_["Singal"]
        _X = pd.DataFrame(_X, columns=["Singal"])
        _nX = pd.DataFrame(newX[:, self.target_columns], columns=["Singal"])
        _X = _X.append(_nX)
        _X.reset_index(inplace=True, drop=True)

        # add row number and time column
        _X["row_number"] = np.arange(0, _X.shape[0])
        _X["time"] = _X["row_number"]

        # add trend and residual value
        _X["Trend"] = self.trend_model_.predict(_X["time"].values.reshape(-1, 1))
        _X["Trend_Res"] = _X["Singal"] - _X["Trend"]

        # prepare lookback window dataset
        for lag_i in range(1, self.i_lookback_win_):
            _X["Trend_Res_" + str(lag_i)] = _X["Trend_Res"].shift(lag_i)

        # now we merge _eX to
        _eX = self.eX_[self.eX_name_].copy()
        _neX = pd.DataFrame(newX[:, self.eX_idx_], columns=self.eX_name_)
        _eX = _eX.append(_neX)
        _eX.reset_index(inplace=True, drop=True)

        for ex_item in self.eX_name_:
            _eX[ex_item + "_xy"] = _eX[ex_item].shift(-1)

        jointX_eX = pd.concat([_X, _eX], axis=1)
        #print(jointX_eX.columns, self.X_col_, self.mdl_eX_name_)

        # now we start predicting the model
        tmpData = (
            jointX_eX[self.X_col_ + self.mdl_eX_name_ + ["Trend", "time"]]
            .dropna()
            .copy()
        )
        #print(tmpData)
        tmpData["pred_residual"] = self.residual_model_.predict(
            tmpData[self.X_col_ + self.mdl_eX_name_].values
        )
        # this is very imp as we predict for next step, so we gave the value
        tmpData["pred_residual_1"] = tmpData["pred_residual"].shift(1)
        tmpData["predicted_y"] = tmpData["pred_residual_1"] + tmpData["Trend"]
        tmpData["predicted_y_0"] = tmpData["predicted_y"]
        tmpData = tmpData.dropna()

        # if we wanted to do recursive multi-step using recursive meachnisum
        # note that we add additional prediction in same row
        impClm = ["predicted_y_0"]
        for i in range(1, pred_horizon):

            # our current prediction become signal
            tmpData["Singal"] = tmpData["predicted_y"]
            # we want to predict next time
            tmpData["time"] = tmpData["time"] + 1

            # calculate the real trend_res
            tmpData["Trend_Res"] = tmpData["Singal"] - tmpData["Trend"]

            # make prediction
            tmpData["pred_residual"] = self.residual_model_.predict(
                tmpData[self.X_col_ + self.mdl_eX_name_].values
            )
            tmpData["Trend"] = self.trend_model_.predict(
                tmpData["time"].values.reshape(-1, 1)
            )
            tmpData["predicted_y_" + str(i)] = (
                tmpData["pred_residual"] + tmpData["Trend"]
            )
            tmpData["predicted_y"] = tmpData["predicted_y_" + str(i)]
            impClm.append("predicted_y_" + str(i))

            # predict trend based on time
            # reassign the row value to old
            for lag_i in reversed(range(2, self.i_lookback_win_)):
                tmpData["Trend_Res_" + str(lag_i)] = tmpData[
                    "Trend_Res_" + str(lag_i - 1)
                ]
            # fill the first one
            tmpData["Trend_Res_1"] = tmpData["Trend_Res"]

        if pred_horizon == 1:
            return tmpData["predicted_y_0"].values[-1 * newX.shape[0] :]
        else:
            return tmpData[impClm].values[-1 * newX.shape[0] : -pred_horizon + 1, :]

    def _prepare_predict_X(self, newX):
        """
        This is the internal method for predict.
        """
        _X = self.X_["Singal"]
        _X = pd.DataFrame(_X, columns=["Singal"])
        _nX = pd.DataFrame(newX[:, self.target_columns], columns=["Singal"])
        _X = _X.append(_nX)
        _X.reset_index(inplace=True, drop=True)

        # add row number and time column
        _X["row_number"] = np.arange(0, _X.shape[0])
        _X["time"] = _X["row_number"]

        # add trend and residual value
        _X["Trend"] = self.trend_model_.predict(_X["time"].values.reshape(-1, 1))
        _X["Trend_Res"] = _X["Singal"] - _X["Trend"]
        res_array = list(_X["Trend_Res"])[-1 * self.i_lookback_win_ :]
        res_array.reverse()
        return _X["time"].max(), res_array

    def predict(self, X=None, B=None, pred_win=None, prediction_type="forecast"):
        """
        This method  is used for predicting future.
        Parameters
        ----------
            X : None.
            pred_win : (int, default=12) look ahead to be used for prediction.
        Returns
        -------
            numpy array.
        """
        if pred_win is None:
            pred_win = self.pred_win

        if prediction_type == "sliding":
            return self.update_multiple_observations(X, pred_horizon=pred_win)

        if X is None:
            # my first starting point is the last record we have in system
            start_v = self.predict_lookup.copy()
            pred = []
            for next_p in range(pred_win):

                # here we check is B is none?
                if B is not None:
                    start_vl = start_v.copy()
                    start_vl.extend(list(B[next_p, :]))
                else:
                    start_vl = start_v.copy()

                # residual model to predict the future residual
                #print(len(start_v))
                ans = self.residual_model_.predict(np.array(start_vl).reshape(1, -1))
                # output of trend model to predict the trend
                ans_1 = self.trend_model_.predict(
                    np.array(self.maxT_ + next_p + 1).reshape(1, -1)
                )

                # adjustment if array is produced
                if isinstance(ans_1, list):
                    ans_1 = ans_1[0]
                # prediction
                real_p = list(ans + ans_1)[0]
                pred.append(real_p)

                # since it is recursive, we put current residual at the first and pop the last one
                start_v.pop()
                start_v.insert(0, ans[0])

                # start_v is used in next iteration

            # return the final result
            return np.array(pred)
        else:
            # this method is an experimental.
            # prepare X first
            maxT, start_v = self._prepare_predict_X(X)
            pred = []
            for next_p in range(pred_win):
                # residual model to predict the future residual

                # here we check is B is none?
                if B is not None:
                    start_vl = start_v.copy()
                    start_vl.extend(list(B[next_p, :]))
                else:
                    start_vl = start_v.copy()

                ans = self.residual_model_.predict(np.array(start_vl).reshape(1, -1))
                # output of trend model to predict the trend
                ans_1 = self.trend_model_.predict(
                    np.array(maxT + next_p + 1).reshape(1, -1)
                )

                # adjustment if array is produced
                if isinstance(ans_1, list):
                    ans_1 = ans_1[0]
                # prediction
                real_p = list(ans + ans_1)[0]
                pred.append(real_p)

                # since it is recursive, we put current residual at the first and pop the last one
                start_v.pop()
                start_v.insert(0, ans[0])

                # start_v is used in next iteration

            # return the final result
            return np.array(pred)

    def predict_sliding_window(self, X):
        """
        This method is for single step prediction.
        Parameters
        ----------
            X : (numpy array) input data.
        Returns
        -------
            numpy array.
        """
        return self.update_multiple_observations(X, pred_horizon=1)

    def predict_multi_step_sliding_window(self, X, pred_win):
        """
        This method is for multi step prediction.
        Parameters
        ----------
            X : (numpy array) input data.
            pred_win : (int, default=12) look ahead to be used for prediction.
        Returns
        -------
            numpy array.
        """
        return self.update_multiple_observations(X, pred_horizon=pred_win)

    def predict_interval(self, X=None, pred_win=None, percentile=95):
        """
        This method  is used for getting predict_interval.
        Parameters
        ----------
            X : None.
            pred_win : (int, default=12) look ahead to be used for prediction.
            percentile : (int default=95)
        Returns
        -------
            numpy array.
        """

        if pred_win is None:
            pred_win = self.pred_win

        zval = st.norm.ppf(1 - ((100 - percentile) * 0.01 / 2))

        pred = []

        pred_itervals = []
        ans_interval = zval * self.res_res_stdev
        ans_1_interval = zval * self.trend_res_stdev

        if X is None:
            start_v = self.predict_lookup.copy()
            for next_p in range(pred_win):
                # residual model to predict the future residual
                ans = self.residual_model_.predict(np.array(start_v,dtype=object).reshape(1, -1))
                # lower and upper values for ans
                lower_ans, upper_ans = ans - ans_interval, ans + ans_interval
                # output of trend model to predict the trend
                ans_1 = self.trend_model_.predict(
                    np.array(self.maxT_ + next_p + 1).reshape(1, -1)
                )
                # adjustment if array is produced
                if isinstance(ans_1, list):
                    ans_1 = ans_1[0]
                # lower and upper values for ans1
                lower_ans_1, upper_ans_1 = (
                    ans_1 - ans_1_interval,
                    ans_1 + ans_1_interval,
                )

                # prediction
                real_p = list(ans + ans_1)[0]
                pred.append(real_p)

                # pred interval
                lower_real_p = list(lower_ans + lower_ans_1)[0]
                upper_real_p = list(upper_ans + upper_ans_1)[0]
                pred_itervals.append([lower_real_p, upper_real_p])

                # since it is recursive, we put current residual at the first and pop the last one
                start_v.pop()
                start_v.insert(0, ans)
                # start_v is used in next iteration
        else:
            # this method is an experimental.
            # prepare X first
            maxT, start_v = self._prepare_predict_X(X)
            pred = []
            for next_p in range(pred_win):
                # residual model to predict the future residual
                ans = self.residual_model_.predict(np.array(start_v,dtype=object).reshape(1, -1))
                # lower and upper values for ans
                lower_ans, upper_ans = ans - ans_interval, ans + ans_interval
                # output of trend model to predict the trend
                ans_1 = self.trend_model_.predict(
                    np.array(maxT + next_p + 1).reshape(1, -1)
                )

                # adjustment if array is produced
                if isinstance(ans_1, list):
                    ans_1 = ans_1[0]

                # prediction
                real_p = list(ans + ans_1)[0]
                pred.append(real_p)

                # pred interval
                lower_ans_1, upper_ans_1 = (
                    ans_1 - ans_1_interval,
                    ans_1 + ans_1_interval,
                )
                lower_real_p = list(lower_ans + lower_ans_1)[0]
                upper_real_p = list(upper_ans + upper_ans_1)[0]
                pred_itervals.append([lower_real_p, upper_real_p])

                # since it is recursive, we put current residual at the first and pop the last one
                start_v.pop()
                start_v.insert(0, ans[0])

        # return the final result
        return np.array(pred_itervals)
