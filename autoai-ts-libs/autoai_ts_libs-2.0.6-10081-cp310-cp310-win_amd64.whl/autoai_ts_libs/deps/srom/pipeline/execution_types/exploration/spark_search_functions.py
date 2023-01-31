"""Attempt to workaround serialization issues in spark search.
See 
 https://www.stefaanlippens.net/python-pickling-and-dealing-with-attributeerror-module-object-has-no-attribute-thing.html
"""
import logging
import time

import numpy as np
from sklearn.base import clone

LOGGER = logging.getLogger(__file__)

# basic function to do train_test_split
def train_test_score(tup, output):
    """
    Performs cross validation.

    Parameters:
        tup (tuple): Tuple containing parameters and pipeline_index.

    output:
        Shared resource for multiprocessing.
    """
    local_logger = logging.getLogger("train_test_learning")
    (
        parameters,
        pipeline_index,
        local_X,
        local_y,
        local_groups,
        local_pipeline,
        cross_val_score,
        cv,
        scorer,
        verbose,
    ) = tup

    fit_time, score_time = -1, -1
    try:
        local_pipeline.set_params(**parameters)
        if cross_val_score:
            scores = cross_val_score(
                local_pipeline,
                local_X,
                local_y,
                groups=local_groups,
                cv=cv,
                scoring=scorer,
                return_train_score=False,
                verbose=verbose,
            )
        else:
            from sklearn.model_selection import train_test_split

            stratify = None
            try:
                from sklearn.base import is_classifier

                if is_classifier(local_pipeline):
                    stratify = local_y
            except:
                pass

            X_train, X_test, y_train, y_test = train_test_split(
                local_X, local_y, random_state=33, test_size=0.1, stratify=stratify
            )
            start_time = time.time()
            local_pipeline.fit(X_train, y_train)
            fit_time = time.time() - start_time
            from sklearn.metrics import get_scorer

            start_time = time.time()
            scores = get_scorer(scorer)(local_pipeline, X_test, y_test)
            score_time = time.time() - start_time

        ret_result = (
            pipeline_index,
            (parameters, scores, np.NaN, fit_time, score_time),
        )
    except Exception as ex:
        local_logger.error(str(ex))
        ret_result = (pipeline_index, (parameters, np.NaN, np.NaN, np.NaN, np.NaN))
    output.put(ret_result)
    return

# basic function to do cv cross validations
def cv_learning(tup, output):
    """
    Performs cross validation.

    Parameters:
        tup (tuple): Tuple containing parameters and pipeline_index.

    output:
        Shared resource for multiprocessing.
    """
    local_logger = logging.getLogger("cv_learning")
    (
        parameters,
        pipeline_index,
        local_X,
        local_y,
        local_groups,
        local_pipeline,
        cross_val_score,
        cv,
        scorer,
        verbose,
    ) = tup

    try:
        local_pipeline.set_params(**parameters)
        if cross_val_score:
            scores = cross_val_score(
                local_pipeline,
                local_X,
                local_y,
                groups=local_groups,
                cv=cv,
                scoring=scorer,
                return_train_score=False,
                verbose=verbose,
            )
        else:
            from sklearn.model_selection import cross_validate

            scores = cross_validate(
                local_pipeline,
                local_X,
                local_y,
                groups=local_groups,
                cv=cv,
                scoring=scorer,
                return_train_score=False,
                verbose=verbose,
            )
        ret_result = (
            pipeline_index,
            (
                parameters,
                np.mean(scores["test_score"]),
                np.std(scores["test_score"]),
                np.std(scores["fit_time"]),
                np.std(scores["score_time"]),
            ),
        )
    except Exception as ex:
        local_logger.error(str(ex))
        ret_result = (pipeline_index, (parameters, np.NaN, np.NaN, np.NaN, np.NaN))
    output.put(ret_result)
    return



# basic function to do cv cross validations on windows
def cv_learning_window(tup, output):
    """
    Performs cross validation.

    Parameters:
        tup (tuple): Tuple containing parameters and pipeline_index.

    output:
        Shared resource for multiprocessing.
    """
    local_logger = logging.getLogger("cv_learning")
    (
        parameters,
        pipeline_index,
        local_X,
        local_y,
        local_groups,
        local_pipeline,
        cross_val_score,
        cv,
        scorer,
        verbose,
    ) = tup
    # = X_bc.value
    # local_y = y_bc.value
    # local_groups = groups_bc.value
    # local_pipelines = pipelines_bc.value

    try:
        local_pipeline.set_params(**parameters)
        if cross_val_score:
            scores = cross_val_score(
                local_pipeline,
                local_X,
                local_y,
                groups=local_groups,
                cv=cv,
                scoring=scorer,
                return_train_score=False,
                verbose=verbose,
            )
        else:
            from sklearn.model_selection import cross_validate

            scores = cross_validate(
                local_pipeline,
                local_X,
                local_y,
                groups=local_groups,
                cv=cv,
                scoring=scorer,
                return_train_score=False,
                verbose=verbose,
            )
        #print(scores["test_score"])
        ret_result = (
            pipeline_index,
            (
                parameters,
                np.mean(scores["test_score"]),
                np.std(scores["test_score"]),
                np.mean(scores["fit_time"]),
                np.mean(scores["score_time"]),
            ),
        )
    except Exception as ex:
        #print(ex)
        local_logger.error(str(ex))
        ret_result = (pipeline_index, (parameters, np.NaN, np.NaN, np.NaN, np.NaN))
    output.put(ret_result)
    return

def model_execution(
    tup,
    X_bc,
    y_bc,
    max_eval_time_minute_bc,
    groups_bc,
    pipelines_bc,
    cross_val_score,
    cv,
    scorer,
    verbose,
):
    """
    Performs time bound execution of pipeline. \
    If cv_learning task is not completed in max_eval_time_minute_bc minutes \
    then that task is terminated.

    Parameters:
        tup (tuple): (parameters, pipeline_index)
            parameters(list, dict): Pipeline grid combination parameters.
            pipeline_index (integer):Index for the pipeline for which cross \
                validation is to be executed.

    Returns: 
        Tuple (pipeline_index, (parameters, score)):
            pipeline_index (integer): Index for the pipeline for which cross \
                validation is to be executed.
            parameters (list, dict): Pipeline grid combination parameters.
            score (integer): Mean test score or nan if execution time exceeds \
                max_eval_time_minute_bc for processing.
    """
    (parameters, pipeline_index) = tup
    import multiprocessing as mp

    output = mp.Queue()
    ret_result = (pipeline_index, (parameters, np.NaN, np.NaN, np.NaN, np.NaN))
    import platform

    tup = (
        parameters,
        pipeline_index,
        X_bc.value,
        y_bc.value,
        groups_bc.value,
        clone(pipelines_bc.value[pipeline_index]),
        cross_val_score,
        cv,
        scorer,
        verbose,
    )
    if "Windows" in str(platform.platform()) or cv == 1:
        if cv == 1:
            train_test_score(tup, output)
        else:
            cv_learning_window(tup, output)
    else:
        cv_learning(tup, output)
        
    try:
        ret_result = output.get()
    except Exception as ex:
        LOGGER.error("Pipeline failed: %s", pipelines_bc.value[pipeline_index])
        LOGGER.error("Pipeline failed reason: %s", str(ex))
        LOGGER.exception(str(ex))
        pass
        
    return ret_result
