# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""Inception.

.. moduleauthor:: SROM Team

"""

from tensorflow.keras.layers import (
    Activation,
    BatchNormalization,
    Conv1D,
    GlobalAveragePooling1D,
    Input,
    Dense,
    MaxPool1D,
    Concatenate,
    Add,
)
from tensorflow.keras.models import Model


def _inception_module(
    input_tensor,
    stride=1,
    activation="linear",
    use_bottleneck=True,
    bottleneck_size=32,
    kernel_size=41,
    nb_filters=32,
):
    if use_bottleneck and int(input_tensor.shape[-1]) > 1:
        input_inception = Conv1D(
            filters=bottleneck_size,
            kernel_size=1,
            padding="same",
            activation=activation,
            use_bias=False,
        )(input_tensor)
    else:
        input_inception = input_tensor

    # kernel_size_s = [3, 5, 8, 11, 17]
    kernel_size_s = [kernel_size // (2 ** i) for i in range(3)]

    conv_list = []

    for i in range(len(kernel_size_s)):
        conv_list.append(
            Conv1D(
                filters=nb_filters,
                kernel_size=kernel_size_s[i],
                strides=stride,
                padding="same",
                activation=activation,
                use_bias=False,
            )(input_inception)
        )

    max_pool_1 = MaxPool1D(pool_size=3, strides=stride, padding="same")(input_tensor)

    conv_6 = Conv1D(
        filters=nb_filters,
        kernel_size=1,
        padding="same",
        activation=activation,
        use_bias=False,
    )(max_pool_1)

    conv_list.append(conv_6)

    x = Concatenate(axis=2)(conv_list)
    x = BatchNormalization()(x)
    x = Activation(activation="relu")(x)
    return x


def _shortcut_layer(input_tensor, out_tensor):
    shortcut_y = Conv1D(
        filters=int(out_tensor.shape[-1]), kernel_size=1, padding="same", use_bias=False
    )(input_tensor)
    shortcut_y = BatchNormalization()(shortcut_y)

    x = Add()([shortcut_y, out_tensor])
    x = Activation("relu")(x)
    return x


def inception_time_model(
    input_dimension,
    output_dimension,
    optimizer="adam",
    loss="mean_squared_error",
    filters=32,
    kernel_size=2,
    dilation_layers=8,
    use_residual=True,
):
    input_layer = Input(input_dimension)

    x = input_layer
    input_res = input_layer

    for d in range(6):

        x = _inception_module(x)

        if use_residual and d % 3 == 2:
            x = _shortcut_layer(input_res, x)
            input_res = x

    gap_layer = GlobalAveragePooling1D()(x)

    output_layer = Dense(1, activation="linear")(gap_layer)

    model = Model(inputs=input_layer, outputs=output_layer)

    model.compile(loss=loss, optimizer=optimizer)

    return model
