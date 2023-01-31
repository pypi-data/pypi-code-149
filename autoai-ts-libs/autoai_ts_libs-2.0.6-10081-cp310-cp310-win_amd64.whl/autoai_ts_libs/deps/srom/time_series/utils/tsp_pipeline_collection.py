from autoai_ts_libs.deps.srom.time_series.utils.types import TSPDAGType
from autoai_ts_libs.deps.srom.pipeline.time_series_prediction import TimeSeriesPredictionPipeline
import numpy as np
from autoai_ts_libs.deps.srom.model_selection import TimeSeriesTrainTestSplit


def generate_tsp_models(
    X,
    feature_columns,
    target_columns,
    lookback_win,
    pred_win=1,
    y=None,
    dag_type=TSPDAGType.BENCHMARK_ML,
    total_execution_time=3,
    execution_type="single_node_random_search",
    store_lookback_history=True,
    num_estimators=5,
    n_jobs=8,
):
    """[summary]

    Args:
        X ([type]): [description]
        feature_columns ([type]): [description]
        target_columns ([type]): [description]
        lookback_win ([type]): [description]
        pred_win (int, optional): [description]. Defaults to 1.
        y ([type], optional): [description]. Defaults to None.
        dag_type ([type], optional): [description]. Defaults to TSPDAGType.STATS.
        total_execution_time (int, optional): [description]. Defaults to 240.
        execution_type (str, optional): [description]. Defaults to "single_node_random_search".
        store_lookback_history (bool, optional): [description]. Defaults to True.
        num_estimators (int, optional): [description]. Defaults to 5.
        n_jobs (int, optional): [description]. Defaults to 8.

    Returns:
        [type]: [description]
    """
    pred_win = 1
    Xt = X.copy()
    # step 1, Reduce the size of X for training
    if Xt.shape[0] > 2000:
        Xt = np.array(Xt)
        Xt = Xt[-2000:, :]

    # step 2, set the ts split to train and test split for TSP
    # make sure to use TimeSeriesSplit (n_split = 1)
    # use srom.model_selection with split = 1
    # now call the following pipeline on 2000 data points
    # we know the
    ts_cv = TimeSeriesTrainTestSplit(n_test_size=20)

    # Avoid MultiOutputRegressor for uni-variate output.
    if ("BENCHMARK_ML" in dag_type.name):
        if (len(target_columns) > 1):
            dag_type = TSPDAGType.BENCHMARK_ML_MULTI_OUTPUT
        else:
            dag_type = TSPDAGType.BENCHMARK_ML
    elif ("STAT" in dag_type.name): # Avoid univaraite output for multi-variate scenarios
        if (len(target_columns) > 1):
            dag_type = TSPDAGType.STATS_MULTI_OUTPUT
        else:
            dag_type = TSPDAGType.STATS

    tmp_stages = dag_type.value

    # step 3, check the negative number and remove some transformers from DAG
    if np.any(Xt[:, target_columns] < 0):
        component_to_be_removed = ["Sqrt", "Reciprocal", "Anscombe"]
        new_dag = []
        for _, stage in enumerate(tmp_stages):
            new_stage = []
            for _, dag_step in enumerate(stage):
                if dag_step[0] not in component_to_be_removed:
                    new_stage.append(dag_step)
            new_dag.append(new_stage)
        tmp_stages = new_dag

    # Step 4, check the zero values and remove some transformers from DAG
    # Not implemented

    # Step 5, check the lookback window and remove some estimators from DAG
    component_to_be_removed = ["HuberRegressor", "RandomForestRegressor"]
    component_to_be_removed_condition = {
        "HuberRegressor": 10,
        "RandomForestRegressor": 100,
    }
    new_dag = []
    for _, stage in enumerate(tmp_stages):
        new_stage = []
        for _, dag_step in enumerate(stage):
            if dag_step[0] in component_to_be_removed:
                if lookback_win < component_to_be_removed_condition[dag_step[0]]:
                    new_stage.append(dag_step)
            else:
                new_stage.append(dag_step)
        new_dag.append(new_stage)
    tmp_stages = new_dag

    # step 6, very large numbers (1000000) ?? eliminate some estimators (such as Skip-- we must
    # normalize the large number either by log or difference)
    component_to_be_removed = ["SkipTransformer"]
    if np.any(Xt[:, target_columns] > 100000):
        new_dag = []
        for _, stage in enumerate(tmp_stages):
            new_stage = []
            for _, dag_step in enumerate(stage):
                if dag_step[0] not in component_to_be_removed:
                    new_stage.append(dag_step)
            new_dag.append(new_stage)
        tmp_stages = new_dag

    # step 3, 4, 5 and 6 , modify the dag_type.value so it can be further reduced

    tsp_dag = TimeSeriesPredictionPipeline(
        feature_columns=feature_columns,
        target_columns=target_columns,
        lookback_win=lookback_win,
        pred_win=pred_win,
        store_lookback_history=store_lookback_history,
    )
    tsp_dag.add_stages(tmp_stages)
    tsp_dag.set_cross_validation(ts_cv)
    tsp_dag.execute(
        X,
        verbosity="high",
        total_execution_time=total_execution_time,
        max_eval_time_minute=-1,
        n_jobs=n_jobs,
        exectype=execution_type,
    )
    # we expect the execution shd be fast

    finished_pipelines = [
        tsp_dag.best_estimators[indx]
        for indx in np.where(~np.isnan(tsp_dag.best_scores))[0]
    ]
    finished_pipeline_scores = [
        tsp_dag.best_scores[indx]
        for indx in np.where(~np.isnan(tsp_dag.best_scores))[0]
    ]
    sorted_tuples = []
    for i, model in enumerate(tsp_dag.best_estimators):
        sorted_tuples.append([model, tsp_dag.best_scores[i]])
    sorted_tuples = sorted(
        sorted_tuples, key=lambda x: (not (np.isnan(x[1])), x[1]), reverse=True
    )

    # due to what-ever reason, if following code fail,
    # we must return an empty or raise a warning or select the default value
    return sorted_tuples[:num_estimators], sorted_tuples


def explore_pipelines_for_predad(
    *,
    train_data,
    feature_columns,
    target_columns,
    lookback_win,
    dag_type,
    total_execution_time,
    execution_type,
    num_estimators,
    store_lookback_history=True
):
    best_models_scores, all_models_scores = generate_tsp_models(
        X=train_data,
        feature_columns=feature_columns,
        target_columns=target_columns,
        lookback_win=lookback_win,
        pred_win=1,
        dag_type=dag_type,
        total_execution_time=total_execution_time,
        execution_type=execution_type,
        store_lookback_history=store_lookback_history,
        num_estimators=num_estimators,
    )
    best_models = [i[0] for i in best_models_scores]
    return best_models
