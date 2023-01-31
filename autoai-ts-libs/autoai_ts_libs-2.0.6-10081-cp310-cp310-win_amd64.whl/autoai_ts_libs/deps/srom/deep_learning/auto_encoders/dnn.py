# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: dnn
   :synopsis: dnn.

.. moduleauthor:: SROM Team 
"""

import tensorflow as tf
from tensorflow.keras import initializers, layers
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

from autoai_ts_libs.deps.srom.deep_learning.utils import get_optimizer

import logging
LOGGER = logging.getLogger(__name__)

def deep_autoencoder(
    input_dimension,
    encoding_dimension,
    output_dimension=None,
    hidden_dimension=20,
    depth=2,
    activation="relu",
    dropout_rate=0.0,
    optimizer="adam",
    learning_rate=0.001,
    loss="mean_squared_error",
    mode=0,
):
    """Builds an autoencoder
    :params: `input_dim` (number of features)
             `encoding_dim` (number of encoding features)
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

    # adding encoding_dim
    if encoding_dimension == None:
        raise Exception('Please specify the encoding_dimension in the argument')

    # adding input_dimension
    if input_dimension == None:
        raise Exception('Please specify the input_dimension in the argument')

    
    if output_dimension is None:
        output_dimension = input_dimension
        # hidden_dimension = input_dimension

    if isinstance(hidden_dimension, list):
        hidden_dim = hidden_dimension
        if len(hidden_dimension) != depth:
            raise Exception(
                "Desired depth is %d but %d hidden layer sizes have been provided"
                % (depth, len(hidden_dimension))
            )
    else:
        hidden_dim = int(hidden_dimension)
        hidden_dim = [hidden_dim] * depth

    hidden_dim = hidden_dim + [encoding_dimension]

    input_layer = Input(shape=(input_dimension,))
    # if dropout > 0.0:
    dropout_layer = Dropout(dropout_rate)
    encoder_layers = []
    for i, layer_dim in enumerate(hidden_dim):
        encoder_layers.append(
            Dense(layer_dim, activation=activation, name="encoder_ae_" + str(i + 1))
        )

    encoder_layer_outputs = []
    for i, layer_dim in enumerate(hidden_dim):
        if i == 0:
            outs = encoder_layers[i](input_layer)
        else:
            if dropout_rate > 0.0:
                outs = encoder_layers[i](dropout_layer(encoder_layer_outputs[i - 1]))
            else:
                outs = encoder_layers[i](encoder_layer_outputs[i - 1])

        encoder_layer_outputs.append(outs)


    decoder_layers = []
    # decoder_dim = [encoding_dimension] + hidden_dim[:-1][::-1] + [output_dimension]
    decoder_dim = hidden_dim[:-1][::-1] + [output_dimension]   # [8,16, output_dim]
    for i, layer_dim in enumerate(decoder_dim):
        # don't use activation at the output
        if i == len(decoder_dim)-1:
            decoder_layers.append(
            Dense(
                decoder_dim[i], activation=None, name="decoder_ae_" + str(i + 1)
                )
            )
        else:
            decoder_layers.append(
            Dense(
                decoder_dim[i], activation=activation, name="decoder_ae_" + str(i + 1)
            )
        )
        

    decoder_layer_outputs = []
    for i, layer_dim in enumerate(decoder_dim):
        if i == 0:
            outs = decoder_layers[i](encoder_layer_outputs[-1])
        else:
            if dropout_rate > 0.0:
                outs = decoder_layers[i](dropout_layer(decoder_layer_outputs[i - 1]))
            else:
                outs = decoder_layers[i](decoder_layer_outputs[i - 1])
        decoder_layer_outputs.append(outs)

    # define optimizer 
    opt = get_optimizer(optimizer, learning_rate=learning_rate)

    train_model = Model(inputs=input_layer, outputs=decoder_layer_outputs[-1])
    train_model.compile(loss=loss, optimizer=opt)
    feature_extractor = Model(inputs=input_layer, outputs=encoder_layer_outputs[-1])
    if mode == 0:
        return train_model
    return train_model, feature_extractor


def uniform_deep_autoencoder(
    input_dimension,
    encoding_dimension=3,    
    output_dimension=None,
    neuron_reduction_gradient=0.5,    
    activation="relu",
    dropout_rate=0.0,
    mode=0,
):

    """Builds an autoencoder
    :params: `input_dim` (number of features)
             `output_dim` (number of output features)
             `encoding_dim` (the number of time steps to be represented by the encoding)
             `neuron_reduction_gradient` (reduce the number of neurons by this value
             from the previous layer)
             `activation` (type of activation to use at each layer, defaults to relu)
             `dropout` (dropout parameter for inputs to each of the hidden layers in
              the encoder and decoder)
    :outputs: `train_model` (encoder-decoder model to be used for training)
              `feature_extractor` (encoder only model which can be used to extract
              embeddings post training)

    """


    if (neuron_reduction_gradient >= 1) | (neuron_reduction_gradient <= 0):
        raise Exception(
                "Desired neuron_reduction_gradient must be less than 1 and greater than 0"
            )

    # hidden dimension list creation
    hidden_dim = []
    input_dim_ = int(input_dimension * neuron_reduction_gradient)
    
    while input_dim_ >= encoding_dimension:
        hidden_dim.append(input_dim_)
        input_dim_ = int(input_dim_ * neuron_reduction_gradient)

    return deep_autoencoder(
        input_dimension=input_dimension,
        encoding_dimension=encoding_dimension,   
        output_dimension=output_dimension,     
        hidden_dimension=hidden_dim,
        depth=len(hidden_dim),
        activation=activation,
        dropout_rate=dropout_rate,
        mode=mode,
    )

def simple_autoencoder(
    input_dimension,
    encoding_dimension,       
    hidden_dimension=[64,16],        
    optimizer='adam',
    learning_rate=0.001,
    loss="mean_squared_error",        
    mode=0
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        encoding_dimension ([type]): [description]
        hidden_dimension (list, optional): [description]. Defaults to [64,16].
        optimizer (str, optional): [description]. Defaults to 'adam'.
        learning_rate (float, optional): [description]. Defaults to 0.001.
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        mode (int, optional): [description]. Defaults to 0.

    Returns:
        [type]: [description]
    """

    LOGGER.debug("Calling simple_autoencoder()")
    

    return deep_autoencoder(
        input_dimension=input_dimension,
        encoding_dimension=encoding_dimension,           
        hidden_dimension=hidden_dimension,
        depth=len(hidden_dimension),
        optimizer=optimizer,
        learning_rate=learning_rate,
        loss=loss,
        mode=mode,
    )




# define the network architecture
def simple_ffn(
    output_dimension,
    layer_dims=(32,16),
    optimizer='adam',
    learning_rate=0.001,
    loss="mse",
    activation="relu",
    output_activation="linear",
    dropout_rate=0.1,
    ):
    """[summary]

    Args:
        output_dimension ([type]): [description]
        layer_dims (tuple, optional): [description]. Defaults to (32,16).
        optimizer ([string or object], optional): [description]. Defaults to 'adam'.
        learning_rate (float, optional): [description]. Defaults to 0.001.
        loss ([type], optional): [description]. Defaults to "mse".
        activation (str, optional): [description]. Defaults to "relu".
        output_activation (str, optional): [description]. Defaults to "linear".
        dropout_rate (float, optional): [description]. Defaults to 0.1.

    Returns:
        [type]: [description]
    """

    layer_dims = list(layer_dims) + [output_dimension]

    encoder = tf.keras.Sequential()

   # Encoder
    for dim in layer_dims[:-1]:
        encoder.add(layers.Dense(dim,
                        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.05, seed=10),
                        activation=activation,
                        )
                 )
        encoder.add(Dropout(rate=dropout_rate))

    # add the last encoder layer with no activation function
    encoder.add(layers.Dense(layer_dims[-1],
                            kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.05, seed=10),
                            activation=output_activation,
                            )
                 )
    encoder.add(Dropout(rate=dropout_rate))

    #opt = optimizer(lr=learning_rate)
    opt = get_optimizer(optimizer, learning_rate=learning_rate)
    encoder.compile(optimizer=opt, loss=loss)

    return encoder
