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

from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from sklearn.metrics import mean_absolute_error
import random
import math
import copy


class ImputationTimeSeries:
    """
    Imputation methods for time series data
    """

    @staticmethod
    def linear(df):
        """
        Perform linear interpolation ignoring index and treating values as equally spaced

        :param df: dataframe with a datetime index
        :return: dataframe with missing values filled in
        """
        return df.interpolate()

    @staticmethod
    def time(df):
        """
        Works on daily and higher resolution data to interpolate given length of interval

        :param df: dataframe with a datetime index
        :return: dataframe with missing values filled in
        """
        return df.interpolate(method="time")

    @staticmethod
    def index(df):
        """
        Use the actual numerical values of the index.

        :param df: dataframe with a datetime index
        :return: dataframe with missing values filled in
        """
        return df.interpolate(method="index")

