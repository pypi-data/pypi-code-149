# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: varitional_dnn
   :synopsis: varitional_dnn.

.. moduleauthor:: SROM Team
"""

from tensorflow.keras import backend as K
from tensorflow.keras.layers import Dense, Dropout, Input, Lambda
from tensorflow.keras.losses import binary_crossentropy
from tensorflow.keras.models import Model
import tensorflow as tf


def variational_autoencoder(
    input_dimension,
    generator_dimension,
    hidden_dim=20,
    depth=3,
    activation="relu",
    dropout=0.0,
    optimizer="adam",
    mode=0,
):
    """
    Builds an variational auto encoder
    Args:
        input_dim: number of features
        output_dim: number of output latent features
        generator_dim: size of latent space
        depth: number of hidden layers in the encoder and decoder layers
        hidden_dim: number of nodes in the hidden layer, can be an int, meaning all layers are of
                    the same size or a list of length `depth`, specifying the size of each
                    hidden layer
        activation: type of activation to use at each layer, defaults to relu
        dropout: dropout parameter for inputs to each of the hidden layers in the encoder and decoder
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

    input_layer = Input(shape=(input_dimension,))
    dropout_layer = None
    # if dropout > 0.0:
    dropout_layer = Dropout(dropout)
    encoder_layers = []
    for i in range(depth):
        encoder_layers.append(
            Dense(
                hidden_dim[i], activation=activation, name="encoder_vae_" + str(i + 1)
            )
        )
    encoder_layer_outputs = []
    for i in range(depth):
        if i == 0:
            outs = encoder_layers[i](input_layer)
        else:
            if dropout_layer:
                outs = encoder_layers[i](dropout_layer(encoder_layer_outputs[i - 1]))
            else:
                outs = encoder_layers[i](encoder_layer_outputs[i - 1])
        encoder_layer_outputs.append(outs)

    z_mean = Dense(generator_dimension)(encoder_layer_outputs[-1])
    z_log_var = Dense(generator_dimension)(encoder_layer_outputs[-1])

    def sampling(args):
        z_mean, z_log_var = args
        epsilon = K.random_normal(shape=K.shape(z_mean), mean=0.0)
        return z_mean + K.exp(z_log_var / 2) * epsilon

    # note that "output_shape" isn't necessary with the TensorFlow backend
    z = Lambda(sampling, output_shape=(generator_dimension,))([z_mean, z_log_var])

    decoder_layers = []
    decoder_dim = hidden_dim[:-1][::-1] + [input_dimension]
    for i in range(depth):
        decoder_layers.append(
            Dense(
                decoder_dim[i], activation=activation, name="decoder_vae_" + str(i + 1)
            )
        )
    decoder_layer_outputs = []
    for i in range(depth):
        if i == 0:
            outs = decoder_layers[i](z)
        else:
            if dropout_layer:
                outs = decoder_layers[i](dropout_layer(decoder_layer_outputs[i - 1]))
            else:
                outs = decoder_layers[i](decoder_layer_outputs[i - 1])
        decoder_layer_outputs.append(outs)

    train_model = Model(inputs=input_layer, outputs=decoder_layer_outputs[-1])
    feature_extractor = Model(inputs=input_layer, outputs=encoder_layer_outputs[-1])

    def vae_loss(y_true, y_pred, mu, sigma):
        """
        loss for the variational auto enocder
        Args:
            y_true: keras tensor containing ground truth data
            y_pred: model predictions
            z_mean: mean of hidden variable
            z_log_var: variance of hidden variable
        """

        loss = tf.reduce_mean(K.square(y_true - y_pred))
        kl_loss = -0.5 * tf.reduce_mean(1 + sigma - tf.square(mu) - tf.exp(sigma))
        return loss + kl_loss

    if mode == 0:
        train_model.add_loss(
            vae_loss(input_layer, decoder_layer_outputs[-1], z_mean, z_log_var)
        )
        train_model.compile(loss=None, optimizer=optimizer)
        return train_model

    return train_model, feature_extractor, vae_loss
