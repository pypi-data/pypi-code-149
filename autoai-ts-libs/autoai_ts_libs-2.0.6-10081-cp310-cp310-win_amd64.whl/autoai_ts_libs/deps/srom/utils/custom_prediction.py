# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Custom function estimator implementation"""
from sklearn.base import BaseEstimator


class CustomPrediction(BaseEstimator):
    """
    Custom Function Estimator could be used to convert your custom function in to an estimator
    Args:
        custom_function (callable object, required): Function to be called
        custom_function_args (dict, optional): dict containing keys as function argument name and
                                                values as argument value
    """

    def __init__(self, column_names=None):
        self.column_names = column_names

    def fit(self, X):
        """Fit is no-op here."""
        return self

    def predict(self, X):
        """
        Calls function with the provided arguments
        Args:
            X (pandas dataframe, required): Data to be passed to the function
        Returns:
            numpy array: Output of the function execution
        """
        return self.column_names
