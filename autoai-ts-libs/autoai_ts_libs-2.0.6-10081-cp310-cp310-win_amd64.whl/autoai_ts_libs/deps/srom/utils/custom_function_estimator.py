# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Custom function estimator implementation"""
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator


class CustomFunctionEstimator(BaseEstimator):
    """
    Custom Function Estimator could be used to convert your custom function in to an estimator
    Args:
        custom_function (callable object, required): Function to be called
        custom_function_args (dict, optional): dict containing keys as function argument name and
                                               values as argument value
        column_names (list, optional): Column names for pandas dataframe
    """

    def __init__(self, custom_function, custom_function_args=None, column_names=None):
        self.custom_function = custom_function
        self.custom_function_args = {}
        self.column_names = column_names
        if custom_function_args:
            self.custom_function_args = custom_function_args

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
        if isinstance(X, (list, np.ndarray)):
            X = pd.DataFrame(X)
            if self.column_names:
                if len(self.column_names) == X.shape[1]:
                    X.columns = self.column_names
                else:
                    raise Exception(
                        "Size of column_names must be equal to n_features in the input"
                    )

        prediction = self.custom_function(X, **self.custom_function_args)

        if isinstance(prediction, pd.DataFrame):
            df = pd.DataFrame(
                [list(prediction.columns)], columns=list(prediction.columns)
            )
            prediction = df.append(prediction, ignore_index=True)
            prediction = prediction.values

        return prediction


class TransformerPipelineDeployer(BaseEstimator):

    """
    Deploys a transformer only pipeline on WML as a model.

    Args:
        sk_pipeline (sklearn pipeline, required): sk pipeline with only transformer. 
            this pipeline cannot be deployed directly due to the fact sk pipeline with no estimator
            has no predict method.
        predict_params (dict, optional): dict containing keys as function argument name and
                                               values as argument value
        column_names (list, optional): Column names for pandas dataframe
    """

    def __init__(self, sk_pipeline, predict_params=None, column_names=None):
        self.pipeline = sk_pipeline
        self.predict_params = {}
        self.column_names = column_names
        if predict_params:
            self.predict_params = predict_params

    def fit(self, X):
        """Fit is no-op here."""
        return self

    def score(self, X):
        try:
            if isinstance(X, (list, np.ndarray)):
                X = pd.DataFrame(X)
                if self.column_names:
                    if len(self.column_names) == X.shape[1]:
                        X.columns = self.column_names
                    else:
                        raise Exception(
                            "Size of column_names must be equal to n_features in the input"
                        )

            prediction = self.pipeline.fit_transform(X, **self.predict_params)

            # in the case (X, y) are return, only return X
            if isinstance(prediction, tuple):
                return prediction[0]

            if isinstance(prediction, pd.DataFrame):
                df = pd.DataFrame(
                    [list(prediction.columns)], columns=list(prediction.columns)
                )
                prediction = df.append(prediction, ignore_index=True)
                prediction = prediction.values

            return prediction

        except Exception as e:
            return {str(e): repr(e)}

    def predict(self, X):
        """
        Calls function with the provided arguments
        Args:
            X (pandas dataframe, required): Data to be passed to the function
        Returns:
            numpy array: Output of the function execution
        """
        return self.score(X)
