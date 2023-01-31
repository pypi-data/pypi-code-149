# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: smart_classification
   :synopsis: SROM SmartClassification.

.. moduleauthor:: SROM Team
"""
import logging
import pandas as pd
import numpy as np
from sklearn import preprocessing
from autoai_ts_libs.deps.srom.auto.auto_classification import AutoClassification
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.auto.base_auto import SROMAutoPipeline
from autoai_ts_libs.deps.srom.utils.pipeline_utils import get_pipeline_description, get_pipeline_name
from sklearn.exceptions import NotFittedError
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
from sklearn.utils import check_X_y
from autoai_ts_libs.deps.srom.utils.classification_helper import prepare_classifier
import time
from sklearn.metrics.pairwise import pairwise_distances


LOGGER = logging.getLogger(__name__)

class SmartClassification(BaseEstimator, ClassifierMixin):
    """
    The class for performing the smart-classification in SROM using a well tested heuristic "Bottom-Up". \
    The model_stages in this class have already been setup from the benchmark results. \
    (link from the results of experimentation can be put here.)


    Example:
    >>> from autoai_ts_libs.deps.srom.classification.smart_classification import SmartClassification
    >>> X = pd.DataFrame([[1,2,3,2,2,1,2][5,6,3,2,5,3,1]])
    >>> y = [1,0,0,0,1,0,1]
    >>> sc = SmartClassification()
    >>> sc.fit(X,y)
    """

    def _measure_imbalance(self, df, data_col, label_col, class_imbalance_ratio=0.2):
        """
            Method to measure the imbalance.
        """
        # NOTE: References
        # https://arxiv.org/pdf/1901.10173.pdf,
        # https://github.com/jasonyanglu/BI3/blob/master/calculate_bi3.py
        try:
            # get the data and labels from data
            df = df.dropna()
            if df.shape[0] == 0:
                raise Exception("The data size is zero after dropping NAs.")
            data = df[data_col].to_numpy()
            label = df[label_col].values.tolist()

            # Encode labels
            le = preprocessing.LabelEncoder()
            le.fit(label)
            label_ = le.transform(label)

            # Checks for only 2 classes otherwise inform the user
            if len(set(label_)) != 2:
                raise Exception(
                    "The "
                    + str(label_col)
                    + " column does not have exactly 2 classes. There should be only 2 classes in the data."
                )

            class_0 = label_.tolist().count(0)
            class_1 = label_.tolist().count(1)
            class_ratio = float(class_0) / float(class_1)

            bi_3 = 1
            # logging info to suggest users that class imbalance is not there.
            if (class_ratio < class_imbalance_ratio) or (
                class_ratio > (1 / class_imbalance_ratio)
            ):
                # setting majority and minority class
                if class_ratio > 1:
                    majority_class = 0
                    minority_class = 1
                else:
                    majority_class = 1
                    minority_class = 0

                min_num = label_.tolist().count(minority_class)
                maj_num = label_.tolist().count(majority_class)
                r = maj_num / min_num

                # getting indices for majority and minority class index
                maj_idx = [i for i, x in enumerate(label_) if x == majority_class]
                min_idx = [i for i, x in enumerate(label_) if x == minority_class]
                min_data = data[min_idx]

                # training a classifier
                k = min(4, data.shape[0] - 1)
                knn = NearestNeighbors(n_neighbors=k + 1)
                knn.fit(data)
                _, neightbor_index = knn.kneighbors(min_data)

                # removing the index for the point itself is chosen as neighbor
                neightbor_index = neightbor_index[:, 1:]

                prob_majority = []
                prob_minority = []
                # iterating over each minority data points.
                for i in range(min_num):
                    # finding intersections between neighbors and majority indices.
                    majority_in_neighbors = len(
                        list(set(neightbor_index[i]).intersection(maj_idx))
                    )
                    majority_prob = majority_in_neighbors / k

                    # if the case when all the k neighbors are majority class
                    if majority_in_neighbors == k:
                        # finding the nearby points until we find a nearby minority point.
                        data_point = min_data[i].reshape(1, -1)
                        neighbor_dist = pairwise_distances(data_point, data)
                        neighbors_in_order = np.argsort(neighbor_dist)[0].tolist()
                        minority_near = [
                            i
                            for i, x in enumerate(label_[neighbors_in_order])
                            if x == minority_class
                        ][1]
                        majority_prob = (minority_near - 1) / minority_near
                    prob_majority.append(majority_prob)

                # calculating minority class probability
                prob_minority = [(1 - i) for i in prob_majority]
                prob_majority = np.array(prob_majority)
                prob_minority = np.array(prob_minority)

                ibi_3 = (
                    r * prob_minority / (prob_majority + r * prob_minority)
                    - prob_minority
                )
                bi_3 = np.mean(ibi_3)
            return bi_3
        except Exception as e:
            raise Exception(
                "Imbalance Impact Validator failed with the following message: "
                + str(e)
            )

    def __init__(
        self,
        level="default",
        save_prefix_ac="smart_classification_output_",
        save_prefix_aic="smart_imbalanced_classification_output_",
        execution_platform="spark_node_random_search",
        mode="auto",
        cv=5,
        scoring=None,
        stages=None,
        execution_time_per_pipeline=2,
        num_options_per_pipeline_for_random_search=10,
        num_option_per_pipeline_for_intelligent_search=30,
        total_execution_time=10,
        param_grid=None,
        n_leaders_for_ensemble=5,
        class_imbalance_threshold=0.2,
        predict_proba_adjust=True
    ):  
        """
        Parameters:
            level (String): Level of exploration (default or comprehensive).
            save_prefix (string): String prefix for the output save file.
            execution_platform (string): Platform for execution from autoai_ts_libs.deps.srom pipeline. Supports spark also.
            cv (int): Value of 'k' in K-crossvalidation. This parameters is used from the sklearn \
                    function GridSearchCV. \
                    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
            scoring (String, function): The value that defines the metrics for scoring the paths. \
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
            mode (string): default='auto' determine class type automatically. User specified options
            mode= '1' binary classification
            mode ='2' binary class imbalance
            mode = '3' multi class
            mode = '4' multi class imbalance.
            n_leaders_for_ensemble = 5
            class_imbalance_threshold=0.2
        """

        self.n_leaders_for_ensemble = n_leaders_for_ensemble
        self.mode = mode
        self.class_imbalance_threshold = class_imbalance_threshold

        ###
        self.level = (level,)
        self.save_prefix_ac = save_prefix_ac
        self.save_prefix_aic = save_prefix_aic
        self.execution_platform = execution_platform
        self.cv = cv
        self.scoring = scoring
        self.stages = stages
        self.execution_time_per_pipeline = execution_time_per_pipeline
        self.num_options_per_pipeline_for_random_search = (
            num_options_per_pipeline_for_random_search
        )
        self.num_option_per_pipeline_for_intelligent_search = (
            num_option_per_pipeline_for_intelligent_search
        )
        self.total_execution_time = total_execution_time
        self.param_grid = param_grid
        self.predict_proba_adjust = predict_proba_adjust

        # label encoder
        # self.label_encoder = None
        self.auto_classification = None
        self._evn_config = None

        if self.mode not in ["1", "2", "3", "4", "auto"]:
            raise ValueError("The input value of mode is not supported")

    def set_environment_config(self, evn_conf):
        """
        The configuration setting for lithops, code engine, cloud function
        """
        self._evn_config = evn_conf

    def _test_predict_proba(self, X, y):
        """
        Test to see if best estimator calling predict_proba() runs fine. If not, update
        the last stage of best estimator with CalibratedClassifierCV wrapped.
        """
        try:
            self.auto_classification.predict_proba(X)
            return True
        except AttributeError:
            self._update_best_estimator()
            self.auto_classification.fit(X, y)  # refit the updated best estimator
            self.auto_classification.predict_proba(X)
            return True
        except Exception as e:
            return False

    def _update_best_estimator(self):
        """
        Update the last stage/layer of best estimator with CalibratedClassifierCV wrapped.
        """
        from sklearn.calibration import CalibratedClassifierCV

        LOGGER.debug("Update the last stage of best estimator with CalibratedClassifierCV wrapped.")
        self.auto_classification.best_estimator_so_far.steps[-1] = \
            (self.auto_classification.best_estimator_so_far.steps[-1][0],
             CalibratedClassifierCV(self.auto_classification.best_estimator_so_far.steps[-1][-1]))

    def fit(self, X, y):
        """
        Train the best model on the given data.

        Parameters:
            X (numpy array): Training dataset. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.
            y (list of strings or encoded numpy parray): Class labels to be used. Can be string or int\
                If target_column is added in the meta data, it is \
                used from there. shape = [n_samples]

        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline.
        """
        X, y = check_X_y(X, y)
        if any(isinstance(elem, str) for elem in np.unique(y)):
            raise NotImplementedError("We do not support Label Encoder")
            # self.label_encoder = LabelEncoder()
            # y = self.label_encoder.fit_transform(y)

        # check class 1 is minory class, else raise an execption
        num_classes = len(np.unique(y))
        LOGGER.info("number of classes: {}".format(num_classes))

        if num_classes != 2:
            if num_classes == 1:
                raise NotImplementedError("Samples from single classes are detected")
            else:
                raise NotImplementedError(
                    "Smart Classification is not supporting more than two classes"
                )

        if self.mode == "auto":
            if isinstance(X, pd.DataFrame):
                X = X.to_numpy()
            Xdf = pd.DataFrame(X, columns=list(range(X.shape[1])))
            Xdf["label"] = y
            data_col = list(range(X.shape[1]))
            label_col = "label"
            bi_3 = self._measure_imbalance(
                Xdf, data_col, label_col, self.class_imbalance_threshold
            )
            LOGGER.info("class imbalance: " + str(bi_3) +
                        ", class imbalance threshold: " + str(self.class_imbalance_threshold))
            del Xdf
            if bi_3 > self.class_imbalance_threshold:
                self.mode = "2"
            else:
                self.mode = "1"

        if self.mode in ["1", "2"]:
            if self.mode == "1":
                save_prefix = self.save_prefix_ac
                LOGGER.info("Running AutoClassification.")
            else:
                save_prefix = self.save_prefix_aic
                LOGGER.info("Running AutoImbalancedClassification.")

                # apply additional check here
                if np.sum(y) > (len(y) / 2.0):
                    raise NotImplementedError(
                        "Smart Classification need class label 1 as a minority samples in order to work imbalanced classifier to work properly"
                    )

            self.auto_classification = prepare_classifier(
                self.mode,
                level=self.level,
                save_prefix=save_prefix,
                execution_platform=self.execution_platform,
                cv=self.cv,
                scoring=self.scoring,
                stages=self.stages,
                execution_time_per_pipeline=self.execution_time_per_pipeline,
                num_options_per_pipeline_for_random_search=self.num_options_per_pipeline_for_random_search,
                num_option_per_pipeline_for_intelligent_search=self.num_option_per_pipeline_for_intelligent_search,
                total_execution_time=self.total_execution_time,
                param_grid=self.param_grid,
            )
            if isinstance(X, pd.DataFrame):
                X = X.to_numpy()

            if self._evn_config:
                self.auto_classification.set_environment_config(self._evn_config)

            self.auto_classification.automate(X, y)
            self.auto_classification.fit(X, y)

            if self.predict_proba_adjust:
                if not self._test_predict_proba(X, y):
                    raise Exception("predict_proba() is not supported for the best estimator.")
                else:
                    LOGGER.debug("Testing predict_proba() succeeded.")

        elif self.mode == "3":
            raise NotImplementedError(
                "Smart classification currently does not support multi-class prediction"
            )
        elif self.mode == "4":
            raise NotImplementedError(
                "Smart classification currently does not support multi-class imbalanced prediction"
            )
        else:
            raise ValueError("mode must be one of '1','2','3' or '4'")
        return self

    def predict(self, X):
        """
        Predict the class labels.
        
        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        if self.auto_classification:
            if self.mode in ["1", "2"]:
                if isinstance(X, pd.DataFrame):
                    X = X.to_numpy()
                return self.auto_classification.predict(X)
            elif self.mode == "3":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class prediction"
                )
            elif self.mode == "4":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class imbalanced prediction"
                )
            else:
                raise ValueError("mode must be one of '1','2','3' or '4'")
        else:
            raise NotFittedError("Model is not trained")

    def predict_proba(self, X):
        """
        Predict the class probabilites.
        
        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        if self.auto_classification:
            if self.mode in ["1", "2"]:
                if isinstance(X, pd.DataFrame):
                    X = X.to_numpy()
                return self.auto_classification.predict_proba(X)
            elif self.mode == "3":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class prediction"
                )
            elif self.mode == "4":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class imbalanced prediction"
                )
            else:
                raise ValueError("mode must be one of '1','2','3' or '4'")
        else:
            raise NotFittedError("Model is not trained")

    def get_best_estimator(self):
        """
        Retrive best estimator.
        Returns:
            scikit-learn classifier
        """
        if self.auto_classification:
            if self.mode in ["1", "2"]:
                return self.auto_classification.best_estimator_so_far
            elif self.mode == "3":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class prediction"
                )
            elif self.mode == "4":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class imbalanced prediction"
                )
            else:
                raise ValueError("mode must be one of '1','2','3', '4' or 'auto'")
        else:
            raise NotFittedError("Model is not trained")

    def get_best_score(self):
        """
        Retrive best score.
        Returns:
            number
        """
        if self.auto_classification:
            if self.mode in ["1", "2"]:
                return self.auto_classification.best_score_so_far
            elif self.mode == "3":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class prediction"
                )
            elif self.mode == "4":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class imbalanced prediction"
                )
            else:
                raise ValueError("mode must be one of '1','2','3', '4' or 'auto'")
        else:
            raise NotFittedError("Model is not trained")

    def get_experiment_info(self):
        """
        Returns all the details of smart classification experiment.
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
        if self.auto_classification:
            if self.mode in ["1", "2"]:
                auto_object = self.auto_classification
            elif self.mode == "3":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class prediction"
                )
            elif self.mode == "4":
                raise NotImplementedError(
                    "Smart classification currently does not support multi-class imbalanced prediction"
                )
            else:
                raise NotFittedError("mode must be one of '1','2','3' or '4'")

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
            experiment_info["best_pipeline_info"] = auto_object.get_model_info()
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

                # temporary shifted to make pyspark 3.1.1 to work
                import dill
                import base64

                dmp = dill.dumps(path["best_estimator"])
                encoded_dmp = base64.encodebytes(dmp).decode("UTF-8")
                cur["pipeline_instance"] = encoded_dmp
                experiment_info["optimization_info"]["results"].append(cur)

        return experiment_info
