from sklearn.ensemble import IsolationForest
import numpy as np
import numbers
import numpy as np
from scipy.sparse import issparse
from warnings import warn

from sklearn.utils import (
    check_random_state,
)

class TSIsolationForest(IsolationForest):
    """
    This implementation bring additional capability:
    1) use warm start capability and then add more tree of the data passed inside predict
    2) generate the ts based isolation forest score (TBA)
    """
    def __init__(
        self,
        n_estimators=100,
        max_samples="auto",
        contamination="auto",
        max_features=1.0,
        bootstrap=False,
        n_jobs=None,
        random_state=None,
        verbose=0,
        warm_start=True,
        n_extra_estimators=100,
        sample_train=False,
        fit_mode='offline',
        ):
        super().__init__(
            n_estimators=n_estimators,
            max_samples=max_samples,
            contamination=contamination,
            max_features=max_features,
            bootstrap=bootstrap,
            n_jobs=n_jobs,
            random_state=random_state,
            verbose=verbose,
            warm_start=warm_start)
        self.n_extra_estimators=n_extra_estimators
        self.sample_train = sample_train
        self.fit_mode = fit_mode

    def adjusted_fit(self, X, y=None, sample_weight=None):
        """
        Fit estimator.
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The input samples. Use ``dtype=np.float32`` for maximum
            efficiency. Sparse matrices are also supported, use sparse
            ``csc_matrix`` for maximum efficiency.
        y : Ignored
            Not used, present for API consistency by convention.
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted.
        Returns
        -------
        self : object
            Fitted estimator.
        """
        X = self._validate_data(X, accept_sparse=["csc"])
        if issparse(X):
            # Pre-sort indices to avoid that each individual tree of the
            # ensemble sorts the indices.
            X.sort_indices()

        # ensure that max_sample is in [1, n_samples]:
        n_samples = X.shape[0]
        if y is None:
            rnd = check_random_state(self.random_state)
            y = rnd.uniform(size=X.shape[0])
        
        if self.contamination != "auto":
            if not (0.0 < self.contamination <= 0.5):
                raise ValueError(
                    "contamination must be in (0, 0.5], got: %f" % self.contamination
                )

        if isinstance(self.max_samples, str):
            if self.max_samples == "auto":
                max_samples = min(256, n_samples)
            else:
                raise ValueError(
                    "max_samples (%s) is not supported."
                    'Valid choices are: "auto", int or'
                    "float"
                    % self.max_samples
                )

        elif isinstance(self.max_samples, numbers.Integral):
            if self.max_samples > n_samples:
                warn(
                    "max_samples (%s) is greater than the "
                    "total number of samples (%s). max_samples "
                    "will be set to n_samples for estimation."
                    % (self.max_samples, n_samples)
                )
                max_samples = n_samples
            else:
                max_samples = self.max_samples
        else:  # float
            if not 0.0 < self.max_samples <= 1.0:
                raise ValueError(
                    "max_samples must be in (0, 1], got %r" % self.max_samples
                )
            max_samples = int(self.max_samples * X.shape[0])

        self.max_samples_ = max_samples
        max_depth = int(np.ceil(np.log2(max(max_samples, 2))))
        super()._fit(
            X,
            y,
            max_samples,
            max_depth=max_depth,
            sample_weight=sample_weight,
            #check_input=False,
        )

        if self.contamination == "auto":
            # 0.5 plays a special role as described in the original paper.
            # we take the opposite as we consider the opposite of their score.
            self.offset_ = -0.5
            return self

        # else, define offset_ wrt contamination parameter
        self.offset_ = np.percentile(self.score_samples(X), 100.0 * self.contamination)
        return self        
        
    def fit(self, X, y=None):
        """
        """
        if self.fit_mode == 'offline':
            self.adjusted_fit(X, y)
        if self.sample_train:
            if len(X) <= 2000:
                self.X_sample_ = X.copy()
            else:
                index = np.random.choice(X.shape[0], 2000, replace=False)
                self.X_sample_ = X[index,:]
        return self
        
        
    def _incremental_fit(self, X):
        """
        """
        if self.warm_start:
            self.fit(X)
        else:
            raise Exception('Error')

    def decision_function(self, X):
        """
        """
        if self.fit_mode == 'online':
            if self.sample_train:
                tmpX = np.concatenate([self.X_sample_,X])
            else:
                tmpX = X.copy()
            self.adjusted_fit(tmpX)
            ans = self.score_samples(X) - self.offset_
            return ans
        elif self.fit_mode == 'offline':
            past_offset=self.offset_
            past_n_estimators_ = self.n_estimators
            self.n_estimators = self.n_estimators + self.n_extra_estimators
            if self.sample_train:
                tmpX = np.concatenate([self.X_sample_,X])
            else:
                tmpX = X.copy()
            self._incremental_fit(tmpX)
            ans = self.score_samples(X) - self.offset_
            for _ in range(self.n_extra_estimators):
                self.estimators_.pop(-1)
                self.estimators_features_.pop(-1)
            self.n_estimators = past_n_estimators_
            self.offset_ = past_offset
        return ans
