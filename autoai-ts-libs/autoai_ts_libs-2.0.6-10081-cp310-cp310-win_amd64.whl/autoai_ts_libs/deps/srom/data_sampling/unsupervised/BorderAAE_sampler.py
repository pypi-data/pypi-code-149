# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""BorderAAE Sampler Module.

.. moduleauthor:: SROM Team

"""

import collections

import numpy as np
import pandas as pd
import tensorflow.keras.backend as K
from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow.keras.layers import Dense, Input, LeakyReLU
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Lambda

from autoai_ts_libs.deps.srom.data_sampling.unsupervised.SMOTE_sampler import sample


class BorderAAE_Sampler(BaseEstimator, TransformerMixin):
    """
    A sampler to generate instances in the boundary of latent space using Adversarial Autoencoder and interpolation.
    Part of Research paper being drafted by SROM group.
    """

    def __init__(
        self,
        latentDim=100,
        encoder=None,
        decoder=None,
        discriminator=None,
        optimizer=None,
        epochs=100,
        batch_size=32,
        proportion=1,
    ):
        """
        Args:
        latentDim (integer,required)= dimensionality of latent space for autoencoder
        encoder (keras.models.Model, optional) = encoder deep learning multi layer keras model.
        decoder (keras.models.Model, optional) = decoder deep learning multi layer keras model.
        discriminator (keras.models.Model, optional) = discriminator deep learning multi layer keras model.
        optimizer (string, optional) = choice of optimizer (adam, rmsprop)
        epochs (int, required) = number of epochs to run deep model on.
        batch_size (int, required) = mini batch size for optimization.
        proportion (float, required) = proportion of the difference of n_maj and n_min to sample for example
        1,0 means that after sampling the number of minority samples will be equal to number of majority samples.

        """
        self.latentDim = latentDim
        self.encoder = encoder
        self.decoder = decoder
        self.discriminator = discriminator
        self.epochs = epochs
        self.batch_size = batch_size
        self.optimizer = optimizer
        self.proportion = proportion

    def _build_encoder(self, latent_dim, data_dim):
        """
            Buil encoder method.
            Parameters
                latentDim (integer,required)= dimensionality of latent space for autoencoder
                data_dim (interger,required)= dimensionality of data_dim to build generator.
            
            Return
                Model.
        """
        inp = Input(shape=(data_dim,))
        h = Dense(512)(inp)
        h = LeakyReLU(alpha=0.2)(h)
        h = Dense(512)(h)
        h = LeakyReLU(alpha=0.2)(h)
        mu = Dense(latent_dim)(h)
        log_var = Dense(latent_dim)(h)
        latent_repr = Lambda(
            lambda p: p[0] + K.random_normal(K.shape(p[0])) * K.exp(p[1] / 2),
            lambda p: p[0],
        )([mu, log_var])
        return Model(inp, latent_repr)

    def _build_decoder(self, latent_dim, data_dim):
        """
            Buil decoder method.
            Parameters
                latentDim (integer,required)= dimensionality of latent space for autoencoder
                data_dim (interger,required)= dimensionality of data_dim to build generator.
            
            Return
                Model.
        """
        model = Sequential()
        model.add(Dense(512, input_dim=latent_dim))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(data_dim, activation="tanh"))
        z = Input(shape=(latent_dim,))
        img = model(z)
        return Model(z, img)

    def _build_discriminator(self, latent_dim):
        """
            Buil discriminator method.
            Parameters
                latentDim (integer,required)= dimensionality of latent space for autoencoder
            
            Return
                Model.
        """
        model = Sequential()
        model.add(Dense(512, input_dim=latent_dim))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(256))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(1, activation="sigmoid"))

        img = Input(shape=(latent_dim,))
        validity = model(img)
        return Model(img, validity)

    def _build_optimizer(self):
        """
            Method to build the optimizer.
        """
        return Adam(0.0002, 0.5)

    def _get_optimizer(self):
        if self.optimizer is None:
            return self._build_optimizer()
        return self.optimizer

    def _prepare_model(self, input_dim):
        """
            Prepare model method.
            Parameters
                input_dim (integer,required).
            
            Return
                Model.
        """
        if self.encoder is None:
            self.encoder = self._build_encoder(self.latentDim, input_dim)

        if self.decoder is None:
            self.decoder = self._build_decoder(self.latentDim, input_dim)

        if self.discriminator is None:
            self.discriminator = self._build_discriminator(self.latentDim)

        self.discriminator.compile(
            loss="binary_crossentropy", optimizer=self._get_optimizer(), metrics=["accuracy"]
        )

        z = Input(shape=(input_dim,))
        encoded_z = self.encoder(z)
        reconstructed_z = self.decoder(encoded_z)

        self.discriminator.trainable = False
        validity = self.discriminator(encoded_z)

        self.AAEmodel = Model(z, [reconstructed_z, validity])
        self.AAEmodel.compile(
            loss=["mse", "binary_crossentropy"],
            loss_weights=[0.999, 0.001],
            optimizer=self._get_optimizer(),
        )

    def _train_model(self, X):
        """
            Train model method.
            Paramters
                lables(interger,required)
                X (pandas dataframe or numpy array): Input samples to be used for train.
        """
        half_batch = int(self.batch_size / 2)

        for epoch in range(self.epochs):

            latent_real = np.random.normal(size=(half_batch, self.latentDim))

            idx = np.random.randint(0, X.shape[0], half_batch)
            dataX = X[idx]
            latent_fake = self.encoder.predict(dataX)

            valid = np.ones((half_batch, 1))
            fake = np.zeros((half_batch, 1))

            d_loss_real = self.discriminator.train_on_batch(latent_real, valid)
            d_loss_fake = self.discriminator.train_on_batch(latent_fake, fake)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            g_loss = self.AAEmodel.train_on_batch(dataX, [dataX, valid])
            # print ("%d [D loss: %f, acc: %.2f%%] [G loss: %f, mse: %f]" % (epoch, d_loss[0], 100*d_loss[1], g_loss[0], g_loss[1]))

    def fit_sample(self, X, y):
        """
        Fits base_model, num_iteration times.
        Args:
            X (pandas dataframe or numpy array, required): pandas dataframe or numpy array
            y (pandas dataframe or numpy array, required): pandas dataframe or numpy array
        """
        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, pd.Series):
            y = np.array(y)

        label_list = list(y)
        label_counter = collections.Counter(label_list)
        label_value = []
        labels = []
        for item in label_counter:
            label_value.append(label_counter[item])
            labels.append(item)

        # print (label_value)
        # print (labels)
        self.min_value = min(label_value)
        self.max_value = max(label_value)
        self.major_class_label = labels[label_value.index(self.max_value)]
        self.minor_class_label = labels[label_value.index(self.min_value)]

        # minor class
        minor_mask = y == self.minor_class_label
        major_mask = y == self.major_class_label
        self.major_x = X[major_mask]
        self.minor_x = X[minor_mask]
        self.minor_y = y[minor_mask]

        self._prepare_model(X.shape[1])
        train_major_X = X[y == self.major_class_label, :]
        train_minor_X = X[y == self.minor_class_label, :]
        self._train_model(X)

        encoded_major_train = self.encoder.predict(train_major_X)
        encoded_minor_train = self.encoder.predict(train_minor_X)

        encoded_all = np.concatenate((encoded_major_train, encoded_minor_train), axis=0)
        encoded_labels_all = np.concatenate(
            (
                np.repeat(self.major_class_label, encoded_major_train.shape[0]),
                np.repeat(self.minor_class_label, encoded_minor_train.shape[0]),
            ),
            axis=0,
        )

        enc_X_sample, Y_sample = sample(
            X=encoded_all, y=encoded_labels_all, proportion=self.proportion
        )
        X_sample = self.decoder.predict(enc_X_sample)
        return X_sample, Y_sample
