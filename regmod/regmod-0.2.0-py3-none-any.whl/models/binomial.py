"""
Binomial Model
"""
from typing import Callable, List, Tuple

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from scipy.stats import binom

from regmod.optimizer import msca_optimize

from .model import Model
from .utils import model_post_init


class BinomialModel(Model):
    param_names = ("p",)
    default_param_specs = {"p": {"inv_link": "expit"}}

    def attach_df(self, df: pd.DataFrame):
        super().attach_df(df)
        if not np.all((self.y >= 0) & (self.y <= 1)):
            raise ValueError("Binomial model requires observations to be "
                             "between zero and one.")
        self.mat[0], self.cmat, self.cvec = model_post_init(
            self.mat[0], self.uvec, self.linear_umat, self.linear_uvec
        )

    def objective(self, coefs: NDArray) -> float:
        """Objective function.
        Parameters
        ----------
        coefs : NDArray
            Given coefficients.
        Returns
        -------
        float
            Objective value.
        """
        inv_link = self.params[0].inv_link
        lin_param = self.params[0].get_lin_param(
            coefs, self.df, mat=self.mat[0]
        )
        param = inv_link.fun(lin_param)

        weights = self.weights*self.trim_weights
        obj_param = -weights * (
            self.y * np.log(param) +
            (1 - self.y) * np.log(1 - param)
        )
        return obj_param.sum() + self.objective_from_gprior(coefs)

    def gradient(self, coefs: NDArray) -> NDArray:
        """Gradient function.

        Parameters
        ----------
        coefs : NDArray
            Given coefficients.

        Returns
        -------
        NDArray
            Gradient vector.
        """
        mat = self.mat[0]
        inv_link = self.params[0].inv_link
        lin_param = self.params[0].get_lin_param(
            coefs, self.df, mat=self.mat[0]
        )
        param = inv_link.fun(lin_param)
        dparam = inv_link.dfun(lin_param)

        weights = self.weights*self.trim_weights
        grad_param = weights * (
            (param - self.y) / (param*(1 - param)) * dparam
        )

        return mat.T.dot(grad_param) + self.gradient_from_gprior(coefs)

    def hessian(self, coefs: NDArray) -> NDArray:
        """Hessian function.

        Parameters
        ----------
        coefs : NDArray
            Given coefficients.

        Returns
        -------
        NDArray
            Hessian matrix.
        """
        mat = self.mat[0]
        inv_link = self.params[0].inv_link
        lin_param = self.params[0].get_lin_param(
            coefs, self.df, mat=self.mat[0]
        )
        param = inv_link.fun(lin_param)
        dparam = inv_link.dfun(lin_param)
        d2param = inv_link.d2fun(lin_param)

        weights = self.weights*self.trim_weights
        hess_param = weights * (
            (self.y / param**2 + (1 - self.y) / (1 - param)**2) * dparam**2 +
            (param - self.y) / (param*(1 - param)) * d2param
        )

        scaled_mat = mat.scale_rows(hess_param)
        hess_mat = mat.T.dot(scaled_mat)
        hess_mat_gprior = type(hess_mat)(self.hessian_from_gprior())
        return hess_mat + hess_mat_gprior

    def jacobian2(self, coefs: NDArray) -> NDArray:
        """Jacobian function.

        Parameters
        ----------
        coefs : NDArray
            Given coefficients.

        Returns
        -------
        NDArray
            Jacobian matrix.
        """
        mat = self.mat[0]
        inv_link = self.params[0].inv_link
        lin_param = self.params[0].get_lin_param(
            coefs, self.df, mat=self.mat[0]
        )
        param = inv_link.fun(lin_param)
        dparam = inv_link.dfun(lin_param)
        weights = self.weights*self.trim_weights
        grad_param = weights * (
            (param - self.y) / (param*(1 - param)) * dparam
        )
        jacobian = mat.T.scale_cols(grad_param)
        hess_mat_gprior = type(jacobian)(self.hessian_from_gprior())
        jacobian2 = jacobian.dot(jacobian.T) + hess_mat_gprior
        return jacobian2

    def fit(self,
            optimizer: Callable = msca_optimize,
            **optimizer_options):
        """Fit function.

        Parameters
        ----------
        optimizer : Callable, optional
            Model solver, by default scipy_optimize.
        """
        super().fit(
            optimizer=optimizer,
            **optimizer_options
        )

    def nll(self, params: List[NDArray]) -> NDArray:
        return -(self.y*np.log(params[0]) + (1 - self.y)*np.log(1.0 - params[0]))

    def dnll(self, params: List[NDArray]) -> List[NDArray]:
        return [-(self.y/params[0] - (1 - self.y)/(1.0 - params[0]))]

    def d2nll(self, params: List[NDArray]) -> List[List[NDArray]]:
        return [[self.y/params[0]**2 + (1 - self.y)/(1.0 - params[0])**2]]

    def get_ui(self, params: List[NDArray], bounds: Tuple[float, float]) -> NDArray:
        p = params[0]
        n = self.y_sample_sizes
        return [binom.ppf(bounds[0], n=n, p=p),
                binom.ppf(bounds[1], n=n, p=p)]
