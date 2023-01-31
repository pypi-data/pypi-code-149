# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: deep_autoencoder_classifier
   :synopsis: Deep AE Classifier - Wrapper for \
       Classifier using Autoencoder Deep Networks.

.. moduleauthor:: SROM Team
"""

from autoai_ts_libs.deps.srom.deep_learning.models.cnn import deep_cnn, seriesNet, simple_cnn, waveNet
from autoai_ts_libs.deps.srom.deep_learning.models.dnn import deep_dnn, simple_dnn
from autoai_ts_libs.deps.srom.deep_learning.models.lstm import deep_lstm, simple_lstm
from autoai_ts_libs.deps.srom.utils.estimator_utils import BuildFnWrapper
from scikeras.wrappers import KerasClassifier

###########################################################
# Standard deep learning Classifier
###########################################################


class DNNClassifier(KerasClassifier):
    """
    Deep Learning Classifier which uses the Simple  DNN which is has one hidden layer.
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="binary_crossentropy",
        hidden_dimension=10,
        activation="relu",
        output_activation="sigmoid",
        kernel_initializer="normal",
        dropout_rate=0.1,
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

        super(DNNClassifier, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            hidden_dimension=hidden_dimension,
            activation=activation,
            output_activation=output_activation,
            kernel_initializer=kernel_initializer,
            dropout_rate=dropout_rate,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )


class DeepDNNClassifier(KerasClassifier):
    """
    Deep Learning Classifier which uses the Deep DNN which is can have multiple hidden layers.
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="binary_crossentropy",
        hidden_dimension=None,
        activation="relu",
        output_activation="sigmoid",
        kernel_initializer="normal",
        dropout_rate=0.2,
        dropout_first=False,
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
            build_fn = BuildFnWrapper(deep_dnn)

        if hidden_dimension is None:
            hidden_dimension = (10, 10, 10)

        super(DeepDNNClassifier, self).__init__(
            build_fn=build_fn,
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
# LSTM Classifiers
###########################################################


class SimpleLSTMClassifier(KerasClassifier):
    """
    Deep Learning Classifier which uses the Simple  DNN which is has one hidden layer.
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="rmsprop",
        loss="binary_crossentropy",
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
            build_fn = BuildFnWrapper(simple_lstm)

        super(SimpleLSTMClassifier, self).__init__(
            build_fn=build_fn,
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


class DeepLSTMClassifier(KerasClassifier):
    """
    Deep Learning Classifier which uses the Simple DNN which is has one hidden layer.
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="rmsprop",
        loss="binary_crossentropy",
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
            build_fn = BuildFnWrapper(deep_lstm)

        if hidden_dimension is None:
            hidden_dimension = (10, 10, 10)

        super(DeepLSTMClassifier, self).__init__(
            build_fn=build_fn,
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
# CNN Classifiers
###########################################################


class SimpleCNNClassifier(KerasClassifier):
    """
    Deep Learning Classifier which uses the Simple  DNN which is has one hidden layer.
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        loss="binary_crossentropy",
        optimizer="adam",
        hidden_dimension=10,
        activation="sigmoid",
        filters=32,
        kernel_size=2,
        max_pool_size=2,
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
            build_fn = BuildFnWrapper(simple_cnn)

        super(SimpleCNNClassifier, self).__init__(
            build_fn=build_fn,
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


class DeepCNNClassifier(KerasClassifier):
    """
    Deep Learning Classifier which uses the Simple  DNN which is has one hidden layer.
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        hidden_dimension=10,
        activation="sigmoid",
        loss="binary_crossentropy",
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
            build_fn = BuildFnWrapper(deep_cnn)

        super(DeepCNNClassifier, self).__init__(
            build_fn=build_fn,
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


class WaveNetClassifier(KerasClassifier):
    """
    Deep Learning Classifier which uses the Simple  DNN which is has one hidden layer.
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="binary_crossentropy",
        filters=32,
        kernel_size=2,
        dilation_layers=8,
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
            build_fn = BuildFnWrapper(waveNet)

        super(WaveNetClassifier, self).__init__(
            build_fn=build_fn,
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


class SeriesNetClassifier(KerasClassifier):
    """
    Deep Learning Classifier which uses the Simple  DNN which is has one hidden layer.
    """

    def __init__(
        self,
        input_dimension,
        output_dimension,
        build_fn=None,
        optimizer="adam",
        loss="binary_crossentropy",
        epochs=10,
        batch_size=128,
        **kwargs,
    ):
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(seriesNet)

        super(SeriesNetClassifier, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            optimizer=optimizer,
            loss=loss,
            epochs=epochs,
            batch_size=batch_size,
            **kwargs,
        )
