import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.pipeline.anomaly_pipeline import AnomalyPipeline
from autoai_ts_libs.deps.srom.utils.anomaly_dag import anomaly_dag
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
import math
import warnings


default_threshold_parameters = {
    "std": [{"std_threshold": 1.0}, {"std_threshold": 2.0}],
    "contamination": [{"contamination": 0.01}, {"contamination": 0.05}],
    "qfunction": [{"qfunction_threshold": 0.01}, {"qfunction_threshold": 0.05}],
    "medianabsolutedev": [
        {"medianabsolutedev_threshold": 2.5},
        {"medianabsolutedev_threshold": 3},
    ],
    "adaptivecontamination":  [{"adaptivecontamination_threshold": 0.01}, {"adaptivecontamination_threshold": 0.05}],
    "otsu": [{"std_threshold": 2.0}],
}


def retrive_base_learner(statsdf, index):
    """[summary]

    Args:
        statsdf ([type]): [description]
        index ([type]): [description]

    Returns:
        [type]: [description]
    """
    return statsdf[index][0].steps[-1][1].base_learner


def get_threshold_statistics(
    pipeline_output, X, number=1, threshold_parameters=None, max_eval_time_minute=1, total_execution_time=10, pipeline_index=0
):
    """[summary]

    Args:
        pipeline_output (required): Output from the `pipeline.execute` call containing results.
        X (np.array, required): Data to be passed
        number (int, optional): Number of pipelines to execute. Defaults to 1.
        threshold_parameters (dict, optional): Threshold parameters. Defaults to None.
        max_eval_time_minute (int, optional): Maximum evaluation time. Defaults to 1.
        total_execution_time (int, optional): total execution time propagated to SROMPipeline. Defaults to 10.
        pipeline_index (int, optional): Index of pipeline to be picked from list of `best_estimators`. If number>1,\
                        this does not have any effect. Defaults to 0.

    Returns:
        (flat_list, dataframe): Threshold statistics results
    """
    if threshold_parameters is None:
        threshold_parameters = default_threshold_parameters
    execution_res = []
    execution_i = 0
    for item in pipeline_output.best_estimators:
        if not math.isnan(pipeline_output.best_scores[execution_i]):
            execution_res.append([item, pipeline_output.best_scores[execution_i]])
        execution_i = execution_i + 1

    execution_res.sort(key=lambda x: x[1], reverse=True)

    top_estimators = []

    number = min(number, len(execution_res))
    if number == 1:
        if pipeline_index > len(execution_res):
            raise Exception("Pass a valid pipeline index lesser than the length of execution results")
        top_estimators.append(execution_res[pipeline_index][0].steps[-1][0])
        if len(execution_res[pipeline_index][0].steps) > 1:
            warnings.warn("Multi-step pipeline encountered. Threshold statistics will be computed only for the final"
                          "estimator.")

    else:
        for i in range(0, number):
            top_estimators.append(execution_res[i][0].steps[-1][0])
            if len(execution_res[pipeline_index][0].steps) > 1:
                warnings.warn(
                    "Multi-step pipeline encountered. Threshold statistics will be computed only for the final"
                    "estimator.")
    threshold_methods = (
        "std",
        "contamination",
        "adaptivecontamination",
        "qfunction",
        "medianabsolutedev",
        "otsu",
    )
    stages = []

    top_algo = [
        algo
        for algo in anomaly_dag
        for estm in top_estimators
        if (algo[3] == estm)
    ]

    execution_results = []
    for algorithm in top_algo:
        stages = (
            algorithm[3],
            GeneralizedAnomalyModel(
                base_learner=algorithm[0],
                fit_function="fit",
                predict_function=algorithm[2],
                score_sign=algorithm[1],
            ),
        )
        for method in threshold_methods:
            params = threshold_parameters[method]
            for param in params:
                supplied_param = "NA" if method == "otsu" else list(param.values())[0]
                param["anomaly_threshold_method"] = method
                fine_param_grid = SROMParamGrid(gridtype="anomaly_detection_fine_grid")
                pipeline = AnomalyPipeline(**param)
                pipeline.set_stages([[stages]])
                pipeline.set_param_grid(fine_param_grid)
                pipeline_output = pipeline.execute(
                    trainX=X,
                    validX=None,
                    validy=None,
                    verbosity="low",
                    param_grid=fine_param_grid,
                    exectype="spark_node_random_search",
                    num_option_per_pipeline=1,
                    max_eval_time_minute=max_eval_time_minute,
                    random_state=42,
                    total_execution_time=total_execution_time,
                )
                predictedX = pipeline.predict(X)
                predictprobaX = pipeline.predict_proba(X)

                execution_res = []
                non_anomaly = np.count_nonzero(predictedX == 1)
                anomaly = np.count_nonzero(predictedX == -1)
                pipeline_name = algorithm[3]
                execution_res.append(
                    [
                        pipeline.best_estimator,
                        predictedX,
                        predictprobaX,
                        method,
                        pipeline.get_best_thresholds()[0],
                        supplied_param,
                        anomaly,
                        non_anomaly,
                        pipeline_name,
                    ]
                )
                execution_results.append(execution_res)
        flat_list = [item for sublist in execution_results for item in sublist]

        df = pd.DataFrame(
            flat_list,
            columns=[
                "Pipeline",
                "prediction",
                "anomaly_score",
                "Method",
                "Detected Threshold",
                "Threshold",
                "Outliers",
                "Inliers",
                "pipeline_name",
            ],
        )
        df = df.reindex(
            columns=["Method", "Threshold", "Outliers", "Inliers", "Detected Threshold"]
        )
    return flat_list, df


def create_param_dict(threshold_method, threshold_value):
    param_dict = {"anomaly_threshold_method": threshold_method}

    if threshold_method not in ("contamination", "otsu"):
        param_dict[str(threshold_method) + str("_threshold")] = threshold_value
    elif threshold_method == "contamination":
        param_dict["contamination"] = threshold_value
    return param_dict


def estimator_comparison(
    pipeline_output,
    X,
    threshold_method,
    threshold_value,
    number=10,
    max_eval_time_minute=1,
    total_execution_time=10,
):
    """[summary]

    Args:
        pipeline_output ([type]): [description]
        X ([type]): [description]
        threshold_method ([type]): [description]
        threshold_value ([type]): [description]
        number (int, optional): [description]. Defaults to 10.
        max_eval_time_minute (int, optional): [description]. Defaults to 1.

    Returns:
        [type]: [description]
    """
    execution_res = []
    execution_i = 0
    for item in pipeline_output.best_estimators:
        if not math.isnan(pipeline_output.best_scores[execution_i]):
            execution_res.append([item, pipeline_output.best_scores[execution_i]])
        execution_i = execution_i + 1

    execution_res.sort(key=lambda x: x[1], reverse=True)

    top_estimators = []

    number = min(number, len(execution_res))
    for i in range(0, number):
        top_estimators.append(execution_res[i][0].steps[-1][0])
        if len(execution_res[i][0].steps) > 1:
            warnings.warn("Multi-step pipeline encountered. Estimator comparison will be computed only for the final"
                          "estimator.")

    top_algo = [
        algo
        for algo in anomaly_dag
        for estm in top_estimators
        if (algo[3] == estm)
    ]
    stages = []
    execution_res = []

    for algorithm in top_algo:
        stages = (
            algorithm[3],
            GeneralizedAnomalyModel(
                base_learner=algorithm[0],
                fit_function="fit",
                predict_function=algorithm[2],
                score_sign=algorithm[1],
            ),
        )

        fine_param_grid = SROMParamGrid(gridtype="anomaly_detection_fine_grid")
        param_dict = create_param_dict(threshold_method, threshold_value)
        pipeline = AnomalyPipeline(**param_dict)
        pipeline.set_stages([[stages]])
        pipeline.set_param_grid(fine_param_grid)
        pipeline_output = pipeline.execute(
            trainX=X,
            validX=None,
            validy=None,
            verbosity="low",
            param_grid=fine_param_grid,
            exectype="spark_node_random_search",
            num_option_per_pipeline=1,
            max_eval_time_minute=max_eval_time_minute,
            total_execution_time=total_execution_time,
            random_state=42,
        )
        anomaly_mean, anomaly_std = pipeline.generate_base_anomaly_score_statistics(X)
        predictedX = pipeline.predict(X)
        predictprobaX = pipeline.predict_proba(X)
        non_anomaly = np.count_nonzero(predictedX == 1)
        anomaly = np.count_nonzero(predictedX == -1)
        pipeline_name = str(algorithm[0]).split("(")[0]
        execution_res.append(
            [
                pipeline.best_estimator,
                predictedX,
                predictprobaX,
                pipeline.get_best_thresholds()[0],
                anomaly,
                non_anomaly,
                anomaly_mean[0],
                anomaly_std[0],
                pipeline_name,
            ]
        )
    df = pd.DataFrame(
        execution_res,
        columns=[
            "Pipeline",
            "prediction",
            "anomaly_score",
            "threshold",
            "Outliers",
            "Inliers",
            "Anomaly Mean",
            "Anomaly Std Dev",
            "Pipeline Name",
        ],
    )
    df = df.reindex(
        columns=[
            "Pipeline Name",
            "Outliers",
            "Inliers",
            "Anomaly Mean",
            "Anomaly Std Dev",
        ]
    )

    return execution_res, df
