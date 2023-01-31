# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: varitional_rnn
   :synopsis: varitional_rnn.

.. moduleauthor:: SROM Team
"""


import torch
import torch.nn as nn
import torch.optim as optim


def rnn_variational_autoencoder(
    input_dim,
    output_dim,
    window_length,
    generator_dim,
    rnn_cells=64,
    rnn_depth=2,
    type_rnn="GRU",
    qnet_dim=64,
    qnet_depth=3,
    rnn_act="Tanh",
    qnet_act="Tanh",
    vae_reg=0.01,
    device="cpu",
):
    """
    Builds a variational-inference RNN
    Args:
        input_dim: number of input features
        output_dim: number of target features
        window_length: number of timesteps in the window
        generator_dim: dimension of the latent variable
        rnn_cells: number of RNN units
        rnn_depth: number of RNN layers in the encoder and decoder
        type_rnn: types of RNN, 'GRU' or 'LSTM'
        qnet_dim: number of neurons per layer of the posterior network
        qnet_depth: number of layers in the posterior network
        rnn_act: type of activation to use for rnn, defaults to 'Tanh'
                 the string should follow the name in torch.nn, e.g., 'ReLU', 'Sigmoid', 'Softplus', ...
        qnet_act: type of activation for the posterior network
        vae_reg: regularization parameter for the variational inference model
        device: devie to run the neural network. "cpu", "cuda", or "cuda:x". x is a GPU id, eg. "cuda:0"
    Returns:
        Python Class: encoder-posterior-decoder model for training
        Python Class: encoder-posterior         model to extract embeddings
    """

    encoder_rnn = GM_RNN(
        x_dim=input_dim,
        y_dim=output_dim,
        h_dim=rnn_cells,
        rnn_depth=rnn_depth,
        rnn_cell=type_rnn,
        rnn_name="Encoder",
        act_func=rnn_act,
        device=device,
    )

    decoder_rnn = GM_RNN(
        x_dim=input_dim + generator_dim,
        y_dim=output_dim,
        h_dim=rnn_cells,
        rnn_depth=rnn_depth,
        rnn_cell=type_rnn,
        rnn_name="Decoder",
        act_func=rnn_act,
        device=device,
    )

    qnet = Post_Net(
        x_dim=rnn_depth * rnn_cells,
        q_dim=generator_dim,
        h_dim=qnet_dim,
        net_height=qnet_depth,
        act_func=qnet_act,
        device=device,
    )

    encoder_rnn.init_net()
    decoder_rnn.init_net()
    qnet.init_net()

    def_loss = Loss(vae_param=vae_reg)

    train_model = VI_RNN_Model(encoder_rnn, decoder_rnn, qnet, def_loss, window_length)
    feature_extractor = VI_RNN_Feature_Extractor(encoder_rnn, qnet)

    return train_model, feature_extractor


# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

# Define common loss functions
class Loss:
    """
    This class defines loss functions used in the training
    Args:
        vae_param: regularziation parameter for ELBO
    """

    def __init__(self, vae_param=1.0):
        """
            vae_param (float):
        """
        self.vae_param = vae_param

    def mse_loss(self, y_true, y_pred, y_var=None):
        """
        Mean Square Error
        Args:
            y_true: observation
            y_pred: mean of the Gaussian
            y_var : redundant
        """
        loss = (y_pred - y_true) ** 2
        return 0.5 * loss.mean()

    def gm_loss(self, y_true, y_pred, y_var):
        """
        Negative log likelihood (NLL) for a diagonal-covariance Gaussian
        Args:
            y_true: observation
            y_pred: mean of the Gaussian
            y_var : variance of the Gaussian
        """
        loss = (y_pred - y_true) ** 2 / y_var + y_var.log()
        return 0.5 * loss.mean()

    def kl_loss(self, y_mean, y_var):
        """
        Kullback-Leibler Divergence between zero-mean Gaussian and a diagonal-cov Gaussian
        Args:
            y_mean: mean of the Gaussian
            y_var : variance of the Gaussian
        """
        loss = y_mean ** 2 + y_var - y_var.log()
        return 0.5 * loss.mean()

    def vi_loss(self, rnn_loss, kl_loss):
        """
        Compute Negative Evidence Lower BOund = beta*KL_Div + NLL
        """
        loss = rnn_loss + self.vae_param * kl_loss
        return loss


# RNN with a Gaussian diagonal covariance model.
# By default, GRU is used
class GM_RNN(nn.Module):
    def __init__(
        self,
        x_dim,  # dimension of input
        y_dim,  # dimension of prediction
        h_dim,  # dimension of the Recurrent layer hidden state
        rnn_depth=1,  # height of RNN layers
        rnn_cell="GRU",  # type of RNN cell "GRU" or "LSTM" supported
        rnn_name="RNN",  # name of the RNN
        act_func="Tanh",  # activation function by default Tanh is used
        device="cpu",
    ):
        """
            x_dim: dimension of input
            y_dim: dimension of prediction
            h_dim: dimension of the Recurrent layer hidden state
            rnn_depth: height of RNN layers
            rnn_cell: type of RNN cell "GRU" or "LSTM" supported
            rnn_name: name of the RNN
            act_func: activation function by default Tanh is used
        """
        super(GM_RNN, self).__init__()

        self.name = rnn_name

        self.x_dim = x_dim
        self.y_dim = y_dim
        self.h_dim = h_dim
        self.rnn_depth = rnn_depth

        if rnn_cell == "LSTM":
            self.rnn_cell = "LSTM"
            rnn = nn.LSTMCell
            self.states = [
                (torch.zeros(1, self.h_dim), torch.zeros(1, self.h_dim))
                for _ in range(self.rnn_depth)
            ]
        else:
            self.rnn_cell = "GRU"
            rnn = nn.GRUCell
            self.states = [torch.zeros(1, self.h_dim) for _ in range(self.rnn_depth)]

        self.act = getattr(nn, act_func)()

        self.encoder = nn.Sequential(nn.Linear(x_dim, h_dim), self.act)
        self.decoder = nn.Sequential(nn.Linear(h_dim, h_dim), self.act)

        self.core_rnn = nn.ModuleList(
            [rnn(h_dim, h_dim) for _ in range(self.rnn_depth)]
        )

        self.expect = nn.Linear(h_dim, y_dim)  # expectation
        self.logvar = nn.Linear(h_dim, y_dim)  # log-variance

        self.device = device

        if self.device == "cpu":
            print("RNN on CPU", flush=True)
        else:
            self.to_dev()

    # change device
    def to_dev(self, device=None):
        """
            to_dev method
        """
        if device is None:
            device = self.device

        print("RNN on device " + device, flush=True)

        dev = torch.device(device)

        self.expect.to(dev)
        self.logvar.to(dev)

        self.encoder.to(dev)
        self.decoder.to(dev)
        self.core_rnn.to(dev)

        for i in range(len(self.states)):
            if self.rnn_cell == "LSTM":
                for j in range(len(self.states[i])):
                    self.states[i][j] = self.states[i][j].to(dev)
            else:
                self.states[i] = self.states[i].to(dev)

    # network initialization
    def init_mod(self, list_params):
        """
            network initialization
        """
        for name, param in list_params.named_parameters():
            if "bias" in name:
                nn.init.uniform_(param, -0.1, 0.1)
            elif "weight" in name:
                nn.init.xavier_normal_(param)

    def init_net(self):
        """
            linear layer initialization
        """
        # linear layer initialization
        nn.init.uniform_(self.expect.bias, -0.1, 0.1)
        nn.init.uniform_(self.logvar.bias, -0.1, 0.1)

        nn.init.xavier_normal_(self.expect.weight)
        nn.init.xavier_normal_(self.logvar.weight)

        self.init_mod(self.encoder)
        self.init_mod(self.decoder)

        # rnn initialization
        for i in range(self.rnn_depth):
            self.init_mod(self.core_rnn[i])

    # one step simulation
    def do_step(self, x_in):
        """
            do_step
        """
        rnn_in = self.encoder(x_in)

        for i in range(self.rnn_depth):
            self.states[i] = self.core_rnn[i](rnn_in, self.states[i])
            if self.rnn_cell == "LSTM":
                rnn_in = self.states[i][0]
            else:
                rnn_in = self.states[i]

        rnn_out = self.decoder(rnn_in)

        pred_mean = self.expect(rnn_out)
        pred_var = self.logvar(rnn_out).exp()
        return pred_mean, pred_var

    # input dimension: nTime x nBatch x nfeature
    def forward(self, input, init_state=True, nstep=None, return_h=False):
        """
            forward method
        """
        if self.rnn_cell == "LSTM":
            for i in range(len(self.states)):
                for j in range(len(self.states[i])):
                    if self.states[i][j].size(0) != input[0].size(0):
                        self.states[i][j].detach_()
                        self.states[i][j].resize_(
                            input[0].size(0), self.states[i][j].size(1)
                        )
            if init_state:
                for i in range(len(self.states)):
                    for j in range(len(self.states[i])):
                        self.states[i][j].detach_()
                        self.states[i][j].zero_()
        else:
            for i in range(len(self.states)):
                if self.states[i].size(0) != input[0].size(0):
                    self.states[i].detach_()
                    self.states[i].resize_(input[0].size(0), self.states[i].size(1))
            if init_state:
                for i in range(len(self.states)):
                    self.states[i].detach_()
                    self.states[i].zero_()

        if not nstep:
            nstep = input.size(0)

        if return_h:
            for i in range(nstep):
                self.do_step(input[i])

            if self.rnn_cell == "LSTM":
                out_h = []
                for i in range(len(self.states)):
                    out_h.append(torch.cat(self.states[i], dim=1))
                return torch.cat(out_h, dim=1)
            else:
                return torch.cat(self.states, dim=1)
        else:
            time_mean = []
            time_var = []
            for i in range(nstep):
                pred_mean, pred_var = self.do_step(input[i])
                time_mean += [pred_mean]
                time_var += [pred_var]

            time_mean = torch.stack(time_mean, dim=0)
            time_var = torch.stack(time_var, dim=0)

            return time_mean, time_var

    def MC_simulation(self, init_cond, nstep, nsamples=1000, control_data=None):
        """
            Mc_simulation method
        """
        # copy internal states
        if self.rnn_cell == "LSTM":
            for i in range(len(self.states)):
                for j in range(len(self.states[i])):
                    self.states[i][j] = self.states[i][j].repeat_interleave(
                        nsamples, dim=0
                    )
        else:
            for i in range(len(self.states)):
                self.states[i] = self.states[i].repeat_interleave(nsamples, dim=0)

        # set initial condition
        traj = init_cond[0].repeat_interleave(nsamples, dim=0)
        eps = init_cond[1].repeat_interleave(nsamples, dim=0)
        eps.normal_()
        traj = traj + eps * init_cond[1].repeat_interleave(nsamples, dim=0).sqrt()

        mc_pred = []
        if control_data is not None:
            for i in range(nstep):
                in_x = torch.cat(
                    (traj, control_data[i].repeat_interleave(nsamples, dim=0)), dim=1
                )
                traj, pred_var = self.do_step(in_x)
                traj = traj + eps.normal_() * pred_var.sqrt()
                mc_pred += [traj]
        else:
            for i in range(nstep):
                traj, pred_var = self.do_step(traj)
                traj = traj + eps.normal_() * pred_var.sqrt()
                mc_pred += [traj]

        return mc_pred


# Multilayer Feedforward Network for approximate posterior distribution
# Approximate posterior distribution is given as a Gaussian with a diagonal covariance
# Prior distribution is zero-mean Gaussian with std = 1.
class Post_Net(nn.Module):
    def __init__(
        self,
        x_dim,  # dimension of input variable
        q_dim=10,  # dimension of latent variable
        h_dim=32,  # dimension of hidden units
        net_height=1,  # height of posterior network
        act_func="Tanh",  # activation function
        device="cpu",
    ):
        """
            x_dim: dimension of input variable
            q_dim: dimension of latent variable
            h_dim: dimension of hidden units
            net_height: height of posterior network
            act_func: activation function
        """
        super(Post_Net, self).__init__()

        self.name = "Posterior"

        self.device = device

        self.x_dim = x_dim
        self.q_dim = q_dim
        self.h_dim = h_dim
        self.net_height = net_height

        self.act = getattr(nn, act_func)()

        # define network
        self.post_net = self.build_post_net()
        self.expect = nn.Linear(self.h_dim, self.q_dim)  # expectation
        self.logvar = nn.Linear(self.h_dim, self.q_dim)  # log-variance

        # temporary storages for mc sampling
        self.rand_noise = torch.zeros(1, 1)

        if self.device == "cpu":
            print("Post_Net on CPU", flush=True)
        else:
            self.to_dev()

    # posterior network
    def build_post_net(self):
        """
            Build post net method
        """
        net = []
        dim_in = self.x_dim
        dim_out = self.h_dim
        for i in range(self.net_height):
            net.append(nn.Linear(dim_in, dim_out))
            net.append(self.act)
            dim_in = self.h_dim
        return nn.Sequential(*net)

    # change device
    def to_dev(self, device=None):
        """
            to_dev method
        """
        if device is None:
            device = self.device

        print("Post_Net on device " + device, flush=True)

        dev = torch.device(device)

        self.expect.to(dev)
        self.logvar.to(dev)
        self.post_net.to(dev)

        self.rand_noise = self.rand_noise.to(dev)

    # network initialization
    def init_net(self):
        """
            network initialization
        """
        # linear layer initialization
        nn.init.uniform_(self.expect.bias, -0.1, 0.1)
        nn.init.uniform_(self.logvar.bias, -0.1, 0.1)

        nn.init.xavier_normal_(self.expect.weight)
        nn.init.xavier_normal_(self.logvar.weight)

        for name, param in self.post_net.named_parameters():
            if "bias" in name:
                nn.init.uniform_(param, -0.1, 0.1)
            elif "weight" in name:
                nn.init.xavier_normal_(param)

    def post_sampling(self, q_mean, q_var, num_samples):
        """
            Post sampling method.
        """
        out_size = torch.Size([q_mean.size(0) * num_samples, q_mean.size(1)])

        if self.rand_noise.size() != out_size:
            self.rand_noise.resize_(out_size)

        self.rand_noise.normal_()

        mc_out = (
            q_mean.repeat_interleave(num_samples, dim=0)
            + q_var.repeat_interleave(num_samples, dim=0).sqrt() * self.rand_noise
        )

        return mc_out

    # input dimension: nBatch x nfeature
    def forward(self, in_x, mc_samples=None):
        """
            forward method.
        """
        out_q = self.post_net(in_x)

        mean_q = self.expect(out_q)
        var_q = self.logvar(out_q).exp()

        if mc_samples is not None:
            return self.post_sampling(mean_q, var_q, mc_samples)
        else:
            return mean_q, var_q


# PyTorch nn.Module for the whole network
class VI_RNN_Model:  # (nn.Module):
    """
    This class contains the whole VI-RNN model: encoder - posterior - decoder
    """

    def __init__(self, encoder, decoder, qnet, loss, nlag):
        """
            Args:
            encoder : encoder RNN
            decoder : decoder RNN
            qnet    : posterior network
            nlag    : length of the time window
        """
        self.encoder = encoder
        self.decoder = decoder
        self.qnet = qnet
        self.nlag = nlag

        self.loss = loss

        self.device = self.encoder.device
        self.opt = None
        self.learning_rate = None
        self.lr_decay = None
        self.mc_samples = None
        self.rnn_loss = None

    def ModelCheckpoint(self, check_file_name, period=10):
        """
        Save intermediate models
        Args:
            check_file_name: string format to save intermediate models. It should be in a format : XXX_{:03d}-XXX{:.2e}
        """
        check_point = {}
        check_point["name"] = "checkpoint"
        check_point["check_file_name"] = check_file_name
        check_point["check_period"] = period

        return check_point

    def fit(
        self, X, Y=None, validation_split=0.1, batch_size=32, epochs=10, callbacks=None
    ):
        """
        Train VI-RNN
        The input data (X,Y) should be 3-D numpy arrays with dimensions (Batch x Time x Features)
        Args:
            X : input features
            Y : target features. If Y == None, X is split into input (t = 0~T-1) and target (t = 1~T)
            validation_split : fraction of data reserved for validation
            batch_size : size of the mini-batch used in the training
            epochs : number of training epochs
            mc_samples : number of posterior samples
            check_period : intermediate model save parameters
        """

        input_X = torch.from_numpy(X)

        if Y is not None:
            input_Y = torch.from_numpy(Y)
        else:
            input_Y = input_X[:, 1:, :].clone()
            input_X = input_X[:, :-1, :].clone()

        if self.device != "cpu":
            input_X = input_X.to(torch.device(self.device))
            input_Y = input_Y.to(torch.device(self.device))

        # separate training and validation data set
        num_batches = int((1 - validation_split) * input_X.size(0) / batch_size)
        num_train = num_batches * batch_size
        num_valid = input_X.size(0) - num_train

        print(
            "Train on "
            + str(num_train)
            + " samples, validate on "
            + str(num_valid)
            + " samples"
        )

        rand_idx = torch.randperm(input_X.size(0))

        train_X = input_X[rand_idx[:num_train]]
        train_Y = input_Y[rand_idx[:num_train]]

        valid_X = input_X[rand_idx[num_train:]]
        valid_Y = input_Y[rand_idx[num_train:]]

        # callback functions
        check_point = None

        if callbacks is not None:
            for ii in range(len(callbacks)):
                if callbacks[ii]["name"] == "checkpoint":
                    check_point = callbacks[ii]

        # define optimizers
        if self.learning_rate is not None:
            opt_rnn = self.opt(self.encoder.parameters(), lr=self.learning_rate)
            opt_vi = self.opt(
                [
                    {"params": self.qnet.parameters()},
                    {"params": self.decoder.parameters()},
                ],
                lr=self.learning_rate,
            )

        else:
            opt_rnn = self.opt(self.encoder.parameters())
            opt_vi = self.opt(
                [
                    {"params": self.qnet.parameters()},
                    {"params": self.decoder.parameters()},
                ]
            )

        if self.lr_decay:
            lr_decay_rnn = optim.lr_scheduler.CosineAnnealingLR(
                opt_rnn, epochs, eta_min=1.0e-4
            )
            lr_decay_vi = optim.lr_scheduler.CosineAnnealingLR(
                opt_vi, epochs, eta_min=1.0e-4
            )

        # define loss function
        if self.rnn_loss == "mse":
            rnn_loss = self.loss.mse_loss
        elif self.rnn_loss == "gaussian":
            rnn_loss = self.loss.gm_loss
        else:
            print("RNN Loss is not defined. Use MSE")
            rnn_loss = self.loss.mse_loss

        kl_loss = self.loss.kl_loss

        # train encoder RNN
        print(" ")
        print("Start Training RNN")
        print(" ")

        rnn_train_loss = []
        rnn_valid_loss = []
        for ii in range(epochs):
            b_id = torch.randperm(num_train)
            loc_loss = 0.0
            for jj in range(num_batches):
                idx = b_id[jj * batch_size : (jj + 1) * batch_size]
                in_x = train_X[idx].transpose(0, 1)
                in_y = train_Y[idx].transpose(0, 1)

                opt_rnn.zero_grad()

                pred_mean, pred_var = self.encoder(in_x)

                loss = rnn_loss(in_y, pred_mean, pred_var)

                loc_loss = loc_loss + loss.item()

                loss.backward()
                opt_rnn.step()

            if self.lr_decay:
                lr_decay_rnn.step()

            with torch.no_grad():
                in_x = valid_X.transpose(0, 1)
                in_y = valid_Y.transpose(0, 1)

                pred_mean, pred_var = self.encoder(in_x)
                loss = rnn_loss(in_y, pred_mean, pred_var)

            rnn_train_loss += [loc_loss / num_batches]
            rnn_valid_loss += [loss.item()]

            print(
                "At epoch {:d} - Training loss: {:.3e}, Validation loss: {:.3e}".format(
                    ii, rnn_train_loss[-1], rnn_valid_loss[-1]
                )
            )

            if check_point is not None:
                if ii % check_point["check_period"] == 0:
                    torch.save(
                        {self.encoder.name: self.encoder.state_dict()},
                        check_point["check_file_name"].format(ii, rnn_train_loss[-1])
                        + "_rnn",
                    )

        # train posterior and decoder RNN
        print(" ")
        print("Start Training VI-RNN")
        print(" ")

        vi_train_loss = []
        vi_valid_loss = []
        for ii in range(epochs):
            b_id = torch.randperm(num_train)
            loc_loss = 0.0
            for jj in range(num_batches):
                idx = b_id[jj * batch_size : (jj + 1) * batch_size]
                in_x = train_X[idx].transpose(0, 1)
                in_y = train_Y[idx].transpose(0, 1)

                opt_vi.zero_grad()

                q_in = self.encoder(in_x, return_h=True)
                q_mean, q_var = self.qnet(q_in)

                q_samples = self.qnet.post_sampling(
                    q_mean, q_var, num_samples=self.mc_samples
                )

                in_x_mc = []
                for t in range(in_x.size(0)):
                    in_x_mc += [
                        torch.cat(
                            (
                                in_x[t].repeat_interleave(self.mc_samples, dim=0),
                                q_samples,
                            ),
                            dim=1,
                        )
                    ]
                in_x_mc = torch.stack(in_x_mc, dim=0)

                in_y_mc = in_y.repeat_interleave(self.mc_samples, dim=1)

                pred_mean, pred_var = self.decoder(in_x_mc)

                l1 = rnn_loss(in_y_mc, pred_mean, pred_var)
                l2 = kl_loss(q_mean, q_var)
                loss = self.loss.vi_loss(l1, l2)

                loc_loss = loc_loss + l1.item()  # loss.item()

                loss.backward()
                opt_vi.step()

            if self.lr_decay:
                lr_decay_vi.step()

            with torch.no_grad():
                in_x = valid_X.transpose(0, 1)
                in_y = valid_Y.transpose(0, 1)

                q_in = self.encoder(in_x, return_h=True)

                q_mean, q_var = self.qnet(q_in)
                q_samples = self.qnet.post_sampling(
                    q_mean, q_var, num_samples=self.mc_samples
                )

                in_x_mc = []
                for t in range(in_x.size(0)):
                    in_x_mc += [
                        torch.cat(
                            (
                                in_x[t].repeat_interleave(self.mc_samples, dim=0),
                                q_samples,
                            ),
                            dim=1,
                        )
                    ]
                in_x_mc = torch.stack(in_x_mc, dim=0)
                in_y_mc = in_y.repeat_interleave(self.mc_samples, dim=1)

                pred_mean, pred_var = self.decoder(in_x_mc)

                l1 = rnn_loss(in_y_mc, pred_mean, pred_var)
                l2 = kl_loss(q_mean, q_var)
                loss = self.loss.vi_loss(l1, l2)

            vi_train_loss += [loc_loss / num_batches]
            vi_valid_loss += [l1.item()]  # [loss.item()]

            print(
                "At epoch {:d} - Training loss: {:.3e}, Validation loss: {:.3e}".format(
                    ii, vi_train_loss[-1], vi_valid_loss[-1]
                )
            )

            if check_point is not None:
                if ii % check_point["check_period"] == 0:
                    self.save_weights(
                        check_point["check_file_name"].format(ii, vi_train_loss[-1])
                        + "_vinet"
                    )

        train_hist = {}
        train_hist["rnn_train_loss"] = rnn_train_loss
        train_hist["rnn_valid_loss"] = rnn_valid_loss
        train_hist["vi_trian_loss"] = vi_train_loss
        train_hist["vi_valid_loss"] = vi_valid_loss

        return train_hist

    def compile(self, optimizer="Adam", loss="mse", **kwarg):
        """
        Define optimization functions for the training of VI-RNN
        Args:
            optimizer (string)    : optimizer to use.
            loss      (string)    : rnn loss function, "mse" or "gaussian"
            learning_rate (float) : learning rate
            lr_decay (logical)    : use learing rate decay or not
            mc_samples (int)       : number of samples for Monte Carlo estimation of the loss function
        """

        if optimizer in ["ADAM", "adam", "Adam"]:
            print("Use ADAM Optimizer")
            self.opt = optim.Adam
        elif optimizer in ["Adadelta", "ADAdelta", "adadelta", "ADADelta"]:
            print("Use Adadelta Optimizer")
            self.opt = optim.Adadelta
        elif optimizer in ["RMSprop", "rmsprop", "RMSPROP"]:
            print("Use RMSprop Optimizer")
            self.opt = optim.RMSprop
        else:
            print("Use SGD Optimizer")
            self.opt = optim.SGD

        self.rnn_loss = loss

        if "learning_rate" in kwarg:
            self.learning_rate = kwarg["learning_rate"]
        else:
            self.learning_rate = None

        if "lr_decay" in kwarg:
            self.lr_decay = kwarg["lr_decay"]
        else:
            self.lr_decay = False

        if "mc_samples" in kwarg:
            self.mc_samples = kwarg["mc_samples"]
        else:
            self.mc_samples = 1

    def save_weights(self, file_name):
        """
        Save model weights on file_name (string)
        Always save on cpu
        """
        if self.device != "cpu":
            self.encoder.to_dev("cpu")
            self.qnet.to_dev("cpu")
            self.decoder.to_dev("cpu")

        torch.save(
            {
                self.encoder.name: self.encoder.state_dict(),
                self.qnet.name: self.qnet.state_dict(),
                self.decoder.name: self.decoder.state_dict(),
            },
            file_name,
        )

        if self.device != "cpu":
            self.encoder.to_dev()
            self.qnet.to_dev()
            self.decoder.to_dev()

    def load_weights(self, saved_model):
        """
        copy saved model weights from saved_model (string)
        """
        load_net = torch.load(saved_model)

        self.encoder.load_state_dict(load_net[self.encoder.name])
        self.qnet.load_state_dict(load_net[self.qnet.name])
        self.decoder.load_state_dict(load_net[self.decoder.name])


# PyTorch nn.Module for the feature extraction
class VI_RNN_Feature_Extractor:  # (nn.Module):
    """
    This class contains only encoder-posterior.
    Args:
        encoder : encoder RNN
        decoder : decoder RNN
    """

    def __init__(self, encoder, qnet):
        self.encoder = encoder
        self.qnet = qnet

        self.device = self.encoder.device

    def predict(self, X):
        """
        Compute the latent state from the input feature, X
        Args:
            X : 3-D numpy array with the dimension (Batch x Time x Features)
        """
        in_x = torch.from_numpy(X)
        in_x = in_x.transpose(0, 1)

        if self.device != "cpu":
            in_x = in_x.to(torch.device(self.device))

        with torch.no_grad():
            q_in = self.encoder(in_x, return_h=True)
            q_mean, _ = self.qnet(q_in)

        if self.device != "cpu":
            out = q_mean.to(torch.device("cpu")).numpy()
        else:
            out = q_mean.numpy()

        return out

    def load_weights(self, saved_model):
        """
        copy saved model weights from saved_model (string)
        """
        load_net = torch.load(saved_model)
        self.encoder.load_state_dict(load_net[self.encoder.name])
        self.qnet.load_state_dict(load_net[self.qnet.name])
