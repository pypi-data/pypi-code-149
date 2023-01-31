# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: ts local reg imputer
   :synopsis: ts local reg imputer.

.. moduleauthor:: SROM Team
"""
import copy

import numpy as np

from autoai_ts_libs.deps.srom.imputation.ts_imputer.ts_mul_var_base_imputer import (
    TSMulVarBaseImputer,
)
from autoai_ts_libs.deps.srom.imputation.ts_imputer.ts_mul_var_simple_imputer import (
    TSMulVarSimpleImputer,
)


def _polyfit(x, y, x0, weights=None, degree=2):
    """
    Internal method to get the polyfit.
    """
    if len(x) == 0:
        return np.nan * np.ones_like(x0)

    if weights is None:
        weights = np.ones_like(x)

    s = np.sqrt(weights)
    X = x[:, None] ** np.arange(degree + 1)
    X0 = x0[:, None] ** np.arange(degree + 1)
    lhs = X * s[:, None]
    rhs = y * s

    rcond = np.finfo(lhs.dtype).eps * max(*lhs.shape)
    beta = np.linalg.lstsq(lhs, rhs, rcond=rcond)[0]
    return X0.dot(beta)


def _rectangular(t):
    """
    Internal method to get the rectangular.
    """
    res = np.zeros_like(t)
    ind = np.where(np.abs(t) <= 1)
    res[ind] = 0.5
    return res


def _triangular(t):
    """
    Internal method to get the traingular.
    """
    res = np.zeros_like(t)
    ind = np.where(np.abs(t) <= 1)
    res[ind] = 1 - np.abs(t[ind])
    return res


def _epanechnikov(t):
    """
    Internal method to get the epanechnikov.
    """
    res = np.zeros_like(t)
    ind = np.where(np.abs(t) <= 1)
    res[ind] = 0.75 * (1 - t[ind] ** 2)
    return res


def _biweight(t):
    """
    Internal method to get the biweight.
    """
    res = np.zeros_like(t)
    ind = np.where(np.abs(t) <= 1)
    res[ind] = (15 / 16) * (1 - t[ind] ** 2) ** 2
    return res


def _triweight(t):
    """
    Internal method to get the triweight.
    """
    res = np.zeros_like(t)
    ind = np.where(np.abs(t) <= 1)
    res[ind] = (35 / 32) * (1 - t[ind] ** 2) ** 3
    return res


def _tricube(t):
    """
    Internal method to get the tricube.
    """
    res = np.zeros_like(t)
    ind = np.where(np.abs(t) <= 1)
    res[ind] = (70 / 81) * (1 - np.abs(t[ind]) ** 3) ** 3
    return res


def _gaussian(t):
    """
    Internal method to get the gaussian.
    """
    res = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * t**2)
    return res


def _cosine(t):
    """
    Internal method to get the cosine.
    """
    res = np.zeros_like(t)
    ind = np.where(np.abs(t) <= 1)
    res[ind] = (np.pi / 4) * np.cos(np.pi * t[ind] / 2)
    return res


def _logistic(t):
    """
    Internal method to get the logistic.
    """
    res = 1 / (np.exp(t) + 2 + np.exp(-t))
    return res


def _sigmoid(t):
    """
    Internal method to get the sigmoid.
    """
    res = (2 / np.pi) / (np.exp(t) + np.exp(-t))
    return res


def _silverman(t):
    """
    Internal method to get the silverman.
    """
    res = (
        0.5
        * np.exp(-np.abs(t) / np.sqrt(2))
        * np.sin(np.abs(t) / np.sqrt(2) + np.pi / 4)
    )
    return res


class TSLocalRegImputer(TSMulVarBaseImputer):
    """
    Transformer obeys Scikit-learn interface and implements local polynomial regression imputer for univariate time series
            utilizing local polynomial regression Imputing


    Algorithm:

        It is a two step imputation.  First it utilizes TSMulVarSimpleImputer to impute the missing values.
        Then, it applies the local regularization imputing with a kernel to have more precise imputing.

    Return:
        imputed univariate time series

    """

    def __init__(
        self,
        degree=2,
        kernel="epanechnikov",
        width=1,
        frac=None,
        default_imputer=None,
        enable_debug: bool = False,
    ):
        """
        Args:
        degree:  The degree used for the internal polynomial fitting
        kernel:  The kernel used for local polynomial regression
        width:   The width is used to tune the kernal
        frac:  The fraction of the data points used for imputing
        default_imputer:  TSMulVarSimpleImputer (used to impute the missing as first step)
        param enable_debug: flag enables printing out debugging information.
        """
        if default_imputer is None:
            default_imputer = TSMulVarSimpleImputer()

        self.degree = degree
        self.kernel = kernel
        self.width = width
        self.frac = frac
        self.default_imputer = default_imputer
        self.enable_debug = enable_debug

    def _impute(self, X: np.ndarray) -> np.ndarray:
        """Does the actual imputation."""

        if X.shape[1] != 1:
            raise ValueError(
                "timeseries imputor expects a single-column matrix as an input"
            )
        if self.enable_debug:
            print("Imputer Class: ", self.__class__.__name__)

        X_source = copy.deepcopy(X)
        length = X_source.shape[0]

        degree = self.degree
        kernel = self.kernel
        width = self.width
        frac = self.frac
        default_imputer = self.default_imputer

        # series = pd.Series(X.flatten())
        # local_series = copy.deepcopy(series)

        # x = np.linspace(1, local_series.shape[0], local_series.shape[0])
        # y = local_series.values
        x = np.linspace(1, length, length)
        y = X_source.flatten()

        if kernel == "epanechnikov":
            kernel = _epanechnikov
        elif kernel == "rectangular":
            kernel = _rectangular
        elif kernel == "triangular":
            kernel = _triangular
        elif kernel == "biweight":
            kernel = _biweight
        elif kernel == "triweight":
            kernel = _triweight
        elif kernel == "tricube":
            kernel = _tricube
        elif kernel == "gaussian":
            kernel = _gaussian
        elif kernel == "cosine":
            kernel = _cosine
        elif kernel == "logistic":
            kernel = _logistic
        elif kernel == "sigmoid":
            kernel = _sigmoid
        elif kernel == "silverman":
            kernel = _silverman
        else:
            pass

        x0 = x
        y0 = np.zeros_like(x0)

        original_missing = np.isnan(y)
        x1 = x
        tmpX = default_imputer.fit_transform(copy.deepcopy(X_source))
        y1 = tmpX.flatten()

        while True:
            if frac is None:
                for i, xi in enumerate(x0):
                    weights = kernel(np.abs(x1 - xi) / width)

                    inds = np.where(np.abs(weights) > 1e-10)[0]
                    y0[i] = _polyfit(
                        x1[inds], y1[inds], np.array([xi]), weights[inds], degree=degree
                    )
            else:
                N = int(frac * len(x1))
                for i, xi in enumerate(x0):
                    dist = np.abs(x1 - xi)
                    inds = np.argsort(dist)[:N]
                    width = dist[inds][-1]
                    weights = kernel(dist[inds] / width)
                    y0[i] = _polyfit(
                        x1[inds], y1[inds], np.array([xi]), weights, degree=degree
                    )

            y[original_missing] = y0[original_missing]
            if len(np.where(np.isnan(y))) == 0:
                break

            # new x and y
            not_missing = ~np.isnan(y0)
            where = np.where(not_missing)
            x1 = x[where]
            y1 = y[where]

            if len(y1) == len(y):
                break

        where = np.where(original_missing)
        y[where] = y0[where]

        ret = y0.reshape(-1, 1)

        return ret
