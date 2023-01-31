# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: neaural_network_nsa
   :synopsis: srom_neaural_network_nsa.
   
.. moduleauthor:: SROM Team
"""

from sklearn.base import BaseEstimator
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import tensorflow as tf


class NeuralNetworkNSA(BaseEstimator):
    """
    Anomaly detection using negative sample selection.
    """

    def __init__(
        self,
        scale,
        sample_ratio,
        sample_delta,
        anomaly_threshold=0.8,
        base_model=None,
        score_sign=-1,
        dropout=0.5,
        layer_width=8,
        n_hidden_layers=10,
        epochs=1000,
        batch_size=10,
        verbose=3,
        seed=42,
    ):
        """
        Parameters:
            scale (boolean): Enable scaling.
            sample_ratio (number) : Sample ratio.
            sample_delta (number): Sample delta.
            base_model (object): Model to be used for anomaly detection.
            anomaly_threshold (number) : Threshold for classifying anomaly.
            fit_params : Additional paramters to be used in fit method.
        """
        self.scale = scale
        self.sample_ratio = sample_ratio
        self.sample_delta = sample_delta
        self.anomaly_threshold = anomaly_threshold
        self.scaler = None
        self.score_sign = score_sign
        self.dropout = dropout
        self.layer_width = layer_width
        self.n_hidden_layers = n_hidden_layers
        self.base_model = base_model
        self.epochs = epochs
        self.batch_size = batch_size
        self.verbose = verbose
        self.seed = seed

    def fit(self, X, y=None):
        """
        Fit estimator.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of NSA.
        """
        if self.seed is not None:
            np.random.seed(self.seed)
            tf.random.set_seed(self.seed)

        Xt = X.copy()
        if self.base_model is None:
            self.base_model = self._get_model(
                input_dim=X.shape[1],
                dropout=self.dropout,
                layer_width=self.layer_width,
                n_hidden_layers=self.n_hidden_layers,
            )
        Xt = Xt.astype(np.float64)

        if isinstance(X, pd.DataFrame):
            Xt = Xt.to_numpy()

        Xdf = pd.DataFrame(Xt, columns=list(range(Xt.shape[1])))

        self.data_col = list(range(X.shape[1]))
        # scaling
        if self.scale:
            self.scaler = StandardScaler()
            Xdf = self.scaler.fit_transform(Xdf)

        if not isinstance(Xdf, pd.DataFrame):
            Xdf = pd.DataFrame(Xdf, columns=self.data_col)

        trainDb = self._generate_training_samples(Xdf)

        self.base_model.fit(
            trainDb[self.data_col].values,
            trainDb["class_label"],
            epochs=self.epochs,
            batch_size=self.batch_size,
            verbose=self.verbose,
        )
        return self

    def _get_neg_sample(self, pos_sample, n_points):
        """
            Internal method as a helper method
        """
        df_neg = pd.DataFrame()
        for clm_name in pos_sample.columns:
            low_val = np.min(pos_sample[clm_name])
            high_val = np.max(pos_sample[clm_name])
            delta_val = high_val - low_val
            df_neg[clm_name] = np.random.uniform(
                low=low_val - self.sample_delta * delta_val,
                high=high_val + self.sample_delta * delta_val,
                size=n_points,
            )
        return df_neg

    def _generate_training_samples(self, positive_sample):
        """
            Internal method as a helper method
        """
        n_neg_points = int(len(positive_sample) * self.sample_ratio)
        negative_sample = self._get_neg_sample(positive_sample, n_neg_points)

        positive_sample["class_label"] = 1
        negative_sample["class_label"] = 0

        training_sample = pd.concat(
            [positive_sample, negative_sample], ignore_index=True, sort=True
        )
        return training_sample.reindex(np.random.permutation(training_sample.index))

    def predict(self, X):
        """
        Return wheather given data point is anomaly or not. -1 for anomaly and 1 for non anomaly.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            anomaly values
        """
        tmp_score = self.anomaly_score(X)

        if self.score_sign < 0:
            tmp_score[tmp_score > self.anomaly_threshold] = 0
        else:
            tmp_score[tmp_score < self.anomaly_threshold] = 0

        tmp_score[tmp_score > 0] = 1
        tmp_score[tmp_score == 1] = -1
        tmp_score[tmp_score == 0] = 1
        return tmp_score

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """

        # each sample will be scored separately
        X = X.astype(np.float64)

        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()

        Xdf = pd.DataFrame(X, columns=list(range(X.shape[1])))

        # get the projected space if required
        if self.scale and self.scaler:
            Xdf = self.scaler.transform(Xdf)

        if not isinstance(Xdf, pd.DataFrame):
            Xdf = pd.DataFrame(Xdf, columns=self.data_col)

        preds = self.base_model.predict(Xdf, verbose=self.verbose)
        return preds[:, 0]

    def decision_function(self, X):
        """
        Predict raw anomaly score of X using the fitted detector.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        """
        return self.anomaly_score(X)

    def _get_model(
        self, input_dim, dropout, layer_width, n_hidden_layers,
    ):
        """
            Internal method as a helper method
        """
        model = tf.keras.Sequential()
        model.add(
            tf.keras.layers.Dense(layer_width, input_dim=input_dim, activation="relu")
        )
        model.add(tf.keras.layers.Dropout(dropout, seed=self.seed))

        for _ in range(n_hidden_layers):
            model.add(tf.keras.layers.Dense(layer_width, activation="relu"))
            model.add(tf.keras.layers.Dropout(dropout, seed=self.seed))

        model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

        model.compile(
            loss="binary_crossentropy",
            optimizer="adam",
            metrics=[tf.keras.metrics.binary_accuracy],
        )
        return model
