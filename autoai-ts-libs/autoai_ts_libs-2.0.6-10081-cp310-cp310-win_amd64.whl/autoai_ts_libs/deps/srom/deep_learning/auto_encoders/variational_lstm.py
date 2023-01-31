# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: varitional_lstm
   :synopsis: varitional_lstm.

.. moduleauthor:: SROM Team
"""


from tensorflow.keras.layers import (
    Input,
    Dense,
    Dropout,
    Lambda,
    LSTM,
    RepeatVector,
    # Concatenate,
)
from tensorflow.keras.models import Model
from tensorflow.keras import backend as K
from tensorflow.keras import losses


def lstm_variational_autoencoder(
    input_dim,
    output_dim,
    window_length,
    generator_dim,
    hidden_dim=20,
    depth=3,
    activation="relu",
    output_dropout=0.0,
    lstm_dropout=0.0,
    lstm_recurrent_dropout=0.0,
):
    """
    Builds an LSTM variational auto encoder
    Args:
        input_dim: number of features
        output_dim: number of output latent features
        window_length: number of timesteps in the window
        depth: number of hidden layers in the encoder and decoder layers
        generator_dim: size of latent space
        hidden_dim: number of nodes in the hidden layer, can be an int, meaning all layers are of
                    the same size or a list of length `depth`, specifying the size of each
                    hidden layer
        activation: type of activation to use at each layer, defaults to relu
        output_dropout: dropout parameter for the final dense layer that reconstructs the input
        lstm_dropout: dropout parameter for inputs to the LSTM layers
        lstm_recurrent_dropout: recurrent dropout parameter for the LSTM layers
    Returns:
        keras.models.Model : encoder-decoder model to be used for training
        keras.models.Model : encoder only model which can be used to extract embeddings post
                             training
    """

    if isinstance(hidden_dim, list):
        if len(hidden_dim) != depth:
            raise Exception(
                "Desired depth is %d but %d hidden layer sizes have been provided"
                % (depth, len(hidden_dim))
            )
    else:
        hidden_dim = int(hidden_dim)
        hidden_dim = [hidden_dim] * depth

    encoder_inputs = Input(shape=(window_length, input_dim))
    encoder_layers = []
    for i in range(depth - 1):
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
    encoder_layers.append(
        LSTM(
            hidden_dim[-1],
            return_sequences=False,
            return_state=True,
            dropout=lstm_dropout,
            recurrent_dropout=lstm_recurrent_dropout,
            name="encoder_lstm_" + str(depth),
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
    # encoder_states = Concatenate(axis=-1)(
    #     [encoder_layer_state_h[-1], encoder_layer_state_c[-1]]
    # )

    z_mean = Dense(generator_dim)(encoder_layer_outputs[-1])
    z_log_var = Dense(generator_dim)(encoder_layer_outputs[-1])

    def sampling(args):
        z_mean, z_log_var = args
        epsilon = K.random_normal(shape=K.shape(z_mean), mean=0.0)
        return z_mean + K.exp(z_log_var / 2) * epsilon

    # note that "output_shape" isn't necessary with the TensorFlow backend
    z = Lambda(sampling, output_shape=(generator_dim,))([z_mean, z_log_var])

    decoder_inputs = RepeatVector(window_length)(z)

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

    decoder_dropout = Dropout(output_dropout, noise_shape=(None, output_dim))
    decoder_dense = Dense(output_dim, activation="linear")
    decoder_outputs = decoder_dense(decoder_dropout(decoder_layer_outputs[-1]))

    train_model = Model(encoder_inputs, decoder_outputs)
    feature_extractor = Model(encoder_inputs, z_mean)

    def vae_loss(y_true, y_pred):
        """
        loss for the variational auto encoder
        Args:
            y_true: keras tensor containing ground truth data
            y_pred: model predictions
            original_dim: number of original dimension
            z_mean: mean of hidden variable
            z_log_var: variance of hidden variable
        """
        xent_loss = losses.MSE(y_true, y_pred)
        kl_loss = -0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var))
        return xent_loss + kl_loss

    return train_model, feature_extractor, vae_loss
