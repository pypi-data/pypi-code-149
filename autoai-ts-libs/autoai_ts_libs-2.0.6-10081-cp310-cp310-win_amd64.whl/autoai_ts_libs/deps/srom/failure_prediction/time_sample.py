# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: time_sample
   :synopsis: Failure prediction preprocessing module.

.. moduleauthor:: SROM Team
"""
from datetime import timedelta
import pandas as pd


def process_time_interval(interval):
    """
    Function to process the interval provided by the user. Takes input either in the \
    dict format or in the string format as shown.

    Parameters:
        interval (dict/str, required): Intervals at which the key has to be generated. \
            - DICT: Interval can be specified in the following format \
              1 day --> \
              interval = {'weeks':0 \
                          'days': 1, \
                          'hours':0, \
                          'minutes':0, \
                          'seconds':0} \
            - STR: Interval can be specified in the following format. \
              1 day --> \
              interval = '1D' \
              Refer to this link:  https://pandas.pydata.org/pandas-docs/stable/timeseries.html

    Returns:
        td (offset format from datetime/pandas): The interval value that can be added or subtracted \
            from timestamp value in python.
    """
    # if interval is provided in dict or offset str
    if isinstance(interval, dict):
        # initializing any missing keys as 0
        interval_keys = ["weeks", "days", "hours", "minutes", "seconds"]
        for key in interval_keys:
            if key not in interval.keys():
                interval[key] = 0
        td = timedelta(
            weeks=interval["weeks"],
            days=interval["days"],
            hours=interval["hours"],
            minutes=interval["minutes"],
            seconds=interval["seconds"],
        )
    elif isinstance(interval, str):
        td = pd.tseries.frequencies.to_offset(interval)
    elif isinstance(interval, int):
        td = interval
    else:
        raise Exception("invalid type for interval, must be dict, int or str")

    return td


def time_sampling(timestamp_st, timestamp_end, interval=None):
    """
    Creates a new dataframe which takes a start timestamp and end timestamp and returns timesamples \
    at regular intervals. By default, the interval is assumed to be one day.

    Parameters:
        timestamp_st (datetime, required): Timestamp for the first entry in the dataframe.
        timestamp_end (datetime, required): Timestamp for the last entry in the dataframe.
        interval (str/dict, optional): Intervals at which the key has to be generated. \
                (key timestamp resolution). (default = 1 day) \
                - dict (format- {'weeks': 0, 'days': 1, 'hours': 0, 'minutes': 0, \
                             'seconds': 0} \
                - str: Refer to this link to see offset strings. \
                http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases

    Returns:
        Dataframe containing timestamps samples from starting to ending at defined interval.
    """
    # if no interval is provided, the the default interval is set at 1 day
    if interval is None:
        interval = {"weeks": 0, "days": 1, "hours": 0, "minutes": 0, "seconds": 0}

    # creating empty dataframe
    timestamp = pd.DataFrame(columns=["timestamp"])

    atime_delta = process_time_interval(interval)

    # filling dataframe with timestamps
    i = 0
    while timestamp_st <= timestamp_end:
        timestamp.loc[i] = timestamp_st
        timestamp_st = timestamp_st + atime_delta
        i += 1
    return timestamp
