# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: variance_based_feature_selection
   :synopsis: Contains class which provides functionalities \
       for variance based feature selection.

.. moduleauthor:: SROM Team
"""
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class LowVarianceFeatureElimination(BaseEstimator, TransformerMixin):
    """
    A method to remove multicollinearity from input data frame. \
    https://en.wikipedia.org/wiki/Multicollinearity \
    Input is a dataframe that contain variables, except target variable. \
    The tranform function removes multi-correlated variables.
    """

    def __init__(self, var_threshold_value=0.1):
        """
        Parameters:
            var_threshold_value: A threshold to remove the variable with low variance. \
                Defaults to 0.1
        """
        self.var_threshold_value = var_threshold_value
        self.var = None  # this argument store the name of removed variables
        self.selected_columns = None
        self.total_columns = 0

    def fit(self, X, y=None, **kwParameters):
        """
        Fit method
        """
        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

        self.total_columns = X.shape[1]
        n_features = X.shape[1]
        remove_indices = []
        var_value = []
        v_name = []

        for i in range(n_features):
            std_var = X.iloc[:, i].var()
            if std_var < self.var_threshold_value:
                remove_indices.append(i)
                var_value.append(std_var)
                v_name.append(X.columns[i])

        self.var = pd.DataFrame()
        self.var["removed_variable"] = v_name
        self.var["var_value"] = var_value

        self.selected_columns = []
        clms = list(X.columns)
        for item in range(self.total_columns):
            if item not in remove_indices:
                self.selected_columns.append(clms[item])
        return self

    def transform(self, X, **kwParameters):
        """
        Parameters:
            X (pandas.DataFrame): Input data. Contain variables, except target variable.
            
        Returns:
            (pandas.DataFrame): Transformed data with low variance features removed.
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
