# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: extreme_value_quantile_regressor
   :synopsis: Contains ExtremeValueQuantileRegressor class.

.. moduleauthor:: SROM Team
"""
import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin

class ExtremeValueQuantileRegressor(BaseEstimator, RegressorMixin):
    """
    An extreme value based quantile regression model \
    that predict only if the value is an extreme.

    Parameters:
        aggr_type: The type of aggregation.
    """
    
    def __init__(self, aggr_type = 'mean'):        
        self.aggr_type = aggr_type

    def fit(self, X, y):
        """
        Parameters:
            X_df (single variate pandas dataframe): 
            y : Target values.
        """

        Xval = X.values
        l_val = np.quantile(Xval, 0.25)
        u_val = np.quantile(Xval, 0.75)
        self.l_val = l_val
        self.u_val = u_val
        self.l_min = np.min(Xval)
        self.u_max = np.max(Xval)

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

        self.l_val_min = np.min(lVals)
        self.l_val_max = np.max(lVals)
        self.u_val_min = np.min(uVals)
        self.u_val_max = np.max(uVals)
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
                diff = (self.l_val-item)/(self.l_val-self.l_min)
                pVal = self.l_val_max - ((self.l_val_max-self.l_val_min)*diff)
                _prediction.append(pVal[0])
            elif item >= self.u_val:
                diff = (item-self.u_val)/(self.u_max-self.u_val)
                pVal = self.u_val_min + ((self.u_val_max-self.u_val_min)*diff)
                _prediction.append(pVal[0])
            else:
                _prediction.append(np.NaN)
        result = np.array(_prediction)
        return result
