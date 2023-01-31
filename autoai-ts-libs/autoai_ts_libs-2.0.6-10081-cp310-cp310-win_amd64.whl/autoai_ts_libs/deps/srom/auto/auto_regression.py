# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: auto_regression
   :synopsis: SROM Autoregression.

.. moduleauthor:: SROM Team
"""
from sklearn.cluster import FeatureAgglomeration
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import NMF, PCA, FastICA, KernelPCA, SparsePCA, TruncatedSVD
from sklearn.ensemble import (
    AdaBoostRegressor,
    BaggingRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.exceptions import NotFittedError
from sklearn.feature_selection import SelectKBest, SelectPercentile, VarianceThreshold
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.kernel_approximation import (
    AdditiveChi2Sampler,
    Nystroem,
    RBFSampler,
    SkewedChi2Sampler,
)
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import (
    BayesianRidge,
    ElasticNet,
    HuberRegressor,
    Lasso,
    LassoLars,
    LinearRegression,
    OrthogonalMatchingPursuit,
    PassiveAggressiveRegressor,
    RANSACRegressor,
    Ridge,
    SGDRegressor,
    TheilSenRegressor,
)
from sklearn.manifold import Isomap, LocallyLinearEmbedding
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import (
    MaxAbsScaler,
    MinMaxScaler,
    Normalizer,
    OneHotEncoder,
    PolynomialFeatures,
    QuantileTransformer,
    RobustScaler,
    StandardScaler,
)
from sklearn.tree import DecisionTreeRegressor
from autoai_ts_libs.deps.srom.auto.base_auto import SROMAutoPipeline
from autoai_ts_libs.deps.srom.feature_engineering.model_based_feature_generator import (
    ModelbasedFeatureGenerator,
)
from autoai_ts_libs.deps.srom.feature_selection.variance_based_feature_selection import (
    LowVarianceFeatureElimination,
)
from autoai_ts_libs.deps.srom.pipeline.hyper_params.regression_fine_grid_for_bayesian import (
    PARAM_GRID as bayesian_paramgrid,
)
from autoai_ts_libs.deps.srom.pipeline.hyper_params.regression_sample_grid_for_rbfopt import (
    PARAM_GRID as rbopt_paramgrid,
)
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.regression.data_partition_based_regression import PartitionRegressor
from autoai_ts_libs.deps.srom.regression.gaussian_mixture_regressor import GaussianMixtureRegressor
from autoai_ts_libs.deps.srom.utils.no_op import NoOp
from xgboost import XGBRegressor
from sklearn.preprocessing import KBinsDiscretizer, PowerTransformer
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from sklearn.inspection import permutation_importance


class AutoRegression(SROMAutoPipeline):
    """
    The class for performing the auto-Regression in SROM using a well tested heuristic "Bottom-Up". \
    The model_stages in this class have already been setup from the benchmark results. \
    (link from the results of experimentation can be put here.)


    Example:
    >>> from autoai_ts_libs.deps.srom.auto.auto_regression import AutoRegression
    >>> X = pd.DataFrame([[1,2,3,2,2,1,2],[5,6,3,2,5,3,1]])
    >>> y = [1,0,0,0,1,0,1]
    >>> ac = AutoRegression()
    >>> ac.automate(X,y)
    """

    def __init__(
        self,
        level="default",
        save_prefix="auto_regression_output_",
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
                    per path (path: combination of estimators and transformers)
            num_options_per_pipeline_for_random_search (int): Integer value denoting number \
                    of parameters to use while performing randomized param search in *which* rounds.
            num_option_per_pipeline_for_intelligent_search: Integer value denoting number of \
                    parameters to use while performing more intelligent param search in *which* rounds.
            total_execution_time (int): Total execution time (minutes) for the auto classification pipeline.
            param_grid (SROMParamGrid): Param grid with various parameter combination.
        """

        super(AutoRegression, self).__init__(
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

        # to extra initialization
        self.stacked_ensemble_estimator = None
        self.voting_ensemble_estimator = None

        if param_grid is None:
            self.param_grid = SROMParamGrid(gridtype="regression_fine_grid")

    def _initialize_default_stages(self, random_state=42):
        """
        Initialize default stages for the pipeline in a pre-defined manner.
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
            ("SkipModelFeatureGeneration", NoOp()),
            (
                "lassolarsfeature",
                ModelbasedFeatureGenerator(LassoLars(random_state=random_state)),
            ),
            (
                "ridgefeature",
                ModelbasedFeatureGenerator(Ridge(random_state=random_state)),
            ),
            ("linearregressionfeature", ModelbasedFeatureGenerator(LinearRegression())),
            (
                "lassofeature",
                ModelbasedFeatureGenerator(Lasso(random_state=random_state)),
            ),
            (
                "elasticnetfeature",
                ModelbasedFeatureGenerator(ElasticNet(random_state=random_state)),
            ),
            (
                "orthogonalmatchingpursuitfeature",
                ModelbasedFeatureGenerator(OrthogonalMatchingPursuit()),
            ),
            ("bayesianridgefeature", ModelbasedFeatureGenerator(BayesianRidge())),
            (
                "sgdregressorfeature",
                ModelbasedFeatureGenerator(SGDRegressor(random_state=random_state)),
            ),
            (
                "passiveaggressiveregressorfeature",
                ModelbasedFeatureGenerator(
                    PassiveAggressiveRegressor(random_state=random_state)
                ),
            ),
            (
                "kneighborsregressorfeature",
                ModelbasedFeatureGenerator(KNeighborsRegressor()),
            ),
            (
                "decisiontreeregressorfeature",
                ModelbasedFeatureGenerator(
                    DecisionTreeRegressor(random_state=random_state)
                ),
            ),
            (
                "mlpregressorfeature",
                ModelbasedFeatureGenerator(MLPRegressor(random_state=random_state)),
            ),
            (
                "gradientboostingregressorfeature",
                ModelbasedFeatureGenerator(
                    GradientBoostingRegressor(random_state=random_state)
                ),
            ),
            (
                "adaboostregressorfeature",
                ModelbasedFeatureGenerator(
                    AdaBoostRegressor(random_state=random_state)
                ),
            ),
            (
                "baggingregressorfeature",
                ModelbasedFeatureGenerator(BaggingRegressor(random_state=random_state)),
            ),
            (
                "randomforestregressorfeature",
                ModelbasedFeatureGenerator(
                    RandomForestRegressor(random_state=random_state)
                ),
            ),
            (
                "extratreesregressorfeature",
                ModelbasedFeatureGenerator(
                    ExtraTreesRegressor(random_state=random_state)
                ),
            ),
            ("plsregressionfeature", ModelbasedFeatureGenerator(PLSRegression())),
            # (
            #    "gaussianprocessregressorfeature",
            #    ModelbasedFeatureGenerator(
            #        GaussianProcessRegressor(random_state=random_state)
            #    ),
            # ),
            ("kernelridgefeature", ModelbasedFeatureGenerator(KernelRidge())),
            (
                "theilsenregressorfeature",
                ModelbasedFeatureGenerator(
                    TheilSenRegressor(random_state=random_state)
                ),
            ),
            ("huberregressorfeature", ModelbasedFeatureGenerator(HuberRegressor())),
            (
                "ransacregressorfeature",
                ModelbasedFeatureGenerator(RANSACRegressor(random_state=random_state)),
            ),
        ]

        estimator_set = [
            ("linearregression", LinearRegression()),
            ("ridge", Ridge(random_state=random_state)),
            ("lasso", Lasso(random_state=random_state)),
            ("elasticnet", ElasticNet(random_state=random_state)),
            ("lassolars", LassoLars(random_state=random_state)),
            ("orthogonalmatchingpursuit", OrthogonalMatchingPursuit()),
            ("bayesianridge", BayesianRidge()),
            ("sgdregressor", SGDRegressor(random_state=random_state)),
            (
                "passiveaggressiveregressor",
                PassiveAggressiveRegressor(random_state=random_state),
            ),
            ("kneighborsregressor", KNeighborsRegressor()),
            ("decisiontreeregressor", DecisionTreeRegressor(random_state=random_state)),
            ("mlpregressor", MLPRegressor(random_state=random_state)),
            (
                "gradientboostingregressor",
                GradientBoostingRegressor(random_state=random_state),
            ),
            ("adaboostregressor", AdaBoostRegressor(random_state=random_state)),
            ("baggingregressor", BaggingRegressor(random_state=random_state)),
            ("randomforestregressor", RandomForestRegressor(random_state=random_state)),
            ("extratreesregressor", ExtraTreesRegressor(random_state=random_state)),
            ("plsregression", PLSRegression()),
            # (
            #    "gaussianprocessregressor",
            #    GaussianProcessRegressor(random_state=random_state),
            # ),
            ("kernelridge", KernelRidge()),
            ("theilsenregressor", TheilSenRegressor(random_state=random_state)),
            ("ransacregressor", RANSACRegressor(random_state=random_state)),
            ("huberregressor", HuberRegressor()),
            ("partitionregressor", PartitionRegressor()),
            ("xgbregressor", XGBRegressor(random_state=random_state)),
            ("gaussianmixtureregressor", GaussianMixtureRegressor()),
        ]

        lgbm_installed = False
        try:
            import lightgbm as lgb

            lgbm_installed = True
            if lgbm_installed:
                lightGBM = lgb.LGBMRegressor(random_state=random_state)
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
        Initialize additionsl stages for the pipeline in a pre-defined manner.
        """
        self.additional_stages = None
        return self.additional_stages

    def summary(self, enable_param_grid=False):
        """
        Summary method to get the summary of the pipeline.
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
        The function for executing the automated training of the SROM pipeline. This \
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
            verbosity (String, Optional) Default value is "low". Possible values: "low", "medium",\
                "high".
        """
        return super(AutoRegression, self).automate(X, y, verbosity)

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
        super(AutoRegression, self).fit(X, y)
        return self

    def predict(self, X):
        """
        Predict the class labels/regression targets/anomaly scores etc. using \
        the trained model pipeline.
        
        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        return super(AutoRegression, self).predict(X)

    def fit_stacked_ensemble(
        self, X, y, num_leader=5, meta_regressor_for_stack=LinearRegression()
    ):
        """
        Train an ensemble model on the given data using Stacking strategy.

        Parameters:
            X (pandas dataframe or numpy array): Training dataset. \
                    shape = [n_samples, n_features] \
                    where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                    if target_column is added in the meta data, it is \
                    used from there. shape = [n_samples] or [n_samples, n_output].
            num_leader (int): Number of model for creating ensemble model
            meta_regressor_for_stack (regressor): Regressor for building stacking model

        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline or pyspark.ml.Pipeline, not SROMPipeline.
        """
        mSet = self.get_leaders(num_leader)
        from autoai_ts_libs.deps.srom.regression.stack_regression import StackRegressor

        self.stacked_ensemble_estimator = StackRegressor(
            base_models=mSet, meta_model=meta_regressor_for_stack
        )
        self.stacked_ensemble_estimator.fit(X, y)
        return self

    def predict_stacked_ensemble(self, X):
        """
        Predict the class labels/regression targets/anomaly scores etc. using \
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

    def fit_voting_ensemble(
        self, X, y, num_leader=5, n_estimators=30, aggr_type="median", n_jobs=None,bootstrap=True
    ):
        """
        Train an ensemble model on the given data using Voting strategy.
        
        Parameters:
            X (pandas dataframe or numpy array): Training dataset. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                If target_column is added in the meta data, it is \
                used from there. shape = [n_samples] or [n_samples, n_output]
            num_leader (int): Number of model for creating ensemble model.
            n_jobs: The number of parallel jobs to run. `None` means 1, `-1` means using all processors.

        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline or pyspark.ml.Pipeline, not SROMPipeline.
        """
        mSet = self.get_leaders(num_leader)
        if mSet is None or len(mSet) == 0:
            raise ValueError(
                "There are no leaders picked. Either there are no leaders or .automate() does not run."
            )
        from autoai_ts_libs.deps.srom.regression.predictive_uncertainity_estimation import (
            PredictiveUncertaintyEstimator,
        )

        self.voting_ensemble_estimator = PredictiveUncertaintyEstimator(
            base_model=mSet,
            n_estimators=n_estimators,
            aggr_type=aggr_type,
            n_jobs=n_jobs,
            bootstrap=bootstrap
        )
        self.voting_ensemble_estimator.fit(X, y)
        return self

    def predict_voting_ensemble(self, X):
        """
        Predict the class labels/regression targets/anomaly scores etc. using \
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

    def predict_voting_ensemble_interval(self, X, prediction_percentile=95):
        """
        Predict the interval (lower bound and upper bound) using \
        the trained ensemble voting model.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.
            prediction_percentile (integer): between 0 to 100.
        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        if self.voting_ensemble_estimator:
            return self.voting_ensemble_estimator.predict_interval(
                X, prediction_percentile
            )
        else:
            raise NotFittedError(
                "Please call fit_voting_ensemble() to fit voting ensemble before predicting."
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

                    round_res.append(np.std(y_test - pred_y))
                    round_res.append(np.mean(y_test - pred_y))
                    round_res.append(mean_absolute_error(y_test, pred_y))
                    round_res.append(mean_squared_error(y_test, pred_y))
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
            "Dev Error",
            "Mean Error",
            "MAE",
            "MSE",
        ]
        return ret_result
