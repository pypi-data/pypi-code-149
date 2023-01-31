# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""Bigan Sampler Module.

.. moduleauthor:: SROM Team

"""

import collections

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow.keras.layers import (
    BatchNormalization,
    Dense,
    Dropout,
    Input,
    LeakyReLU,
    concatenate,
)
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam


class BIGAN_MajorityClass_DownSampler(BaseEstimator, TransformerMixin):
    """
    Bi-Directional Generative Adversarial Network (BiGAN) based Majority class downsampler.
    """

    def __init__(
        self,
        latentDim=100,
        generator=None,
        discriminator=None,
        encoder=None,
        optimizer=None,
        epochs=100,
        batch_size=128,
        sampling_rate=1,
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
        sampling_rate (float, required) = proportion of the difference of n_maj and n_min to sample for example
        1,0 means that after sampling the number of minority samples will be equal to number of majority samples.
        """
        self.latentDim = latentDim
        self.generator = generator
        self.discriminator = discriminator
        self.epochs = epochs
        self.batch_size = batch_size
        self.optimizer = optimizer
        self.sampling_rate = sampling_rate
        self.encoder = encoder

    def _build_generator(self, latent_dim, data_dim):
        """
            Buil generator method.
            Parameters
                latentDim (integer,required)= dimensionality of latent space for autoencoder
                data_dim (interger,required)= dimensionality of data_dim to build generator.
            
            Return
                Model.
        """
        model = Sequential()
        model.add(Dense(512, input_dim=latent_dim))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(1024))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(data_dim, activation="tanh"))
        noise = Input(shape=(latent_dim,))
        img = model(noise)
        return Model(noise, img)

    def _build_encoder(self, latent_dim, data_dim):
        """
            Buil encoder method.
            Parameters
                latentDim (integer,required)= dimensionality of latent space for autoencoder
                data_dim (interger,required)= dimensionality of data_dim to build generator.
            
            Return
                Model.
        """
        model = Sequential()
        model.add(Dense(512, input_shape=(data_dim,)))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(latent_dim))
        img = Input(shape=(data_dim,))
        z = model(img)
        return Model(img, z)

    def _build_discriminator(self, latent_dim, data_dim):
        """
            Buil discriminator method.
            Parameters
                latentDim (integer,required)= dimensionality of latent space for autoencoder
                data_dim (interger,required)= dimensionality of data_dim to build generator.
            
            Return
                Model.
        """
        z = Input(shape=(latent_dim,))
        img = Input(shape=(data_dim,))
        d_in = concatenate([z, img])

        model = Dense(1024)(d_in)
        model = LeakyReLU(alpha=0.2)(model)
        model = Dropout(0.5)(model)
        model = Dense(1024)(model)
        model = LeakyReLU(alpha=0.2)(model)
        model = Dropout(0.5)(model)
        model = Dense(1024)(model)
        model = LeakyReLU(alpha=0.2)(model)
        model = Dropout(0.5)(model)
        validity = Dense(1, activation="sigmoid")(model)
        return Model([z, img], validity)

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
        if self.generator is None:
            self.generator = self._build_generator(self.latentDim, input_dim)

        if self.discriminator is None:
            self.discriminator = self._build_discriminator(self.latentDim, input_dim)

        if self.encoder is None:
            self.encoder = self._build_encoder(self.latentDim, input_dim)

        self.discriminator.compile(
            loss="binary_crossentropy", optimizer=self._get_optimizer(), metrics=["accuracy"]
        )
        self.discriminator.trainable = False

        z = Input(shape=(self.latentDim,))
        gen_z = self.generator(z)

        inData = Input(shape=(input_dim,))
        inData_ = self.encoder(inData)

        fake = self.discriminator([z, gen_z])
        valid = self.discriminator([inData_, inData])

        self.BIGANmodel = Model([z, inData], [fake, valid])
        self.BIGANmodel.compile(
            loss=["binary_crossentropy", "binary_crossentropy"],
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

        for _ in range(self.epochs):

            noise = np.random.normal(0, 1, (half_batch, self.latentDim))
            gen_dataX = self.generator.predict(noise)

            idx = np.random.randint(0, X.shape[0], half_batch)
            dataX = X[idx]
            dataX_ = self.encoder.predict(dataX)

            valid = np.ones((half_batch, 1))
            fake = np.zeros((half_batch, 1))

            d_loss_real = self.discriminator.train_on_batch([dataX_, dataX], valid)
            d_loss_fake = self.discriminator.train_on_batch([noise, gen_dataX], fake)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            g_loss = self.BIGANmodel.train_on_batch([noise, dataX], [valid, fake])
            # print ("%d [D loss: %f, acc.: %.2f%%] [G loss: %f]" % (epoch, d_loss[0], 100*d_loss[1], g_loss))

    def generate_samples(self):
        """ generate samples X_sample, Y_sample. """
        number_of_samples = int(self.sampling_rate * float(self.min_value))
        noise = np.random.normal(0, 1, (number_of_samples, self.latentDim))
        gen_dataX = self.generator.predict(noise)
        X_sample = np.concatenate((self.minor_x, gen_dataX), axis=0)
        Y_sample = np.concatenate(
            (self.minor_y, np.repeat(self.major_class_label, number_of_samples)), axis=0
        )
        return X_sample, Y_sample

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

        self.min_value = min(label_value)
        self.max_value = max(label_value)
        self.major_class_label = labels[label_value.index(self.max_value)]

        # minor class
        minor_mask = y != self.major_class_label
        self.minor_x = X[minor_mask]
        self.minor_y = y[minor_mask]

        self._prepare_model(X.shape[1])
        train_X = X[y == self.major_class_label, :]
        self._train_model(train_X)

        gen_dataX, sample_lbl = self.generate_samples()

        return gen_dataX, sample_lbl
