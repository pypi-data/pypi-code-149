# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: extreme_value_regressor
   :synopsis: Contains ExtremeValueRegressor class.

.. moduleauthor:: SROM Team
"""
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, RegressorMixin

class ExtremeValueRegressor(BaseEstimator, RegressorMixin):
    """
    An extreme value based regression model \
    that predict only if the value is an extreme.

    Parameters:
        aggr_type: The type of aggregation
    """

    def __init__(self, aggr_type = 'median'):
        self.aggr_type = aggr_type

    def fit(self, X, y):
        """
        Parameters:
            X_df (single variate pandas dataframe):
            y: Target values.
        """

        Xval = X.values
        l_val = np.quantile(Xval, 0.25)
        u_val = np.quantile(Xval, 0.75)
        self.l_val = l_val
        self.u_val = u_val

        l_val = np.quantile(y.values, 0.25)
        u_val = np.quantile(y.values, 0.75)
        lVals = []
        uVals = []
        for item in y.values:
            if item <= l_val:
                lVals.append(item)
            if item >= u_val:
                uVals.append(item)
        
        if self.aggr_type == 'median':
            self.l_val_pred = np.median(lVals)
            self.u_val_pred = np.median(uVals)
        elif self.aggr_type == 'mean':
            self.l_val_pred = np.mean(lVals)
            self.u_val_pred = np.mean(uVals)
        else:
            self.l_val_pred = np.NaN
            self.u_val_pred = np.NaN
        
        return self
    
    def predict(self, X):
        """
        Parameters:
            X (single variate pandas dataframe):
        """
        X = X.values
        _prediction = []
        for item in X:
            if item <= self.l_val:
                _prediction.append(self.l_val_pred)
            elif item >= self.u_val:
                _prediction.append(self.u_val_pred)
            else:
                _prediction.append(np.NaN)
        result = pd.DataFrame(np.array(_prediction))
        return result
