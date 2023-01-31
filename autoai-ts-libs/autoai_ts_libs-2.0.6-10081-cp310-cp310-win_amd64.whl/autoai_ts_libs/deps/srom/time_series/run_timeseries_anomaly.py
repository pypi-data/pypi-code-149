import argparse
import copy
import sys
import time
import traceback
from collections import Counter

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.model_selection import train_test_split
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.NMT_anomaly import NMT_anomaly
from autoai_ts_libs.deps.srom.preprocessing.transformer import DataStationarizer
from autoai_ts_libs.deps.srom.time_series.pipeline import PredAD, DeepAD
from autoai_ts_libs.deps.srom.time_series.utils.lookback import intelligent_lookback_window
from autoai_ts_libs.deps.srom.time_series.utils.reconstructad_pipeline_collection import (
    get_reconstructad_anomaly_estimator,
)
from autoai_ts_libs.deps.srom.time_series.utils.relationshipad_pipeline_collection import (
    get_relationshipad_anomaly_estimator,
)
from autoai_ts_libs.deps.srom.time_series.utils.tsp_pipeline_collection import generate_tsp_models
from autoai_ts_libs.deps.srom.time_series.utils.types import (
    TSPDAGType,
    AnomalyAlgorithmType,
    AnomalyScoringPredictionType,
    AnomalyScoringAlgorithmType,
    lookback_win_type,
    AnomalyAlgoAction,
    DagAction,
    AnomalyScoringAlgoAction,
    PredTypeAction,
    WindowADAlgorithmType,
    AnomalyEstimatorAction,
    AnomalyExecutionModeType,
    AnomalyExecutionModeAction,
    RelationshipADAlgorithmType,
    ReconstructADAlgorithmType,
)
from autoai_ts_libs.deps.srom.time_series.utils.windowad_pipeline_collection import (
    get_windowad_anomaly_estimator,
)
from autoai_ts_libs.deps.srom.utils.data_utils import is_present

# parameter for data testing
MAX_DATA_SIZE = 50000
MAX_COLUMN_SIZE = 100
MAX_MISSING_VALUES_RATIO = 0.1
MIN_DATA_SIZE = 50
OBSERVATION_WINDOW_SIZE = 0.1
UNIFORM_SAMPLING_THRESHOLD = 0.9  # this will need to be improved as time pass
DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def run_timeseries_anomaly_wrapper(
    data,
    execution_mode=AnomalyExecutionModeType.STREAM,
    train_test_split_ratio=1,
    feature_columns=None,
    target_columns=None,
    time_column=None,
    time_format=DEFAULT_TIME_FORMAT,
    algorithm_type=AnomalyAlgorithmType.DEEPAD,
    num_estimators=1,
    dag_type=TSPDAGType.BENCHMARK_ML,
    total_execution_time=240,
    execution_time_per_pipeline=-1,
    execution_type="single_node_random_search",
    lookback_win="auto",
    observation_window=10,
    scoring_method=AnomalyScoringAlgorithmType.CHISQUARE,
    scoring_threshold=10,
    prediction_type=AnomalyScoringPredictionType.RECENT,
    anomaly_estimator=WindowADAlgorithmType.ISOLATION_FOREST,
    n_jobs=4,
    from_service=False,
):
    # the following dic is storing the results
    results = {}
    start_time = time.time()

    # Splitting below code multple try except blocks to handle specific errors.
    try:
        # check data type
        if data is None:
            return {"error": "Input data should not be None"}

        if not isinstance(data, pd.DataFrame):
            return {
                "error": "Allowed input data structure is Pandas DataFrame where as given structure is {}".format(
                    type(data)
                )
            }

        # number of # row < 50k : 8
        if data.shape[0] > MAX_DATA_SIZE:
            return {
                "error": "Data size too large. Max data size accepted is {} data points".format(
                    MAX_DATA_SIZE
                )
            }

        # number of # row > 5 : 9
        if data.shape[0] < MIN_DATA_SIZE:
            return {
                "error": "Data size too small. Min data size accepted is {} data points".format(
                    MIN_DATA_SIZE
                )
            }

        # check input columns
        if not is_present(data.columns.tolist(), time_column):
            return {
                "error": "Provided time column '{}' is not part of data schema {}".format(
                    time_column, data.columns.tolist()
                )
            }

        if not is_present(data.columns.tolist(), feature_columns):
            return {
                "error": "Some or all of provided feature columns {} are not part of input data schema {}".format(
                    feature_columns, data.columns.tolist()
                )
            }

        if not is_present(data.columns.tolist(), target_columns):
            return {
                "error": "Some or all of provided target columns {} are not part of input data schema {}".format(
                    target_columns, data.columns.tolist()
                )
            }
    except Exception as ex:
        traceback.print_exc(file=sys.stdout)
        return {"error": "{}".format(ex)}

    try:
        if time_format is not None:
            data[time_column] = pd.to_datetime(data[time_column], format=time_format)
        else:
            if data[time_column].dtypes not in [
                np.int8,
                np.int16,
                np.int32,
                np.int64,
                np.int,
            ]:
                try:
                    data[time_column] = pd.to_datetime(
                        data[time_column], infer_datetime_format=True
                    )
                except:
                    return {
                        "error": "Time format of time column '{}' should either be one of numpy.int, numpy.int8, numpy.int16, numpy.int32, numpy.int64 or Pandas time format.. e.g. '{}'".format(
                            time_column, DEFAULT_TIME_FORMAT
                        )
                    }
    except:
        return {
            "error": "Provided time format '{}' does not match the format of time column in data: '{}'. Supported formats are: 'None' for any of numpy.int, numpy.int8, numpy.int16, numpy.int32, numpy.int64 and String for Pandas time format.. e.g. '{}'".format(
                time_format, data[time_column][0], DEFAULT_TIME_FORMAT
            )
        }

    try:
        # feature column and target column should be numeric: 2
        if not all(
            [is_numeric_dtype(data[feature]) for feature in feature_columns]
        ) and all([is_numeric_dtype(data[target]) for target in target_columns]):
            return {"error": "Feature columns and target columns need to be numeric"}

        # time column
        # no duplicate time column : 3
        if any(data[time_column].duplicated().values):
            return {
                "error": "Duplicate time values present in time column '{}'. Remove deplicate time values and try again.".format(
                    time_column
                )
            }

        # No infinite value : 4
        if np.isinf(data[feature_columns]).values.sum() > 0:
            return {
                "error": "Infinite values are present in some of the feature columns. Remove infinite values and try again."
            }

        # no constant feature columns : 5
        if not all(((data[feature_columns].nunique()) >= 1).values):
            return {
                "error": "Some of the feature columns are constant. Drop constant features and try again."
            }

        # missing % > 10% reject the call : 6
        if (
            ((data.isna().sum() > 0).values).sum() / data.shape[0]
        ) > MAX_MISSING_VALUES_RATIO:
            return {
                "error": "Data has too many missing values. Prepare data with missing values fewer than {} percent of data or no missing values and try again.".format(
                    MAX_MISSING_VALUES_RATIO * 100
                )
            }
        else:
            data.fillna(method="ffill", inplace=True)
            data.fillna(method="bfill", inplace=True)

        # number of # columns < 100 : 7
        if len(feature_columns) > MAX_COLUMN_SIZE:
            return {
                "error": "Data has too many feature columns, enter fewer than {} columns and try again".format(
                    MAX_COLUMN_SIZE
                )
            }

        # very large observation window : 10
        if observation_window > int(data.shape[0] * OBSERVATION_WINDOW_SIZE):
            return {
                "error": "Provided observation window size is too large. Please keep the value to smaller than "
                + str(OBSERVATION_WINDOW_SIZE * 100)
                + "%"
                + " of the data size and try again."
            }

        # sort the data (inplace or create a copy?)
        data = data.sort_values(by=time_column)

        # check the interval between adjacent time points, use atleast initial 5000 data point
        # to assess the data
        # check 11
        intervals = []
        for i in range(1, min(2000, data.shape[0])):
            if time_format is None:
                intervals.append((data[time_column][i] - data[time_column][i - 1]))
            else:
                intervals.append(
                    (data[time_column][i] - data[time_column][i - 1]).seconds
                )
        cnt = Counter(intervals)
        df_cnt = pd.DataFrame(sorted(cnt.items(), key=lambda x: x[1], reverse=True))
        df_cnt.columns = ["Interval", "Counts"]
        max_interval_count = list(df_cnt["Counts"])[0]
        if max_interval_count >= len(intervals) - 1:
            # data is alredy uniformaly samples
            pass
        elif (
            max_interval_count * 1.0 / len(intervals) >= UNIFORM_SAMPLING_THRESHOLD
            and time_format is not None
        ):
            # resampling only if the time_format is real timestamp
            max_interval = list(df_cnt["Interval"])[
                0
            ]  # this is an interval where the time series will be sampled
            data = data.resample(str(max_interval) + "S", on=time_column).mean()
            data.insert(loc=0, column=time_column, value=data.index)
            data.reset_index(drop=True, inplace=True)
            data.fillna(method="ffill", inplace=True)
        else:
            return {
                "error": "The initial check on data suggest that the time series is not regularly sampled. Correct the time sampling and try again."
            }

        # if code is able to come here, only after that point we call the remaining
        # prepare train and test data
        if execution_mode.value == "Stream":
            # we need to prepare train and test
            # data.dropna(inplace=True) (if there is still NA, we can do bfill)

            train_data, test_data = train_test_split(
                data, test_size=train_test_split_ratio, shuffle=False
            )
        elif execution_mode.value == "Batch":
            # train and test are identical
            train_data = data.copy()
            test_data = data.copy()
        else:
            return {
                "error": "Provided execution mode {} is not accepted. Accepted values are 'Batch' or 'Stream'".format(
                    execution_mode.value
                )
            }

        if (lookback_win == "auto") or (lookback_win is None):
            # call the lookback widnow method and set it
            feature_column_indices = [
                train_data.columns.tolist().index(col) for col in feature_columns
            ]
            target_column_indices = [
                train_data.columns.tolist().index(col) for col in target_columns
            ]

            lookbacks = {}
            methods = ["aic", "bic", "t-stat", "cv", "model-cv", "multi-stat"]

            for m in methods:
                lookbacks[m] = intelligent_lookback_window(
                    train_data.values,
                    feature_columns=feature_column_indices,
                    target_columns=target_column_indices,
                    approach=m,
                    max_lookback=50,
                )
            lookback_win = np.nanmax(list(lookbacks.values()))

        if lookback_win < 0:
            return {
                "error": "Provided lookback window {} is not accepted. Set lookback window to any positive integer lower than size of input data and try again.".format(
                    lookback_win
                )
            }
        elif lookback_win > train_data.shape[0]:
            return {
                "error": "Lookback window value should be lower than size of data to be used for training. Set lookback window to any positive integer lower than size of input data and try again."
            }
        else:
            pass

        # Invoke respective function call to build anomaly model and return anomalies.
        if algorithm_type in [AnomalyAlgorithmType.DEEPAD, AnomalyAlgorithmType.PREDAD]:
            # call deepad only and internally invoke predad for num_est=1
            num_estimators = 1 if algorithm_type == AnomalyAlgorithmType.PREDAD else 5
            results = run_timeseries_deepad(
                train_data=train_data,
                test_data=test_data,
                feature_columns=feature_columns,
                target_columns=target_columns,
                time_column=time_column,
                lookback_win=lookback_win,
                total_execution_time=total_execution_time,
                execution_time_per_pipeline=execution_time_per_pipeline,
                execution_type=execution_type,
                dag_type=dag_type,
                num_estimators=num_estimators,
                observation_window=observation_window,
                scoring_method=scoring_method,
                scoring_threshold=scoring_threshold,
                anomaly_prediction_type=prediction_type,
                n_jobs=n_jobs,
            )
        elif algorithm_type == AnomalyAlgorithmType.WINDOWAD:
            results = run_timeseries_windowad(
                train_data=train_data,
                test_data=test_data,
                time_column=time_column,
                feature_columns=feature_columns,
                target_columns=target_columns,
                lookback_win=lookback_win,
                observation_window=observation_window,
                scoring_method=scoring_method,
                scoring_threshold=scoring_threshold,
                prediction_type=prediction_type,
                return_threshold=True,
                anomaly_estimator=anomaly_estimator,
            )
        elif algorithm_type == AnomalyAlgorithmType.RELATIONSHIPAD:
            results = run_timeseries_relationshipAD(
                train_data=train_data,
                test_data=test_data,
                time_column=time_column,
                feature_columns=feature_columns,
                target_columns=target_columns,
                lookback_win=lookback_win,
                observation_window=observation_window,
                scoring_method=scoring_method,
                scoring_threshold=scoring_threshold,
                prediction_type=prediction_type,
                return_threshold=True,
                anomaly_estimator=anomaly_estimator,
            )
        elif algorithm_type == AnomalyAlgorithmType.RECONSTRUCTAD:
            results = run_timeseries_reconstructAD(
                train_data=train_data,
                test_data=test_data,
                time_column=time_column,
                feature_columns=feature_columns,
                target_columns=target_columns,
                lookback_win=lookback_win,
                observation_window=observation_window,
                scoring_method=scoring_method,
                scoring_threshold=scoring_threshold,
                prediction_type=prediction_type,
                return_threshold=True,
                anomaly_estimator=anomaly_estimator,
            )
    except Exception as ex:
        traceback.print_exc(file=sys.stdout)
        return {"error": "Error during training: {}.".format(ex)}
    end_time = time.time()
    # prepare results
    struct_results = []
    if "error" not in results:
        for i in range(len(results["predictions"])):

            # anomaly score
            if isinstance(results["anomaly_score"][i], np.float_):
                anomaly_score = [results["anomaly_score"][i]]
            else:
                anomaly_score = list(results["anomaly_score"][i])

            # predictions
            if isinstance(results["predictions"][i], np.float_):
                predictions = [results["predictions"][i]]
            else:
                predictions = list(results["predictions"][i])

            # anomaly_threshold
            if isinstance(results["anomaly_threshold"][i], np.float_):
                anomaly_threshold = [results["anomaly_threshold"][i]]
            else:
                anomaly_threshold = list(results["anomaly_threshold"][i])

            if scoring_method == AnomalyScoringAlgorithmType.IID:
                struct_results.append(
                    {
                        "timestamp": str(results["timestamps"][i]),
                        "value": {
                            "anomaly_score": anomaly_score,
                        },
                    }
                )
            else:
                if from_service:
                    struct_results.append(
                        {
                            "timestamp": str(results["timestamps"][i]),
                            "value": {
                                "anomaly_score": anomaly_score,
                                "anomaly_label": predictions,
                            },
                        }
                    )
                else:
                    struct_results.append(
                        {
                            "timestamp": str(results["timestamps"][i]),
                            "value": {
                                "anomaly_score": anomaly_score,
                                "anomaly_label": predictions,
                                "anomaly_threshold": anomaly_threshold,
                            },
                        }
                    )
        final_summary = {
            "run_time": str(end_time - start_time),
            "lookback_window": str(results["lookback_win"]),
            "model_summary": str(results["model_summary"]),
            "num_pipelines_explored": results["num_pipelines_explored"],
            "num_pipelines_finished": results["num_pipelines_finished"],
            "result": struct_results,
        }
    else:
        final_summary = {
            "run_time": "na",
            "lookback_window": "na",
            "model_summary": "na",
            "num_pipelines_explored": "na",
            "num_pipelines_finished": "na",
            "result": "na",
            "error": results["error"],
        }

    return final_summary


def run_timeseries_anomaly(
    dataName,
    execution_mode=AnomalyExecutionModeType.STREAM,
    train_test_split_ratio=1,
    feature_columns=None,
    target_columns=None,
    time_column=None,
    time_format="%Y-%m-%d %H:%M:%S",
    algorithm_type=AnomalyAlgorithmType.DEEPAD,
    num_estimators=1,
    dag_type=TSPDAGType.BENCHMARK_ML,
    total_execution_time=240,
    execution_time_per_pipeline=-1,
    execution_type="single_node_random_search",
    lookback_win=None,
    observation_window=10,
    scoring_method=AnomalyScoringAlgorithmType.CHISQUARE,
    scoring_threshold=10,
    prediction_type=AnomalyScoringPredictionType.RECENT,
    anomaly_estimator=WindowADAlgorithmType.ISOLATION_FOREST,
    outputdataName="",
    n_jobs=4,
):
    """
    Runs anomaly detection techniques such as (Deep)Prediction Based Anomaly and Window Based Anomaly
    Detection based on selection and returns anomaly scores based on selected anomaly score method.

    Parameters:
    ----------
        data (Pandas DataFrame or Numpy ndarray, required):
            Dataset to use. TODO: change to dataName
        execution_mode (String, optional):
            Service specif user's intent on Anomaly Discovery (Batch/Stream).
        train_test_split (Float, optional, default 1):
            Used to split dataset into train and test (for anomaly discovery)
            -1 for Batch
            1 for Stream
        feature_columns (List[String], optional):
            Feature column names in the dataset. Default is None.
        target_columns (String, optional):
            Target (anomaly label) column name in the dataset. Default is None.
        time_column (String, optional):
            Name of time column in the dataset. Default is None.
        time_format (String, optional):
            Format of time column in the dataset. Default is "%m-%d-%y"
        algorithm_type (String, optional):
            Type of Anomaly algorithm to be used. Default is 'DeepAD'
        outputdataName (String, optional):
            The place where to store the output
        ....
    """
    # load the data
    try:
        if isinstance(dataName, pd.DataFrame):
            data = dataName
        else:
            if dataName.endswith(".csv"):
                data = pd.read_csv(dataName)
            elif dataName.endswith(".json"):
                # need to check with shuxin on
                # orient='records' or orient=â€™indexâ€™
                data = pd.read_json(dataName)
            elif dataName.endswith(".csv.gz"):
                import gzip

                data = pd.read_csv(gzip.GzipFile(dataName, "rb"))
            else:
                return {"error": "provide a csv or a json file path"}
    except:
        return {"error": "provide valid data path"}

    try:
        ret_answer = run_timeseries_anomaly_wrapper(
            data,
            execution_mode=execution_mode,
            train_test_split_ratio=train_test_split_ratio,
            feature_columns=feature_columns,
            target_columns=target_columns,
            time_column=time_column,
            time_format=time_format,
            algorithm_type=algorithm_type,
            num_estimators=num_estimators,
            dag_type=dag_type,
            total_execution_time=total_execution_time,
            execution_time_per_pipeline=execution_time_per_pipeline,
            execution_type=execution_type,
            lookback_win=lookback_win,
            observation_window=observation_window,
            scoring_method=scoring_method,
            scoring_threshold=scoring_threshold,
            prediction_type=prediction_type,
            anomaly_estimator=anomaly_estimator,
            n_jobs=n_jobs,
        )
        if len(outputdataName) > 0:
            # here we store the output
            import json

            with open(outputdataName, "w") as fp:
                json.dump(ret_answer, fp)
        return ret_answer
    except Exception as ex:
        traceback.print_exc(file=sys.stdout)
        if len(outputdataName) > 0:
            # here we store the output
            import json

            with open(outputdataName, "w") as fp:
                json.dump({"error": "{}".format(ex)}, fp)
        return {"error": "{}".format(ex)}


def run_timeseries_deepad(
    train_data,
    test_data,
    feature_columns,
    target_columns,
    time_column,
    lookback_win=None,
    num_estimators=4,
    total_execution_time=240,
    execution_time_per_pipeline=-1,
    execution_type="single_node_random_search",
    dag_type=TSPDAGType.BENCHMARK_ML,
    observation_window=10,
    scoring_method=AnomalyScoringAlgorithmType.CHISQUARE,
    scoring_threshold=10,
    anomaly_prediction_type=AnomalyScoringPredictionType.RECENT,
    n_jobs=4,
):
    """
    Runs Deep Prediction Based Anomaly (DeepAD) and returns anomaly scores based on selected anomaly score method.

    Parameters:
    ----------
        data (Pandas DataFrame or Numpy ndarray, required):
            Dataset to use.
        train_test_split (Float, required):
            Used to split dataset into train and test
        feature_columns (List[String], optional):
            Feature column names in the dataset. Default is None.
        target_columns (String, optional):
            Target (anomaly label) column name in the dataset. Default is None.
        time_column (String, optional):
            Name of time column in the dataset. Default is None.
        time_format (String, optional):
            Format of time column in the dataset. Default is "%m-%d-%y"

        ....
    """
    results = {}
    start = time.time()

    backup_timestamps = copy.deepcopy(train_data[time_column].astype(str).values)
    train_data[time_column] = train_data[time_column].astype(int).astype(float)
    test_data[time_column] = test_data[time_column].astype(int).astype(float)
    time_column = train_data.columns.tolist().index(time_column)
    feature_columns = [
        train_data.columns.tolist().index(col) for col in feature_columns
    ]
    target_columns = [train_data.columns.tolist().index(col) for col in target_columns]

    if isinstance(train_data, pd.DataFrame):
        train_data = train_data.values

    if isinstance(test_data, pd.DataFrame):
        test_data = test_data.values

    # get best models using tsp
    best_models_scores, all_models_scores = generate_tsp_models(
        X=train_data,
        feature_columns=feature_columns,
        target_columns=target_columns,
        lookback_win=lookback_win,
        pred_win=1,
        dag_type=dag_type,
        total_execution_time=total_execution_time,
        execution_type=execution_type,
        store_lookback_history=True,
        num_estimators=num_estimators,
        n_jobs=n_jobs,
    )
    best_models = [i[0] for i in best_models_scores]
    all_models = [i[0] for i in all_models_scores]
    all_scores = [i[1] for i in all_models_scores]

    finished_pipelines = [
        all_models[indx] for indx in np.where(~np.isnan(all_scores))[0]
    ]

    if num_estimators == 1:
        pipeline = PredAD(
            steps=best_models[0].steps,
            lookback_win=lookback_win,
            feature_columns=feature_columns,
            target_columns=target_columns,
            time_column=None,
            store_lookback_history=True,
            pred_win=1,
            observation_window=observation_window,
            scoring_method=scoring_method.value,
            scoring_threshold=scoring_threshold,
        )

    else:
        predad_estimators = []
        num_models_to_use = min(num_estimators, len(best_models))
        for i in range(num_models_to_use):
            steps = best_models[i].steps
            predad_pipeline = PredAD(
                steps=steps,
                lookback_win=lookback_win,
                feature_columns=feature_columns,
                target_columns=target_columns,
                time_column=None,
                store_lookback_history=True,
                pred_win=1,
                observation_window=observation_window,
                scoring_method=scoring_method.value,
                scoring_threshold=scoring_threshold,
            )
            predad_estimators.append(predad_pipeline)
        pipeline = DeepAD(
            steps=predad_estimators,
            observation_window=observation_window,
            scoring_method=scoring_method.value,
            scoring_threshold=scoring_threshold,
        )
    pipeline.fit(train_data)
    if anomaly_prediction_type in [
        AnomalyScoringPredictionType.BATCH,
    ]:
        X = None
    else:
        X = test_data
    predictions = pipeline.predict(
        X,
        prediction_type=anomaly_prediction_type.value,
    )
    anomaly_scores, thresholds = pipeline.anomaly_score(
        X=X,
        prediction_type=anomaly_prediction_type.value,
        return_threshold=True,
    )
    if X is None:
        timestamps = train_data[:, time_column][-len(anomaly_scores) :]
    else:
        timestamps = X[:, time_column][-len(anomaly_scores) :]

    if (anomaly_prediction_type.name in ["SLIDING", "RECENT"]) and (
        scoring_method.name == "CONTEXTUAL_ANOMALY"
    ):
        if X is not None:
            all_timestamps = (
                train_data[:, time_column].tolist() + test_data[:, time_column].tolist()
            )
            timestamps = all_timestamps[-len(anomaly_scores) :]

    timestamps = backup_timestamps[-len(timestamps) :]
    results["timestamps"] = timestamps
    if num_estimators == 1:
        results["model_summary"] = get_sklearn_str_repr(pipeline)
    else:
        results["model_summary"] = get_sklearn_str_repr(pipeline.steps[0])
    results["run_time"] = time.time() - start
    results["anomaly_score"] = anomaly_scores
    results["anomaly_threshold"] = thresholds
    results["predictions"] = predictions
    results["lookback_win"] = lookback_win
    results["num_pipelines_explored"] = len(all_models)
    results["num_pipelines_finished"] = len(finished_pipelines)
    return results


def run_timeseries_windowad(
    train_data,
    test_data,
    time_column,
    feature_columns,
    target_columns,
    lookback_win=None,
    observation_window=10,
    scoring_method=AnomalyScoringAlgorithmType.CHISQUARE,
    scoring_threshold=10,
    prediction_type=AnomalyScoringPredictionType.RECENT,
    return_threshold=True,
    anomaly_estimator=WindowADAlgorithmType.ISOLATION_FOREST,
    data_stationarizer=True,
):
    """
    Runs Window Based Anomaly (WindowAD) and returns anomaly scores based on selected anomaly score method.

    Parameters:
    ----------
        data (Pandas DataFrame or Numpy ndarray, required):
            Dataset to use.
        train_test_split (Float, required):
            Used to split dataset into train and test
        feature_columns (List[String], optional):
            Feature column names in the dataset. Default is None.
        target_columns (String, optional):
            Target (anomaly label) column name in the dataset. Default is None.
        time_column (String, optional):
            Name of time column in the dataset. Default is None.
        time_format (String, optional):
            Format of time column in the dataset. Default is "%m-%d-%y"

        ....
    """
    results = {}
    start = time.time()
    backup_timestamps = copy.deepcopy(train_data[time_column].astype(str).values)
    time_column = train_data.columns.tolist().index(time_column)
    target_columns = [
        train_data[feature_columns].columns.tolist().index(col)
        for col in target_columns
    ]
    feature_columns_ind = [
        train_data[feature_columns].columns.tolist().index(col)
        for col in feature_columns
    ]

    # Move it out, ordered list of pipelines
    pipeline = get_windowad_anomaly_estimator(
        anomaly_estimator=anomaly_estimator.value,
        lookback_win=lookback_win,
        target_columns=target_columns,
        time_column=time_column,
        scoring_method=scoring_method.value,
        observation_window=observation_window,
        scoring_threshold=scoring_threshold,
    )

    # Fit the data
    pipeline.lookback_win = lookback_win
    if len(target_columns) > 1 or len(feature_columns) > 1:
        train_data = np.array(train_data[feature_columns])
        test_data = np.array(test_data[feature_columns])
    else:
        train_data = train_data[feature_columns].values.reshape(-1, 1)
        test_data = test_data[feature_columns].values.reshape(-1, 1)
    if data_stationarizer:
        if prediction_type in [
            AnomalyScoringPredictionType.BATCH,
        ]:
            ds_transformer = DataStationarizer(
                feature_columns=feature_columns_ind,
                target_columns=target_columns,
            )
            train_data_transformed = ds_transformer.fit_transform(train_data, y=None)
            if train_data.shape[0] != train_data_transformed.shape[0]:
                train_data = np.insert(
                    train_data_transformed, 0, [train_data_transformed[0]], axis=0
                )

            test_data_transformed = ds_transformer.transform(test_data)
            if test_data.shape[0] != test_data_transformed.shape[0]:
                test_data = np.insert(
                    test_data_transformed, 0, [test_data_transformed[0]], axis=0
                )

    pipeline.fit(train_data)
    # Predict based on prediction type
    if prediction_type in [
        AnomalyScoringPredictionType.BATCH,
    ]:
        X = None
    else:
        X = test_data
    predictions = pipeline.predict(
        X,
        prediction_type=prediction_type.value,
    )
    # Set anomaly scoring params
    pipeline.set_anomaly_scoring_params(
        scoring_method=scoring_method.value, scoring_threshold=scoring_threshold
    )
    anomalies = pipeline.anomaly_score(
        X,
        return_threshold=return_threshold,
        prediction_type=prediction_type.value,
    )
    end = time.time()
    # return threshold -> always true. Else anomalies cant be returned
    results["run_time"] = end - start
    if return_threshold:
        results["anomaly_score"] = anomalies[0]
        results["anomaly_threshold"] = anomalies[1]
    else:
        results["anomaly_score"] = anomalies
    results["predictions"] = predictions
    results["lookback_win"] = lookback_win
    if X is None:
        timestamps = train_data[:, time_column][-len(anomalies[0]) :]
    else:
        timestamps = X[:, time_column][-len(anomalies[0]) :]

    if (prediction_type.name in ["SLIDING", "RECENT"]) and (
        scoring_method.name == "CONTEXTUAL_ANOMALY"
    ):
        if X is not None:
            all_timestamps = (
                train_data[:, time_column].tolist() + test_data[:, time_column].tolist()
            )
            timestamps = all_timestamps[-len(anomalies[0]) :]

    timestamps = backup_timestamps[-len(timestamps) :]
    results["timestamps"] = timestamps
    results["model_summary"] = get_sklearn_str_repr(pipeline)
    results["num_pipelines_explored"] = 1
    results["num_pipelines_finished"] = 1
    return results


def run_timeseries_relationshipAD(
    train_data,
    test_data,
    feature_columns,
    target_columns,
    time_column=None,
    lookback_win=None,
    observation_window=10,
    scoring_method=AnomalyScoringAlgorithmType.IID,
    scoring_threshold=10,
    prediction_type=AnomalyScoringPredictionType.RECENT,
    return_threshold=True,
    anomaly_estimator=RelationshipADAlgorithmType.GMM_L1,
):
    """
    Runs Relationship Based Anomaly (RelationshipAD) and returns anomaly scores based on selected anomaly score method.

    Parameters:
    ----------
        data (Pandas DataFrame or Numpy ndarray, required):
            Dataset to use.
        train_test_split (Float, required):
            Used to split dataset into train and test
        feature_columns (List[String], optional):
            Feature column names in the dataset. Default is None.
        target_columns (String, optional):
            Target (anomaly label) column name in the dataset. Default is None.
        time_column (String, optional):
            Name of time column in the dataset. Default is None.
        time_format (String, optional):
            Format of time column in the dataset. Default is "%m-%d-%y"

        ....
    """
    # check scoring method and only approve for IID (since others dont support multivariate)
    if scoring_method != AnomalyScoringAlgorithmType.IID:
        return {"error": "RelationshipAD requires Anomaly Scoring Method to be IID"}
    results = {}
    start = time.time()
    backup_timestamps = copy.deepcopy(train_data[time_column].astype(str).values)
    time_column = train_data.columns.tolist().index(time_column)
    target_columns = [
        train_data[feature_columns].columns.tolist().index(col)
        for col in target_columns
    ]
    feature_columns_ind = [
        train_data[feature_columns].columns.tolist().index(col)
        for col in feature_columns
    ]
    # Move it out, ordered list of pipelines
    pipeline = get_relationshipad_anomaly_estimator(
        feature_columns=feature_columns,
        anomaly_estimator=anomaly_estimator.value,
        lookback_win=lookback_win,
        target_columns=target_columns,
        time_column=time_column,
        scoring_method=scoring_method.value,
        observation_window=observation_window,
        scoring_threshold=scoring_threshold,
    )

    # Fit the data
    pipeline.lookback_win = lookback_win
    if len(target_columns) > 1 or len(feature_columns) > 1:
        train_data = np.array(train_data[feature_columns])
        test_data = np.array(test_data[feature_columns])
    else:
        train_data = train_data[feature_columns].values.reshape(-1, 1)
        test_data = test_data[feature_columns].values.reshape(-1, 1)
    pipeline.steps[0][1].feature_columns = feature_columns_ind
    pipeline.feature_columns = feature_columns_ind

    pipeline.fit(train_data)
    # Predict based on prediction type
    if prediction_type in [
        AnomalyScoringPredictionType.BATCH,
    ]:
        X = None
    else:
        X = test_data
    predictions = pipeline.predict(
        X,
        prediction_type=prediction_type.value,
    )
    # Set anomaly scoring params
    pipeline.set_anomaly_scoring_params(
        scoring_method=scoring_method.value, scoring_threshold=scoring_threshold
    )
    anomalies = pipeline.anomaly_score(
        X,
        return_threshold=return_threshold,
        prediction_type=prediction_type.value,
    )
    end = time.time()
    # return threshold -> always true. Else anomalies cant be returned
    results["run_time"] = end - start
    if return_threshold:
        results["anomaly_score"] = anomalies[0]
        results["anomaly_threshold"] = anomalies[1]
    else:
        results["anomaly_score"] = anomalies
    results["predictions"] = predictions
    results["lookback_win"] = lookback_win
    if X is None:
        timestamps = train_data[:, time_column][-len(anomalies[0]) :]
    else:
        timestamps = X[:, time_column][-len(anomalies[0]) :]

    if (prediction_type.name in ["SLIDING", "RECENT"]) and (
        scoring_method.name == "CONTEXTUAL_ANOMALY"
    ):
        if X is not None:
            all_timestamps = (
                train_data[:, time_column].tolist() + test_data[:, time_column].tolist()
            )
            timestamps = all_timestamps[-len(anomalies[0]) :]

    timestamps = backup_timestamps[-len(timestamps) :]
    results["timestamps"] = timestamps
    results["model_summary"] = get_sklearn_str_repr(pipeline)
    results["num_pipelines_explored"] = 1
    results["num_pipelines_finished"] = 1
    return results


def run_timeseries_reconstructAD(
    train_data,
    test_data,
    feature_columns,
    target_columns,
    time_column=None,
    lookback_win=None,
    observation_window=10,
    scoring_method=AnomalyScoringAlgorithmType.CHISQUARE,
    scoring_threshold=10,
    prediction_type=AnomalyScoringPredictionType.RECENT,
    return_threshold=True,
    anomaly_estimator=ReconstructADAlgorithmType.DNN_AE,
):
    """
    Runs Reconstruction Based Anomaly (ReconstructAD) and returns anomaly scores based on selected anomaly score method.

    Parameters:
    ----------
        data (Pandas DataFrame or Numpy ndarray, required):
            Dataset to use.
        train_test_split (Float, required):
            Used to split dataset into train and test
        feature_columns (List[String], optional):
            Feature column names in the dataset. Default is None.
        target_columns (String, optional):
            Target (anomaly label) column name in the dataset. Default is None.
        time_column (String, optional):
            Name of time column in the dataset. Default is None.
        time_format (String, optional):
            Format of time column in the dataset. Default is "%m-%d-%y"

    """
    results = {}
    start = time.time()
    backup_timestamps = copy.deepcopy(train_data[time_column].astype(str).values)
    time_column = train_data.columns.tolist().index(time_column)
    target_columns = [
        train_data[feature_columns].columns.tolist().index(col)
        for col in target_columns
    ]
    feature_columns_ind = [
        train_data[feature_columns].columns.tolist().index(col)
        for col in feature_columns
    ]
    # Move it out, ordered list of pipelines
    pipeline = get_reconstructad_anomaly_estimator(
        feature_columns=feature_columns_ind,
        anomaly_estimator=anomaly_estimator.value,
        lookback_win=lookback_win,
        target_columns=target_columns,
        time_column=time_column,
        scoring_method=scoring_method.value,
        observation_window=observation_window,
        scoring_threshold=scoring_threshold,
        store_lookback_history=True
    )

    # Fit the data
    pipeline.lookback_win = lookback_win
    if len(target_columns) > 1 or len(feature_columns) > 1:
        train_data = np.array(train_data[feature_columns])
        test_data = np.array(test_data[feature_columns])
    else:
        train_data = train_data[feature_columns].values.reshape(-1, 1)
        test_data = test_data[feature_columns].values.reshape(-1, 1)
    if isinstance(pipeline.steps[-1][1], NMT_anomaly):
        pipeline.steps[0][1].feature_columns = feature_columns_ind
        pipeline.feature_columns = feature_columns_ind
    if anomaly_estimator == ReconstructADAlgorithmType.CNN:
        try:
            pipeline.fit(train_data)
        except:
            raise Exception("Lookback window not compatible with input dim of CNN")
    else:
        pipeline.fit(train_data)
    # Predict based on prediction type
    if prediction_type in [
        AnomalyScoringPredictionType.BATCH,
    ]:
        X = None
    else:
        X = test_data
    predictions = pipeline.predict(
        X,
        prediction_type=prediction_type.value,
    )
    # Set anomaly scoring params
    pipeline.set_anomaly_scoring_params(
        scoring_method=scoring_method.value, scoring_threshold=scoring_threshold
    )
    anomalies = pipeline.anomaly_score(
        X,
        return_threshold=return_threshold,
        prediction_type=prediction_type.value,
    )
    end = time.time()
    # return threshold -> always true. Else anomalies cant be returned
    results["run_time"] = end - start
    if return_threshold:
        results["anomaly_score"] = anomalies[0]
        results["anomaly_threshold"] = anomalies[1]
    else:
        results["anomaly_score"] = anomalies
    results["predictions"] = predictions
    results["lookback_win"] = lookback_win
    if X is None:
        timestamps = train_data[:, time_column][-len(anomalies[0]) :]
    else:
        timestamps = X[:, time_column][-len(anomalies[0]) :]

    if (prediction_type.name in ["SLIDING", "RECENT"]) and (
        scoring_method.name == "CONTEXTUAL_ANOMALY"
    ):
        if X is not None:
            all_timestamps = (
                train_data[:, time_column].tolist() + test_data[:, time_column].tolist()
            )
            timestamps = all_timestamps[-len(anomalies[0]) :]

    timestamps = backup_timestamps[-len(timestamps) :]
    results["timestamps"] = timestamps
    pipeline.steps[1] = (pipeline.steps[1][0], pipeline.steps[1][1].__str__())
    results["model_summary"] = get_sklearn_str_repr(pipeline)
    results["num_pipelines_explored"] = 1
    results["num_pipelines_finished"] = 1
    return results


def get_sklearn_str_repr(sk_pipeline):
    str_rep = "["
    for sI in sk_pipeline.steps:
        str_rep = str_rep + str(sI) + ","
    str_rep = str_rep + "]"
    return str_rep.replace("\n", "").replace("\t", "").replace(" ", "")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-df",
        "--dataName",
        type=str,
        default="./price.csv",
        help="Name or full path of time series datafile",
    )
    parser.add_argument(
        "-output_df",
        "--outputdataName",
        type=str,
        default="",
        help="Name or full path of output place",
    )
    parser.add_argument(
        "-em",
        "--execution_mode",
        default=AnomalyExecutionModeType.BATCH,
        action=AnomalyExecutionModeAction,
        choices=["STREAM", "BATCH"],
        help="Run in 'BATCH','STREAM' or '...' mode",
    )
    parser.add_argument(
        "-sp",
        "--train_test_split_ratio",
        type=str,
        default="0.7",
        help="Ratio of train-test split",
    )
    parser.add_argument(
        "-fc",
        "--feature_columns",
        type=str,
        nargs="+",
        default=["sensor_1"],
        help="List of names of the feature columns",
    )
    parser.add_argument(
        "-tc",
        "--target_columns",
        type=str,
        nargs="+",
        default=["sensor_1"],
        help="List of names of the feature columns",
    )
    parser.add_argument(
        "-tmc",
        "--time_column",
        type=str,
        default="Time",
        help="Name of the time column",
    )
    parser.add_argument(
        "-tf",
        "--time_format",
        type=str,
        default="%Y-%m-%d %H:%M:%S",
        help="Format of the time column",
    )
    parser.add_argument(
        "-al",
        "--algorithm_type",
        default=AnomalyAlgorithmType.DEEPAD,
        action=AnomalyAlgoAction,
        choices=["DEEPAD", "WINDOWAD"],
        help="Type of algorithm to use among [DEEPAD, WINDOWAD]",
    )
    parser.add_argument(
        "-n",
        "--num_estimators",
        type=int,
        default=4,
        help="Number of models/estimators to use",
    )
    parser.add_argument(
        "-dt",
        "--dag_type",
        default=TSPDAGType.EXT_ML,
        action=DagAction,
        choices=["EXT_ML", "STATS", "BENCHMARK_ML", "DL", "TS_DL"],
        help="Type of algorithm to use among [EXT_ML, STATS, BENCHMARK_ML, DL, TS_DL]",
    )
    parser.add_argument(
        "-te",
        "--total_execution_time",
        type=int,
        default=240,
        help="Total execution time allowed to explore models/estimators",
    )
    parser.add_argument(
        "-et",
        "--execution_type",
        type=str,
        default="single_node_random_search",
        choices=["single_node_random_search"],
        help="Execution type to use to explore models/estimators among [single_node_random_search]",
    )
    parser.add_argument(
        "-lb",
        "--lookback_win",
        type=lookback_win_type,
        default="auto",
        help="Lookback window or steps of previous indices to consider",
    )
    parser.add_argument(
        "-ob",
        "--observation_window",
        type=int,
        default=10,
        help="Observation window to use during anomaly detection",
    )
    parser.add_argument(
        "-sc",
        "--scoring_method",
        default=AnomalyScoringAlgorithmType.CHISQUARE,
        choices=[
            "CHISQUARE",
            "IID",
            "QSCORE",
            "SLIDING_WINDOW",
            "ADAPTIVE_SLIDING_WINDOW",
            "CONTEXTUAL_ANOMALY",
        ],
        action=AnomalyScoringAlgoAction,
        help='Scoring method to use among ["CHISQUARE", "IID", "QSCORE", "SLIDING_WINDOW", "ADAPTIVE_SLIDING_WINDOW", "CONTEXTUAL_ANOMALY",]',
    )
    parser.add_argument(
        "-st",
        "--scoring_threshold",
        type=float,
        default=10,
        help="Threshold to use for scoring anomalies",
    )
    parser.add_argument(
        "-pt",
        "--prediction_type",
        default=AnomalyScoringPredictionType.RECENT,
        action=PredTypeAction,
        choices=["TRAINING", "RECENT", "BATCH", "SLIDING"],
        help='Prediction type to use among ["TRAINING", "RECENT", "BATCH", "SLIDING"]',
    )
    parser.add_argument(
        "-ae",
        "--anomaly_estimator",
        default=WindowADAlgorithmType.ISOLATION_FOREST,
        action=AnomalyEstimatorAction,
        choices=[
            "ISOLATION_FOREST",
            "NEAREST_NEIGHBOR",
            "ELLIPTIC_ENVELOPE",
            "MIN_COV_DET",
            "ANOMALY_ENSEMBLER",
        ],
        help="Anomaly model estimator to perform windowAD, among ['ISOLATION_FOREST','NEAREST_NEIGHBOR',"
        "'ELLIPTIC_ENVELOPE','MIN_COV_DET','ANOMALY_ENSEMBLER']",
    )

    """
    ---- add the other argument here
    """
    args = vars(parser.parse_args())
    print("run parameters are: " + str(args))
    print("results: {}".format(run_timeseries_anomaly(**args)))
    import multiprocessing as mp

    print("num cpus: " + str(mp.cpu_count()))


if __name__ == "__main__":
    if __name__ == "__main__":
        """
        Run from CLI:
            python run_time_series_anomaly.py -rm 'Batch' -df 'price'
        """

        start_time = time.time()
        main()
        print("\n\n== DONE with TOTAL TIME: %d seconds" % (time.time() - start_time))
