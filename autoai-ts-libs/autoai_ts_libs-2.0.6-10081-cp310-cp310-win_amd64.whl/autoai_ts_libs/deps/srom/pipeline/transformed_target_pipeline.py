from matplotlib.pyplot import step
from sklearn.pipeline import Pipeline
from sklearn.base import clone
from sklearn.utils import check_array
from sklearn.utils.validation import check_is_fitted
from sklearn.preprocessing import FunctionTransformer

class TransformedTarget(Pipeline):
    """
    Class which wraps sklearn's pipeline to accomodate transformers
    which modify both X and y. This transformation is required in
    Time Series modelling tasks.

    Parameters
    ----------
        steps (list of tuples): This is the list of tuples storing items
            in the pipeline. For eg.
                steps =  [('log', Log(...)),
                            ('xgboost', Xgboost(...))]
        We will add the steps here
    """

    def __init__(
        self,
        steps,
        *,
        transformer=None, 
        func=None, 
        inverse_func=None, 
        check_inverse=True,
        memory=None, 
        verbose=False
    ):
        self.transformer = transformer
        self.func = func
        self.inverse_func = inverse_func
        self.check_inverse = check_inverse
        super(TransformedTarget, self).__init__(steps,memory=memory,verbose=verbose)
        
    def _pre_fit(self, y):
        if self.transformer is not None and (self.func is not None or self.inverse_func is not None):
            raise ValueError(
                "'transformer' and functions 'func'/'inverse_func' cannot both be set."
            )
        elif self.transformer is not None:
            self.transformer_ = clone(self.transformer)
        else:
            if self.func is not None and self.inverse_func is None:
                raise ValueError(
                    "When 'func' is provided, 'inverse_func' must also be provided"
                )
            self.transformer_ = FunctionTransformer(
                func=self.func,
                inverse_func=self.inverse_func,
                validate=True,
                check_inverse=self.check_inverse,
            )
        self.transformer_.fit(y)
        
    def fit(self, X, y, **fit_params):
        y = check_array(
            y,
            accept_sparse=False,
            force_all_finite=True,
            ensure_2d=False,
            dtype="numeric",
            allow_nd=True,
        )

        # store the number of dimension of the target to predict an array of
        # similar shape at predict
        self._training_dim = y.ndim

        # transformers are designed to modify X which is 2d dimensional, we
        # need to modify y accordingly.
        if y.ndim == 1:
            y_2d = y.reshape(-1, 1)
        else:
            y_2d = y
        self._pre_fit(y_2d)

        # transform y and convert back to 1d array if needed
        y_trans = self.transformer_.transform(y_2d)
        # FIXME: a FunctionTransformer can return a 1D array even when validate
        # is set to True. Therefore, we need to check the number of dimension
        # first.
        if y_trans.ndim == 2 and y_trans.shape[1] == 1:
            y_trans = y_trans.squeeze(axis=1)

        super(TransformedTarget, self).fit(X, y_trans, **fit_params)
        return self
    
    
    def predict(self, X, **predict_params):
        """Predict using the base regressor, applying inverse.
        The regressor is used to predict and the `inverse_func` or
        `inverse_transform` is applied before returning the prediction.
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Samples.
        **predict_params : dict of str -> object
            Parameters passed to the `predict` method of the underlying
            regressor.
        Returns
        -------
        y_hat : ndarray of shape (n_samples,)
            Predicted values.
        """
        check_is_fitted(self)
        pred = super(TransformedTarget, self).predict(X, **predict_params)
        if pred.ndim == 1:
            pred_trans = self.transformer_.inverse_transform(pred.reshape(-1, 1))
        else:
            pred_trans = self.transformer_.inverse_transform(pred)
        if (
            self._training_dim == 1
            and pred_trans.ndim == 2
            and pred_trans.shape[1] == 1
        ):
            pred_trans = pred_trans.squeeze(axis=1)

        return pred_trans
