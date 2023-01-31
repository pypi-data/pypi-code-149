from sklearn.covariance import MinCovDet
import numpy as np

class ExtendedMinCovDet(MinCovDet):
    """_summary_

    Args:
        MinCovDet (_type_): _description_
    """

    def __init__(
        self,
        *,
        store_precision=True,
        assume_centered=False,
        support_fraction=None,
        random_state=None,
        num_rows=10000,
        num_cols=50,
    ):
        """
            Init method
        """
        super(ExtendedMinCovDet, self).__init__(
            store_precision=store_precision,
            assume_centered=assume_centered,
            support_fraction=support_fraction,
            random_state=random_state,
        )
        self.num_rows = num_rows
        self.num_cols = num_cols

    def fit(self, X, y=None):
        """
            Fit estimator.
            Parameters:
                X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                    Set of samples, where n_samples is the number of samples and n_features is the number of features.
                y (pandas dataframe or numpy array, optional): Defaults to None.

            Returns:
                self: Trained instance of ExtendedIsolationForest. 

        """
        
        if X.shape[1] > self.num_cols:
            self.selected_columns_ = np.random.choice(np.arange(X.shape[1]),self.num_cols,replace=False)
        else:
            self.selected_columns_ = np.arange(X.shape[1])

        subset_X_ = X[:,self.selected_columns_]

        if X.shape[0] > self.num_rows:
            selected_row_ = np.random.choice(np.arange(X.shape[0]),self.num_rows,replace=False)
            subset_X_ = subset_X_[selected_row_,:]
            if y is not None:
                y = y[selected_row_,:]
        
        return super(ExtendedMinCovDet, self).fit(subset_X_, y)
        
    def score(self, X_test, y=None):
        """
        Score method 
        
        Parameters:
            X_test (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                    Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

            Returns:
                score.
        """
        X_test = X_test[:,self.selected_columns_]
        return super(ExtendedMinCovDet, self).score(X_test, y)
    
    def mahalanobis(self, X):
        """
        Mahalanbis method 
        
        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                    Set of samples, where n_samples is the number of samples and n_features is the number of features.

            Returns:
                mahalanobis.
        """
        X = X[:,self.selected_columns_]
        return super(ExtendedMinCovDet, self).mahalanobis(X)
   
    
