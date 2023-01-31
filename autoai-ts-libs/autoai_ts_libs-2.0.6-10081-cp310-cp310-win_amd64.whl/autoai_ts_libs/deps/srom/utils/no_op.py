﻿# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Maintains NoOp utility functions
"""
from sklearn.base import BaseEstimator, TransformerMixin


class NoOp(BaseEstimator, TransformerMixin):
    """
    A no operation transformer to be used in case the user wants to use an empty fill
    in a stage in SROMPipeline.
    For example, if user wants to try PCA as data transformation before applying
    RandomForestRegressor and also wants to try RandomForestRegressor on the original dataset,
    the SROMPipeline stages would be [[PCA(), NoOp()], [RandomForestRegressor()]]
    """

    def __init__(self):
        pass

    def fit(self, *args):
        """No operation fit"""
        return self

    def transform(self, X, *args):
        """No operation transform"""
        return X
