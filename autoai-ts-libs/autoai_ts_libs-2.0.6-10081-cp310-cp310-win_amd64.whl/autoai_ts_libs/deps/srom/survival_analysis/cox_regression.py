# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
This class provides survival analysis using the Cox regression.
"""
import copy
import numpy as np
import pandas as pd
import logging
from lifelines import CoxPHFitter
from lifelines.utils import concordance_index

from sklearn.base import BaseEstimator, TransformerMixin

LOGGER = logging.getLogger(__name__)


class CoxRegression(BaseEstimator, TransformerMixin):
    """
    Performs survival analysis using Cox regression
    """

    def __init__(
        self,
        duration_column,
        event_column=None,
        base_model=None,
        alpha=0.05,
        tie_method="Efron",
        penalizer=0.0,
        strata=None,
    ):
        """
        For Cox regression

        :param duration_column:
        :param event_column:
        :param base_model:
        :param alpha: float, optional (default=0.05)
            the level in the confidence intervals.
        :param tie_method: string, optional
            specify how the fitter should deal with ties. Currently only
            'Efron' is available.
        :param penalizer: float, optional (default=0.0)
            Attach an L2 penalizer to the size of the coefficients during regression. This improves
            stability of the estimates and controls for high correlation between covariates.
            For example, this shrinks the absolute value of :math:`\beta_i`.
            The penalty is :math:`\frac{1}{2} \text{penalizer} ||\beta||^2`.
        :param strata: list, optional
            specify a list of columns to use in stratification. This is useful if a
            categorical covariate does not obey the proportional hazard assumption. This
            is used similar to the `strata` expression in R.
            See http://courses.washington.edu/b515/l17.pdf.
            """
        self.duration_column = duration_column
        self.event_column = event_column
        self.base_model = base_model
        if not self.base_model:
            self.base_model = CoxPHFitter(
                alpha=alpha, tie_method=tie_method, penalizer=penalizer, strata=strata
            )
        self.fitted = False  # this field prevents fit from being called multiple times
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
            out_keys["base_model__penalizer"] = self.base_model.penalizer
        return out_keys

    def _check_fitted_model(self):
        if not self.fitted:
            raise Exception("model is not fitted.")

    def fit(
        self,
        X,
        y=None,
        show_progress=False,
        strata=None,
        step_size=None,
        weights_col=None,
    ):
        """
        Fit method.

        Args:
            X (Pandas dataframe, required): 0th column contains durations.
                1st column has a 1 if event was observed, 0 otherwise.
                Remaining columns contain covariates.
            y (Pandas dataframe, optional):
                Currently not used, included to be consistent with the sklearn pipeline interface
        show_progress: boolean, optional (default=False)
            since the fitter is iterative, show convergence
            diagnostics. Useful if convergence is failing.
        strata: list or string, optional
            specify a column or list of columns n to use in stratification. This is useful if a
            categorical covariate does not obey the proportional hazard assumption. This
            is used similar to the `strata` expression in R.
            See http://courses.washington.edu/b515/l17.pdf.
        step_size: float, optional
            set an initial step size for the fitting algorithm. Setting to 1.0 may improve performance, but could also hurt convergence.
        weights_col: string, optional
            an optional column in the DataFrame, df, that denotes the weight per subject.
            This column is expelled and not used as a covariate, but as a weight in the
            final regression. Default weight is 1.
            This can be used for case-weights. For example, a weight of 2 means there were two subjects with
            identical observations.
            This can be used for sampling weights. In that case, use `robust=True` to get more accurate standard errors.

        Returns:
            self
        """
        x_copy = X.copy()
        est = copy.deepcopy(self.base_model)
        est.fit(
            x_copy,
            self.duration_column,
            self.event_column,
            show_progress=show_progress,
            strata=strata,
            step_size=step_size,
            weights_col=weights_col,
        )
        self.estimator = est
        self.fitted = True
        return self

    def predict(self, X):
        """
        Args:
            X (Pandas dataframe, optional): a (n,d) covariate numpy array or DataFrame.
                If a DataFrame, columns can be in any order.
                If a numpy array, columns must be in the same order as the training data.
                Each row represents a different data point to predict.
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
        The score method expected by sklearn. Currently, parameters are not used, but they could be in the future.
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

    def print_summary(self):
        """
        Print important information from analyzing the training data
        """
        self._check_fitted_model()
        self.estimator.print_summary()

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
        self._check_fitted_model()
        self.print_summary()
        self.plot()
