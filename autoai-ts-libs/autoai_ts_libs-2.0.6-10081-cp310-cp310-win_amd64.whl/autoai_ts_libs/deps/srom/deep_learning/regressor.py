# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: regressor
   :synopsis: regressor.

.. moduleauthor:: SROM Team
"""
import numpy as np

from autoai_ts_libs.deps.srom.deep_learning.auto_encoders.dnn import simple_autoencoder, simple_ffn
from autoai_ts_libs.deps.srom.deep_learning.models.cnn import (
    deep_cnn,
    resnet_model,
    seriesNet,
    simple_cnn,
    simple_fcn,
    waveNet,
)
from autoai_ts_libs.deps.srom.deep_learning.models.dnn import deep_dnn, simple_dnn
from autoai_ts_libs.deps.srom.deep_learning.models.inception import inception_time_model
from autoai_ts_libs.deps.srom.deep_learning.models.lstm import (
    deep_lstm,
    fixed_bidirectional_lstm,
    fixed_lstm,
    fixed_seq2seq,
    fixed_seq2seq_attention,
    simple_lstm,
)
from autoai_ts_libs.deps.srom.utils.estimator_utils import BuildFnWrapper
from scikeras.wrappers import KerasRegressor
from keras.utils.generic_utils import has_arg
import types

import logging
LOGGER = logging.getLogger(__name__)

###########################################################
# Standard deep learning Regressor
###########################################################

class DeepLearningRegressor(KerasRegressor):
    def fit(self, X, y, **kwargs):
        if self.build_fn is None:
            self.model_ = self.__call__(**self.filter_sk_params(self.__call__))
        elif (not isinstance(self.build_fn, types.FunctionType) and
              not isinstance(self.build_fn, types.MethodType)):
            self.model_ = self.build_fn(
                **self.filter_sk_params(self.build_fn.__call__))
        else:
            self.model_ = self.build_fn(**self.filter_sk_params(self.build_fn))
        if type(X) != np.ndarray:
            X = np.array(X)
        X_dtype_ = X.dtype
        X_shape_ = X.shape
        n_features_in_ = X.shape[-1]
        self.X_dtype_ = X_dtype_
        self.X_shape_ = X_shape_
        self.n_features_in_ = n_features_in_
        self.feature_encoder_ = self.feature_encoder.fit(X)
        if y is not None and type(y)!=np.ndarray:
            y = np.array(y)
        self.target_encoder_ = self.target_encoder.fit(y)
        history = self.model_.fit(X, y, **kwargs)
        self.history_ = history
        return self

    def predict(self, X, **kwargs):
        """
        Predict values.

        If the base is a keras regressor, in order to be compatible with generalized anomaly model, predict should be
        overridden with the upper case X as a parameter, since GeneralizedAnomalyModel checks the signature of the
        function, and produces NaNs if method is not overridden.
        """
        self._initialize_callbacks()

        return super(DeepLearningRegressor, self).predict(X, **kwargs)

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

class DNNRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension=None,
        output_dimension=None,
        build_fn=None,
        optimizer="adam",
        loss="mean_squared_error",
        hidden_dimension=10,
        activation="relu",
        output_activation="linear",
        kernel_initializer="normal",
        dropout_rate=0.2,
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type], optional): [description]. Defaults to None.
            output_dimension ([type], optional): [description]. Defaults to None.
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
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
            build_fn = BuildFnWrapper(simple_dnn)

        super(DNNRegressor, self).__init__(
            build_fn=build_fn,
            model=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            hidden_dimension=hidden_dimension,
            activation=activation,
            kernel_initializer=kernel_initializer,
            dropout_rate=dropout_rate,
            epochs=epochs,
            batch_size=batch_size,
            output_activation=output_activation,
            **kwargs,
        )


class DeepDNNRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="mean_squared_error",
        hidden_dimension=None,
        activation="relu",
        output_activation="linear",
        kernel_initializer="normal",
        dropout_rate=0.2,
        dropout_first=False,
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            hidden_dimension ([type], optional): [description]. Defaults to None.
            activation (str, optional): [description]. Defaults to "relu".
            output_activation (str, optional): [description]. Defaults to "linear".
            kernel_initializer (str, optional): [description]. Defaults to "normal".
            dropout_rate (float, optional): [description]. Defaults to 0.2.
            dropout_first (bool, optional): [description]. Defaults to False.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(deep_dnn)

        if hidden_dimension is None:
            hidden_dimension = (10, 10, 10)

        super(DeepDNNRegressor, self).__init__(
            build_fn=build_fn,
            model=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            hidden_dimension=hidden_dimension,
            activation=activation,
            output_activation=output_activation,
            kernel_initializer=kernel_initializer,
            dropout_rate=dropout_rate,
            dropout_first=dropout_first,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


###########################################################
# LSTM Regressors
###########################################################
class SimpleLSTMRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="rmsprop",
        loss="mean_squared_error",
        hidden_dimension=10,
        activation="sigmoid",
        kernel_initializer="normal",
        dropout_rate=0.2,
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "rmsprop".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            hidden_dimension (int, optional): [description]. Defaults to 10.
            activation (str, optional): [description]. Defaults to "sigmoid".
            kernel_initializer (str, optional): [description]. Defaults to "normal".
            dropout_rate (float, optional): [description]. Defaults to 0.2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(simple_lstm)

        super(SimpleLSTMRegressor, self).__init__(
            build_fn=build_fn,
            model=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            hidden_dimension=hidden_dimension,
            activation=activation,
            kernel_initializer=kernel_initializer,
            dropout_rate=dropout_rate,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class DeepLSTMRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="rmsprop",
        loss="mean_squared_error",
        hidden_dimension=None,
        activation="sigmoid",
        kernel_initializer="normal",
        dropout_rate=0.2,
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "rmsprop".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            hidden_dimension ([type], optional): [description]. Defaults to None.
            activation (str, optional): [description]. Defaults to "sigmoid".
            kernel_initializer (str, optional): [description]. Defaults to "normal".
            dropout_rate (float, optional): [description]. Defaults to 0.2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(deep_lstm)

        if hidden_dimension is None:
            hidden_dimension = (10, 10, 10)

        super(DeepLSTMRegressor, self).__init__(
            build_fn=build_fn,
            model=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            hidden_dimension=hidden_dimension,
            activation=activation,
            kernel_initializer=kernel_initializer,
            dropout_rate=dropout_rate,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


###########################################################
# CNN Regressors
###########################################################
class SimpleCNNRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        loss="mean_squared_error",
        optimizer="adam",
        hidden_dimension=10,
        activation="relu",
        filters=32,
        kernel_size=2,
        max_pool_size=2,
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            optimizer (str, optional): [description]. Defaults to "adam".
            hidden_dimension (int, optional): [description]. Defaults to 10.
            activation (str, optional): [description]. Defaults to "relu".
            filters (int, optional): [description]. Defaults to 32.
            kernel_size (int, optional): [description]. Defaults to 2.
            max_pool_size (int, optional): [description]. Defaults to 2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(simple_cnn)

        super(SimpleCNNRegressor, self).__init__(
            build_fn=build_fn,
            model=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            hidden_dimension=hidden_dimension,
            activation=activation,
            kernel_size=kernel_size,
            max_pool_size=max_pool_size,
            filters=filters,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class DeepCNNRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        hidden_dimension=10,
        activation="relu",
        loss="mean_squared_error",
        optimizer="adam",
        filters=32,
        kernel_size=2,
        max_pool_size=2,
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            hidden_dimension (int, optional): [description]. Defaults to 10.
            activation (str, optional): [description]. Defaults to "relu".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            optimizer (str, optional): [description]. Defaults to "adam".
            filters (int, optional): [description]. Defaults to 32.
            kernel_size (int, optional): [description]. Defaults to 2.
            max_pool_size (int, optional): [description]. Defaults to 2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(deep_cnn)

        super(DeepCNNRegressor, self).__init__(
            build_fn=build_fn,
            model=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            hidden_dimension=hidden_dimension,
            activation=activation,
            kernel_size=kernel_size,
            max_pool_size=max_pool_size,
            filters=filters,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class WaveNetRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="mean_squared_error",
        filters=32,
        kernel_size=2,
        dilation_layers=8,
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            filters (int, optional): [description]. Defaults to 32.
            kernel_size (int, optional): [description]. Defaults to 2.
            dilation_layers (int, optional): [description]. Defaults to 8.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(waveNet)

        super(WaveNetRegressor, self).__init__(
            build_fn=build_fn,
            model=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            dilation_layers=dilation_layers,
            kernel_size=kernel_size,
            filters=filters,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class SeriesNetRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="mean_squared_error",
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(seriesNet)

        super(SeriesNetRegressor, self).__init__(
            build_fn=build_fn,
            model=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class FCNRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="mean_squared_error",
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(simple_fcn)

        super(FCNRegressor, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class InceptionTimeRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="mean_squared_error",
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(inception_time_model)

        super(InceptionTimeRegressor, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class ResnetRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="mean_squared_error",
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            output_dimension ([type]): [description]
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(resnet_model)

        super(ResnetRegressor, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class FixedLSTMRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension=(1, 1),
        output_dimension=1,
        build_fn=None,
        output_type="flatten",
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension (tuple, optional): [description]. Defaults to (1, 1).
            output_dimension (int, optional): [description]. Defaults to 1.
            build_fn ([type], optional): [description]. Defaults to None.
            output_type (str, optional): [description]. Defaults to "flatten".
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(fixed_lstm)

        super(FixedLSTMRegressor, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            output_type=output_type,
            **kwargs,
        )


class FixedSeq2SeqLSTMRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension=(1, 1),
        output_dimension=1,
        build_fn=None,
        output_type="structured",
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension (tuple, optional): [description]. Defaults to (1, 1).
            output_dimension (int, optional): [description]. Defaults to 1.
            build_fn ([type], optional): [description]. Defaults to None.
            output_type (str, optional): [description]. Defaults to "structured".
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(fixed_seq2seq)

        super(FixedSeq2SeqLSTMRegressor, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            output_type=output_type,
            **kwargs,
        )


class FixedSeq2SeqAttentionLSTMRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension=(1, 1),
        output_dimension=1,
        build_fn=None,
        output_type="structured",
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension (tuple, optional): [description]. Defaults to (1, 1).
            output_dimension (int, optional): [description]. Defaults to 1.
            build_fn ([type], optional): [description]. Defaults to None.
            output_type (str, optional): [description]. Defaults to "structured".
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(fixed_seq2seq_attention)

        super(FixedSeq2SeqAttentionLSTMRegressor, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            output_type=output_type,
            **kwargs,
        )


class FixedBidirectionalLSTM(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension=(1, 1),
        output_dimension=1,
        build_fn=None,
        output_type="flatten",
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension (tuple, optional): [description]. Defaults to (1, 1).
            output_dimension (int, optional): [description]. Defaults to 1.
            build_fn ([type], optional): [description]. Defaults to None.
            output_type (str, optional): [description]. Defaults to "flatten".
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(fixed_bidirectional_lstm)

        super(FixedBidirectionalLSTM, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            output_type=output_type,
            **kwargs,
        )


class AERegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension,
        encoding_dimension=16,
        hidden_dimension=[64,32],
        build_fn=simple_autoencoder,
        optimizer="adam",
        loss="mean_squared_error",
        activation="relu",
        learning_rate=0.001,
        dropout_rate=0,
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type]): [description]
            encoding_dimension (int, optional): [description]. Defaults to 16.
            hidden_dimension (list, optional): [description]. Defaults to [64,32].
            build_fn ([type], optional): [description]. Defaults to simple_autoencoder.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            activation (str, optional): [description]. Defaults to "relu".
            learning_rate (float, optional): [description]. Defaults to 0.001.
            dropout_rate (int, optional): [description]. Defaults to 0.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """

        super(AERegressor, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            encoding_dimension=encoding_dimension,
            hidden_dimension=hidden_dimension,
            optimizer=optimizer,
            learning_rate=learning_rate,
            loss=loss,
            activation=activation,            
            dropout_rate=dropout_rate,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )

    def fit(self, X, y, **kwargs):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]
        """
        # First step
        if LOGGER.debug:
            LOGGER.debug('BEGIN, AE: First step')
            LOGGER.debug("sk_params: %s", str(self.sk_params))

        super(AERegressor, self).fit(
            X,
            X,
            epochs=self.sk_params["epochs"],
            batch_size=self.sk_params["batch_size"],
            shuffle=True,
        )

        # Second step
        LOGGER.debug('AE: Second step')
        # freeze the encoder and only train the decoder with respect to the input data y_train
        self.model.layers[0].trainable = False
        
        verbose = 0
        if 'verbose' in kwargs:
            verbose = kwargs['verbose']

        # fit the model with y_train
        self.model.fit(
            y,
            y,
            epochs=self.sk_params["epochs"],
            batch_size=self.sk_params["batch_size"],
            shuffle=True,
            verbose=verbose,
        )

    def predict(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.model.predict(X)

    def score(self, X, y):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]

        Returns:
            [type]: [description]
        """
        y_pred = self.model.predict(X)
        std = (y - y_pred).std(axis=0)
        return std.mean()


class FFNRegressor(DeepLearningRegressor):
    """[summary]

    Args:
        DeepLearningRegressor ([type]): [description]
    """

    def __init__(
        self,
        output_dimension,
        layer_dims=(32, 16),
        build_fn=simple_ffn,
        optimizer="adam",
        loss="mean_squared_error",
        activation="relu",
        output_activation="linear",
        dropout_rate=0,
        epochs=10,
        batch_size=128,
        learning_rate=0.001,
        **kwargs,
    ):
        """[summary]

        Args:
            output_dimension ([type]): [description]
            layer_dims (tuple, optional): [description]. Defaults to (32, 16).
            build_fn ([type], optional): [description]. Defaults to simple_ffn.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            activation (str, optional): [description]. Defaults to "relu".
            output_activation (str, optional): [description]. Defaults to "linear".
            dropout_rate (int, optional): [description]. Defaults to 0.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
            learning_rate (float, optional): [description]. Defaults to 0.001.
        """

        super(FFNRegressor, self).__init__(
            build_fn=build_fn,
            output_dimension=output_dimension,
            layer_dims=layer_dims,
            optimizer=optimizer,
            loss=loss,
            activation=activation,
            dropout_rate=dropout_rate,
            epochs=epochs,
            batch_size=batch_size,
            learning_rate=learning_rate,
            output_activation=output_activation,
            **kwargs,
        )

    def fit(self, X, y, **kwargs):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]
        """

        # First step
        super(FFNRegressor, self).fit(
            X,
            y,
            epochs=self.sk_params["epochs"],
            batch_size=self.sk_params["batch_size"],
            shuffle=True,
        )

    def predict(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.model.predict(X)

    def score(self, X, y):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]

        Returns:
            [type]: [description]
        """

        y_pred = self.model.predict(X)
        std = (y - y_pred).std(axis=0)
        return std.mean()
