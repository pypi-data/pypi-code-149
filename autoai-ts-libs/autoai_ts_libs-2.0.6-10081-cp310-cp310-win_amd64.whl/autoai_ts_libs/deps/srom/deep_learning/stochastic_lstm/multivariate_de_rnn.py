# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


# -*- coding: utf-8 -*-

""" Module implementing the multivariate DE RNN model

Created on Feb 1, 2018
@author: wmgifford
"""

import tensorflow as tf

from autoai_ts_libs.deps.srom.deep_learning.stochastic_lstm.univariate_de_rnn import UnivariateDERNN


class MultivariateDERNN(object):
    """
    Description for the class.

    """

    def __init__(
        self,
        bins=None,
        input_size=1,
        control_size=0,
        rnn_state_size=128,
        rnn_layers=1,
        lr=0.1,
        predict_num_samples=20 * 10 ** 3,
        reg_lambda=0.1,
        cpus=None,
    ):
        """ Create model for multivariate density estimation rnn """

        self.input_size = input_size
        self.control_size = control_size

        self.bins = bins
        self.d_size = bins.shape[0] - 1  ### FIX, bins is 2d now

        self.rnn_state_size = rnn_state_size
        self.rnn_layers = rnn_layers
        self.predict_num_samples = predict_num_samples
        self.lr = lr

        self.reg_lambda = reg_lambda
        # allow_soft_placement=True,
        if cpus is not None:
            self.config = tf.compat.v1.ConfigProto(device_count={"CPU": cpus})
        else:
            self.config = tf.compat.v1.ConfigProto()
            self.config.gpu_options.allow_growth = True

        # create a univariate model to handle each variable
        m = self.control_size
        l = self.input_size
        self.univariate_models = [
            UnivariateDERNN(
                control_size=l - 1 + m + i,
                bins=bins[i],
                rnn_state_size=self.rnn_state_size,
                rnn_layers=self.rnn_layers,
                lr=self.lr,
                predict_num_samples=self.predict_num_samples,
            )
            for i in range(l)
        ]

    def build_multistep_prediction(self, prediction_control_inputs, bin_defs):
        """
        Build the graph for multistep prediction for the
        multivariate case

        Args:
            prediction_control_inputs (type, optional/required): Desc
            bin_defs
        """
        # update for each time step:
        # assume 3 variables y0, y1, y2
        # 1. get next output for y0 --
        #   y0(t+1), given y0(t), y1(t), y2(t), U
        # 2. get next output for y1 --
        #   y1(t+1), given y0(t), y1(t), y2(t), U | y1(t+1)
        # 3. get next output for y2 --
        #   y2(t+1), given y0(t), y1(t), y2(t), U | y1(t+1), y2(t+1)
        #
        # now state is y0(t+1), y1(t+1), y2(t+1)

        l = self.input_size
        Ns = self.predict_num_samples
        num_steps = tf.shape(prediction_control_inputs)[1]
        # rnn_state_size = self.rnn_state_size

        # tensor array for outputs of prediction
        pred_outputs = tf.TensorArray(
            dtype=tf.float32,
            size=num_steps,
            name="multistep-prediction-outputs-tensor-array",
        )
        self.pred_outputs = pred_outputs

        prediction_control_inputs_ta = tf.TensorArray(
            dtype=tf.float32,
            size=num_steps,
            name="multistep-prediction-controls-tensor-array",
        )
        prediction_control_inputs_ta = prediction_control_inputs_ta.unstack(
            tf.transpose(prediction_control_inputs, perm=[1, 0, 2])
        )

        # set up random sampling
        # uniform_distribution = tfp.distributions.Uniform(
        #    name="distribution-driver")  # [0,1)
        # uniform_distribution_samples = \
        # uniform_distribution.sample(sample_shape=(num_steps, Ns, 1))

        # initial inputs / states from all underlying lstms
        with tf.compat.v1.variable_scope("mv-multistep-init"):
            init_input, init_lstm_state, init_lstm_output, primed_input = [], [], [], []
            for i in range(l):
                # self.multistep_init_state = (init_input,
                #   pred_init_lstm_state, init_lstm_output)
                tmp_input, tmp_lstm_state, tmp_lstm_output = self.univariate_models[
                    i
                ]._init_multistep(self.univariate_models[i].x)
                init_input.append(tmp_input)  # full input including controls
                init_lstm_state.append(tmp_lstm_state)
                init_lstm_output.append(tmp_lstm_output)

                output = tf.nn.softmax(
                    self.univariate_models[i].output_decoder_op(init_lstm_output[i])
                )
                primed_input.append(
                    self.univariate_models[i]._sample_output_distribution(
                        output, tf.random.uniform((Ns, 1)), bin_defs[i]
                    )
                    + tf.expand_dims(init_input[i][:, 0], 1)
                )

        # prepare the while loop
        # condition for multistep prediction
        def condition(i, *arg):
            return i < num_steps

        def body(k, cur_input, lstm_output_list, state_list, the_prediction):
            """
            Body for multistep prediction while_loop, multivariate case

            Args:
                k: step index
                cur_input: current input
                lstm_output_list: list of prior lstm output
                state_list: list of prior states
                the_prediction: tensorarray used to store the prediction
                    results

                new output is a function of prior lstm output, prior state,
                    and prior output (current input)

                cur_input, lstm_output_list, state_list are all lists of
                    dimension equal to the number of variables in the
                    multivariate time series.
            """
            # prediction_control_inputs = tf.tile(tf.expand_dims(
            #     prediction_control_inputs_ta.read(k), 0), [Ns, 1])
            prediction_control_inputs = tf.tile(
                prediction_control_inputs_ta.read(k), [Ns, 1]
            )
            cur_input_new = [None] * l
            control_inputs = [None] * l
            for i in range(l):
                # 0: old_output = old_output[0] + old_output from other

                # input: yprev[i], controls = yprev[ all but i ] + additional
                #   controls + youtput[:i]
                # formulated input = input + controls
                # set the controls right, multistep_prediction does the concat
                # with input
                control_inputs[i] = tf.concat(
                    [cur_input[j] for j in range(l) if j != i]
                    + [prediction_control_inputs]
                    + cur_input_new[:i],
                    axis=1,
                )
                (
                    cur_input_new[i],
                    lstm_output_list[i],
                    state_list[i],
                ) = self.univariate_models[i]._multistep_prediction_step(
                    cur_input[i],
                    lstm_output_list[i],
                    state_list[i],
                    control_inputs[i],
                    Ns,
                    bin_defs[i],
                )
            this_step_prediction = tf.stack(cur_input_new, axis=1)
            return (
                k + 1,
                cur_input_new,
                lstm_output_list,
                state_list,
                the_prediction.write(k, this_step_prediction),
            )

        # y = tf.split(tf.tile(tf.expand_dims(self.inputs[-1,0,:],0), [Ns,1]),
        # num_or_size_splits=l, axis=1)
        # initial state for while loop
        # primed_input is the predicted output from the input at t-1 (i.e.,
        # input[-2])
        with tf.compat.v1.variable_scope("mv-multistep-predict"):
            pred_outputs = pred_outputs.write(0, tf.stack(primed_input, axis=1))
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

    def model_fn(self, features, labels, mode=None, params=None, config=None):
        """
        Build graph for multivariate DE RNN
        """
        # inputs should be of the form:
        # at each time t: y_1, y_2, ... y_l
        # control_inputs should be of the form: u_1, u_2, ..., u_m

        # number of bins in discretized output, for multivariate case this is
        # a vector of length l, size of multivariate input
        d_size = self.d_size
        m = self.control_size
        l = self.input_size

        inputs = tf.cast(features["inputs"], tf.float32)
        control_inputs = tf.cast(features["controls"], tf.float32)

        # inputs should be [batches, time steps, covariates]
        # make length and batch size dynamic we need this for rolling
        # multistep prediction
        max_time = tf.shape(inputs)[1]
        batch_size = tf.shape(inputs)[0]
        print(inputs.shape)
        print(control_inputs.shape)

        # set up placeholders and add as class members
        # outputs_ = tf.placeholder(tf.int64, shape=(None, None, l),
        #                           name="output-placeholder")
        # inputs = tf.placeholder(tf.float32, shape=(None, None, l),
        #                         name='input-placeholder')
        # inputs are: [max_time, batch_size, 1]
        # bin_defs = tf.placeholder(dtype=tf.float32, shape=(l, max(d_size)+1),
        #                           name="distribution-bins-placeholder")
        # reg_lambda = tf.placeholder(tf.float32, shape=())

        # bin_defs = tf.convert_to_tensor(self.bins, dtype=tf.float32)

        bin_defs = [
            tf.convert_to_tensor(self.bins[i, :], dtype=tf.float32)
            for i in range(self.bins.shape[0])
        ]
        reg_lambda = self.reg_lambda

        # not needed?
        #   self.inputs = inputs
        #   self.outputs_ = outputs_

        # each univariate model expects input of the form:
        # 1. y_1, y_2, ... y_l, u_1, u_2, ..., u_m,
        # 2. y_1, y_2, ... y_l, u_1, u_2, ..., u_m, y(t+1)_1, ...
        # 3. y_1, y_2, ... y_l, u_1, u_2, ..., u_m, y(t+1)_1, y(t+1)_2, ...
        # 4. etc.

        if labels is not None:
            outputs_ = tf.cast(labels, tf.int64)
        else:
            outputs_ = None

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

        # multivariate
        # in multivariate case, we need next time step as input for the
        # conditional distributions to avoid missing values at end of the
        # batches, we shorten the original input
        # this is only for the input (y) portion, not control

        if mode == tf.estimator.ModeKeys.TRAIN:
            the_controls = control_inputs[:, :-1, :]
            the_inputs = inputs[:, :-1, :]
            next_time_step_inputs = inputs[:, 1:, :]
            the_outputs_ = outputs_[:, :-1, :]
        else:
            the_controls = control_inputs[:, :, :]
            the_inputs = inputs[:, :, :]
            next_time_step_inputs = inputs[:, 1:, :]
            the_outputs_ = None

        inputs_split = tf.split(the_inputs, num_or_size_splits=l, axis=2)

        for i in range(l):
            with tf.compat.v1.variable_scope("univariate_model_y_{}".format(i + 1)):
                # construct input and controls
                # input should be one variable
                # control consists of all other inputs at this time step, the
                # original control inputs, and the next time step for all
                # previous input variables
                # inputs: y_i(t)
                # controls: y_{j\ne i}(t), u_1, u_2, u_3, ... u_m, y_{j<i}(t+1)
                # this_input = tf.expand_dims(inputs[:-1,:,i],2) # concatenate
                # original inputs with next time step
                # * we organize the above as follows *
                # input to univariate is only one variable,
                # controls capture the remaining information, in this order:
                # other_vars (y2, y3, etc.), original controls, next step
                # inputs
                this_input = inputs_split[
                    i
                ]  # tf.expand_dims(inputs_split[i], axis=[2])
                print(i)
                print("/")
                print(this_input.shape)
                print("/")
                if l == 1:  # one dimensional case
                    this_control_input = the_controls
                else:
                    other_vars = tf.concat(
                        [inputs_split[j] for j in range(l) if j != i], axis=2
                    )
                    # formulate the controls for this covariate
                    if i == 0:
                        # easy case, no dependence on "future values"
                        this_control_input = tf.concat(
                            [other_vars, the_controls], axis=2
                        )
                    elif mode == tf.estimator.ModeKeys.TRAIN:
                        # if training, we don't use the last value, so simple concat works
                        this_control_input = tf.concat(
                            [other_vars, the_controls, next_time_step_inputs[:, :, :i]],
                            axis=2,
                        )
                    else:
                        # prediction case
                        # the next value at the end of the time series does
                        # not exist, so we use the 1-step ahead mean,
                        # we need to first get these predictions for the last step, and add them
                        # to our next_step inputs to finalize the control inputs
                        last_step = tf.concat(
                            [
                                self.univariate_models[j].outputs_1step_mean[:, -1, :]
                                for j in range(i)
                            ],
                            axis=-1,
                        )
                        last_step = tf.expand_dims(last_step, axis=[1])
                        next_time = tf.concat(
                            [next_time_step_inputs[:, :, :i], last_step], axis=1
                        )
                        this_control_input = tf.concat(
                            [other_vars, the_controls, next_time], axis=2
                        )

                if mode == tf.estimator.ModeKeys.TRAIN:
                    this_output = tf.expand_dims(the_outputs_[:, :, i], axis=[2])
                else:
                    this_output = None

                self.univariate_models[i].build(
                    this_input,
                    this_control_input,
                    prediction_control_inputs,
                    this_output,
                    bin_defs[i],
                )

        with tf.compat.v1.variable_scope("multivariate_1step_prediction"):
            self.outputs_1step_mean = tf.concat(
                [u.outputs_1step_mean for u in self.univariate_models], -1
            )
            self.outputs_1step_var = tf.concat(
                [u.outputs_1step_var for u in self.univariate_models], -1
            )
            self.outputs_1step_distribution = tf.concat(
                [u.outputs_distribution for u in self.univariate_models], -1
            )  # sf.concat([u.outputs_tmp for u in univariate_models],-1)

        # multistep?
        # prediction_control_inputs = tf.placeholder(
        #    tf.float32, shape=(None, m), name='prediction-control-placeholder')
        # self.prediction_control_inputs = prediction_control_inputs
        self.build_multistep_prediction(prediction_control_inputs, bin_defs)

        if mode == tf.estimator.ModeKeys.PREDICT:
            if do_multistep:
                # mm = tf.expand_dims(self.outputs_multistep_mean, axis=[1])
                hook = tf.estimator.LoggingTensorHook(
                    {
                        "multistep raw shape": tf.shape(self.outputs_multistep_raw),
                        "1step mean shape": tf.shape(self.outputs_1step_mean),
                    },
                    every_n_iter=10,
                )
                predictions = {
                    "predictions_1step_mean": self.outputs_1step_mean,
                    "predictions_1step_var": self.outputs_1step_var,
                    "predictions_distribution": self.outputs_1step_distribution,
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
                return tf.estimator.EstimatorSpec(
                    mode, predictions=predictions, prediction_hooks=[]
                )
            else:
                hook = tf.estimator.LoggingTensorHook(
                    {"dist shape": tf.shape(self.outputs_1step_mean)}, every_n_iter=1
                )
                predictions = {
                    "predictions_1step_mean": self.outputs_1step_mean,
                    "predictions_1step_var": self.outputs_1step_var,
                    "predictions_distribution": self.outputs_1step_distribution,
                }
                return tf.estimator.EstimatorSpec(
                    mode, predictions=predictions, prediction_hooks=[]
                )

        # Training op and metrics

        global_step = tf.compat.v1.train.get_global_step()

        # self.train_op = tf.group(*[u.train_op for u in self.univariate_models])
        with tf.control_dependencies([u.train_op for u in self.univariate_models]):
            increment_global_step = tf.compat.v1.assign_add(global_step, 1)
            self.train_op = increment_global_step

        with tf.compat.v1.variable_scope("multivariate_loss"):
            self.loss = (1.0 / l) * tf.add_n([u.loss for u in self.univariate_models])
            tf.compat.v1.summary.scalar("loss", self.loss)
        with tf.compat.v1.variable_scope("multivariate_accuracy"):
            self.accuracy = (1.0 / l) * tf.add_n(
                [u.accuracy for u in self.univariate_models]
            )
            tf.compat.v1.summary.scalar("accuracy", self.accuracy)

        logging_hook = tf.estimator.LoggingTensorHook(
            {"loss": self.loss, "accuracy": self.accuracy,}, every_n_iter=100,
        )

        if mode == tf.estimator.ModeKeys.TRAIN:
            return tf.estimator.EstimatorSpec(
                mode,
                loss=self.loss,
                train_op=self.train_op,
                training_hooks=[logging_hook],
            )

        if mode == tf.estimator.ModeKeys.EVAL:
            metrics = {"accuracy": self.accuracy}
            return tf.estimator.EstimatorSpec(
                mode, loss=self.loss, eval_metric_ops=metrics
            )
