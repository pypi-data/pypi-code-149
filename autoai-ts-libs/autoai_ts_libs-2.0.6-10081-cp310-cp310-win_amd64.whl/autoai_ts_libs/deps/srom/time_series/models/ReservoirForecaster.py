import pandas as pd
import numpy as np
import math
import scipy.stats as st
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from collections import namedtuple
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.base import BaseEstimator
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator
from scipy import sparse

class ReservoirForecaster(BaseEstimator, StateSpaceEstimator):
    """
    Reservoir Forecaster.

    Parameters
    ----------
        trend : (string, default = Linear) It can be Linear, Mean, Poly.
        residual : (string, default = Linear) It can be Linear, Difference.
        lookback_win : (int or string, default = auto) Look-back window for the model.
        pred_win : (int, optional, default = 12) Look-ahead window for the model.
    """

    def __init__(
        self,
        hidden_units=500, 
        connectivity=0.25, 
        spectral_radius=0.6,
        activation='tanh',
        time_column=-1,
        feature_columns=[0],
        target_columns=[0],
        lookback_win=10,
        pred_win=1,
        random_state=42,
    ):
        self.hidden_units = hidden_units
        self.connectivity = connectivity
        self.spectral_radius = spectral_radius
        self.activation = activation
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.random_state = random_state

    def _pre_fit_initialize(self, input_size, output_size):
        """
        This is a pre-initialization stage
        """
        np.random.seed(self.random_state)
        self.W_in_  = np.random.uniform(-0.1, 0.1, (input_size, self.hidden_units))
        internal_weights = sparse.rand(self.hidden_units,self.hidden_units,density=self.connectivity).todense()
        internal_weights[np.where(internal_weights > 0)] -= 0.5
        E, _ = np.linalg.eig(internal_weights)
        e_max = np.max(np.abs(E))
        internal_weights /= np.abs(e_max) / self.spectral_radius
        self.W_s_ = internal_weights
        self.W_fb_ = np.random.uniform(-0.1, 0.1, (output_size, self.hidden_units))
        if self.activation == 'tanh':
            self.activation_fun_ = np.tanh

    def fit(self, X, y=None):
        """
        Fit the model.
        Parameters
        ----------
            X : (numpy array) input data.
            y : None.
        Returns
        -------
            self : object
        """
        # automatically infer the lookback window for this model (only one time)
        self._pre_fit_initialize(X.shape[1], X.shape[1])

        # start with univariate time series, one step ahead forecasting
        self.lookback_data_X_ = X[(X.shape[0] - self.lookback_win) :, :]
        y = X[1:]
        x = X[:-1]

        last_state = np.zeros((1, self.hidden_units))
        last_output = np.zeros_like(y[[0]])
        states = []
        for t in range(x.shape[0]):
            current_input = x[[t]]
            state = current_input.dot(self.W_in_) + last_state.dot(self.W_s_) + last_output.dot(self.W_fb_)
            state = self.activation_fun_(np.array(state.astype(float)))
            states.append(state)
            last_state = state
            last_output = y[[t]]

        self.w_out_ = LinearRegression()
        self.w_out_.fit(np.array(np.concatenate(states, axis=0)), np.array(y))
        # store useful parameters
        self.last_state_ = last_state
        self.last_output_ = last_output
        return self

    def predict(self, X, prediction_type='sliding'):
        """
        Adding Predict Function
        """
        states = []
        forecast_len = X.shape[0]

        if self.lookback_win > 0 and prediction_type != 'training':
            X = np.concatenate([self.lookback_data_X_, X]).copy()
            last_state = self.last_state_.copy()
            last_output = self.last_output_.copy()
        else:
            last_state = np.zeros((1, self.hidden_units))
            last_output = np.zeros_like(X[[0]])

        for i in range(self.lookback_win, X.shape[0]):
            for p in reversed(range(1, self.lookback_win + 1)):              
                current_state = X[i-p].dot(self.W_in_) + last_state.dot(self.W_s_) + last_output.dot(self.W_fb_)
                current_state = self.activation_fun_(current_state.astype(float))
                last_state = current_state
                last_output = X[i-p+1]
            states.append(last_state)
        outputs = self.w_out_.predict(np.array(np.concatenate(states, axis=0)))
        return outputs.astype(np.float_)[-forecast_len:]
