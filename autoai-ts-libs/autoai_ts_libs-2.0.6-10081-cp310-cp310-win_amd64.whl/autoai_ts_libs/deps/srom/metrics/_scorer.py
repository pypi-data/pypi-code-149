import numpy as np
from sklearn.metrics._scorer import _BaseScorer, _cached_call
from functools import partial
from sklearn.metrics import make_scorer

class _MixtureModelScorer(_BaseScorer):
    """
    ??? add doc string ??? or explanation
    """

    def __call__(self, estimator, X, y_true=None, sample_weight=None):
        """Evaluate predicted target values for X relative to y_true.
        Parameters
        ----------
        estimator : object
            Trained estimator to use for scoring. Must have a predict_proba
            method; the output of that is used to compute the score.
        X : {array-like, sparse matrix}
            Test data that will be fed to estimator.predict.
        y_true : array-like
            Gold standard target values for X.
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.
        Returns
        -------
        score : float
            Score function applied to prediction of estimator on X.
        """
        return self._score(partial(_cached_call, None), estimator, X, y_true,
                           sample_weight=sample_weight)


    def _score(self, method_caller, estimator, X, y_true=None, sample_weight=None):
        return method_caller(estimator, "score", X, score_option=self._score_func)

    def __repr__(self):
        kwargs_string = "".join(
            [", %s=%s" % (str(k), str(v)) for k, v in self._kwargs.items()]
        )
        return "make_scorer(%s%s%s%s)" % (
            self._score_func,
            "" if self._sign > 0 else ", greater_is_better=False",
            self._factory_args(),
            kwargs_string,
        )
    
    
def make_mixture_scorer(score_func, *, greater_is_better=True, **kwargs):
    sign = 1 if greater_is_better else -1
    return _MixtureModelScorer(score_func, sign, kwargs)

bic_scorer = make_mixture_scorer('bic')
aic_scorer = make_mixture_scorer('aic')

CustomSCORERS = dict(
    bic=bic_scorer,
    aic=aic_scorer,
)
