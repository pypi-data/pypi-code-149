# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: rolling_window_feature_extraction_parallel
   :synopsis: Rolling window feature extraction parallel.

.. moduleauthor:: SROM Team
"""
import pandas as pd
import numpy as np
from multiprocessing import cpu_count, Pool
from .function_map import mapper


def single_asset_univariate_summary(input_params):
    """
    Applies pandas rolling window aggregate function over a single asset in a pandas \
    dataframe.
    """
    (
        x,
        asset_id_clm,
        date_clm,
        aggregation_type,
        rolling_window_size,
        min_periods,
        aggregation_methods,
    ) = input_params
    # take out the asset_id column
    asset_name = list(set(x[asset_id_clm]))[0]
    del x[asset_id_clm]

    if aggregation_type == "time" or aggregation_type == "record":
        x = x.set_index(date_clm, drop=True)
    elif aggregation_type == "incident":
        temp_date_clm = x[date_clm]
        x[date_clm] = pd.to_datetime(x[date_clm], unit="s")
        x = x.set_index(date_clm, drop=True)
    else:
        raise Exception("Please provide a valid aggregation_type.")

    aggregation_methods = [mapper(i) for i in aggregation_methods]
    print("aggregation_methods: ", aggregation_methods)

    x = x.sort_index()
    x = x.rolling(rolling_window_size, min_periods=min_periods).agg(aggregation_methods)
    x.columns = [
        ("__".join(col) + "__" + str(rolling_window_size)) for col in x.columns.values
    ]
    x[asset_id_clm] = asset_name
    x.reset_index(drop=False, inplace=True)

    if aggregation_type == "incident":
        x[date_clm] = temp_date_clm
    return x


def single_asset_bivariate_summary(input_params):
    """
    Applies pandas rolling window aggregate function over a single asset in a pandas \
    dataframe.
    """
    (
        x,
        asset_id_clm,
        date_clm,
        aggregation_type,
        rolling_window_size,
        min_periods,
        aggregation_methods,
    ) = input_params
    # take out the asset_id column
    asset_name = list(set(x[asset_id_clm]))[0]
    del x[asset_id_clm]

    if aggregation_type == "time" or aggregation_type == "record":
        x = x.set_index(date_clm, drop=True)
    elif aggregation_type == "incident":
        temp_date_clm = x[date_clm]
        x[date_clm] = pd.to_datetime(x[date_clm], unit="s")
        x = x.set_index(date_clm, drop=True)
    else:
        raise Exception("Please provide a valid aggregation_type.")

    # looping over each aggregation type
    x = x.sort_index()
    numRow, numCol = x.shape

    if aggregation_methods == "correlation":
        variable_clms = list(x.columns)
        col_names = []
        for i in range(len(variable_clms)):
            for j in range(i + 1, len(variable_clms)):
                col_names.append(
                    variable_clms[i]
                    + "__"
                    + variable_clms[j]
                    + "__"
                    + aggregation_methods
                    + "__"
                    + str(rolling_window_size)
                )

        BivarX = x.rolling(rolling_window_size, min_periods=min_periods).corr()

        finalRes = []
        for row_i in range(numRow):
            finalRes.append(
                BivarX.iloc[row_i * numCol : (row_i * numCol + numCol), :].values[
                    np.triu_indices(numCol, k=1)
                ]
            )

    elif aggregation_methods == "covariance":
        variable_clms = list(x.columns)
        col_names = []
        for i in range(len(variable_clms)):
            for j in range(i, len(variable_clms)):
                col_names.append(
                    variable_clms[i]
                    + "__"
                    + variable_clms[j]
                    + "__"
                    + aggregation_methods
                    + "__"
                    + str(rolling_window_size)
                )

        BivarX = x.rolling(rolling_window_size, min_periods=min_periods).cov()
        finalRes = []
        for row_i in range(numRow):
            finalRes.append(
                BivarX.iloc[row_i * numCol : (row_i * numCol + numCol), :].values[
                    np.triu_indices(numCol)
                ]
            )

    tmp_res = pd.DataFrame(finalRes)
    tmp_res.index = x.index
    tmp_res.columns = col_names
    tmp_res.reset_index(drop=False, inplace=True)
    tmp_res[asset_id_clm] = asset_name

    if aggregation_type == "incident":
        tmp_res[date_clm] = temp_date_clm
    return tmp_res


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
    Extracts the rolling window aggregation features by distributing workload on \
    all cores.

    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        aggregation_methods (string:list, required): It is a list of aggregation methods to be \
                used for feature extraction.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days. \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
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
                    - 'time': rolling window based on timestamp. \
                    - 'record': rolling window based on pandas rows/record. \
                    - 'incident': rolling windows based on non-time events or incidents. \
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
                the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
                * <aggregation method> _ <history window size> _ <sensor name>.
                example: mean_30_sensor_1(for sensor_1).
    """
    # check if date column is not int, date_clm_format should be given
    if df.dtypes[date_clm] != "int64":
        if date_clm_format is None:
            raise Exception(
                "The '"
                + str(date_clm)
                + "' column should either be in shifts or timestamps"
            )
        else:
            df[date_clm] = pd.to_datetime(df[date_clm], format=date_clm_format)

    if aggregation_methods is None:
        aggregation_methods = ["mean", "max", "min", "median", "std", "sum", "count"]

    # creating new datafram
    df = df[[asset_id_clm, date_clm] + variable_clms]

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    part = [
        (
            grp,
            asset_id_clm,
            date_clm,
            aggregation_type,
            rolling_window_size,
            min_periods,
            aggregation_methods,
        )
        for name, grp in df.groupby(asset_id_clm)
    ]
    cores = cpu_count() - 1
    with Pool(cores) as p:
        resList = p.map(single_asset_univariate_summary, part)

    extractedFeatures = pd.concat(resList)
    print(extractedFeatures.head())
    sensor_features = pd.merge(
        df, extractedFeatures, on=[asset_id_clm, date_clm], how="left"
    )
    sensor_features.rename(
        columns=dict(zip([asset_id_clm, date_clm], ["asset_id", "datetime"])),
        inplace=True,
    )
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
    Extracts the rolling window aggregation features by distributing workload on \
    all cores.

    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        aggregation_methods (string:list, required): It is a list of aggregation methods to be \
                used for feature extraction.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter). eg. '30D' - 30 days \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                    A number followed by a character denoting the resolution of the window. \
                    (s-seconds, m-minutes,  h-hours, d-days, w-weeks) \
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
                    - 'time': rolling window based on timestamp \
                    - 'record': rolling window based on pandas rows/record \
                    - 'incident': rolling windows based on non-time events or incidents. \
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
                the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
                * <aggregation method> _ <history window size> _ <sensor name> \
                example: mean_30_sensor_1 (for sensor_1).
    """
    # check if date column is not int, date_clm_format should be given
    if df.dtypes[date_clm] != "int64":
        if date_clm_format is None:
            raise Exception(
                "The '"
                + str(date_clm)
                + "' column should either be in shifts or timestamps"
            )
        else:
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

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    part = [
        (
            grp,
            asset_id_clm,
            date_clm,
            aggregation_type,
            rolling_window_size,
            min_periods,
            aggregation_methods,
        )
        for name, grp in df.groupby(asset_id_clm)
    ]
    cores = cpu_count() - 1
    with Pool(cores) as p:
        resList = p.map(single_asset_univariate_summary, part)

    extractedFeatures = pd.concat(resList)
    print(extractedFeatures.head())
    sensor_features = pd.merge(
        df, extractedFeatures, on=[asset_id_clm, date_clm], how="left"
    )
    sensor_features.rename(
        columns=dict(zip([asset_id_clm, date_clm], ["asset_id", "datetime"])),
        inplace=True,
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
    Extracts the rolling window aggregation features by distributing workload on \
    all cores.
    
    Parameters:
        df (pandas dataframe, required): Dataframe for sensor table.
        aggregation_methods (string:list, required): It is a list of aggregation methods to be \
                used for feature extraction.
        rolling_window_size (string, required): Window size for which the rolling window aggregation \
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days  \
                Assumes number of days  \
                - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                  A number followed by a character denoting the resolution of the window. \
                  (s-seconds, m-minutes,  h-hours, d-days, w-weeks) \
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
                    - 'time': rolling window based on timestamp \
                    - 'record': rolling window based on pandas rows/record \
                    - 'incident': rolling windows based on non-time events or incidents.
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
                the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
            * <aggregation method> _ <history window size> _ <sensor name> \
            example: mean_30_sensor_1(for sensor_1)
    """

    # check if date column is not int, date_clm_format should be given
    if df.dtypes[date_clm] != "int64":
        if date_clm_format is None:
            raise Exception(
                "The '"
                + str(date_clm)
                + "' column should either be in shifts or timestamps"
            )
        else:
            df[date_clm] = pd.to_datetime(df[date_clm], format=date_clm_format)

    if aggregation_methods is None:
        aggregation_methods = [
            "rate_of_change",
            "sum_of_change",
            "absoluate_sum_of_change",
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
            "delta_diff",
            "past_value",
        ]

    # creating new datafram
    df = df[[asset_id_clm, date_clm] + variable_clms]

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    part = [
        (
            grp,
            asset_id_clm,
            date_clm,
            aggregation_type,
            rolling_window_size,
            min_periods,
            aggregation_methods,
        )
        for name, grp in df.groupby(asset_id_clm)
    ]
    cores = cpu_count() - 1
    with Pool(cores) as p:
        resList = p.map(single_asset_univariate_summary, part)

    extractedFeatures = pd.concat(resList)
    print(extractedFeatures.head())
    sensor_features = pd.merge(
        df, extractedFeatures, on=[asset_id_clm, date_clm], how="left"
    )
    sensor_features.rename(
        columns=dict(zip([asset_id_clm, date_clm], ["asset_id", "datetime"])),
        inplace=True,
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
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                    A number followed by a character denoting the resolution of the window. \
                    (s-seconds, m-minutes,  h-hours, d-days, w-weeks) \
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
                    - 'time': rolling window based on timestamp. \
                    - 'record': rolling window based on pandas rows/record. \
                    - 'incident': rolling windows based on non-time events or incidents. \
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
                the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
        * <feature1>__<feature2>...__<correlation>__<rolling_window_size> \
            e.g. f1__f2__correlation__3D for features f1,f2 in df_variables
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

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    part = [
        (
            grp,
            asset_id_clm,
            date_clm,
            aggregation_type,
            rolling_window_size,
            min_periods,
            "correlation",
        )
        for _, grp in df.groupby(asset_id_clm)
    ]
    cores = cpu_count() - 1
    with Pool(cores) as p:
        resList = p.map(single_asset_bivariate_summary, part)

    extractedFeatures = pd.concat(resList)
    sensor_features = pd.merge(
        df, extractedFeatures, on=[asset_id_clm, date_clm], how="left"
    )
    sensor_features.rename(
        columns=dict(zip([asset_id_clm, date_clm], ["asset_id", "datetime"])),
        inplace=True,
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
                should be in string format (integer followed by a letter.) eg. '30D' - 30 days \
                Assumes number of days \
                    - string (eg. '1d': 1 day, '10h': 10 hours, '250s: 250 seconds') \
                    A number followed by a character denoting the resolution of the window. \
                    (s-seconds, m-minutes,  h-hours, d-days, w-weeks)
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
                    - 'time': rolling window based on timestamp \
                    - 'record': rolling window based on pandas rows/record \
                    - 'incident': rolling windows based on non-time events or incidents.
        min_periods (int, optional): No of rows to consider by pandas.DataFrame.rolling to calculate \
                the rolling value. This is advanced option to be used during irregular sampling.

    Return:
        dataframe: Table with the extracted features in the following format. \
            * <feature combination>__<covariance>__<rolling_window_size> \
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

    # converting int to secs later
    if aggregation_type == "incident":
        rolling_window_size = str(rolling_window_size) + "s"

    part = [
        (
            grp,
            asset_id_clm,
            date_clm,
            aggregation_type,
            rolling_window_size,
            min_periods,
            "covariance",
        )
        for _, grp in df.groupby(asset_id_clm)
    ]
    cores = cpu_count() - 1
    with Pool(cores) as p:
        resList = p.map(single_asset_bivariate_summary, part)

    extractedFeatures = pd.concat(resList)
    sensor_features = pd.merge(
        df, extractedFeatures, on=[asset_id_clm, date_clm], how="left"
    )
    sensor_features.rename(
        columns=dict(zip([asset_id_clm, date_clm], ["asset_id", "datetime"])),
        inplace=True,
    )

    # maintaining column names in the sensor_features table
    sensor_features = sensor_features.rename(
        columns={asset_id_clm: "asset_id", date_clm: "datetime"}
    )
    return sensor_features
