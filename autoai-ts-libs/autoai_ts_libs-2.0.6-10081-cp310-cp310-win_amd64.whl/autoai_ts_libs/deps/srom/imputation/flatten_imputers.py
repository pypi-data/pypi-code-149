# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: flatten_imputers
   :synopsis: flatten_imputers.

.. moduleauthor:: SROM Team
"""

from sklearn.utils.validation import check_array
from sklearn.impute import SimpleImputer
from sklearn.impute._base import _BaseImputer
from sklearn.base import clone
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from autoai_ts_libs.deps.srom.imputation.base import TSImputer, FlattenImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from autoai_ts_libs.deps.srom.imputation.interpolators import PreMLImputer
from sklearn.impute import KNNImputer

class FlattenIterativeImputer(FlattenImputer):
    """
    Flatten Iterative Imputer.
    """

    def __init__(
        self,
        time_column=-1,
        missing_values=np.nan,
        enable_fillna=True,
        order=-1,
        base_imputer=PreMLImputer(),
        model_imputer=IterativeImputer(),
    ):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill the backword and forward.
        order (int): lookback window.
        base_imputer(obj): base imputer object.
        model_imputer(obj): model imputer object.
        """
        super(FlattenIterativeImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            order=order,
            base_imputer=base_imputer,
            model_imputer=model_imputer,
        )


class FlattenKNNImputer(FlattenImputer):
    """
    Flatten KNNImputer.
    """

    def __init__(
        self,
        time_column=-1,
        missing_values=np.nan,
        enable_fillna=True,
        order=-1,
        base_imputer=PreMLImputer(),
        model_imputer=KNNImputer(),
    ):
        """
        Parameters:
        time_column (int): time column.
        missing_values (obj): missing value to be imputed.
        enable_fillna (boolean): fill the backword and forward.
        order (int): lookback window.
        base_imputer(obj): base imputer object.
        model_imputer(obj): model imputer object.
        """
        super(FlattenKNNImputer, self).__init__(
            time_column=time_column,
            missing_values=missing_values,
            enable_fillna=enable_fillna,
            order=order,
            base_imputer=base_imputer,
            model_imputer=model_imputer,
        )
