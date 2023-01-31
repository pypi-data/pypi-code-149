# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: ts mul var simple imputer
   :synopsis: ts mul var simple imputer.

.. moduleauthor:: SROM Team
"""
import copy
import math
import random

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error

from autoai_ts_libs.deps.srom.imputation.ts_imputer.ts_mul_var_base_imputer import (
    TSMulVarBaseImputer,
)


class TSMulVarSimpleImputer(TSMulVarBaseImputer):

    """
    Simple Interpolation Imputer


    Algorithm:

        Loop over a set of interpolation algorithms, and find out the best interpolation
        using an artificial missing sampled data points.

        Using the best imputer to impute the data

    Return:
        imputed univariate time series

    """

    def __init__(self, enable_debug: bool = False):
        """
        Args:

        missing_values:  default - np.nan
        enable_debug: booloon - False
        """

        self.missing_values = np.nan
        self.enable_debug = enable_debug

        self.strategy = "auto"

        self.autoOptions = [
            {"method": "polynomial", "order": 5, "limit_area": None},
            {"method": "polynomial", "order": 2, "limit_area": None},
            {"method": "polynomial", "order": 3, "limit_area": None},
            {"method": "polynomial", "order": 7, "limit_area": None},
            {"method": "spline", "order": 3, "limit_area": None},
            {"method": "spline", "order": 4, "limit_area": None},
            {"method": "spline", "order": 5, "limit_area": None},
            {"method": "cubic", "limit_area": None},
            {"method": "slinear", "limit_area": None},
            {"method": "akima", "limit_area": None},
            {"method": "linear", "limit_area": None},
            {"method": "quadratic", "limit_area": None},
        ]

    def _impute(self, X: np.ndarray) -> np.ndarray:
        """Does the actual imputation."""

        if self.enable_debug:
            print("Imputer Class: ", self.__class__.__name__)
            print("Type of X", type(X))
            print(X)

        num_vars = X.shape[1]
        ans = None

        if num_vars == 1:
            ans = self._univar_impute(X)
        else:
            imputed = []
            for i in range(num_vars):

                if self.enable_debug:
                    print("column: ", i)
                X_i = X[:, i]
                X_i = X_i.reshape(-1, 1)
                tmp_X_i = self._univar_impute(X_i)

                if self.enable_debug:
                    print(np.concatenate((X_i, tmp_X_i), axis=1))

                imputed.append(tmp_X_i)

            ans = np.hstack(imputed)
            if self.enable_debug:
                print("Imputed Results: ", ans)

        return ans

    def _univar_impute(self, X: np.ndarray) -> np.ndarray:
        """Does the actual imputation."""

        if self.enable_debug:
            print("Imputer Class: ", self.__class__.__name__)

        series = pd.Series(X.flatten())

        missing_num = sum(np.isnan(series))

        if missing_num > 0:
            self.autoOptions_score = []
            for item in self.autoOptions:
                self.autoOptions_score.append(self._score(series, **item))

            self.selected_options = np.where(
                self.autoOptions_score == np.nanmin(self.autoOptions_score)
            )[0]

            if self.enable_debug:
                print("All the scores: ", self.autoOptions_score)

            if len(self.selected_options) == 0:
                self.selected_options = [0]

            local_series = copy.deepcopy(series)
            local_series = local_series.interpolate(
                **self.autoOptions[self.selected_options[0]]
            )

            if self.enable_debug:
                print("Selected: ", self.autoOptions[self.selected_options[0]])

            local_series = local_series.fillna(method="ffill")
            local_series = local_series.fillna(method="bfill")

            ans = local_series.values
            ans = ans.reshape(-1, 1)

            return ans
        else:
            return copy.deepcopy(X)

    def _score(self, X, **interpolate_param):
        """
        calling score method
        """

        if self.enable_debug:
            print("Invoke: ", interpolate_param)

        try:

            series = X.copy()
            missing_num = sum(np.isnan(series))

            if self.enable_debug:
                print("Missed Values: ", missing_num)

            if missing_num == len(series):
                return np.nan

            random.seed()
            artificial_miss = random.sample(
                list(np.where(~np.isnan(series))[0]), math.ceil(missing_num * 0.5)
            )
            series[artificial_miss] = np.nan
            local_series = series.interpolate(**interpolate_param)
            local_series = local_series.fillna(method="ffill")
            local_series = local_series.fillna(method="bfill")

            orig_y = X[artificial_miss]
            pred_y = local_series[artificial_miss]

            mae = mean_absolute_error(orig_y, pred_y)

            return mae

        except Exception as e:

            if self.enable_debug:
                print(e)

            return np.nan
