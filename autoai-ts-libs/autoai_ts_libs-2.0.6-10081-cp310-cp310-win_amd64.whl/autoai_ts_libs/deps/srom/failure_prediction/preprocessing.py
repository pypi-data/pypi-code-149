# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: preprocessing
   :synopsis: Failure prediction preprocessing module.

.. moduleauthor:: SROM Team
"""
from datetime import datetime
import pandas as pd
import numpy as np
import time
from datetime import timedelta

from autoai_ts_libs.deps.srom.failure_prediction.time_sample import time_sampling, process_time_interval
from datetime import datetime


def generate_key_col(df, date_clm, asset_id_clm, interval=None, time_component=None):
    """
    Generates the key table. This table is used to generate the FPA table.

    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        date_clm (string, required): Column name for the date column in sensor table.
        asset_id_clm (string, required): Column name for the asset-id column in sensor table.
        interval (int/str/dict, optional): Intervals at which the key has to be generated. \
                - DICT: Interval can be specified in the following format \
                1 day --> \
                interval = {'weeks':0 \
                            'days': 1, \
                            'hours':0, \
                            'minutes':0, \
                            'seconds':0} \
                - STR: Interval can be specified in the following format \
                1 day --> \
                interval = '1D' \
                Refer to this link:  https://pandas.pydata.org/pandas-docs/stable/timeseries.html
        time_component (dict, optional): time component for each asset id in the generated key table. \
                For each pair in time_component, the key is the asset id, the value is the starting time component \
                for each asset in format "HH:MM:SS". \
                For example, if time_component is {"asset_1": "10:00:00"}, and assumingly the starting timestamp for \
                asset_1 is "01/01/2020 10:30:01", the output key table will start from "01/01/2020 10:00:00".

    Return:
        Dataframe containing the keys for the FPA table generation used in the FPA pipeline.
    """
    asset_id = []
    timestamp = []
    # check the datatype of 1st value in date_clm and apply either time based key column
    # or integer range based key column
    if isinstance(df.loc[df.index[0], date_clm], pd._libs.tslib.Timestamp):
        # if the first item in date_clm is timestamp
        for name, grp in df.groupby(asset_id_clm):
            tmp_sorted_date_clm = sorted(grp[date_clm])
            timestamp_st = min(tmp_sorted_date_clm).to_pydatetime()
            if isinstance(time_component, dict) and name in time_component:
                time_ = pd.to_datetime(time_component[name], infer_datetime_format=True)
                timestamp_st = timestamp_st.replace(hour=time_.hour)
                timestamp_st = timestamp_st.replace(minute=time_.minute)
                timestamp_st = timestamp_st.replace(second=time_.second)
            timestamp_end = max(tmp_sorted_date_clm).to_pydatetime()
            time_samples = time_sampling(timestamp_st, timestamp_end, interval)
            time_samples = list(time_samples["timestamp"])
            asset_id += [name] * len(time_samples)
            timestamp += time_samples
    elif isinstance(df.loc[df.index[0], date_clm], np.int64):
        # if the first item in date_clm is int
        for name, grp in df.groupby(asset_id_clm):
            tmp_sorted_date_clm = sorted(grp[date_clm])
            incident_st = min(tmp_sorted_date_clm)
            incident_end = max(tmp_sorted_date_clm)
            asset_time_samples = range(incident_st, incident_end + 1)
            asset_id += [name] * len(asset_time_samples)
            timestamp += asset_time_samples
    else:
        raise Exception(
            "The datatype of the sensor_data column should be datetime or int."
            "Convert the datatype to either format and remove all the Nans from"
            "dataframe"
        )

    # maintaning
    failure_keys = pd.DataFrame()
    failure_keys["asset_id"] = asset_id
    failure_keys["datetime"] = timestamp

    return failure_keys


def generate_failure_targets(
    failure_table,
    failure_keys,
    failure_detection_window_size,
    failure_asset_id,
    failure_date,
    failure_id,
    dead_period=None,
):
    """
    Generated the target tables for the failures based on the prediction window.

    Parameters:
        failure_table (pandas dataframe, required): Table having the asset failure information.
        failure_keys (pandas dataframe, required): Key table generated from the FPA pipeline.
        failure_detection_window_size  (dict/int/offset-str, required): Intervals at which the  \
                failure_detection_window_size has to be generated. \
                - DICT: Interval can be specified in the following format \
                1 day --> \
                interval = {'weeks':0, \
                            'days': 1, \
                            'hours':0, \
                            'minutes':0, \
                            'seconds':0} \
                - STR: Interval can be specified in the following format \
                1 day --> \
                interval = '1D' \
                Refer to this link: https://pandas.pydata.org/pandas-docs/stable/timeseries.html
        failure_asset_id (string, required): Column name for asset-id in failure data table.
        failure_date (string, required): Column name for date in failure data table.
        failure_id (string, required): Column name for failure id in failure data table.
        dead_period (dict/int/offset-str, optional): Some time right before the failure which \
                is considered invalid for analysis. This period will be flagged as -1.

    Return:
        Dataframe containing the target label column for all variables.
    """

    if dead_period is None:
        dead_period = 0

    # initializing another column in keys table
    failure_target_table = failure_keys
    failure_target_table["target_label"] = [0 for i in range(len(failure_keys))]

    # filtering failure table taking asset_id and date_clm
    failure_comp = failure_table[[failure_asset_id, failure_date, failure_id]]

    # Failure_date should be either in datetime or int in the failure table
    if (
        isinstance(
            failure_comp.loc[failure_comp.index[0], failure_date],
            pd._libs.tslib.Timestamp,
        )
        and isinstance(failure_detection_window_size, (int, dict, str))
        and isinstance(dead_period, (int, dict, str))
    ):
        # if the first item in date_clm is timestamp
        # processing time interval

        if dead_period == 0:
            dead_period = {
                "weeks": 0,
                "days": 0,
                "hours": 0,
                "minutes": 0,
                "seconds": 0,
            }

        failure_detection_window_size = process_time_interval(
            failure_detection_window_size
        )
        #         failure_detection_window_size = pd.tseries.frequencies.to_offset(failure_detection_window_size).delta

        dead_period = process_time_interval(dead_period)
    #         dead_period = pd.tseries.frequencies.to_offset(dead_period).delta

    elif (
        isinstance(failure_comp.loc[failure_comp.index[0], failure_date], np.int64)
        and isinstance(failure_detection_window_size, int)
        and isinstance(dead_period, int)
    ):
        # if the first item in date_clm is int

        failure_detection_window_size = failure_detection_window_size
        dead_period = dead_period

    else:
        raise TypeError(
            "The datatype of the date column failure table should be datetime or int."
            "Convert the datatype to either format and remove all the Nans from dataframe."
        )

    for i in range(len(failure_comp)):
        # for every failure, getting the asset_id, datetime and failure_id
        asset_id = failure_comp.loc[failure_comp.index[i], failure_asset_id]
        dead_period_end = failure_comp.loc[failure_comp.index[i], failure_date]
        failure_val = failure_comp.loc[failure_comp.index[i], failure_id]

        dead_period_start = dead_period_end - dead_period
        failure_detection_start = dead_period_start - failure_detection_window_size

        # inserting dead_period
        failure_target_table.loc[
            (failure_target_table["asset_id"] == asset_id)
            & (failure_target_table["datetime"] >= dead_period_start)
            & (failure_target_table["datetime"] < dead_period_end),
            "target_label",
        ] = -1

        # insert failure_target_label
        failure_target_table.loc[
            (failure_target_table["asset_id"] == asset_id)
            & (failure_target_table["datetime"] >= failure_detection_start)
            & (failure_target_table["datetime"] < dead_period_start),
            "target_label",
        ] = failure_val

    return failure_target_table


def generate_failure_targets_multiclass(
    failure_table,
    failure_keys,
    failure_detection_window_size,
    failure_asset_id,
    failure_date,
    failure_id,
):
    """
    Generated the target tables for the failures based on the prediction window.

    Parameters:
        failure_table (pandas dataframe, required): Table having the asset failure information.
        failure_keys (pandas dataframe, required): Key table generated from the in FPA pipeline.
        failure_detection_window_size  (dict/int/offset-str, required): Intervals at which the \
                failure_detection_window_size has to be generated. \
                - DICT: Interval can be specified in the following format \
                1 day --> \
                interval = {'weeks':0 \
                            'days': 1, \
                            'hours':0, \
                            'minutes':0, \
                            'seconds':0} \
                - STR: Interval can be specified in the following format \
                1 day --> \
                interval = '1D' \
                Refer to this link:  https://pandas.pydata.org/pandas-docs/stable/timeseries.html
        failure_asset_id (string, required): Column name for asset-id in failure data table.
        failure_date (string, required): Column name for date in failure data table.
        failure_id (string, required): Column name for failure id in failure data table.

    Return:
        Dataframe containing the target label column for all variables.
    """

    # initializing another column in keys table
    failure_target_table = failure_keys
    idlist = failure_table[failure_id].unique()
    for failid in idlist:
        failure_target_table["target_label_" + str(failid)] = [
            0 for i in range(len(failure_keys))
        ]

    # filtering failure table taking asset_id and date_clm
    failure_comp = failure_table[[failure_asset_id, failure_date, failure_id]]
    failure_comp = failure_comp

    # Failure_date should be either in datetime or int in the failure table
    if isinstance(
        failure_comp.loc[failure_comp.index[0], failure_date], pd._libs.tslib.Timestamp
    ):
        # if the first item in date_clm is timestamp
        # processing time interval
        failure_detection_window_size = process_time_interval(
            failure_detection_window_size
        )
        failure_detection_window_size = pd.tseries.frequencies.to_offset(
            failure_detection_window_size
        ).delta
    elif isinstance(failure_comp.loc[failure_comp.index[0], failure_date], np.int64):
        # if the first item in date_clm is int
        failure_detection_window_size = failure_detection_window_size
    else:
        raise Exception(
            "The datatype of the date column failure table should be datetime or int. \
                         Convert the datatype to either format and remove all the Nans from \
                         dataframe"
        )

    for i in range(len(failure_comp)):
        asset_id = failure_comp.loc[failure_comp.index[i], failure_asset_id]
        failure_detection_end = failure_comp.loc[failure_comp.index[i], failure_date]
        failure_val = failure_comp.loc[failure_comp.index[i], failure_id]
        failure_detection_start = failure_detection_end - failure_detection_window_size
        failure_target_table.loc[
            (failure_target_table["asset_id"] == asset_id)
            & (failure_target_table["datetime"] >= failure_detection_start)
            & (failure_target_table["datetime"] < failure_detection_end),
            "target_label_" + str(failure_val),
        ] = 1

    return failure_target_table


def merge_feature_and_failure(
    failure_target_table,
    sensor_features,
    failure_asset_id,
    failure_date,
    direction="backward",
):
    """
    Merge feature table and failure table. The failure_target_table and sensor_features should both have \
        failure_date and failure_asset_id columns.

    Parameters:
        failure_target_table (pandas dataframe, required): Table having the asset failure information.
        sensor_features (pandas dataframe, required): Table having the asset sensor feature information.
        failure_asset_id (string, required): Column name for asset-id in failure data table.
        failure_date (string, required): Column name for date in failure data table.
        direction (string, optional): the direction of merge_asof. one of 'backward', 'forward', 'nearest'
    Return:
        A merged Dataframe based on asset id and datetime
    """
    df1 = pd.DataFrame()
    for asset_id in failure_target_table[failure_asset_id].unique():
        df2 = pd.merge_asof(
            failure_target_table[failure_target_table[failure_asset_id] == asset_id],
            sensor_features[sensor_features[failure_asset_id] == asset_id],
            on=failure_date,
            direction=direction,
        )
        df1 = pd.concat([df1, df2], ignore_index=True)
    df1.rename(columns={failure_asset_id + "_x": failure_asset_id}, inplace=True)
    del df1[failure_asset_id + "_y"]
    return df1
