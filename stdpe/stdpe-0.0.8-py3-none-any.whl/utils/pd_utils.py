""" Pandas utilities
    Authors: Joshoua Bigler 
    
    Description
    -----------
    Pandas utilities for the daily work.

    Provides
    --------
    PandasConverter
    PandasFilter
    PandasSQLMode
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from pandas import DataFrame, Series, Timestamp
from sqlmodel import SQLModel
from typing import List


class PandasConverter:
  """ Class for converting pandas data frames"""

  def str_to_datetime(data: DataFrame, utc: bool, column: str):
    data[column] = pd.to_datetime(data[column], utc=utc)

  @staticmethod
  def datetime_to_str(data: DataFrame, column: str, sep: str = 'T', timespec: str = 'auto'):
    """ Converts an DataFrame column of datetimes into strings. 

        Paramters
        ---------
        data:       Data to convert
        identifier: Column identifier of the datetime data
        seperator:  Seperator of the timestamp
        timespec:   Specifies the number of additional terms of the time to include. The valid values are: 
                    'auto', 'hours', 'minutes', 'seconds', 'milliseconds', 'microseconds', and 'nanoseconds'.

    """

    timestamp_list = [timestamp.isoformat(sep=sep, timespec=timespec) for timestamp in data[column]]
    data[column] = pd.DataFrame(timestamp_list, columns=[column])

  @staticmethod
  def convert_dtypes(data: DataFrame, dtypes: dict):
    """ Converts the DataFrame into given data type from the dictionary. 

        Example
        -------
        input:
        data = ['temperature' = 22]
        dtypes =  {float: ['temperature', ...]}

        output:
        data = ['temperature' = 22.0]
    """

    column_names = list(data.columns)
    for name in column_names:
      for type in dtypes:
        if name in dtypes[type]:
          data[name] = data[name].astype(type)

  @staticmethod
  def rename_col_names(data: DataFrame, col_names: dict):
    """ Renames the columns of the DataFrame with given dictionary. 
        
        Example
        -------
        input:
        df_data =   ['veryLongColumnName': 'value']
        col_names = {'shortName': 'veryLongColumnName'}

        output:
        df_data = ['shortName': 'value']
    """

    columns_old = list(data.columns)
    columns_new = columns_old
    for idx, column_name in enumerate(columns_old):
      for key, value in col_names.items():
        if value == column_name:
          columns_new[idx] = key
    data.columns = columns_new


class PandasFilter:
  """ Class for filtering pandas data frames. """

  @staticmethod
  def get_time_delta_filter(data: DataFrame, time_delta_sec: int, col_filt_name: str, col_time_name: str) -> Series:
    """ Returns a filter for the given DataFrame if the interval is smaller then the time_delta_sec. 

        Parameters
        ----------
        data:           Data to filter
        time_delta_sec: Time interval to filter
        col_filt_name:  Column name for grouping the data to filter by.
        col_time_name:  Column name of the timestamp
    
    """

    if type(data[col_time_name].iloc[0]) != Timestamp:
      raise Exception("Timestamp has to be a pandas Timestamp object!")

    time_delta_nan = timedelta(seconds=time_delta_sec)
    grp = data.groupby(data[col_filt_name], group_keys=False)
    grp_time_diff = grp[col_time_name].diff().fillna(time_delta_nan).dt.seconds
    filt = grp_time_diff >= time_delta_sec
    return filt

  @staticmethod
  def get_day_filter(data: DataFrame, col_time_name: str, days_before_today: int) -> DataFrame:
    """ Filters the incoming data by the given day before today.

        Parameters
        ----------
        df_data:            Data to filter
        col_time_name:      Timestamp column name  
        days_before_today:  Number of days before today, example: today = 0, yesterday=1    
    """

    if type(data[col_time_name].iloc[0]) != Timestamp:
      raise Exception("Timestamp has to be a pandas Timestamp object!")

    str_format = '%Y-%m-%d'
    today = datetime.utcnow()
    day_before = today - timedelta(days=days_before_today + 1)

    # if day_filt != today:
    day_after = today - timedelta(days=days_before_today - 1)
    day_before_str = datetime.strftime(day_before, str_format)
    day_after_str = datetime.strftime(day_after, str_format)
    filt = (data[col_time_name] > day_before_str) & (data[col_time_name] < day_after_str)
    return filt


class PandasSQLModel:
  """Class for working with the SQLModel library and the pandas library. """

  @staticmethod
  def sqlmodel_to_df(objects: List[SQLModel], col_idx_name: str = None) -> DataFrame:
    """ Converts SQLModel objects into a Pandas DataFrame.

        Parameters
        ----------
        objects:      List of SQLModel objects to be converted.
        col_idx_name: Column name for setting the index. If no column name is given the index will not be set.  
    """

    if not objects:
      return None
    records = [obj.dict() for obj in objects]
    columns = list(objects[0].schema()['properties'].keys())
    df = DataFrame.from_records(records, columns=columns)
    if col_idx_name:
      return df.set_index(col_idx_name)
    else:
      return df

  @staticmethod
  def df_to_sqlmodel(data: DataFrame, orm_obj: SQLModel) -> List[SQLModel]:
    """ Convert a pandas DataFrame into a a list of SQLModel objects. """

    objs = [orm_obj(**row) for row in data.to_dict('records')]
    return objs