'''
The File is borrowed from the anomaly detection service to let AD-Service just free from 
any SROM Related code
'''
def anomaly_job(params, credentials):
    job_name = params["job"]

    # imports to be trimmed/cleaned up in one of future commits
    import logging
    import json
    from enum import Enum
    import datetime
    import inspect
    from ibm_botocore.exceptions import ClientError
    from autoai_ts_libs.deps.srom.utils.no_op import NoOp
    from sklearn.preprocessing import MinMaxScaler

    from sklearn.model_selection import TimeSeriesSplit, train_test_split

    from sklearn.linear_model import (
        ElasticNet,
        LassoLars,
        LinearRegression,
        Ridge,
    )

    from autoai_ts_libs.deps.srom.feature_selection.variance_inflation_feature_selection import (
        VarianceInflationFeatureSelection,
    )
    from autoai_ts_libs.deps.srom.feature_selection.correlation_based_feature_selection import (
        CorrelatedFeatureElimination,
    )
    from autoai_ts_libs.deps.srom.feature_selection.variance_based_feature_selection import (
        LowVarianceFeatureElimination,
    )
    from autoai_ts_libs.deps.srom.model_selection import TimeSeriesKFoldSlidingSplit
    from autoai_ts_libs.deps.srom.auto.auto_regression import AutoRegression
    from sklearn.utils import check_array

    from sklearn.pipeline import Pipeline
    import pickle
    import base64
    from pandas.api.types import is_numeric_dtype, is_string_dtype, is_float_dtype
    from autoai_ts_libs.deps.srom.auto.auto_gmm import AutoGMM
    from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
    from autoai_ts_libs.deps.srom.mixture_model.utils import GMMPipeline
    from sklearn.mixture import GaussianMixture
    from autoai_ts_libs.deps.srom.data_sampling.unsupervised.random_sampler import DataSampler
    from sklearn.cluster import AgglomerativeClustering
    from io import StringIO
    import pandas as pd
    from autoai_ts_libs.deps.srom.time_series.run_timeseries_anomaly import (
        run_timeseries_anomaly_wrapper,
    )
    from autoai_ts_libs.deps.srom.time_series.utils.types import (
        AnomalyAlgorithmType,
        AnomalyScoringPredictionType,
        AnomalyScoringAlgorithmType,
        WindowADAlgorithmType,
        TSPDAGType,
        AnomalyExecutionModeType,
        ReconstructADAlgorithmType,
        RelationshipADAlgorithmType,
    )
    from lithops import Storage
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.model_selection import TimeSeriesSplit

    from sklearn.linear_model import (
        ElasticNet,
        LassoLars,
        LinearRegression,
        Ridge,
    )

    from autoai_ts_libs.deps.srom.feature_selection.variance_inflation_feature_selection import (
        VarianceInflationFeatureSelection,
    )
    from autoai_ts_libs.deps.srom.feature_selection.correlation_based_feature_selection import (
        CorrelatedFeatureElimination,
    )
    from autoai_ts_libs.deps.srom.feature_selection.variance_based_feature_selection import (
        LowVarianceFeatureElimination,
    )
    from autoai_ts_libs.deps.srom.model_selection import TimeSeriesKFoldSlidingSplit
    from autoai_ts_libs.deps.srom.auto.auto_regression import AutoRegression
    from sklearn.utils import check_X_y
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from autoai_ts_libs.deps.srom.data_sampling.unsupervised.random_sampler import DataSampler
    import pickle
    import base64
    from pandas.api.types import is_numeric_dtype, is_string_dtype, is_float_dtype
    from sklearn.ensemble import IsolationForest
    from sklearn.mixture import GaussianMixture, BayesianGaussianMixture
    from sklearn.svm import OneClassSVM
    from sklearn.covariance import (
        EmpiricalCovariance,
        EllipticEnvelope,
        LedoitWolf,
        MinCovDet,
        OAS,
        ShrunkCovariance,
    )
    from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler

    from autoai_ts_libs.deps.srom.pipeline.anomaly_pipeline import AnomalyPipeline
    from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
    from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import (
        GeneralizedAnomalyModel,
    )
    from autoai_ts_libs.deps.srom.anomaly_detection.gaussian_graphical_anomaly_model import (
        GaussianGraphicalModel,
    )
    from autoai_ts_libs.deps.srom.anomaly_detection.algorithms import (
        NearestNeighborAnomalyModel,
        LOFNearestNeighborAnomalyModel,
    )
    from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.pca_t2 import AnomalyPCA_T2
    from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.pca_q import AnomalyPCA_Q
    from autoai_ts_libs.deps.srom.utils.no_op import NoOp
    from collections import Counter

    import itertools
    import numpy as np

    class JobAsyncStatus(Enum):
        submitted = "submitted"
        executing = "executing"
        done = "done"
        queued = "queued"
        timeout = "timeout"

    def _get_data_profile(df):
        info_ = {}
        MAX_NUM_DISTINCT_VALUES = 10
        for column_name, dtype in zip(df.columns.tolist(), df.dtypes):
            column_info = {"dtype": dtype}
            if is_numeric_dtype(dtype):
                column_info["is_numeric"] = True
                column_info["is_string"] = False
                column_info["min_value"] = df[column_name].min()
                column_info["max_value"] = df[column_name].max()
                column_info["median_value"] = df[column_name].median()
                if df[column_name].nunique() <= MAX_NUM_DISTINCT_VALUES:
                    column_info["values"] = df[column_name].unique().tolist()
                else:
                    column_info["values"] = []
            elif is_string_dtype(dtype):
                column_info["is_numeric"] = False
                column_info["is_string"] = True
                if df[column_name].nunique() <= MAX_NUM_DISTINCT_VALUES:
                    column_info["values"] = df[column_name].unique().tolist()
                else:
                    column_info["values"] = []
                column_info["mode"] = df[column_name].value_counts().idxmax()
            else:
                column_info["error"] = f"No profile for column {column_name}"

            info_[column_name] = column_info

        return info_

    LOGGER = logging.getLogger(__name__)

    # step 0: update the job status in cos
    jobId = params["jobId"]
    LOGGER.info("Running job {}".format(jobId))

    data_filename = params["data_filename"]
    result_filename = params["jobId"]
    data_bucket = credentials["data_bucket"]
    result_bucket = credentials["result_bucket"]
    storage = Storage()

    status_update = {}
    try:
        obj = storage.get_object(bucket=result_bucket, key=result_filename)
        status_update = obj.decode("utf-8")
        status_update = json.loads(status_update)
        status_update["updated_on"]["execution_started@"] = datetime.datetime.now(
            datetime.timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        status_update["status"] = JobAsyncStatus.executing.value

        storage.put_object(
            bucket=credentials["result_bucket"],
            key=data_filename,
            body=bytes(json.dumps(status_update).encode("UTF-8")),
        )

    except ClientError as be:
        LOGGER.error("CLIENT ERROR: {0}\n".format(be))

    starttime = datetime.datetime.now()
    result = {}
    df = None

    # step 1: retrieve the data from cos
    try:
        # step 1: retrieve the data from cos
        if "data_cos_cred" in params:  # read data from COS from users
            from ibm_watson_machine_learning.helpers.connections import (
                S3Connection,
                S3Location,
                DataConnection,
            )

            cos_data = DataConnection(
                connection=S3Connection(
                    endpoint_url=params["data_cos_cred"]["connection"][
                        "endpoint_url"
                    ],
                    access_key_id=params["data_cos_cred"]["connection"][
                        "access_key_id"
                    ],
                    secret_access_key=params["data_cos_cred"]["connection"][
                        "secret_access_key"
                    ],
                ),
                location=S3Location(
                    bucket=params["data_cos_cred"]["location"]["bucket"],
                    path=params["data_cos_cred"]["location"]["path"],
                ),
            )
            df = cos_data.read()
        else:
            obj = storage.get_object(bucket=data_bucket, key=data_filename)
            sio = StringIO(obj.decode("UTF-8"))
            df = pd.read_csv(sio)
    except Exception as e:
        result = {"error": str(e)}

    # step 2: run_timeseries_anomaly_wrapper
    if 'error' not in result:
        try:
            if job_name == "run_timeseries_anomaly_detection":
                specs = inspect.getfullargspec(run_timeseries_anomaly_wrapper)
                arguments = specs.args
                defaults = [df] + list(specs.defaults)
                kwargs = dict(zip(arguments, defaults))
                for arg, val in kwargs.items():
                    if arg in params:
                        if arg == "execution_mode":
                            kwargs[arg] = AnomalyExecutionModeType(params[arg])
                        elif arg == "algorithm_type":
                            kwargs[arg] = AnomalyAlgorithmType(params[arg])
                        elif arg == "dag_type":
                            kwargs[arg] = TSPDAGType(params[arg])
                        elif arg == "scoring_method":
                            kwargs[arg] = AnomalyScoringAlgorithmType(params[arg])
                        elif arg == "prediction_type":
                            kwargs[arg] = AnomalyScoringPredictionType(params[arg])
                        elif arg == "anomaly_estimator":
                            if params["algorithm_type"] == "WindowAD":
                                kwargs[arg] = WindowADAlgorithmType(params[arg])
                            elif params["algorithm_type"] == "RelationshipAD":
                                kwargs[arg] = RelationshipADAlgorithmType(params[arg])
                            elif params["algorithm_type"] == "ReconstructAD":
                                kwargs[arg] = ReconstructADAlgorithmType(params[arg])
                            else:
                                kwargs[arg] = WindowADAlgorithmType("IsolationForest")
                        else:
                            kwargs[arg] = params[arg]

                print("Job {} params: {}".format(jobId, str(kwargs)))
                result = run_timeseries_anomaly_wrapper(**kwargs)
            elif job_name == "run_regression_model":
                X_ = df[params["feature_columns"]]
                y_ = df[params["target_column"]]
                random_state = 42

                # add the code here
                # if the unsupervised feature selector is on, we apply each of the feature selector and
                # then use the features that appear in atleast two feature selector methods
                # if the final feature selected is None, we may raise an error and then ask them to turn the flag off if it on
                if params["unsupervised_feature_selector"]:
                    # initalize the three FS
                    lvf = LowVarianceFeatureElimination()
                    vif = VarianceInflationFeatureSelection()
                    cor = CorrelatedFeatureElimination()
                    try:
                        lvf.fit(X_)
                        cor.fit(X_)
                        selected_columns = []
                        selected_columns.extend(lvf.selected_columns)
                        selected_columns.extend(cor.selected_columns)
                        if X_.shape[1] < 30:
                            if X_.shape[0] < 1000:
                                vif.fit(X_)
                            else:
                                ds = DataSampler(num_samples=1000)
                                vif.fit(ds.fit_transform(X_))
                            selected_columns.extend(vif.selected_columns)

                        final_selected_columns = []
                        for column in X_.columns:
                            if selected_columns.count(column) > 1:
                                print(column)
                                final_selected_columns.append(column)
                    except Exception as e:
                        final_selected_columns = params["feature_columns"]

                    # update X, and store the final_selected_features
                    X_ = X_[final_selected_columns]
                else:
                    final_selected_columns = params["feature_columns"]

                # timeseries split prepare
                X, y = check_X_y(X_, y_)

                finalX = X.copy()
                finaly = y.copy()

                X_train, X_test, y_train, y_test = train_test_split(
                    finalX,
                    finaly,
                    test_size=params["train_test_split"],
                    random_state=random_state,
                    shuffle=False,
                )

                CV = TimeSeriesKFoldSlidingSplit(n_splits=params["train_cv_split"])

                execution_type = ""
                stages = None

                # Dag type
                if params["dag_type"] == "Minimal":
                    # create DAG
                    stages = [
                        [("NoOp", NoOp()), ("MinMaxScaler", MinMaxScaler())],
                        [
                            ("linearregression", LinearRegression()),
                            ("ridge", Ridge(random_state=random_state)),
                            ("elasticnet", ElasticNet(random_state=random_state)),
                            ("lassolars", LassoLars(random_state=random_state)),
                        ],
                    ]
                    # execute_tye = 'default'
                    execution_type = "default"

                    # create a AutoReg here only
                elif params["dag_type"] == "Efficient":
                    # execute_tye = 'default'
                    execution_type = "default"
                    # set the execute_type
                    stages = None
                elif params["dag_type"] == "Comprehensive":
                    # execute_tye = ''
                    execution_type = "comprehensive"
                    stages = None
                else:
                    pass
                # DAG
                # minimal --> the one i provided for Demo, build the stage and pass it
                # efficient --> default
                # comprehensive ---> comprehensive

                if params["evaluation_metrics"] == "r2":
                    scoring_metric = "r2"
                elif params["evaluation_metrics"] == "mae":
                    scoring_metric = "neg_mean_absolute_error"
                elif params["evaluation_metrics"] == "mse":
                    scoring_metric = "neg_mean_squared_error"
                else:
                    scoring_metric = "r2"

                ar = AutoRegression(
                    level=execution_type,
                    scoring=scoring_metric,
                    total_execution_time=int(params["evaluation_time"]),
                    execution_time_per_pipeline=max(
                        1, int(params["evaluation_time"]) / 5
                    ),
                    execution_platform="single_node",
                    cv=CV,
                    stages=stages,
                )

                # use the cross validation
                # --> X-train, y-train

                # call the automate the process and get the results
                ar.automate(X_train, y_train)

                ar.best_estimator_so_far.fit(X_train, y_train)
                filename = ar.csv_filename
                results_csv = pd.read_csv(filename, sep="\t")
                cv_results = results_csv.sort_values(["best_scores"], ascending=False)[
                    ["best_estimator", "best_scores"]
                ].head(30)
                cv_results.columns = ["Pipeline", "Score"]
                cv_results = cv_results.dropna()
                top_pipelines = dict(cv_results.head(5).values)

                # export pipeline
                pickleMdl = pickle.dumps(ar.best_estimator_so_far)
                jsonMdl = base64.encodebytes(pickleMdl)

                try:
                    from mlprodict.onnx_conv import to_onnx
                
                    ppl = Pipeline(steps=[("estimator", ar.best_estimator_so_far)])
                    if ppl:
                        onnx_ppl = to_onnx(ppl, X_train[:1], options={id(ppl.steps[-1][0]): {'score_samples': True}})
                
                        exported_pipeline_onnx = onnx_ppl
                    else:
                        exported_pipeline_onnx = None
                    
                    jsonOnnxMdl = base64.encodebytes(exported_pipeline_onnx.SerializeToString())

                except Exception as ex:
                    LOGGER.debug(str(ex))
                    exported_pipeline_onnx = None

                # exported_pipeline_pickle = pickle.dumps(ar.best_estimator_so_far)

                # Get predictions
                predictions = ar.best_estimator_so_far.predict(X_test)

                actual = y_test

                from sklearn.metrics import (
                    r2_score,
                    mean_absolute_error,
                    mean_squared_error,
                )

                score = None
                if params["evaluation_metrics"] == "r2":
                    score = r2_score(actual, predictions)
                elif params["evaluation_metrics"] == "mae":
                    score = mean_absolute_error(actual, predictions)
                elif params["evaluation_metrics"] == "mse":
                    score = mean_squared_error(actual, predictions)

                result["score"] = score
                # result['anomaly_threshold'] = anomaly_threshold
                result["pickled_pipeline"] = jsonMdl.decode("ascii")
                result['onnx_pipeline'] = jsonOnnxMdl.decode("ascii")
                result["top5_pipelines"] = top_pipelines
                runtime = str(datetime.datetime.now() - starttime)
                result["total_execution_time"] = runtime
                result["predictions"] = list(predictions)
                result["ground_truth"] = list(actual.astype(float))
                result["features_selected"] = final_selected_columns
                result["dag_info"] = ar.summary()
                if params["data_profiler"]:
                    result["data_profile"] = str(_get_data_profile(df))
            elif job_name == "run_semi_supervised_anomaly_detection":
                validate_label_column = params["label_column"]
                trainDb = df.loc[df[params["train_validation_test_column"]] == 0]
                validateDb = df.loc[df[params["train_validation_test_column"]] == 1]
                testDb = df.loc[df[params["train_validation_test_column"]] == 2]

                trainX = trainDb[params["target_columns"]]
                validX = validateDb[params["target_columns"]]
                validy = validateDb[validate_label_column]
                testX = testDb[params["target_columns"]]
                testy = testDb[validate_label_column]

                # Rule-Density
                gam_if = GeneralizedAnomalyModel(
                    base_learner=IsolationForest(),
                    predict_function="decision_function",
                    score_sign=-1,
                )
                gam_gm = GeneralizedAnomalyModel(
                    base_learner=GaussianMixture(),
                    predict_function="score_samples",
                    score_sign=1,
                )
                gam_bgm = GeneralizedAnomalyModel(
                    base_learner=BayesianGaussianMixture(),
                    predict_function="score_samples",
                    score_sign=1,
                )
                gam_ocsvm = GeneralizedAnomalyModel(
                    base_learner=OneClassSVM(),
                    predict_function="decision_function",
                    score_sign=-1,
                )
                gam_nnam = GeneralizedAnomalyModel(
                    base_learner=NearestNeighborAnomalyModel(),
                    predict_function="predict",
                    score_sign=1,
                )
                gam_lof_nnam = GeneralizedAnomalyModel(
                    base_learner=LOFNearestNeighborAnomalyModel(),
                    predict_function="predict",
                    score_sign=1,
                )
                gam_pcaT2 = GeneralizedAnomalyModel(
                    base_learner=AnomalyPCA_T2(),
                    predict_function="anomaly_score",
                    score_sign=1,
                )
                gam_pcaQ = GeneralizedAnomalyModel(
                    base_learner=AnomalyPCA_Q(),
                    predict_function="anomaly_score",
                    score_sign=1,
                )
                # Covariance-Matrix
                gam_empirical = GeneralizedAnomalyModel(
                    base_learner=EmpiricalCovariance(),
                    fit_function="fit",
                    predict_function="mahalanobis",
                    score_sign=1,
                )
                gam_elliptic = GeneralizedAnomalyModel(
                    base_learner=EllipticEnvelope(),
                    fit_function="fit",
                    predict_function="mahalanobis",
                    score_sign=1,
                )
                gam_ledoitwolf = GeneralizedAnomalyModel(
                    base_learner=LedoitWolf(),
                    fit_function="fit",
                    predict_function="mahalanobis",
                    score_sign=1,
                )
                gam_mincovdet = GeneralizedAnomalyModel(
                    base_learner=MinCovDet(),
                    fit_function="fit",
                    predict_function="mahalanobis",
                    score_sign=1,
                )
                gam_OAS = GeneralizedAnomalyModel(
                    base_learner=OAS(),
                    fit_function="fit",
                    predict_function="mahalanobis",
                    score_sign=1,
                )
                gam_ShrunkCovariance = GeneralizedAnomalyModel(
                    base_learner=ShrunkCovariance(),
                    fit_function="fit",
                    predict_function="mahalanobis",
                    score_sign=1,
                )
                # Gaussian-Graphical
                ggm_Default = GaussianGraphicalModel()
                ggm_Stochastic = GaussianGraphicalModel(
                    distance_metric="Stochastic_Nearest_Neighbors"
                )
                ggm_KLDiverse = GaussianGraphicalModel(
                    distance_metric="KL_Divergence_Dist"
                )
                ggm_Frobenius = GaussianGraphicalModel(distance_metric="Frobenius_Norm")
                ggm_Likelihood = GaussianGraphicalModel(distance_metric="Likelihood")
                ggm_Spectral = GaussianGraphicalModel(distance_metric="Spectral")
                ggm_Mahalanobis_Distance = GaussianGraphicalModel(
                    distance_metric="Mahalanobis_Distance"
                )

                pipeline = AnomalyPipeline()
                stages = []

                # data_normalization = false, remove scaling
                if params["data_normalization"]:
                    stages.append(
                        [
                            ("skipscaling", NoOp()),
                            ("standardscaler", StandardScaler()),
                            ("robustscaler", RobustScaler()),
                            ("minmaxscaling", MinMaxScaler()),
                        ]
                    )
                else:
                    stages.append([("skipscaling", NoOp())])

                if params["model_category"] == "Rule-Density":
                    stages.append(
                        [
                            ("isolationforest", gam_if),
                            ("gaussianmixture", gam_gm),
                            ("bayesiangaussianmixture", gam_bgm),
                            ("oneclasssvm", gam_ocsvm),
                            ("nearestneighboranomalymodel", gam_nnam),
                            ("lofnearestneighboranomalymodel", gam_lof_nnam),
                            ("anomalypca_t2", gam_pcaT2),
                            ("anomalypca_q", gam_pcaQ),
                        ]
                    )
                elif params["model_category"] == "Covariance-Matrix":
                    stages.append(
                        [
                            ("empiricalcovariance", gam_empirical),
                            ("ellipticenvelope", gam_elliptic),
                            ("ledoitwolf", gam_ledoitwolf),
                            ("mincovdet", gam_mincovdet),
                            ("oas", gam_OAS),
                            ("shrunkcovariance", gam_ShrunkCovariance),
                        ]
                    )
                elif params["model_category"] == "Gaussian-Graphical":
                    stages.append(
                        [
                            ("ggm_default", ggm_Default),
                            ("ggm_stochastic", ggm_Stochastic),
                            ("ggm_kldiverse", ggm_KLDiverse),
                            ("ggm_frobenius", ggm_Frobenius),
                            ("ggm_likelihood", ggm_Likelihood),
                            ("ggm_spectral", ggm_Spectral),
                            ("ggm_mahalanobis_distance", ggm_Mahalanobis_Distance),
                        ]
                    )
                elif params["model_category"] == "All":
                    stages.append(
                        [
                            ("isolationforest", gam_if),
                            ("gaussianmixture", gam_gm),
                            ("bayesiangaussianmixture", gam_bgm),
                            ("oneclasssvm", gam_ocsvm),
                            ("nearestneighboranomalymodel", gam_nnam),
                            ("lofnearestneighboranomalymodel", gam_lof_nnam),
                            ("anomalypca_t2", gam_pcaT2),
                            ("anomalypca_q", gam_pcaQ),
                            ("empiricalcovariance", gam_empirical),
                            ("ellipticenvelope", gam_elliptic),
                            ("ledoitwolf", gam_ledoitwolf),
                            ("mincovdet", gam_mincovdet),
                            ("oas", gam_OAS),
                            ("shrunkcovariance", gam_ShrunkCovariance),
                            ("ggm_default", ggm_Default),
                            ("ggm_stochastic", ggm_Stochastic),
                            ("ggm_kldiverse", ggm_KLDiverse),
                            ("ggm_frobenius", ggm_Frobenius),
                            ("ggm_likelihood", ggm_Likelihood),
                            ("ggm_spectral", ggm_Spectral),
                            ("ggm_mahalanobis_distance", ggm_Mahalanobis_Distance),
                        ]
                    )

                pipeline.set_stages(stages)

                scoring_metric = None
                if params["evaluation_metrics"] == "auc":
                    scoring_metric = "roc_auc"
                elif params["evaluation_metrics"] == "f1":
                    scoring_metric = "anomaly_f1"
                elif params["evaluation_metrics"] == "accuracy":
                    scoring_metric = "anomaly_acc"
                elif params["evaluation_metrics"] == "precision-recall":
                    scoring_metric = "pr_auc"
                else:
                    scoring_metric = "anomaly_acc"

                pipeline.set_scoring(scoring_metric=scoring_metric)

                fine_param_grid = SROMParamGrid(gridtype="anomaly_detection_fine_grid")

                print("trainX", trainX.shape)
                print(trainX)
                print("validX", validX.shape)
                print(validX)
                print("validy", validy.shape)
                print(validy)
                output = pipeline.execute(
                    trainX=trainX,
                    validX=validX,
                    validy=validy,
                    verbosity="low",
                    param_grid=fine_param_grid,
                    exectype="single_node_random_search",
                    random_state=42,
                    n_jobs=2,
                    num_option_per_pipeline=params["model_parameters"],
                    total_execution_time=int(params["evaluation_time"]),
                )
                print("pipeline.best_estimator", pipeline.best_estimator)
                print("pipeline.best_score", pipeline.best_score)

                vscore = pipeline.score(validX, validy)
                print("vscore", vscore)
                anomaly_score = pipeline.predict_proba(testX)
                print("anomaly_score", anomaly_score)

                anomaly_label = pipeline.predict(testX)
                print("anomaly_label", anomaly_label)

                anomaly_threshold = pipeline.get_best_thresholds()
                print("anomaly_threshold", anomaly_threshold)

                top_pipelines = []
                for i, model in enumerate(pipeline.best_estimators):
                    top_pipelines.append([model, pipeline.best_scores[i]])

                # top_pipelines = Counter(top_pipelines).most_common()
                print("top_pipelines", top_pipelines)

                top_pipelines = (
                    pd.DataFrame(top_pipelines, columns=["Pipeline", "Score"])
                    .sort_values("Score", ascending=False)
                    .reset_index(drop=True)
                )
                top_pipelines = top_pipelines.values.tolist()
                top_pipelines = [(str(k.steps), v) for k, v in top_pipelines]
                print("top_pipelines", top_pipelines)

                result["best_pipeline"] = str(pipeline.best_estimator)
                result["best_score"] = pipeline.best_score

                result["anomaly_score"] = list(itertools.chain(*anomaly_score.tolist()))
                result["anomaly_label"] = list(itertools.chain(*anomaly_label.tolist()))
                result["anomaly_threshold"] = list(anomaly_threshold)
                # result['anomaly_threshold'] = anomaly_threshold
                result["top5_pipelines"] = top_pipelines[:5]
                runtime = datetime.datetime.now() - starttime
                result["total_execution_time"] = str(runtime)
            elif job_name == "run_mixture_model":
                X_ = df[params["feature_columns"]]
                random_state = 42

                # add the code here
                # if the unsupervised feature selector is on, we apply each of the feature selector and
                # then use the features that appear in atleast two feature selector methods
                # if the final feature selected is None, we may raise an error and then ask them to turn the flag off if it on
                if params["unsupervised_feature_selector"]:
                    # initalize the three FS
                    lvf = LowVarianceFeatureElimination()
                    vif = VarianceInflationFeatureSelection()
                    cor = CorrelatedFeatureElimination()
                    try:
                        lvf.fit(X_)
                        cor.fit(X_)
                        selected_columns = []
                        selected_columns.extend(lvf.selected_columns)
                        selected_columns.extend(cor.selected_columns)
                        if X_.shape[1] < 30:
                            if X_.shape[0] < 1000:
                                vif.fit(X_)
                            else:
                                ds = DataSampler(num_samples=1000)
                                vif.fit(ds.fit_transform(X_))
                            selected_columns.extend(vif.selected_columns)

                        final_selected_columns = []
                        for column in X_.columns:
                            if selected_columns.count(column) > 1:
                                print(column)
                                final_selected_columns.append(column)
                    except Exception as e:
                        final_selected_columns = params["feature_columns"]

                    # update X, and store the final_selected_features
                    X_ = X_[final_selected_columns]
                else:
                    final_selected_columns = params["feature_columns"]

                # timeseries split prepare
                X = check_array(X_)

                finalX = X.copy()

                print("finalX", finalX)

                if params["train_test_split"] == 0:
                    X_train, X_test = (finalX.copy(), finalX.copy())
                else:
                    X_train, X_test = train_test_split(
                        finalX,
                        test_size=params["train_test_split"],
                        random_state=random_state,
                        shuffle=False,
                    )
                print("X_train", X_train)
                print("X_train.shape", X_train.shape)
                print("X_test", X_test)
                print("X_test.shape", X_test.shape)

                CV = TimeSeriesKFoldSlidingSplit(n_splits=params["train_cv_split"])

                # Dag type
                execution_type = ""
                stages = None
                if params["dag_type"] == "Minimal":
                    # create DAG
                    stages = [
                        [
                            ("data_sampler_2", DataSampler(num_samples=2000)),
                            ("NoOp", NoOp()),
                        ],
                        [
                            ("gmm_1", GaussianMixture()),
                            (
                                "agglomerativeclustering_euclidean_ward",
                                AgglomerativeClustering(
                                    affinity="euclidean", linkage="ward"
                                ),
                            ),
                            ("gmm_3", GaussianMixture(n_components=3)),
                        ],
                    ]

                    execution_type = "default"

                    # create a AutoReg here only
                elif params["dag_type"] == "Efficient":
                    # execute_tye = 'default'
                    execution_type = "default"
                    # set the execute_type
                    stages = None
                elif params["dag_type"] == "Comprehensive":
                    # execute_tye = ''
                    execution_type = "comprehensive"
                    stages = None
                else:
                    pass
                # DAG
                # minimal --> the one i provided for Demo, build the stage and pass it
                # efficient --> default
                # comprehensive ---> comprehensive

                scoring_metric = params["evaluation_metrics"]

                gmm = AutoGMM(
                    level=execution_type,
                    scoring=scoring_metric,
                    total_execution_time=int(params["evaluation_time"]),
                    execution_time_per_pipeline=max(
                        2, int(params["evaluation_time"]) / 5
                    ),
                    execution_platform="single_node_random_search",
                    cv=CV,
                    stages=stages,
                )
                print("gmm", gmm)

                # use the cross validation
                # --> X-train, y-train

                # call the automate the process and get the results
                best_pipeline, best_score = gmm.automate(
                    X_train,
                )
                print("best_pipeline", best_pipeline)
                print("best_score", best_score)
                best_pipeline.fit(X_train)
                filename = gmm.csv_filename
                results_csv = pd.read_csv(filename, sep="\t")
                cv_results = results_csv.sort_values(["best_scores"], ascending=False)[
                    ["best_estimator", "best_scores"]
                ].head(30)
                cv_results.columns = ["Pipeline", "Score"]
                cv_results = cv_results.dropna()
                top_pipelines = dict(cv_results.head(5).values)

                # export pipeline
                pickleMdl = pickle.dumps(best_pipeline)
                jsonMdl = base64.encodebytes(pickleMdl)

                # Get predictions
                predictions = best_pipeline.predict(X_test)

                result["score"] = best_score
                # result['anomaly_threshold'] = anomaly_threshold
                result["pickled_pipeline"] = jsonMdl.decode("ascii")
                result["top5_pipelines"] = top_pipelines
                runtime = str(datetime.datetime.now() - starttime)
                result["total_execution_time"] = runtime
                result["predictions"] = {
                    "cluster_id": list(np.array(predictions).astype(float)),
                    "weights": str(list(best_pipeline.steps[-1][1].weights_)),
                    "means": list(best_pipeline.steps[-1][1].means_.tolist()),
                    "converged": str(best_pipeline.steps[-1][1].converged_),
                }
                result["features_selected"] = final_selected_columns
                result["dag_info"] = gmm.summary()
                if params["data_profiler"]:
                    result["data_profile"] = str(_get_data_profile(df))
            else:
                result = {
                    "error": "job {} is not configured in Anomaly Detection Service.".format(
                        job_name
                    )
                }
        except Exception as e:
            result = {"error": str(e)}

    print("Job {} {} is done.".format(jobId, job_name))

    # step 3: post-process result
    if "run_time" in result:
        result["total_execution_time (sec)"] = result["run_time"]  # rename run_time
    result.pop("run_time", None)  # remove run_time

    prediction_type = params.get("prediction_type", "")
    if prediction_type == "batch":
        prediction_type = "entire"

    # step 4: upload the result to cos
    try:
        obj = storage.get_object(bucket=result_bucket, key=result_filename)
        status_update = obj.decode("utf-8")
        status_update = json.loads(status_update)
        status_update["updated_on"]["done@"] = datetime.datetime.now(
            datetime.timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        status_update["status"] = JobAsyncStatus.done.value
        status_update["prediction_type"] = prediction_type
        status_update["param"] = params
        status_update["summary"] = result

        storage.put_object(
            bucket=credentials["result_bucket"],
            key=data_filename,
            body=bytes(json.dumps(status_update).encode("UTF-8")),
        )
        LOGGER.info("Result of job {} is uploaded.".format(jobId))

    except ClientError as be:
        LOGGER.error("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        LOGGER.error("Unable to create text file: {0}".format(e))

    return status_update
