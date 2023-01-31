# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: auto_classification
   :synopsis: Auto Classification class.

.. moduleauthor:: SROM Team
"""
import os
import time
import warnings
import uuid
import numpy as np
from operator import itemgetter
from multiprocessing import cpu_count

from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis,
    QuadraticDiscriminantAnalysis,
)
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.kernel_approximation import (
    RBFSampler,
    AdditiveChi2Sampler,
    Nystroem,
    SkewedChi2Sampler,
)
from sklearn.cluster import KMeans, FeatureAgglomeration

from sklearn.ensemble import (
    AdaBoostClassifier,
    BaggingClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import (
    LogisticRegression,
    PassiveAggressiveClassifier,
    SGDClassifier,
    RidgeClassifier,
    Perceptron,
)
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC, NuSVC, SVC
from xgboost import XGBClassifier
from sklearn.preprocessing import OneHotEncoder, Normalizer
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.utils.no_op import NoOp
from autoai_ts_libs.deps.srom.feature_engineering.model_based_feature_generator import (
    ModelbasedFeatureGenerator,
)
from sklearn.feature_selection import VarianceThreshold
from autoai_ts_libs.deps.srom.feature_selection.variance_based_feature_selection import (
    LowVarianceFeatureElimination,
)
from autoai_ts_libs.deps.srom.auto.base_auto import SROMAutoPipeline
from sklearn.manifold import (
    Isomap,
    LocallyLinearEmbedding,
    MDS,
    SpectralEmbedding,
    TSNE,
)
from sklearn.exceptions import NotFittedError
from sklearn.preprocessing import KBinsDiscretizer, PowerTransformer

from sklearn.feature_selection import SelectKBest, SelectPercentile
from sklearn.preprocessing import (
    MinMaxScaler,
    MaxAbsScaler,
    StandardScaler,
    RobustScaler,
)
from sklearn.decomposition import (
    PCA,
    FactorAnalysis,
    FastICA,
    IncrementalPCA,
    KernelPCA,
    NMF,
    SparsePCA,
    TruncatedSVD,
)
from sklearn.preprocessing import PolynomialFeatures, QuantileTransformer

from autoai_ts_libs.deps.srom.pipeline.hyper_params.classification_fine_grid_for_bayesian import (
    PARAM_GRID as bayesian_paramgrid,
)
from autoai_ts_libs.deps.srom.pipeline.hyper_params.classification_sample_grid_for_rbfopt import (
    PARAM_GRID as rbopt_paramgrid,
)
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    roc_auc_score,
    balanced_accuracy_score,
)
import numpy as np
from sklearn.inspection import permutation_importance


class AutoClassification(SROMAutoPipeline):
    """
    The class for performing the auto-classification in SROM using a well tested heuristic "Bottom-Up". \
    The model_stages in this class have already been setup from the benchmark results. \
    (link from the results of experimentation can be put here.)



    Example:
    >>> from autoai_ts_libs.deps.srom.auto.auto_classification import AutoClassification
    >>> X = pd.DataFrame([[1,2,3,2,2,1,2],[5,6,3,2,5,3,1]])
    >>> y = [1,0,0,0,1,0,1]
    >>> ac = AutoClassification()
    >>> ac.automate(X,y)
    """

    def __init__(
        self,
        level="default",
        save_prefix="auto_classification_output_",
        execution_platform="spark_node_random_search",
        cv=5,
        scoring=None,
        stages=None,
        execution_time_per_pipeline=2,
        num_options_per_pipeline_for_random_search=10,
        num_option_per_pipeline_for_intelligent_search=30,
        total_execution_time=10,
        param_grid=None,
    ):
        """
        Parameters:
        level (String): Level of exploration (default or comprehensive).
        save_prefix (string): String prefix for the output save file.
        execution_platform (string): Platform for execution from autoai_ts_libs.deps.srom pipeline. Supports spark also.
        cv (int): Value of 'k' in K-crossvalidation. This parameters is used from the sklearn \
                function GridSearchCV. \
                https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
        scoring (Sting, function): The value that defines the metrics for scoring the paths. \
                Can be a string if sklearn defined metrics used. Can be a funtion if a user \
                defined metric is used. This parameters is used from the sklearn function GridSearchCV. \
            https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
        stages (list of list of estimators): A list of list containing the transformer and \
                estimator tuples for customizing the preconfigured auto pipeline.
        execution_time_per_pipeline (int): Integer value denoting time (minutes) of execution \
                per path (path: combination of estimators and transformers).
        num_options_per_pipeline_for_random_search (int): Integer value denoting number \
                of parameters to use while performing randomized param search in *which* rounds.
        num_option_per_pipeline_for_intelligent_search: Integer value denoting number of \
                parameters to use while performing more intelligent param search in *which* rounds.
        total_execution_time (int): Total execution time (minutes) for the auto classification pipeline.
        param_grid (SROMParamGrid): Param grid with various parameter combination.
        """

        super(AutoClassification, self).__init__(
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
            bayesian_paramgrid=bayesian_paramgrid,
            rbopt_paramgrid=rbopt_paramgrid,
            param_grid=param_grid,
        )

        self.stacked_ensemble_estimator = None
        self.voting_ensemble_estimator = None

        if param_grid is None:
            self.param_grid = SROMParamGrid(gridtype="classification_fine_grid")

    def _initialize_default_stages(self, random_state=42):
        """
        Set stages for the pipeline in a pre-defined manner.
        """
        feature_transformation_set = [
            ("skiptransformation", NoOp()),
            ("discretizer", KBinsDiscretizer()),
            ("powertransformer", PowerTransformer()),
            ("onehotencoder", OneHotEncoder(sparse=False)),
            ("polynomialfeatures", PolynomialFeatures()),
            ("normalizer", Normalizer()),
        ]

        scaler_set = [
            ("skipscaling", NoOp()),
            ("standardscaler", StandardScaler()),
            ("minmaxscaler", MinMaxScaler()),
            ("maxabsscaler", MaxAbsScaler()),
            ("robustscaler", RobustScaler(quantile_range=(25, 75))),
            (
                "quantilescalinguniform",
                QuantileTransformer(
                    output_distribution="uniform", random_state=random_state
                ),
            ),
            (
                "quantilescalingnormal",
                QuantileTransformer(
                    output_distribution="normal", random_state=random_state
                ),
            ),
        ]

        feature_preprocessing_set = [
            ("skipfeaturepreprocessing", NoOp()),
            ("pca", PCA(random_state=random_state)),
            ("fastica", FastICA(random_state=random_state)),
            ("kernelpca", KernelPCA(random_state=random_state)),
            ("selectkbest", SelectKBest()),
            ("variancethreshold", VarianceThreshold()),
            ("lowvariancefeatureelimination", LowVarianceFeatureElimination()),
            ("selectpercentile", SelectPercentile()),
            ("rbfsampler", RBFSampler(random_state=random_state)),
            ("additivechi2sampler", AdditiveChi2Sampler()),
            ("nmf", NMF(random_state=random_state)),
            ("nystroem", Nystroem(random_state=random_state)),
            ("truncatedsvd", TruncatedSVD(random_state=random_state)),
            ("skewedchi2sampler", SkewedChi2Sampler(random_state=random_state)),
            ("sparsepca", SparsePCA(random_state=random_state)),
            ("isomap", Isomap()),
            (
                "locallylinearembedding",
                LocallyLinearEmbedding(random_state=random_state),
            ),
            ("featureagglomeration", FeatureAgglomeration()),
        ]

        estimator_feature_generator = [
            ("skipmodelfeaturegeneration", NoOp()),
            ("bernoullinbfeature", ModelbasedFeatureGenerator(BernoulliNB())),
            ("multinomialnbfeature", ModelbasedFeatureGenerator(MultinomialNB())),
            (
                "decisiontreeclassifierfeature",
                ModelbasedFeatureGenerator(
                    DecisionTreeClassifier(random_state=random_state)
                ),
            ),
            (
                "extratreesclassifierfeature",
                ModelbasedFeatureGenerator(
                    ExtraTreesClassifier(random_state=random_state)
                ),
            ),
            (
                "randomforestclassifierfeature",
                ModelbasedFeatureGenerator(
                    RandomForestClassifier(random_state=random_state)
                ),
            ),
            (
                "gradientboostingclassifierfeature",
                ModelbasedFeatureGenerator(
                    GradientBoostingClassifier(random_state=random_state)
                ),
            ),
            (
                "kneighborsclassifierfeature",
                ModelbasedFeatureGenerator(KNeighborsClassifier()),
            ),
            (
                "linearsvcfeature",
                ModelbasedFeatureGenerator(LinearSVC(random_state=random_state)),
            ),
            (
                "logisticregressionfeature",
                ModelbasedFeatureGenerator(
                    LogisticRegression(random_state=random_state)
                ),
            ),
            (
                "xgbclassifierfeature",
                ModelbasedFeatureGenerator(XGBClassifier(random_state=random_state)),
            ),
            (
                "sgdclassifierfeature",
                ModelbasedFeatureGenerator(SGDClassifier(random_state=random_state)),
            ),
            ("svcfeature", ModelbasedFeatureGenerator(SVC(random_state=random_state))),
            (
                "perceptronfeature",
                ModelbasedFeatureGenerator(Perceptron(random_state=random_state)),
            ),
            (
                "mlpclassifierfeature",
                ModelbasedFeatureGenerator(MLPClassifier(random_state=random_state)),
            ),
            (
                "passiveaggressiveclassifierfeature",
                ModelbasedFeatureGenerator(
                    PassiveAggressiveClassifier(random_state=random_state)
                ),
            ),
            (
                "adaboostclassifierfeature",
                ModelbasedFeatureGenerator(
                    AdaBoostClassifier(random_state=random_state)
                ),
            ),
            ("gaussiannbfeature", ModelbasedFeatureGenerator(GaussianNB())),
            (
                "lineardiscriminantanalysisfeature",
                ModelbasedFeatureGenerator(LinearDiscriminantAnalysis()),
            ),
            (
                "quadraticdiscriminantanalysisfeature",
                ModelbasedFeatureGenerator(QuadraticDiscriminantAnalysis()),
            ),
            # """
            # (
            #    "gaussianprocessclassifierfeature",
            #    ModelbasedFeatureGenerator(
            #        GaussianProcessClassifier(random_state=random_state)
            #    ),
            # ),
            # """
            (
                "ridgeclassifierfeature",
                ModelbasedFeatureGenerator(RidgeClassifier(random_state=random_state)),
            ),
            (
                "baggingclassifierfeature",
                ModelbasedFeatureGenerator(
                    BaggingClassifier(random_state=random_state)
                ),
            ),
            (
                "kmeanclusterfeature",
                ModelbasedFeatureGenerator(KMeans(random_state=random_state)),
            ),
            (
                "nusvcfeature",
                ModelbasedFeatureGenerator(NuSVC(random_state=random_state)),
            ),
        ]

        estimator_set = [
            ("bernoullinb", BernoulliNB()),
            ("multinomialnb", MultinomialNB()),
            (
                "decisiontreeclassifier",
                DecisionTreeClassifier(random_state=random_state),
            ),
            ("extratreesclassifier", ExtraTreesClassifier(random_state=random_state)),
            (
                "randomforestclassifier",
                RandomForestClassifier(random_state=random_state),
            ),
            (
                "gradientboostingclassifier",
                GradientBoostingClassifier(random_state=random_state),
            ),
            ("kneighborsclassifier", KNeighborsClassifier()),
            ("linearsvc", LinearSVC(random_state=random_state)),
            ("logisticregression", LogisticRegression(random_state=random_state)),
            ("xgbclassifier", XGBClassifier(random_state=random_state)),
            ("sgdclassifier", SGDClassifier(random_state=random_state)),
            ("svc", SVC(random_state=random_state)),
            ("perceptron", Perceptron(random_state=random_state)),
            ("mlpclassifier", MLPClassifier(random_state=random_state)),
            (
                "passiveaggressiveclassifier",
                PassiveAggressiveClassifier(random_state=random_state),
            ),
            ("adaboostclassifier", AdaBoostClassifier(random_state=random_state)),
            ("gaussiannb", GaussianNB()),
            ("lineardiscriminantanalysis", LinearDiscriminantAnalysis()),
            ("quadraticdiscriminantanalysis", QuadraticDiscriminantAnalysis()),
            # """
            # (
            #    "gaussianprocessclassifier",
            #    GaussianProcessClassifier(random_state=random_state),
            # ),
            # """
            ("ridgeclassifier", RidgeClassifier(random_state=random_state)),
            ("baggingclassifier", BaggingClassifier(random_state=random_state)),
            ("nusvc", NuSVC(random_state=random_state)),
        ]

        lgbm_installed = False
        try:
            import lightgbm as lgb

            lgbm_installed = True
            if lgbm_installed:
                lightGBM = lgb.LGBMClassifier(random_state=random_state)
                estimator_set.append(("lightGBM", lightGBM))
        except:
            pass

        # initialize the stages of the pipeline
        self.stages = [
            feature_transformation_set,
            scaler_set,
            feature_preprocessing_set,
            estimator_feature_generator,
            estimator_set,
        ]

        return self.stages

    def _initialize_additional_stages(self, random_state=42):
        """
            Method Initialize additional stages for the pipeline.
        """
        self.additional_stages = None
        return self.additional_stages

    def summary(self, enable_param_grid=False):
        """
            Method for summary of the pipeline.
        """
        tmp_auto_pipeline = SROMPipeline()
        if self.stages:
            tmp_auto_pipeline.set_stages(self.stages)
        else:
            tmp_auto_pipeline.set_stages(self._initialize_default_stages())
        if self.param_grid:
            tmp_auto_pipeline.set_param_grid(self.param_grid)
        return tmp_auto_pipeline.summary(
            enable_param_grid=enable_param_grid, is_auto=True
        )

    def automate(self, X, y, verbosity="low"):
        """
        The function is for executing the automated training of the SROM pipeline. This \
        code follows a well-defined strategy for iteratively training a subset of pipeline \
        and finding the best estimator in each iteration. This strategy provides best results \
        in the shortest amount of time.

        Parameters:
            X (pandas dataframe or numpy array): The dataset to be used for model selection. \
                    shape = [n_samples, n_features] \
                    where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. This is optional, \
                    if target_column is added in the meta data, it is used from \
                    there.shape = [n_samples] or [n_samples, n_output].
        """
        return super(AutoClassification, self).automate(X, y, verbosity)

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
        super(AutoClassification, self).fit(X, y)
        return self

    def predict(self, X):
        """
        Predict the class labels targets/anomaly scores etc. using \
        the trained model pipeline.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        return super(AutoClassification, self).predict(X)

    def fit_voting_ensemble(self, X, y, num_leader=5, check_pred_proba_cond=False):
        """ 
        Train an ensemble model on the given data using Voting strategy.

        Parameters:
            X (pandas dataframe or numpy array): Training dataset. \
                    shape = [n_samples, n_features] \
                    where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                    If target_column is added in the meta data, it is \
                    used from there. shape = [n_samples] or [n_samples, n_output].
            num_leader (int): Number of model for creating ensemble model.
            check_pred_proba_cond (bool): Remove model based on predict_prob condition

        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline or pyspark.ml.Pipeline, not SROMPipeline.
        """
        mSet = self.get_leaders(num_leader, check_pred_proba_cond=check_pred_proba_cond)
        pSet = []
        for i_item, item in enumerate(mSet):
            pSet.append(("mdl_" + str(i_item), item))
        from sklearn.ensemble import VotingClassifier

        if check_pred_proba_cond:
            self.voting_ensemble_estimator = VotingClassifier(
                estimators=pSet, voting="soft"
            )
        else:
            self.voting_ensemble_estimator = VotingClassifier(
                estimators=pSet, voting="hard"
            )
        self.voting_ensemble_estimator.fit(X, y)
        return self

    def fit_stacked_ensemble(
        self, X, y, num_leader=5, meta_classifier_for_stack=LogisticRegression()
    ):
        """
        Train an ensemble model on the given data using Stacking strategy.

        Parameters:
            X (pandas dataframe or numpy array): Training dataset. \
                    shape = [n_samples, n_features] \
                    where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                    If target_column is added in the meta data, it is \
                    used from there. shape = [n_samples] or [n_samples, n_output].
            num_leader (int): Number of model for creating ensemble model.
            meta_classifier_for_stack (classifier): Classifier for building stacking model
        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline or pyspark.ml.Pipeline, not SROMPipeline.
        """
        mSet = self.get_leaders(num_leader, check_pred_proba_cond=False)
        from autoai_ts_libs.deps.srom.classification.stack_classification import StackClassifier

        self.stacked_ensemble_estimator = StackClassifier(
            base_models=mSet, meta_model=meta_classifier_for_stack
        )
        self.stacked_ensemble_estimator.fit(X, y)
        return self

    def predict_voting_ensemble(self, X):
        """
        Predict the class labels targets/anomaly scores etc. using \
        the trained ensemble voting model.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        if self.voting_ensemble_estimator:
            return self.voting_ensemble_estimator.predict(X)
        else:
            raise NotFittedError(
                "Please call fit_voting_ensemble() to fit voting ensemble before predicting."
            )

    def predict_stacked_ensemble(self, X):
        """
        Predict the class labels targets/anomaly scores etc. using \
        the trained ensemble stacking model.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        if self.stacked_ensemble_estimator:
            return self.stacked_ensemble_estimator.predict(X)
        else:
            raise NotFittedError(
                "Please call fit_stacked_ensemble() to fit stacked ensemble before predicting."
            )

    def predict_voting_ensemble_proba(self, X):
        """
        Predict the class labels probability using \
        the trained ensemble voting model.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        if self.voting_ensemble_estimator:
            if "predict_proba" in dir(self.voting_ensemble_estimator):
                return self.voting_ensemble_estimator.predict_proba(X)
            else:
                raise Exception("The fitted model does not has predict_proba method.")
        else:
            raise NotFittedError(
                "Please call fit_voting_ensemble() to fit voting ensemble before predicting."
            )

    def predict_stacked_ensemble_proba(self, X):
        """
        Predict the class labels probability scores etc. using \
        the trained ensemble stacking model.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        if self.stacked_ensemble_estimator:
            if "predict_proba" in dir(self.stacked_ensemble_estimator):
                return self.stacked_ensemble_estimator.predict_proba(X)
            else:
                raise Exception("The class does not has predict_proba method.")
        else:
            raise NotFittedError(
                "Please call fit_stacked_ensemble() to fit stacked ensemble before predicting."
            )

    def evaluate_top_pipelines_on_holdout(
        self, trainX, trainY, testX, testY, auto_model, num_top_models=10
    ):
        """
        this is a utility function
        trainX: Training X data
        trainY: Training Y data
        testX: Testing X data
        testY: Testing Y data
        auto_model: the saved auto model pickle
        num_top_models: integer
        Note- classification some time has issue in getting score
        """

        all_score = []
        for item in range(len(auto_model["best_path"])):
            all_score.append(auto_model["best_path"][item]["best_score"])

        all_score = np.array(all_score, dtype=np.float_)
        sort_index = np.argsort(all_score)
        current_path = 0

        post_evaluation = []
        for item in sort_index[::-1]:
            if abs(float(all_score[item])) >= 0:
                round_res = []
                round_res.append(auto_model["best_path"][item]["estimator_id"])
                round_res.append(all_score[item])

                try:
                    pSet = auto_model["best_path"][item]["best_estimator"]
                    pSet.fit(trainX, trainY)
                    pred_y = pSet.predict(testX)

                    # this will work for univariate output
                    pred_y = pred_y.flatten()
                    y_test = testY.flatten()

                    round_res.append(roc_auc_score(y_test, pred_y))
                    round_res.append(balanced_accuracy_score(y_test, pred_y))
                    round_res.append(accuracy_score(y_test, pred_y))
                    round_res.append(f1_score(y_test, pred_y))
                    post_evaluation.append(round_res)

                    current_path = current_path + 1
                    if current_path >= num_top_models:
                        break
                except:
                    pass

        ret_result = pd.DataFrame(post_evaluation)
        ret_result.columns = [
            "estimator_id",
            "CV_score",
            "roc_auc_score",
            "balanced_accuracy_score",
            "accuracy_score",
            "f1_score",
        ]
        return ret_result
