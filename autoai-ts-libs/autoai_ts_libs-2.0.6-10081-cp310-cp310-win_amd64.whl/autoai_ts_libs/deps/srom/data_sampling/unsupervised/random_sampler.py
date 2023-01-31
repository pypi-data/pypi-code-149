# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""Random Sampler Module.

.. moduleauthor:: SROM Team

"""


import collections

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class Random_MajorityClass_DownSampler(BaseEstimator, TransformerMixin):
    """
    A sampler to generate balanced dataset. Idea is to down sample the
    observations from majority class using size of the minority class.
    Here, class ratio parameter plays an important role here to decide the
    number of samples to be selected from majority class
    """

    def __init__(self, sampling_rate=1.0):
        """
        Args:
            sampling_rate (real value, required):
                Data sampling rate in majority class vs other class
        """
        self.sampling_rate = sampling_rate

    def fit(self, X, y):
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
        major_class_label = labels[label_value.index(self.max_value)]

        # minor class
        minor_mask = y != major_class_label
        self.minor_x = X[minor_mask]
        self.minor_y = y[minor_mask]

        # major class
        major_mask = y == major_class_label
        self.major_x = X[major_mask]
        self.major_y = y[major_mask]

        return self

    def generate_samples(self):
        """ generate samples X_sample, Y_sample. """
        threshold_to_filter = int(self.sampling_rate * float(self.min_value))
        random_index = np.random.randint(
            self.major_x.shape[0], size=threshold_to_filter
        )
        major_x_random_data = self.major_x[random_index, :]
        major_y_random_data = self.major_y[random_index]
        X_sample = np.concatenate((self.minor_x, major_x_random_data), axis=0)
        Y_sample = np.concatenate((self.minor_y, major_y_random_data), axis=0)
        return X_sample, Y_sample

    def fit_sample(self, X, y):
        """ fit and generate samples. """
        self.fit(X, y)
        return self.generate_samples()


class Random_MinorityClass_UpSampler(BaseEstimator, TransformerMixin):
    """
    A sampler to generate balanced dataset. Idea is to up sample the
    observations from minority class using size of the minority class.
    Here, class ratio parameter plays an important role here to decide the
    number of samples to be generated from minority class
    """

    def __init__(self, sampling_rate=2):
        """
        Args:
            sampling_rate (real value, required):
                Data sampling rate in minority class vs other class
        """
        self.sampling_rate = sampling_rate

    def fit(self, X, y):
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

        self.max_value = max(label_value)
        self.major_class_label = labels[label_value.index(self.max_value)]

        self.labels = labels
        self.train_X = X
        self.train_y = y

        return self

    def generate_samples(self):
        """ generate samples X_sample, Y_sample. """
        X_sample = []
        Y_sample = []
        for lbl in self.labels:
            _mask = self.train_y == lbl
            tmpX = self.train_X[_mask]
            tmpY = self.train_y[_mask]

            if self.major_class_label != lbl:
                random_index = np.random.randint(
                    tmpX.shape[0], size=self.sampling_rate * tmpX.shape[0]
                )
                _x_random_data = tmpX[random_index, :]
                _y_random_data = tmpY[random_index]
                X_sample.extend(_x_random_data)
                Y_sample.extend(_y_random_data)
            else:
                X_sample.extend(tmpX)
                Y_sample.extend(tmpY)

        return (
            pd.DataFrame(X_sample).values,
            pd.DataFrame(Y_sample).transpose().values[0],
        )

    def fit_sample(self, X, y):
        """ fit and generate samples. """
        self.fit(X, y)
        return self.generate_samples()


class Random_Classwise_BalancedSampler(BaseEstimator, TransformerMixin):
    """
    A sampler to generate balanced dataset. Idea is to down sample the
    observations from majority class using size of the minority class.
    Here, class ratio parameter plays an important role here to decide the
    number of samples to be generated
    """

    def __init__(self, sample_per_class="auto"):
        """
        Args:
            sample_per_class: proportion of sample to retain per class
        """
        self.sample_per_class = sample_per_class

    def fit(self, X, y):
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

        if self.sample_per_class == "auto":
            self.sample_per_class = np.min(label_value)

        self.labels = labels
        self.train_X = X
        self.train_y = y

        return self

    def generate_samples(self):
        """ generate samples X_sample, Y_sample. """
        X_sample = []
        Y_sample = []
        for lbl in self.labels:
            _mask = self.train_y == lbl
            tmpX = self.train_X[_mask]
            tmpY = self.train_y[_mask]

            random_index = np.random.randint(tmpX.shape[0], size=self.sample_per_class)
            _x_random_data = tmpX[random_index, :]
            _y_random_data = tmpY[random_index]
            X_sample.extend(_x_random_data)
            Y_sample.extend(_y_random_data)
        return (
            pd.DataFrame(X_sample).values,
            pd.DataFrame(Y_sample).transpose().values[0],
        )

    def fit_sample(self, X, y):
        """ fit and generate samples. """
        self.fit(X, y)
        return self.generate_samples()


class DataSampler(BaseEstimator, TransformerMixin):
    """
    In some cases we like to sample the data for processing
    """

    def __init__(self, num_samples, random_state=None, shuffle=True, stratify=None):
        """
        Args:
            sample_per_class: proportion of sample to retain per class
        """
        self.num_samples = num_samples
        self.random_state = random_state
        self.shuffle = shuffle
        self.stratify = stratify

    def fit(self, X, y=None):
        """
        Fits base_model, num_iteration times.
        Args:
            X (pandas dataframe or numpy array, required): pandas dataframe or numpy array
            y (pandas dataframe or numpy array, required): pandas dataframe or numpy array
        """
        return self

    def generate_samples(self, X, y=None):
        """ generate samples X_sample, Y_sample. """

        if len(X) <= self.num_samples:
            if y is not None:
                return X, y
            else:
                return X, None

        from sklearn.model_selection import train_test_split

        if y is not None:
            X_train, _, y_train, _ = train_test_split(
                X,
                y,
                test_size=len(X) - self.num_samples,
                random_state=self.random_state,
                shuffle=self.shuffle,
                stratify=self.stratify,
            )
            return X_train, y_train
        else:
            X_train, _ = train_test_split(
                X,
                test_size=len(X) - self.num_samples,
                random_state=self.random_state,
                shuffle=self.shuffle,
                stratify=self.stratify,
            )
            return X_train, None

    def fit_sample(self, X, y=None):
        """ fit and generate samples. """
        self.fit(X, y)
        return self.generate_samples(X, y)

    def fit_transform(self, X, y=None):
        """ fit and generate samples. """
        return self.fit(X, y).transform(X)

    def transform(self, X):
        return self.generate_samples(X)
