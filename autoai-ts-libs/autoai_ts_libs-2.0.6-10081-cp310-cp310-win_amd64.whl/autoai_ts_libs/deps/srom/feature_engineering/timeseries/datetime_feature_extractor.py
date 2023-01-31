# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: datetime_feature_extractor
   :synopsis: Date time feature extraction.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np


class DateTimeFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    Performs datetime feature extraction on a column with datetime stamp.
    """

    def __init__(self, time_id, features=["Year", "Month", "Quarter", "isWeekDay"]):
        """
        Parameters:
            time_id (string/int): Column name for a data frame contained datetime or column index for numpy.

        Returns:
            DataFrame with extracted features or numpy.
        """
        self.time_id = time_id
        self.features = features

    def _supported_features(self):
        """
            Internal method for supported features
        """
        return [
            "Year",
            "Month",
            "Day",
            "Hour",
            "Minute",
            "Second",
            "WeekofYear",
            "Quarter",
            "DayofWeek",
            "DayofYear",
            "isWeekDay",
        ]

    def _weekofyear_features(self, x):
        """
            Internal method for weekofyear features
        """
        ans_x = x.weekofyear
        return ans_x

    def _month_features(self, x):
        """
            Internal method for month features
        """
        ans_x = x.month
        return ans_x

    def _day_features(self, x):
        """
            Internal method for day features
        """
        ans_x = x.day
        return ans_x

    def _year_features(self, x):
        """
            Internal method for year features
        """
        ans_x = x.year
        return ans_x

    def _hour_features(self, x):
        """
            Internal method for hour features
        """
        ans_x = x.hour
        return ans_x

    def _minute_features(self, x):
        """
            Internal method for minute features
        """
        ans_x = x.minute
        return ans_x

    def _second_features(self, x):
        """
            Internal method for second features
        """
        ans_x = x.second
        return ans_x

    def _dayofweek_features(self, x):
        """
            Internal method for dayofweek features
        """
        ans_x = x.dayofweek
        return ans_x

    def _dayofyear_features(self, x):
        """
            Internal method for dayofyear features
        """
        ans_x = x.dayofyear
        return ans_x

    def _quarter_features(self, x):
        """
            Internal method for quarter features
        """
        ans_x = x.quarter
        return ans_x

    def _isWeekDay_features(self, x):
        """
            Internal method for issWeekDay features
        """
        if x >= 5:
            return 0
        return 1

    def _generate_intermediate_features(self, X):
        """
            Internal method for generate intermediate features
        """
        sampleX = X.copy()
        sampleX[self.time_id] = pd.to_datetime(sampleX[self.time_id])

        # simple
        sampleX["Year"] = sampleX[self.time_id].apply(self._year_features)
        sampleX["Month"] = sampleX[self.time_id].apply(self._month_features)
        sampleX["Day"] = sampleX[self.time_id].apply(self._day_features)
        sampleX["Hour"] = sampleX[self.time_id].apply(self._hour_features)
        sampleX["Minute"] = sampleX[self.time_id].apply(self._minute_features)
        sampleX["Second"] = sampleX[self.time_id].apply(self._second_features)

        # derived
        sampleX["WeekofYear"] = sampleX[self.time_id].apply(self._weekofyear_features)
        sampleX["Quarter"] = sampleX[self.time_id].apply(self._quarter_features)
        sampleX["DayofWeek"] = sampleX[self.time_id].apply(self._dayofweek_features)
        sampleX["DayofYear"] = sampleX[self.time_id].apply(self._dayofyear_features)
        sampleX["isWeekDay"] = sampleX["DayofWeek"].apply(self._isWeekDay_features)
        return sampleX[self.features]

    def fit(self, X, y=None, **kwargs):
        """
        Fit method. (For actual transformation, use the 'transform' method instead)
        """
        if not (set(self.features).issubset(set(self._supported_features()))):
            raise Exception(
                "DateTimeFeatureExtractor cannot extrct some features given in init argument. Please call _supported_features to obtain list of supported features"
            )

        if isinstance(X, (np.ndarray, np.generic)):
            X = pd.DataFrame(X)
            columns_name = ["c_" + str(i) for i in range(X.shape[1])]
            self.time_id = "c_" + str(self.time_id)
            X.columns = columns_name

        sampleX = self._generate_intermediate_features(X)

        enc = OneHotEncoder(handle_unknown="ignore", sparse=False)
        tmpX = sampleX
        enc.fit(tmpX)
        tmpName = enc.get_feature_names()

        clmName = []
        replacementName = {}
        for item_i, item in enumerate(self.features):
            replacementName["x" + str(item_i)] = item

        for item in tmpName:
            prefix_n = item.split("_")[0]
            clmName.append(item.replace(prefix_n, replacementName[prefix_n]))

        self.enc = enc
        self.clmName = clmName
        return self

    def transform(self, X, **kwargs):
        """
        Parameters:
            X (pandas.DataFrame, required): Transforming the input dataframe to the episode \
                    time series dataframe to be fed into the srom pipeline.

        Returns:
            pandas.DataFrame: TS Fresh extracted dataframe.
        """
        is_numpy_array = False
        if isinstance(X, (np.ndarray, np.generic)):
            X = pd.DataFrame(X)
            columns_name = ["c_" + str(i) for i in range(X.shape[1])]
            X.columns = columns_name
            is_numpy_array = True

        sampleX = self._generate_intermediate_features(X)
        newX = self.enc.transform(sampleX)

        if is_numpy_array:
            return newX

        newX = pd.DataFrame(newX)
        newX.columns = self.clmName
        return newX
