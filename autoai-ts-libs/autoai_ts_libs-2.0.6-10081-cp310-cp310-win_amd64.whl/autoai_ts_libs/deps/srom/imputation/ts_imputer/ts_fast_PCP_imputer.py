# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2019 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: ts fast pcp imputer
   :synopsis: ts fast pcp imputer.

.. moduleauthor:: SROM Team
"""


import numpy as np
from scipy.sparse.linalg import svds
from scipy.interpolate import interp1d
from autoai_ts_libs.deps.srom.imputation.ts_imputer.ts_mul_var_base_imputer import TSMulVarBaseImputer


class TSFastPCPImputer(TSMulVarBaseImputer):
    """
    An univariate imputation for timeseries.
    Transformer obeys Scikit-learn interface and implements modified FastPCP
    algorithm.

    Algorithm:
        A updated version of Fast-PCP data imputation algorithm, which does not
        require any mandatory parameter to be specified. Automatic parameter
        selection should be fine in the majority of cases.
        This class implements modified FastPCP algorithm originally described in:
        "Fast principal component pursuit via alternating minimization",
        by Rodriguez and Wohlberg, 2013.
        https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6738015
        Note, the original paper has a typo, which was fixed in the next one:
        "An incremental principal component pursuit algorithm via projections
         onto the L1 ball", where the objective function is:
            0.5 * |L + S - D|^2_fro + lambda * |S|_1.
        We extended the objective to ElasticNet one:
            0.5 * |L + S - D|^2_fro + lambda * |S|_1 + 0.5 * mu * |S|^2_fro.
        Our modifications:
        - rank = max(1, round(math.sqrt(min(D.shape))))
        - parameter lambda = 1.0 / sqrt(max(D.shape))
        - many iterations until a stop-condition is met.
        - the objective function is ElasticNet instead of Lasso.
        We take a timeseries and place it progressively in a square matrix
        row by row. This matrix is subsequently called a data matrix.
        Essentially:
        - missing values are filled in by matrix completion, i.e. by finding
          a low-rank approximation to the incomplete data matrix.
        - initially, the gaps are filled by linear interpolation between
          observable values; this makes up a starting "point" in optimization
          procedure.
        - missing end values are filled initially by the first or the last
          observable values respectively.
    Return:
        imputed univariate timeseries or (optionally) its low-rank approximation.
    TODO and open questions:
    (1) Compute matrix size based on the number of non-missing values.
    (2) Better goodness-of-fit measure, namely, do not consider those entries
        roughly imputed by linear interpolation. Will it really help?
    (3) automatically find the best lambda amd mu.
    Open questions:
    (*) What would be the best way to skip imputation of the long sub-sequence
        of all-missing values?
    (*) We assume that all values in timeseries (observable or missing) are
        are sampled uniformly on time axis. If this is not the case, what should
        we do?
    """

    def __init__(
        self, rank: int = 0, return_approx: bool = False, enable_debug: bool = False
    ):
        """
        Args:
        rank: rank of low-rank approximation;
              automatically selected if rank <= 0.
        return_approx: if true, returns low-rank approximation of
                       the input timeseries, otherwise imputed one.
        enable_debug: flag enables recording of debugging information.
        """
        super().__init__(enable_debug)
        fname = TSFastPCPImputer.__init__.__name__
        if not isinstance(rank, int):
            raise TypeError(ErrorAt(fname, "parameter 'rank' must be integer"))
        if not isinstance(return_approx, bool):
            raise TypeError(ErrorAt(fname, "parameter 'return_approx' must be boolean"))
        if not isinstance(enable_debug, bool):
            raise TypeError(ErrorAt(fname, "parameter 'enable_debug' must be boolean"))
        self.rank = rank
        self.return_approx = return_approx
        cls_name = self.__class__.__name__
        self.debug = dict({"imputer": cls_name}) if enable_debug else None

    def get_debug_info(self) -> dict:
        return self.debug if isinstance(self.debug, dict) else dict()

    def _impute(self, X: np.ndarray) -> np.ndarray:
        """Does the actual imputation."""
        fname = TSFastPCPImputer._impute.__name__
        if not isinstance(X, np.ndarray):
            raise TypeError(ErrorAt(fname, "expects timeseries as Numpy array"))
        if X.shape != (X.size, 1):
            raise ValueError(
                ErrorAt(fname, "expects timeseries as 2D array of size Nx1")
            )

        N = int(X.size)
        if N < MinTimeseriesLength():
            raise ValueError(ErrorAt(fname, "input timeseries is too short"))
        finite_X = np.isfinite(X)
        num_valid_entries = np.count_nonzero(finite_X)
        if num_valid_entries == N:
            return X  # nothing to do

        if 3 * num_valid_entries <= N:
            raise ValueError(
                ErrorAt(
                    fname,
                    "Too many missing observations in timeseries, imputation is unreliable",
                )
            )
        # Creates a data matrix by laying out the timeseries progressively,
        # row by row. Data matrix's shape is chosen close to square.
        ncols = max(int(round(np.floor(np.sqrt(float(X.size))))), int(1))
        nrows = int((X.size + ncols - 1) // ncols)
        D = np.full((nrows, ncols), fill_value=np.nan, dtype=np.float64)
        D.ravel()[: X.size] = X.ravel()

        # Roughly impute the data matrix at missing entries.
        D_repaired = LinearInterpolation(D)

        # Compute low-rank approximation of the data matrix.
        D = self._fast_pcp(D_repaired)

        # Drop the alignment piece.
        Xt = D.ravel()[: X.size].reshape(-1, 1)

        if self.debug:
            self.debug["low_rank_series"] = Xt.copy()

        if not self.return_approx:
            # Impute retaining the old values wherever possible.
            Xt = np.where(finite_X, X, Xt)
        return Xt

    def _fast_pcp(self, D: np.ndarray) -> np.ndarray:
        """
        Modified FastPCP algorithm. This implementation augments the algorithm
        from Lasso to ElasticNet.
        :param D: a feasible data matrix with all valid (!) entries, i.e.
                  all the missing entry values must be filled somehow,
                  not necessarily in an optimal way.
        :return: low-rank approximation to input data matrix.
        """
        fname = TSFastPCPImputer._fast_pcp.__name__
        # Minimum number of iterations:
        min_iter_num = int(50)
        # Number of alternating iterations improving L and S given current rank:
        num_iters = max(int(1), min_iter_num, int(D.size))
        # Desired rank of of the low-rank approximation:
        if self.rank >= 1:  # user-supplied
            rank = max(int(1), min(self.rank, min(D.shape) - 1))
        else:  # automatic
            rank = max(int(1), round(float(np.ceil(np.sqrt(min(D.shape))))))
        # Threshold on relative change of objective function:
        change_thr = float(np.power(np.finfo(np.float64).eps, 1.0 / 3.0))

        # Initialize statistics.
        enable_debug = self.debug is not None
        profile = list() if enable_debug else None

        L = D.copy()
        S = np.full_like(D, fill_value=0.0)

        if not np.all(np.isfinite(D)):
            raise ValueError(ErrorAt(fname, "expects data matrix (roughly) imputed"))

        L_best, gof_best, lam_best = None, np.finfo(float).max, 1.0

        # Find the best low-rank approximation for several reasonable choices of
        # regularization parameter lambda. Solution obtained for the previous
        # lambda is used as a starting 'point' for the current one. Note, we
        # begin from the least regularized solution.
        # TODO: would it be better, to loop from 1 down to 0.001?
        # TODO: most regularized solution is closer to global minimum from the beginning?
        for lam in [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]:
            mu = 0.5 * lam  # scale of ElasticNet term
            fobj_prev, fobj, iter_count = -1.0, -1.0, int(0)

            # Iterate until convergence.
            while iter_count < num_iters:
                iter_count += 1
                # Partial SVD.
                U, Diag, Vt = svds(D - S, k=rank)

                # Current low-rank approximation.
                L = U.dot(np.diag(Diag).dot(Vt))

                # Shrinkage, see the paper for details.
                S = D - L
                S = np.sign(S) * np.maximum(0, np.abs(S) - lam) / (1.0 + mu)

                # Compute the objective function and check the stop-condition.
                fobj = (
                    0.5 * (np.linalg.norm(D - L - S, "fro") ** 2)
                    + lam * np.sum(np.abs(S))
                    + 0.5 * mu * np.dot(S.ravel(), S.ravel())
                )
                if (
                    iter_count >= min_iter_num
                    and fobj_prev >= fobj
                    and fobj_prev - fobj <= change_thr * fobj_prev
                ):
                    break
                fobj_prev = fobj

            # Update the best goodness-of-fit and the corresponding entities.
            diff = np.abs(L - D).ravel()
            kth = min(round(0.75 * diff.size), diff.size - 1)
            gof = np.partition(diff, kth)[kth]
            # gof = np.nanmedian(np.abs(L - D))
            if (gof < gof_best) or (L_best is None):
                L_best, lam_best, gof_best = L.copy(), lam, gof

            # Update statistics.
            if enable_debug:
                profile.append((fobj, iter_count, lam, gof))

            # |S|=0 indicates too large lambda.
            if np.sum(np.abs(S)) < float(np.sqrt(np.finfo(float).eps)):
                break

        if enable_debug:
            self.debug.update(
                {"L": L_best, "rank": rank, "fobj": profile, "lam_best": lam_best}
            )
        return L_best


def ErrorAt(function_name: str, message: str) -> str:
    """Prints error message about an issue in certain function."""
    return "error in function {:s}(): {:s}".format(str(function_name), str(message))


def MinTimeseriesLength() -> int:
    """Returns the minimal length of timeseries eligible for imputation."""
    return int(10)


def LinearInterpolation(X: np.ndarray) -> np.ndarray:
    """
    Repairs data array (timeseries) by linear interpolation at missing entries.
    The result can be used as an initial solution to some elaborated imputer.
    N O T E, the array will be flattened before interpolation and restored
    back to its original shape afterwards.
    :param X: input data array.
    :return: linearly interpolated data array (timeseries).
    """
    fname = LinearInterpolation.__name__
    vec = X.ravel()  # flattened data array
    idx = np.where(np.isfinite(vec))[0]  # indices of valid entries

    if not (idx.size >= 2 and 3 * idx.size > X.size):
        raise ValueError(ErrorAt(fname, "Too many missing observations in timeseries"))
    # Other possible "fill_values": "extrapolate", np.nanmedian(vec)
    interpolator = interp1d(
        x=idx,
        y=vec[idx],
        kind="linear",
        bounds_error=False,
        fill_value=(vec[idx[0]], vec[idx[-1]]),
    )
    X_repaired = interpolator(np.arange(0, X.size))

    if not np.all(np.isfinite(X_repaired)):
        raise ValueError(ErrorAt(fname, "linear interpolation failed"))
    return X_repaired.reshape(X.shape)
