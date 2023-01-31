# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: feature_selection
   :synopsis: Contains Contains classes which can be used \
        for feature selection.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class FeatureListSelector(BaseEstimator, TransformerMixin):
    """
    Allows users to provide a list of features to be used for modelling and \
    get a dataframe of selected features.
    """

    def __init__(self, feature_list=None):
        """
        Parameters:
            feature_list: List of feature names to be selected, these have to \
                match with the column names in the input dataframe.
        """
        self.feature_list = feature_list
        self.input_features = None

    def fit(self, X, y=None, **kwParameters):
        """
        Fit method.
        """
        return self

    def transform(self, X, **kwParameters):
        """
        Transform method.
        """
        if self.feature_list is not None:
            if not isinstance(X, pd.DataFrame):
                raise Exception("Input data must be a pandas dataframe.")
            self.input_features = X.columns.tolist()

            return X.loc[:, self.feature_list]
        return X


class FeatureListDropper(BaseEstimator, TransformerMixin):
    """
    Allows users to provide a list of features to be dropped from the \
    input dataframe and get a dataframe of selected features.
    """

    def __init__(self, feature_list=None):
        """
        Parameters:
            feature_list: list of feature names to be dropped, these have \
                to match with the column names in the input dataframe.
        """
        self.feature_list = feature_list
        self.input_features = None

    def fit(self, X, y=None, **kwParameters):
        """
        Fit method.
        """
        return self

    def transform(self, X, **kwParameters):
        """
        Transform method.
        """
        if self.feature_list is not None:
            if not isinstance(X, pd.DataFrame):
                raise Exception("Input data must be a pandas dataframe.")
            self.input_features = X.columns.tolist()

            return X.drop(list(self.feature_list), axis=1)
        return X
