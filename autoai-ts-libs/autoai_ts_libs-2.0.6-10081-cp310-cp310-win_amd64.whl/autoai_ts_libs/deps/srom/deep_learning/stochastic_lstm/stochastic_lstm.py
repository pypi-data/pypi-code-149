# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import numpy as np
import tensorflow as tf
from sklearn.base import BaseEstimator
from sklearn.metrics import mean_absolute_error
from sklearn.utils.validation import check_is_fitted

from autoai_ts_libs.deps.srom.deep_learning.stochastic_lstm.differencing_discretizer import (
    DifferencingDiscretizerTransformer
)
from autoai_ts_libs.deps.srom.deep_learning.stochastic_lstm.multivariate_de_rnn import MultivariateDERNN
from autoai_ts_libs.deps.srom.deep_learning.stochastic_lstm.univariate_de_rnn import UnivariateDERNN
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import TimeTensorTransformer


class StochasticLSTM(BaseEstimator):
    def __init__(
        self,
        feature_list,
        control_list=[],
        window_size=100,
        n_bins=100,
        rnn_state_size=128,
        rnn_layers=1,
        lr=0.1,
        batch_size=32,
        predict_num_samples=20 * 10 ** 3,
        distribution_regularizer=0.1,
        bin_size_expansion=0.1,
        steps=100,
        model_dir=None,
        score_func=mean_absolute_error,
    ):
        """
        feature_list (list of indices, required): list of column indices to predict
        control_list (list of indices, required): list of column indices to use as
            exogenous predictors, default: empty list ([])

        """
        self.feature_list = feature_list
        self.control_list = control_list
        self.n_bins = n_bins

        self.control_size = len(control_list)
        self.input_size = len(feature_list)
        self.rnn_state_size = rnn_state_size
        self.rnn_layers = rnn_layers
        self.predict_num_samples = predict_num_samples
        self.distribution_regularizer = distribution_regularizer
        self.lr = lr
        self.batch_size = batch_size
        self.window_size = window_size
        self.steps = steps

        self.bin_size_expansion = bin_size_expansion
        self.diff_trans = DifferencingDiscretizerTransformer(
            self.n_bins, self.feature_list, bin_size_expansion=self.bin_size_expansion
        )
        self.model_dir = model_dir
        self.score_func = score_func

    def set_params(self, **kwarg):
        """
        Used to set params.
        """

        if "window_size" in kwarg:
            self.window_size = kwarg["window_size"]
        if "n_bins" in kwarg:
            self.n_bins = kwarg["n_bins"]
        if "rnn_state_size" in kwarg:
            self.rnn_state_size = kwarg["rnn_state_size"]
        if "rnn_layers" in kwarg:
            self.rnn_layers = kwarg["rnn_layers"]
        if "lr" in kwarg:
            self.lr = kwarg["lr"]
        if "batch_size" in kwarg:
            self.batch_size = kwarg["batch_size"]
        if "distribution_regularizer" in kwarg:
            self.distribution_regularizer = kwarg["distribution_regularizer"]

        if hasattr(self, 'estimator'):
            for k in self.estimator._params.keys():
                if k in kwarg:
                    self.estimator._params[k] = kwarg[k]
        return self

    def get_params(self, deep=False):
        """
        Used to get params.
        """
        model_param = {}
        model_param["window_size"] = self.window_size
        model_param["n_bins"] = self.n_bins
        model_param["rnn_state_size"] = self.rnn_state_size
        model_param["rnn_layers"] = self.rnn_layers
        model_param["lr"] = self.lr
        model_param["batch_size"] = self.batch_size
        model_param["distribution_regularizer"] = self.distribution_regularizer

        return model_param

    def _transform_and_segment(self, X):
        """
        Helper function to transform and segment data prior to fitting.


        X (2D numpy array, time is first axis, required): input data, which
            has the same width as original training data. This must contain
            any control variables that are necessary.
        """
        # Check that we haven't already trained the transformer responsible
        # for differencing and binning our data
        if not hasattr(self.diff_trans, "bins"):
            labels_all = self.diff_trans.fit_transform(X)
        else:
            labels_all = self.diff_trans.transform(X)

        # @ todo
        # don't create a truncated Xnew, just add labels_all
        # fix diff_trans so that it is cauals
        # use a real target_col instead of hacking the TTT
        # this should make all the index jockeying much simpler
        #
        # join with original data
        # Xnew = np.hstack((X[:, self.feature_list + self.control_list], labels_all))[:-1]
        Xnew = np.hstack([X, labels_all])[:-1,]
        # labels are all the columns added to X
        label_col_index = list(range(X.shape[1], Xnew.shape[1]))

        feature_columns = self.feature_list + self.control_list + label_col_index

        # Check that we haven't already fitted the time tensor transformer
        if not hasattr(self, "T"):
            # slightly abuse Time Tensor functionality, no target, not lookahead
            self.T = TimeTensorTransformer(
                feature_columns=feature_columns,
                target_columns=[],
                lookback_win=self.window_size,
                pred_win=0,
            )
            inputs, _ = self.T.fit_transform(Xnew)
        else:
            inputs, _ = self.T.transform(Xnew)
        labels = np.copy(inputs[:, :, -len(label_col_index) :]).astype(np.int64)
        controls = np.copy(
            inputs[
                :,
                :,
                len(self.feature_list) : len(self.feature_list) + self.control_size,
            ]
        )
        inputs = np.copy(inputs[:, :, : len(self.feature_list)])

        # create final input dictionary
        inputs = {"inputs": inputs, "controls": controls}
        return inputs, labels

    def fit(self, X, y=None, **kwargs):
        """
        Fit the univariate stochastic LSTM model.


        X (2D numpy array, time is first axis, required): input data, which
            has the same width as original training data. This must contain
            any control variables that are necessary.
        y (numpy array, optional): not used.
        """
        inputs, labels = self._transform_and_segment(X)

        train_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
            inputs, labels, shuffle=True, batch_size=self.batch_size, num_epochs=100
        )

        # only rebuild model if it doesn't exist already
        if not hasattr(self, "model"):
            if self.input_size == 1:
                self.model = UnivariateDERNN(
                    bins=self.diff_trans.bins[0],
                    control_size=self.control_size,
                    rnn_state_size=self.rnn_state_size,
                    rnn_layers=self.rnn_layers,
                    lr=self.lr,
                    predict_num_samples=self.predict_num_samples,
                    reg_lambda=self.distribution_regularizer,
                )
            else:
                self.model = MultivariateDERNN(
                    bins=self.diff_trans.bins,
                    input_size=self.input_size,
                    control_size=self.control_size,
                    rnn_state_size=self.rnn_state_size,
                    rnn_layers=self.rnn_layers,
                    lr=self.lr,
                    predict_num_samples=self.predict_num_samples,
                    reg_lambda=self.distribution_regularizer,
                )
            self.estimator = tf.estimator.Estimator(
                model_fn=self.model.model_fn, params={}, model_dir=self.model_dir
            )
        steps = kwargs.get("steps", self.steps)
        self.estimator.train(train_input_fn, steps=steps)
        return self

    def predict(
        self, X, prediction_type="rowwise", W=None, full_output=False, horizon=10
    ):
        """Return predictions for a trained model. This function handles both 1-step ahead in sample
        predictions as well as future predictions (forecast).

        Args:
            X (Numpy array): Input data.
            prediction_type (str, optional): Two values are possible:
                rowwise: make 1-step ahead predictions for each input row in the data.
                forecast: make an horizon-step ahead prediction continuing from the end of the data.
                    In this case user should specify "horizon" option (defaults to 10) and optionally
                    matrix of data containing control values "W" option.

                Defaults to "rowwise".
            W (Numpy array, optional): Contains future values for control variables. Defaults to None.
            full_output (boolean, optional): If true will provide additional outputs from the model.
                Defaults to False. Outputs depend on the prediction_type and are as follows:
                prediction_type=="rowwise":
                    'logits': logit values
                    'predictions_1step_mean': mean value based on estimated probabilities of distribution
                    'predictions_1step_var': variance based on estimated probabilities of distribution
                    'predictions_distribution': estimated probabilities of each bin in the discretized distribution
                prediction_type=="forecast":
                    'logits', 'predictions_1step_mean', 'predictions_1step_var', 'predictions_distribution': same
                        as prediction_type=="rowwise" for the input data X (in sample)
                    'multistep_mean': mean value of the prediction over the forecast horizon (one value per
                        timestep, per dimension)
                    'multistep_var': variance of the predictions over the forecast horizon (one value per
                        time-step, per dimension)
                    'multistep_raw': all the separate realizations of the predictions over the forecast horizon
                        this is the raw data used to calculate 'multistep_mean' and 'multistep_var'.
            horizon (int, optional): Number of future time periods to predict when forecasting
                (prediction_type=="forecast"). Defaults to 10. This option is ignored when prediction_type=="rowwise".

        Raises:
            ValueError: When a user provides an invalid value for `prediction_type`

        Returns:
            Numpy array of predictions.
            If `full_output`==True, the the output will be a dictionary of numpy arrays as described above.
        """

        if prediction_type == "rowwise":
            return self._predict(X, full_output=full_output)
        elif prediction_type == "forecast":
            return self._forecast(X, W=W, horizon=horizon, full_output=full_output)
        else:
            raise ValueError(
                "Argument prediction_type must be either `rowwise` or `forecast`"
            )

    def _predict(self, X, full_output=False):
        """
        Return single step prediction results for input X. Note that we
        produce a prediction for each value in X.


        X (2D numpy array, time is first axis, required): input data, which
            has the same width as original training data. This must contain
            any control variables that are necessary.

        """
        check_is_fitted(self, ("model", "estimator"))

        # it should be that len(X.shape) == 2
        inputs = {
            "inputs": np.expand_dims(X[:, self.feature_list], axis=0),
            "controls": np.expand_dims(X[:, self.control_list], axis=0),
        }
        # 'pred_controls': np.array([],dtype=np.float32).reshape(1, t2-t, 0)

        predict_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
            inputs, shuffle=False
        )  # , batch_size=X.shape[0])

        out = list(self.estimator.predict(predict_input_fn))[0]
        if full_output:
            return out
        else:
            return out["predictions_1step_mean"]

    def _forecast(self, X, W=None, horizon=10, full_output=False):
        """
        Produce a forecast of the features for a number of future steps

        The order of the columns in W, must be consistent with the order of
        the columns specified by self.control_list.
        """

        check_is_fitted(self, ("model", "estimator"))

        if (W is None and self.control_size > 0) or (
            self.control_size > 0 and W.shape != (horizon, self.control_size)
        ):
            raise ValueError(
                "Appropriate control variables need to be provided for forecasting."
            )

        inputs = {
            "inputs": np.expand_dims(X[:, self.feature_list], axis=0),
            "controls": np.expand_dims(X[:, self.control_list], axis=0),
        }

        if self.control_size == 0:
            inputs["pred_controls"] = np.array([]).reshape(1, horizon, 0)
        else:
            inputs["pred_controls"] = np.expand_dims(W, axis=0)

        forecast_input_fn = tf.compat.v1.estimator.inputs.numpy_input_fn(
            inputs, shuffle=False
        )

        out = list(self.estimator.predict(forecast_input_fn))[0]
        if full_output:
            return out
        else:
            return out["multistep_mean"]

    def score(self, X, y=None):
        """
        Scoring function handler, to be used during training / cross
        validation. We assume that the provided y is none, given that
        the data is internally transformed.
        """

        # estimator is based on 1-step ahead predictions
        y_true = X[:, self.feature_list][1:]
        y_pred = self.predict(X)[:-1]

        return self.score_func(y_true, y_pred)
