# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: smart_regression
   :synopsis: SROM SmartRegression.

.. moduleauthor:: SROM Team
"""
import logging
from autoai_ts_libs.deps.srom.auto.auto_regression import AutoRegression
from autoai_ts_libs.deps.srom.utils.pipeline_utils import get_pipeline_description, get_pipeline_name
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.exceptions import NotFittedError
import time

LOGGER = logging.getLogger(__name__)


class SmartRegression(BaseEstimator, RegressorMixin):
    """
    The class for performing the smart-Regression in SROM using a well tested heuristic "Bottom-Up". \
    The model_stages in this class have already been setup from the benchmark results. \
    (link from the results of experimentation can be put here.)

    Parameters:
        level (String): Level of exploration (default or comprehensive).
        save_prefix (string): String prefix for the output save file.
        execution_platform (string): Platform for execution from autoai_ts_libs.deps.srom pipeline. Supports spark also.
        cv (int): Value of 'k' in K-crossvalidation. This parameters is used from the sklearn \
                function GridSearchCV. \
                https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
        scoring (Sting, function): The value that defines the metrics for scoring the paths. \
                Can be a string if sklearn defined metrics used. Can be a function if a user \
                defined metric is used. This parameters is used from the sklearn function GridSearchCV. \
                https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
        stages (list of list of estimators): A list of list containing the transformer and \
                estimator tuples for customizing the preconfigured smart pipeline.
        execution_time_per_pipeline (int): Integer value denoting time (minutes) of execution \
                per path (path: combination of estimators and transformers)
        total_execution_time (int): Total execution time (minutes) for the smart Regression pipeline.
        num_options_per_pipeline_for_random_search (int): Integer value denoting number \
                of parameters to use while performing randomized param search in *which* rounds.
        num_option_per_pipeline_for_intelligent_search: Integer value denoting number of \
                parameters to use while performing more intelligent param search in *which* rounds.
        n_estimators_for_pred_interval = 30, 
        bootstrap_for_pred_interval = True, 
        aggr_type_for_pred_interval = 'median', 
        n_leaders_for_ensemble = 5


    Example:
    >>> from autoai_ts_libs.deps.srom.regression.smart_regression import SmartRegression
    >>> X = pd.DataFrame([[1,2,3,2,2,1,2][5,6,3,2,5,3,1]])
    >>> y = [1,0,0,0,1,0,1]
    >>> sr = SmartRegression()
    >>> sr.fit(X,y)
    """

    def __init__(
        self,
        level="default",
        save_prefix="smart_regression_output_",
        execution_platform="spark_node_random_search",
        cv=5,
        scoring=None,
        stages=None,
        execution_time_per_pipeline=2,
        num_options_per_pipeline_for_random_search=10,
        num_option_per_pipeline_for_intelligent_search=30,
        total_execution_time=10,
        param_grid=None,
        n_estimators_for_pred_interval=30,
        bootstrap_for_pred_interval=True,
        aggr_type_for_pred_interval="median",
        n_leaders_for_ensemble=5,
    ):

        self.level=level
        self.save_prefix=save_prefix
        self.execution_platform=execution_platform
        self.cv=5
        self.scoring=scoring
        self.stages=stages
        self.execution_time_per_pipeline=execution_time_per_pipeline
        self.num_options_per_pipeline_for_random_search=num_options_per_pipeline_for_random_search
        self.num_option_per_pipeline_for_intelligent_search=num_option_per_pipeline_for_intelligent_search
        self.total_execution_time=total_execution_time
        self.param_grid=param_grid
        self.n_leaders_for_ensemble = n_leaders_for_ensemble
        self.bootstrap_for_pred_interval = bootstrap_for_pred_interval
        self.aggr_type_for_pred_interval = aggr_type_for_pred_interval
        self.n_estimators_for_pred_interval = n_estimators_for_pred_interval
        self._evn_config = None
        
        self.auto_regression = AutoRegression(
            level=level,
            save_prefix=save_prefix,
            execution_platform=execution_platform,
            cv=cv,
            scoring=scoring,
            stages=stages,
            execution_time_per_pipeline=execution_time_per_pipeline,
            num_options_per_pipeline_for_random_search=num_options_per_pipeline_for_random_search,
            num_option_per_pipeline_for_intelligent_search=num_option_per_pipeline_for_intelligent_search,
            total_execution_time=total_execution_time,
            param_grid=param_grid,
        )        

    def set_environment_config(self, evn_conf):
        """
        The configuration setting for lithops, code engine, cloud function
        """
        self._evn_config = evn_conf
        
    def fit(self, X, y):
        """
        Train the best model on the given data.

        Parameters:
            X (pandas dataframe or numpy array): Training dataset. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                If target_column is added in the meta data, it is \
                used from there. shape = [n_samples] or [n_samples, n_output]

        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline.
        """
        LOGGER.info("Running Auto Regression.")
    
        if self._evn_config:
            self.auto_regression.set_environment_config(self._evn_config)
        
        self.auto_regression.automate(X, y)
        LOGGER.info("Train an ensemble model using Voting strategy.")
        self.auto_regression.fit_voting_ensemble(
            X,
            y,
            self.n_leaders_for_ensemble,
            n_estimators=self.n_estimators_for_pred_interval,
            aggr_type=self.aggr_type_for_pred_interval,
        )
        return self

    def predict(self, X):
        """
        Predict the regression scores etc. using \
        the trained model pipeline.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        return self.auto_regression.predict_voting_ensemble(X)

    def predict_proba(self, X):
        """
        Predict the class interval etc. using \
        the trained model pipeline.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        return self.auto_regression.predict_voting_ensemble_interval(X)

    def get_best_estimator(self):
        """
        Retrive best estimator.
        Returns:
            scikit-learn pipeline/srom estimator based pipeline
        """
        if self.auto_regression:
            if self.auto_regression.voting_ensemble_estimator:
                return self.auto_regression.voting_ensemble_estimator
            else:
                raise NotFittedError("Votting Ensemble Model is not trained")
        else:
            raise NotFittedError("Model is not trained")

    def get_experiment_info(self):
        """
        Returns all the details of smart regression experiment.
        Return object:
        {
          experiment_id: <>,
          train_data: X,
          train_labels: y,
          start_time: <>,
          end_time: <>,
          execution_time: <>,    
          best_pipeline_info: {
              model_name: <>,
              model_family: <>,
              model_description: <>,
              attributes: {
                  "key": "value"
              }
          },
          optimization_info: {
              stages: <>,
              hyperparameters: <>,
              results: [
                    {
                        pipeline_id: <>,
                        model_name: <>,
                        model_family: <>,
                        model_description: <>,
                        pipeline_instance: <>,
                        params: <>,
                        score: <>,
                        round: <>,
                        start_time: <>,
                        end_time:<>,
                        execution_time: <>,
                        cross_validation_results: <>
                    }
                ]
          }
        }
        """
        experiment_info = {}
        if self.auto_regression.voting_ensemble_estimator:
            # experiment_info = self.auto_regression.voting_ensemble_estimator.get_model_info()
            auto_object = self.auto_regression

            experiment_info["experiment_id"] = auto_object.best_path_info[
                "experiment_id"
            ]
            experiment_info["start_time"] = time.strftime(
                "%Y-%m-%dT%H:%M:%SZ",
                time.gmtime(auto_object.best_path_info["start_time"]),
            )
            experiment_info["end_time"] = time.strftime(
                "%Y-%m-%dT%H:%M:%SZ",
                time.gmtime(auto_object.best_path_info["end_time"]),
            )
            experiment_info["execution_time"] = auto_object.best_path_info[
                "execution_time"
            ]
            experiment_info[
                "best_pipeline_info"
            ] = auto_object.voting_ensemble_estimator.get_model_info()
            experiment_info["optimization_info"] = {}
            experiment_info["optimization_info"]["stages"] = auto_object.stages
            experiment_info["optimization_info"][
                "hyperparameters"
            ] = auto_object.param_grid
            # experiment_info['optimization_info']['results'] = auto_object.best_path_info["best_path"]
            experiment_info["optimization_info"]["results"] = []
            for path in auto_object.best_path_info["best_path"]:
                cur = {}
                cur["pipeline_id"] = path["estimator_id"]
                cur["model_name"] = get_pipeline_name(path["best_estimator"])
                cur["model_family"] = "sklearn"
                cur["model_description"] = get_pipeline_description(
                    path["best_estimator"]
                )
                cur["params"] = path["best_params"]
                cur["score"] = path["best_score"]
                cur["round"] = path["round"]
                cur["start_time"] = time.strftime(
                    "%Y-%m-%dT%H:%M:%SZ", time.gmtime(path["start_time"])
                )
                cur["end_time"] = time.strftime(
                    "%Y-%m-%dT%H:%M:%SZ", time.gmtime(path["end_time"])
                )
                cur["execution_time"] = path["execution_time"]

                import dill
                import base64

                dmp = dill.dumps(path["best_estimator"])
                encoded_dmp = base64.encodebytes(dmp).decode("UTF-8")
                cur["pipeline_instance"] = encoded_dmp
                experiment_info["optimization_info"]["results"].append(cur)

        return experiment_info
