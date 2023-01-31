# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: lstm
   :synopsis: lstm.

.. moduleauthor:: SROM Team
"""

from tensorflow.keras.layers import (
    LSTM,
    Concatenate,
    Dense,
    Dropout,
    Input,
    RepeatVector,
    TimeDistributed,
)
from tensorflow.keras.models import Model


def simple_lstm_autoencoder(
    input_dimension, hidden_dimension, loss="mae", optimizer="adam"
):
    """[summary]

    Args:
        input_dimension ([time, feature]): [description]

    Returns:
        [type]: [description]
    """
    if not isinstance(hidden_dimension, list):
        hidden_dimension = int(hidden_dimension)
        hidden_dimension = [hidden_dimension] * 3

    inputs = Input(shape=input_dimension)
    L1 = LSTM(16, activation="relu", return_sequences=True)(inputs)
    L2 = LSTM(4, activation="relu", return_sequences=False)(L1)
    L3 = RepeatVector(input_dimension[0])(L2)
    L4 = LSTM(4, activation="relu", return_sequences=True)(L3)
    L5 = LSTM(16, activation="relu", return_sequences=True)(L4)
    output = TimeDistributed(Dense(input_dimension[1]))(L5)
    train_model = Model(inputs=inputs, outputs=output)
    train_model.compile(loss=loss, optimizer=optimizer)
    return train_model


def lstm_autoencoder(
    input_dim,
    encoding_dim,
    window_length,
    output_dim=None,
    hidden_dim=20,
    depth=2,
    activation="relu",
    dropout=0.0,
    recurrent_dropout=0.0,
    output_dropout=0.0,
    loss="mean_squared_error",
    optimizer="rmsprop",
    mode=0,
):
    """Builds an autoencoder
    :params: `input_dim` (number of features)
             `encoding_dim` (the number of time steps to be represented by the encoding)
             `window_length` (the number of time steps used in the prediction step)
             `output_dim` (number of output features)
             `depth` (number of hidden layers in the encoder and decoder layers)
             `hidden_dim` (number of nodes in the hidden layer, can be an int,
             meaning all layers are of the same size,
             or a list of length `depth`, specifying the size of each hidden layer)
             `activation` (type of activation to use at each layer, defaults to relu)
             `dropout` (dropout parameter for inputs to each of the hidden layers in
              the encoder and decoder)
    :outputs: `train_model` (encoder-decoder model to be used for training)
              `feature_extractor` (encoder only model which can be used to extract
              embeddings post training)
    """

    if output_dim is None:
        output_dim = input_dim

    if isinstance(hidden_dim, list):
        if len(hidden_dim) != depth:
            raise Exception(
                "Desired depth is %d but %d hidden layer sizes have been provided"
                % (depth, len(hidden_dim))
            )
    else:
        hidden_dim = int(hidden_dim)
        hidden_dim = [hidden_dim] * depth

    # adding encoding_dim
    hidden_dim = hidden_dim + [encoding_dim]

    input_layer = Input(shape=(None, input_dim))

    encoder_layers = []
    for i, layer_dim in enumerate(hidden_dim):
        if i + 1 != len(hidden_dim):
            encoder_layers.append(
                LSTM(
                    layer_dim,
                    return_sequences=True,
                    dropout=dropout,
                    recurrent_dropout=recurrent_dropout,
                    name="encoder_lstm_" + str(i + 1),
                )
            )
        else:
            encoder_layers.append(
                LSTM(
                    layer_dim,
                    return_sequences=False,
                    dropout=dropout,
                    recurrent_dropout=recurrent_dropout,
                    name="encoder_lstm_" + str(i + 1),
                )
            )
    encoder_layer_outputs = []

    for i, layer_dim in enumerate(hidden_dim):
        if i == 0:
            outs = encoder_layers[i](input_layer)
        else:
            outs = encoder_layers[i](encoder_layer_outputs[i - 1])
        encoder_layer_outputs.append(outs)

    decoder_inputs = RepeatVector(window_length)(encoder_layer_outputs[-1])

    decoder_layers = []
    decoder_dim = hidden_dim[:-1][::-1] + [output_dim]
    for i, layer_dim in enumerate(decoder_dim):
        decoder_layers.append(
            LSTM(
                layer_dim,
                return_sequences=True,
                dropout=dropout,
                recurrent_dropout=recurrent_dropout,
                name="decoder_ae_" + str(i + 1),
            )
        )
    # decoder_layers.append(TimeDistributed(Dense(window_length)))

    decoder_layer_outputs = []
    for i, _ in enumerate(decoder_layers):
        if i == 0:
            outs = decoder_layers[i](decoder_inputs)
        else:
            outs = decoder_layers[i](decoder_layer_outputs[i - 1])
        decoder_layer_outputs.append(outs)

    decoder_dropout = Dropout(output_dropout, noise_shape=(None, output_dim))
    decoder_dense = Dense(output_dim, activation="linear")
    decoder_outputs = decoder_dense(decoder_dropout(decoder_layer_outputs[-1]))

    train_model = Model(inputs=input_layer, outputs=decoder_outputs)
    train_model.compile(loss=loss, optimizer=optimizer)
    feature_extractor = Model(inputs=input_layer, outputs=encoder_layer_outputs[-1])
    if mode == 0:
        return train_model
    return train_model, feature_extractor


def lstm_teacher_forcing_autoencoder(
    data_dim,
    output_dim,
    hidden_dim=20,
    depth=3,
    output_dropout=0.0,
    lstm_dropout=0.0,
    lstm_recurrent_dropout=0.0,
):
    """
    Builds an LSTM autoencoder with a teacher forcing mechanism at the decoder layer.
    Args:
        data_dim: number of features in the time series
        output_dim: number of output features
        depth: number of hidden layers in the encoder and decoder layers
        hidden_dim: number of hidden nodes in the LSTM layer, can be an int, meaning all layers are
                    of the same size, or a list of length `depth`, specifying the size of each hidden layer)
        output_dropout: dropout parameter for the final dense layer that reconstructs the input
        lstm_dropout: dropout parameter for inputs to the LSTM layers
        lstm_recurrent_dropout: recurrent dropout parameter for the LSTM layers

    Returns:
        keras.models.Model : encoder-decoder model to be used for training
        keras.models.Model: encoder only model which can be used to extract embeddings post training
    """
    if isinstance(hidden_dim, list) and len(hidden_dim) != depth:
        raise Exception(
            "Desired depth is %d but %d hidden layer sizes have been provided"
            % (depth, len(hidden_dim))
        )
    if isinstance(hidden_dim, int):
        hidden_dim = [hidden_dim] * depth

    encoder_inputs = Input(shape=(None, data_dim))
    encoder_layers = []
    for i in range(depth):
        encoder_layers.append(
            LSTM(
                hidden_dim[i],
                return_sequences=True,
                return_state=True,
                dropout=lstm_dropout,
                recurrent_dropout=lstm_recurrent_dropout,
                name="encoder_lstm_" + str(i + 1),
            )
        )
    encoder_layer_outputs = []
    encoder_layer_state_h, encoder_layer_state_c = [], []
    for i in range(depth):
        if i == 0:
            outs, state_h, state_c = encoder_layers[i](encoder_inputs)
        else:
            outs, state_h, state_c = encoder_layers[i](encoder_layer_outputs[i - 1])
        encoder_layer_outputs.append(outs)
        encoder_layer_state_h.append(state_h)
        encoder_layer_state_c.append(state_c)
    encoder_states = [encoder_layer_state_h[-1], encoder_layer_state_c[-1]]

    decoder_inputs = Input(shape=(None, data_dim))
    decoder_layers = []
    decoder_dim = hidden_dim[::-1]
    for i in range(depth):
        decoder_layers.append(
            LSTM(
                decoder_dim[i],
                return_sequences=True,
                return_state=True,
                dropout=lstm_dropout,
                recurrent_dropout=lstm_recurrent_dropout,
                name="decoder_lstm_" + str(i + 1),
            )
        )
    decoder_layer_outputs = []

    for i in range(depth):
        if i == 0:
            state = [encoder_layer_state_h[i], encoder_layer_state_c[i]]
            outs, _, _ = decoder_layers[i](decoder_inputs, initial_state=state)
        else:
            state = [encoder_layer_state_h[i], encoder_layer_state_c[i]]
            outs, _, _ = decoder_layers[i](
                decoder_layer_outputs[i - 1], initial_state=state
            )
        decoder_layer_outputs.append(outs)

    decoder_dropout = Dropout(output_dropout, noise_shape=(None, data_dim))
    decoder_dense = Dense(output_dim, activation="linear")
    decoder_outputs = decoder_dense(decoder_dropout(decoder_layer_outputs[-1]))

    train_model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
    feature_extractor = Model(encoder_inputs, encoder_states)
    return train_model, feature_extractor


def lstm_repeat_vector_autoencoder(
    data_dim,
    output_dim,
    window_length,
    hidden_dim=20,
    depth=3,
    output_dropout=0.0,
    lstm_dropout=0.0,
    lstm_recurrent_dropout=0.0,
):
    """
    Builds an LSTM autoencoder which repeats the embeddings and uses that as the input to the
    decoder layer
    Args:
        data_dim: number of features in the time series
        output_dim: number of output features
        window_length: number of timesteps in the window
        depth: number of hidden layers in the encoder and decoder layers
        hidden_dim: number of hidden nodes in the LSTM layer, can be an int, meaning all layers
                    are of the same size, or a list of length `depth`, (specifying the size of
                    each hidden layer)
        output_dropout: dropout parameter for the final dense layer that reconstructs the input
        lstm_dropout: dropout parameter for inputs to the LSTM layers
        lstm_recurrent_dropout: recurrent dropout parameter for the LSTM layers

     Returns:
            keras.models.Model: encoder-decoder model to be used for training.
            keras.models.Model: encoder only model which can be used to extract embeddings post training.
    """
    if isinstance(hidden_dim, list):
        if len(hidden_dim) != depth:
            raise Exception(
                "Desired depth is %d but %d hidden layer sizes have been provided"
                % (depth, len(hidden_dim))
            )
    if isinstance(hidden_dim, int):
        hidden_dim = [hidden_dim] * depth
    encoder_inputs = Input(shape=(window_length, data_dim))
    encoder_layers = []
    for i in range(depth):
        encoder_layers.append(
            LSTM(
                hidden_dim[i],
                return_sequences=True,
                return_state=True,
                dropout=lstm_dropout,
                recurrent_dropout=lstm_recurrent_dropout,
                name="encoder_lstm_" + str(i + 1),
            )
        )
    encoder_layer_outputs = []
    encoder_layer_state_h, encoder_layer_state_c = [], []
    for i in range(depth):
        if i == 0:
            outs, state_h, state_c = encoder_layers[i](encoder_inputs)
        else:
            outs, state_h, state_c = encoder_layers[i](encoder_layer_outputs[i - 1])
        encoder_layer_outputs.append(outs)
        encoder_layer_state_h.append(state_h)
        encoder_layer_state_c.append(state_c)
    encoder_states = Concatenate(axis=-1)(
        [encoder_layer_state_h[-1], encoder_layer_state_c[-1]]
    )

    decoder_inputs = RepeatVector(window_length)(encoder_states)

    decoder_layers = []
    decoder_dim = hidden_dim[::-1]
    for i in range(depth):
        decoder_layers.append(
            LSTM(
                decoder_dim[i],
                return_sequences=True,
                return_state=True,
                dropout=lstm_dropout,
                recurrent_dropout=lstm_recurrent_dropout,
                name="decoder_lstm_" + str(i + 1),
            )
        )

    decoder_layer_outputs = []
    for i in range(depth):
        if i == 0:
            outs, _, _ = decoder_layers[i](decoder_inputs)
        else:
            outs, _, _ = decoder_layers[i](decoder_layer_outputs[i - 1])
        decoder_layer_outputs.append(outs)

    decoder_dropout = Dropout(output_dropout, noise_shape=(None, data_dim))
    decoder_dense = Dense(output_dim, activation="linear")
    decoder_outputs = decoder_dense(decoder_dropout(decoder_layer_outputs[-1]))

    train_model = Model(encoder_inputs, decoder_outputs)
    feature_extractor = Model(encoder_inputs, encoder_states)
    return train_model, feature_extractor
