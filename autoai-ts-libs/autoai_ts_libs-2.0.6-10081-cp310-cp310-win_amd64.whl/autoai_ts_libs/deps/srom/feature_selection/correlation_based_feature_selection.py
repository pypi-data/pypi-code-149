# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: correlation_based_feature_selection
   :synopsis: Contains class which provides functionalities for \
        correlation based feature selection.

.. moduleauthor:: SROM Team
"""
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CorrelatedFeatureElimination(BaseEstimator, TransformerMixin):
    """
    A method to remove multicollinearity from input data frame. \
    https://en.wikipedia.org/wiki/Multicollinearity \
    Input is a dataframe that contain variables, except target variable. \
    The tranform function removes multi-correlated variables.
    """

    def __init__(self, cl_threshold_value=0.9):
        """
        Parameters:
            cl_threshold_value: A threshold to remove the variable with high correlation. \
                                Defaults to 0.9.
        """
        self.cl_threshold_value = cl_threshold_value
        self.cl = None  # this argument store the name of removed variables
        self.selected_columns = None
        self.total_columns = 0

    def fit(self, X, y=None, **kwParameters):
        """
        Parameters:
            X (pandas.DataFrame): Input data. Contain variables, except target variable.

        Returns:
            (pandas.DataFrame): Transformed data with multicollinearity removed.
        """

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

        corr_mat = X.corr()
        n_features = corr_mat.shape[0]

        remove_indices = []
        cl_value = []
        v_name = []

        for i in range(n_features):
            for j in range(i + 1, n_features):
                if abs(corr_mat.iloc[i, j]) > self.cl_threshold_value:
                    if i not in remove_indices:
                        remove_indices.append(i)
                        cl_value.append(corr_mat.iloc[i, j])
                        v_name.append(X.columns[i])

        self.total_columns = X.shape[1]
        self.selected_columns = []
        clms = list(X.columns)
        for item in range(self.total_columns):
            if item not in remove_indices:
                self.selected_columns.append(clms[item])

        self.cl = pd.DataFrame()
        self.cl["removed_variable"] = v_name
        self.cl["correlation_value"] = cl_value

        return self

    def transform(self, X, **kwParameters):
        """
        Parameters:
            X (pandas.DataFrame): Input data. Contain variables, except target variable.
            
        Returns:
            (pandas.DataFrame): Transformed data with multicollinearity removed.
        """
        if self.selected_columns:
            if not isinstance(X, pd.DataFrame):
                X = pd.DataFrame(
                    X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])]
                )
            else:
                for item in self.selected_columns:
                    if item not in list(X.columns):
                        raise Exception("Column is not found")

            if X.shape[1] == self.total_columns:
                return X[self.selected_columns]
            else:
                raise Exception("Model Data Missmatch")
        else:
            raise Exception("Model is not trained")
