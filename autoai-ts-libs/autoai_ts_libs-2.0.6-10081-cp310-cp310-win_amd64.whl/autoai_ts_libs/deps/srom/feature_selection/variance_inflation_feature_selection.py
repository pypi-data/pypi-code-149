# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: variance_inflation_feature_selection
   :synopsis: Contains class which provides functionalities \
       for variance inflation based feature selection.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


class VarianceInflationFeatureSelection(BaseEstimator, TransformerMixin):
    """
    A method to remove multicollinearity from input data frame. \
    https://en.wikipedia.org/wiki/Multicollinearity \
    Input is a dataframe that contain variables, except target variable. \
    The tranform function removes multi-correlated variables. \
    https://beckmw.wordpress.com/2013/02/05/collinearity-and-stepwise-vif-selection/
    """

    def __init__(self, vif_threshold_value=10):
        """
        Parameters:
            vif_threshold_value: A threshold to remove the variable with high correlation. \
                Defaults to 10.
        """
        self.vif_threshold_value = vif_threshold_value
        self.vif = None  # this argument store the name of removed variables
        self.selected_columns = None
        self.total_columns = 0

    def _variance_inflation_factor(self, exogs, data):
        vif_list = []

        # form input data for each exogenous variable
        for exog in exogs:
            not_exog = [i for i in exogs if i != exog]
            X, y = data[not_exog], data[exog]

            # extract r-squared from the fit
            r_squared = LinearRegression().fit(X, y).score(X, y)

            # calculate VIF
            vif = 1 / (1 - r_squared)
            vif_list.append(vif)
        return vif_list

    def fit(self, X, y=None, **kwParameters):
        """
        Parameters:
            X (pandas.DataFrame): Input data. Contain variables, except target variable.

        Returns:
            (pandas.DataFrame): Transformed data with multicollinearity removed.
        """

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

        if X.shape[1] == 0:
            self.total_columns = 1
            self.selected_columns = list(X.columns)
            return self

        self.total_columns = X.shape[1]
        X = X.copy()
        X["intercept"] = np.ones(X.shape[0])
        variables = list(X.columns)
        v_name = []
        i_value = []

        dropped = True
        while dropped is True:
            dropped = False
            vif = self._variance_inflation_factor(variables, X)

            max_vif = max(vif)
            maxloc = vif.index(max_vif)
            if max_vif > self.vif_threshold_value:
                v_name.append(X[variables].columns[maxloc])
                i_value.append(max_vif)
                del variables[maxloc]
                dropped = True

        self.vif = pd.DataFrame()
        self.vif["removed_variable"] = v_name
        self.vif["vif_value"] = i_value

        # remove the intercept we added
        del variables[len(variables) - 1]
        self.selected_columns = variables
        # return the data frame
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
