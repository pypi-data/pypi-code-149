import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator
from autoai_ts_libs.deps.srom.time_series.models.T2RForecaster import T2RForecaster
from sklearn.base import clone
from joblib import Parallel, delayed
from multiprocessing import cpu_count


class MT2RForecaster(BaseEstimator, StateSpaceEstimator):
    """
    Trend-to-Residual Multi-Step Multi-Variate Singal Predictor.
    Parameters
    ----------
        target_columns : (list of int) index of target cols .
        trend : (string, default = Linear) Trend model to be used. It can be Linear, Difference.
        residual : (string, default = Linear) Residual model to be used. It can be Linear.
        lookback_win : (int or string, default = auto) Look-back window for the model.
        pred_win : (int, optional, default = 12) Look-ahead window for the model.
        n_jobs : (int, optional, default = -1) no of jobs.
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
        n_jobs=1,
    ):
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.trend = trend
        self.residual = residual
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.trained_models = []

        if n_jobs == -1:
            n_jobs = cpu_count() - 1
        if n_jobs < 1:
            n_jobs = 1
        self.n_jobs = n_jobs

    def name(self):
        return "MT2RForecaster"

    def _get_exogenous_cols(self):
        """"""
        exogenous_cols = []
        for fc in self.feature_columns:
            if not fc in self.target_columns:
                exogenous_cols.append(fc)
        return exogenous_cols

    def _fit_single_model(self, X, idx, i):
        _x = X[:, i]
        model_i = self.trained_models[idx]
        model_i.fit(_x)
        return model_i

    def _parallel_fit(self, X, y=None):
        """
        Utility to parallelize the code.
        """
        exogenous_cols = self._get_exogenous_cols()
        self.trained_models = Parallel(n_jobs=self.n_jobs)(
            delayed(self._fit_single_model)(X, idx, [item] + exogenous_cols)
            for idx, item in enumerate(self.target_columns)
        )

    def _sequential_fit(self, X, y=None):
        """
        Utility to run code sequentially.
        """
        exogenous_cols = self._get_exogenous_cols()
        for idx, i in enumerate(self.target_columns):
            cols = [i] + exogenous_cols
            _x = X[:, cols]
            self.trained_models[idx].fit(_x)

    def fit(self, X, y=None):
        """
        Fit the model.
        Parameters
        ----------
            X : (numpy array) input data.

        """
        # target columns might not be parameterized while creating object.
        if not self.target_columns:
            raise (
                "Argument `target_columns` has None value. Provide a valid value before proceeding with fit."
            )
        self.n_jobs = min(len(self.target_columns), self.n_jobs)

        # first time we create an empty model for each variable
        self.trained_models = []
        exogenous_cols = self._get_exogenous_cols()
        feature_columns = (
            list(range(0, len(exogenous_cols) + 1)) if len(exogenous_cols) > 0 else [0]
        )
        for i, col in enumerate(self.target_columns):
            self.trained_models.append(
                T2RForecaster(
                    trend=self.trend,
                    target_columns=[0],
                    feature_columns=feature_columns,
                    residual=self.residual,
                    lookback_win=self.lookback_win,
                    pred_win=self.pred_win,
                )
            )

        if self.n_jobs > 1:
            self._parallel_fit(X)
        else:
            self._sequential_fit(X)
        return self

    def _sequential_predict(self, X=None, B=None):
        """
        This function is for predicting future.
        """
        exogenous_cols = self._get_exogenous_cols()
        for idx, i in enumerate(self.target_columns):
            # When X is none don't pass any input.
            if X is None:
                pred = self.trained_models[idx].predict(B=B)
            else:
                cols = [i] + exogenous_cols
                try:
                    pred = self.trained_models[idx].predict(X=X[:, cols], B=B)
                except Exception as e:
                    raise Exception(
                        "Invalid input is specified for the model: "
                        + str(e)
                        + ". Correct the input and try again."
                    )
            if len(self.trained_models) > 1:
                reshaped = pred.reshape(-1, 1)
                if i == 0:
                    result = reshaped
                else:
                    result = np.hstack((result, reshaped))
            else:
                result = pred
        return result.flatten().reshape(-1, len(self.trained_models))

    def _predict(self, X, idx, index, B):
        # When X is none don't pass any input.
        if X is None:
            pred = self.trained_models[idx].predict(B=B)
        else:
            pred = self.trained_models[idx].predict(X=X[:, index], B=B)

        return pred

    def _parallel_predict(self, X=None, B=None):
        """
        Utility to parallelize the code.
        """
        exogenous_cols = self._get_exogenous_cols()
        ret_preds = Parallel(n_jobs=self.n_jobs)(
            delayed(self._predict)(X, idx, [item] + exogenous_cols, B)
            for idx, item in enumerate(self.target_columns)
        )

        for i, row in enumerate(ret_preds):
            if len(self.trained_models) > 1:
                reshaped = row.reshape(-1, 1)
                if i == 0:
                    result = reshaped
                else:
                    result = np.hstack((result, reshaped))
            else:
                result = row
        return result.flatten().reshape(-1, len(self.trained_models))

    def predict(self, X=None, B=None, prediction_type="forecast"):
        """
        This is to predict.
        Parameters
        ----------
            X : (numpy array) input data. It can be none as well.
            prediction_type : It can be sliding_window or forecast. Default is forecast.
        Returns
        -------
            numpy array.
        """
        if prediction_type.lower() == "sliding":
            if X is None:
                raise Exception("X cannot be None")
            elif self.pred_win == 1:
                return self.predict_sliding_window(X)
            elif self.pred_win > 1:
                return self.predict_multi_step_sliding_window(X, self.pred_win)
            else:
                raise Exception("prediction window is not supported.")

        if isinstance(X, pd.DataFrame):
            X = np.array(X)

        if self.n_jobs > 1:
            return self._parallel_predict(X, B)
        else:
            return self._sequential_predict(X, B)

    def _predict_single_model(self, X, idx, i):
        return self.trained_models[idx].predict_sliding_window(X[:, i])

    def _parallel_predict_sliding_window(self, X):
        """
        utility to parallelize the code.
        """
        exogenous_cols = self._get_exogenous_cols()
        self.ret_ans = Parallel(n_jobs=self.n_jobs)(
            delayed(self._predict_single_model)(X, idx, [item] + exogenous_cols)
            for idx, item in enumerate(self.target_columns)
        )

        return pd.DataFrame(self.ret_ans).T.values

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
        y = self._parallel_predict_sliding_window(X)
        return y

    def _predict_single_multi_step_model(self, X, idx, i, pred_win):
        return self.trained_models[idx].predict_multi_step_sliding_window(
            X[:, i], pred_win
        )

    def _parallel_predict_multi_step_sliding_window(self, X, pred_win):
        """
        internal function for predict.
        """
        exogenous_cols = self._get_exogenous_cols()
        self.ret_ans = Parallel(n_jobs=self.n_jobs)(
            delayed(self._predict_single_multi_step_model)(
                X, idx, [item] + exogenous_cols, pred_win
            )
            for idx, item in enumerate(self.target_columns)
        )

        ret_ans = np.empty(
            [self.ret_ans[0].shape[0], pred_win * len(self.trained_models)]
        )
        for dim_i in range(len(self.ret_ans)):
            for row_i in range(self.ret_ans[0].shape[0]):
                for col_i in range(pred_win):
                    ret_ans[
                        row_i, col_i * len(self.trained_models) + dim_i
                    ] = self.ret_ans[dim_i][row_i, col_i]
        return ret_ans

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
        y = self._parallel_predict_multi_step_sliding_window(X, pred_win)
        return y

    def predict_proba(self, X=None):
        """
        Prediction probability.
        Parameters
        ----------
            X : numpy array.
        Returns
        -------
            y : numpy array
        """
        if self.n_jobs > 1:
            return self._parallel_predict_proba(X)
        else:
            return self._sequential_predict_proba(X)

    def _sequential_predict_proba(self, X=None):
        """
        Helper function for predict_proba.
        """
        for idx, i in enumerate(self.target_columns):
            # When X is none don't pass any input.
            if X is None:
                pred = self.trained_models[idx].predict_interval()
            else:
                pred = self.trained_models[idx].predict_interval(X[:, i])
            # reshape by column and append by column.
            reshaped = pred.reshape(-1, 1, 2)
            if len(self.trained_models) > 1:
                if i == 0:
                    result = reshaped
                else:
                    result = np.hstack((result, reshaped))
            else:
                result = reshaped
        return result

    def _predict_proba(self, X, idx, index):
        # When X is none don't pass any input.
        if X is None:
            pred = self.trained_models[idx].predict_interval()
        else:
            pred = self.trained_models[idx].predict_interval(X[:, index])

        return pred

    def _parallel_predict_proba(self, X=None):
        """
        Helper function for predict_proba.
        """

        ret_preds = Parallel(n_jobs=self.n_jobs)(
            delayed(self._predict_proba)(X, idx, item)
            for idx, item in enumerate(self.target_columns)
        )

        for i, row in enumerate(ret_preds):
            reshaped = row.reshape(-1, 1, 2)
            if len(self.trained_models) > 1:
                if i == 0:
                    result = reshaped
                else:
                    result = np.hstack((result, reshaped))
            else:
                result = reshaped
        return result
