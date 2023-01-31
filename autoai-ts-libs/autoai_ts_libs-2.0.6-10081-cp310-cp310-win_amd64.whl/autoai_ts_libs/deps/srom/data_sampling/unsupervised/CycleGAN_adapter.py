# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""CycleGAN Sampler Module.

.. moduleauthor:: SROM Team

"""


from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow.keras.layers import Conv1D, LeakyReLU

from tensorflow_addons.layers import InstanceNormalization


class CycleGAN(BaseEstimator, TransformerMixin):
    """
    A domain adapter to generate instances in the boundary of latent space using Adversarial Autoencoder and interpolation.
    Part of Research paper being drafted by SROM group.
    """

    def __init__(self):
        pass

    def _build_generator(self, latent_dim, data_dim):

        # 1D Convolution
        def conv1d(layer_input, filters, f_size=4):
            d = Conv1D(filters, kernel_size=f_size)(layer_input)
            d = LeakyReLU(alpha=0.2)(d)
            d = InstanceNormalization()(d)
            return d

        pass

    def _build_discriminator(self, data_dim):
        pass

    def _build_optimizer(self):
        pass

    def _prepare_model(self, input_dim):
        pass

    def _train_model(self, X):
        pass

    def fit(self, X, y):
        pass
