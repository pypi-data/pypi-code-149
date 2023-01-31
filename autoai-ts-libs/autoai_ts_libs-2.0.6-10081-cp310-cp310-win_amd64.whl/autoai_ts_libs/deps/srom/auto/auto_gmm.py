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

from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.mixture_model.utils import GMMPipeline
from sklearn.mixture import GaussianMixture
from autoai_ts_libs.deps.srom.mixture_model.utils import GMM_score
from autoai_ts_libs.deps.srom.utils.no_op import NoOp
from sklearn.cluster import AgglomerativeClustering, KMeans
from autoai_ts_libs.deps.srom.data_sampling.unsupervised.random_sampler import DataSampler
from autoai_ts_libs.deps.srom.auto.base_auto import SROMAutoPipeline
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.utils.pipeline_utils import check_custom_stage_random_state
from autoai_ts_libs.deps.srom.model_selection import TrainKFold

class AutoGMM(SROMAutoPipeline):
    """
    The class for performing the automatic-GMM in SROM using a well tested heuristic "Bottom-Up". \
    The model_stages in this class have already been setup from the benchmark results. \
    (link from the results of experimentation can be put here.)


    Example:
    >>> from autoai_ts_libs.deps.srom.auto.auto_gmm import AutoGMM
    >>> X = pd.DataFrame([[1,2,3,2,2,1,2],[5,6,3,2,5,3,1]])
    >>> ac = AutoGMM()
    >>> ac.automate(X)
    """

    def __init__(
        self,
        level="default",
        save_prefix="auto_gmm_output_",
        execution_platform="default",
        cv=TrainKFold(3),
        scoring="bic",
        stages=None,
        execution_time_per_pipeline=2,
        num_options_per_pipeline_for_random_search=10,
        num_option_per_pipeline_for_intelligent_search=30,
        total_execution_time=10,
        param_grid=None,
        min_components=2,
        max_components=10,
        max_sample_size=2000,
        additional_stages=None,
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
        super(AutoGMM, self).__init__(
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
            bayesian_paramgrid=None,
            rbopt_paramgrid=None,
            param_grid=param_grid,
        )

        # to extra initialization
        self.min_components = min_components
        self.max_components = max_components
        self.max_sample_size = max_sample_size
        self.additional_stages = additional_stages

        if param_grid is None:
            self.param_grid = SROMParamGrid()

    def _initialize_default_stages(self, random_state=42):
        """
            Method to Initialize default stages for pipeline. 
        """
        # initialize the stages of the pipeline
        self.stages = []

        # DAG 1 : Data Sampling Based DAG
        data_samplers = [("datasampler", DataSampler(num_samples=self.max_sample_size))]

        cluster_initializers = [
            (
                "agglomerativeclustering_euclidean_ward",
                AgglomerativeClustering(affinity="euclidean", linkage="ward"),
            ),
            ("kmeans_random", KMeans(init="random", random_state=random_state)),
            ("kmeans_++", KMeans(init="k-means++", random_state=random_state)),
        ]

        affinity = ["euclidean", "l1", "l2", "manhattan", "cosine"]
        linkage = ["complete", "average", "single"]

        for afn in affinity:
            for lnk in linkage:
                cluster_initializers.append(
                    (
                        "agglomerativeclustering_" + afn + "_" + lnk,
                        AgglomerativeClustering(affinity=afn, linkage=lnk),
                    )
                )

        gmms = self._get_GMM(random_state)

        self.stages = [data_samplers, cluster_initializers, gmms]

        return self.stages

    def _get_GMM(self, random_state):
        """
            Internal method get_gmm.
        """
        _gmm = []
        for item in range(self.min_components, self.max_components):
            for covariance_type in ["full", "tied", "diag", "spherical"]:
                _gmm.append(
                    (
                        "gaussianmixture_" + str(item) + str(covariance_type),
                        GaussianMixture(
                            n_components=item,
                            covariance_type=covariance_type,
                            random_state=random_state,
                        ),
                    )
                )
        return _gmm

    def summary(self, enable_param_grid=False):
        """
            Method for Summary of the pipeline. 
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

    def _initialize_additional_stages(self, random_state=42):
        """
            Method to initialize additional stages for pipeline.
        """
        gmms_2 = self._get_GMM(random_state)
        self.additional_stages = []
        self.additional_stages.append([gmms_2])
        return self.additional_stages

    def _init_pipeline(self, stages=None):
        """
            Method init_pipeline to initialize pipeline.
        """
        self.auto_pipeline = SROMPipeline()
        self.auto_pipeline.set_pipeline_type_for_path(pipeline_type=GMMPipeline)
        if isinstance(self.scoring, str):
            self.auto_pipeline.set_pipeline_init_param_for_path(pipeline_init_param={'scoring':self.scoring})
        else:
            self.auto_pipeline.set_scoring(self.scoring)
        self.auto_pipeline.set_cross_val_score(GMM_score)
        self.auto_pipeline.set_cross_validation(self.cv)

        # set default stages if custom stages not provided
        if stages is None:
            if self.stages is None:
                self.stages = self._initialize_default_stages()
            if self.additional_stages is None:
                self.additional_stages = self._initialize_additional_stages()
            self.auto_pipeline.set_stages(self.stages)
            for a_stage in self.additional_stages:
                self.auto_pipeline.sromgraph.add_stages(a_stage)
            check_custom_stage_random_state(self.stages)
        else:
            self.auto_pipeline.set_stages(stages)
            check_custom_stage_random_state(stages)
        print(self.auto_pipeline.sromgraph.stages)

    def automate(self, X, y=None, verbosity="low"):
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
        return super(AutoGMM, self).automate(X, None, verbosity)

    def fit(self, X, y=None):
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
        super(AutoGMM, self).fit(X, y)
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
        return super(AutoGMM, self).predict(X)


    def export_to_onnx(self, X):
        """_summary_

        Args:
            X (_type_): _description_
        """
        if self.best_estimator_so_far:
            return self.best_estimator_so_far.export_to_onnx(X)
        else:
            raise Exception('Best model is not set')
