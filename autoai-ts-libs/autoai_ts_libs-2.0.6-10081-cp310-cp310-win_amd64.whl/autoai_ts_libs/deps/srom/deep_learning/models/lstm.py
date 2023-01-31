from tensorflow.keras import optimizers
from tensorflow.keras.layers import (
    LSTM,
    Activation,
    BatchNormalization,
    Dense,
    Dropout,
    Input,
    RepeatVector,
    TimeDistributed,
    concatenate,
    Activation,
    dot,
    Bidirectional,
)
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Flatten as TSFlatten


def simple_lstm(
    input_dimension,
    output_dimension,
    optimizer="rmsprop",
    loss="mean_squared_error",
    hidden_dimension=10,
    activation="sigmoid",
    kernel_initializer="normal",
    dropout_rate=0.2,
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        optimizer (str, optional): [description]. Defaults to "rmsprop".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        hidden_dimension (int, optional): [description]. Defaults to 10.
        activation (str, optional): [description]. Defaults to "sigmoid".
        kernel_initializer (str, optional): [description]. Defaults to "normal".
        dropout_rate (float, optional): [description]. Defaults to 0.2.

    Returns:
        [type]: [description]
    """
    model = Sequential()
    model.add(
        LSTM(
            hidden_dimension,
            input_shape=input_dimension,
            kernel_initializer=kernel_initializer,
        )
    )
    model.add(Dropout(dropout_rate))
    model.add(Dense(output_dimension, activation=activation))
    model.compile(loss=loss, optimizer=optimizer)
    return model


def deep_lstm(
    input_dimension,
    output_dimension,
    optimizer="rmsprop",
    loss="mean_squared_error",
    hidden_dimension=(10, 20, 10),
    activation="sigmoid",
    kernel_initializer="normal",
    dropout_rate=0.20,
):
    """[summary]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        optimizer (str, optional): [description]. Defaults to "rmsprop".
        loss (str, optional): [description]. Defaults to "mean_squared_error".
        hidden_dimension (tuple, optional): [description]. Defaults to (10, 20, 10).
        activation (str, optional): [description]. Defaults to "sigmoid".
        kernel_initializer (str, optional): [description]. Defaults to "normal".
        dropout_rate (float, optional): [description]. Defaults to 0.20.

    Returns:
        [type]: [description]
    """
    model = Sequential()
    for layer_num, hidden_dimension_ in enumerate(hidden_dimension):
        if layer_num == 0:
            model.add(
                LSTM(
                    hidden_dimension_,
                    input_shape=input_dimension,
                    return_sequences=True,
                    kernel_initializer=kernel_initializer,
                )
            )
        elif layer_num < len(hidden_dimension) - 1:
            model.add(
                LSTM(
                    hidden_dimension_,
                    return_sequences=True,
                    kernel_initializer=kernel_initializer,
                )
            )
        else:
            model.add(
                LSTM(
                    hidden_dimension_,
                    return_sequences=False,
                    kernel_initializer=kernel_initializer,
                )
            )
        model.add(Dropout(dropout_rate))
    model.add(Dense(output_dimension, activation=activation))
    model.compile(loss=loss, optimizer=optimizer)

    return model


def fixed_lstm(input_dimension, output_dimension, output_type="flatten"):
    """This is a light weight LSTM - two layered model

    Args:
        input_dimension ([tuple]): [input dimensionality]
        output_dimension ([integer]): [output dimentionality]
        output_type (str, optional): [the indicator of output_type]. Defaults to "flatten".

    Returns:
        [Keras Model]: [It return a keras model]
    """
    model = Sequential()
    model.add(
        LSTM(128, return_sequences=True, input_shape=input_dimension, name="lstm_1")
    )
    model.add(LSTM(32, name="lstm_2"))
    model.add(Dense(output_dimension))
    model.compile(
        loss="mean_squared_error",
        optimizer=optimizers.Adam(lr=0.01),
        metrics=["mean_absolute_error"],
    )
    return model


def fixed_seq2seq(
    input_dimension,
    output_dimension,
    n_hidden=128,
    output_type="structured",
):
    """Seq to Seq model with Strucutred Output

    Args:
        input_dimension ([tuple]): [input dimensionality of the model]
        output_dimension ([tuple]): [output dimentionality of the model]
        n_hidden (int, optional): [description]. Defaults to 128.
        output_type (str, optional): [description]. Defaults to "structured".

    Returns:
        [type]: [description]
    """
    input_train = Input(shape=input_dimension)
    encoder_last_h1, _, encoder_last_c = LSTM(
        n_hidden,
        activation="elu",
        dropout=0.2,
        recurrent_dropout=0.2,
        return_sequences=False,
        return_state=True,
    )(input_train)
    encoder_last_h1 = BatchNormalization(momentum=0.6)(encoder_last_h1)
    encoder_last_c = BatchNormalization(momentum=0.6)(encoder_last_c)
    decoder = RepeatVector(output_dimension[0])(encoder_last_h1)
    decoder = LSTM(
        n_hidden,
        activation="elu",
        dropout=0.2,
        recurrent_dropout=0.2,
        return_state=False,
        return_sequences=True,
    )(decoder, initial_state=[encoder_last_h1, encoder_last_c])
    out = TimeDistributed(Dense(output_dimension[1]))(decoder)
    model = Model(inputs=input_train, outputs=out)
    model.compile(
        loss="mean_squared_error",
        optimizer=optimizers.Adam(lr=0.01, clipnorm=1),
        metrics=["mean_absolute_error"],
    )
    return model


def fixed_seq2seq_attention(
    input_dimension,
    output_dimension,
    n_hidden=128,
    output_type="structured",
):
    """[summary]

    Args:
        input_dimension ([tuple]): [input dimensionality of the model]
        output_dimension ([tuple]): [output dimentionality of the model]
        n_hidden (int, optional): [description]. Defaults to 128.
        output_type (str, optional): [description]. Defaults to "structured".

    Returns:
        [type]: [description]
    """
    input_train = Input(shape=input_dimension)
    encoder_stack_h, encoder_last_h, encoder_last_c = LSTM(
        n_hidden,
        activation="elu",
        dropout=0.2,
        recurrent_dropout=0.2,
        return_sequences=True,
        return_state=True,
    )(input_train)
    encoder_last_h = BatchNormalization(momentum=0.6)(encoder_last_h)
    encoder_last_c = BatchNormalization(momentum=0.6)(encoder_last_c)
    decoder_input = RepeatVector(output_dimension[0])(encoder_last_h)
    decoder_stack_h = LSTM(
        n_hidden,
        activation="elu",
        dropout=0.2,
        recurrent_dropout=0.2,
        return_state=False,
        return_sequences=True,
    )(decoder_input, initial_state=[encoder_last_h, encoder_last_c])
    attention = dot([decoder_stack_h, encoder_stack_h], axes=[2, 2])
    attention = Activation("softmax")(attention)
    context = dot([attention, encoder_stack_h], axes=[2, 1])
    context = BatchNormalization(momentum=0.6)(context)
    decoder_combined_context = concatenate([context, decoder_stack_h])
    out = TimeDistributed(Dense(output_dimension[1]))(decoder_combined_context)
    model = Model(inputs=input_train, outputs=out)
    model.compile(
        loss="mean_squared_error",
        optimizer=optimizers.Adam(lr=0.01, clipnorm=1),
        metrics=["mean_absolute_error"],
    )
    return model


def fixed_bidirectional_lstm(
    input_dimension, output_dimension, n_hidden=100, output_type="flatten"
):
    """[Bidirectional LSTM]

    Args:
        input_dimension ([type]): [description]
        output_dimension ([type]): [description]
        n_hidden (int, optional): [description]. Defaults to 100.

    Returns:
        [type]: [description]
    """

    model = Sequential()
    model.add(
        Bidirectional(
            LSTM(
                n_hidden,
                return_sequences=True,
                input_shape=input_dimension,
            )
        )
    )
    model.add(
        TimeDistributed(
            Dense(128, activation="relu"),
            input_shape=(None, input_dimension[0], input_dimension[1]),
        )
    )
    model.add(TSFlatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(output_dimension, activation="relu"))
    model.compile(optimizer="adam", loss=["mape"], metrics=["mse", "mape"])
    return model
