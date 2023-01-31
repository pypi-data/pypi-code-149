# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""CNN.

.. moduleauthor:: SROM Team

"""

from tensorflow.keras.initializers import TruncatedNormal
from tensorflow.keras.layers import (
    Activation,
    Add,
    BatchNormalization,
    Conv1D,
    Dense,
    Dropout,
    Flatten,
    GlobalAveragePooling1D,
    Input,
    MaxPooling1D,
    add,
)
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.regularizers import l2


def simple_cnn(
    input_dimension,
    output_dimension,
    hidden_dimension=10,
    filters=32,
    kernel_size=2,
    max_pool_size=2,
    activation="relu",
    loss="mean_squared_error",
    optimizer="adam",
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        hidden_dimension (int, optional): [description]. Defaults to 10.
        filters (int, optional): [description]. Defaults to 32.
        kernel_size (int, optional): [description]. Defaults to 2.
        max_pool_size (int, optional): [description]. Defaults to 2.
        activation (str, optional): [description]. Defaults to "relu".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        optimizer (str, optional): [description]. Defaults to "adam".

    Returns:
        [type]: [description]
    """
    model = Sequential()
    model.add(
        Conv1D(
            filters=filters,
            kernel_size=kernel_size,
            activation=activation,
            input_shape=input_dimension,
        )
    )
    model.add(MaxPooling1D(pool_size=max_pool_size))
    model.add(Flatten())
    model.add(Dense(hidden_dimension, activation=activation))
    model.add(Dense(output_dimension))
    model.compile(loss=loss, optimizer=optimizer)
    return model


def deep_cnn(
    input_dimension,
    output_dimension,
    hidden_dimension=10,
    filters=32,
    kernel_size=2,
    max_pool_size=2,
    activation="relu",
    loss="mean_squared_error",
    optimizer="adam",
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        hidden_dimension (int, optional): [description]. Defaults to 10.
        filters (int, optional): [description]. Defaults to 32.
        kernel_size (int, optional): [description]. Defaults to 2.
        max_pool_size (int, optional): [description]. Defaults to 2.
        activation (str, optional): [description]. Defaults to "relu".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        optimizer (str, optional): [description]. Defaults to "adam".

    Returns:
        [type]: [description]
    """
    model = Sequential()
    model.add(
        Conv1D(
            filters=filters,
            kernel_size=kernel_size,
            activation=activation,
            input_shape=input_dimension,
            padding="same",
        )
    )
    model.add(
        Conv1D(
            filters=filters,
            kernel_size=kernel_size,
            activation=activation,
            padding="same",
        )
    )
    model.add(MaxPooling1D(pool_size=max_pool_size))
    model.add(
        Conv1D(
            filters=(int)(filters / 2.0),
            kernel_size=kernel_size,
            activation=activation,
            padding="same",
        )
    )
    model.add(MaxPooling1D(pool_size=max_pool_size))
    model.add(Flatten())
    model.add(Dense(hidden_dimension, activation=activation))
    model.add(Dense(output_dimension))
    model.compile(loss=loss, optimizer=optimizer)
    return model


def waveNet(
    input_dimension,
    output_dimension,
    optimizer="adam",
    loss="mean_squared_error",
    filters=32,
    kernel_size=2,
    dilation_layers=8,
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        optimizer (str, optional): [description]. Defaults to "adam".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        filters (int, optional): [description]. Defaults to 32.
        kernel_size (int, optional): [description]. Defaults to 2.
        dilation_layers (int, optional): [description]. Defaults to 8.

    Returns:
        [type]: [description]
    """
    history_seq = Input(shape=input_dimension)
    x = history_seq
    dilation_rates = [2 ** i for i in range(dilation_layers)]

    for dilation_rate in dilation_rates:
        x = Conv1D(
            filters=filters,
            kernel_size=kernel_size,
            padding="causal",
            dilation_rate=dilation_rate,
        )(x)

    x = Dense(128, activation="relu")(x)
    x = Dropout(0.2)(x)
    x = Flatten()(x)
    x = Dense(output_dimension)(x)
    model = Model(inputs=history_seq, outputs=x)
    model.compile(loss=loss, optimizer=optimizer)
    return model


def seriesNet(
    input_dimension, output_dimension, optimizer="adam", loss="mean_squared_error"
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        optimizer (str, optional): [description]. Defaults to "adam".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
    """

    def DC_CNN_Block(filters, kernel_size, dilation, l2_layer_reg):
        """
            filters (int, optional): [description].
            kernel_size (int, optional): [description].
            dilation (int, optional): [description].
            l2_layer_reg (int, optional) [description].
        """
        def f(input_):

            residual = input_
            layer_out = Conv1D(
                filters=filters,
                kernel_size=kernel_size,
                dilation_rate=dilation,
                activation="linear",
                padding="causal",
                use_bias=False,
                kernel_initializer=TruncatedNormal(mean=0.0, stddev=0.05, seed=42),
                kernel_regularizer=l2(l2_layer_reg),
            )(input_)

            layer_out = Activation("selu")(layer_out)

            skip_out = Conv1D(
                1,
                1,
                activation="linear",
                use_bias=False,
                kernel_initializer=TruncatedNormal(mean=0.0, stddev=0.05, seed=42),
                kernel_regularizer=l2(l2_layer_reg),
            )(layer_out)

            network_in = Conv1D(
                1,
                1,
                activation="linear",
                use_bias=False,
                kernel_initializer=TruncatedNormal(mean=0.0, stddev=0.05, seed=42),
                kernel_regularizer=l2(l2_layer_reg),
            )(layer_out)

            network_out = Add()([residual, network_in])

            return network_out, skip_out

        return f

    input = Input(shape=input_dimension)

    l1a, l1b = DC_CNN_Block(32, 2, 1, 0.001)(input)
    l2a, l2b = DC_CNN_Block(32, 2, 2, 0.001)(l1a)
    l3a, l3b = DC_CNN_Block(32, 2, 4, 0.001)(l2a)
    l4a, l4b = DC_CNN_Block(32, 2, 8, 0.001)(l3a)
    l5a, l5b = DC_CNN_Block(32, 2, 16, 0.001)(l4a)
    l6a, l6b = DC_CNN_Block(32, 2, 32, 0.001)(l5a)
    l6b = Dropout(0.8)(l6b)  # dropout used to limit influence of earlier data
    l7a, l7b = DC_CNN_Block(32, 2, 64, 0.001)(l6a)
    l7b = Dropout(0.8)(l7b)  # dropout used to limit influence of earlier data

    l8 = Add()([l1b, l2b, l3b, l4b, l5b, l6b, l7b])

    l9 = Activation("relu")(l8)

    l21 = Conv1D(
        1,
        1,
        activation="linear",
        use_bias=False,
        kernel_initializer=TruncatedNormal(mean=0.0, stddev=0.05, seed=42),
        kernel_regularizer=l2(0.001),
    )(l9)

    x = Dense(128, activation="relu")(l21)
    x = Dropout(0.2)(x)
    x = Flatten()(x)
    x = Dense(output_dimension)(x)

    model = Model(inputs=input, outputs=x)

    # adam = optimizers.Adam(lr=0.00075, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0,
    # amsgrad=False)
    model.compile(loss=loss, optimizer=optimizer)
    return model


def simple_fcn(
    input_dimension,
    output_dimension,
    optimizer="adam",
    loss="mean_squared_error",
    filters=32,
    kernel_size=2,
    dilation_layers=8,
):
    """
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        optimizer (str, optional): [description]. Defaults to "adam".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        filter (Integer): [description]. Defaults to 32.
        kernel_size (Integer): [description]. Defaults to 2.
        dilation_layer (Integer): [description]. Defaults to 8.
    """
    input_layer = Input(input_dimension)

    conv1 = Conv1D(filters=128, kernel_size=8, padding="same")(input_layer)
    conv1 = BatchNormalization()(conv1)
    conv1 = Activation(activation="relu")(conv1)

    conv2 = Conv1D(filters=256, kernel_size=5, padding="same")(conv1)
    conv2 = BatchNormalization()(conv2)
    conv2 = Activation("relu")(conv2)

    conv3 = Conv1D(128, kernel_size=3, padding="same")(conv2)
    conv3 = BatchNormalization()(conv3)
    conv3 = Activation("relu")(conv3)

    gap_layer = GlobalAveragePooling1D()(conv3)

    output_layer = Dense(1, activation="linear")(gap_layer)

    model = Model(inputs=input_layer, outputs=output_layer)

    model.compile(loss=loss, optimizer=optimizer)

    return model


def resnet_model(
    input_dimension,
    output_dimension,
    optimizer="adam",
    loss="mean_squared_error",
    filters=32,
    kernel_size=2,
    dilation_layers=8,
):
    """
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        optimizer (str, optional): [description]. Defaults to "adam".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        filter (Integer): [description]. Defaults to 32.
        kernel_size (Integer): [description]. Defaults to 2.
        dilation_layer (Integer): [description]. Defaults to 8.
    """
    n_feature_maps = 64
    input_layer = Input(input_dimension)

    # BLOCK 1
    conv_x = Conv1D(filters=n_feature_maps, kernel_size=8, padding="same")(input_layer)
    conv_x = BatchNormalization()(conv_x)
    conv_x = Activation("relu")(conv_x)

    conv_y = Conv1D(filters=n_feature_maps, kernel_size=5, padding="same")(conv_x)
    conv_y = BatchNormalization()(conv_y)
    conv_y = Activation("relu")(conv_y)

    conv_z = Conv1D(filters=n_feature_maps, kernel_size=3, padding="same")(conv_y)
    conv_z = BatchNormalization()(conv_z)

    # expand channels for the sum
    shortcut_y = Conv1D(filters=n_feature_maps, kernel_size=1, padding="same")(
        input_layer
    )
    shortcut_y = BatchNormalization()(shortcut_y)

    output_block_1 = add([shortcut_y, conv_z])
    output_block_1 = Activation("relu")(output_block_1)

    # BLOCK 2
    conv_x = Conv1D(filters=n_feature_maps * 2, kernel_size=8, padding="same")(
        output_block_1
    )
    conv_x = BatchNormalization()(conv_x)
    conv_x = Activation("relu")(conv_x)

    conv_y = Conv1D(filters=n_feature_maps * 2, kernel_size=5, padding="same")(conv_x)
    conv_y = BatchNormalization()(conv_y)
    conv_y = Activation("relu")(conv_y)

    conv_z = Conv1D(filters=n_feature_maps * 2, kernel_size=3, padding="same")(conv_y)
    conv_z = BatchNormalization()(conv_z)

    # expand channels for the sum
    shortcut_y = Conv1D(filters=n_feature_maps * 2, kernel_size=1, padding="same")(
        output_block_1
    )
    shortcut_y = BatchNormalization()(shortcut_y)

    output_block_2 = add([shortcut_y, conv_z])
    output_block_2 = Activation("relu")(output_block_2)

    # BLOCK 3
    conv_x = Conv1D(filters=n_feature_maps * 2, kernel_size=8, padding="same")(
        output_block_2
    )
    conv_x = BatchNormalization()(conv_x)
    conv_x = Activation("relu")(conv_x)

    conv_y = Conv1D(filters=n_feature_maps * 2, kernel_size=5, padding="same")(conv_x)
    conv_y = BatchNormalization()(conv_y)
    conv_y = Activation("relu")(conv_y)

    conv_z = Conv1D(filters=n_feature_maps * 2, kernel_size=3, padding="same")(conv_y)
    conv_z = BatchNormalization()(conv_z)

    # no need to expand channels because they are equal
    shortcut_y = BatchNormalization()(output_block_2)

    output_block_3 = add([shortcut_y, conv_z])
    output_block_3 = Activation("relu")(output_block_3)

    # FINAL
    gap_layer = GlobalAveragePooling1D()(output_block_3)

    output_layer = Dense(1, activation="linear")(gap_layer)

    model = Model(inputs=input_layer, outputs=output_layer)

    model.compile(loss=loss, optimizer=optimizer)

    return model
