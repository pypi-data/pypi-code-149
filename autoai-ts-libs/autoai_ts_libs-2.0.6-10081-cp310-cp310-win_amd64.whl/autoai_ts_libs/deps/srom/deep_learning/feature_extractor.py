# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: deep_autoencoder_feature_extraction
   :synopsis: Deep AE Feature Extraction - Wrapper for \
       Feature Extraction using Autoencoder Deep Networks.

.. moduleauthor:: SROM Team
"""

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from autoai_ts_libs.deps.srom.utils.file_utils import possibly_unsafe_join
from tensorflow.keras.callbacks import ModelCheckpoint
from autoai_ts_libs.deps.srom.utils.estimator_utils import BuildFnWrapper
from scikeras.wrappers import KerasRegressor
from autoai_ts_libs.deps.srom.deep_learning.auto_encoders.dnn import deep_autoencoder
from tensorflow import keras

# class to be build for geenral purpose anomaly detection based on Encode
# class to be build for geenral purpose anomaly detection based on Encode
class DNNFeatureExtractor(KerasRegressor):
    """[summary]

    Args:
        KerasRegressor ([type]): [description]
    """

    def __init__(
        self,
        input_dimension=None,
        encoding_dimension=None,
        output_dimension=None,
        loss="mean_squared_error",
        build_fn=None,
        **kwargs,
    ):
        """[summary]

        Args:
            input_dimension ([type], optional): [description]. Defaults to None.
            output_dimension ([type], optional): [description]. Defaults to None.
            build_fn ([type], optional): [description]. Defaults to None.
            optimizer (str, optional): [description]. Defaults to "adam".
            loss (str, optional): [description]. Defaults to "mean_squared_error".
            hidden_dimension (int, optional): [description]. Defaults to 10.
            activation (str, optional): [description]. Defaults to "relu".
            output_activation (str, optional): [description]. Defaults to "linear".
            kernel_initializer (str, optional): [description]. Defaults to "normal".
            dropout_rate (float, optional): [description]. Defaults to 0.2.
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 128.
        """
        # DO NOT REMOVE - Required when sklearn clones and pushes params old params
        if build_fn is None:
            build_fn = BuildFnWrapper(deep_autoencoder)

        super(DNNFeatureExtractor, self).__init__(
            build_fn=build_fn,
            input_dimension=input_dimension,
            output_dimension=output_dimension,
            encoding_dimension=encoding_dimension,
            loss=loss,
            **kwargs,
        )

    def fit(self, X, y, **kwargs):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]
        """

        # First step
        super(DNNFeatureExtractor, self).fit(X, y, **kwargs)

        ext_layers = None
        for item in self.model.layers:
            if "decoder_" in item.name:
                break
            else:
                ext_layers = item.output

        if ext_layers is not None:
            self.extractor = keras.Model(inputs=self.model.inputs, outputs=ext_layers)
        else:
            raise Exception("model is not AE based")

        print(self.extractor.summary())

        return self

    def predict(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.extractor.predict(X)


class DeepAutoEncoderFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    This class extracts features from data using an Autoencoder-based transform.

    Parameters:
        train_model (keras type model obj, required): Encoder-decoder model \
            used to train the transform.
        feature_extractor (keras type model obj, required): Encoder model used \
            to extract features.
        train_loss_function (string or function handle, optional): Loss function \
            used to train the encoder-decoder model can choose from the \
            Keras library, or pass handles to custom loss functions that are \
            of the form `loss_fn(y_true, y_pred)`.
        optimizer (string, optional): Optimizer used to fit the encoder-decoder model. \
            Any Keras optimizer is a valid choice.
    """

    def __init__(
        self,
        train_model=None,
        feature_extractor=None,
        train_loss_function="mse",
        optimizer="adam",
    ):
        """
        Parameters:
        train_model (keras type model obj, required): Encoder-decoder model used to \
                train the transform.
        feature_extractor (keras type model obj, required): Encoder model used to extract features.
        train_model_type (string, optional): Type of encoder-decoder model, choice of \
                'teacher-forcing' and 'repeat-vector'.
                new option: 'vi-rnn' will train Variational Inference RNN using PyTorch
        train_loss_function (string or function handle, optional): Loss function used to train the \
                encoder-decoder model can choose from the Keras library, or pass handles to custom \
                loss functions that are of the form `loss_fn(y_true, y_pred)`.
                'vi-rnn' works only with "mse" or "gaussian"
        optimizer (string, optional): Optimizer used to fit the encoder-decoder model. Any Keras \
                optimizer is a valid choice.
        """
        # related to algorithm
        self.train_model = train_model
        self.feature_extractor = feature_extractor
        self.train_loss_function = train_loss_function
        self.optimizer = optimizer

        # related to fit method
        self.checkpointer = None
        self.train_history = None

        # related to execution
        self.verbose = None
        self.val_frac = None
        self.epochs = None
        self.batch_size = None
        self.save_dir = None
        self.save_period = None
        self.load_file = None

    def set_params(self, **kwarg):
        """
        Set the parameters for the deep AE feature extractor.

        Parameters:
            batch_size (int, required): Batch size for training the \
                sequence-to-sequence models defaults to 100.
            epochs (int, required): Number of training epochs, defaults to 20.
            val_frac (float, required): Fraction of training data to set \
                aside for validation, defaults to 0.1.
            save_dir (string, required): Directory to save model weights \
                and checkpoints.
            save_period (int, required): Interval (in epochs) between checkpoints, \
                defaults to 10.
            load_file (string, required): File name from which to load feature \
                extractor weights.
        """
        if "verbose" in kwarg:
            self.verbose = kwarg["verbose"]
        if "val_frac" in kwarg:
            self.val_frac = kwarg["val_frac"]
        if "epochs" in kwarg:
            self.epochs = kwarg["epochs"]
        if "batch_size" in kwarg:
            self.batch_size = kwarg["batch_size"]
        if "save_dir" in kwarg:
            self.save_dir = kwarg["save_dir"]
        if "save_period" in kwarg:
            self.save_period = kwarg["save_period"]
        if "load_file" in kwarg:
            self.load_file = kwarg["load_file"]

    def _get_encoder_inputs(self, X):
        """
        To get encode inputs from User Data.

        Parameters:
            X (matrix or dataframe like object, required): Input to the \
                encoder-decoder model, N x D numpy array where N is \
                the number of samples in training set and \
                D is the number of features.
        """
        encoder_inputs = np.copy(X)
        return encoder_inputs

    def _get_targets(self, X, y=None):
        """
        Get the target from the user data.

        Parameters:
        X (matrix or dataframe like object, required):Input to the encoder-decoder model, \
            N x D numpy array where N isthe number of samples in training set and \
            D is the number of features.
        y (matrix or dataframe like object, optional):
            Optional argument to be provided when user wants to train the encoder-decoder \
            model against a target that is different from the inputs.numpy array with same N \
            as X, D needs to be the same size as the output of `train_model`.
        """
        if y is not None:
            target_data = np.copy(y)
        else:
            target_data = np.copy(X)
        return target_data

    def fit(self, X, y=None):
        """
        This method fits the `train_model` and save the weights to a local file.

        Parameters:
            X (matrix or dataframe like object, required):Input to the encoder-decoder model, \
                N x D numpy array where N is the number of samples in training set and \
                D is the number of features.
            y (matrix or dataframe like object, optional):Optional argument to be provided \
                when user wants to train the encoder-decoder model against a target that is \
                different from the inputs. numpy array with same N as X, D needs to be the \
                same size as the output of `train_model`.
        """
        if self.train_model is None:
            raise Exception("No train model provided")

        self.checkpointer = ModelCheckpoint(
            possibly_unsafe_join(
                self.save_dir, "train_weights.{epoch:02d}-{val_loss:.2f}.hdf5"
            ),
            monitor="val_loss",
            verbose=self.verbose,
            save_best_only=True,
            save_weights_only=True,
            mode="auto",
            period=self.save_period,
        )

        train_input_data = self._get_encoder_inputs(X)
        train_target_data = self._get_targets(X, y=y)

        self.train_model.compile(
            optimizer=self.optimizer, loss=self.train_loss_function
        )
        self.train_history = self.train_model.fit(
            train_input_data,
            train_target_data,
            validation_split=self.val_frac,
            batch_size=self.batch_size,
            epochs=self.epochs,
            callbacks=[self.checkpointer],
        )
        self.train_model.save_weights(
            possibly_unsafe_join(self.save_dir, "final_weights.hdf5")
        )
        return self

    def _transfer_extractor_weights(self):
        """
        Function to get the feature extractor weights from the saved model.
        """
        extractor_layer_names = [
            x.name for x in self.feature_extractor.layers if "encoder" in x.name
        ]
        for name in extractor_layer_names:
            self.feature_extractor.get_layer(name).set_weights(
                self.train_model.get_layer(name).get_weights()
            )

    def transform(self, X):
        """
        This method transforms input timeseries to features.

        Parameters:
            X (matrix or dataframe like object, required): Input to the encoder-decoder model, \
                N x D numpy array where N is the number of samples in training set and D is \
                the number of features.
        """
        if self.feature_extractor is None:
            raise Exception("No feature_extractor provided")

        if self.load_file is not None:
            self.feature_extractor.load_weights(self.load_file, by_name=True)
        else:
            if self.train_model is not None:
                self._transfer_extractor_weights()

        features = self.feature_extractor.predict(X)
        return features


class DeepSeqFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    This class extracts features from time series windows using a \
    RNN-based transform that was learned using a sequence-to-sequence model. \
    The sequence model is for use with the LSTM and other time-series models \
    that encode temporal sequences.

    Parameters:
        train_model (keras type model obj, required): Encoder-decoder model used to \
                train the transform.
        feature_extractor (keras type model obj, required): Encoder model used to extract features.
        train_model_type (string, optional): Type of encoder-decoder model, choice of \
                'teacher-forcing' and 'repeat-vector'.
                new option: 'vi-rnn' will train Variational Inference RNN using PyTorch
        train_loss_function (string or function handle, optional): Loss function used to train the \
                encoder-decoder model can choose from the Keras library, or pass handles to custom \
                loss functions that are of the form `loss_fn(y_true, y_pred)`.
                'vi-rnn' works only with "mse" or "gaussian"
        optimizer (string, optional): Optimizer used to fit the encoder-decoder model. Any Keras \
                optimizer is a valid choice.
    """

    def __init__(
        self,
        train_model=None,
        feature_extractor=None,
        train_model_type="teacher-forcing",
        train_loss_function="mse",
        optimizer="adam",
    ):

        # related to algorithm
        self.train_model = train_model
        self.feature_extractor = feature_extractor
        self.train_loss_function = train_loss_function
        self.optimizer = optimizer
        self.train_model_type = train_model_type

        # related to fit method
        self.checkpointer = None
        self.train_history = None

        # related to execution
        self.verbose = None
        self.val_frac = None
        self.epochs = None
        self.batch_size = None
        self.save_dir = None
        self.save_period = None
        self.load_file = None
        self.device = None
        self.lr_decay = None
        # self.mc_samples = None
        self.learning_rate = None
        self.epochs_vi = None

    def set_params(self, **kwarg):
        """
        Set the parameters for the deep AE feature extractor.

        Parameters:
            batch_size (int, required): Batch size for training the sequence-to-sequence models \
                    defaults to 100.
            epochs (int, required): Number of training epochs, defaults to 20.
            val_frac (float, required): Fraction of training data to set aside for validation, \
                    defaults to 0.1.
            save_dir (string, required): Directory to save model weights and checkpoints.
            save_period (int, required): Interval (in epochs) between checkpoints, defaults to 10.
            load_file (string, required): File name from which to load feature extractor weights.
            device (string, optional): device to run -  "cpu", "cuda:0", "cuda:1", ... (pytorch argument)
            lr_decay (bool, optional): use learning rate decay or not, (pytorch argument)
            mc_samples (int, optional): number of Monte Carlo samples for VI-RNN
            epochs_vi (int, optional): number of epochs for variational inference model
        """
        if "verbose" in kwarg:
            self.verbose = kwarg["verbose"]
        if "val_frac" in kwarg:
            self.val_frac = kwarg["val_frac"]
        if "epochs" in kwarg:
            self.epochs = kwarg["epochs"]
        if "batch_size" in kwarg:
            self.batch_size = kwarg["batch_size"]
        if "save_dir" in kwarg:
            self.save_dir = kwarg["save_dir"]
        if "save_period" in kwarg:
            self.save_period = kwarg["save_period"]
        if "load_file" in kwarg:
            self.load_file = kwarg["load_file"]

        self.device = "cpu"
        if "device" in kwarg:
            self.device = kwarg["devivce"]

        if "lr_decay" in kwarg:
            self.lr_decay = kwarg["lr_decay"]

        if "mc_samples" in kwarg:
            self.mc_samples = kwarg["mc_samples"]

        if "learning_rate" in kwarg:
            self.learning_rate = kwarg["learning_rate"]

        if "epochs_vi" in kwarg:
            self.epochs_vi = kwarg["epochs_vi"]

    def _get_encoder_inputs(self, X):
        """
        To get encoder inputs from User Data.

        Parameters:
            X (matrix or dataframe like object, required): Input to the encoder-decoder model, \
                    N x T x D numpy array where N is the number of samples in training set, \
                    T is the number of timesteps in the time series and \
                    D is the number of features in the time series.
        """
        encoder_inputs = np.copy(X)
        return encoder_inputs

    def _get_decoder_inputs(self, X):
        """
        To get decoder inputs from User Data.

        Parameters:
            X (matrix or dataframe like object, required): Input to the encoder-decoder model, \
                    N x T x D numpy array where N is the number of samples in training set, \
                    T is the number of timesteps in the time series and \
                    D is the number of features in the time series.
        """
        decoder_inputs = np.zeros_like(X)
        decoder_inputs[:, 1:, :] = np.copy(
            X[:, :-1, :]
        )  # pylint: disable=unsupported-assignment-operation
        return decoder_inputs

    def _get_targets(self, X, y=None):
        """
        Get the target from the user data.

        Parameters:
            X (matrix or dataframe like object, required): Input to the encoder-decoder model, \
                    N x T x D numpy array where N is the number of samples in training set, \
                    T is the number of timesteps in the time series and \
                    D is the number of features in the time series.
            y (matrix or dataframe like object, optional): Optional argument to be provided when \
                    user wants to train the encoder-decoder model against a target that is different \
                    from the inputs. \
                    numpy array with same N and T as X, D needs to be of the same size as the output of \
                    `train_model`.
        """
        if y is not None:
            target_data = np.copy(y)
        else:
            target_data = np.copy(X)
        return target_data

    def fit(self, X, y=None):
        """
        This method fits the `train_model` and saves the weights to a local file.

        Parameters:
            X (matrix or dataframe like object, required): Input to the encoder-decoder model, \
                    N x T x D numpy array where N is the number of samples in training set, \
                    T is the number of timesteps in the time series and \
                    D is the number of features in the time series.
            y (matrix or dataframe like object, optional):Optional argument to be provided \
                    when user wants to train the encoder-decoder model against a target \
                    that is different from the inputs. \
                    numpy array with same N and T as X, D needs to be the same size as the output of \
                    `train_model`.
        """
        if self.train_model is None:
            raise Exception("No train model provided")

        if self.train_model_type == "vi-rnn":
            self.checkpointer = self.train_model.ModelCheckpoint(
                possibly_unsafe_join(self.save_dir, "train_weights.{:03d}-{:.2e}.pth"),
                period=self.save_period,
            )
        else:
            self.checkpointer = ModelCheckpoint(
                possibly_unsafe_join(
                    self.save_dir, "train_weights.{epoch:02d}-{val_loss:.2f}.hdf5"
                ),
                monitor="val_loss",
                verbose=self.verbose,
                save_best_only=True,
                save_weights_only=True,
                mode="auto",
                period=self.save_period,
            )

        train_encoder_inputs = self._get_encoder_inputs(X)
        train_target_data = self._get_targets(X, y=y)

        if self.train_model_type == "teacher-forcing":
            train_decoder_inputs = self._get_decoder_inputs(X)
            train_input_data = [train_encoder_inputs, train_decoder_inputs]
        elif self.train_model_type == "vi-rnn":
            train_input_data = train_encoder_inputs
            train_target_data = None
        else:
            train_input_data = train_encoder_inputs

        if self.train_model_type == "vi-rnn":
            compile_arg = {}
            if hasattr(self, "learning_rate"):
                compile_arg["learning_rate"] = self.learning_rate

            if hasattr(self, "mc_samples"):
                compile_arg["mc_samples"] = self.mc_samples

            if hasattr(self, "lr_decay"):
                compile_arg["lr_decay"] = self.lr_decay

            self.train_model.compile(
                optimizer=self.optimizer, loss=self.train_loss_function, **compile_arg
            )
        else:
            self.train_model.compile(
                optimizer=self.optimizer, loss=self.train_loss_function
            )

        self.train_history = self.train_model.fit(
            train_input_data,
            train_target_data,
            validation_split=self.val_frac,
            batch_size=self.batch_size,
            epochs=self.epochs,
            callbacks=[self.checkpointer],
        )

        if self.train_model_type == "vi-rnn":
            self.train_model.save_weights(
                possibly_unsafe_join(self.save_dir, "final_weights.pth")
            )
        else:
            self.train_model.save_weights(
                possibly_unsafe_join(self.save_dir, "final_weights.hdf5")
            )
        return self

    def _transfer_extractor_weights(self):
        """
        Function to get the feature extractor weights from the saved model.
        """
        if self.train_model_type == "vi-rnn":
            # do nothing
            # in pytorch, the networks in feature_extractor are replicas of those in train_model
            pass
        else:
            extractor_layer_names = [
                x.name for x in self.feature_extractor.layers if "encoder" in x.name
            ]
            for name in extractor_layer_names:
                self.feature_extractor.get_layer(name).set_weights(
                    self.train_model.get_layer(name).get_weights()
                )

    def transform(self, X):
        """
        This method transforms input timeseries to features.

        Parameters:
            X (matrix or dataframe like object, required): Input timeseries to transform, \
                    N x T x D numpy array where N is the number of samples to transform, \
                    T is the number of timesteps in the time series and \
                    D is the number of features in the time series.
        """
        if self.feature_extractor is None:
            raise Exception("No feature_extractor provided")

        if self.load_file is not None:
            self.feature_extractor.load_weights(self.load_file, by_name=True)
        else:
            if self.train_model is not None:
                self._transfer_extractor_weights()

        features = self.feature_extractor.predict(X)
        return features
