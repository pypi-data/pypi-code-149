import warnings
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.utils.pipeline_utils import get_pipeline_description, get_pipeline_name
from autoai_ts_libs.deps.srom.utils.estimator_utils import get_estimator_meta_attributes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from abc import ABC, abstractmethod
import numpy as np

class EnsembleRegressor(BaseEstimator, RegressorMixin):
    """[summary]

    Args:
        BaseEstimator ([type]): [description]
        RegressorMixin ([type]): [description]
    """

    def __init__(
        self,
        base_model=[
            LinearRegression(),
            HuberRegressor(),
            MLPRegressor(),
            RandomForestRegressor(),
            GradientBoostingRegressor(),
        ],
        random_state=42,
    ):
        self.base_model = base_model
        self.random_state=random_state

    def fit(self, X, y):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]
        """
        
        self.mdl_error_ = []
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=min(10, len(X)),random_state=self.random_state)
        for mdl in self.base_model:
            mdl.fit(X_train, y_train)
            pred_ans = mdl.predict(X_test)
            mdl_mae = mean_absolute_error(y_test, pred_ans)
            self.mdl_error_.append(mdl_mae)
        
        return self
        
    @abstractmethod
    def predict(self, X):
        pass

class BestEnsembleRegressor(EnsembleRegressor):
    """
    """
    
    def fit(self, X, y):
        '''
        '''
        super(BestEnsembleRegressor, self).fit(X, y)
        self.min_index_ = self.mdl_error_.index(min(self.mdl_error_))
        self.trained_model = self.base_model[self.min_index_]
        self.trained_model.fit(X, y)
        return self

    def predict(self, X):
        '''
        '''
        return self.trained_model.predict(X)


class WeightedEnsembleRegressor(EnsembleRegressor):
    """
    """

    def fit(self, X, y):
        '''
        '''
        super(WeightedEnsembleRegressor, self).fit(X, y)
        if np.sum(self.mdl_error_) > 0:
            self.mdl_weight_ = [(np.sum(self.mdl_error_) - item)/np.sum(self.mdl_error_) for item in self.mdl_error_]
        else:
            self.mdl_weight_ = [1.0/len(self.mdl_error_) for item in self.mdl_error_]
        for mdl in self.base_model:
            mdl.fit(X, y)
        return self
    
    def predict(self, X):
        tmp_ans = []
        for mdl_index, mdl in enumerate(self.base_model):
            val=mdl.predict(X)
            if len(val.shape)==1:
                val=val.reshape(-1,1)
            tmp_ans.append(val*self.mdl_weight_[mdl_index])        
        tmp_ans = np.array(tmp_ans)
        return tmp_ans.sum(axis=0)
