"""
.. module:: ts_transformer
   :synopsis: Contains TimeTensorTransformer class.

.. moduleauthor:: SROM Team
"""

import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from sklearn.utils import check_random_state
from sklearn.utils.validation import check_array, check_is_fitted
from autoai_ts_libs.deps.srom.feature_engineering.base import DataTransformer, TargetTransformer
from autoai_ts_libs.deps.srom.feature_engineering.timeseries.function_map import mapper
from autoai_ts_libs.deps.srom.utils.time_series_utils import get_max_lookback

# Constants

# Summary Statistics
PD_FUNC_LIST_SS = ["mean", "max", "min", "median", "sum", "std", "var"]

# Advanced Summary Statistics
FUNC_LIST_ASS = [
    "rate_of_change",
    "sum_of_change",
    "absoluate_sum_of_change",
    "trend_slop",
    "abs_energy",
    "mean_abs_change",
    "mean_change",
    "mean_second_derivate_central",
    "count_above_mean",
    "count_below_mean",
    "last_location_of_maximum",
    "first_location_of_maximum",
    "corr_coefficient",
]

# Wavelet Features
FUNC_LIST_WT = ["wavelet_feature_haar"]

# FFT Features
FUNC_LIST_FFT = ["fft_coefficient_real"]

# Higher Order Features
FUNC_LIST_HOF = ["quantile_25", "quantile_75", "quantile_range"]
PD_FUNC_LIST_HOF = ["sum", "skew", "kurt"]

# All Features
FUNC_LIST_UNION = (
    FUNC_LIST_ASS + FUNC_LIST_FFT + FUNC_LIST_HOF
)  # +FUNC_LIST_WT  #Todo Dissable as wavelet support is not there.
PD_FUNC_LIST_UNION = PD_FUNC_LIST_SS + PD_FUNC_LIST_HOF


class TimeTensorTransformer(DataTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the \
            number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        id_column=None,
        time_column=None,
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
        mode="forecasting",
    ):
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.id_column = id_column
        self.time_column = time_column
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.skip_observation = skip_observation
        self.mode = mode

    def _check_meta_data(self, data_shape):
        if self.feature_columns is None:
            raise Exception(
                "`feature_columns` is set to `None`. Set the value for `feature_columns`"
            )
        if self.target_columns is None:
            raise Exception(
                "`target_columns` is set to `None`. Set the value for `target_columns`"
            )
        if (
            get_max_lookback(self.lookback_win) + self.pred_win + self.skip_observation
        ) > data_shape[0]:
            err = "sum of history window size ({})".format(
                get_max_lookback(self.lookback_win)
            )
            err += " and prediction window size({})".format(self.pred_win)
            err += " and skip observations ({})".format(self.skip_observation)
            err += " should be less than data set size({})".format(data_shape[0])
            raise Exception(err)

    def _check_window_params(self):
        if isinstance(self.lookback_win, list):
            if len(self.feature_columns) != len(self.lookback_win):
                raise Exception(
                    "1 or more feature columns should have mapping lookback window"
                )

        if self.skip_observation < 0:
            err = "skip observation should be greater than 0"
            raise Exception(err)

    def _apply_custom_transformer_func(self, func_list, values, col_prefix=""):
        temp = []
        cols = []
        for func in func_list:
            t_x = mapper(func)(values)
            if isinstance(t_x, (list, np.ndarray)):
                for i, t_x_i in enumerate(t_x):
                    cols.append(col_prefix + func + "_" + str(i))
                    temp.append(t_x_i)
            else:
                cols.append(col_prefix + func)
                temp.append(t_x)

        temp_df = pd.DataFrame(np.array([temp]), columns=cols)
        return temp_df

    def _apply_transformer_func(self, df, func_list=None, pd_func_list=None):
        transformed_df = None
        for col in df.columns:
            col_prefix = "c" + str(col) + "_"

            if func_list is not None:
                if not isinstance(transformed_df, pd.DataFrame):
                    transformed_df = self._apply_custom_transformer_func(
                        func_list, df[col], col_prefix
                    )
                else:
                    temp_df = self._apply_custom_transformer_func(
                        func_list, df[col], col_prefix
                    )
                    transformed_df = pd.concat([transformed_df, temp_df], axis=1)
            if pd_func_list is not None:
                new_pd_func_list = [col_prefix + x for x in pd_func_list]
                new_ser = df[col].agg(pd_func_list)
                temp_df = pd.DataFrame(new_ser.tolist(), index=new_pd_func_list)

                if transformed_df is None:
                    transformed_df = temp_df.T
                else:
                    transformed_df = pd.concat([transformed_df, temp_df.T], axis=1)

        return transformed_df

    def _fit_classification(self, X, y=None):
        """fit method for classification

        Args:
            X (_type_): _description_
            y (_type_, optional): _description_. Defaults to None.
        """
        pass

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        self._check_meta_data(X.shape)
        # self._check_window_params()   # TODO: this check has Exception: skip observation should be greater than 0
        if isinstance(X, (np.ndarray, np.generic)):
            X = check_array(X, accept_sparse=True, dtype=None)
        self.n_features_ = X.shape[1]
        return self

    def _transform_classification(self, X, y=None):
        self._check_meta_data(X.shape)

        # copy X and y
        _X = X.copy()

        if y is not None:
            _y = y.copy()

        # the intput X and y are converted to pd.DataFrame since it is easier to do groupby() and fill() in pandas
        if isinstance(_X, np.ndarray):
            _X = pd.DataFrame(_X, columns=range(_X.shape[1]))

        if y is not None:
            if isinstance(_y, np.ndarray):
                _y = pd.DataFrame(_y, columns=range(_y.shape[1]))

            if _X.shape[0] != _y.shape[0]:
                raise ValueError("X and y are not in same length.")

        # check id_column, time_column, feature_columns, target_columns
        X_columns = self.feature_columns + [self.id_column, self.time_column]
        for col in X_columns:
            if col not in list(_X.columns) and col is not None:
                raise ValueError("{} is not in X.".format(col))

        if y is not None:
            y_columns = self.target_columns + [self.id_column, self.time_column]
            for col in y_columns:
                if col not in list(_y.columns) and col is not None:
                    raise ValueError("{} is not in y.".format(col))

            if (
                not isinstance(self.target_columns, list)
                or len(self.target_columns) != 1
            ):
                raise ValueError(
                    "target_columns needs to be a list with a single value."
                )

        lookback_win = get_max_lookback(self.lookback_win)
        X_out, y_out = [], []
        context_ = []

        if lookback_win > 0:
            if y is not None:
                # backward fill or forward fill 1's in _y based on pred_win
                if self.pred_win == 0:  # do nothing
                    pass
                elif self.pred_win < 0:  # forward fill
                    _y[self.target_columns[0]][_y[self.target_columns[0]] == 0] = np.nan
                    grouped = _y.groupby(self.id_column)
                    for name, group in grouped:
                        mask = (
                            group[self.target_columns[0]].ffill(limit=-self.pred_win)
                            == 1
                        )
                        pos_idx = list(mask[mask].index.values)
                        _y.loc[pos_idx, self.target_columns[0]] = 1
                    _y[self.target_columns[0]] = _y[self.target_columns[0]].fillna(0)
                elif self.pred_win > 0:  # backward fill
                    _y[self.target_columns[0]][_y[self.target_columns[0]] == 0] = np.nan
                    grouped = _y.groupby(self.id_column)
                    for name, group in grouped:
                        mask = (
                            group[self.target_columns[0]].bfill(limit=self.pred_win)
                            == 1
                        )
                        pos_idx = list(mask[mask].index.values)
                        _y.loc[pos_idx, self.target_columns[0]] = 1
                    _y[self.target_columns[0]] = _y[self.target_columns[0]].fillna(0)
                else:
                    # TODO: pred_win == auto
                    pass

            # append each rows one by one to outputs
            target_col = "label"
            if y is not None:
                _X[target_col] = _y[self.target_columns[0]]
            for name, group in _X.groupby(self.id_column):
                for i in range(lookback_win, group.shape[0] + 1):
                    X_out.append(group[self.feature_columns][i - lookback_win : i])
                    if y is not None:
                        y_out.append(
                            group.iloc[i - 1, group.columns.get_loc(target_col)]
                        )
                    context_.append(
                        group[[self.id_column, self.time_column]]
                        .iloc[[i - 1]]
                        .values.tolist()
                    )

            # convert to numpy array
            X_out, y_out, context_ = (
                np.array(X_out),
                np.array(y_out),
                np.array(context_),
            )
        self.context_ = context_
        return X_out, y_out

    def _transform_forecasting(self, X, y=None):
        self._check_meta_data(X.shape)
        if isinstance(X, pd.DataFrame):
            X = X.values

        X = check_array(X, accept_sparse=True, dtype=None)
        check_is_fitted(self, "n_features_")
        if X.shape[1] != self.n_features_:
            raise ValueError(
                "Shape of input is different from what was seen" "in `fit`"
            )

        _x, _y = [], []
        if get_max_lookback(self.lookback_win) > 0:
            for i in range(
                get_max_lookback(self.lookback_win) + self.skip_observation,
                X.shape[0] - self.pred_win + 1,
            ):
                _x.append(
                    X[i - get_max_lookback(self.lookback_win) : i, self.feature_columns]
                )
                if self.pred_win > 1:
                    _y.append(X[i : i + self.pred_win, self.target_columns])
                else:
                    _y.append(X[i + self.pred_win - 1, self.target_columns])
            _x, _y = np.array(_x), np.array(_y)
        elif (
            get_max_lookback(self.lookback_win) <= -1
        ):  # to support univariate arima model
            _x = X[self.skip_observation :, self.feature_columns]
            _x = _x.flatten()
            _y = _x.copy()
        else:
            raise Exception("Not Supported...")

        # this is to ensure that the underlying numpy array is numeric
        if _x.dtype == "object":
            _x = _x.astype(float)
        if _y.dtype == "object":
            _y = _y.astype(float)

        return _x, _y

    def transform(self, X, y=None):
        if self.mode == "forecasting":
            return self._transform_forecasting(X, y)
        elif self.mode == "classification":
            return self._transform_classification(X, y)
        else:
            raise ValueError("mode is classification or forecasting")

    def fit_transform(self, X, y=None, **fit_params):
        return self.fit(X, y).transform(X, y)


class Flatten(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.
    This utility support univariate, multi-variate, single-step and multi-step functionality.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        id_column=None,
        time_column="time",
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
        mode="forecasting",
    ):

        super(Flatten, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            id_column=id_column,
            time_column=time_column,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
            mode=mode,
        )

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        _x, _y = super(Flatten, self).transform(X, y)

        # Regular flattening of 3D data to 2D data for consumption of IID models
        if not isinstance(self.lookback_win, list):
            _x = [list(_x[i].flatten()) for i in range(len(_x))]
        else:
            max_lookback = get_max_lookback(self.lookback_win)
            _x_tf = []
            for i in range(len(_x)):
                row = _x[i]
                x_tf_row = np.array([])
                for idx, fc_win in enumerate(self.lookback_win):
                    if isinstance(fc_win, list):
                        idx_list = [[max_lookback - idx] for idx in fc_win]
                        x_tf_row = np.concatenate(
                            (
                                x_tf_row,
                                row[idx_list, [idx]].flatten(),
                            )
                        )
                    else:
                        x_tf_row = np.concatenate(
                            (
                                x_tf_row,
                                row[fc_win * -1 :, [idx]].flatten(),
                            )
                        )
                _x_tf.append(x_tf_row)
            _x = _x_tf
        _x = np.array(_x)

        if self.mode == "forecasting":
            if self.pred_win == 1:
                # Single Step Support
                if len(self.target_columns) > 1:
                    _y = _y.reshape(-1, len(self.target_columns))
                else:
                    _y = np.array(_y.ravel()).reshape(-1, 1)
            elif self.pred_win > 1:
                # Multi Step Support
                if len(self.target_columns) == 1:
                    _y = _y.reshape(-1, self.pred_win)
                else:
                    _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
            else:
                # this part is for pred_win = 0
                _y = _y.reshape(-1, len(self.target_columns))
        elif self.mode == "classification":
            _y = _y.reshape(-1, len(self.target_columns))
        else:
            pass

        return _x, _y


class WaveletFeatures(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing
    using WaveletFeatures Transformer

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        lookback_win (int, optional): Look-back window for the model.
        pred_win (int): Look-ahead window for the model.

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_jobs=None,
        apply_mean_imputation=True,
    ):

        super(WaveletFeatures, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )
        self.n_jobs = n_jobs
        self.apply_mean_imputation = apply_mean_imputation

    def _transform(self, X, y=None):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        # self._check_window_params()
        _x, _y = super(WaveletFeatures, self).transform(X)

        # @TODO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]
        func_list = FUNC_LIST_WT

        transformed_x = Parallel(n_jobs=self.n_jobs)(
            delayed(self._apply_transformer_func)(item, func_list=func_list)
            for item in _x
        )
        _x = transformed_x
        col_len = len(_x[0].columns)
        self._output_data_dim = (None, col_len * len(self.feature_columns))
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        if self.pred_win == 1:
            # Single Step Support
            if len(self.target_columns) > 1:
                _y = _y.reshape(-1, len(self.target_columns))
            else:
                _y = np.array(_y.ravel()).reshape(-1, 1)
        elif self.pred_win > 1:
            # Multi Step Support
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
        else:
            _y = _y.reshape(-1, len(self.target_columns))
        return _x, _y

    def transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if self.apply_mean_imputation:
            check_is_fitted(self, "learned_x_mean_")
        _x, _y = self._transform(X, y)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y

    def fit_transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        self.fit(X, y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y


class FFTFeatures(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing
    using FFTFeatures Transformer

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        lookback_win (int, optional): Look-back window for the model.
        pred_win (int): Look-ahead window for the model.

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_jobs=None,
        apply_mean_imputation=True,
    ):

        super(FFTFeatures, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )
        self.n_jobs = n_jobs
        self.apply_mean_imputation = apply_mean_imputation

    def _transform(self, X, y=None):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        # self._check_window_params()
        _x, _y = super(FFTFeatures, self).transform(X)

        # @TODO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]

        func_list = FUNC_LIST_FFT
        transformed_x = Parallel(n_jobs=self.n_jobs)(
            delayed(self._apply_transformer_func)(item, func_list=func_list)
            for item in _x
        )

        _x = transformed_x
        col_len = len(_x[0].columns)
        self._output_data_dim = (None, col_len * len(self.feature_columns))
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        if self.pred_win == 1:
            # Single Step Support
            if len(self.target_columns) > 1:
                _y = _y.reshape(-1, len(self.target_columns))
            else:
                _y = np.array(_y.ravel()).reshape(-1, 1)
        elif self.pred_win > 1:
            # Multi Step Support
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
        else:
            _y = _y.reshape(-1, len(self.target_columns))
        return _x, _y

    def transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if self.apply_mean_imputation:
            check_is_fitted(self, "learned_x_mean_")
        _x, _y = self._transform(X, y)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y

    def fit(self,X,y=None):
        super().fit(X,y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        return self

    def fit_transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        self.fit(X, y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y


class SummaryStatistics(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing
    using SS(Summary Statistics) Transformer

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        lookback_win (int, optional): Look-back window for the model.
        pred_win (int): Look-ahead window for the model.

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_jobs=None,
        apply_mean_imputation=True,
    ):

        super(SummaryStatistics, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )
        self.n_jobs = n_jobs
        self.apply_mean_imputation = apply_mean_imputation

    def _transform(self, X, y=None):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        # self._check_window_params()
        _x, _y = super(SummaryStatistics, self).transform(X)

        # @TODO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]

        pd_func_list = PD_FUNC_LIST_SS
        transformed_x = Parallel(n_jobs=self.n_jobs)(
            delayed(self._apply_transformer_func)(item, pd_func_list=pd_func_list)
            for item in _x
        )

        _x = transformed_x
        col_len = len(_x[0].columns)
        self._output_data_dim = (None, col_len * len(self.feature_columns))
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        if self.pred_win == 1:
            # Single Step Support
            if len(self.target_columns) > 1:
                _y = _y.reshape(-1, len(self.target_columns))
            else:
                _y = np.array(_y.ravel()).reshape(-1, 1)
        elif self.pred_win > 1:
            # Multi Step Support
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
        else:
            _y = _y.reshape(-1, len(self.target_columns))
        return _x, _y

    def transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if self.apply_mean_imputation:
            check_is_fitted(self, "learned_x_mean_")
        _x, _y = self._transform(X, y)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y
    
    def fit(self,X,y=None):
        super().fit(X,y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        return self
    
    def fit_transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        self.fit(X, y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y


class AdvancedSummaryStatistics(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing
    using ASS(Advanced Summary Statistics) Transformer

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        lookback_win (int, optional): Look-back window for the model.
        pred_win (int): Look-ahead window for the model.

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_jobs=None,
        apply_mean_imputation=True,
    ):

        super(AdvancedSummaryStatistics, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )
        self.n_jobs = n_jobs
        self.apply_mean_imputation = apply_mean_imputation

    def _transform(self, X, y=None):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        # self._check_window_params()
        _x, _y = super(AdvancedSummaryStatistics, self).transform(X)

        # @TODO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]
        func_list = FUNC_LIST_ASS
        transformed_x = Parallel(n_jobs=self.n_jobs)(
            delayed(self._apply_transformer_func)(item, func_list=func_list)
            for item in _x
        )

        _x = transformed_x
        col_len = len(_x[0].columns)
        self._output_data_dim = (None, col_len * len(self.feature_columns))
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        if self.pred_win == 1:
            # Single Step Support
            if len(self.target_columns) > 1:
                _y = _y.reshape(-1, len(self.target_columns))
            else:
                _y = np.array(_y.ravel()).reshape(-1, 1)
        elif self.pred_win > 1:
            # Multi Step Support
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
        else:
            _y = _y.reshape(-1, len(self.target_columns))
        return _x, _y

    def transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if self.apply_mean_imputation:
            check_is_fitted(self, "learned_x_mean_")
        _x, _y = self._transform(X, y)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y

    def fit(self,X,y=None):
        super().fit(X,y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        return self
    
    def fit_transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        self.fit(X, y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y


class HigherOrderStatistics(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing
    using HOS(Higher Order Statistics) Transformer

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        lookback_win (int, optional): Look-back window for the model.
        pred_win (int): Look-ahead window for the model.

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_jobs=None,
        apply_mean_imputation=True,
    ):

        super(HigherOrderStatistics, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )
        self.n_jobs = n_jobs
        self.apply_mean_imputation = apply_mean_imputation

    def _transform(self, X, y=None):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        # self._check_window_params()
        _x, _y = super(HigherOrderStatistics, self).transform(X)

        # @TODO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]

        func_list = FUNC_LIST_HOF
        pd_func_list = PD_FUNC_LIST_HOF
        transformed_x = Parallel(n_jobs=self.n_jobs)(
            delayed(self._apply_transformer_func)(
                item, func_list=func_list, pd_func_list=pd_func_list
            )
            for item in _x
        )

        _x = transformed_x
        col_len = len(_x[0].columns)
        self._output_data_dim = (None, col_len * len(self.feature_columns))
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        if self.pred_win == 1:
            # Single Step Support
            if len(self.target_columns) > 1:
                _y = _y.reshape(-1, len(self.target_columns))
            else:
                _y = np.array(_y.ravel()).reshape(-1, 1)
        elif self.pred_win > 1:
            # Multi Step Support
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
        else:
            _y = _y.reshape(-1, len(self.target_columns))
        return _x, _y

    def transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if self.apply_mean_imputation:
            check_is_fitted(self, "learned_x_mean_")
        _x, _y = self._transform(X, y)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y

    def fit(self,X,y=None):
        super().fit(X,y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        return self

    
    def fit_transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        self.fit(X, y)
        self.learned_x_mean_ = []
        _x, _y = self._transform(X, y)
        self.learned_x_mean_ = np.nanmean(_x, axis=0)
        if self.apply_mean_imputation:
            inds = np.where(np.isnan(_x))
            _x[inds] = np.take(self.learned_x_mean_, inds[1])
        return _x, _y


class TimeSeriesFeatureUnion(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing
    using TimeSeriesFeatureUnion Transformer. (includes Summary Statistics, Advanced Summary Statistics,
    Higher Order Statistics, Wavelet and FFT featuers)

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        lookback_win (int, optional): Look-back window for the model.
        pred_win (int): Look-ahead window for the model.

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_jobs=None,
    ):

        super(TimeSeriesFeatureUnion, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )
        self.n_jobs = n_jobs

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        # self._check_window_params()
        _x, _y = super(TimeSeriesFeatureUnion, self).transform(X)

        # TO DO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]

        func_list = FUNC_LIST_UNION
        pd_func_list = PD_FUNC_LIST_UNION
        transformed_x = Parallel(n_jobs=self.n_jobs)(
            delayed(self._apply_transformer_func)(
                item, func_list=func_list, pd_func_list=pd_func_list
            )
            for item in _x
        )

        _x = transformed_x
        col_len = len(_x[0].columns)
        self._output_data_dim = (None, col_len * len(self.feature_columns))
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        if self.pred_win == 1:
            # Single Step Support
            if len(self.target_columns) > 1:
                _y = _y.reshape(-1, len(self.target_columns))
            else:
                _y = np.array(_y.ravel()).reshape(-1, 1)
        elif self.pred_win > 1:
            # Multi Step Support
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
        else:
            _y = _y.reshape(-1, len(self.target_columns))
        return _x, _y


class customTimeSeriesFeatures(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing
    using TimeSeriesFeatureUnion Transformer. (includes Summary Statistics, Advanced Summary Statistics,
    Higher Order Statistics, Wavelet and FFT featuers)

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        lookback_win (int, optional): Look-back window for the model.
        pred_win (int): Look-ahead window for the model.
        func_list (list): name of features
        pd_func_list (list): name of features based on pandas

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        func_list,
        pd_func_list,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_jobs=None,
    ):

        super(customTimeSeriesFeatures, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )
        self.n_jobs = n_jobs
        self.func_list = func_list
        self.pd_func_list = pd_func_list

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        # self._check_window_params()
        _x, _y = super(customTimeSeriesFeatures, self).transform(X)

        # TO DO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]

        func_list = self.func_list
        pd_func_list = self.pd_func_list
        transformed_x = Parallel(n_jobs=self.n_jobs)(
            delayed(self._apply_transformer_func)(
                item, func_list=func_list, pd_func_list=pd_func_list
            )
            for item in _x
        )
        _x = transformed_x
        col_len = len(_x[0].columns)
        self._output_data_dim = (None, col_len * len(self.feature_columns))
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        if self.pred_win == 1:
            # Single Step Support
            if len(self.target_columns) > 1:
                _y = _y.reshape(-1, len(self.target_columns))
            else:
                _y = np.array(_y.ravel()).reshape(-1, 1)
        elif self.pred_win > 1:
            # Multi Step Support
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
        else:
            _y = _y.reshape(-1, len(self.target_columns))
        return _x, _y


class RandomTimeTensorTransformer(TimeTensorTransformer):
    """
    Prepare Randomized data to be consumed by the model either for training.
    Random Samples are ordered w.r.t. input data

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the \
            number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
        n_intervals (string or float or int): number of intervals to be generated, \
            default : 'sqrt' of total samples,
            other values: positive number,
                        log of total samples,
                        float with <= 1.0 and >= 0
        random_state (None or int): setting seed of randomness

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_intervals="sqrt",
        random_state=None,
    ):
        super(RandomTimeTensorTransformer, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )

        self.n_intervals = n_intervals
        self.random_state = random_state

    def predict_transform(self, X, y=None):
        """
        Transform the data w/o dropping records
        """
        return super(RandomTimeTensorTransformer, self).transform(X, y)

    def transform(self, X, y=None):
        self._check_meta_data(X.shape)
        if isinstance(X, pd.DataFrame):
            X = X.values

        X = check_array(X, accept_sparse=True, dtype=None)

        check_is_fitted(self, "n_features_")
        if X.shape[1] != self.n_features_:
            raise ValueError(
                "Shape of input is different from what was seen" "in `fit`"
            )

        len_series = X.shape[0]
        _x, _y = [], []
        if self.lookback_win > 0:
            if self.n_intervals == "sqrt":
                n_intervals = int(np.sqrt(len_series))
            elif self.n_intervals == "log":
                n_intervals = int(np.log(len_series))
            elif (
                np.issubdtype(type(self.n_intervals), np.floating)
                and (self.n_intervals > 0)
                and (self.n_intervals <= 1)
            ):
                n_intervals = int(len_series * self.n_intervals)
            else:
                raise ValueError(
                    f'Number of intervals must be either "sqrt", a positive integer, or a float '
                    f"value between 0 and 1, but found {self.n_intervals}."
                )
            n_intervals = np.maximum(1, n_intervals)

            _rng = check_random_state(self.random_state)
            ind_value = _rng.randint(
                self.lookback_win, len_series - self.pred_win + 1, size=n_intervals
            )
            ind_value.sort()

            for i in ind_value:
                _x.append(X[i - self.lookback_win : i, self.feature_columns])
                # _y.append(X[i + self.pred_win-1, self.target_columns])
                if self.pred_win > 1:
                    _y.append(X[i : i + self.pred_win, self.target_columns])
                else:
                    _y.append(X[i + self.pred_win - 1, self.target_columns])
            _x, _y = np.array(_x), np.array(_y)
        else:
            raise Exception("Not Supported...")

        return _x, _y


class RandomTimeSeriesFeatures(RandomTimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing
    using RandomTimeSeriesFeatures Transformer.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        lookback_win (int, optional): Look-back window for the model.
        pred_win (int): Look-ahead window for the model.
        n_intervals (string or float or int): number of intervals to be generated, \
            default : 'sqrt' of total samples,
            other values: positive number,
                        log of total samples,
                        float with <= 1.0 and >= 0
        random_state (None or int): setting seed of randomness
        n_random_features (int): number of time series features to be selected
        baseline_feature (string: default 'identity'): features to be used as a baseline

    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        n_intervals="sqrt",
        random_state=None,
        n_random_features=3,
        baseline_feature="identity",
        n_jobs=None,
    ):

        super(RandomTimeSeriesFeatures, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            n_intervals=n_intervals,
            random_state=random_state,
        )
        self.n_jobs = n_jobs
        self.n_random_features = n_random_features
        self.baseline_feature = baseline_feature

        # function lists
        self.func_list = None
        self.pd_func_list = None

    def _init_features_bundle(self):
        if not self.func_list and not self.pd_func_list:
            from autoai_ts_libs.deps.srom.feature_engineering.timeseries.function_map import (
                get_random_featureset,
            )

            self.pd_func_list, self.func_list = get_random_featureset(
                self.n_random_features
            )
            if self.baseline_feature:
                if self.func_list:
                    if self.baseline_feature not in self.func_list:
                        self.func_list.append(self.baseline_feature)
                else:
                    self.func_list = [self.baseline_feature]

    def fit(self, X, y=None):
        self._check_meta_data(X.shape)
        X = check_array(X, accept_sparse=True, dtype=None)
        self.n_features_ = X.shape[1]

        # call function to fix the features to be extracted
        self._init_features_bundle()

        return self

    def _transform(self, X, y=None, mode="train"):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        # self._check_window_params()
        if mode == "train":
            _x, _y = super(RandomTimeSeriesFeatures, self).transform(X)
        elif mode == "predict":
            _x, _y = super(RandomTimeSeriesFeatures, self).predict_transform(X)
        else:
            Exception("Not Supported...")

        # TO DO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]

        func_list = self.func_list
        pd_func_list = self.pd_func_list
        transformed_x = Parallel(n_jobs=self.n_jobs)(
            delayed(self._apply_transformer_func)(
                item, func_list=func_list, pd_func_list=pd_func_list
            )
            for item in _x
        )

        _x = transformed_x
        col_len = len(_x[0].columns)
        self._output_data_dim = (None, col_len * len(self.feature_columns))
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        if self.pred_win == 1:
            # Single Step Support
            if len(self.target_columns) > 1:
                _y = _y.reshape(-1, len(self.target_columns))
            else:
                _y = np.array(_y.ravel()).reshape(-1, 1)
        elif self.pred_win > 1:
            # Multi Step Support
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = _y.reshape(-1, self.pred_win * len(self.target_columns))
        else:
            _y = _y.reshape(-1, len(self.target_columns))

        return _x, _y

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        # self._check_flatten_type(self.flatten_type)
        return self._transform(X, y, "train")

    def predict_transform(self, X, y=None):
        # calling the function to first create time tensors
        # this will make sure that tensor is not dropped
        # self._check_flatten_type(self.flatten_type)
        return self._transform(X, y, "predict")


class NormalizedFlatten(TimeTensorTransformer, TargetTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
    ):

        super(NormalizedFlatten, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
        )

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        _x, _y = super(NormalizedFlatten, self).transform(X)

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [
            list(_x[i][:, j].flatten())
            for i in range(len(_x))
            for j in range(len(self.feature_columns))
        ]
        _x = np.array(_x)

        self._x_mean = _x.mean(axis=1).reshape(-1, 1)
        self._x_std = _x.std(axis=1).reshape(-1, 1)
        self._x_std[self._x_std == 0] = 1.0
        _x = (_x - self._x_mean) / self._x_std

        if self.pred_win == 1:
            _y = np.array(_y.ravel()).reshape(-1, 1)
            _y = (_y - self._x_mean) / self._x_std
        else:
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
                _y = (_y - self._x_mean) / self._x_std
            else:
                _y = [
                    list(_y[i][:, j].flatten())
                    for i in range(len(_y))
                    for j in range(len(self.target_columns))
                ]
                _y = np.array(_y)
                _y = (_y - self._x_mean) / self._x_std

        return _x, _y

    def inverse_transform(self, y):
        # make sure we have correct shape of y
        if self.pred_win == 1:
            y = y.reshape(-1, 1)
        else:
            y = y.reshape(-1, self.pred_win)
        return (y * self._x_std) + self._x_mean


class DifferenceFlatten(TimeTensorTransformer, TargetTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
    ):

        super(DifferenceFlatten, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
        )

    def _check_meta_data(self, data_shape):
        """Override parent method

        Args:
            data_shape ([type]): [description]

        Raises:
            Exception: [description]

        Returns:
            [type]: [description]
        """
        super()._check_meta_data(data_shape)

        def _check_col_index():
            for i in range(len(self.feature_columns)):
                if self.feature_columns[i] != self.target_columns[i]:
                    return True
            return False

        if (
            len(self.feature_columns) != len(self.target_columns)
            or set(self.feature_columns) != set(self.target_columns)
            or _check_col_index()
        ):
            raise Exception("Value of feature_columns and target_columns must match")

    def transform(self, X, y=None):
        # calling the function to first create time tensors

        _x, _y = super(DifferenceFlatten, self).transform(X)

        # Regular flattening of 3D data to 2D data for consumption of IID models
        self._x_last = np.array(
            [
                list(_x[i][:, j])[-1]
                for i in range(len(_x))
                for j in range(len(self.feature_columns))
            ]
        ).reshape(-1, 1)

        _x = [
            list(np.diff(_x[i][:, j]))
            for i in range(len(_x))
            for j in range(len(self.feature_columns))
        ]

        _x = np.array(_x)

        if self.pred_win == 1:
            _y = np.array(_y.ravel()).reshape(-1, 1)

            _y = _y - self._x_last

        else:
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)

                _y = _y - self._x_last

            else:
                _y = [
                    list(_y[i][:, j].flatten())
                    for i in range(len(_y))
                    for j in range(len(self.target_columns))
                ]

                _y = np.array(_y)
                _y = _y - self._x_last

        return _x, _y

    def inverse_transform(self, y):
        if self.pred_win == 1:
            y = y.reshape(-1, 1)
        else:
            y = y.reshape(-1, self.pred_win)
        return y + self._x_last


class DifferenceFlattenX(TimeTensorTransformer, TargetTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self, feature_columns=[0], target_columns=[0], lookback_win=1, pred_win=1
    ):
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.pred_win = pred_win

    def _pre_fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Raises:
            Exception: [description]
        """
        # define two internal trasformer
        self.diff_lookback_win_ = self.flatten_lookback_win_ = self.lookback_win
        self.flatten_features_ = []
        if len(self.feature_columns) > len(self.target_columns):
            for item_index, item in enumerate(self.feature_columns):
                if item not in self.target_columns:
                    self.flatten_features_.append(item)
        else:
            raise Exception("feature columns should be larger")

        if isinstance(self.lookback_win, list):
            self.diff_lookback_win_ = []
            self.flatten_lookback_win_ = []
            for item_index, item in enumerate(self.feature_columns):
                if item in self.target_columns:
                    self.diff_lookback_win_.append(self.lookback_win[item_index])
                else:
                    self.flatten_lookback_win_.append(self.lookback_win[item_index])

        # adjust the skip record if max_lookback of the group is higher than the individual records
        skip_observation_for_tmp_difference_flatten_ = get_max_lookback(
            self.lookback_win
        ) - get_max_lookback(self.diff_lookback_win_)

        self.tmp_difference_flatten_ = DifferenceFlatten(
            feature_columns=self.target_columns,
            target_columns=self.target_columns,
            pred_win=self.pred_win,
            lookback_win=self.diff_lookback_win_,
            skip_observation=skip_observation_for_tmp_difference_flatten_,
        )

        skip_observation_for_flatten_ = get_max_lookback(
            self.lookback_win
        ) - get_max_lookback(self.flatten_lookback_win_)

        self.tmp_flatten_ = Flatten(
            feature_columns=self.flatten_features_,
            target_columns=self.target_columns,
            pred_win=self.pred_win,
            lookback_win=self.flatten_lookback_win_,
            skip_observation=skip_observation_for_flatten_,
        )

    def _check_meta_data(self):
        if self.feature_columns is None:
            raise Exception(
                "`feature_columns` is set to `None`. Set the value for `feature_columns`"
            )
        if self.target_columns is None:
            raise Exception(
                "`target_columns` is set to `None`. Set the value for `target_columns`"
            )
        if not set(self.target_columns).issubset(set(self.feature_columns)):
            raise Exception(
                "1 or more `target_columns` are not present in `feature_columns`"
            )

    def _check_window_params(self):
        if isinstance(self.lookback_win, list):
            if len(self.feature_columns) != len(self.lookback_win):
                raise Exception(
                    "1 or more feature columns should have mapping lookback window"
                )

    def fit(self, X, y=None):
        self._check_meta_data()
        self._check_window_params()
        self._pre_fit(X, y)
        self.tmp_difference_flatten_.fit(X, y)
        self.tmp_flatten_.fit(X, y)
        return self

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        check_is_fitted(self, "tmp_difference_flatten_")
        check_is_fitted(self, "tmp_flatten_")
        _d_x, _d_y = self.tmp_difference_flatten_.transform(X, y)
        _f_x, _ = self.tmp_flatten_.transform(X, y)
        # we expect now _d_x and _f_x shd match on number of rows
        _f_x = np.repeat(_f_x, repeats=len(self.target_columns), axis=0)
        _x = np.concatenate(
            (_d_x, _f_x),
            axis=1,
        )
        return _x, _d_y

    def inverse_transform(self, y):
        check_is_fitted(self, "tmp_difference_flatten_")
        # this place I will make sure, the number of records in y is same as
        # number of record emited by transform method of tmp_difference_flatten_ class
        # if they are not then i shd append the few records at the start of y and then
        # feed y to the Difference Flattern.
        return self.tmp_difference_flatten_.inverse_transform(y)
        """
        return self.tmp_difference_flatten_.inverse_transform(y)[
            -len(self.tmp_difference_flatten_.target_columns) :,
        ]
        """


class DifferenceNormalizedFlatten(DifferenceFlatten):
    """
    Prepare the data to be consumed by the model either for training or testing.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self, feature_columns=[0], target_columns=[0], lookback_win=1, pred_win=1
    ):

        super(DifferenceNormalizedFlatten, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        _x, _y = super(DifferenceNormalizedFlatten, self).transform(X)

        self._x_mean = _x.mean(axis=1).reshape(-1, 1)
        self._x_std = _x.std(axis=1).reshape(-1, 1)
        self._x_std[self._x_std == 0] = 1.0
        _x = (_x - self._x_mean) / self._x_std
        _y = (_y - self._x_mean) / self._x_std

        return _x, _y

    def inverse_transform(self, y):
        if self.pred_win == 1:
            y = y.reshape(-1, 1)
        else:
            y = y.reshape(-1, self.pred_win)
        return super(DifferenceNormalizedFlatten, self).inverse_transform(
            (y * self._x_std) + self._x_mean
        )


class LocalizedFlatten(TimeTensorTransformer, TargetTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.
    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
    ):

        super(LocalizedFlatten, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
        )

    def _check_meta_data(self, data_shape):
        """Override parent method

        Args:
            data_shape ([type]): [description]

        Raises:
            Exception: [description]

        Returns:
            [type]: [description]
        """
        super()._check_meta_data(data_shape)

        def _check_col_index():
            for i in range(len(self.feature_columns)):
                if self.feature_columns[i] != self.target_columns[i]:
                    return True
            return False

        if (
            len(self.feature_columns) != len(self.target_columns)
            or set(self.feature_columns) != set(self.target_columns)
            or _check_col_index()
        ):
            raise Exception("Value of feature_columns and target_columns must match")

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        _x, _y = super(LocalizedFlatten, self).transform(X)

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [
            list(_x[i][:, j].flatten())
            for i in range(len(_x))
            for j in range(len(self.feature_columns))
        ]
        _x = np.array(_x)

        if self.pred_win == 1:
            _y = np.array(_y.ravel()).reshape(-1, 1)
        else:
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
            else:
                _y = [
                    list(_y[i][:, j].flatten())
                    for i in range(len(_y))
                    for j in range(len(self.target_columns))
                ]
                _y = np.array(_y)

        return _x, _y

    def inverse_transform(self, y):
        # make sure we have correct shape of y
        if self.pred_win == 1:
            y = y.reshape(-1, 1)
        else:
            y = y.reshape(-1, self.pred_win)
        return y


class TensorAggregateTransformer(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.
    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        flatten_type="summary_statistics",
    ):
        super(TensorAggregateTransformer, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )
        self.flatten_type = flatten_type

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        _x, _y = super(TensorAggregateTransformer, self).transform(X)

        # @TODO: Need to converge this aggregation with rolling_window_feature_extraction

        # finding the aggregate of each tensor using different window agg methods
        # like summary statistics
        _x = [pd.DataFrame(np.array(_x[i])) for i in range(len(_x))]
        if self.flatten_type == "summary_statistics":
            _x = [
                _x[i].agg(["mean", "median", "prod", "sum", "std", "var"]).dropna()
                for i in range(len(_x))
            ]
        _x = [_x[i].values for i in range(len(_x))]

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        _y = np.array(_y.ravel())

        return _x, _y


class TensorFlattenTransformer(TimeTensorTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.
    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self, feature_columns=[0], target_columns=[0], lookback_win=1, pred_win=1
    ):
        super(TensorFlattenTransformer, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
        )

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        _x, _y = super(TensorFlattenTransformer, self).transform(X)

        # Regular flattening of 3D data to 2D data for consumption of IID models
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        _y = np.array(_y.ravel())

        return _x, _y


class DivisionFlatten(TimeTensorTransformer, TargetTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
    ):

        super(DivisionFlatten, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
        )

    def _check_meta_data(self, data_shape):
        """Override parent method

        Args:
            data_shape ([type]): [description]

        Raises:
            Exception: [description]

        Returns:
            [type]: [description]
        """
        super()._check_meta_data(data_shape)

        def _check_col_index():
            for i in range(len(self.feature_columns)):
                if self.feature_columns[i] != self.target_columns[i]:
                    return True
            return False

        if (
            len(self.feature_columns) != len(self.target_columns)
            or set(self.feature_columns) != set(self.target_columns)
            or _check_col_index()
        ):
            raise Exception("Value of feature_columns and target_columns must match")

    def transform(self, X, y=None):
        # calling the function to first create time tensors

        _x, _y = super(DivisionFlatten, self).transform(X)

        # Regular flattening of 3D data to 2D data for consumption of IID models

        self._x_last = np.array(
            [
                list(_x[i][:, j])[-1]
                for i in range(len(_x))
                for j in range(len(self.feature_columns))
            ]
        ).reshape(-1, 1)

        # Dividing consequtive elements

        _x = [
            list(_x[i][:, j])
            for i in range(len(_x))
            for j in range(len(self.feature_columns))
        ]

        _x = np.array(_x)

        if self.pred_win == 1:
            _y = np.array(_y.ravel()).reshape(-1, 1)

            _y = _y / self._x_last

        else:
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)

                _y = _y / self._x_last

            else:
                _y = [
                    list(_y[i][:, j].flatten())
                    for i in range(len(_y))
                    for j in range(len(self.target_columns))
                ]

                _y = np.array(_y)
                _y = _y / self._x_last

        return _x, _y

    def inverse_transform(self, y):
        if self.pred_win == 1:
            y = y.reshape(-1, 1)
        else:
            y = y.reshape(-1, self.pred_win)
        return y * self._x_last


class DivisionFlattenX(TimeTensorTransformer, TargetTransformer):
    """
    Prepare the data to be consumed by the model either for training or testing.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
        where n_samples is the number of samples and n_features is the number of features.
        num_look_back (int, optional): Look-back window for the model.
        n_steps_ahead (int): Look-ahead window for the model.
    Returns:
        _x (list of list): Each index in the list has a list of lookback window elements.
        _y (list of list): Each index in the list has a list of look ahead window elements.
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
    ):

        super(DivisionFlattenX, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
        )

    def transform(self, X, y=None):
        # calling the function to first create time tensors

        _x, _y = super(DivisionFlattenX, self).transform(X)

        # Regular flattening of 3D data to 2D data for consumption of IID models

        self._x_last = np.array(
            [
                list(_x[i][:, j])[-1]
                for i in range(len(_x))
                for j in range(len(self.feature_columns))
            ]
        ).reshape(-1, 1)

        # Dividing consequtive elements

        def np_divide(x):
            """Finds division of consequitive elements in an array"""
            return x[1:] / x[:-1]

        _x = [
            list(np_divide(_x[i][:, j]))
            for i in range(len(_x))
            for j in range(len(self.feature_columns))
        ]

        _x = np.array(_x)

        if self.pred_win == 1:
            _y = np.array(_y.ravel()).reshape(-1, 1)

            _y = _y / self._x_last

        else:
            if len(self.target_columns) == 1:
                _y = _y.reshape(-1, self.pred_win)
                _y = _y / self._x_last

            else:
                _y = [
                    list(_y[i][:, j].flatten())
                    for i in range(len(_y))
                    for j in range(len(self.target_columns))
                ]
                _y = np.array(_y)
                _y = _y / self._x_last
        return _x, _y

    def inverse_transform(self, y):
        if self.pred_win == 1:
            y = y.reshape(-1, 1)
        else:
            y = y.reshape(-1, self.pred_win)
        return y * self._x_last


class LocalizedFlattenX(TimeTensorTransformer, TargetTransformer):
    """ """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
    ):
        super(LocalizedFlattenX, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
        )

    def _pre_fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Raises:
            Exception: [description]
        """
        # define two internal trasformer
        self.diff_lookback_win_ = self.flatten_lookback_win_ = self.lookback_win
        self.flatten_features_ = []
        if len(self.feature_columns) > len(self.target_columns):
            for item_index, item in enumerate(self.feature_columns):
                if item not in self.target_columns:
                    self.flatten_features_.append(item)
        else:
            raise Exception("feature columns should be larger")

        if isinstance(self.lookback_win, list):
            self.diff_lookback_win_ = []
            self.flatten_lookback_win_ = []
            for item_index, item in enumerate(self.feature_columns):
                if item in self.target_columns:
                    self.diff_lookback_win_.append(self.lookback_win[item_index])
                else:
                    self.flatten_lookback_win_.append(self.lookback_win[item_index])

        # adjust the skip record if max_lookback of the group is higher than the individual records
        skip_observation_for_tmp_difference_flatten_ = get_max_lookback(
            self.lookback_win
        ) - get_max_lookback(self.diff_lookback_win_)

        self.tmp_localized_flatten_ = LocalizedFlatten(
            feature_columns=self.target_columns,
            target_columns=self.target_columns,
            pred_win=self.pred_win,
            lookback_win=self.diff_lookback_win_,
            skip_observation=skip_observation_for_tmp_difference_flatten_,
        )

        skip_observation_for_flatten_ = get_max_lookback(
            self.lookback_win
        ) - get_max_lookback(self.flatten_lookback_win_)

        self.tmp_flatten_ = Flatten(
            feature_columns=self.flatten_features_,
            target_columns=self.target_columns,
            pred_win=self.pred_win,
            lookback_win=self.flatten_lookback_win_,
            skip_observation=skip_observation_for_flatten_,
        )

    def _check_window_params(self):
        if isinstance(self.lookback_win, list):
            if len(self.feature_columns) != len(self.lookback_win):
                raise Exception(
                    "1 or more feature columns should have mapping lookback window"
                )

    def _check_meta_data(self):
        if self.feature_columns is None:
            raise Exception(
                "`feature_columns` is set to `None`. Set the value for `feature_columns`"
            )
        if self.target_columns is None:
            raise Exception(
                "`target_columns` is set to `None`. Set the value for `target_columns`"
            )
        if not set(self.target_columns).issubset(set(self.feature_columns)):
            raise Exception(
                "1 or more `target_columns` are not present in `feature_columns`"
            )

    def fit(self, X, y=None):
        self._check_meta_data()
        self._check_window_params()
        self._pre_fit(X, y)
        self.tmp_localized_flatten_.fit(X, y)
        self.tmp_flatten_.fit(X, y)
        return self

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        check_is_fitted(self, "tmp_localized_flatten_")
        check_is_fitted(self, "tmp_flatten_")
        _d_x, _d_y = self.tmp_localized_flatten_.transform(X, y)
        _f_x, _ = self.tmp_flatten_.transform(X, y)
        _f_x = np.repeat(_f_x, repeats=len(self.target_columns), axis=0)
        _x = np.concatenate(
            (_d_x, _f_x),
            axis=1,
        )
        return _x, _d_y

    def inverse_transform(self, y):
        check_is_fitted(self, "tmp_localized_flatten_")
        return self.tmp_localized_flatten_.inverse_transform(y)


class NormalizedFlattenX(TimeTensorTransformer, TargetTransformer):
    """ """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
        skip_observation=0,
    ):
        super(NormalizedFlattenX, self).__init__(
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
        )

    def _pre_fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Raises:
            Exception: [description]
        """
        # define two internal trasformer
        self.diff_lookback_win_ = self.flatten_lookback_win_ = self.lookback_win
        self.flatten_features_ = []
        if len(self.feature_columns) > len(self.target_columns):
            for item_index, item in enumerate(self.feature_columns):
                if item not in self.target_columns:
                    self.flatten_features_.append(item)
        else:
            raise Exception("feature columns should be larger")

        if isinstance(self.lookback_win, list):
            self.diff_lookback_win_ = []
            self.flatten_lookback_win_ = []
            for item_index, item in enumerate(self.feature_columns):
                if item in self.target_columns:
                    self.diff_lookback_win_.append(self.lookback_win[item_index])
                else:
                    self.flatten_lookback_win_.append(self.lookback_win[item_index])

        # adjust the skip record if max_lookback of the group is higher than the individual records
        skip_observation_for_tmp_difference_flatten_ = get_max_lookback(
            self.lookback_win
        ) - get_max_lookback(self.diff_lookback_win_)

        self.tmp_localized_flatten_ = NormalizedFlatten(
            feature_columns=self.target_columns,
            target_columns=self.target_columns,
            pred_win=self.pred_win,
            lookback_win=self.diff_lookback_win_,
            skip_observation=skip_observation_for_tmp_difference_flatten_,
        )

        skip_observation_for_flatten_ = get_max_lookback(
            self.lookback_win
        ) - get_max_lookback(self.flatten_lookback_win_)

        self.tmp_flatten_ = Flatten(
            feature_columns=self.flatten_features_,
            target_columns=self.target_columns,
            pred_win=self.pred_win,
            lookback_win=self.flatten_lookback_win_,
            skip_observation=skip_observation_for_flatten_,
        )

    def _check_meta_data(self):
        if self.feature_columns is None:
            raise Exception(
                "`feature_columns` is set to `None`. Set the value for `feature_columns`"
            )
        if self.target_columns is None:
            raise Exception(
                "`target_columns` is set to `None`. Set the value for `target_columns`"
            )
        if not set(self.target_columns).issubset(set(self.feature_columns)):
            raise Exception(
                "1 or more `target_columns` are not present in `feature_columns`"
            )

    def _check_window_params(self):
        if isinstance(self.lookback_win, list):
            if len(self.feature_columns) != len(self.lookback_win):
                raise Exception(
                    "1 or more feature columns should have mapping lookback window"
                )

    def fit(self, X, y=None):
        self._check_meta_data()
        self._check_window_params()
        self._pre_fit(X, y)
        self.tmp_localized_flatten_.fit(X, y)
        self.tmp_flatten_.fit(X, y)
        return self

    def transform(self, X, y=None):
        # calling the function to first create time tensors
        check_is_fitted(self, "tmp_localized_flatten_")
        check_is_fitted(self, "tmp_flatten_")
        _d_x, _d_y = self.tmp_localized_flatten_.transform(X, y)
        _f_x, _ = self.tmp_flatten_.transform(X, y)
        _f_x = np.repeat(_f_x, repeats=len(self.target_columns), axis=0)
        _x = np.concatenate(
            (_d_x, _f_x),
            axis=1,
        )
        return _x, _d_y

    def inverse_transform(self, y):
        check_is_fitted(self, "tmp_localized_flatten_")
        return self.tmp_localized_flatten_.inverse_transform(y)
