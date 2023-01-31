# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: lstm_sequence_classification
   :synopsis: Code to perform sequence classification, for predictive maintainance type of data.

.. moduleauthor:: SROM Team
"""
import numpy as np
from sklearn.base import BaseEstimator
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential


class LSTMSequenceClassification(BaseEstimator):
    """
    Simple AutoEncoderMethod based Anomaly
    """

    def __init__(
        self,
        hidden_dim=10,
        depth=3,
        lstm_dropout=0.0,
        epochs=250,
        batch_size=1000,
        shuffle=True,
        verbose=0,
        loss="binary_crossentropy",
        optimizer="adam",
        metric="accuracy",
    ):
        """
        Builds an LSTM Classifier.

        Parameters:
            hidden_dim: Number of hidden nodes in the LSTM layer, can be an int, \
                    i.e. all layers are of the same size, or a list of length `depth`,\
                    specifying the size of each hidden layer.
            depth: Depth of the LSTM model.
            lstm_dropout: Dropout parameter for inputs to the LSTM layers.

        Returns:
            keras.models.Model: Encoder-decoder model to be used for training.
        """

        if isinstance(hidden_dim, list) and len(hidden_dim) != depth:
            raise Exception("Error")
        if isinstance(hidden_dim, int):
            hidden_dim = [hidden_dim] * depth

        self.hidden_dim = hidden_dim
        self.lstm_dropout = lstm_dropout
        self.depth = depth
        self.epochs = epochs
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.verbose = verbose
        self.loss = loss
        self.optimizer = optimizer
        self.metric = metric

        self.model = None
        self.time_steps = None
        self.features = None
        self.output_dim = None

    def set_params(self, **kwarg):
        """
        Used to set params.
        """
        if "hidden_dim" in kwarg:
            self.hidden_dim = kwarg["hidden_dim"]
        if "lstm_dropout" in kwarg:
            self.lstm_dropout = kwarg["lstm_dropout"]
        if "depth" in kwarg:
            self.depth = kwarg["depth"]
        if "epochs" in kwarg:
            self.epochs = kwarg["epochs"]
        if "batch_size" in kwarg:
            self.batch_size = kwarg["batch_size"]
        if "shuffle" in kwarg:
            self.shuffle = kwarg["shuffle"]
        if "verbose" in kwarg:
            self.verbose = kwarg["verbose"]
        if "loss" in kwarg:
            self.loss = kwarg["loss"]
        if "optimizer" in kwarg:
            self.optimizer = kwarg["optimizer"]
        if "metric" in kwarg:
            self.metric = kwarg["metric"]

        if isinstance(self.hidden_dim, list) and len(self.hidden_dim) != self.depth:
            raise Exception("Error")
        if isinstance(self.hidden_dim, int):
            self.hidden_dim = [self.hidden_dim] * self.depth

    # a function to create a model
    def create_model(self):
        """
        Create model.
        """
        self.model = Sequential()
        stack_len = self.depth

        # First Stack
        self.model.add(
            LSTM(
                input_shape=(self.time_steps, self.features),
                units=self.hidden_dim[0],
                return_sequences=True,
            )
        )
        self.model.add(Dropout(self.lstm_dropout))

        # Intermediate Stack
        for i in range(1, (stack_len - 1)):
            self.model.add(LSTM(units=self.hidden_dim[i], return_sequences=True))
            self.model.add(Dropout(self.lstm_dropout))

        # Last Stack
        self.model.add(
            LSTM(units=self.hidden_dim[stack_len - 1], return_sequences=False)
        )
        self.model.add(Dropout(self.lstm_dropout))

        self.model.add(Dense(units=self.output_dim, activation="sigmoid"))
        self.model.compile(
            loss=self.loss, optimizer=self.optimizer, metrics=[self.metric]
        )

    # fit the model
    def fit(self, X, y):
        """
        Fit model.

        Parameters:
            X (pandas dataframe, required) : Pandas dataframe.
            y (pandas dataframe, required) : Pandas dataframe.

        Returns:
            Object: Instance of LSTMSequenceClassification.

        Raises:
            Exception: If length of X.shape is not equal to 3.
        """
        X = X.astype(np.float64)
        if len(X.shape) != 3:
            raise Exception("Training Data must be of 3 dimensional space")

        # some variable are inferred from input data size
        self.time_steps = X.shape[1]
        self.features = X.shape[2]
        self.output_dim = y.shape[1]

        # calling the create model function
        self.create_model()

        # call fit method
        self.model.fit(
            X,
            y,
            epochs=self.epochs,
            batch_size=self.batch_size,
            shuffle=self.shuffle,
            verbose=self.verbose,
            validation_split=0.05,
        )

        # need to check the need of evaluate function
        scores = self.model.evaluate(X, y, verbose=1, batch_size=200)
        print(("Accuracy: {}".format(scores[1])))

        return self

    # predict the label
    def predict(self, X):
        """
        Predict.

        Parameters:
            X (pandas dataframe, required) : Pandas dataframe.

        Returns:
            predicted_class.
        """
        predict_x = self.model.predict(X)
        if predict_x.ndim == 2 and predict_x.shape[1] == 1:
            return (predict_x > 0.5).astype('int32')
        predicted_class = np.argmax(predict_x,axis=1)
        return predicted_class
