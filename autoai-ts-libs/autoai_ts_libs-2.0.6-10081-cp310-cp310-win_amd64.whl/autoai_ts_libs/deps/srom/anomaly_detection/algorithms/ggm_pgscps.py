# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: ggm_pgscps
   :synopsis: PGSCPS - Projected Gradient Sparsity Constrained Precision Selection.

.. moduleauthor:: SROM Team
"""
import numpy as np
from numpy.linalg import inv
from numpy.linalg import cholesky

from sklearn.utils.extmath import fast_logdet
from sklearn.covariance import empirical_covariance
from sklearn.covariance import EmpiricalCovariance
from sklearn.covariance import shrunk_covariance


def objective(emp_cov, X, reg=0):
    """
    Compute the objective function.

    Parameterss:
        emp_cov (datatype, required): <description>
        X (pandas.Dataframe or numpy.ndarray, required): <description>
        reg (integer, optional): <description>
    
    Returns:
        cost: <description>
    """
    cost = (
        np.trace(np.dot(emp_cov, X))
        - fast_logdet(X)
        + 0.5 * reg * np.trace(np.dot(X.transpose(), X))
    )
    return cost


def objective_g(emp_cov, X, reg=0):
    """
    Compute the objective gradient.

    Paramters:
        emp_cov (datatype, required): <description>
        X (pandas.Dataframe or numpy.ndarray, required): <description>
        reg (integer, optional): <description>
    
    Returns:
        grad: Gradient of objective function at current iterate.
        invX(pandas.Dataframe or numpy.ndarray): Inverse of current iterate X.
    """
    invX = inv(X)
    invX = (0.5) * (invX + invX.T)
    grad = emp_cov - invX + reg * X
    return grad, invX


def l0_projection(X, sparsity):
    """
    Project matrix X onto l0 constraint.

    Parameters:
        X (pandas.Dataframe or numpy.ndarray, required): <description>
        sparsity (datatype, required): <description>
    
    Returns:
        A: <description>
        support: <description>
    """
    n_samples = X.shape[0]
    A = np.zeros(n_samples ** 2)
    # Get off-diagonal entries
    X_off = X - np.diag(np.diag(X))

    # Project onto l0 ball
    sorted_indices = X_off.ravel().__abs__().argsort()
    support = sorted_indices[
        int(n_samples ** 2 - sparsity) :
    ]  # int added to convert indec to integer
    A[support] = X_off.ravel()[support]
    A = A.reshape([n_samples, n_samples])
    A = A + np.diag(np.diag(X))
    return A, support


"""
Inner conjugate gradient method. 

Should eventually be replaced with something that explicitly takes advantage 
of the sparse input matrices when doing multiplications, 
as this will greatly improve the running time.
"""


def cg(support, invX, grad, reg=0, K=10, eps_r=1e-4):
    """
    Conjugate Gradient method

    Parameters:
        support (datatype, required): Indices of nonzeros to define subspace.
        invX (pandas.Dataframe or numpy.ndarray, required): Inverse of current iterate X.
        grad (datatype, required): Gradient of objective function at current iterate.
        reg (integer, optional): <description>. Defaults to 0.
        K (integer, optional): Maximum number of loops to carry out (stopping criterion). Defaults to 10.
        eps_r (float, optional): Residual norm tolerance (stopping criterion). Defaults to 1e-4.

    Returns:
        D <datatype> : <description>
        q <datatype> : <description>
    """

    n = grad.shape[0]
    g = np.zeros(n ** 2)
    x = np.zeros(n ** 2)

    # restrict gradient g to support
    g[support] = grad.ravel()[support]

    R = (-1.0) * g.reshape([n, n])

    # initialize the cg loop
    k = 0
    r = R.ravel()
    q = r

    while k <= min(n ** 2, K) and np.max(r) > eps_r:
        Q = q.reshape([n, n])

        # can be optimized by blocking:
        Y = np.dot(invX, np.dot(Q, invX))
        y = np.zeros(n ** 2)
        y[support] = Y.ravel()[support]
        # regularizer term
        y = y + reg * q
        rtr = np.dot(r, r)
        qty = np.dot(q, y)
        alpha = rtr / qty
        x = x + alpha * q
        r_next = r - alpha * y
        beta = np.dot(r_next, r_next) / rtr
        q = r_next + beta * q
        r = r_next
        k = k + 1

    # print('CG Iters: ' + repr(k))
    D = x.reshape([n, n])
    XiDXi = np.dot(np.dot(invX, D), invX)
    prod = np.zeros(n ** 2)
    prod[support] = XiDXi.ravel()[support]
    q = (
        np.dot(g, x)
        + 0.5 * np.trace(np.dot(D, prod.reshape([n, n])))
        + 0.5 * reg * np.trace(np.dot(D.transpose(), D))
    )

    return D, q


def line_search(
    emp_cov, X, D, q, f, sparsity, reg=0, eta=0.1, alpha_min=1e-8, gamma=0.5
):
    """
    <description>

    Paramters:
        emp_cov (datatype, required): Empirical covariance matrix.
        X (datatype, required): Current iterate.
        D (datatype, required): Search direction from Newton method.
        q (datatype, required): Quadratic predicted decrease.
        f (datatype, required): Current true objective value.
        sparsity (datatype, required): Number of off-diagonal nonzeros.
        reg (datatype, required) : <description>
        alpha_min (datatype, required): Minimum step size.
        gamma (datatype, required): Shrinkage factor for backtracking.
        eta (datatype, required): Fraction of decrease.

    Returns:
        Xnew <datatype>: <description>
        fnew <datatype>: <description>
        alpha <datatype>: <description>
        support <datatype>: <description>
    """

    stop = 0
    alpha = 1
    while not stop and alpha > alpha_min:
        Xnew = X + alpha * D
        Xnew, support = l0_projection(Xnew, sparsity)
        fnew = objective(emp_cov, Xnew, reg=reg)
        if fnew - f < eta * q:
            # Is this PD?
            chol_X = 1
            try:
                L = cholesky(Xnew)
            except Exception as _:
                chol_X = 0

            if chol_X and all(np.diag(L)) > 1e-12:
                stop = 1
            else:
                alpha = gamma * alpha

        else:
            alpha = gamma * alpha

    # end while
    return Xnew, fnew, alpha, support


"""
The "main" method. See the working paper (coming soon)
"""


def orthant_method(
    X0,
    emp_cov,
    sparsity,
    eta=0.001,
    gamma=0.5,
    alpha_min=1e-4,
    eps_outer=1e-4,
    eps_cg=1e-4,
    outer_maxiter=30,
    cg_maxiter=None,
    reg=0,
):
    """
    <description>

    Parameters:
        X0 (numpy.ndarray, required): Initial iterate.
        emp_cov (numpy.ndarray, required): Empirical covariance.
        sparsity (integer, required): number of nonzero off-diagonal entries in solution.
        eta (float, optional): <description>. Defaults to 0.001.
        gamma (float, optional): <description>. Defaults to 0.05.
        alpha_min (float, optional): Smallest allowable step size. Defaults to 1e-4.
        eps_outer (float, optional): Multi-purpose stopping criterion. Defaults to 1e-4.
        eps_cg (float, optional): Stopping criterion for cg method. Defaults to 1e-4.
        outer_maxiter (integer, optional): Maximum number iterations for orthant method. Defaults to 30.
        cg_maxiter (integer, optional): Maximum number iterations for cg method. Defaults to None.

    Returns:
        tuple : (<description>, <description>)
    """

    if cg_maxiter is None:
        cg_maxiter = (X0.shape[0]) ** 2

    # a silly correction in case homotopy method does weird stuff
    sparsity = sparsity - X0.shape[0]
    sparsity = max(X0.shape[0] + 2, 2 * (sparsity / 2))

    # Insist that the initial point be feasible:
    X, old_support = l0_projection(X0, sparsity)
    eigs, _ = np.linalg.eig(X)
    mineig = min(eigs)
    if mineig <= 0:
        print("Correcting spectrum.")
        X = X + (abs(mineig) + eps_outer) * np.eye(X0.shape[0])

    # What's the initial objective value?
    f = objective(emp_cov, X, reg=reg)

    # Start the outer loop.
    itr = 1
    stop = 0
    prevX = X
    fnew = np.inf

    while not stop:
        # Compute the gradient at the current iterate.
        grad, invX = objective_g(emp_cov, X, reg=reg)
        _, grad_support = l0_projection(grad, sparsity)

        # Get steepest descent iterate.
        sd_step = X - grad

        # A precaution in case of asymmetry
        sd_step = 0.5 * (sd_step + sd_step.T)

        # Project onto sparsity constraints
        sd_step, support = l0_projection(sd_step, sparsity)
        support = list(set(support) | set(old_support) | set(grad_support))

        # Solve the cg-subproblem over the support subspace
        cg_iters = 10
        # cg_iters = cg_maxiter
        D, q = cg(support, invX, grad, reg=reg, K=cg_iters, eps_r=eps_cg)

        # D = sd_step
        D = 0.5 * (D + D.T)
        # Do a TR-ish line search in the direction D:
        Xnew, fnew, alpha, support = line_search(
            emp_cov,
            X,
            D,
            q,
            f,
            sparsity,
            eta=eta,
            reg=reg,
            alpha_min=alpha_min,
            gamma=gamma,
        )

        # stopping criteria
        stop_quad = 0
        if itr >= outer_maxiter:
            stop = 1
            # print('Iteration count exceeded.')
        elif abs(q) < eps_outer:
            stop_quad = 1
            # print('Stationary point found within stopping criteria.')

        # possibly correct early ls termination with gradient step
        alpha2 = 1
        if (alpha <= alpha_min and not stop) or stop_quad:
            # print('Entered rectification stage')
            Xnew, fnew, alpha2, support = line_search(
                emp_cov,
                X,
                -1 * grad,
                0,
                f,
                sparsity,
                eta=0,
                reg=reg,
                alpha_min=alpha_min,
                gamma=gamma,
            )

        # more stopping criteria
        if alpha <= alpha_min and alpha2 <= alpha_min:
            stop = 1
            # print('Step size is too small.')
        elif abs(f - fnew) < eps_outer and itr > 1:
            stop = 1
            # print('Insufficient function decrease found.')

        # prepare for next iteration
        if alpha2 > alpha_min:
            X = (Xnew + Xnew.T) / 2.0
            f = fnew
            old_support = support

        prevX = X

        # iterate
        itr = itr + 1

    return X, f


def homotopy_wrapper(S, sparsity, reg=0, num_runs=5, eps_weak=1e-4, eps_strong=1e-4):
    """
    <description>

    Paramters:
        S (pandas.Dataframe or numpy.ndarray, required): <description>
        sparsity (scalar, required):  Sparsity.
        reg (integer,optional): Defaults to 0.
        num_runs (integer,optional): Defaults to 5.
        eps_weak (float,optional): Defaults to 1e-4.
        eps_strong (float,optional): Defaults to 1e-4.
        
    Returns:
        tuple
    """
    sparsity_vec = np.linspace(S.shape[0], sparsity, num_runs + 1)
    # sparsity_vec = np.linspace(3*sparsity,sparsity,num_runs+1)
    X = np.eye(S.shape[0])
    eps = eps_weak

    for level in sparsity_vec:
        level = np.ceil(level)
        # print('New sparsity level: ' + repr(level))
        if level >= sparsity:
            eps_outer = eps_strong

        X, f = orthant_method(X, S, level, reg=reg, eps_outer=eps)

    return X, f


class GraphPgscps(EmpiricalCovariance):
    """
    GraphPgscps
    """

    def __init__(
        self,
        sparsity=10,
        eta=0.001,
        gamma=0.5,
        alpha_min=1e-4,
        eps_outer=1e-4,
        eps_cg=1e-4,
        outer_maxiter=100,
        cg_maxiter=None,
        reg=0,
    ):
        """
            Init method for class GraphPgscps
        """
        self.sparsity = sparsity
        self.eta = eta
        self.gamma = gamma
        self.alpha_min = alpha_min
        self.eps_outer = eps_outer
        self.eps_cg = eps_cg
        self.outer_maxiter = outer_maxiter
        self.cg_maxiter = cg_maxiter
        # The base class needs this for the score method
        self.store_precision = True
        self.reg = reg

    """
    def fit(self, X):
        emp_cov = empirical_covariance(X)

        self.precision_, self.objective_function_value = homotopy_wrapper(emp_cov, sparsity = self.sparsity, reg = self.reg)
        self.covariance_ =  np.linalg.inv(self.precision_)
        return self
    """

    # new method
    def fit(self, X):
        """
        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features),
            Set of samples, where n_samples is the number of samples and n_features is the number of features.

        Returns:
            self: trained instance of GraphPgscps
        """
        emp_cov = empirical_covariance(X)
        self.location_ = np.mean(X, axis=0)

        try:
            self.precision_, self.objective_function_value = homotopy_wrapper(
                emp_cov, sparsity=self.sparsity, reg=self.reg
            )
            self.covariance_ = np.linalg.inv(self.precision_)
        except FloatingPointError:
            done = True
            shrinkage_th = 0.1
            shrunk_cov = None
            while done:
                try:
                    shrunk_cov = shrunk_covariance(emp_cov, shrinkage=shrinkage_th)
                    self.precision_, self.objective_function_value = homotopy_wrapper(
                        shrunk_cov, sparsity=self.sparsity, reg=self.reg
                    )
                    self.covariance_ = np.linalg.inv(self.precision_)
                    done = False
                except FloatingPointError:
                    shrinkage_th = shrinkage_th + 0.1

                if shrinkage_th >= 1:
                    done = False

        return self
