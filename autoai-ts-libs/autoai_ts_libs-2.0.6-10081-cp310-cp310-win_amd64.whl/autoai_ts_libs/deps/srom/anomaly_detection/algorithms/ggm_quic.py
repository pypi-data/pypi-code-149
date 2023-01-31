# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: ggm_quic
   :synopsis: Gaussian graphical model with quick algorithm.

.. moduleauthor:: SROM Team
"""

import numpy as np
from numpy import dot, power
from numpy.linalg import inv
from sklearn.covariance import empirical_covariance, EmpiricalCovariance
from sklearn.utils.extmath import fast_logdet
from sklearn.utils.validation import check_array
from sklearn.covariance import shrunk_covariance

# from sklearn.exceptions import ConvergenceWarning


"""
QUIC algoritm solve the following optimization.

\begin{equation}
\min f(X) = -\log \det X + trace(SX) + \lambda \lVert X \rVert_1
\end{equation}
where S is the empirical covariance matrix
$$
S = \frac{1}{n} \sum_{i=1}^n x_i x_i^T
$$

Denote
$$g(X) = -\log \det X + trace(SX).
$$
The optimization is writen as
$$
\min g(X) + \lambda \lVert X \rVert_1
$$
A popular to solve this optimization is at each step, $g(X)$ is approximated by a quadratic function, then a new direction is calculated by solving a simpler optimization.

Notice that by Taylor expansion
$$
\log det(X_t + \Delta) = \log \det(X_t) + trace(X_t^{-1} \Delta) + \frac{1}{2} trace(X_t^{-1} \Delta X_t^{-1} \Delta).
$$
We have
$$
g(X_t + \Delta) = trace((S- W_t) \Delta) + \frac{1}{2} trace(W_t \Delta W_t \Delta) - \log \det X_t + trace(S X_t)
$$
where $W_t = X_t^{-1}$.

Now solving the following optimization to find the direction $\Delta$
$$
\min_{\Delta} g(X_t + \Delta) + \lambda \lVert X + \Delta \rVert_1.
$$
Here, $g(X_t + \Delta)$ has the quaratic form, thus the optimization is expected to be easy to solve.

$$
\bar{g}_{(X_t)}(\Delta) = trace((S - W_t)\Delta) + \frac{1}{2} trace(W_t \Delta W_t \Delta) - \log \det X_t + trace(S X_t)
$$

Solve the Newton direction
$$
D_t = argmin_{\Delta} \,\, \bar{g}_{(X_t)}(\Delta) + \lVert X_t + \Delta \rVert_1   \quad\quad  (2)
$$


**The optimization will look like:**

For t = 0,1,..
    1. Compute $W_t = X_t^{-1}$
    2. Solve $$D_t = argmin_{\Delta} \,\, \bar{g}_{(X_t)}(\Delta) + \lVert X_t + \Delta \rVert_1$$
    3. Using Armijo rule to find the step-size $\alpha$
    3. Update $X_{t+1} =  X_t + \alpha D_t$

"""


# Helper functions to compute the objective
def _objective(emp_cov, precision, L=None, regularize_param=0.5):
    """
    Evaluation of the graph-lasso objective function.

    The objective function is made of a shifted scaled version of the
    normalized log-likelihood (i.e. its empirical mean over the samples) and a
    penalisation term to promote sparsity.

    Parameters:
        emp_cov (numpy.ndarray, required): Empirical covariance matrix of size \
            n_feature x n_features.
        precision (numpy.ndarray, required): The precision matrix at the t-th step of \
            size n_feature x n_features.
        L (numpy.ndarray, optional): The triangular matrix obtained from Cholesky \
            decomposition of the precision matrix. Defaults to None.
        regularize_param (float, optional): Regularization parameter. Defaults to 0.5.

    Returns:
        cost (float): The cost function value.
    """
    if L is None:
        cost = np.sum(precision * emp_cov.T) - fast_logdet(precision)
    else:
        cost = np.sum(precision * emp_cov.T) - 2 * np.sum(np.log(np.diag(L)))

    cost += regularize_param * np.abs(precision).sum()
    return cost


# Find the stepsize and return the new estimate
def armijo_step(
    emp_cov, X, W, D, current_cost, regularize_param, beta=0.5, sigma=0.499
):
    """
    Parameters:
        emp_cov (numpy.ndarray, required): Empirical covariance matrix of size n_feature x n_features.
        X (numpy.ndarray, required): The precision matrix at the t-th step.
        W (numpy.ndarray, required): The covariance matrix at the t-th step, W = inv(X).
        D: The Newton direction found from solving the quadratic approximation optimization.
        current_cost: Value of the objective function at X.
        regularize_param (float, required): Regularization parameter to promote sparsity.
        beta (float, optional): Decreasing rate. Defaults to 0.5.
        sigma (float, optional): Measure the closeness. Defaults  to 0.499.

    Returns:
        alpha: Armijo stepsize.
        new_X: New precision matrix at the (t+1) iteration.
        new_W: New covariance matrix at the (t+1) iteration.
        L: Lower triangular matrix from Cholesky decomposition of (X + alpha D).
    """
    i = 0
    current_l1_cost = np.abs(X).sum()

    while True:
        # Armijo stepsize
        # alpha = power(beta,i)
        # get the updated precision matrix
        # new_X = X + alpha*D
        # Get the lower triangular matrix from Cholesky decomposition
        # L = np.linalg.cholesky(new_X)
        # Check the positive definiteness of new_X
        # if (np.diag(L)>0).all():
        # Compute the new loss function
        #    new_cost = _objective(emp_cov, new_X, L, regularize_param)
        #    delta = np.sum((emp_cov - W) * D.T) + regularize_param*np.abs(X+D).sum() - regularize_param * current_l1_cost
        #    if new_cost <= current_cost + alpha*sigma*delta:
        #        break

        try:
            # Armijo stepsize
            alpha = power(beta, i)
            # get the updated precision matrix
            new_X = X + alpha * D
            L = np.linalg.cholesky(new_X)
            if (np.diag(L) > 0).all():
                # Compute the new loss function
                new_cost = _objective(emp_cov, new_X, L, regularize_param)
                delta = (
                    np.sum((emp_cov - W) * D.T)
                    + regularize_param * np.abs(X + D).sum()
                    - regularize_param * current_l1_cost
                )
                if new_cost <= current_cost + alpha * sigma * delta:
                    break
        except np.linalg.linalg.LinAlgError as err:
            print("error:", str(err))

        i += 1

    L_inv = inv(L)
    new_W = dot(L_inv.T, L_inv)

    return new_X, new_W, L, new_cost


def soft_threshold(z, r):
    """
    Parameters:
        z(array_like, required): <description>
        r(<description>,required): <description>

    Returns:
        soft_threshold: numpy.ndarray.
    """
    return np.sign(z) * np.maximum(abs(z) - r, 0)


def approximate_newton_direction(
    X, W, emp_cov, max_newton_iter, regularize_param, inner_tolerance
):
    r"""
    Solve the Newton direction

    $$
    D_t = argmin_{\Delta} \,\, trace((S - W_t)\Delta) + \frac{1}{2} trace(W_t \Delta W_t \Delta) - \log \det X_t + \lVert X_t + \Delta \rVert_1   \quad\quad  (3)
    $$

    Parameters:
        X: Precision matrix at the t-th step, X : n_features x n_features.
        W: Covariance matrix at the t-th step.
        emp_cov: Empirical covariance matrix.
        max_newton_iter: Maximum iteration for solving Newton direction.
        regularize_param: Regularization parameter to promote sparsity.
        inner_tolerance: Tolerance to stop the algorithm.

    Returns:
        D: Newton direction.
        U = D*W.
    """

    _, n_features = emp_cov.shape
    D = np.zeros([n_features, n_features])
    U = np.zeros([n_features, n_features])
    D_update = D
    U_update = U

    # Store cost values
    inner_costs = []
    current_cost = regularize_param * np.abs(X).sum()
    inner_costs.append(current_cost)

    for _ in range(max_newton_iter):
        # Partition the variables into fixed and free set
        gradient_X = emp_cov - W
        free_set = (gradient_X.__abs__() > regularize_param - inner_tolerance) | (
            X != 0
        )
        for (i, j) in zip(np.where(free_set)[0], np.where(free_set)[1]):
            if i <= j:
                a = W[i, j] * W[i, j]
                if i != j:
                    a = a + W[i, i] * W[j, j]
                # b = emp_cov[i,j] - W[i,j] + dot(W[:,i],dot(D,W[:,j]))
                # U = D*W
                b = emp_cov[i, j] - W[i, j] + dot(W[:, i], U[:, j])
                c = X[i, j] + D[i, j]
                mu = -c + soft_threshold(
                    c - (1.0 * b) / a, (1.0 * regularize_param) / a
                )
                # Update the coordinate (i,j) of U and D
                D_update[i, j] = D[i, j] + mu
                D_update[j, i] = D[j, i] + mu
                U_update[i, :] = U[i, :] + mu * W[j, :]
                U_update[j, :] = U[j, :] + mu * W[i, :]

        D = D_update
        U = U_update
        WD = dot(W, D)
        new_cost = (
            np.sum((emp_cov - W) * D.T)
            + 0.5 * np.sum(WD * WD.T)
            + regularize_param * np.abs(X + D).sum()
        )

    return D


def graph_quic(
    emp_cov,
    cov_init=None,
    regularize_param=0.1,
    beta=0.5,
    sigma=0.5,
    tol=1e-12,
    inner_tol=1e-5,
    max_iter=50,
    max_Newton_iter=100,
    verbose=False,
):

    """
    Paramters:
        emp_cov (numpy.ndarray, required): Empirical covariance from which to compute the \
            covariance estimate.
        cov_init (numpy.ndarray, optional): The initial guess for the covariance. Defaults to None.
        regularize_param (float, optional): The regularization parameter. Defaults to 0.1.
        beta (float, optional): The decreasing rate in the armijo step. Defaults to 0.5.
        sigma (float, optional): The measure of the closeness in the Newton step. Defaults to 0.5.
        tol (float, optional): The tolerance to declare convergence: if the dual gap goes below \
            this value, iterations are stopped. Defaults to 1e-12.
        inner_tol (float, optional): Defaults to 1e-5.
        max_iter (integer, optional): The maximum number of iterations. Defaults to 50.
        max_Newton_iter (integer, optional): The max iteration in the Newton step. Defaults to 100.
        verbose (integer, optional): If verbose is True, the objective function and the difference \
            between two consecutive costs are printed at each iteration. Defaults to False.

    Returns:
        tuple: (covariance, precision, costs, iteration).
    """

    _, n_features = emp_cov.shape

    if regularize_param == 0:
        estimated_precision = inv(emp_cov)
        costs = n_features - fast_logdet(estimated_precision)
        return estimated_precision, emp_cov, costs, 0

    # Initial estimate of the covariance
    if cov_init is None:
        estimated_covariance = emp_cov.copy()
    else:
        estimated_covariance = cov_init.copy()

    estimated_covariance *= 0.95
    diagonal = emp_cov.flat[:: n_features + 1]
    estimated_covariance.flat[:: n_features + 1] = diagonal

    estimated_precision = inv(estimated_covariance)

    costs = []
    current_cost = _objective(emp_cov, estimated_precision, None, regularize_param)
    costs.append(current_cost)

    for iteration in range(max_iter):
        D = approximate_newton_direction(
            estimated_precision,
            estimated_covariance,
            emp_cov,
            max_Newton_iter,
            regularize_param,
            inner_tol,
        )

        estimated_precision, estimated_covariance, L, current_cost = armijo_step(
            emp_cov,
            estimated_precision,
            estimated_covariance,
            D,
            current_cost,
            regularize_param,
            0.5,
            0.499,
        )
        costs.append(current_cost)
        cost_diff = current_cost - costs[iteration]
        if verbose:
            print(
                (
                    "[graph_quic] Iteration % 3i, cost % 3.2e, difference %.3e"
                    % (iteration, current_cost, cost_diff)
                )
            )
        if np.abs(cost_diff) < tol * np.abs(current_cost):
            break

    return estimated_precision, estimated_covariance, costs, iteration


class GraphQUIC(EmpiricalCovariance):
    """
    GraphQUIC
    """

    def __init__(
        self,
        regularize_param=0.1,
        beta=0.5,
        sigma=0.5,
        tol=1e-5,
        inner_tol=1e-5,
        max_iter=50,
        max_Newton_iter=100,
        verbose=False,
        assume_centered=False,
    ):
        """
            Init method for calss GraphQUIC
        """

        self.regularize_param = regularize_param
        self.beta = beta
        self.sigma = sigma
        self.tol = tol
        self.inner_tol = inner_tol
        self.max_iter = max_iter
        self.max_Newton_iter = max_Newton_iter
        self.verbose = verbose
        self.assume_centered = assume_centered
        # The base class needs this for the score method
        self.store_precision = True

    """
    def fit(self, X):

        # Covariance does not make sense for a single feature
        X = check_array(X, ensure_min_features=2, ensure_min_samples=2,
                        estimator=self)

        if self.assume_centered:
            self.location_ = np.zeros(X.shape[1])
        else:
            self.location_ = X.mean(0)
        emp_cov = empirical_covariance(X, assume_centered=self.assume_centered)

        self.precision_, self.covariance_, self.costs, self.n_iter_ = graph_quic(emp_cov, regularize_param=self.regularize_param,
                                                                                 beta=self.beta, sigma=self.sigma, tol=self.tol,
                                                                                 inner_tol=self.inner_tol, max_iter=self.max_iter,
                                                                                 max_Newton_iter=self.max_Newton_iter, verbose=self.verbose)

        return self
    """

    def fit(self, X):
        """
        Paramters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features) \
            Set of samples, where n_samples is the number of samples and n_features is the number of features.

        Returns:
            self: Trained instance of GraphQUIC.
        """
        # Covariance does not make sense for a single feature
        X = check_array(X, ensure_min_features=2, ensure_min_samples=2, estimator=self)

        if self.assume_centered:
            self.location_ = np.zeros(X.shape[1])
        else:
            self.location_ = X.mean(0)
        emp_cov = empirical_covariance(X, assume_centered=self.assume_centered)

        try:
            self.precision_, self.covariance_, self.costs, self.n_iter_ = graph_quic(
                emp_cov,
                regularize_param=self.regularize_param,
                beta=self.beta,
                sigma=self.sigma,
                tol=self.tol,
                inner_tol=self.inner_tol,
                max_iter=self.max_iter,
                max_Newton_iter=self.max_Newton_iter,
                verbose=self.verbose,
            )
        except FloatingPointError:
            done = True
            shrinkage_th = 0.1
            shrunk_cov = None
            while done:
                try:
                    shrunk_cov = shrunk_covariance(emp_cov, shrinkage=shrinkage_th)
                    (
                        self.precision_,
                        self.covariance_,
                        self.costs,
                        self.n_iter_,
                    ) = graph_quic(
                        shrunk_cov,
                        regularize_param=self.regularize_param,
                        beta=self.beta,
                        sigma=self.sigma,
                        tol=self.tol,
                        inner_tol=self.inner_tol,
                        max_iter=self.max_iter,
                        max_Newton_iter=self.max_Newton_iter,
                        verbose=self.verbose,
                    )
                    done = False
                except FloatingPointError:
                    shrinkage_th = shrinkage_th + 0.1

                if shrinkage_th >= 1:
                    done = False

        return self
