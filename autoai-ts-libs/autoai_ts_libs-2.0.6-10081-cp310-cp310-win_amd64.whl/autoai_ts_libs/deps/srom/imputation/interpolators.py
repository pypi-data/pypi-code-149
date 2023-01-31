# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2019 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.
"""
.. module:: imputation time series
   :synopsis: imputation time series.

.. moduleauthor:: SROM Team
"""

from autoai_ts_libs.deps.srom.imputation.base import TSImputer
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np
import random
import math
import copy
from random import sample
from sklearn.utils.validation import check_array


class InterpolateImputer(TSImputer):
    """
    InterpolateImputer using Panda's Extension
    """

    def __init__(
        self,
        time_column=-1,
        missing_values=np.nan,
        enable_fillna=None,
        method="linear",
        **kwargs,
    ):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill na after interpolation if any.
        method (str): method.
        kwargs (dict): Keyword arguments.
        """
        self.enable_fillna = enable_fillna
        self.method = method
        self.kwargs = kwargs
        super(InterpolateImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
        )

    def transform(self, X):
        """
        Transform input
        Parameters:
            X(array like): input values.
        """
        if isinstance(X, (np.ndarray, np.generic)):
            X = pd.DataFrame(X).infer_objects()

        if not np.isnan(self.missing_values):
            X[X == self.missing_values] = np.NaN

        if not (X.isnull().values.any()):
            return X.to_numpy()

        X = X.interpolate(method=self.method, **self.kwargs)
        if self.enable_fillna:
            X = X.fillna(method="ffill")
            X = X.fillna(method="bfill")
        return X.to_numpy()


class PolynomialImputer(InterpolateImputer):
    """
    PolynomialImputer imputer.
    
    """

    def __init__(
        self, time_column=-1, missing_values=np.nan, enable_fillna=True, order=1
    ):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill na after interpolation if any.
        order (int): order.
        """
        self.order = order
        super(PolynomialImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            method="polynomial",
            order=self.order,
        )


class SplineImputer(InterpolateImputer):
    """
    SplineImputer imputer.
    """

    def __init__(
        self, time_column=-1, missing_values=np.nan, enable_fillna=True, order=1
    ):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill na after interpolation if any.
        order (int): order.
        """
        self.order = order
        super(SplineImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            method="spline",
            order=self.order,
        )


class CubicImputer(InterpolateImputer):
    """
    CubicImputer imputer.
    """

    def __init__(self, time_column=-1, missing_values=np.nan, enable_fillna=True):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill na after interpolation if any.
        """
        super(CubicImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            method="cubic",
        )


class QuadraticImputer(InterpolateImputer):
    """
    QuadraticImputer imputer.
    """

    def __init__(self, time_column=-1, missing_values=np.nan, enable_fillna=True):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill na after interpolation if any.
        """
        super(QuadraticImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            method="quadratic",
        )


class AkimaImputer(InterpolateImputer):
    """
    AkimaImputer imputer.
    """

    def __init__(self, time_column=-1, missing_values=np.nan, enable_fillna=True):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill na after interpolation if any.
        """
        super(AkimaImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            method="akima",
        )


class LinearImputer(InterpolateImputer):
    """
    LinearImputer imputer.
    """

    def __init__(self, time_column=-1, missing_values=np.nan, enable_fillna=True):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill na after interpolation if any.
        """
        super(LinearImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            method="linear",
        )


class BaryCentricImputer(InterpolateImputer):
    """
    BaryCentricImputer imputer.
    """

    def __init__(self, time_column=-1, missing_values=np.nan, enable_fillna=True):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill na after interpolation if any.
        """
        super(BaryCentricImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            method="barycentric",
        )


class PreMLImputer(TSImputer):
    """
    Curve Imputer
    Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        random_state (int): random state.
    """

    def __init__(self, time_column=-1, missing_values=np.nan, random_state=0):
        """[summary]

        Args:
            time_column (int, optional): [description]. Defaults to -1.
            missing_values ([type], optional): [description]. Defaults to np.nan.
            random_state (int, optional): [description]. Defaults to 0.
        """
        self.random_state = random_state
        super(PreMLImputer, self).__init__(
            time_column=time_column, missing_values=missing_values
        )

    def _prepare_options(self):
        """
        Internal helper method.
        """
        default_options = [
            PolynomialImputer(
                time_column=self.time_column,
                missing_values=self.missing_values,
                order=1,
            ),
            PolynomialImputer(
                time_column=self.time_column,
                missing_values=self.missing_values,
                order=2,
            ),
            PolynomialImputer(
                time_column=self.time_column,
                missing_values=self.missing_values,
                order=3,
            ),
            PolynomialImputer(
                time_column=self.time_column,
                missing_values=self.missing_values,
                order=5,
            ),
            SplineImputer(
                time_column=self.time_column,
                missing_values=self.missing_values,
                order=3,
            ),
            SplineImputer(
                time_column=self.time_column,
                missing_values=self.missing_values,
                order=4,
            ),
            SplineImputer(
                time_column=self.time_column,
                missing_values=self.missing_values,
                order=5,
            ),
            CubicImputer(
                time_column=self.time_column, missing_values=self.missing_values
            ),
            LinearImputer(
                time_column=self.time_column, missing_values=self.missing_values
            ),
            AkimaImputer(
                time_column=self.time_column, missing_values=self.missing_values
            ),
            QuadraticImputer(
                time_column=self.time_column, missing_values=self.missing_values
            ),
        ]
        return default_options

    def fit(self, X, y=None, **fit_params):
        """
        fit imputer.
        Parameters:
            X(array like): input data.
        """
        if "skip_fit" in fit_params.keys() and fit_params["skip_fit"]:
            return self

        self.default_options_ = self._prepare_options()
        return self

    def _score(self, imputer, X_original, X_imputed):
        """
        internal score method.
        """
        try:
            X_filled = imputer.fit_transform(X_imputed)
            X_filled[np.isnan(X_filled)] = 0
            X_original[np.isnan(X_original)] = 0
            return mean_absolute_error(X_original, X_filled)
        except:
            return np.nan

    def get_best_imputer(self):
        """
        Return the best imputer.
        """
        if self.selected_options is None:
            raise Exception("Model is not trained")
        else:
            return self.default_options[self.selected_options[0]]

    def transform(self, X):
        """
        Transform input.
        Parameters:
            X(array like): input values.
        """
        if X is None:
            return X

        # use the local data to make decision
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()

        if not np.isnan(self.missing_values):
            X[X == self.missing_values] = np.NaN

        if np.count_nonzero(np.isnan(X)) == 0:
            return X

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        if not hasattr(self, 'default_options_'):
            self.default_options_ = self._prepare_options()

        # inject artificial noise
        random.seed(self.random_state)
        inputDB = X.copy()
        xy = np.where(inputDB != np.nan)
        idx = list(zip(xy[0], xy[1]))
        impute_size = 0.1
        sampled_idx = sample(idx, int(math.ceil(impute_size * len(idx))))
        p_data = inputDB.copy()
        for item in sampled_idx:
            p_data[item] = np.nan

        self.options_score_ = []
        for imputer in self.default_options_:
            self.options_score_.append(self._score(imputer, inputDB, p_data))

        self.selected_options = np.where(
            self.options_score_ == np.nanmin(self.options_score_)
        )[0]

        if len(self.selected_options) == 0:
            self.selected_options = [0]

        return self.default_options_[self.selected_options[0]].fit_transform(X)

    def get_performance_score(self):
        """
        Method to get performance score
        """
        if hasattr(self, "default_options_"):
            return list(tuple(zip(self.default_options_, self.options_score_)))
        else:
            raise Exception('Model is not yet fit and transformed')

    def get_X(self, X, order, is_imputed=False):
        """
        Apply flatten transformation on input.
        Parameters:
            X(array like): input array.
            order(int): lookback order.
        """
        X = check_array(X, accept_sparse=True, force_all_finite="allow-nan")
        self.original_shape = X.shape
        if is_imputed:
            X = self.default_options_[self.selected_options[0]].fit_transform(X)
        _x = []
        for i in range(order, X.shape[0] + 1):
            _x.append(X[i - order : i, :])
        _x = np.array(_x)
        _x = [list(_x[i].flatten()) for i in range(len(_x))]
        _x = np.array(_x)
        return _x

    def get_TS(self, X, order=None):
        """
        Get timeseries from input data
        Parameters:
            (X array like): input array 
        """

        def index_function(i, orig_length, order, num_cols):
            """
            The input X matrix has a fliped diagonal structure, we seek to get
            the indicies of the common elements. Example X matrix:
             array([[ 0, 40,  1, 41,  2, 42],
                    [ 1, 41,  2, 42,  3, 43],
                    [ 2, 42,  3, 43,  4, 44],
                    [ 3, 43,  4, 44,  5, 45],
                    [ 4, 44,  5, 45,  6, 46],
                    [ 5, 45,  6, 46,  7, 47],
                    [ 6, 46,  7, 47,  8, 48],
                    [ 7, 47,  8, 48,  9, 49]])
            The original time series looks like: 
             array([[ 0, 40],
                    [ 1, 41],
                    [ 2, 42],
                    [ 3, 43],
                    [ 4, 44],
                    [ 5, 45],
                    [ 6, 46],
                    [ 7, 47],
                    [ 8, 48],
                    [ 9, 49]])

            We need to colect the appropriate pairs of elements in the diagonals from lower left to upper right.
            """
            l = order
            m = orig_length - l + 1
            n = num_cols

            # create base row and column indices being aware of ts dimension
            rows = range(min(i, m - 1), max(0, i - l + 1) - 1, -1)
            cols = range(max(0, i - m + 1) * n, min(i, l - 1) * n + 1, n)

            # now replicate appropriately to pick up other dimensions
            # rows duplicate, columns increment
            rows = np.repeat(rows, n)
            cols = np.repeat(cols, n) + np.repeat(np.arange(n), len(cols))
            return (list(rows), list(cols))

        if len(self.original_shape) > 1:
            original_cols_size = self.original_shape[1]
        else:
            original_cols_size = 1

        num_rows = X.shape[0]
        num_cols = X.shape[1]

        result = np.full((self.original_shape[0], original_cols_size), np.nan)
        order = num_cols // original_cols_size

        for j in range(self.original_shape[0]):
            res = X[
                index_function(j, self.original_shape[0], order, original_cols_size)
            ]
            result[j] = np.mean(res.reshape(-1, original_cols_size, order="F"), axis=0)

        return result


"""
A = PolynomialImputer(time_column=-1, missing_values=np.nan, order=1)
df = pd.DataFrame({"A":[12, 4, 5, None, 1],
                   "B":[None, 2, 54, 3, None],
                   "C":[20, 16, None, 3, 8],
                   "D":[14, 3, None, None, 6]})

# Print the dataframe
print (df.values)
ans = A.transform(df.values)
print (ans)

A = PolynomialImputer(time_column=-1, missing_values=np.nan, order=2)
ans = A.transform(df.values)
print (ans)

A = PreMLImputer()
X= pd.DataFrame({"A":[1,2,3,4,5,None,7,8,9]})
X= pd.DataFrame({"A":[1,2,3,4,5,None,7,8,9,10],"B":[101,102,None,104,105,106,107,108,109,110],"C":[51,52,None,54,55,56,None,58,59,60]})
df = X
#print (df)
ans = A.transform(df)
#print (ans)
X=A.get_X(df,order=5,is_imputed=True)
print(X)
print(A.get_TS(X))

"""
