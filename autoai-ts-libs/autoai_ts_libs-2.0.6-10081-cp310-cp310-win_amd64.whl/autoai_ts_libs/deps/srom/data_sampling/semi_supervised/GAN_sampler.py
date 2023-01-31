# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import collections

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow.keras.layers import BatchNormalization, Dense, Dropout, Input, LeakyReLU
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

"""Gan Sampler Module.

.. moduleauthor:: SROM Team

""" 


class SGAN_MajorityClass_DownSampler(BaseEstimator, TransformerMixin):
    """
    A sampler to generate synthetic samples for Majority class.
    """

    def __init__(
        self,
        latentDim=100,
        generator=None,
        discriminator=None,
        optimizer=None,
        epochs=100,
        batch_size=128,
        sampling_rate=1,
    ):
        """
        Args:
        latentDim (integer,required)= dimensionality of latent space for autoencoder
        generator (keras.models.Model, optional) = generator deep learning multi layer keras model.
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
        model.add(Dense(256, input_dim=latent_dim))
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

    def _build_discriminator(self, data_dim, num_classes):
        """
            Buil discriminator method.
            Parameters
                latentDim (integer,required)= dimensionality of latent space for autoencoder
                num_classes (interger,required).
            
            Return
                Model.
        """
        model = Sequential()
        model.add(Dense(31, input_dim=data_dim))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.25))
        model.add(Dense(16))
        model.add(LeakyReLU(alpha=0.2))

        img = Input(shape=(data_dim,))
        features = model(img)
        valid = Dense(1, activation="sigmoid")(features)
        label = Dense(num_classes + 1, activation="softmax")(features)
        return Model(img, [valid, label])

    def _build_optimizer(self):
        """
            Method to build the optimizer.
        """
        return Adam(0.0002, 0.5)

    def _get_optimizer(self):
        if self.optimizer is None:
            return self._build_optimizer()
        return self.optimizer

    def _prepare_model(self, input_dim, num_class):
        """
            Prepare model method.
            Parameters
                input_dim (integer,required).
                num_classes (interger,required).
            
            Return
                Model.
        """
        if self.generator is None:
            self.generator = self._build_generator(self.latentDim, input_dim)

        if self.discriminator is None:
            self.discriminator = self._build_discriminator(input_dim, num_class)

        self.discriminator.compile(
            loss=["binary_crossentropy", "categorical_crossentropy"],
            loss_weights=[0.5, 0.5],
            optimizer=self._get_optimizer(),
            metrics=["accuracy"],
        )

        z = Input(shape=(self.latentDim,))
        img = self.generator(z)
        self.discriminator.trainable = False
        valid, _ = self.discriminator(img)
        self.GANmodel = Model(z, valid)
        self.GANmodel.compile(loss="binary_crossentropy", optimizer=self._get_optimizer())

    def _train_model(self, labels, X, y):
        """
            Train model method.
            Paramters
                lables(interger,required)
                X (pandas dataframe or numpy array): Input samples to be used for train.
                y (pandas dataframe, required): Label for Input Data.
        """
        # start training
        half_batch = int(self.batch_size / 2)
        num_classes = len(labels)
        cw1 = {0: 1, 1: 1}
        cw2 = {i: num_classes / half_batch for i in range(num_classes)}
        cw2[num_classes] = 1 / half_batch

        for epoch in range(self.epochs):

            noise = np.random.normal(0, 1, (half_batch, self.latentDim))
            gen_dataX = self.generator.predict(noise)

            idx = np.random.randint(0, X.shape[0], half_batch)
            dataX = X[idx]

            valid = np.ones((half_batch, 1))
            fake = np.zeros((half_batch, 1))
            real_labels = to_categorical(y[idx], num_classes=num_classes + 1)
            fake_labels = to_categorical(
                np.full((half_batch, 1), num_classes), num_classes=num_classes + 1
            )

            d_loss_real = self.discriminator.train_on_batch(
                dataX, [valid, real_labels], class_weight=[cw1, cw2]
            )
            d_loss_fake = self.discriminator.train_on_batch(
                gen_dataX, [fake, fake_labels], class_weight=[cw1, cw2]
            )
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
            g_loss = self.GANmodel.train_on_batch(noise, valid)
            # print ("%d [D loss: %f, acc.: %.2f%%] [G loss: %f]" % (epoch, d_loss[0], 100*d_loss[1], g_loss))

    def generate_samples(self):
        """
            Generate samples method
        """
        number_of_samples = int(self.sampling_rate * float(self.min_value))
        noise = np.random.normal(0, 1, (number_of_samples, self.latentDim))
        gen_dataX = self.generator.predict(noise)
        _, sample_lbl = self.discriminator.predict(gen_dataX)
        return gen_dataX, sample_lbl

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

        self._prepare_model(X.shape[1], len(labels))
        self._train_model(labels, X, y)

        gen_dataX, sample_lbl = self.generate_samples()

        return gen_dataX, sample_lbl
