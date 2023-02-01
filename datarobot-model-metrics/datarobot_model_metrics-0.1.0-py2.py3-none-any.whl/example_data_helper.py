from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta

from dmm.constants import ColumnName, TimeBucket


def timedelta_for_bucket(time_bucket: TimeBucket):
    if time_bucket == TimeBucket.SECOND:
        return timedelta(seconds=1)
    elif time_bucket == TimeBucket.MINUTE:
        return timedelta(minutes=1)
    elif time_bucket == TimeBucket.HOUR:
        return timedelta(hours=1)
    elif time_bucket == TimeBucket.DAY:
        return timedelta(days=1)
    elif time_bucket == TimeBucket.WEEK:
        return timedelta(weeks=1)
    elif time_bucket == TimeBucket.MONTH:
        return relativedelta(months=1)
    elif time_bucket == TimeBucket.ALL:
        return timedelta(seconds=0)
    else:
        raise Exception(f"Time Bucket {time_bucket} is not supported")


def gen_timestamps_list(nr_rows, time_bucket, rows_per_time_bucket):
    timedelta_obj = timedelta_for_bucket(time_bucket)
    datetime_object = datetime.strptime("Jun 1 2005  1:00:00PM", "%b %d %Y %I:%M:%S%p")
    timestamps = []
    for row in range(nr_rows):

        if row % rows_per_time_bucket == 0 and row != 0:
            datetime_object += timedelta_obj
        timestamp_str = (datetime_object.strftime("%d/%m/%Y %H:%M:%S.%f"),)
        timestamps.append(timestamp_str)
    return timestamps


def gen_dataframe_for_accuracy_metric(
    nr_rows=1000,
    timestamp_col=ColumnName.TIMESTAMP,
    with_predictions=True,
    prediction_col=ColumnName.PREDICTIONS,
    with_actuals=True,
    actuals_col=ColumnName.ACTUALS,
    with_dr_timestamp_column=False,
    dr_timestamp_column=ColumnName.DR_TIMESTAMP_COLUMN,
    with_association_id=False,
    association_id_col=ColumnName.ASSOCIATION_ID_COLUMN,
    prediction_value=None,
    random_predictions=False,
    time_bucket=TimeBucket.MINUTE,
    rows_per_time_bucket=100,
    prediction_actual_diff=0.001,
):
    """
    Generate a dataframe for testing
    :param nr_rows: Number of rows to generate
    :param with_predictions: Add predictions to the data
    :param prediction_col: Name of prediction column
    :param prediction_value: A fixed value to use for predictions
    :param random_predictions: If True generate random predictions instead of a fixed value
    :param with_actuals: Add actuals column to the data
    :param actuals_col: Name of actuals column
    :param with_association_id: Add association id column to the data
    :param association_id_col: Name of association id column
    :param with_dr_timestamp_column: Add predictions timestamp column to the data
    :param dr_timestamp_column: Name of predictions timestamp column
    :param time_bucket: Time bucket to generate predictions for
    :param rows_per_time_bucket: How many rows per time bucket to generate
    :param prediction_actual_diff: diff between predictions and actuals
    :param timestamp_col: Name of timestamp column
    :return: Dataframe with the generated data
    """

    timestamps = gen_timestamps_list(nr_rows, time_bucket, rows_per_time_bucket)
    df = pd.DataFrame(timestamps, columns=[timestamp_col])

    if prediction_value:
        predictions = np.full(nr_rows, prediction_value)
    elif random_predictions:
        predictions = np.random.randint(1, 10, size=nr_rows)
    else:
        predictions = [x for x in range(nr_rows)]

    if with_predictions:
        df[prediction_col] = np.array(predictions)
    if with_actuals:
        df[actuals_col] = [x - prediction_actual_diff for x in predictions]
    if with_association_id:
        df[association_id_col] = [x for x in range(nr_rows)]
    if with_dr_timestamp_column:
        df[dr_timestamp_column] = df[timestamp_col]

    return df


def gen_dataframe_for_data_metrics(
    nr_rows=1000,
    time_bucket=TimeBucket.MINUTE,
    rows_per_time_bucket=100,
    columns=("A", "B"),
    add_missing_values=0,
):
    if add_missing_values > nr_rows:
        raise Exception(
            f"Number of missing values requested {add_missing_values} > number of rows {rows_per_time_bucket}"
        )

    timestamps = gen_timestamps_list(
        nr_rows=nr_rows,
        time_bucket=time_bucket,
        rows_per_time_bucket=rows_per_time_bucket,
    )
    df = pd.DataFrame(timestamps, columns=[ColumnName.TIMESTAMP])

    for col_name in columns:
        df[col_name] = range(nr_rows)

    return df
