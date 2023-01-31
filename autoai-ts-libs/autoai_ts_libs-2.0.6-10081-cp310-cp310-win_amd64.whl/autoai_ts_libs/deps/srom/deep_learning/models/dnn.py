# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""DNN.

.. moduleauthor:: SROM Team

"""

from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential


def simple_dnn(
    input_dimension,
    output_dimension,
    hidden_dimension=10,
    optimizer="adam",
    loss="mean_squared_error",
    activation="relu",
    output_activation="linear",
    kernel_initializer="normal",
    dropout_rate=0.1,
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        hidden_dimension (int, optional): [description]. Defaults to 10.
        optimizer (str, optional): [description]. Defaults to "adam".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        activation (str, optional): [description]. Defaults to "relu".
        output_activation (str, optional): [description]. Defaults to "linear".
        kernel_initializer (str, optional): [description]. Defaults to "normal".
        dropout_rate (float, optional): [description]. Defaults to 0.1.

    Returns:
        [type]: [description]
    """
    model = Sequential()
    model.add(
        Dense(
            hidden_dimension,
            input_shape=input_dimension,
            kernel_initializer=kernel_initializer,
            activation=activation,
        )
    )
    model.add(Dropout(rate=dropout_rate))
    model.add(
        Dense(
            output_dimension,
            kernel_initializer=kernel_initializer,
            activation=output_activation,
        )
    )
    model.compile(loss=loss, optimizer=optimizer)
    return model


def deep_dnn(
    input_dimension,
    output_dimension,
    hidden_dimension=(10, 10, 10),
    optimizer="adam",
    loss="mean_squared_error",
    activation="relu",
    output_activation="linear",
    kernel_initializer="normal",
    dropout_rate=0.1,
    dropout_first=False,
    kernel_constraint=None,
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        hidden_dimension (tuple, optional): [description]. Defaults to (10, 10, 10).
        optimizer (str, optional): [description]. Defaults to "adam".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        activation (str, optional): [description]. Defaults to "relu".
        output_activation (str, optional): [description]. Defaults to "linear".
        kernel_initializer (str, optional): [description]. Defaults to "normal".
        dropout_rate (float, optional): [description]. Defaults to 0.1.
        dropout_first (bool, optional): [description]. Defaults to False.
        kernel_constraint ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    model = Sequential()

    if dropout_first:
        model.add(Dropout(rate=dropout_rate, input_shape=input_dimension))

    for i, h in enumerate(hidden_dimension):
        if i == 0 and not dropout_first:
            model.add(
                Dense(
                    h,
                    kernel_initializer=kernel_initializer,
                    input_shape=input_dimension,
                    activation=activation,
                    kernel_constraint=kernel_constraint,
                )
            )
        else:
            model.add(
                Dense(
                    h,
                    kernel_initializer=kernel_initializer,
                    activation=activation,
                    kernel_constraint=kernel_constraint,
                )
            )
        model.add(Dropout(rate=dropout_rate))

    model.add(
        Dense(
            output_dimension,
            kernel_initializer=kernel_initializer,
            activation=output_activation,
        )
    )
    model.compile(loss=loss, optimizer=optimizer)
    return model
