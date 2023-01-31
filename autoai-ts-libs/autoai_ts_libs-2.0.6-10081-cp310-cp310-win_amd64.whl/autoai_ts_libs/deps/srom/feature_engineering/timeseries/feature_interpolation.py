# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: feature_interpolation
   :synopsis: Time Series Feature Interpolation : Example Dataset Project Health.

.. moduleauthor:: SROM Team
"""
import copy
import logging
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

LOGGER = logging.getLogger(__name__)


class FeatureInterpolation(BaseEstimator, TransformerMixin):
    """
    Performs feature interpolation on time series data \
    at given set of regular intervals for given set of columns.
    """

    def __init__(
        self,
        feature_column=None,
        time_id=None,
        interpolation_point=None,
        delta_boundary=0.05,
    ):
        """
        Parameters:
            feature_column: Column names w.r.t. which data extraction is performed.
            time_id: Column name for representing a time.
            interpolation_point: A list of time, where the sampling should be performed.
            delta_boundary: A delta threshold for prediction_Interval.

        Returns:
            A panda dataframe columns are interpolation_point, and feature_column are row.
        """

        self.feature_column = feature_column
        self.time_id = time_id
        self.delta_boundary = delta_boundary

        if interpolation_point:
            self.interpolation_point = interpolation_point
        else:
            self.interpolation_point = []

        self.extracted_features_columns = None

    def fit(self, X, y=None, **kwargs):
        """
        Fit method
        """
        return self

    def transform(self, X, **kwargs):
        """
        Parameters:
            X: pandas.DataFrame.

        Returns:
            pandas.DataFrame: Sampled DataFrame.
        """

        if not isinstance(X, pd.DataFrame):
            LOGGER.info("Feature Sampler needs pandas dataframe")
            raise ValueError("Input must be panda dataframe")

        s_val = []
        for col in self.feature_column:
            Y = list(X.loc[:, col])
            X1 = list(X.loc[:, self.time_id])
            y_temp = []
            x1_temp = []

            for ind, item in enumerate(X1):
                if not np.isnan(item):
                    if not np.isnan(Y[ind]):
                        y_temp.append(Y[ind])
                        x1_temp.append(item)
            Y = y_temp
            X1 = x1_temp

            p_interval = copy.copy(self.interpolation_point)
            val = list(np.interp(p_interval, X1, Y))
            for i, _ in enumerate(val):
                if (np.nanmax(X1) + self.delta_boundary) < p_interval[i]:
                    val[i] = np.nan

            s_val.append(val)

        sampled_db = pd.DataFrame(s_val)
        sampled_db.index = self.feature_column
        sampled_db.columns = p_interval
        return sampled_db
