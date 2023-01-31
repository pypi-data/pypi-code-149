# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: deep_autoencoder_anomaly_detector
   :synopsis: Deep AE Anomaly Detector - Wrapper for \
       Anomaly Detector using Autoencoder Deep Networks.

.. moduleauthor:: SROM Team
"""

# this class will define the auto-encoder based Anomaly Detector
from autoai_ts_libs.deps.srom.utils.estimator_utils import BuildFnWrapper
from scikeras.wrappers import KerasRegressor
from autoai_ts_libs.deps.srom.deep_learning.auto_encoders.dnn import deep_autoencoder
from autoai_ts_libs.deps.srom.deep_learning.auto_encoders.lstm import simple_lstm_autoencoder
from autoai_ts_libs.deps.srom.deep_learning.auto_encoders.cnn import cnn_ae, simple_cnn
from autoai_ts_libs.deps.srom.deep_learning.auto_encoders.variational_dnn import variational_autoencoder
from autoai_ts_libs.deps.srom.deep_learning.base import BaseAutoEncoderAnomalyDetector
import numpy as np
import types
import copy
from tensorflow.python.keras import losses
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from keras.utils.generic_utils import has_arg

RANDOM_STATE = 42
tf.random.set_seed(RANDOM_STATE)


def set_seed(random_seed):
    tf.random.set_seed(random_seed)


class EarlyStoppingAutoEncoder(KerasRegressor):
    """
    Fit function performs early stopping for dynamic training
    """

    def fit(self, X, y, **kwargs):
        """Constructs a new model with `build_fn` & fit the model to `(x, y)`.

        Args:
            X : array-like, shape `(n_samples, n_features)`
                Training samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            y : array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
                True labels for `x`.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.fit`

        Returns:
            history : object
                details about the training history at each epoch.
        """
        if self.build_fn is None:
            self.model_ = self.__call__(**self.filter_sk_params(self.__call__))
        elif (not isinstance(self.build_fn, types.FunctionType) and
              not isinstance(self.build_fn, types.MethodType)):
            self.model_ = self.build_fn(
                **self.filter_sk_params(self.build_fn.__call__))
        else:
            self.model_ = self.build_fn(**self.filter_sk_params(self.build_fn))
        set_seed(RANDOM_STATE)

        if (losses.is_categorical_crossentropy(self.model_.loss) and
                len(y.shape) != 2):
            y = to_categorical(y)
        if 'val_data' in kwargs and kwargs['val_data'] is not None:
            es = tf.keras.callbacks.EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=2,
                                                  min_delta=0.0001)
            val_data = kwargs['val_data']
            del kwargs['val_data']
        else:
            es = tf.keras.callbacks.EarlyStopping(monitor='loss', mode='min', verbose=1, patience=2,
                                                  min_delta=0.0001)
            val_data = None
            if 'val_data' in kwargs:
                del kwargs['val_data']
        fit_args = copy.deepcopy(self.filter_sk_params(Sequential.fit))
        fit_args.update(kwargs)
        fit_args.update({'callbacks': [es]})
        X_dtype_ = X.dtype
        X_shape_ = X.shape
        n_features_in_ = X.shape[-1]
        self.X_dtype_ = X_dtype_
        self.X_shape_ = X_shape_
        self.n_features_in_ = n_features_in_
        if val_data is not None:
            fit_args.update({'validation_data': (val_data, val_data)})
        self.feature_encoder_ = self.feature_encoder.fit(X)
        self.target_encoder_ = self.target_encoder.fit(y)
        # This is accepted in later versions of keras.engine.training.py and not an acceptable param in training_v1.
        if 'validation_batch_size' in fit_args:
            del fit_args['validation_batch_size']
        history = self.model_.fit(X, y, **fit_args)
        self.history_ = history
        return self

    def filter_sk_params(self, fn, override=None):
        """Filters `get_params()` and returns those in `fn`'s arguments.
        Args:
            fn : arbitrary function
            override: dictionary, values to override `get_params()`
        Returns:
            res : dictionary containing variables
                in both `get_params()` and `fn`'s arguments.
        """
        override = override or {}
        res = {}
        for name, value in self.get_params().items():
            if has_arg(fn, name):
                res.update({name: value})
        res.update(override)
        return res

    def predict(self, X, **kwargs):
        """
        Predict values.

        If the base is a keras regressor, in order to be compatible with generalized anomaly model, predict should be
        overridden with the upper case X as a parameter, since GeneralizedAnomalyModel checks the signature of the
        function, and produces NaNs if method is not overridden.
        """
        self._initialize_callbacks()

        return super(EarlyStoppingAutoEncoder, self).predict(X, **kwargs)


# class to be build for geenral purpose anomaly detection based on Encode
class DNNAutoEncoder(EarlyStoppingAutoEncoder, BaseAutoEncoderAnomalyDetector):
    """[summary]

    Args:
        KerasRegressor ([type]): [description]
    """

    def __init__(
            self,
            input_dimension=None,
            encoding_dimension=None,
            loss="mean_squared_error",
            build_fn=None,
            verbose=3,
            random_state=42,
            **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type], optional): [description]. Defaults to None.
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            hidden_dimension (int, optional): [description]. Defaults to 10.
            random_state (int, optional): random state. Defaults to 42.
            activation (str, optional): [description]. Defaults to "relu".
            output_activation (str, optional): [description]. Defaults to "linear".
            kernel_initializer (str, optional): [description]. Defaults to "normal".
            dropout_rate (float, optional): [description]. Defaults to 0.2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(deep_autoencoder)
        set_seed(random_state)
        super(DNNAutoEncoder, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            encoding_dimension=encoding_dimension,
            loss=loss,
            verbose=verbose,
            **kwargs,
        )

    def __str__(self):
        return (
                "DNNAutoEncoder"
                + "(input_dimension="
                + str(self.get_params()["input_dimension"])
                + ", encoding_dimension="
                + str(self.get_params()["encoding_dimension"])
                + ", loss="
                + str(self.get_params()["loss"])
                + ")"
        )

    def fit(self, X, y=None, **kwargs):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.
        """

        # set the parameter based on the incoming X if it is not set
        if self.get_params()["input_dimension"] is None:
            self.set_params(**{"input_dimension":X.shape[1]})
        if self.get_params()["encoding_dimension"] is None:
            self.set_params(**{"encoding_dimension":np.max([int(X.shape[1] / 2), 3])})
        super(DNNAutoEncoder, self).fit(
            X,
            X,
            **kwargs,
        )


# class to be build for geenral purpose anomaly detection based on Encode
class LSTMAutoEncoder(EarlyStoppingAutoEncoder):
    """[summary]

    Args:
        KerasRegressor ([type]): [description]
    """

    def __init__(
            self, input_dimension=None, hidden_dimension=None, build_fn=None, random_state=42, loss="mean_squared_error", **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type], optional): [description]. Defaults to None.
            output_dimension ([type], optional): [description]. Defaults to None.
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            random_state (int, optional): random state. Defaults to 42.
            hidden_dimension (int, optional): [description]. Defaults to 10.
            activation (str, optional): [description]. Defaults to "relu".
            output_activation (str, optional): [description]. Defaults to "linear".
            kernel_initializer (str, optional): [description]. Defaults to "normal".
            dropout_rate (float, optional): [description]. Defaults to 0.2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(simple_lstm_autoencoder)
        set_seed(random_state)
        super(LSTMAutoEncoder, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            hidden_dimension=hidden_dimension,
            loss=loss,
            **kwargs,
        )

    def __str__(self):
        return (
                "LSTMAutoEncoder"
                + "(input_dimension="
                + str(self.get_params()["input_dimension"])
                + ", hidden_dimension="
                + str(self.get_params()["hidden_dimension"])
                + ")"
        )

    def fit(self, x, y, **kwargs):
        """Constructs a new model with `build_fn` & fit the model to `(x, y)`.

        Args:
            x : array-like, shape `(n_samples, n_features)`
                Training samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            y : array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
                True labels for `x`.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.fit`

        Returns:
            history : object
                details about the training history at each epoch.
        """
        super(LSTMAutoEncoder, self).fit(
            x,
            y,
            **kwargs,
        )


class CNNAutoEncoder(EarlyStoppingAutoEncoder):
    """[summary]

    Args:
        KerasRegressor ([type]): [description]
    """

    def __init__(
            self, input_dimension=None, build_fn=None, random_state=42,  loss="mean_squared_error", **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type], optional): [description]. Defaults to None.
            output_dimension ([type], optional): [description]. Defaults to None.
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            random_state (int, optional): random state. Defaults to 42.
            hidden_dimension (int, optional): [description]. Defaults to 10.
            activation (str, optional): [description]. Defaults to "relu".
            output_activation (str, optional): [description]. Defaults to "linear".
            kernel_initializer (str, optional): [description]. Defaults to "normal".
            dropout_rate (float, optional): [description]. Defaults to 0.2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(simple_cnn)
        set_seed(random_state)
        super(CNNAutoEncoder, self).__init__(
            build_fn=build_fn, input_dimension=input_dimension, loss=loss, **kwargs,
        )

    def __str__(self):
        return (
                "CNNAutoEncoder"
                + "(input_dimension="
                + str(self.get_params()["input_dimension"])
                + ")"
        )

    def fit(self, x, y, **kwargs):
        """Constructs a new model with `build_fn` & fit the model to `(x, y)`.

        Args:
            x : array-like, shape `(n_samples, n_features)`
                Training samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            y : array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
                True labels for `x`.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.fit`

        Returns:
            history : object
                details about the training history at each epoch.
        """
        super(CNNAutoEncoder, self).fit(
            x,
            y,
            **kwargs,
        )


class DNNVariationalAutoEncoder(EarlyStoppingAutoEncoder):
    """[summary]

    Args:
        KerasRegressor ([type]): [description]
    """

    def __init__(
            self, input_dimension=None, generator_dimension=None, build_fn=None, random_state=42,  loss="mean_squared_error", **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type], optional): [description]. Defaults to None.
            output_dimension ([type], optional): [description]. Defaults to None.
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            random_state (int, optional): random state. Defaults to 42.
            hidden_dimension (int, optional): [description]. Defaults to 10.
            activation (str, optional): [description]. Defaults to "relu".
            output_activation (str, optional): [description]. Defaults to "linear".
            kernel_initializer (str, optional): [description]. Defaults to "normal".
            dropout_rate (float, optional): [description]. Defaults to 0.2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(variational_autoencoder)
        set_seed(random_state)
        super(DNNVariationalAutoEncoder, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            generator_dimension=generator_dimension,
            loss=loss,
            **kwargs,
        )

    def __str__(self):
        return (
                "DNNVariationalAutoEncoder"
                + "(input_dimension="
                + str(self.get_params()["input_dimension"])
                + ", generator_dimension="
                + str(self.get_params()["generator_dimension"])
                + ")"
        )

    def fit(self, x, y, **kwargs):
        """Constructs a new model with `build_fn` & fit the model to `(x, y)`.

        Args:
            x : array-like, shape `(n_samples, n_features)`
                Training samples where `n_samples` is the number of samples
                and `n_features` is the number of features.
            y : array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
                True labels for `x`.
            **kwargs: dictionary arguments
                Legal arguments are the arguments of `Sequential.fit`

        Returns:
            history : object
                details about the training history at each epoch.
        """
        super(DNNVariationalAutoEncoder, self).fit(
            x,
            y,
            **kwargs,
        )
