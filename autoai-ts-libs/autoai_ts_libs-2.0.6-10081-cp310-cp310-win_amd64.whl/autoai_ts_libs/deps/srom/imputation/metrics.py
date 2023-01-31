# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: metrics 
   :synopsis: metrics.

.. moduleauthor:: SROM Team
"""

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_squared_log_error,
    median_absolute_error,
)


from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
import numpy as np


def median_absolute_imputation_score(clf, X, y_true):
    """
    Parameters
    ----------
        clf: Imputer.
        X (pandas.Dataframe or numpy array): Data for imputation.
        y_true(numpy array): Target value for imputed column.
    
    Returns
    --------
        Median absolute score for imputed values.
    """
    y_pred = clf.transform(X)
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    y_non_true_index = np.where(~np.isnan(y_true))
    y_true = y_true[y_non_true_index]
    y_pred = y_pred[y_non_true_index]
    if len(y_pred) == len(y_true):
        _score = median_absolute_error(y_true, y_pred)
        return -1 * _score
    else:
        return np.NaN


def mean_squared_log_imputation_score(clf, X, y_true):
    """
    Parameters
    ----------
        clf: Imputer.
        X (pandas.Dataframe or numpy array): Data for imputation.
        y_true(numpy array): Target value for imputed column.
    
    Returns
    --------
        Mean squared log score for imputed values after applying the MinMaxScaler
    """
    y_pred = clf.transform(X)
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    y_non_true_index = np.where(~np.isnan(y_true))
    y_true = y_true[y_non_true_index]
    y_pred = y_pred[y_non_true_index]

    # Apply MinMaxScaler to ensure the positive values before having mean squared log score
    y_combined = np.concatenate((y_true, y_pred))
    scaler = MinMaxScaler()
    scaler.fit(y_combined.reshape(-1, 1))

    y_true = scaler.transform(y_true.reshape(-1, 1))
    y_pred = scaler.transform(y_pred.reshape(-1, 1))

    y_pred = y_pred.flatten()
    y_true = y_true.flatten()

    if len(y_pred) == len(y_true):
        _score = mean_squared_log_error(y_true, y_pred)
        return -1 * _score
    else:
        return np.NaN


def mean_absolute_imputation_score(clf, X, y_true):
    """
    Parameters
    ----------
        clf: Imputer.
        X (pandas.Dataframe or numpy array): Data for imputation.
        y_true(numpy array): Target value for imputed column.
    
    Returns
    --------
        Negative mean absolute score for imputed values.
    """
    y_pred = clf.transform(X)
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    y_non_true_index = np.where(~np.isnan(y_true))
    y_true = y_true[y_non_true_index]
    y_pred = y_pred[y_non_true_index]
    if len(y_pred) == len(y_true):
        _score = mean_absolute_error(y_true, y_pred)
        return -1 * _score
    else:
        return np.NaN


def mean_squared_imputation_score(clf, X, y_true):
    """
    Parameters
    ----------
        clf: Imputer.
        X (pandas.Dataframe or numpy array): Data for imputation.
        y_true(numpy array): Target value for imputed column.
    
    Returns
    --------
        Mean squared score for imputed values.
    """
    y_pred = clf.transform(X)
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    y_non_true_index = np.where(~np.isnan(y_true))
    y_true = y_true[y_non_true_index]
    y_pred = y_pred[y_non_true_index]
    if len(y_pred) == len(y_true):
        _score = mean_squared_error(y_true, y_pred, squared=True)
        return -1 * _score
    else:
        return np.NaN


def root_mean_squared_imputation_score(clf, X, y_true):
    """
    Parameters
    ----------
        clf: Imputer.
        X (pandas.Dataframe or numpy array): Data for imputation.
        y_true(numpy array): Target value for imputed column.
    
    Returns
    --------
        Negative root mean square score for imputed values.
    """
    y_pred = clf.transform(X)
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    y_non_true_index = np.where(~np.isnan(y_true))
    y_true = y_true[y_non_true_index]
    y_pred = y_pred[y_non_true_index]
    if len(y_pred) == len(y_true):
        _score = mean_squared_error(y_true, y_pred, squared=False)
        return -1 * _score
    else:
        return np.NaN


def r2_imputation_score(clf, X, y_true):
    """
    Parameters
    ----------
        clf: Imputer.
        X (pandas.Dataframe or numpy array): Data for imputation.
        y_true(numpy array): Target value for imputed column.
    
    Returns
    --------
        R2 imputation score for imputed values.  
    """
    y_pred = clf.transform(X)
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    y_non_true_index = np.where(~np.isnan(y_true))
    y_true = y_true[y_non_true_index]
    y_pred = y_pred[y_non_true_index]
    if len(y_pred) == len(y_true):
        _score = r2_score(y_true, y_pred)
        return _score
    else:
        return np.NaN
