# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: event_preprocessing
   :synopsis: Contains implementation for event based preprocessing.

.. moduleauthor:: SROM Team
"""
import logging
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)


class DaysSinceLastEvent(BaseEstimator, TransformerMixin):
    """
    DaysSinceLastEvent Class: Contains functionality to transform input dataset
    to have engineered features having count of days since last event occurred.
    """

    def __init__(
        self, time_column=None, event_columns=None, columns_to_be_ignored=None
    ):
        """
        Parameters:
            time_column: Column name for time column in the input data.
            event_columns: List of event column names.
            columns_to_be_ignored: List of columns to be ignore while processing.

        Note:
            event_columns and columns_to_be_ignored should not be provided at same time.
        """
        self.time_column = time_column
        self.event_columns = event_columns
        self.columns_to_be_ignored = columns_to_be_ignored

    def fit(self, X, y=None, **kwargs):
        """
        fit method.
        """
        return self

    def transform(self, X, **kwargs):
        """
        Parameters:
            X (pandas.DataFrame, required): Training set.

        Returns:
            pandas.DataFrame: Original training set along with engineered features \
                having count of days since last event occurred.
        """
        if not isinstance(X, pd.DataFrame):
            raise TypeError("X should be of type : pandas.Dataframe")
        pd.to_datetime(X[self.time_column])
        X = X.set_index(pd.DatetimeIndex(X[self.time_column]), drop=True)
        if self.event_columns is not None and self.columns_to_be_ignored is not None:
            raise BaseException(
                "Please specify either event_columns or columns_to_be_ignored"
            )
        if self.event_columns is not None:
            features = list(self.event_columns)
            if self.time_column not in features:
                features.append(self.time_column)
            dataframe = X[features]
        elif self.columns_to_be_ignored is not None:
            columns = X.columns
            columns = list(set(columns) - set(self.columns_to_be_ignored))
            dataframe = X[columns]
        else:
            dataframe = X
        event_columns = list(dataframe.columns)
        if self.time_column in event_columns:
            event_columns.remove(self.time_column)
        for column in event_columns:
            last_col = "last_" + column
            X[last_col] = np.where(X[column] > 0, X.index, np.datetime64("NaT"))
            X[last_col] = X[last_col].fillna(method="ffill")
            X[last_col] = X.index - X[last_col]
            X[last_col] = X[last_col].dt.days

        X.drop(dataframe.index)
        X = X.fillna(np.iinfo(np.int32).max)
        return X


class ConsecutiveEventCount(BaseEstimator, TransformerMixin):
    """
    ConsecutiveEventCount class contains the functionality to transform input dataset \
    to have engineered features having count of consecutive events that occurred.
    """

    def __init__(
        self, time_column=None, event_columns=None, columns_to_be_ignored=None
    ):
        """
        Parameters:
            time_column: Column name for time column in the input data.
            event_columns: List of event column names.
            columns_to_be_ignored: List of columns to be ignore while processing.

        Note:
            event_columns and columns_to_be_ignored should not be provided at same time.
        """
        self.time_column = time_column
        self.event_columns = event_columns
        self.columns_to_be_ignored = columns_to_be_ignored

    def fit(self, X, y=None, **kwargs):
        """
        fit method.
        """
        return self

    def transform(self, X, **kwargs):
        """
        Parameters:
            X (pandas.DataFrame, required): Training set.

        Returns:
            pandas.DataFrame: Original training set along with engineered features \
                having count of consecutive events that occurred.
        """
        if not isinstance(X, pd.DataFrame):
            raise TypeError("X should be of type : pandas.Dataframe")
        pd.to_datetime(X[self.time_column])
        X = X.set_index(pd.DatetimeIndex(X[self.time_column]), drop=True)

        if self.event_columns is not None and self.columns_to_be_ignored is not None:
            raise BaseException(
                "Please specify either event_columns or columns_to_be_ignored"
            )
        if self.event_columns is not None:
            features = list(self.event_columns)
            if self.time_column not in features:
                features.append(self.time_column)
            dataframe = X[features]
        elif self.columns_to_be_ignored is not None:
            columns = X.columns
            columns = list(set(columns) - set(self.columns_to_be_ignored))
            dataframe = X[columns]
        else:
            dataframe = X
        event_columns = list(dataframe.columns)
        if self.time_column in event_columns:
            event_columns.remove(self.time_column)
        
        for column in event_columns:
            consec_col = "consecutive_" + column
            prev = 0
            values = []
            consec_count = 0
            for _, value in list(X[column].items()):
                if value > 0 and prev == 1:
                    consec_count += 1
                    prev = 1
                else:
                    consec_count = 0
                    if value > 0:
                        prev = 1
                    else:
                        prev = 0
                values.append(consec_count)
            X[consec_col] = values
        X.drop(X.index)
        X = X.fillna(0)
        return X
