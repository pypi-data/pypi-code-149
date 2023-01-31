# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: rolling_window_feature_extraction
   :synopsis: Failure prediction preprocessing module.

.. moduleauthor:: SROM Team
"""
import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.feature_engineering.timeseries.functions import (
    rate_of_change,
    corr_coefficient,
    first_location_of_maximum,
    last_location_of_maximum,
    count_below_mean,
    count_above_mean,
    mean_second_derivate_central,
    mean_change,
    mean_abs_change,
    abs_energy,
    trend_slop,
    sum_of_change,
    absoluate_sum_of_changes,
    delta_diff,
    past_value,
)
from sklearn.base import BaseEstimator, TransformerMixin


def simple_summary_statistics(
    df,
    rolling_window_size,
    variable_clms,
    asset_id_clm,
    date_clm,
    date_clm_format=None,
    min_periods=None,
    aggregation_type="time",
    aggregation_methods=None,
):
    """
    Extracts the rolling window aggregation features.

    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        aggregation_methods (string:list, required): It is a list of aggregation methods to be \
                used for feature extraction.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days. \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds'). \
                        A number followed by a character denoting the resolution of the window. \
                        (s-seconds, m-minutes,  h-hours, d-days, w-weeks) \
        variable_clms (string:list, required): List of column names for feature extraction \
            from sensor table.
        asset_id_clm (string, required): Column name for the asset-id column in sensor table.
        date_clm (string, required): Column name for the date column in sensor table.
        date_clm_format (datetime, optional): Format of the string containing date in sensor \
            table. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        aggregation_type (string, optional): The string denoting the aggregation types. \
                Read pandas-rolling documentation for more info. For missing values monitoring, use \
                `min_periods` parameter in `rolling()`. \
                3 types of `aggregation_type`: \
                    - 'time': Rolling window based on timestamp. \
                    - 'record': Rolling window based on pandas rows/record. \
                    - 'incident': Rolling windows based on non-time events or incidents.
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
            the rolling value. This is advanced option to be used during irregular sampling.

    Return: 
        dataframe: Table with the extracted features in the following format. \
            * <aggregation method> _ <history window size> _ <sensor name> \
            example: mean_30_sensor_1 \
                     (for sensor_1)
    """

    # check if date column is not int, date_clm_format should be given
    if df.dtypes[date_clm] != "int64":
        if date_clm_format is None:
            raise Exception(
                "The '"
                + str(date_clm)
                + "' column should either be in shifts or timestamps. \
Either provide integer values for shifts or datetime.datetime values for timestamps in '"
                + str(date_clm)
                + "' column.\
If the '"
                + str(date_clm)
                + "' column is timestamps but strings format, specify the format of date using \
'date_clm_format' variable."
            )
        else:
            # apply datetime conversion to date_clm
            df[date_clm] = pd.to_datetime(df[date_clm], format=date_clm_format)

    if aggregation_methods is None:
        aggregation_methods = ["mean", "max", "min", "median", "std", "sum", "count"]

    # creating new datafram
    df = df[[asset_id_clm, date_clm] + variable_clms]
    sensor_features = df[[asset_id_clm, date_clm] + variable_clms]

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    # looping over each aggregation type
    for aggr in aggregation_methods:
        col_names = []
        for i in variable_clms:
            col_names.append(i + "__" + aggr + "__" + str(rolling_window_size))

        # looping over each asset group
        temp_table = pd.DataFrame(columns=[col_names])
        for name, grp in df.groupby(asset_id_clm):
            del grp[asset_id_clm]
            tmp = grp.set_index(date_clm)
            tmp = tmp.sort_index()
            if aggregation_type == "time" or aggregation_type == "record":
                pass
            elif aggregation_type == "incident":
                # converting int to timestamp for handling missing info
                tmp["date"] = pd.to_datetime(tmp.index, unit="s")
                index_retain = tmp.index
                tmp = tmp.set_index("date")
            else:
                raise Exception("Please provide a valid aggregation_type.")

            if aggr == "mean":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).mean()
            elif aggr == "max":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).max()
            elif aggr == "min":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).min()
            elif aggr == "std":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).std()
            elif aggr == "sum":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).sum()
            elif aggr == "count":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).count()
            elif aggr == "median":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).median()
            else:
                raise Exception("Invalid type in 'aggregation_methods'.")

            if aggregation_type == "incident":
                tmp.index = index_retain
            tmp.columns = col_names
            tmp.reset_index(inplace=True)
            tmp[asset_id_clm] = name

            try:
                temp_table = pd.concat([temp_table, tmp])
            except Exception:
                temp_table = tmp

        # merging each aggregation type result to the sensor_features table
        sensor_features = pd.merge(
            sensor_features, temp_table, on=[asset_id_clm, date_clm], how="left"
        )
    # maintaining column names in the sensor_features table
    sensor_features = sensor_features.rename(
        columns={asset_id_clm: "asset_id", date_clm: "datetime"}
    )

    sensor_features["datetime"] = sensor_features["datetime"].astype(str)
    return sensor_features


def higher_order_summary_statistics(
    df,
    rolling_window_size,
    variable_clms,
    asset_id_clm,
    date_clm,
    date_clm_format=None,
    min_periods=None,
    aggregation_type="time",
    aggregation_methods=None,
):
    """
    Extracts the rolling window aggregation features.

    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        aggregation_methods (string:list, required):  It is a list of aggregation methods to be \
                used for feature extraction.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter). eg. '30D' - 30 days. \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                        A number followed by a character denoting the resolution of the window. \
                        (s-seconds, m-minutes,  h-hours, d-days, w-weeks).
        variable_clms (list of strings, required): List of column names for feature extraction \
                from sensor table.
        asset_id_clm (string, required): Name of the asset-id column in sensor table.
        date_clm (string, required): Name of the date column in sensor table.
        date_clm_format (datetime, optional): Format of the string containing date in sensor \
                table. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        aggregation_type (string, optional): The string denoting the aggregation types. \
                Read pandas-rolling documentation for more info. For missing values monitoring, use \
                `min_periods` parameter in `rolling()`. \
                3 types of `aggregation_type`: \
                    - 'time': Rolling window based on timestamp. \
                    - 'record': Rolling window based on pandas rows/record. \
                    - 'incident': Rolling windows based on non-time events or incidents. \
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
            the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
            * <aggregation method> _ <history window size> _ <sensor name> \
            example: mean_30_sensor_1 \
                     (for sensor_1).
    """

    # check if date column is not int, date_clm_format should be given
    if df.dtypes[date_clm] != "int64":
        if date_clm_format is None:
            raise Exception(
                "The '"
                + str(date_clm)
                + "' column should either be in shifts or timestamps. \
Either provide integer values for shifts or datetime.datetime values for timestamps in '"
                + str(date_clm)
                + "' column.\
If the '"
                + str(date_clm)
                + "' column is timestamps but strings format, specify the format of date using \
'date_clm_format' variable."
            )
        else:
            # apply datetime conversion to date_clm
            df[date_clm] = pd.to_datetime(df[date_clm], format=date_clm_format)

    if aggregation_methods is None:
        aggregation_methods = [
            "sum",
            "skew",
            "kurt",
            "quantile_25",
            "quantile_75",
            "quantile_range",
        ]

    # creating new datafram
    df = df[[asset_id_clm, date_clm] + variable_clms]
    sensor_features = df[[asset_id_clm, date_clm] + variable_clms]

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    # looping over each aggregation type
    for aggr in aggregation_methods:
        col_names = []
        for i in variable_clms:
            col_names.append(i + "__" + aggr + "__" + str(rolling_window_size))

        # looping over each asset group
        temp_table = pd.DataFrame(columns=[col_names])
        for name, grp in df.groupby(asset_id_clm):
            del grp[asset_id_clm]
            tmp = grp.set_index(date_clm)
            tmp = tmp.sort_index()
            if aggregation_type == "time" or aggregation_type == "record":
                pass
            elif aggregation_type == "incident":
                # converting int to timestamp for handling missing info
                tmp["date"] = pd.to_datetime(tmp.index, unit="s")
                index_retain = tmp.index
                tmp = tmp.set_index("date")
            else:
                raise Exception("Please provide a valid aggregation_type.")

            if aggr == "sum":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).sum()
            elif aggr == "skew":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).skew()
            elif aggr == "kurt":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).kurt()
            elif aggr == "quantile_25":
                tmp = tmp.rolling(
                    rolling_window_size, min_periods=min_periods
                ).quantile(0.25)
            elif aggr == "quantile_75":
                tmp = tmp.rolling(
                    rolling_window_size, min_periods=min_periods
                ).quantile(0.75)
            elif aggr == "quantile_range":
                tmp1 = tmp.rolling(
                    rolling_window_size, min_periods=min_periods
                ).quantile(0.25)
                tmp2 = tmp.rolling(
                    rolling_window_size, min_periods=min_periods
                ).quantile(0.75)
                tmp = tmp2 - tmp1
            else:
                raise Exception("Invalid type in 'aggregation_methods'.")

            if aggregation_type == "incident":
                tmp.index = index_retain
            tmp.columns = col_names
            tmp.reset_index(inplace=True)
            tmp[asset_id_clm] = name

            try:
                temp_table = pd.concat([temp_table, tmp])
            except Exception:
                temp_table = tmp

        # merging each aggregation type result to the sensor_features table
        sensor_features = pd.merge(
            sensor_features, temp_table, on=[asset_id_clm, date_clm], how="left"
        )
    # maintaining column names in the sensor_features table
    sensor_features = sensor_features.rename(
        columns={asset_id_clm: "asset_id", date_clm: "datetime"}
    )
    return sensor_features


def advance_summary_statistics(
    df,
    rolling_window_size,
    variable_clms,
    asset_id_clm,
    date_clm,
    date_clm_format=None,
    min_periods=None,
    aggregation_type="time",
    aggregation_methods=None,
):
    """
    Extracts the rolling window aggregation features.

    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        aggregation_methods (string:list, required):  It is a list of aggregation methods to be \
                used for feature extraction.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days. \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                        A number followed by a character denoting the resolution of the window. \
                        (s-seconds, m-minutes,  h-hours, d-days, w-weeks). \
        variable_clms (string:list, required): List of column names for feature extraction \
                from sensor table.
        asset_id_clm (string, required): Name of the asset-id column in sensor table.
        date_clm (string, required): Name of the date column in sensor table.
        date_clm_format (datetime, optional): Format of the string containing date in sensor \
                table. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        aggregation_type (string, optional): The string denoting the aggregation types. \
                Read pandas-rolling documentation for more info. For missing values monitoring, use \
                `min_periods` parameter in `rolling()`. \
                    3 types of `aggregation_type`: \
                        - 'time': Rolling window based on timestamp. \
                        - 'record': Rolling window based on pandas rows/record. \
                        - 'incident': Rolling windows based on non-time events or incidents.
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
            the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
            * <aggregation method> _ <history window size> _ <sensor name>  \
            example: mean_30_sensor_1   \
                    (for sensor_1).
    """

    # check if date column is not int, date_clm_format should be given
    if df.dtypes[date_clm] != "int64":
        if date_clm_format is None:
            raise Exception(
                "The '"
                + str(date_clm)
                + "' column should either be in shifts or timestamps. \
Either provide integer values for shifts or datetime.datetime values for timestamps in '"
                + str(date_clm)
                + "' column.\
If the '"
                + str(date_clm)
                + "' column is timestamps but strings format, specify the format of date using \
'date_clm_format' variable."
            )
        else:
            # apply datetime conversion to date_clm
            df[date_clm] = pd.to_datetime(df[date_clm], format=date_clm_format)

    if aggregation_methods is None:
        aggregation_methods = [
            "rate_of_change",
            "sum_of_change",
            "absoluate_sum_of_changes",
            "trend_slop",
            "abs_energy",
            "mean_abs_change",
            "mean_change",
            "mean_second_derivate_central",
            "count_above_mean",
            "count_below_mean",
            "last_location_of_maximum",
            "first_location_of_maximum",
            "corr_coefficient",
        ]

    # creating new datafram
    df = df[[asset_id_clm, date_clm] + variable_clms]
    sensor_features = df[[asset_id_clm, date_clm] + variable_clms]

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    # looping over each aggregation type
    for aggr in aggregation_methods:
        col_names = []
        for i in variable_clms:
            col_names.append(i + "__" + aggr + "__" + str(rolling_window_size))

        # looping over each asset group
        temp_table = pd.DataFrame(columns=[col_names])
        for name, grp in df.groupby(asset_id_clm):
            del grp[asset_id_clm]
            tmp = grp.set_index(date_clm)
            tmp = tmp.sort_index()
            if aggregation_type == "time" or aggregation_type == "record":
                pass
            elif aggregation_type == "incident":
                # converting int to timestamp for handling missing info
                tmp["date"] = pd.to_datetime(tmp.index, unit="s")
                index_retain = tmp.index
                tmp = tmp.set_index("date")
            else:
                raise Exception("Please provide a valid aggregation_type.")

            if aggr == "rate_of_change":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: rate_of_change(x)
                )
            elif aggr == "sum_of_change":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: sum_of_change(x)
                )
            elif aggr == "absoluate_sum_of_changes":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: absoluate_sum_of_changes(x)
                )
            elif aggr == "trend_slop":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: trend_slop(x)
                )
            elif aggr == "abs_energy":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: abs_energy(x)
                )
            elif aggr == "mean_abs_change":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: mean_abs_change(x)
                )
            elif aggr == "mean_change":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: mean_change(x)
                )
            elif aggr == "mean_second_derivate_central":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: mean_second_derivate_central(x)
                )
            elif aggr == "count_above_mean":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: count_above_mean(x)
                )
            elif aggr == "count_below_mean":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: count_below_mean(x)
                )
            elif aggr == "last_location_of_maximum":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: last_location_of_maximum(x)
                )
            elif aggr == "first_location_of_maximum":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: first_location_of_maximum(x)
                )
            elif aggr == "corr_coefficient":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: corr_coefficient(x)
                )
            elif aggr == "delta_diff":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: delta_diff(x)
                )
            elif aggr == "past_value":
                tmp = tmp.rolling(rolling_window_size, min_periods=min_periods).apply(
                    lambda x: past_value(x)
                )

            else:
                raise Exception("Invalid type in 'aggregation_methods'.")

            if aggregation_type == "incident":
                tmp.index = index_retain
            tmp.columns = col_names
            tmp.reset_index(inplace=True)
            tmp[asset_id_clm] = name

            try:
                temp_table = pd.concat([temp_table, tmp])
            except Exception:
                temp_table = tmp

        # merging each aggregation type result to the sensor_features table
        sensor_features = pd.merge(
            sensor_features, temp_table, on=[asset_id_clm, date_clm], how="left"
        )
    # maintaining column names in the sensor_features table
    sensor_features = sensor_features.rename(
        columns={asset_id_clm: "asset_id", date_clm: "datetime"}
    )
    return sensor_features


def correlation_statistics(
    df,
    rolling_window_size,
    variable_clms,
    asset_id_clm,
    date_clm,
    date_clm_format=None,
    min_periods=None,
    aggregation_type="time",
):
    """
    Extracts the rolling window aggregation features.

    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days. \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                    A number followed by a character denoting the resolution of the window. \
                    (s-seconds, m-minutes,  h-hours, d-days, w-weeks).
        variable_clms (string:list, required): List of column names for feature extraction \
            from sensor table.
        asset_id_clm (string, required): Name of the asset-id column in sensor table.
        date_clm (string, required): Name of the date column in sensor table.
        date_clm_format (datetime, required): Format of the string containing date in sensor \
                table. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        aggregation_type (string, optional): The string denoting the aggregation types. \
                Read pandas-rolling documentation for more info. For missing values monitoring, use \
                `min_periods` parameter in `rolling()`. \
                    3 types of `aggregation_type`: \
                        - 'time': Rolling window based on timestamp. \
                        - 'record': Rolling window based on pandas rows/record. \
                        - 'incident': Rolling windows based on non-time events or incidents.
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
            the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
            * <feature1>__<feature2>...__<correlation>__<rolling_window_size> \
                e.g. f1__f2__correlation__3D \
                for features f1,f2 in df_variables.
    """

    # check if date column is not int, date_clm_format should be given
    if df.dtypes[date_clm] != "int64":
        if date_clm_format is None:
            raise Exception(
                "The '"
                + str(date_clm)
                + "' column should either be in shifts or timestamps. \
            Either provide integer values for shifts or datetime.datetime values for timestamps in '"
                + str(date_clm)
                + "' column.\
            If the '"
                + str(date_clm)
                + "' column is timestamps but strings format, specify the format of date using \
            'date_clm_format' variable."
            )
        else:
            # apply datetime conversion to date_clm
            df[date_clm] = pd.to_datetime(df[date_clm], format=date_clm_format)

    # creating new datafram
    df = df[[asset_id_clm, date_clm] + variable_clms]
    sensor_features = df[[asset_id_clm, date_clm] + variable_clms]

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    # looping over each aggregation type
    col_names = []
    for i in range(len(variable_clms)):
        for j in range(i + 1, len(variable_clms)):
            col_names.append(
                variable_clms[i]
                + "__"
                + variable_clms[j]
                + "__"
                + "correlation"
                + "__"
                + str(rolling_window_size)
            )

    # looping over each asset group
    temp_table = pd.DataFrame(columns=[col_names])

    for name, grp in df.groupby(asset_id_clm):
        del grp[asset_id_clm]
        tmp = grp.set_index(date_clm)
        tmp = tmp.sort_index()
        if aggregation_type == "time" or aggregation_type == "record":
            pass
        elif aggregation_type == "incident":
            # converting int to timestamp for handling missing info
            tmp["date"] = pd.to_datetime(tmp.index, unit="s")
            index_retain = tmp.index
            tmp = tmp.set_index("date")
        else:
            raise Exception("Please provide a valid aggregation_type.")

        numRow, numCol = tmp.shape
        corX = tmp.rolling(rolling_window_size, min_periods=min_periods).corr()

        finalRes = []
        for row_i in range(numRow):
            finalRes.append(
                corX.iloc[row_i * numCol : (row_i * numCol + numCol), :].values[
                    np.triu_indices(numCol, k=1)
                ]
            )

        tmp_res = pd.DataFrame(finalRes)
        tmp_res.index = tmp.index

        if aggregation_type == "incident":
            tmp_res.index = index_retain

        tmp_res.columns = col_names
        tmp_res.reset_index(inplace=True)
        tmp_res[asset_id_clm] = name

        try:
            temp_table = pd.concat([temp_table, tmp_res])
        except Exception:
            temp_table = tmp_res

    # merging each aggregation type result to the sensor_features table
    sensor_features = pd.merge(
        sensor_features, temp_table, on=[asset_id_clm, date_clm], how="left"
    )

    # maintaining column names in the sensor_features table
    sensor_features = sensor_features.rename(
        columns={asset_id_clm: "asset_id", date_clm: "datetime"}
    )
    return sensor_features


def covariance_statistics(
    df,
    rolling_window_size,
    variable_clms,
    asset_id_clm,
    date_clm,
    date_clm_format=None,
    min_periods=None,
    aggregation_type="time",
):
    """
Extracts the rolling window aggregation features.       

    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days . \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                    A number followed by a character denoting the resolution of the window. \
                    (s-seconds, m-minutes,  h-hours, d-days, w-weeks) .
        variable_clms (string:list, required): List of column names for feature extraction \
            from sensor table.
        asset_id_clm (string, required): Name of the asset-id column in sensor table.
        date_clm (string, required): Name of the date column in sensor table.
        date_clm_format (datetime, optional): Format of the string containing date in sensor \
            table. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        aggregation_type (string, optional): The string denoting the aggregation types. \
                Read pandas-rolling documentation for more info. For missing values monitoring, use \
                `min_periods` parameter in `rolling()`. \
                    3 types of `aggregation_type`: \
                        - 'time': Rolling window based on timestamp. \
                        - 'record': Rolling window based on pandas rows/record. \
                        - 'incident': Rolling windows based on non-time events or incidents.
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
            the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
            * <feature combination>__<covariance>__<rolling_window_size>. \
                e.g. f1__f2__covariance__3D, f1__f1__covariance__3D, f2__f2__covariance__3D \
                for features f1,f2 in df_variables.
    """

    # check if date column is not int, date_clm_format should be given
    if df.dtypes[date_clm] != "int64":
        if date_clm_format is None:
            raise Exception(
                "The '"
                + str(date_clm)
                + "' column should either be in shifts or timestamps. \
            Either provide integer values for shifts or datetime.datetime values for timestamps in '"
                + str(date_clm)
                + "' column.\
            If the '"
                + str(date_clm)
                + "' column is timestamps but strings format, specify the format of date using \
            'date_clm_format' variable."
            )
        else:
            # apply datetime conversion to date_clm
            df[date_clm] = pd.to_datetime(df[date_clm], format=date_clm_format)

    # creating new datafram
    df = df[[asset_id_clm, date_clm] + variable_clms]
    sensor_features = df[[asset_id_clm, date_clm] + variable_clms]

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    # looping over each aggregation type
    col_names = []
    for i in range(len(variable_clms)):
        for j in range(i, len(variable_clms)):
            col_names.append(
                variable_clms[i]
                + "__"
                + variable_clms[j]
                + "__"
                + "covariance"
                + "__"
                + str(rolling_window_size)
            )

    # looping over each asset group
    temp_table = pd.DataFrame(columns=[col_names])

    for name, grp in df.groupby(asset_id_clm):
        del grp[asset_id_clm]
        tmp = grp.set_index(date_clm)
        tmp = tmp.sort_index()
        if aggregation_type == "time" or aggregation_type == "record":
            pass
        elif aggregation_type == "incident":
            # converting int to timestamp for handling missing info
            tmp["date"] = pd.to_datetime(tmp.index, unit="s")
            index_retain = tmp.index
            tmp = tmp.set_index("date")
        else:
            raise Exception("Please provide a valid aggregation_type.")

        numRow, numCol = tmp.shape
        corX = tmp.rolling(rolling_window_size, min_periods=min_periods).cov()

        finalRes = []
        for row_i in range(numRow):
            finalRes.append(
                corX.iloc[row_i * numCol : (row_i * numCol + numCol), :].values[
                    np.triu_indices(numCol)
                ]
            )

        tmp_res = pd.DataFrame(finalRes)
        tmp_res.index = tmp.index

        if aggregation_type == "incident":
            tmp_res.index = index_retain

        tmp_res.columns = col_names
        tmp_res.reset_index(inplace=True)
        tmp_res[asset_id_clm] = name

        try:
            temp_table = pd.concat([temp_table, tmp_res])
        except Exception:
            temp_table = tmp_res

    # merging each aggregation type result to the sensor_features table
    sensor_features = pd.merge(
        sensor_features, temp_table, on=[asset_id_clm, date_clm], how="left"
    )

    # maintaining column names in the sensor_features table
    sensor_features = sensor_features.rename(
        columns={asset_id_clm: "asset_id", date_clm: "datetime"}
    )
    return sensor_features


class SimpleSummaryStats(BaseEstimator, TransformerMixin):
    """
    A Formal Transformation for Rolling window based feature extraction.
    """

    def __init__(
        self,
        rolling_window_size,
        sensor_feature_columns=None,
        asset_id_column=None,
        sensor_datetime_column=None,
        sensor_datetime_format=None,
        aggregation_type="time",
    ):
        self.rolling_window_size = rolling_window_size
        self.sensor_feature_columns = sensor_feature_columns
        self.asset_id_column = asset_id_column
        self.sensor_datetime_column = sensor_datetime_column
        self.sensor_datetime_format = sensor_datetime_format
        self.aggregation_type = aggregation_type
        self._feature_names = None

    def _transform_input_data(self, X):
        """
        Inernal method to transfrom input data.
        Parameters:
            X (pandas.DataFrame, required): Training set.
        """
        from autoai_ts_libs.deps.srom.feature_engineering.timeseries.rolling_window_feature_extraction import (
            simple_summary_statistics
        )

        sensor_features = simple_summary_statistics(
            df=X,
            rolling_window_size=self.rolling_window_size,
            variable_clms=self.sensor_feature_columns,
            asset_id_clm=self.asset_id_column,
            date_clm=self.sensor_datetime_column,
            date_clm_format=self.sensor_datetime_format,
            aggregation_type=self.aggregation_type,
        )
        self._feature_names = list(sensor_features.columns)
        return sensor_features.values

    def fit(self, X, y=None):
        """
        Fit method.
        Parameters:
            X (pandas.DataFrame, required): Training set.
            y (pandas.DataFrame, optional):
        """
        return self

    def transform(self, X, y=None):
        """
        Fit method.
        Parameters:
            X (pandas.DataFrame, required): Training set.
            y (pandas.DataFrame, optional):
        Returns:
            pandas.DataFrame: Original training set along with engineered features \
                having count of consecutive events that occurred.
        """
        return self._transform_input_data(X)

    def _update_param(self, attr, value):
        setattr(self, attr, value)

    def get_feature_names(self):
        """
        get feature names method.
        """
        return self._feature_names


class HigherOrderStats(BaseEstimator, TransformerMixin):
    """
    A Formal Transformation for Rolling window based feature extraction.
    """

    def __init__(
        self,
        rolling_window_size,
        sensor_feature_columns=None,
        asset_id_column=None,
        sensor_datetime_column=None,
        sensor_datetime_format=None,
        aggregation_type="time",
    ):
        """
        Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days . \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                    A number followed by a character denoting the resolution of the window. \
                    (s-seconds, m-minutes,  h-hours, d-days, w-weeks) .
        variable_clms (string:list, required): List of column names for feature extraction \
            from sensor table.
        asset_id_clm (string, required): Name of the asset-id column in sensor table.
        date_clm (string, required): Name of the date column in sensor table.
        date_clm_format (datetime, optional): Format of the string containing date in sensor \
            table. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        aggregation_type (string, optional): The string denoting the aggregation types. \
                Read pandas-rolling documentation for more info. For missing values monitoring, use \
                `min_periods` parameter in `rolling()`. \
                    3 types of `aggregation_type`: \
                        - 'time': Rolling window based on timestamp. \
                        - 'record': Rolling window based on pandas rows/record. \
                        - 'incident': Rolling windows based on non-time events or incidents.
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
            the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
            * <feature combination>__<covariance>__<rolling_window_size>. \
                e.g. f1__f2__covariance__3D, f1__f1__covariance__3D, f2__f2__covariance__3D \
                for features f1,f2 in df_variables.
        """
        self.rolling_window_size = rolling_window_size
        self.sensor_feature_columns = sensor_feature_columns
        self.asset_id_column = asset_id_column
        self.sensor_datetime_column = sensor_datetime_column
        self.sensor_datetime_format = sensor_datetime_format
        self.aggregation_type = aggregation_type
        self._feature_names = None

    def _transform_input_data(self, X):
        """
        Parameters:
            X (pandas.DataFrame, required): Training set.
        """
        from autoai_ts_libs.deps.srom.feature_engineering.timeseries.rolling_window_feature_extraction import (
            higher_order_summary_statistics
        )

        sensor_features = higher_order_summary_statistics(
            df=X,
            rolling_window_size=self.rolling_window_size,
            variable_clms=self.sensor_feature_columns,
            asset_id_clm=self.asset_id_column,
            date_clm=self.sensor_datetime_column,
            date_clm_format=self.sensor_datetime_format,
            aggregation_type=self.aggregation_type,
        )
        self._feature_names = list(sensor_features.columns)
        return sensor_features.values

    def fit(self, X, y=None):
        """
        Fit method.
        Parameters:
            X (pandas.DataFrame, required): Training set.
        """
        return self

    def _update_param(self, attr, value):
        setattr(self, attr, value)

    def transform(self, X, y=None):
        """
        Transform method.
        Parameters:
            X (pandas.DataFrame, required): Training set.
            y (pandas.DataFrame, optional):
        Returns:
            pandas.DataFrame: Original training set along with engineered features \
                having count of consecutive events that occurred.
        """
        return self._transform_input_data(X)

    def get_feature_names(self):
        """
        get feature names method.
        
        """
        return self._feature_names


class AdvanceSummaryStats(BaseEstimator, TransformerMixin):
    """
    A Formal Transformation for Rolling window based feature extraction.
    """

    def __init__(
        self,
        rolling_window_size,
        sensor_feature_columns=None,
        asset_id_column=None,
        sensor_datetime_column=None,
        sensor_datetime_format=None,
        aggregation_type="time",
        aggregation_methods=None,
    ):
        """
        Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days . \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                    A number followed by a character denoting the resolution of the window. \
                    (s-seconds, m-minutes,  h-hours, d-days, w-weeks) .
        variable_clms (string:list, required): List of column names for feature extraction \
            from sensor table.
        asset_id_clm (string, required): Name of the asset-id column in sensor table.
        date_clm (string, required): Name of the date column in sensor table.
        date_clm_format (datetime, optional): Format of the string containing date in sensor \
            table. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        aggregation_type (string, optional): The string denoting the aggregation types. \
                Read pandas-rolling documentation for more info. For missing values monitoring, use \
                `min_periods` parameter in `rolling()`. \
                    3 types of `aggregation_type`: \
                        - 'time': Rolling window based on timestamp. \
                        - 'record': Rolling window based on pandas rows/record. \
                        - 'incident': Rolling windows based on non-time events or incidents.
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
            the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
            * <feature combination>__<covariance>__<rolling_window_size>. \
                e.g. f1__f2__covariance__3D, f1__f1__covariance__3D, f2__f2__covariance__3D \
                for features f1,f2 in df_variables.
        """
        if not isinstance(rolling_window_size, list):
            rolling_window_size = [rolling_window_size]
        self.rolling_window_size = rolling_window_size
        self.sensor_feature_columns = sensor_feature_columns
        self.asset_id_column = asset_id_column
        self.sensor_datetime_column = sensor_datetime_column
        self.sensor_datetime_format = sensor_datetime_format
        self.aggregation_type = aggregation_type
        self.aggregation_methods = aggregation_methods
        self._feature_names = None

    def _transform_input_data(self, X):
        """
        Parameters:
            X (pandas.DataFrame, required): Training set.
        """
        from autoai_ts_libs.deps.srom.feature_engineering.timeseries.rolling_window_feature_extraction import (
            advance_summary_statistics
        )

        sensor_features = pd.DataFrame()
        for history_window in self.rolling_window_size:
            result = advance_summary_statistics(
                df=X,
                rolling_window_size=history_window,
                variable_clms=self.sensor_feature_columns,
                asset_id_clm=self.asset_id_column,
                date_clm=self.sensor_datetime_column,
                date_clm_format=self.sensor_datetime_format,
                aggregation_type=self.aggregation_type,
                aggregation_methods=self.aggregation_methods,
            )
            if "datetime" not in sensor_features.columns.tolist():
                sensor_features = result
            else:
                sensor_features = pd.merge(
                    left=sensor_features,
                    right=result,
                    on=["datetime", self.asset_id_column],
                )
        self._feature_names = list(sensor_features.columns)
        return sensor_features.values

    def fit(self, X, y=None):
        """
        Parameters:
            X (pandas.DataFrame, required): Training set.
        """
        return self

    def _update_param(self, attr, value):
        setattr(self, attr, value)

    def transform(self, X, y=None):
        """
        Transform method.
        Parameters:
            X (pandas.DataFrame, required): Training set.
            y (pandas.DataFrame, optional):
        Returns:
            pandas.DataFrame: Original training set along with engineered features \
                having count of consecutive events that occurred.
        """
        return self._transform_input_data(X)

    def get_feature_names(self):
        """
        get feature names method.
        """
        return self._feature_names
