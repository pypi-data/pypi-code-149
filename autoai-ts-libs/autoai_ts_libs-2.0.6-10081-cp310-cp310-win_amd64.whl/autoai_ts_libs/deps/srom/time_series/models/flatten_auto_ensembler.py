from autoai_ts_libs.deps.srom.time_series.pipeline import Forecaster
from sklearn.metrics._scorer import neg_mean_absolute_error_scorer
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.regression.auto_ensemble_regressor import EnsembleRegressor
from autoai_ts_libs.deps.srom.utils.regression_dag import get_flat_dag, get_multi_output_flat_dag
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator
from autoai_ts_libs.deps.srom.utils.estimator_utils import check_model_type_is_dl
from sklearn.model_selection import TimeSeriesSplit

import time


class FlattenAutoEnsembler(Forecaster):
    def __init__(
        self,
        feature_columns=None,
        target_columns=None,
        time_column=None,
        id_column=None,
        lookback_win=None,
        pred_win=None,
        store_lookback_history=False,
        scoring=neg_mean_absolute_error_scorer,
        total_execution_time=2,
        execution_time_per_pipeline=1,
        execution_platform="spark_node_random_search",  # "single_node"
        n_leaders_for_ensemble=1,
        n_estimators_for_pred_interval=30,
        max_samples_for_pred_interval=1.0,
        ensemble_type="voting",
        init_time_optimization=True,
        cv=None,
        n_jobs=-1,
    ):
        if len(target_columns) > 1 or pred_win > 1:
            dag = get_multi_output_flat_dag(n_jobs=n_jobs)
        else:
            dag = get_flat_dag()
        self.cv = cv
        super().__init__(
            steps=[
                ("flatten", Flatten()),
                (
                    "AutoEnsemble",
                    EnsembleRegressor(
                        stages=dag,
                        total_execution_time=total_execution_time,
                        execution_time_per_pipeline=execution_time_per_pipeline,
                        execution_platform=execution_platform,
                        n_leaders_for_ensemble=n_leaders_for_ensemble,
                        n_estimators_for_pred_interval=n_estimators_for_pred_interval,
                        max_samples_for_pred_interval=max_samples_for_pred_interval,
                        ensemble_type=ensemble_type,
                    ),
                ),
            ],
            feature_columns=feature_columns,
            target_columns=target_columns,
            time_column=time_column,
            id_column=id_column,
            lookback_win=lookback_win,
            pred_win=pred_win,
            store_lookback_history=store_lookback_history,
            scoring=scoring,
        )
        

