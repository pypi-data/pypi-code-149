# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: feature_engineering
   :synopsis: Contains class which provides functionalities \
       for feature engineering.

.. moduleauthor:: SROM Team
"""
import numpy as np
import pandas as pd


class MovingAverage(object):
    """
    Provides functionality to add time based moving averages for each of the \
    original features as additional features.

    Note:
        column_names or columns_to_be_ignored must be not be specified together.
    """

    def __init__(
        self,
        window_size=1,
        min_periods=None,
        column_names=None,
        columns_to_be_ignored=None,
    ):
        """
        Parameters:
        window_size (integer): Size of the moving window in terms of number of observations \
            used for computing mean. Defaults to 1.
        min_periods (integer): Minimum number of observations in window required to \
            have a value (otherwise result is NA). Defaults to None.
        column_names (list): A list of column names if the moving average needs to be \
            selectively applied to columns. Defaults to None.
        columns_to_be_ignored (list): A list of column names to be ignored. Defaults to None.
        """
        self.window_size = window_size
        self.min_periods = min_periods
        self.column_names = column_names
        self.columns_to_be_ignored = columns_to_be_ignored

    def fit(self, X, y=None, **kwargs):
        """
        Fit method
        """
        return self

    def transform(self, X, **kwargs):
        """
        Adds time based moving averages for each of the original \
            features as additional feature.
            
        Parameters:
            X: (pandas.DataFrame or numpy.ndarray, required): Input data.

        Returns:
            (pandas.DataFrame): Transformed data.
        """
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)
        if not isinstance(X, pd.DataFrame):
            raise Exception(
                "Input data must be either pandas dataframe or numpy ndarray."
            )
        if self.column_names is not None and self.columns_to_be_ignored is not None:
            raise BaseException(
                "Please specify either column_names or columns_to_be_ignored"
            )
        if self.column_names is not None:
            df = X[self.column_names]
        elif self.columns_to_be_ignored is not None:
            columns = X.columns
            columns = list(set(columns) - set(self.columns_to_be_ignored))
            df = X[columns]
        else:
            df = X
        columns = df.columns
        new_feature_names = []
        for column in columns:
            new_feature_names.append(column + "_mavg_" + str(self.window_size))
        df_new_features = df.rolling(
            self.window_size, min_periods=self.min_periods
        ).mean()
        df_new_features.columns = new_feature_names

        df = pd.concat([X, df_new_features], axis=1)
        # first self.window_size -1 rows are NaN, so drop them.
        return df[self.window_size - 1 :]
