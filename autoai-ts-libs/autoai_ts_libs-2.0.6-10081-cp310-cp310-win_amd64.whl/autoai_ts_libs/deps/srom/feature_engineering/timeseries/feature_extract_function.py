# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: feature_extract_function
   :synopsis: Additional functions for feature extraction.

.. moduleauthor:: SROM Team
"""

import numpy as np
import pandas as pd
from scipy.stats import linregress


def RateofChange(x):
    """
    Computes rate of change.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = x[~np.isnan(x)]
    if len(x) <= 1:
        return float(np.nan)
    return (x[len(x) - 1] - x[0]) / (len(x) * 1.0)


def SumofChange(x):
    """
    Computes sum of change.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = x[~np.isnan(x)]
    if len(x) <= 1:
        return float(np.nan)
    x = np.diff(x)
    return np.sum(x)


def AbsoluateSumofChange(x):
    """
    Computes absolute sum of change.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = x[~np.isnan(x)]
    if len(x) <= 1:
        return float(np.nan)
    x = np.diff(x)
    return np.sum(abs(x))


def trend_slop(x):
    """
    Computes trend slope.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = x[~np.isnan(x)]
    if len(x) <= 1:
        return float(np.nan)
    x1 = list(range(len(x)))
    y = np.array(list(x))
    try:
        slope, _, _, _, _ = linregress(x1, y)
    except:
        return float(np.nan)
    return slope


def abs_energy(x):
    """
    Computes absolute energy.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = np.asarray(x)
    return sum(x * x)


def mean_abs_change(x):
    """
    Computes mean absolute change.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    return np.mean(abs(np.diff(x)))


def mean_change(x):
    """
    Computes mean change.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    return np.mean(np.diff(x))


def mean_second_derivate_central(x):
    """
    Computes mean second derivate central.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    diff = (np.roll(x, 1) - 2 * np.array(x) + np.roll(x, -1)) / 2.0
    return np.mean(diff[1:-1])


def absolute_sum_of_changes(x):
    """
    Computes absolute sum of change.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    return np.sum(abs(np.diff(x)))


def count_above_mean(x):
    """
    Computes count above mean.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = np.asarray(x)
    m = np.mean(x)
    return np.where(x > m)[0].shape[0]


def count_below_mean(x):
    """
    Computes count below mean.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = np.asarray(x)
    m = np.mean(x)
    return np.where(x < m)[0].shape[0]


def last_location_of_maximum(x):
    """
    Computes last location of maximum.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = np.asarray(x)
    return 1.0 - np.argmax(x[::-1]) / len(x) if len(x) > 0 else np.NaN


def first_location_of_maximum(x):
    """
    Computes first location of maximum.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = np.asarray(x)
    return np.argmax(x) / len(x) if len(x) > 0 else np.NaN


def percentage_of_reoccurring_values_to_all_values(x):
    """
    Computes percentage of recurring values.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = pd.Series(x)

    if len(x) == 0:
        return np.nan

    value_counts = x.value_counts()
    return value_counts[value_counts > 1].sum() / len(x)


def corr_coefficient(x):
    """
    Computes coefficient.

    Parameters:
        x (numpy array, required): Array of integers.

    Return:
        integer
    """
    x = x[~np.isnan(x)]
    if len(x) <= 1:
        return float(np.nan)
    x1 = list(range(len(x)))
    y = np.array(list(x))
    try:
        _, _, r_value, _, _ = linregress(x1, y)
    except:
        return float(np.nan)
    return r_value


def delta_diff(x):
    """
    compute the difference
    Args:
        x (numpy array, required): array of numeric values
    Return:
        numeric value
    """
    return x[-1] - x[0]


def past_value(x):
    """
    return the head, i.e., oldest value in the window
    Args:
        x (numpy array, required): array of numeric values
    Return:
        numeric value
    """
    return x[0]
