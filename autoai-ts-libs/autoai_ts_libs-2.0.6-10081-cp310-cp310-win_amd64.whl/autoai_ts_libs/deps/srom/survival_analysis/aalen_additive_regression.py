# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
This class provides survival analysis using Aalen's additive model.
"""
import copy
import numpy as np
import pandas as pd
import logging
from lifelines import AalenAdditiveFitter
from lifelines.utils import concordance_index
from sklearn.base import BaseEstimator, TransformerMixin

LOGGER = logging.getLogger(__name__)


class AalenAdditiveRegression(BaseEstimator, TransformerMixin):
    """
    Performs survival analysis using Aalen's additive model
    """

    def __init__(self, duration_column, event_column=None, base_model=None):
        """
        AalenAdditiveRegression
        """
        self.duration_column = duration_column
        self.event_column = event_column
        self.base_model = base_model
        if not self.base_model:
            self.base_model = AalenAdditiveFitter(fit_intercept=False)
        self.fitted = False
        self.estimator = None

    def set_params(self, **kwarg):
        """
        Used to set params
        """
        if "duration_column" in kwarg:
            self.duration_column = kwarg["duration_column"]
        if "event_column" in kwarg:
            self.event_column = kwarg["event_column"]

        base_model_params = {}
        for d_item in kwarg:
            if "base_model__" in d_item:
                base_model_params[d_item.split("base_model__")[1]] = kwarg[d_item]
        for item_val in base_model_params:
            self.base_model.__setattr__(item_val, base_model_params[item_val])
        return self

    def get_params(self, deep=False):
        out_keys = {}
        out_keys["duration_column"] = self.duration_column
        out_keys["event_column"] = self.event_column
        if deep:
            out_keys["base_model__coef_penalizer"] = self.base_model.coef_penalizer
            out_keys["base_model__fit_intercept"] = self.base_model.fit_intercept
            out_keys[
                "base_model__smoothing_penalizer"
            ] = self.base_model.smoothing_penalizer
        return out_keys

    def _check_fitted_model(self):
        if not self.fitted:
            raise Exception("model is not fitted.")

    def fit(self, X, y=None, **fit_params):
        """
        Fit method

        Args:
            X (Pandas dataframe, required): Input Data
            y (Pandas dataframe, optional): Currently not used, included to be consistent
                                            with the sklearn pipeline interface
        kwargs:
            fit_params:
             Currently not used, included to be consistent with the sklearn pipeline interface
        Returns:
            self
        """
        x_copy = X.copy()
        est = copy.deepcopy(self.base_model)
        est.fit(x_copy, self.duration_column, self.event_column)
        self.estimator = est
        self.fitted = True
        return self

    def predict(self, X):
        """
        Args:
            X (Pandas dataframe, required): Each row represents a different data point to predict.
        Returns:
            DataFrame containing predicted values for each set of inputs.
            DataFrame contains one column with each row of the column containing a predicated value.
        """
        self._check_fitted_model()
        if isinstance(X, (list, np.ndarray)):
            X = pd.DataFrame(X).values
        return self.estimator.predict_expectation(X).values

    def score(self, X=None, y=None):
        """
        The score method expected by sklearn.  Currently, parameters are not used, but they could be in the future.

        Args:
            X (Pandas dataframe): a (n,d) covariate numpy array or DataFrame.
                If a DataFrame, columns can be in any order.
                If a numpy array, columns must be in the same order as the training data.
            y (numpy vector): ground-truth survival times.
        Returns:
            concordance
        """
        self._check_fitted_model()
        preds = self.estimator.predict_expectation(X).values
        return self.estimator.score_
        # return concordance_index(y, preds)

    def plot(self):
        """
        Plots results of regression analysis
        """
        try:
            import matplotlib.pyplot as plt
        except ImportError as _:
            LOGGER.warning(
                "Cannot import matplotlib.pyplot. Drawing of plots will not be possible."
            )
            return
        self._check_fitted_model()
        self.estimator.plot()
        plt.show()

    def information(self):
        """
        Provides valuable information to users
        """
        self.plot()
