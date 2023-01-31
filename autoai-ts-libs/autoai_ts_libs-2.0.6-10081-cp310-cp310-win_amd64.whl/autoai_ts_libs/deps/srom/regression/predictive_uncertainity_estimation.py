# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: predictive_uncertainity_estimation
   :synopsis: Contains PredictiveUncertaintyEstimator class.

.. moduleauthor:: SROM Team
"""
import warnings
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import BaggingRegressor
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.utils.pipeline_utils import get_pipeline_description, get_pipeline_name
from autoai_ts_libs.deps.srom.utils.estimator_utils import get_estimator_meta_attributes

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


class PredictiveUncertaintyEstimator(BaseEstimator, RegressorMixin):
    """
    The class for performing the predictive uncertainity in SROM. \
    It is generic and boot strap based method for predicting uncertainity \
    interval using single models or set of different models. \

    Parameters:
        base_model (list of pipelines): This list contains a set of top-k performing pipeline.
        n_estimators (int): for boot strap.
        bootstrap (bool): True or False
        aggr_type (string): median or mean
        n_jobs (number of parallel job to run) = -1 
    """

    def __init__(
        self,
        base_model=[],
        n_estimators=200,
        bootstrap=True,
        aggr_type="median",
        n_jobs=None,
        random_state = 32
    ):

        if len(base_model) == 0:
            base_model = [Pipeline([("linearreg", LinearRegression())])]

        self.base_model = base_model
        self.bagging_models = []
        self.n_estimators = n_estimators
        self.bootstrap = bootstrap
        self.aggr_type = aggr_type
        self.n_jobs = n_jobs

        for idx,item in enumerate(self.base_model):

            if self.n_jobs is None:
                # check n_jobs in item, and update n_jobs to be None
                for step in item.steps:
                    if "n_jobs" in step[-1].get_params():
                        step[-1].set_params(n_jobs=None)

            if random_state is None:
                tmp_rand_state = None
            else:
                tmp_rand_state = idx
            
            self.bagging_models.append(
                BaggingRegressor(
                    base_estimator=item,
                    n_estimators=self.n_estimators,
                    bootstrap=self.bootstrap,
                    n_jobs=self.n_jobs,
                    random_state=tmp_rand_state
                )
            )

    def fit(self, X, y):
        for item in self.bagging_models:
            item.fit(X, y)
        return self

    def _get_result_summary(self, tmp_result):
        if self.aggr_type == "mean":
            result = tmp_result.apply(lambda x: np.mean(x), axis=1)
        elif self.aggr_type == "median":
            result = tmp_result.apply(lambda x: np.median(x), axis=1)
        else:
            raise Exception("Not Supported")
        return result.values

    def predict(self, X):
        _prediction = []
        for item in self.bagging_models:
            for item_estimator in item.estimators_:
                _prediction.append(item_estimator.predict(X).flatten())
        result = pd.DataFrame(np.array(_prediction)).transpose()
        return self._get_result_summary(result)

    def predict_proba(self, X):
        return self.predict_interval(X)

    def predict_interval(self, X, percentile=95):
        _prediction = []
        for item in self.bagging_models:
            for item_estimator in item.estimators_:
                _prediction.append(item_estimator.predict(X).flatten())
        result = pd.DataFrame(np.array(_prediction)).transpose()
        lower_bound = result.apply(
            lambda x: np.percentile(x, (100 - percentile) / 2.), axis=1
        )
        upper_bound = result.apply(
            lambda x: np.percentile(x, 100 - (100 - percentile) / 2.), axis=1
        )
        result = pd.DataFrame([lower_bound, upper_bound]).transpose().values
        return result

    def get_model_info(self):
        """
        Retrive model information in the form of dictionary containing model_name,model_family and model_family.
        Returns:
            dict
        """
        model_family = "sklearn_ensemble_estimators"
        m_name = "bagging_regressor"
        m_description = []
        import re

        for ind, item in enumerate(self.bagging_models):
            base_estimator = item.base_estimator_
            attrs = None
            model_description = ""
            model_name = ""
            attrs = []
            if isinstance(base_estimator, Pipeline):
                model_description = model_description + get_pipeline_description(
                    base_estimator
                )
                model_name = (
                    model_name
                    + "bagging_"
                    + str(ind)
                    + "_("
                    + get_pipeline_name(base_estimator)
                    + "),"
                )
                for _est in item.estimators_:
                    last = _est.steps[-1]
                    vals = get_estimator_meta_attributes(last[1])
                    if vals:
                        attrs.append(vals)
            else:
                name = str(base_estimator)
                name = re.sub(r"\(.*\)", "", name, flags=re.S)
                name = name.lower()
                model_description = model_description + str(base_estimator)
                model_name = model_name + "bagging_" + str(ind) + "_" + name + ","
                for _est in item.estimators_:
                    vals = get_estimator_meta_attributes(_est)
                    if vals:
                        attrs.append(vals)

            data = {"model_name": model_name, "model_description": model_description}
            if attrs:
                data["attributes"] = attrs
            else:
                data["attributes"] = "cannot find/discover parameters"
            m_description.append(data)
        info = {
            "model_name": m_name,
            "model_family": model_family,
            "model_description": m_description,
        }
        return info
