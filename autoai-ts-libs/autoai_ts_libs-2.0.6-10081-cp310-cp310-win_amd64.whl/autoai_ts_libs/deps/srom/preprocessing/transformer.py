"""
.. module:: ts_transformer
   :synopsis: Contains TimeTensorTransformer class.

.. moduleauthor:: SROM Team
"""

import copy
import operator
import warnings
from abc import abstractmethod
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceTransformer
from sklearn.utils.validation import check_array
from sklearn.utils.validation import check_is_fitted
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import logging

LOGGER = logging.getLogger(__name__)

try:
    from statsmodels.tsa.stattools import adfuller, kpss
    from statsmodels.tsa.statespace.tools import diff
    from statsmodels.stats.multitest import multipletests
except ImportError:
    LOGGER.error("ImportError in function.py : statsmodels is not installed ")
    pass


def _get_log_transform(x):
    """[summary]

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    if x >= 0:
        return np.log(1 + x)
    else:
        return -np.log(-x + 1)


def _get_inv_log_transform(x):
    """[summary]

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    if x >= 0:
        x = min(x, np.log(np.finfo(type(1.0)).max))
        return np.exp(x) - 1
    else:
        x = max(x, np.log(np.finfo(type(1.0)).min))
        return 1 - np.exp(-x)


def _mean_transform(x, operation, mean_clm):
    """"""
    if operation == "division":
        mean_clm[mean_clm == 0] = 1.0
        x = x / mean_clm
    elif operation == "substraction":
        x = x - mean_clm
    else:
        raise ValueError(
            "The `operation` value specified is incorrect. It should be 'division' or 'subtraction'.`"
        )
    return x


def _min_max_scaling(x, max_clm, scale_factor):
    """"""
    x = (max_clm - x) / scale_factor
    return x


def _inv_min_max_scaling(x, max_clm, scale_factor, clm_index):
    """[summary]

    Args:
        x ([type]): [description]
        max_clm ([type]): [description]
        scale_factor ([type]): [description]
        clm_index ([type]): [description]

    Returns:
        [type]: [description]
    """
    tmp_max = max_clm[clm_index]
    tmp_scale = scale_factor[clm_index]
    tmp_max = np.array(tmp_max)
    tmp_scale = np.array(tmp_scale)
    if x.ndim == 1:
        x = x.reshape(1, -1)
    tmp_max = np.tile(tmp_max, (x.shape[0], int(x.shape[1] / len(clm_index))))
    tmp_scale = np.tile(tmp_scale, (x.shape[0], int(x.shape[1] / len(clm_index))))
    x = -np.subtract(np.multiply(x, tmp_scale), tmp_max)
    # x = -((x * scale_factor) - max_clm) This also works.
    return x


def _inv_std_scaling(x, scale, mean, clm_index):
    """[summary]

    Args:
        x ([type]): [description]
        scale ([type]): [description]
        mean ([type]): [description]
        clm_index ([type]): [description]

    Returns:
        [type]: [description]
    """
    tmp_mean = mean[clm_index]
    tmp_scale = scale[clm_index]
    tmp_max = np.array(tmp_mean)
    tmp_scale = np.array(tmp_scale)
    if x.ndim == 1:
        x = x.reshape(1, -1)
    tmp_mean = np.tile(tmp_mean, (x.shape[0], len(clm_index)))
    tmp_scale = np.tile(tmp_scale, (x.shape[0], len(clm_index)))
    x[:,clm_index] = np.add(np.multiply(x[:,clm_index], tmp_scale), tmp_mean)
    # x = -((x * scale_factor) - max_clm) This also works.
    return x


def _inv_mean_transform(x, mean_clm, clm_index, operation):
    """[summary]

    Args:
        x ([type]): [description]
        mean_clm ([type]): [description]
        clm_index ([type]): [description]
        operation ([type]): [description]

    Raises:
        ValueError: [description]

    Returns:
        [type]: [description]
    """
    if operation == "division":
        op_func = operator.mul
    elif operation == "substraction":
        op_func = operator.add
    else:
        raise ValueError(
            "The `operation` value specified is incorrect. It should be 'division' or 'subtraction'.`"
        )

    if len(clm_index) > 1:
        original_shape = x.shape
        x = x.reshape(-1, len(clm_index))
        x = op_func(x, mean_clm[clm_index])
        return x.reshape(original_shape)
    else:
        return op_func(x, mean_clm[clm_index])


class DualTransformer(BaseEstimator, TransformerMixin):
    """
    Base transformer class in which the number of rows is \
    preserved during transformation.
    """

    def fit(self, X, y=None):
        """"""
        return self

    @abstractmethod
    def transform(self, X):
        pass

    @abstractmethod
    def inverse_transform(self, X):
        pass


class Log(DualTransformer):
    """Transformer class to find logarithm of data"""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        vec_log_fun = np.vectorize(_get_log_transform)
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = vec_log_fun(X[:, clm_index])
        return X

    def inverse_transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        inv_vec_log_fun = np.vectorize(_get_inv_log_transform)
        return inv_vec_log_fun(X)


class Sqrt(DualTransformer):
    """Transformer to perform Square tranform of the data."""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        sqrt_fun = lambda d: np.sqrt(d)
        vec_sqrt_fun = np.vectorize(sqrt_fun)
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = vec_sqrt_fun(X[:, clm_index])
        return X

    def inverse_transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        sqr_fun = lambda d: np.square(d)
        vec_sqr_fun = np.vectorize(sqr_fun)
        return vec_sqr_fun(X)


class Reciprocal(DualTransformer):
    """Transformer to perform Reciprocal transform of the data."""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        reci_fun = lambda d: np.reciprocal(d + 1)
        vec_reci_fun = np.vectorize(reci_fun)
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = vec_reci_fun(X[:, clm_index])
        return X

    def inverse_transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        reci_fun = lambda d: np.reciprocal(d) - 1
        vec_reci_fun = np.vectorize(reci_fun)
        return vec_reci_fun(X)


class MeanDivision(DualTransformer):
    """Transformer to perform division by mean of data."""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        self.clm_index_ = list(set(self.feature_columns + self.target_columns))
        tmp_mean_clm = np.mean(X[:, self.clm_index_], axis=0)
        self.mean_clm_ = np.ones(X.shape[1])
        self.mean_clm_[self.clm_index_] = tmp_mean_clm
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "mean_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        X[:, self.clm_index_] = _mean_transform(
            x=X[:, self.clm_index_],
            operation="division",
            mean_clm=self.mean_clm_[self.clm_index_],
        )
        return X

    def inverse_transform(self, X):
        """
        NOTE:
        - need to learn  target_len=1 or remove
        """
        check_is_fitted(self, "mean_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        return _inv_mean_transform(X, self.mean_clm_, self.target_columns, "division")


class MeanSubtraction(DualTransformer):
    """Transformer to perform subtraction by mean transform of the data."""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        self.clm_index_ = list(set(self.feature_columns + self.target_columns))
        tmp_mean_clm = np.mean(X[:, self.clm_index_], axis=0)
        self.mean_clm_ = np.zeros(X.shape[1])
        self.mean_clm_[self.clm_index_] = tmp_mean_clm
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "mean_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        X[:, self.clm_index_] = _mean_transform(
            X[:, self.clm_index_], "substraction", self.mean_clm_[self.clm_index_]
        )
        return X

    def inverse_transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "mean_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        return _inv_mean_transform(
            X, self.mean_clm_, self.target_columns, "substraction"
        )


class MeanDivisionLog(DualTransformer):
    """Transformer to perform Reciprocal transform of the data."""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        self.clm_index_ = list(set(self.feature_columns + self.target_columns))
        tmp_mean_clm = np.mean(X[:, self.clm_index_], axis=0)
        self.mean_clm_ = np.ones(X.shape[1])
        self.mean_clm_[self.clm_index_] = tmp_mean_clm
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "mean_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        X[:, self.clm_index_] = _mean_transform(
            X[:, self.clm_index_], "division", self.mean_clm_[self.clm_index_]
        )
        vec_log_fun = np.vectorize(_get_log_transform)
        X[:, self.clm_index_] = vec_log_fun(X[:, self.clm_index_])
        return X

    def inverse_transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "mean_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        inv_vec_log_fun = np.vectorize(_get_inv_log_transform)
        X = inv_vec_log_fun(X)
        return _inv_mean_transform(X, self.mean_clm_, self.target_columns, "division")


class MeanSubtractionLog(DualTransformer):
    """[summary]

    Args:
        DualTransformer ([type]): [description]
    """

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        self.clm_index_ = list(set(self.feature_columns + self.target_columns))
        tmp_mean_clm = np.mean(X[:, self.clm_index_], axis=0)
        self.mean_clm_ = np.zeros(X.shape[1])
        self.mean_clm_[self.clm_index_] = tmp_mean_clm
        return self

    def transform(self, X):
        """"""
        check_is_fitted(self, "mean_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        X[:, self.clm_index_] = _mean_transform(
            X[:, self.clm_index_], "substraction", self.mean_clm_[self.clm_index_]
        )
        vec_log_fun = np.vectorize(_get_log_transform)
        X[:, self.clm_index_] = vec_log_fun(X[:, self.clm_index_])
        return X

    def inverse_transform(self, X):
        """"""
        check_is_fitted(self, "mean_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        inv_vec_log_fun = np.vectorize(_get_inv_log_transform)
        X = inv_vec_log_fun(X)
        return _inv_mean_transform(
            X, self.mean_clm_, self.target_columns, "substraction"
        )


class Anscombe(DualTransformer):
    """"""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        anscombe_fun = lambda d: 2 * np.sqrt(d + 3.0 / 8.0)
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        vec_anscombe_fun = np.vectorize(anscombe_fun)
        X[:, clm_index] = vec_anscombe_fun(X[:, clm_index])
        return X

    def inverse_transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        return np.square(X) / 4.0 - (3.0 / 8.0)


class Fisher(DualTransformer):
    """[summary]

    Args:
        DualTransformer ([type]): [description]
    """

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        fisher_fun = lambda d: np.arctanh(np.clip(d, -1 + 1.0e-8, 1.0 - 1.0e-8))
        vec_fisher_fun = np.vectorize(fisher_fun)
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = vec_fisher_fun(X[:, clm_index])
        return X

    def inverse_transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        return np.tanh(X)


class TSMinMaxScaler(DualTransformer):
    """Transformer to perform division by mean of data."""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        self.clm_index_ = list(set(self.feature_columns + self.target_columns))
        self.min_clm_ = np.ones(X.shape[1])
        self.max_clm_ = np.ones(X.shape[1])
        self.min_clm_[self.clm_index_] = np.min(X[:, self.clm_index_], axis=0)
        self.max_clm_[self.clm_index_] = np.max(X[:, self.clm_index_], axis=0)
        self.scale_factor_ = self.max_clm_ - self.min_clm_
        self.scale_factor_[self.scale_factor_ == 0] = 1.0
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "scale_factor_")
        check_is_fitted(self, "max_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        X[:, self.clm_index_] = _min_max_scaling(
            x=X[:, self.clm_index_],
            max_clm=self.max_clm_[self.clm_index_],
            scale_factor=self.scale_factor_[self.clm_index_],
        )
        return X

    def inverse_transform(self, X):
        """
        NOTE:
        - need to learn  target_len=1 or remove
        """
        check_is_fitted(self, "scale_factor_")
        check_is_fitted(self, "max_clm_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        X = _inv_min_max_scaling(
            x=X,
            max_clm=self.max_clm_,
            scale_factor=self.scale_factor_,
            clm_index=self.target_columns,
        )
        return X


class TSStandardScaler(DualTransformer):
    """Transformer to perform division by mean of data."""

    def __init__(self, feature_columns=[0], target_columns=[0]):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            target_columns (list, optional): [description]. Defaults to [0].
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        self.clm_index_ = list(set(self.feature_columns + self.target_columns))
        self.scaler_ = StandardScaler().fit(X[:, self.clm_index_])
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "scaler_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        X[:, self.clm_index_] = self.scaler_.transform(
            X=X[:, self.clm_index_],
        )
        return X

    def inverse_transform(self, X):
        """
        NOTE:
        - need to learn  target_len=1 or remove
        """
        check_is_fitted(self, "scaler_")
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        return self.scaler_.inverse_transform(X)
        # todo - the following code assume we have target columns and feature columns are same
        '''
        for i in range(X.shape[0]):
            if i in self.target_columns:
        return _inv_std_scaling(X, self.scaler_.scale_,self.scaler_.mean_,self.target_columns)
        '''

class XYScaler(DualTransformer):
    """Base scaler to scale both X and Y."""

    def __init__(self, base_scaler):
        """Base scaler to scale both X and Y.

        Args:
            base_scaler (TransformerMixin): Scaler function from scikit-learn or extending sklearn.base.TransformerMixin
        """
        self.base_scaler = base_scaler

    def fit(self, X, y):
        """Fit transformer.

        Args:
            X (numpy array): Input data
            y (numpy array): target data
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        self.X_scaler_ = copy.deepcopy(self.base_scaler)
        self.y_scaler_ = copy.deepcopy(self.base_scaler)
        self.X_scaler_.fit(X)
        self.y_scaler_.fit(y)
        return self

    def transform(self, X, y=None):
        """Transform

        Args:
            X (numpy array): Input data
            y (numpy array): target data

        Returns:
            result (tuple): (transformed input data, transformed target data)
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        X = self.X_scaler_.transform(X)
        if y is not None:
            return X, self.y_scaler_.transform(y)
        return X, y

    def fit_transform(self, X, y, **fit_params):
        """Fit and Transform X and Y.

        Args:
            X (numpy array): Input data
            y (numpy array): target data

        Returns:
            tuple: (transformed input data, transformed target data)
        """
        return self.fit(X, y, **fit_params).transform(X, y)

    def inverse_transform(self, X):
        """[summary]

        Args:
            X (numpy array): target data (in transformed form)

        Returns:
            X (numpy array): target data
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        return self.y_scaler_.inverse_transform(X)


class MinMaxXYScaler(XYScaler):
    """XY Scaler to scale both X and Y using sklearn MinMaxScaler"""

    def __init__(self):
        super(MinMaxXYScaler, self).__init__(base_scaler=MinMaxScaler(),)


class StandardXYScaler(XYScaler):
    """XY Scaler to scale both X and Y using sklearn StandardScaler"""

    def __init__(self):
        super(StandardXYScaler, self).__init__(base_scaler=StandardScaler(),)


class DataStationarizer(StateSpaceTransformer):
    """[This Transformer Look at the Data and Do some Transformation]

    Args:
        DualTransformer ([type]): [description]
    """

    def __init__(
        self, feature_columns=[0], target_columns=[0], skip_record=0, alpha=0.05
    ):
        """[summary]

        Args:
            feature_columns (int, optional): [description]. Defaults to 0.
            target_columns (int, optional): [description]. Defaults to 0.
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.skip_record = skip_record
        self.alpha = alpha

    def _conclude_adf_and_kpss_results(self, adf_reject, kpss_reject):
        """[summary]

        Args:
            adf_reject ([type]): [description]
            kpss_reject ([type]): [description]

        Returns:
            [type]: [description]
        """
        if adf_reject and kpss_reject:
            return ["Differentiate"]
        if adf_reject and (not kpss_reject):
            return ["Detrend"]
        if (not adf_reject) and kpss_reject:
            return ["Differentiate"]
        # if we're here, both H0 cannot be rejected
        return ["Detrend", "Differentiate"]

    def fit(self, X, y=None):
        """It will learn now what shd be done

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.
        """
        check_array(
            X[list(set(self.feature_columns + self.target_columns))],
            accept_sparse=True,
            dtype=None,
            ensure_2d=False,
        )

        self.trainX_ = X.copy()
        X = X.copy()

        adf_results = []
        clm_index = []
        kpss_results = []

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            for item in set(self.feature_columns + self.target_columns):
                clm_item = X[:, item]
                adf_result = adfuller(clm_item, regression="ct")
                try:
                    kpss_result = kpss(clm_item, regression="ct")
                except ValueError:
                    kpss_result = (0,1, 0, {}) 
                adf_results.append(adf_result)
                kpss_results.append(kpss_result)
                clm_index.append(item)

        adf_pvals = [x[1] for x in adf_results]
        kpss_pvals = [x[1] for x in kpss_results]
        pvals = adf_pvals + kpss_pvals
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            by_res = multipletests(
                pvals=pvals, alpha=self.alpha, method="fdr_by", is_sorted=False
            )
        reject = by_res[0]
        adf_rejections = reject[: len(clm_index)]
        kpss_rejections = reject[len(clm_index) :]

        self.clm_decisions_ = []
        self.clm_index_ = []
        for item_index, item in enumerate(clm_index):
            self.clm_decisions_.append(
                self._conclude_adf_and_kpss_results(
                    adf_reject=adf_rejections[item_index],
                    kpss_reject=kpss_rejections[item_index],
                )
            )
            self.clm_index_.append(item)
        return self

    def _transform(self, X, y=None):
        X = X.copy()
        cols_value = {}

        for item_index, item in enumerate(self.clm_index_):

            clm_decisions = self.clm_decisions_[item_index]
            clm_item = X[:, item].copy()

            if "Detrend" in clm_decisions:

                if self.skip_record >= len(clm_item):
                    raise Exception(
                        "The Number of record to skip should be smaller than the length of time series data"
                    )

                trends = np.vander(
                    np.arange(float(len(clm_item) - self.skip_record)), N=2
                )
                beta = np.linalg.pinv(trends).dot(clm_item)

                if self.skip_record > 0:
                    trends = np.vander(np.arange(float(len(clm_item))), N=2)

                # self.cols_trend_beta[item] = beta
                clm_item = clm_item - np.dot(trends, beta)

            if "Differentiate" in clm_decisions:
                clm_item = diff(clm_item, k_diff=1)

            cols_value[item] = clm_item

        min_len = min([len(cols_value[x]) for x in cols_value])
        X = X[X.shape[0] - min_len :, :]
        for item in self.clm_index_:
            new_col = cols_value[item][:min_len]
            X[:, item] = new_col

        return X

    def fit_transform(self, X, y, **fit_params):
        self.fit(X, y)
        return self._transform(X)

    def transform(self, X, is_lookback_appended=False, lookback_win=0):
        """[summary]

        Args:
            X ([type]): [description]
            append_lookback_history (bool, optional): [description]. Defaults to False.
            lookback_win (int, optional): [description]. Defaults to 0.

        Raises:
            ValueError: [description]

        Returns:
            [type]: [description]
        """
        check_array(
            X[list(set(self.feature_columns + self.target_columns))],
            accept_sparse=True,
            dtype=None,
            ensure_2d=False,
        )

        new_X = None
        if is_lookback_appended:
            if lookback_win > 0:
                new_X = np.concatenate([self.trainX_, X[lookback_win:, :]])
            else:
                raise ValueError("value of lookback_win > 0")
        else:
            new_X = np.concatenate([self.trainX_, X])

        return self._transform(new_X)[
            -X.shape[0] :,
        ]


class TargetColumnsSelector(BaseEstimator):
    """[This Transformer Look at the Data and Do some Transformation]

    Args:
        DualTransformer ([type]): [description]
    """

    def __init__(self, target_columns=[0]):
        """[summary]

        Args:
            feature_columns (int, optional): [description]. Defaults to 0.
            target_columns (int, optional): [description]. Defaults to 0.
        """
        self.target_columns = target_columns

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        return X[:, self.target_columns]

class SoftPlus(DualTransformer):
    """Transformer to SoftPlus transaformation of the target."""

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        return self

    def transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        check_array(X, accept_sparse=True, dtype=None, ensure_2d=False)
        softplus_fun = lambda d: np.log(np.exp(d) - 1)
        vec_softplus_fun = np.vectorize(softplus_fun)
        clm_index = list(range(X.shape[1]))
        X = X.copy()
        X[:, clm_index] = vec_softplus_fun(X[:, clm_index])
        return X

    def inverse_transform(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        softplus_fun = lambda d: np.log(np.exp(d) + 1)
        vec_softplus_fun = np.vectorize(softplus_fun)
        clm_index = list(range(X.shape[1]))
        X = X.copy()
        X[:, clm_index] = vec_softplus_fun(X[:, clm_index])
        return X
