# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Utility class for SROM's non-linear optimization implementation"""

import warnings

import pandas as pd


def todf(x, columns):
    """
    Converts numpy array to pandas dataframe.
    Args:
        x(numpy.ndarray)
        columns(list of strings)
    Returns:
        ans(pandas.Dataframe)
    """
    warnings.warn(
        "todf method is deprecated. Use pandas DataFrame constructor instead.",
        DeprecationWarning,
    )
    ans: pd.DataFrame = pd.DataFrame(data=[x], columns=columns)
    return ans


def concatbyrow(df1, df2, cols1, cols2):
    """
    Concatenate dataframe row wise from df1 and df2.
    Args:
        df1,df2(pandas.Datframe)
        cols1,cols2(list of strings)
    Returns:
        ans(pandas.Dataframe)
    """

    warnings.warn(
        "concatbyrow method is deprecated. Use pandas DataFrame join method instead.",
        DeprecationWarning,
    )

    left: pd.DataFrame = pd.DataFrame(data=df1.values, columns=cols1)
    right: pd.DataFrame = pd.DataFrame(data=df2.values, columns=cols2)
    return left.join(right)

    # return ans
