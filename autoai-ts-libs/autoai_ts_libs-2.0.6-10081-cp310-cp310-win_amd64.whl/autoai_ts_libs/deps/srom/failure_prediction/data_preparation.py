# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: data_preparation
   :synopsis: Data Preparation.

.. moduleauthor:: SROM Team
"""
import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.failure_prediction.time_sample import process_time_interval
from scipy.spatial.distance import pdist, squareform


def _min_tbf_flag(
    failure_table, min_time_between_failure, failure_date, failure_asset_id
):
    """
    Validate and correct the failure table if the failure does not have \
    appropriate min_time_between_failure.Minimum time between failure can be \
    defined as the minimum time to be consider before an asset failure after \
    the previous failure.

    Parameters:
        failure_table (pandas DataFrame, required): Failure table consisting of the \
                    columns asset_id, datetime, and failure_type.
        min_time_between_failure (dict/str, required): Interval which provides value \
                    for the mean time between failures. \
                    - DICT: Interval can be specified in the following format. \
                    1 day --> \
                    interval = {'weeks':0 \
                                'days': 1, \
                                'hours':0, \
                                'minutes':0, \
                                'seconds':0} \
                    - STR: Interval can be specified in the following format. \
                    1 day --> \
                    interval = '1D' \
                    Refer to this link: \
                        https://pandas.pydata.org/pandas-docs/stable/timeseries.html 
        failure_date (str, required): Column name for the datetime in failure_table.
        failure_asset_id (str, required): Column name for the asset_id in failure_table.

    Returns:
        failure_table (pandas DataFrame): Table flagged with minimum time between \
            failures for each asset.
    """
    failure_table["valid_failure"] = 0
    # Failure_date should be either in datetime or int in the failure table
    if isinstance(
        failure_table.loc[failure_table.index[0], failure_date],
        pd._libs.tslib.Timestamp,
    ):
        # if the first item in date_clm is timestamp
        # processing time interval
        min_time_between_failure = process_time_interval(min_time_between_failure)
        gap_between_failures = pd.tseries.frequencies.to_offset(
            min_time_between_failure
        )
    elif isinstance(failure_table.loc[failure_table.index[0], failure_date], np.int64):
        # if the first item in date_clm is int
        gap_between_failures = min_time_between_failure
    else:
        raise Exception(
            "The datatype of the date column failure table should be datetime or int. \
Convert the datatype to either format and remove all the Nans from dataframe"
        )

    for name, grp in failure_table.groupby(failure_asset_id):
        recent_failure = min(sorted(grp[failure_date])).to_pydatetime()
        for j in range(len(grp)):
            valid_failure_gap = (
                recent_failure == grp.loc[grp.index[j], failure_date]
            ) or (
                (recent_failure + gap_between_failures)
                <= grp.loc[grp.index[j], failure_date]
            )
            if not valid_failure_gap:
                failure_table.loc[
                    (failure_table[failure_asset_id] == name)
                    & (
                        failure_table[failure_date]
                        == grp.loc[grp.index[j], failure_date]
                    ),
                    "valid_failure",
                ] = 1
            else:
                recent_failure = grp.loc[grp.index[j], failure_date]

    return failure_table


def min_tbf_check(
    failure_table, min_time_between_failure, failure_date, failure_asset_id
):
    """
    Validate and correct the failure table if the failure does not have \
    appropriate min_time_between_failure. Minimum time between failure can be \
    defined as the minimum time to be consider before an asset failure after \
    the previous failure.

    Parameters:
        failure_table (pandas DataFrame, required): failure table consisting of the \
                    columns asset_id, datetime, and failure_type.
        min_time_between_failure (dict/str, required): Interval which provides value \
                    for the mean time between failures. \
                    - DICT: Interval can be specified in the following format. \
                    1 day --> \
                    interval = {'weeks':0 \
                                'days': 1, \
                                'hours':0, \
                                'minutes':0, \
                                'seconds':0} \
                    - STR: Interval can be specified in the following format. \
                    1 day --> \
                    interval = '1D' \
                    Refer to this link: \
                        https://pandas.pydata.org/pandas-docs/stable/timeseries.html
        failure_date (str, required): Column name for the datetime in failure_table.
        failure_asset_id (str, required): Column name for the asset_id in failure_table.

    Returns:
        check (Boolean): True is min_tbf is not satisfied.
    """

    failure_table = _min_tbf_flag(
        failure_table, min_time_between_failure, failure_date, failure_asset_id
    )
    check = False
    if len(failure_table[failure_table["valid_failure"] == 1]) > 0:
        check = True

    return check


def min_tbf_correction(
    failure_table, min_time_between_failure, failure_date, failure_asset_id
):
    """
    Validate and correct the failure table if the failure is the does not have \
    appropriate min_time_between_failure.Minimum time between failure can be \
    defined as the minimum time to be consider before an asset failure after \
    the previous failure.

    Parameters:
        failure_table (pandas DataFrame, required): failure table consisting of the \
                    columns asset_id, datetime, and failure_type.
        min_time_between_failure (dict/str, required): Interval which provides value \
                    for the mean time between failures. \
                    - DICT: Interval can be specified in the following format. \
                    1 day --> \
                    interval = {'weeks':0 \
                                'days': 1, \
                                'hours':0, \
                                'minutes':0, \
                                'seconds':0} \
                    - STR: Interval can be specified in the following format. \
                    1 day --> \
                    interval = '1D' \
                    Refer to this link: \
                        https://pandas.pydata.org/pandas-docs/stable/timeseries.html
        failure_date (str, required): Column name for the datetime in failure_table.
        failure_asset_id (str, required): Column name for the asset_id in failure_table.

    Returns:
        failure_table_corrected (pandas DataFrame): Table corrected with minimum time \
                    between failures.
    """

    failure_table = _min_tbf_flag(
        failure_table, min_time_between_failure, failure_date, failure_asset_id
    )
    failure_table_corrected = failure_table[failure_table["valid_failure"] == 0]
    failure_table_corrected = failure_table_corrected.drop(["valid_failure"], axis=1)

    return failure_table_corrected


def check_datetime_column_format(df, datetime_col, datetime_col_format=None):
    """
    Checks whether the datetime column in the given dateframe is in the datatime format.
    """
    if datetime_col_format is None:
        if isinstance(df.loc[df.index[0], datetime_col], pd._libs.tslib.Timestamp):
            pass
        else:
            raise Exception(
                "The date_time column in your table is not in datetime format.\
Convert the datetie column to datetime format or provide the `datetime_col_format` in the function call. "
            )
    else:
        df[datetime_col] = pd.to_datetime(df[datetime_col], format=datetime_col_format)

    return df


def failure_classes(failure_table, failure_id):
    """
    Checks how many types of failures are identified.
    """
    num_classes = len(failure_table[failure_id].unique())

    if num_classes == 1:
        type = "two-class"
    elif num_classes > 1:
        type = "multi-class"
    else:
        raise Exception(
            "The number of failures is 0 in the failure table. Should be \
more than 1 type of class."
        )

    return num_classes, type


def data_prevalidation(
    sensor_table,
    sensor_date,
    sensor_date_format,
    failure_table,
    failure_date,
    failure_date_format,
    failure_asset_id,
    failure_id,
    min_time_between_failure,
):
    """
    Function for validating the data in Failure Prediction module. This function should be \
    used before running failure prediction notebook/module.
    """
    sensor_table = check_datetime_column_format(
        sensor_table, sensor_date, datetime_col_format=sensor_date_format
    )
    failure_table = check_datetime_column_format(
        failure_table, failure_date, datetime_col_format=failure_date_format
    )
    (num_class, classification_type) = failure_classes(failure_table, failure_id)

    check = min_tbf_check(
        failure_table, min_time_between_failure, failure_date, failure_asset_id
    )

    ## provide warning if the check returns True and inform the user that we are
    ## applying the min_tfb correction.

    if check:
        failure_table = min_tbf_correction(
            failure_table, min_time_between_failure, failure_date, failure_asset_id
        )
    else:
        raise Exception(
            "Minimum time betwen failure is not satisfied. Provide \
`min_time_between_failure` variable some value."
        )

    return sensor_table, failure_table, num_class, classification_type


def dcov(X, Y):
    """
    Computes the distance covariance between matrices X and Y.
    """
    n = X.shape[0]
    XY = np.multiply(X, Y)
    cov = np.sqrt(XY.sum()) / n
    return cov


def dvar(X):
    """
    Computes the distance variance of a matrix X.
    """
    return np.sqrt(np.sum(X**2 / X.shape[0] ** 2))


def cent_dist(X):
    """
    Computes the pairwise euclidean distance between rows of X and centers \
    each cell of the distance matrix with row mean, column mean and grand mean.
    """
    M = squareform(pdist(X))  # distance matrix
    rmean = M.mean(axis=1)
    cmean = M.mean(axis=0)
    gmean = rmean.mean()
    R = np.tile(rmean, (M.shape[0], 1)).transpose()
    C = np.tile(cmean, (M.shape[1], 1))
    G = np.tile(gmean, M.shape)
    CM = M - R - C + G
    return CM


def dcor(X, Y):
    """
    Computes the distance correlation between two matrices X and Y. \
    X and Y must have the same number of rows.
    """
    if X.shape[0] != Y.shape[0]:
        raise ValueError("X.shape[0] is not equal to Y.shape[0].")

    A = cent_dist(X)
    B = cent_dist(Y)

    dcov_AB = dcov(A, B)
    dvar_A = dvar(A)
    dvar_B = dvar(B)

    dcor = 0.0
    if dvar_A > 0.0 and dvar_B > 0.0:
        dcor = dcov_AB / np.sqrt(dvar_A * dvar_B)

    return 1 - dcor
