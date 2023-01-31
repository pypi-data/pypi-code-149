# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Contains methods to object cross validation objects 
"""


def get_assets_based_CV(X, y, groups, n_splits=5):
    """
    Args:
        n_splits (int): Similar to K in KFold cross validation analysis
        X: Pandas dataframe for train
        y: list for test
        groups (int): asset id or group id for each sample of X

    Returns:
        An cross validatoin object that can be passed to srom/sklearn pipeline.
    """
    from sklearn.model_selection import GroupKFold

    group_kfold = GroupKFold(n_splits=n_splits)
    cv = list(group_kfold.split(X, y, groups))
    return cv


def get_time_based_CV(X, y, time_index, n_splits=5):
    """
    Args:
        n_splits (int): Similar to K in KFold cross validation analysis
        X: Pandas dataframe for train
        y: list for test
        groups (int): asset id or group id for each sample of X

    Returns:
        An cross validatoin object that can be passed to srom/sklearn pipeline.
    """
    import numpy as np
    from sklearn.model_selection import TimeSeriesSplit

    A = np.array(list(set(time_index)))
    A.sort()
    tscv = TimeSeriesSplit(n_splits=n_splits)
    cv = list(tscv.split(A))
    newCV = []
    for item in cv:
        train_start = A[min(item[0])]
        train_end = A[max(item[0])]

        test_start = A[min(item[1])]
        test_end = A[max(item[1])]

        A_ind = np.where(time_index >= train_start)[0]
        B_ind = np.where(time_index <= train_end)[0]
        train_ind = np.intersect1d(A_ind, B_ind)

        A_ind = np.where(time_index >= test_start)[0]
        B_ind = np.where(time_index <= test_end)[0]
        test_ind = np.intersect1d(A_ind, B_ind)

        newCV.append((train_ind, test_ind))
    return newCV


def get_stratified_KFold_CV(X, y, n_splits=5):
    """
    Args:
        n_splits (int): Similar to K in KFold cross validation analysis
        X: Pandas dataframe for train
        y: list for test
        groups (int): asset id or group id for each sample of X

    Returns:
        An cross validatoin object that can be passed to srom/sklearn pipeline.
    """
    from sklearn.model_selection import StratifiedKFold

    startified_kfold = StratifiedKFold(n_splits=n_splits)
    cv = list(startified_kfold.split(X, y))
    return cv

