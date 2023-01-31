# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
Contains methods to perform operations over data
"""
import os
import numpy as np
import pandas as pd


def data_label_split(test_data, label_prefix):
    """
    Args:
        test_data: Pandas dataframe
        label_prefix (str): Either name of the label column or
                            common prefix for feature-wise lables
    Returns:
        An object with the test data matrix (without the index column), data column headers,
        the index column vector if any, label matrix with labels for the test data.
        The number of rows in the two matrices are the same.
        In case of feature-wise labels, the number of columns are same too.
        In case of row-wise labels, the second matrix is a column vector.
    """

    data = []
    index_label_dict = {}
    if isinstance(test_data, pd.DataFrame):
        data = test_data.values
    else:
        data = test_data

    label_columns_indices = []
    row_wise_label_column = None
    row_wise_label_column_index = None
    headers = test_data.columns
    data_headers = []
    test_data = None
    test_data_labels = None

    if label_prefix is None or label_prefix == "":
        pass
    else:
        label_prefix = (
            label_prefix.strip()
        )  # striping blank spaces if no label prefix is given
        for column_index, _ in enumerate(headers):
            column = headers[column_index]
            if column.startswith(label_prefix):
                label_index = column[len(label_prefix) :]
                if label_index != "":
                    index_label_dict[int(label_index)] = data[:, column_index]
                else:
                    # will happen if there is a row-wise label,
                    # in that case the label_prefix is the name of the label column
                    # and there should be only one label column
                    row_wise_label_column = data[:, column_index]
                    row_wise_label_column_index = column_index
                label_columns_indices.append(column_index)
        non_label_columns_indices = set(list(range(len(headers)))) - set(
            label_columns_indices
        )

        # For each of the columns with data (not labels), add it to the data array,
        # get the corresponding label if present
        nrows = data.shape[0]
        for index in non_label_columns_indices:
            data_headers.append(headers[index])
            if (
                row_wise_label_column_index is None
                or index != row_wise_label_column_index
            ):
                if test_data is None:
                    test_data = data[:, index]
                else:
                    test_data = np.vstack((test_data, data[:, index]))
                if row_wise_label_column_index is None:
                    # That would mean, there are feature-wise labels
                    try:
                        labels_column_vector = index_label_dict[index]
                    except KeyError:
                        # This is not an error condition because,
                        # we allow labels for subset of columns
                        # Labels for such columns are added as nans as of now.
                        # Nan because that is handled by pandas as missing values
                        labels_column_vector = np.full(nrows, np.nan)
                    if test_data_labels is None:
                        test_data_labels = labels_column_vector
                    else:
                        test_data_labels = np.vstack(
                            (test_data_labels, labels_column_vector)
                        )
                else:
                    test_data_labels = row_wise_label_column
        test_data = test_data.T
        test_data_labels = test_data_labels.T

    return test_data, test_data_labels


def train_test_split(df, test_size=0.2, test_rows=None):
    """
    Split the data into train and test keeping the order.
    Args:
        test_size (float:optional): Fraction of axis items to return.
        test_rows (integer:optional): Represents the absolute number of test samples.
    Returns train and test dataframes
    """
    n_rows = df.shape[0]
    # if test_rows is None, we assume that test_size value needs to be used
    if test_rows is None:
        n_rows_train = int(np.floor(n_rows * (1 - test_size)))
    else:
        n_rows_train = int(n_rows - test_rows)

    return df[:n_rows_train], df[n_rows_train:]


def random_train_test_split(df, test_size=0.2):
    """
    Split the data into train and test randomly.
    Args:
        test_size (float): Fraction of axis items to return.
    Returns train and test dataframes
    """
    if isinstance(df, np.ndarray):
        df = pd.DataFrame(df)
    df_test = df.sample(frac=test_size)
    df_train = df.drop(df_test.index)
    return df_train, df_test


def is_present(source, target):
    """
    Check whether target is in source or not.
    """
    if (not isinstance(target, (str, list, np.ndarray))) or (
        not isinstance(source, (list, np.ndarray))
    ):
        raise Exception(
            "Comparison of source type {} with target type {} is not supported.".format(
                type(source), type(target)
            )
        )
    if isinstance(target, str) and (target not in source):
        return False
    diff = np.setdiff1d(target, source)
    if not diff:
        return True
    return False

def load_seasonal_trend():
    
    A = [
        ["2017-05-07",0.0],
        ["2017-05-14",1.2],
        ["2017-05-21",2.4],
        ["2017-05-28",3.6],
        ["2017-06-04",4.8],
        ["2017-06-11",6.0],
        ["2017-06-18",7.2],
        ["2017-06-25",1.4],
        ["2017-07-02",2.6],
        ["2017-07-09",3.8],
        ["2017-07-16",5.0],
        ["2017-07-23",6.2],
        ["2017-07-30",7.4],
        ["2017-08-06",8.6],
        ["2017-08-13",2.8],
        ["2017-08-20",4.0],
        ["2017-08-27",5.2],
        ["2017-09-03",6.4],
        ["2017-09-10",7.6],
        ["2017-09-17",8.8],
        ["2017-09-24",10.0],
        ["2017-10-01",4.2],
        ["2017-10-08",5.4],
        ["2017-10-15",6.6],
        ["2017-10-22",7.8],
        ["2017-10-29",9.0],
        ["2017-11-05",10.2],
        ["2017-11-12",11.4],
        ["2017-11-19",5.6],
        ["2017-11-26",6.8],
        ["2017-12-03",13.0],
        ["2017-12-10",9.2],
        ["2017-12-17",10.4],
        ["2017-12-24",11.6],
        ["2017-12-31",12.8],
        ["2018-01-07",7.0],
        ["2018-01-14",8.2],
        ["2018-01-21",9.4],
        ["2018-01-28",10.6],
        ["2018-02-04",11.8],
        ["2018-02-11",13.0],
        ["2018-02-18",14.2],
        ["2018-02-25",8.4],
        ["2018-03-04",9.6],
        ["2018-03-11",10.8],
        ["2018-03-18",12.0],
        ["2018-03-25",13.2],
        ["2018-04-01",14.4],
        ["2018-04-08",15.6],
        ["2018-04-15",9.8],
        ["2018-04-22",11.0],
        ["2018-04-29",12.2],
        ["2018-05-06",13.4],
        ["2018-05-13",14.6],
        ["2018-05-20",15.8],
        ["2018-05-27",17.0],
        ["2018-06-03",11.2],
        ["2018-06-10",12.4],
        ["2018-06-17",13.6],
        ["2018-06-24",14.8],
        ["2018-07-01",16.0],
        ["2018-07-08",17.2],
        ["2018-07-15",18.4],
        ["2018-07-22",12.6],
        ["2018-07-29",13.8],
        ["2018-08-05",15.0],
        ["2018-08-12",16.2],
        ["2018-08-19",17.4],
        ["2018-08-26",18.6],
        ["2018-09-02",19.8],
        ["2018-09-09",14.0],
        ["2018-09-16",15.2],
        ["2018-09-23",16.4],
        ["2018-09-30",17.6],
        ["2018-10-07",18.8],
        ["2018-10-14",20.0],
        ["2018-10-21",21.2],
        ["2018-10-28",15.4],
        ["2018-11-04",16.6],
        ["2018-11-11",17.8],
        ["2018-11-18",19.0],
        ["2018-11-25",20.2],
        ["2018-12-02",21.4],
        ["2018-12-09",22.6],
        ["2018-12-16",16.8],
        ["2018-12-23",18.0],
        ["2018-12-30",19.2],
        ["2019-01-06",20.4],
        ["2019-01-13",21.6],
        ["2019-01-20",22.8],
        ["2019-01-27",24.0],
        ["2019-02-03",18.2],
        ["2019-02-10",19.4],
        ["2019-02-17",20.6],
        ["2019-02-24",21.8],
        ["2019-03-03",23.0],
        ["2019-03-10",24.2],
        ["2019-03-17",25.4],
        ["2019-03-24",19.6],
        ["2019-03-31",20.8],
    ]
    
    df = pd.DataFrame(A,columns=["Time","Value"])
    df["Time"] = pd.to_datetime(df["Time"])
    return df
