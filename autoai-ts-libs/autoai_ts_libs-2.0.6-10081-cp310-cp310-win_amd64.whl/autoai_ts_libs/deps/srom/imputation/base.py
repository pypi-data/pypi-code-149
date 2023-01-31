# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: base
   :synopsis: base.

.. moduleauthor:: SROM Team
"""

from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from sklearn.utils.validation import check_array
from autoai_ts_libs.deps.srom.imputation.utils import _fit_decomposition, _transform_decomposition
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA


class TSImputer(BaseEstimator, TransformerMixin):
    """
    Base class for time series based imputer.
    """

    def __init__(self, time_column=-1, missing_values=np.nan, enable_fillna=True):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill the backword and forward.
        """
        self.time_column = time_column
        self.missing_values = missing_values
        self.enable_fillna = enable_fillna

    def _check_param_values(self):
        """
        Internal method work as a helper method
        """
        if hasattr(self, "time_column"):
            if self.time_column:
                if self.time_column < -1:
                    raise (ValueError)

    def fit(self, X, y=None, **fit_params):
        """
        Fit the imputer
        Parameters:
            X(array like): input.
        """
        if "skip_fit" in fit_params.keys() and fit_params["skip_fit"]:
            return self

        self._check_param_values()
        return self

    def transform(self, X):
        """
        Transform the imputer
        Parameters:
            X(array like): input.
        """
        return X


class DecompositionImputer(BaseEstimator, TransformerMixin):
    """
    Base class for deecomposition based imputer.
    """

    def __init__(
        self,
        time_column=-1,
        missing_values=np.nan,
        enable_fillna=True,
        order=-1,
        base_imputer=SimpleImputer(),
        scaler=None,
        decomposer=PCA(),
        max_iter=None,
        tol=None,
    ):
        """
        Parameters:
            time_column(int): time column.
            missing_values (obj): missing value to be imputed.
            enable_fillna(boolean): fill the backword and forward.
            order(int): lookback in case of time series imputer.
            base_imputer(obj): object of sklearn Imputer or srom. 
            scaler(obj): data scaler object necessary for decomposition.
            decomposer(obj): object of sklearn.decomposition.
            max_iter(int): Number of iteration to run the decomposition.
            tol(float): the tolerance of the imputed value on each iteration.
        """
        self.time_column = time_column
        self.missing_values = missing_values
        self.enable_fillna = enable_fillna
        self.order = order
        self.base_imputer = base_imputer
        self.scaler = scaler
        self.decomposer = decomposer
        self.max_iter = max_iter
        self.tol = tol

    def _check_param_values(self):
        """
        Internal method work as a helper method
        """
        if hasattr(self, "time_column"):
            if self.time_column < -1:
                raise (ValueError)
            elif self.time_column >= 0:
                raise Exception("the given time_column is not supported")

    def fit(self, X, y=None, **fit_params):
        """
        Fit the imputer
        Parameters:
            X(array like): input.
        """
        if "skip_fit" in fit_params.keys() and fit_params["skip_fit"]:
            return self

        self._check_param_values()
        X = check_array(X, dtype=np.float64, force_all_finite=False)
        if not np.isnan(self.missing_values):
            X[X == self.missing_values] = np.NaN

        if isinstance(self.base_imputer, TSImputer):
            X_nan = np.isnan(self.base_imputer.get_X(X, order=self.order))
            imputed = self.base_imputer.fit_transform(X)
            imputed = self.base_imputer.get_X(imputed, order=self.order)
        else:
            X_nan = np.isnan(X)
            imputed = self.base_imputer.fit_transform(X)

        if self.scaler:
            imputed = self.scaler.fit_transform(imputed)
            new_imputed = imputed.copy()
        else:
            new_imputed = imputed.copy()

        self.decomposer = _fit_decomposition(
            self.decomposer, imputed, new_imputed, X_nan, self.max_iter, self.tol
        )

        return self

    def transform(self, X):
        """
        Transform the imputer
        Parameters:
            X(array like): input.
        """
        X = check_array(X, dtype=np.float64, force_all_finite=False)
        if not np.isnan(self.missing_values):
            X[X == self.missing_values] = np.NaN

        if isinstance(self.base_imputer, TSImputer):
            if len(X) < self.order:
                if np.count_nonzero(np.isnan(X)) > 0:
                    raise Exception("imputation transformation is not supported")
                else:
                    return X
            X_nan = np.isnan(self.base_imputer.get_X(X, order=self.order))
            imputed = self.base_imputer.fit_transform(X)
            X = self.base_imputer.get_X(imputed, order=self.order)
        else:
            X_nan = np.isnan(X)
            X = self.base_imputer.transform(X)

        X = _transform_decomposition(self.decomposer, self.scaler, X, X_nan)
        if isinstance(self.base_imputer, TSImputer):
            X = self.base_imputer.get_TS(X, order=self.order)
        return X

    def set_params(self, **kwarg):
        """
        Set params.
        Parameters:
            kwarg(dict): keyword arguments.
        """
        super(DecompositionImputer, self).set_params(**kwarg)
        decomposer_param = {}

        for item in self.decomposer.get_params().keys():
            if item in kwarg.keys():
                decomposer_param[item] = kwarg[item]
        if len(decomposer_param) > 0:
            self.decomposer.set_params(**decomposer_param)


class FlattenImputer(BaseEstimator, TransformerMixin):
    """
    Base class for imputer based on flatten transformer.
    """

    def __init__(
        self,
        time_column=-1,
        missing_values=np.nan,
        enable_fillna=True,
        order=-1,
        base_imputer=None,
        model_imputer=None,
    ):
        """
        Parameters:
            time_column (int): time column.
            missing_values (obj): missing value to be imputed.
            enable_fillna (boolean): fill the backword and forward.
            order (int): lookback in case of time series imputer.
            base_imputer (obj): object of sklearn Imputer or srom.
            model_imputer (obj): object of sklearn Imputer or srom. 
        """
        self.time_column = time_column
        self.missing_values = missing_values
        self.enable_fillna = enable_fillna
        self.order = order
        self.base_imputer = base_imputer
        self.model_imputer = model_imputer

    def fit(self, X, y=None, **fit_params):
        """
        Fit the imputer
        Parameters:
            X(array like): input.
        """
        if "skip_fit" in fit_params.keys() and fit_params["skip_fit"]:
            return self

        X = check_array(X, dtype=np.float64, force_all_finite=False)
        if not np.isnan(self.missing_values):
            X[X == self.missing_values] = np.NaN

        X = self.base_imputer.get_X(X, order=self.order)
        self.model_imputer.fit(X)
        return self

    def transform(self, X):
        """
        Transform the imputer
        Parameters:
            X(array like): input.
        """
        X = check_array(X, dtype=np.float64, force_all_finite=False)
        if not np.isnan(self.missing_values):
            X[X == self.missing_values] = np.NaN

        if len(X) < self.order:
            if np.count_nonzero(np.isnan(X)) > 0:
                raise Exception("imputation transformation is not supported")
            else:
                return X
        X = self.base_imputer.get_X(X, order=self.order)
        X = self.model_imputer.transform(X)
        X = self.base_imputer.get_TS(X, order=self.order)
        return X

    def set_params(self, **kwarg):
        """
        Set params.
        Parameters:
            kwarg(dic): keyword arguments.
        """

    def set_params(self, **kwarg):
        """
        Set params.
        Parameters:
            kwarg(dic): keyword arguments.
        """
        super(FlattenImputer, self).set_params(**kwarg)

        """
        # techically parent class shd help
        if "base_imputer" in kwarg:
            self.base_imputer = kwarg["base_imputer"]
        if "model_imputer" in kwarg:
            self.model_imputer = kwarg["model_imputer"]
        if "time_column" in kwarg:
            self.time_column = kwarg["time_column"]
        if "missing_values" in kwarg:
            self.missing_values = kwarg["missing_values"]
        if "enable_fillna" in kwarg:
            self.enable_fillna = kwarg["enable_fillna"]
        if "order" in kwarg:
            self.order = kwarg["order"]
        """

        model_param = {}
        for d_item in kwarg:
            if "base_imputer__" in d_item:
                model_param[d_item.split("base_imputer__")[1]] = kwarg[d_item]
        if len(model_param) > 0:
            self.base_imputer.set_params(**model_param)

        model_param = {}
        for d_item in kwarg:
            if "model_imputer__" in d_item:
                model_param[d_item.split("model_imputer__")[1]] = kwarg[d_item]
        if len(model_param) > 0:
            self.model_imputer.set_params(**model_param)
        return self

    def get_params(self, deep=False):
        """
        Get params.
        Parameters:
            deep(boolean): flag to get nested parameters.
        
        """
        model_param = super(FlattenImputer, self).get_params(deep=deep)

        if deep:
            for item in self.base_imputer.get_params().keys():
                model_param["base_imputer__" + item] = self.base_imputer.get_params()[
                    item
                ]
            for item in self.model_imputer.get_params().keys():
                model_param["model_imputer__" + item] = self.model_imputer.get_params()[
                    item
                ]
        return model_param
