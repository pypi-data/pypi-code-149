# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
This class provides survival analysis using the Nelson-Aalen estimator.
"""
import copy
import pandas as pd
import logging
from lifelines import NelsonAalenFitter
from sklearn.base import BaseEstimator, TransformerMixin

LOGGER = logging.getLogger(__name__)


class NelsonAalen(BaseEstimator, TransformerMixin):
    """
    Performs survival analysis using the Nelson-Aalen estimator
    """

    def __init__(self, duration_column, event_column=None, base_model=None):
        self.duration_column = duration_column
        self.event_column = event_column
        self.base_model = base_model
        if not self.base_model:
            self.base_model = NelsonAalenFitter()
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
            out_keys[
                "base_model__nelson_aalen_smoothing"
            ] = self.base_model.nelson_aalen_smoothing
        return out_keys

    def _check_fitted_model(self):
        if not self.fitted:
            raise Exception("model is not fitted.")

    # fit method
    def fit(self, X, y=None, **fit_params):
        """
        Args:
            X (Pandas dataframe, required): Pandas dataframe. 0th column contains durations.
                1st column has a 1 if event was observed, 0 otherwise.
        kwargs:
            fit_params:
                Currently not used, included to be consistent with the sklearn pipeline interface.
        Returns:
            self
        """
        est = copy.deepcopy(self.base_model)
        event_observed = None
        if self.event_column:
            event_observed = X[self.event_column]
        est.fit(X[self.duration_column], event_observed=event_observed)
        self.estimator = est
        self.fitted = True
        return self

    def predict(self, X=None):
        """
        The predict method returns the hazard function. Note that the Nelson-Aalen predictor
        is designed to determine hazard functions. It thus does not predict estimated survival
        values, unlike other survival algorithms.

        Args:
            X (Pandas dataframe, optional):
                not used, included for consistency with sklearn pipeline.
        Returns:
            DataFrame containing the hazard function.
        """
        self._check_fitted_model()
        haz_df = self.estimator.cumulative_hazard_.copy()
        haz_df.reset_index(inplace=True)
        df = pd.DataFrame([list(haz_df.columns)], columns=list(haz_df.columns))
        haz_df = df.append(haz_df, ignore_index=True)
        haz_df = haz_df.values
        return haz_df

    def score(self, X=None, y=None, sample_weight=None):
        """
        The score is given by the concordance probability. The Nelson-Aalen approach, as a non-parametric method,
        cannot distinguish survival probability differences between different data points. Therefore, the concordance
        probability is 0.5, which one can get by randomly selecting one data point as having a longer lifetime than
        another.

        Args:
            X (Pandas dataframe, optional):
                not used, included for consistency with sklearn pipeline.
            y (Pandas dataframe, optional):
                not used, included for consistency with sklearn pipeline.
            sample_weight (<datatype>, optional):
                not used, included for consistency with sklearn pipeline.
        Returns:
            concordance
        """
        return 0.5

    def hazard_function(self):
        """
        Return the hazard function
        Returns:
            DataFrame containing the hazard function
        """
        self._check_fitted_model()
        return self.estimator.cumulative_hazard_

    def plot_hazard_function(self):
        """
        Plots the hazard function
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
        plt.title("Hazard Function")
        plt.show()

    def information(self):
        """
        Provides valuable information to users
        """
        self._check_fitted_model()
        print(self.estimator.cumulative_hazard_)
        self.plot_hazard_function()
