# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""Cgan Sampler Module.

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
    Embedding,
    Flatten,
    Input,
    LeakyReLU,
    multiply,
)
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam


class CGAN_Sampler(BaseEstimator, TransformerMixin):
    """
    Conditional GAN sampler to generate synthetic samples for each class or pre-defined class.
    Reference: https://arxiv.org/pdf/1411.1784.pdf
    """

    def __init__(
        self,
        latentDim=100,
        generator=None,
        discriminator=None,
        optimizer=None,
        epochs=100,
        batch_size=128,
        num_samples_per_class=100,
    ):
        """
        Args:
        latentDim (integer,required)= dimensionality of latent space for autoencoder
        generator (keras.models.Model, optional) = generator deep learning multi layer keras model.
        discriminator (keras.models.Model, optional) = discriminator deep learning multi layer keras model.
        optimizer (string, optional) = choice of optimizer (adam, rmsprop)
        epochs (int, required) = number of epochs to run deep model on.
        batch_size (int, required) = mini batch size for optimization.
        num_samples_per_class (int, required) = number of instances to oversample for a given classs.
        """
        self.latentDim = latentDim
        self.generator = generator
        self.discriminator = discriminator
        self.epochs = epochs
        self.batch_size = batch_size
        self.optimizer = optimizer
        self.num_samples_per_class = num_samples_per_class

    def _build_generator(self, latent_dim, data_dim, num_classes):
        """
            Buil generator method.
            Parameters
                latentDim (integer,required)= dimensionality of latent space for autoencoder
                data_dim (interger,required)= dimensionality of data_dim to build generator.
                num_classes (integer,required)
            
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
        model.add(Dense(np.prod(data_dim), activation="tanh"))

        noise = Input(shape=(latent_dim,))
        label = Input(shape=(1,), dtype="int32")
        label_embedding = Flatten()(Embedding(num_classes, latent_dim)(label))
        model_input = multiply([noise, label_embedding])
        img = model(model_input)
        return Model([noise, label], img)

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
        model.add(Dense(512, input_dim=np.prod(data_dim)))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.4))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.4))
        model.add(Dense(1, activation="sigmoid"))

        img = Input(shape=(data_dim,))
        label = Input(shape=(1,), dtype="int32")
        label_embedding = Flatten()(Embedding(num_classes, np.prod(data_dim))(label))
        model_input = multiply([img, label_embedding])
        validity = model(model_input)
        return Model([img, label], validity)

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
            Buil discriminator method.
            Parameters
                input_dim (integer,required).
                num_classes (interger,required).
            
            Return
                Model.
        """
        if self.generator is None:
            self.generator = self._build_generator(self.latentDim, input_dim, num_class)

        if self.discriminator is None:
            self.discriminator = self._build_discriminator(input_dim, num_class)


        losses = ["binary_crossentropy", "sparse_categorical_crossentropy"]

        self.discriminator.compile(
            loss="binary_crossentropy", optimizer=self._get_optimizer(), metrics=["accuracy"]
        )

        z = Input(shape=(self.latentDim,))
        z_label = Input(shape=(1,))
        img = self.generator([z, z_label])
        self.discriminator.trainable = False

        valid = self.discriminator([img, z_label])

        self.GANmodel = Model([z, z_label], valid)
        self.GANmodel.compile(loss=["binary_crossentropy"], optimizer=self._get_optimizer())

    def _train_model(self, labels, X, y):
        """
            Train model method.
            Paramters
                lables(interger,required)
                X (pandas dataframe or numpy array): Input samples to be used for train.
                y (pandas dataframe, required): Label for Input Data.
        """
        # start training
        self.num_classes = len(labels)
        y = y.reshape(-1, 1)

        valid = np.ones((self.batch_size, 1))
        fake = np.zeros((self.batch_size, 1))

        for epoch in range(self.epochs):

            noise = np.random.normal(0, 1, (self.batch_size, self.latentDim))
            sampled_labels = np.random.randint(
                0, self.num_classes, (self.batch_size, 1)
            )
            gen_dataX = self.generator.predict([noise, sampled_labels])

            idx = np.random.randint(0, X.shape[0], self.batch_size)
            dataX = X[idx]
            data_labels = y[idx]

            d_loss_real = self.discriminator.train_on_batch([dataX, data_labels], valid)
            d_loss_fake = self.discriminator.train_on_batch(
                [gen_dataX, sampled_labels], fake
            )
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            g_loss = self.GANmodel.train_on_batch([noise, sampled_labels], valid)
            # print ("%d [D loss: %f, acc.: %.2f%%, op_acc: %.2f%%] [G loss: %f]" % (epoch, d_loss[0], 100*d_loss[3], 100*d_loss[4], g_loss[0]))

    def generate_samples(self):
        """ returns newX, newY samples. """
        newX = []
        newY = []
        for i in range(self.num_classes):
            number_of_samples = self.num_samples_per_class
            noise = np.random.normal(0, 1, (number_of_samples, self.latentDim))
            sampled_labels = np.array([i for _ in range(number_of_samples)])
            gen_dataX = self.generator.predict([noise, sampled_labels])
            newX.extend(gen_dataX)
            newY.extend(sampled_labels)
        newX = np.array(newX)
        newY = np.array(newY)
        return newX, newY

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
