# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
In this module we define some custom loss functions to train models with missing data.
To pass these loss functions to the `compile` method of keras models, first get a function
with the desired `value_to_ignore` parameter as follows. If the desired value to ignore is `MV`,
we get a handle to the loss function as:

loss_masked_mae = lambda y_true, y_pred : masked_mae(y_true, y_pred, MV)
We can use this function to compile our model:
model.compile(optimizer='sgd', loss=loss_masked_mae)
"""

import tensorflow.keras.backend as K
import tensorflow as tf
from tensorflow.keras.optimizers import get


def masked_mae(y_true, y_pred, value_to_ignore):
    """
    Mean Absolute Error loss function that ignores a desired value in the true signal
    Args:
        y_true: keras tensor containing ground truth data
        y_pred: model predictions
        value_to_ignore: value to ignore in the ground truth while computing absolute error
                         between ground truth and prediction
    Returns:
        tensor: tensor with Mean Absolute Error
    """
    mask = K.not_equal(y_true, value_to_ignore)
    return K.mean(K.tf.boolean_mask(K.abs(y_true - y_pred), mask), axis=None)


def masked_mse(y_true, y_pred, value_to_ignore):
    """
    Mean Squared Error loss function that ignores a desired value in the true signal
    Args:
        y_true: keras tensor containing ground truth data
        y_pred: model predictions
        value_to_ignore: value to ignore in the ground truth while computing squared error between
                         ground truth and prediction
    Returns:
        tensor: tensor with Mean Squared Error
    """
    mask = K.not_equal(y_true, value_to_ignore)
    return K.mean(K.tf.boolean_mask(K.square(y_true - y_pred), mask), axis=None)


def get_optimizer(optimizer, **kwargs):
    """[summary] Returns a new optimizer with updated parameters. 
    Input can be the name of an optimizer from `tensorflow.keras.optimizers` or 
    an existing optimizer object.

    Args:
        optimizer ([string, optimizer]): [description] Name of an optimizer or an existing 
                                          optimizer object

    Returns:
        [optimizer]: [description] A new optimizer object with updated parameters
    """
    saved_args = locals()
    current_optimizer = get(optimizer)
    opt_config = current_optimizer.get_config()

    # update any parameters in opt_config specified by the caller in kwargs    
    for item in saved_args['kwargs'].keys():
        if item in opt_config.keys():
            opt_config[item] = saved_args['kwargs'][item]

    # create dict needed to 'get' a new optimizer
    opt_config = {'class_name': opt_config['name'], 
                  'config': opt_config
                 }
    
    new_optimizer = get(opt_config)
    return new_optimizer

#from tensorflow.keras.optimizers import Adam
#opt1 = get_optimizer('adam')
#opt2 = get_optimizer(opt1, learning_rate=0.3)
#print(opt1.get_config())
#print(opt2.get_config())

#from tensorflow.keras.optimizers import Adam
#opt3 = get_optimizer(Adam())
