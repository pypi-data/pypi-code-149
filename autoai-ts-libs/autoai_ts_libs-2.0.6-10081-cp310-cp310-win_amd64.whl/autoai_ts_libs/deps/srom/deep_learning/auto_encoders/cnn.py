# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: cnn
   :synopsis: cnn.

.. moduleauthor:: SROM Team
"""

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers import Conv1D, Input, MaxPooling1D, UpSampling1D
from tensorflow.keras.models import Model

from autoai_ts_libs.deps.srom.deep_learning.utils import get_optimizer

def cnn_ae(
    input_dimension,
    optimizer='adam',
    enc_num_filters=(16, 16, 1),
    dec_num_filters=(1, 16, 16),
    learning_rate=0.001,
    loss="mean_squared_error",
    activation="relu",
    output_activation="linear",
    kernel_initializer="normal",
    dropout_rate=0.1,
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        optimizer (string or optimizer object, optional): [description]. Defaults to 'adam'.
        enc_num_filters (tuple, optional): [description]. Defaults to (16, 16, 1).
        dec_num_filters (tuple, optional): [description]. Defaults to (1, 16, 16).
        learning_rate (float, optional): [description]. Defaults to 0.001.
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        activation (str, optional): [description]. Defaults to "relu".
        output_activation (str, optional): [description]. Defaults to "linear".
        kernel_initializer (str, optional): [description]. Defaults to "normal".
        dropout_rate (float, optional): [description]. Defaults to 0.1.

    Returns:
        [type]: [description]
    """

    # ENCODER
    encoder = tf.keras.Sequential()
    # layer 1
    encoder.add(
        layers.Conv1D(
            filters=enc_num_filters[0],
            kernel_size=3,
            activation=activation,
            input_shape=input_dimension[1:],
            padding="same",
        )
    )
    encoder.add(layers.Dropout(dropout_rate))
    encoder.add(layers.MaxPooling1D(pool_size=2, padding='same'))  # 2970 / 2 / 3/ 3
    # layer 2
    encoder.add(
        layers.Conv1D(
            filters=enc_num_filters[1],
            kernel_size=3,
            activation=activation,
            padding="same",
        )
    )
    encoder.add(layers.Dropout(dropout_rate))
    encoder.add(layers.MaxPooling1D(pool_size=3, padding='same'))
    # layer 3
    encoder.add(
        layers.Conv1D(
            filters=enc_num_filters[2],
            kernel_size=3,
            activation=activation,
            padding="same",
        )
    )
    encoder.add(layers.Dropout(dropout_rate))
    encoder.add(layers.MaxPooling1D(pool_size=3, padding='same'))

    # DECODER
    decoder = tf.keras.Sequential()
    # layer 3
    decoder.add(
        layers.Conv1D(
            filters=dec_num_filters[0],
            kernel_size=3,
            activation=activation,
            padding="same",
        )
    )
    decoder.add(layers.UpSampling1D(size=3))
    decoder.add(layers.Dropout(dropout_rate))
    # layer 2
    decoder.add(
        layers.Conv1D(
            filters=dec_num_filters[1],
            kernel_size=3,
            activation=activation,
            padding="same",
        )
    )
    decoder.add(layers.UpSampling1D(size=3))
    decoder.add(layers.Dropout(dropout_rate))
    # layer 1
    decoder.add(
        layers.Conv1D(
            filters=dec_num_filters[2],
            kernel_size=3,
            activation=activation,
            padding="same",
        )
    )
    decoder.add(layers.UpSampling1D(size=2))
    decoder.add(layers.Dropout(dropout_rate))

    decoder.add(
        layers.Conv1D(
            filters=1, kernel_size=3, activation=output_activation, padding="same"
        )
    )

    # Concatenate encoder and decoder
    model = tf.keras.Sequential([encoder, decoder])

    opt = get_optimizer(optimizer, learning_rate=learning_rate)
    model.compile(optimizer=opt, loss=loss)

    return model


def simple_cnn(input_dimension, optimizer='adam', loss="binary_crossentropy"):
    """[summary]

    Args:
        input_dimension ([type]): [description]

    Returns:
        [type]: [description]
    """

    input_window = Input(shape=input_dimension)
    x = Conv1D(16, 3, activation="relu", padding="same")(input_window)
    x = MaxPooling1D(2, strides=1, padding="same")(x)
    x = Conv1D(1, 3, activation="relu", padding="same")(x)
    encoded = MaxPooling1D(2, strides=1, padding="same")(x)

    #encoder = Model(input_window, encoded)

    # 3 dimensions in the encoded layer
    x = Conv1D(1, 3, activation="relu", padding="same")(encoded)
    #x = UpSampling1D(2)(x)
    x = Conv1D(16, 2, activation="relu", padding="same")(x)
    #x = UpSampling1D(2)(x)
    decoded = Conv1D(input_dimension[1], 3, activation="sigmoid", padding="same")(x)
    autoencoder = Model(input_window, decoded)
    autoencoder.compile(optimizer=optimizer, loss=loss)
    if autoencoder.layers[0].output_shape[0] != autoencoder.layers[-1].output_shape:
        raise Exception("X shape not compatible with input_dimension")
    return autoencoder
