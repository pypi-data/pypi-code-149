# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Generates time_series_episodic data
"""
import pandas as pd


def generate_episode_data(
    input_df,
    episode_id=None,
    sensor_columns=None,
    time_column=None,
    episode_data_type=0,
):
    """
    Generates time series episodic data table.

    Args:
        input_df (pandas.DataFrame, required): pandas dataframe to be converted to episodic
        time series data.
        episode_id (string, required): column name having the distinct id of each episode.
        sensor_columns (python list, required): column names for sensor variable in a list
        time_column (string, required): column name of the time column or the time sequence column
        episode_data_type (int, optional): type for the 'episode_data' column. 
            0: pandas.DataFrame
            1: dict
            ** Option episode_data_type=1 (dict) should be chosed for performing root cause with WML deployment and scoring.

    Returns:
        pandas.DataFrame: time series episodic dataframe returned.
    """
    group_d = []
    names = []
    if sensor_columns is None:
        sensor_columns = []

    if time_column is not None:
        sensor_columns = [time_column] + sensor_columns
    for name, item in input_df.groupby(episode_id):
        names.append(name)
        tmp_episode_data = item[sensor_columns]
        if episode_data_type == 1:
            tmp_episode_data = tmp_episode_data.to_dict()
        elif episode_data_type == 0:
            pass
        else:
            raise Exception(
                "`episode_data_type` value is invalid. Provide value of either 0 or 1."
            )
        group_d.append(tmp_episode_data)

    data = pd.DataFrame(names)
    data.columns = [episode_id]
    data["episode_data"] = group_d

    data = data.sort_values([episode_id], ascending=True).reset_index(drop=True)
    return data
