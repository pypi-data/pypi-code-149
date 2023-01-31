# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


""" Module implementing the univariate DE RNN model

"""
import numpy as np
import tensorflow as tf


class UnivariateDERNN(object):
    """
    Class for building the tensorflow graph for the univariate density
    estimation time series predictor

    Args:
    control_size (int, required): number of exogenous control variables
    bins (numpy array, required): bins for the discretized distribution
    rnn_state_size (int, optional): size of rnn internal state, default 128
    rnn_layers (int, optional): number of layers in rnn (not fully
        implemented), default 1
    lr (float, optional): learning rate to use during training,
        default=0.1
    predict_num_samples (int, optional): number of parallel time series to
        generate during multistep prediction
    reg_lambda (float, optional): regularization parameter for estimated
        distribution smoothness, default 0.1
    """

    def __init__(
        self,
        bins=None,
        control_size=0,
        rnn_state_size=128,
        rnn_layers=1,
        lr=0.1,
        predict_num_samples=20 * 10 ** 3,
        reg_lambda=0.1,
    ):
        """ Initialize the model for the univariate density estimation RNN
        """

        self.control_size = control_size

        self.rnn_state_size = rnn_state_size
        self.rnn_layers = rnn_layers
        self.predict_num_samples = predict_num_samples

        self.bins = bins
        self.d_size = bins.shape[0] - 1

        # self.max_time = max_time

        # fit params
        self.reg_lambda = reg_lambda
        self.lr = lr

    @staticmethod
    def _sample_output_distribution(x, y, bin_defs):
        """
        Sample the output distribution based on the inverse CDF method

        Args:
        x: tensor of probabilities (dim: [batch_size,
            discrete distribution categories])
        y: tensor of random samples from uniform distribution
            (dim: [batch_size, 1])
        bin_defs: tensor of boundaries for bins which discretize the
                    distribution, (dim: [discrete distribution categories])
                    should return [batch_size] vector of samples

        Returns: tensor of sampled values from distribution

        """
        with tf.compat.v1.variable_scope("distribution-scaler"):
            bin_diffs = bin_defs[1:] - bin_defs[:-1]
            # cumulative sum of probabilities: [0, p0, p1+p0, ...]
            prob_bins = tf.cumsum(x, axis=1, exclusive=True)
            # y_ = tf.expand_dims(y, 1)
            idx = tf.reduce_sum(tf.cast(y >= prob_bins, tf.int32), axis=1) - 1
            # tf.range(x.shape[1])
            idx_2 = tf.stack([tf.range(y.shape[0]), idx], axis=1)
            # idx_h = tf.stack([tf.range(y.shape[0]), idx],axis=1)
            cum_prob_bin = tf.expand_dims(tf.gather_nd(prob_bins, idx_2), 1)
            prob_bin = tf.expand_dims(tf.gather_nd(x, idx_2), 1)
            diff_bin = tf.expand_dims(tf.gather(bin_diffs, idx), 1)  # check
            bin_offset = tf.expand_dims(tf.gather(bin_defs, idx), 1)  # check
            """
            print(idx.eval())
            print(prob_bin.eval())
            print(diff_bin.eval())
            print(bin_offset.eval())
            print(cum_prob_bin.eval())
            """
            return (y - cum_prob_bin) / prob_bin * diff_bin + bin_offset

    @staticmethod
    def custom_lstm(
        cell,
        input_encoder_op,
        output_decoder_op,
        inputs_ta,
        max_time,
        batch_size,
        state_size,
    ):
        """
        Custom LSTM model which wraps the standard LSTM with additional
        layers as per the DE-LSTM design.

        Since we want to feed LSTM output to subsequent inputs, we need raw_rnn
        and we need to define loop_fn.

        inputs at time t are underlying process inputs: x_t, and previous LSTM
        output h_{tâˆ’1}
        assume we are working with batches, x_t has dimension [batch_size,
            input_size]
        h_{t-1}: [batch_size, output_size = state_size]

        Args:
            cell (instantiated RNN cell, required): the fundamental LSTM cell
                used by the prediction method
            input_encoder_op (type, required): a tensorflow operation to apply
                to the inputs to the RNN
            output_decoder_op (type, required): a tensorflow operation to apply
                to the output of the RNN
            inputs_ta (tensor array, required): tensorflow tensor array 
                containing input tensors
            max_time (int, required): length of input time series
            batch_size (int, required): size of input batches
            state_size (int, required): size of LSTM state

        Returns:
            mapped_outputs_logit (tensor): Outputs of the prediction process after
                converting to logits
            mapped_outputs (tensor): Outputs of the prediction process
            final_state (tensor): Final internal state of the LSTM
        """

        def loop_fn(time_, cell_output, cell_state, loop_state):
            """
            Required tensorflow loop_fn to implement a custom LSTM.

            https://www.tensorflow.org/versions/r1.0/api_docs/python/tf/nn/raw_rnn

            Args:
                time_ (Tensor, required): Time index
                cell_output (Tensor/tuple of Tensor, required): Output of the RNN cell
                cell_state (Tensor/tuple of Tensor, required): State of RNN cell
                loop_state (Tensor/tuple of Tensor, required): Additional loop state

            Returns:
                elements_finished (TensorArray): TensorArray of 
                next_input (Tensor): Next input to feed to the LSTM
                next_cell_state (Tensor): Next state to feed to the LSTM
                emit_output (Tensor): Additional output to be emitted
                next_loop_state (Tensor): Next loop state
            """
            emit_output = cell_output  # == None for time_ == 0

            if cell_output is None:  # time_ == 0
                # next_cell_state = cell.zero_state(batch_size, tf.float32)
                next_cell_state = cell.get_initial_state(
                    batch_size=batch_size, dtype=tf.float32
                )
                prev_output = tf.zeros([batch_size, state_size])
            else:
                next_cell_state = cell_state
                prev_output = cell_output

            elements_finished = time_ >= max_time
            finished = tf.reduce_all(elements_finished)
            next_input = tf.cond(
                finished,
                lambda: tf.zeros([batch_size, state_size], dtype=tf.float32),
                lambda: input_encoder_op(inputs_ta.read(time_), prev_output),
            )
            next_loop_state = None

            return (
                elements_finished,
                next_input,
                next_cell_state,
                emit_output,
                next_loop_state,
            )

        outputs_ta, final_state, _ = tf.compat.v1.nn.raw_rnn(cell, loop_fn)
        # outputs ta was created with first dimension equal to time
        # thus we need to transpose it so that batch is first dim
        outputs = tf.transpose(outputs_ta.stack(), perm=[1, 0, 2])
        mapped_outputs_logit = tf.map_fn(output_decoder_op, outputs)
        mapped_outputs = tf.nn.softmax(mapped_outputs_logit)

        return mapped_outputs_logit, mapped_outputs, final_state

    def _init_multistep(self, pred_inputs):
        """
        Initialization for the multistep prediction:
         - instantiate tensor array for outputs
         - create the initial state for the LSTM

        For the multistep prediction, we must first prime the trained LSTM
        with known inputs. Then we replicate that state across all the parallel
        realizations that were are generating via monte carlo.

         Args:
            pred_inputs (Tensor, required): Initial inputs to the multistep
                prediction, dimensions are [batch size, time, covariates==1].

        Return:
            init_input (Tensor): initial input to use when running multistep
                LSTM
            pred_init_lstm_state (Tensorflow state tuple): Represents the
                initial state for the multistep prediction
            init_lstm_output (Tensor): initial output of the LSTM
        """
        with tf.compat.v1.variable_scope("multi-step-prediction-init"):
            Ns = self.predict_num_samples
            # get the right state in cell
            # for the internal LSTM take output and final state from the
            # final state of the priming period
            # replicate initial state
            # FIX: need to do this to allow for multiple LSTM layers
            pred_init_lstm_state = (
                tf.compat.v1.nn.rnn_cell.LSTMStateTuple(
                    tf.tile(self.final_state[-1].c, [Ns, 1]),
                    tf.tile(self.final_state[-1].h, [Ns, 1]),
                ),
            )
            init_lstm_output = tf.tile(self.final_state[-1].h, [Ns, 1])
            # replicate prior input
            # initial input is the last input during the priming
            # init_input = tf.tile(pred_inputs[:, -1, :], [Ns, 1])
            # now, this is univariate so retain only the single dimension of input
            init_input = tf.tile(pred_inputs[:, -1, :1], [Ns, 1])
        return init_input, pred_init_lstm_state, init_lstm_output

    def _multistep_prediction_step(
        self,
        y,
        lstm_output,
        state,
        prediction_control_inputs,
        number_samples,
        bin_defs,
    ):
        """
        Perform one step of the multistep prediction, this serves as the
        main code for the tf_while loop

        Args:
            y (type, required): description
            lstm_output (type, required): description
            state (type, required): description
            prediction_control_inputs (type, required): description
            distribution (type, required): description
            number_samples (type, required): description
            bin_defs (type, required): description

        Returns:
            pred_output_samples (Tensor): Output samples of the stochastic LSTM
                for this step
            lstm_output (Tensor): Underlying lstm output representing the 
                distribution at this step
            state_new (Tensor): Updated state of the LSTM
        """
        input_incoming = tf.concat([y, prediction_control_inputs], axis=1)
        cur_input = self.input_encoder_op(input_incoming, lstm_output)
        lstm_output, state_new = self.cell(cur_input, state)

        output = tf.nn.softmax(self.output_decoder_op(lstm_output))
        pred_output_samples = (
            self._sample_output_distribution(
                output, tf.random.uniform((number_samples, 1)), bin_defs
            )
            + y
        )

        # predicted output only contains the predicted variable for each of the
        # monte-carlo runs
        # pred_output_samples dim: [Ns,1]
        return pred_output_samples, lstm_output, state_new

    def build_multistep_prediction(self, prediction_control_inputs, bin_defs):
        """
        Build graph to compute predict_ns parallel multistep
        predictions for the model. Output at each time step is based on
        sampling from the discretized distribution. Sampling is performed using
        the inverse cdf method using the sampling function defined above
        (_sample_output_distribution).

        Args:
            prediction_control_inputs (tensor placeholder, required): placeholder
            bin_defs (tensor placeholder, required): placeholder for definition of discretized
                bins for the probability distribution
        """
        with tf.compat.v1.variable_scope("multi-step-prediction"):
            Ns = self.predict_num_samples  # number of parallel samples
            num_steps = tf.shape(prediction_control_inputs)[1]  # *** [0]
            rnn_state_size = self.rnn_state_size

            pred_inputs = self.x  # use self.x since it is wired to the LSTM
            # self.outputs, self.final_state will be the output after "priming"
            # create storage for outputs of multistep prediction
            pred_outputs = tf.TensorArray(
                dtype=tf.float32,
                size=num_steps,
                name="multistep-prediction-outputs-tensor-array",
            )
            prediction_control_inputs_ta = tf.TensorArray(
                dtype=tf.float32,
                size=num_steps,
                name="multistep-prediction-controls-tensor-array",
            )
            prediction_control_inputs_ta = prediction_control_inputs_ta.unstack(
                tf.transpose(prediction_control_inputs, perm=[1, 0, 2])
            )  # *** remove transpose
            # self.pred_outputs = pred_outputs

            init_input, init_lstm_state, init_lstm_output = self._init_multistep(
                pred_inputs
            )

            # with tf.compat.v1.variable_scope("distribution-driver"):
            #    # set up random sampling, to be used later
            #    uniform_distribution = tfp.distributions.Uniform()  # [0,1)

            def condition(i, *args):
                return i < num_steps

            # OLD
            # def body(i, prior_input, lstm_output, state, the_prediction):
            #    input_incoming, lstm_output, state_new, pred_output_samples =
            #        self._multistep_prediction_step(prior_input, lstm_output,
            #        state,  \
            #        tf.tile(tf.expand_dims(
            #           prediction_control_inputs_ta.read(i),0),
            #           [Ns,1]), \
            #        uniform_distribution, Ns, bin_defs)
            #    return i+1, input_incoming, lstm_output, state_new,
            #       the_prediction.write(i, pred_output_samples)

            def body(i, cur_input, lstm_output, state, the_prediction):
                """
                Body for a tf while loop. See:
                https://www.tensorflow.org/api_docs/python/tf/while_loop

                This essentially wraps the call to _multistep_prediction_step

                Args:
                    i (integer): step index
                    cur_input (Tensor): tensor for current input
                    lstm_output (Tensor): output from LSTM
                    state (Tensor): state of LSTM
                    the_prediction (TensorArray): the prediction from the LSTM

                Returns:
                    i+1 (integer): incremented step index
                    cur_input_new (Tensor): new input to the next step
                    lstm_output (Tensor): output from LSTM
                    state_new (Tensor): updated state from LSTM
                    the_prediction.write(i, cur_input_new) (TensorArray): updated
                        prediction, this essentially writes the prediction output to 
                        index i in the TensorArray, and returns the updated array

                """
                cur_input_new, lstm_output, state_new = self._multistep_prediction_step(
                    cur_input,
                    lstm_output,
                    state,
                    tf.tile(prediction_control_inputs_ta.read(i), [Ns, 1]),
                    Ns,
                    bin_defs,
                )
                return (
                    i + 1,
                    cur_input_new,
                    lstm_output,
                    state_new,
                    the_prediction.write(i, cur_input_new),
                )

            # get samples and formulate next input
            output = tf.nn.softmax(self.output_decoder_op(init_lstm_output))
            primed_input = (
                self._sample_output_distribution(
                    output, tf.random.uniform((Ns, 1)), bin_defs
                )
                + init_input
            )
            # tf.expand_dims(init_input[:, 0], 1)
            # *** tf.expand_dims(init_input[:, 0], 1)
            # write first input to output array
            pred_outputs = pred_outputs.write(0, primed_input)
            init_state = (
                1,
                primed_input,
                init_lstm_output,
                init_lstm_state,
                pred_outputs,
            )
            n, pred_output_samples, lstm_output, state, pred_outputs = tf.while_loop(
                condition, body, init_state, parallel_iterations=1, back_prop=False
            )
            self.outputs_multistep_raw = pred_outputs.stack(
                name="multistep-prediction-outputs-raw"
            )
            self.outputs_multistep_mean, self.outputs_multistep_var = tf.nn.moments(
                self.outputs_multistep_raw,
                axes=[1],
                name="multistep-prediction-outputs-moments",
            )

    def build(
        self, inputs, control_inputs, prediction_control_inputs, labels, bin_defs
    ):
        """
        Build the graph for the univariate de rnn. Sets up the necessary
        placeholders and calls underlying graph building functions.

        For the univariate case inputs should be of the form:
        - inputs: y_1,
        - controls: u_1, u_2, ..., u_m
        - outputs: o_1

        dimensions of inputs are: batch size, time length, covariates

        all inputs should be tensors of the proper type.
        """

        d_size = self.d_size  # number of bins in discretized output

        # inputs should be [batches, time steps, covariates]
        # make length and batch size dynamic we need this for rolling
        # multistep prediction
        max_time = tf.shape(inputs)[1]
        batch_size = tf.shape(inputs)[0]
        m = self.control_size

        # print(prediction_control_inputs.shape)
        # print("inputs: ")
        # print(inputs.shape)
        # print("controls: ")
        # print(control_inputs.shape)

        reg_lambda = self.reg_lambda
        # begin build model
        lr = self.lr
        rnn_state_size = self.rnn_state_size
        rnn_layers = self.rnn_layers

        # print('max_time: {}'.format(max_time))
        # tf.print("max_time:", max_time, output_stream=tf.logging.info)
        # print('batch_size: {}'.format(batch_size))
        # tf.print("batch_size:", batch_size, output_stream=tf.logging.info)
        # x, the concatenation of inputs and controls is what gets fed to the
        #   LSTM, if control_inputs is a 0-dim tensor, concat adds nothing
        x = tf.concat([inputs, control_inputs], axis=2)
        self.x = x

        inputs_ta = tf.TensorArray(dtype=tf.float32, size=max_time, name="x-ta")
        # unstack along time, tensor array can only be filled with first
        # dimension, to make that the time dimension, we transpose first
        inputs_ta = inputs_ta.unstack(tf.transpose(x, perm=[1, 0, 2]))

        with tf.compat.v1.variable_scope("input-network"):
            # Define networks for input encoder
            input_layer_2 = tf.compat.v1.layers.Dense(
                rnn_state_size, activation=None, name="input-linear-2"
            )
            input_layer_1 = tf.compat.v1.layers.Dense(
                rnn_state_size, activation=tf.nn.tanh, name="input-tanh-linear-1"
            )
            input_layer_3 = tf.compat.v1.layers.Dense(
                rnn_state_size, activation=None, name="input-linear-3"
            )

            self.input_encoder_op = lambda cur_input, prev_lstm_output: input_layer_2(
                input_layer_1(cur_input)
            ) + input_layer_3(prev_lstm_output)

        with tf.compat.v1.variable_scope("output-network"):
            # Define network for output decoder
            output_layer_1 = tf.compat.v1.layers.Dense(
                rnn_state_size, activation=tf.nn.tanh, name="output-tanh-linear"
            )
            output_layer_2 = tf.compat.v1.layers.Dense(
                d_size, activation=None, name="output-linear"
            )
            output_layer_sp = tf.compat.v1.layers.Dense(
                d_size, activation=tf.nn.softplus, name="output-softplus"
            )
            # output_decoder_op = lambda cur_output: tf.layers.dense(
            #    tf.layers.dense(cur_output, rnn_state_size,
            #                    activation=tf.nn.tanh,
            #                    name="output-tanh-linear"),
            #                    d_size, activation=None,
            #                    name="output-linear")
            self.output_decoder_op = lambda cur_output: output_layer_2(
                output_layer_1(output_layer_sp(cur_output))
            )

        # need to migrate to tf.keras.layers.StackedRNNCells
        # tf.keras.layers.LSTMCell
        with tf.compat.v1.variable_scope("internal-lstm"):
            self.cell = tf.compat.v1.nn.rnn_cell.MultiRNNCell(
                [
                    tf.compat.v1.nn.rnn_cell.LSTMCell(rnn_state_size)
                    for _ in range(rnn_layers)
                ]
            )  # tf.expand_dims(x, -1)
            self.outputs_logit, self.outputs, self.final_state = self.custom_lstm(
                self.cell,
                self.input_encoder_op,
                self.output_decoder_op,
                inputs_ta,
                max_time,
                batch_size,
                rnn_state_size,
            )

        # Compute 1-step prediction mean and variance
        with tf.compat.v1.variable_scope("one-step-prediction"):
            alpha_half = tf.expand_dims(0.5 * (bin_defs[:-1] + bin_defs[1:]), 1)

            self.outputs_distribution = tf.identity(self.outputs)  # outputs_tmp
            outputs_shape = tf.gather(tf.shape(self.outputs), [0, 1])
            outputs_tmp = tf.reshape(self.outputs, [-1, d_size])

            outputs_mean = tf.matmul(outputs_tmp, alpha_half)
            target_shape = [outputs_shape[0], outputs_shape[1], 1]
            self.outputs_1step_mean = tf.identity(
                tf.reshape(outputs_mean, target_shape)
                + tf.reshape(inputs, target_shape),
                name="one-step-mean",
            )

            outputs_var = tf.matmul(outputs_tmp, tf.square(alpha_half)) - tf.square(
                outputs_mean
            )
            self.outputs_1step_var = tf.reshape(
                outputs_var, target_shape, name="one-step-var"
            )

        ### 1
        if labels is not None:
            # target outputs
            # outputs_ = tf.cast(tf.transpose(labels[:, :, 0]), tf.int64)
            outputs_ = tf.cast(labels[:, :, 0], tf.int64)
            # print("labels: ")
            # print(outputs_.shape)

            # define loss and train op for training
            with tf.compat.v1.variable_scope("training_and_loss"):
                # training function and loss calculation
                # create matrix for regularization
                k = d_size
                L = np.zeros((k - 2, k), np.float32)
                L[: k - 2, : k - 2] = np.eye(k - 2)
                L[: k - 2, 1 : k - 1] += -2 * np.eye(k - 2)
                L[: k - 2, 2:k] += np.eye(k - 2)

                def weighted_inner_product(x, L):
                    """ compute (Lx)^T (Lx)
                        x is a vector k x 1
                        L is a matrix k-2 x k
                    """
                    tmp = tf.matmul(L, tf.expand_dims(x, axis=1))
                    return tf.matmul(tmp, tmp, transpose_a=True)

                L = tf.constant(L, name="regularization_constraint_matrix")

                # outputs_tmp = tf.reshape(self.outputs, [-1, k])

                def reg_op(x):
                    return weighted_inner_product(x, L)

                reg_tmp = tf.map_fn(reg_op, outputs_tmp)
                reg = (1.0 / tf.cast(batch_size, tf.float32)) * tf.reduce_sum(reg_tmp)

                self.loss = (1.0 / tf.cast(batch_size, tf.float32)) * tf.reduce_sum(
                    tf.nn.sparse_softmax_cross_entropy_with_logits(
                        labels=outputs_, logits=self.outputs_logit
                    )
                ) + reg_lambda * reg

                self.train_op = tf.compat.v1.train.AdamOptimizer(lr).minimize(self.loss)

            # define accuracy for train and eval
            self.accuracy = tf.reduce_mean(
                tf.cast(tf.equal(tf.argmax(self.outputs, 2), outputs_), tf.float32)
            )

            ### 2

    def model_fn(self, features, labels, mode=None, params=None, config=None):
        """
        Defines the model_fn for use with tf.estimator, using build above. The
        separation is necessary because build will be used in the multivariate
        case, and we don't need the extra steps required for tf.estimator.
        """
        inputs = tf.cast(features["inputs"], tf.float32)
        control_inputs = tf.cast(features["controls"], tf.float32)
        bin_defs = tf.convert_to_tensor(self.bins, dtype=tf.float32)

        # Dynamically determine if multistep prediction is needed
        # multistep is computationally costly, so we don't want to do this
        # always remember that in TF 1.x we build the graph first -- so we
        # must have these inputs to set up the depenencies if multistep is
        # needed in the future

        if "pred_controls" in features:
            do_multistep = True
            # one series of prediction controls, batch size should be 1
            prediction_control_inputs = tf.cast(features["pred_controls"], tf.float32)
        else:
            do_multistep = False
            batch_size = tf.shape(inputs)[0]
            m = self.control_size
            prediction_control_inputs = tf.cast(
                tf.fill([batch_size, 0, m], -1), tf.float32
            )
            # prediction_control_inputs = tf.convert_to_tensor(np.empty((inputs.shape[0], 0, control_inputs.shape[2])), dtype=np.float32)
            # prediction_control_inputs = tf.convert_to_tensor(np.empty((0, control_inputs.shape[2])), dtype=np.float32)  # *** use this line instead of the above

        self.build(inputs, control_inputs, prediction_control_inputs, labels, bin_defs)
        self.build_multistep_prediction(prediction_control_inputs, bin_defs)

        ### 1
        if mode == tf.estimator.ModeKeys.PREDICT:
            predictions = {
                "logits": self.outputs_logit,
                "predictions_1step_mean": self.outputs_1step_mean,
                "predictions_1step_var": self.outputs_1step_var,
                "predictions_distribution": self.outputs_distribution,
            }

            if do_multistep:
                # mm = tf.expand_dims(self.outputs_multistep_mean, axis=[1])
                # hook = tf.train.LoggingTensorHook(
                #    {"multistep raw shape":
                #        tf.shape(self.outputs_multistep_raw),
                #     "1step mean shape":
                #        tf.shape(self.outputs_1step_mean)}, every_n_iter=10)
                predictions = dict(
                    **predictions,
                    **{
                        "multistep_mean": tf.expand_dims(
                            self.outputs_multistep_mean, axis=[0]
                        ),
                        "multistep_var": tf.expand_dims(
                            self.outputs_multistep_var, axis=[0]
                        ),
                        "multistep_raw": tf.expand_dims(
                            self.outputs_multistep_raw, axis=[0]
                        ),
                    }
                )
            return tf.estimator.EstimatorSpec(
                mode, predictions=predictions, prediction_hooks=[]
            )

        ### 2
        logging_hook = tf.estimator.LoggingTensorHook(
            {"loss": self.loss, "accuracy": self.accuracy,}, every_n_iter=100,
        )

        global_step = tf.compat.v1.train.get_global_step()
        with tf.control_dependencies([self.train_op]):
            increment_global_step = tf.compat.v1.assign_add(global_step, 1)
            self.train_op_with_step = increment_global_step

        if mode == tf.estimator.ModeKeys.TRAIN:
            return tf.estimator.EstimatorSpec(
                mode,
                loss=self.loss,
                train_op=self.train_op_with_step,
                training_hooks=[logging_hook],
            )

        if mode == tf.estimator.ModeKeys.EVAL:
            metrics = {"accuracy": self.accuracy}
            return tf.estimator.EstimatorSpec(
                mode, loss=self.loss, eval_metric_ops=metrics
            )
