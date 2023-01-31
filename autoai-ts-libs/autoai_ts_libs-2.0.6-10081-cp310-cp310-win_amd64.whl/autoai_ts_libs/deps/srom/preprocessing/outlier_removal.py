# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: outlier_removal
   :synopsis: Contains methods which could be used \
       for outlier removal.

.. moduleauthor:: SROM Team
"""
import pandas
import numpy as np

def prob_density_based_outlier_removal(X, threshold=5.e-3, columns_to_be_ignored=None):
    """
    Performs global outlier removal based on probability density.
    
    Steps:
        1. Define a threshold and compute the probability density of a feature.
        2. Compute the probability in each bin.
        3. Remove the entire row if, probability in each bin is less than the threshold.
        4. Repeat the removal process for relevant variables.

    Parameters:
        X (pandas.DataFrame): Data on which outlier removal is to be performed.
        threshold (float, optional): Defaults to 5.e-3.
        columns_to_be_ignored (list, optional): Defaults to None.

    Returns:
        X (pandas.DataFrame): Data without outliers.
    """
    if columns_to_be_ignored is None:
        columns_to_be_ignored = []
    if isinstance(X, pandas.DataFrame):
        columns = X.columns
        for column in columns:
            if column not in columns_to_be_ignored:
                X = remove_rows_based_on_single_attribute_prob(X, column, threshold)
    return X

def remove_rows_based_on_single_attribute_prob(data_in, column_name, threshold):
    """
    Removes rows from the dataframe based on the provided threshold \
    for a single feature.

    Parameters:
        data_in (pandas.DataFrame): Data on which outlier removal is to \
            be performed.
        column_name (str): Feature column name.
        threshold (float)
        
    Returns:
        pandas.DataFrame: Data without outliers.
    """

    ans1, ans2 = np.histogram(data_in[column_name], bins=51)

    a1 = ans2
    a2 = ans2
    a1 = np.delete(a1, len(a1) - 1, 0)
    a2 = np.delete(a2, 0, 0)
    diff = np.delete(ans2, len(ans2) - 1, 0) + ((a2 - a1) / 2.0)
    df = (a2[0] - a1[0])
    point_in = diff[(ans1 / (1.0 * ans1.sum())) > threshold]

    flag = np.zeros((len(data_in[column_name])), dtype=bool)

    for i, _ in enumerate(point_in):
        flag1 = data_in[column_name] >= (point_in[i] - 0.5 * df)
        flag2 = data_in[column_name] <= (point_in[i] + 0.5 * df)
        flag = np.logical_or(flag, (np.logical_and(flag1, flag2)))

    return data_in[flag]
