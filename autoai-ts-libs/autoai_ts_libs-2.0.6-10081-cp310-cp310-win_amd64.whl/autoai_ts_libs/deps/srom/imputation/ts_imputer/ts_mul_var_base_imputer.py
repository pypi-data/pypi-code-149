# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: ts mul var base imputer
   :synopsis: ts mul var base imputer.

.. moduleauthor:: SROM Team
"""


import copy

import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.imputation.base import TSImputer


class TSMulVarBaseImputer(TSImputer):

    """
    TSMulVarBaseImputer obeys Scikit-learn interface and implements the formward imputation for univariate time series

    The forward imputer keeps

    Algorithm:

        Using the latest known non-missing value to impute the missing

    Return:
        imputed univariate or multi-variate time series using forward imputing

    """

    def __init__(self, enable_debug: bool = False):
        """
        Args:
        param enable_debug: flag enables printing out debugging information.
        """
        self.enable_debug = enable_debug

    def transform(self, X: np.ndarray) -> np.ndarray:

        """Scikit interface function."""

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        return self._impute(X)

    def _impute(self, X: np.ndarray) -> np.ndarray:
        """Does the actual imputation."""

        if self.enable_debug:
            print("Imputer Class: ", self.__class__.__name__)
            print("The dimension of multi-variate input: ", X.shape)

        # Loop over all the columns, and make imputation for each of the column

        num_vars = X.shape[1]

        imputed = []
        for i in range(num_vars):

            if self.enable_debug:
                print("column: ", i)
            X_i = X[:, i]

            series = pd.Series(X_i.flatten())

            local_series = copy.deepcopy(series)
            local_series = local_series.fillna(method="ffill")
            local_series = local_series.fillna(method="bfill")

            tmp_X_i = local_series.values
            tmp_X_i = tmp_X_i.reshape(-1, 1)

            X_i = X_i.reshape(-1, 1)

            if self.enable_debug:
                print(np.concatenate((X_i, tmp_X_i), axis=1))

            imputed.append(tmp_X_i)

        ans = np.hstack(imputed)
        if self.enable_debug:
            print("Imputed Results: ", ans)

        return ans
