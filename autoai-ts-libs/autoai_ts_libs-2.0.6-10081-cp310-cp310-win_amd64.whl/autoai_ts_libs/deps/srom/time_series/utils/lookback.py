import statistics
from math import log

import numpy as np
import pandas as pd
from scipy.stats import t
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from autoai_ts_libs.deps.srom.model_selection import TimeSeriesKFoldSlidingSplit
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.time_series.utils.period_detection import generalized_cross_validation_error
from autoai_ts_libs.deps.srom.utils.time_series_utils import recommend_lookback_MTS


def intelligent_lookback_window(
    X,
    feature_columns=[0],
    target_columns=[0],
    time_column=None,
    approach="aic",
    max_lookback=50,
    min_lookback=1,
    pred_win=1,
):
    """
    Detects the best lookback window for timeseries dataset based on various approaches.

    Parameters:
        X (pandas dataframe or numpy array, required): shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        feature_columns (numpy array): feature indices
        target_columns (numpy array): target indices
        time_column (str): The column name of time values.
        approach (string): Approach for calculating lookback window
            - `aic`: The Akaike information criterion is an estimator of prediction error 
                and thereby relative quality of statistical models for a given set of data.
                https://en.wikipedia.org/wiki/Akaike_information_criterion
            - `bic`: Bayesian information criterion
                https://en.wikipedia.org/wiki/Bayesian_information_criterion
            - `model-cv`: 5-fold model crossvalidation MAE error minimization
            - `t-stat`: Feature significance based approach by finding the p-value 
                of different lookbacks
            - `cv`: period based evalution of MSE for different lookbacks.
            - `multi-stat`: Multiple Statistics based Combination

    Returns:
        lookback value (int): integer value denoting lookback window value.
    """
    n = len(X)

    max_lag = max_lookback
    if max_lag >= n:
        max_lag = n-1

    if min_lookback > max_lookback:
        raise ValueError("value of min_lookback should be less than max_lookback")

    if min_lookback > max_lookback:
        return min_lookback

    if approach in ["bic", "aic"]:
        # approach for bic/aic based method
        scores = []
        for i in range(1, max_lag):
            flatten = Flatten(
                feature_columns=feature_columns,
                target_columns=target_columns,
                lookback_win=i,
                pred_win=pred_win,
            )
            lr = LinearRegression()
            Xt_train, yt_train = flatten.fit_transform(X)
            lr.fit(Xt_train, yt_train)
            y_pred = lr.predict(Xt_train)

            error = mean_squared_error(yt_train, y_pred)
            
            if error == 0:
                if approach == "aic":
                    aic = 2 * i
                    scores.append((i, aic))
                elif approach == "bic":
                    bic = i * log(n)
                    scores.append((i, bic))                
            else:
                if approach == "aic":
                    aic = n * log(error) + 2 * i
                    scores.append((i, aic))
                elif approach == "bic":
                    bic = n * log(error) + i * log(n)
                    scores.append((i, bic))

        # sorting scores
        scores = sorted(scores, key=lambda x: x[1])
        if len(scores) > 0:
            return max(min_lookback, scores[0][0])

        return min_lookback

    # check if approach is t-stat
    elif approach == "t-stat":

        # setting default for max observed
        min_p_val = (float("inf"), 1)

        # iterating through all the lookbacks
        for i in range(max_lag, 1, -1):
            # https://blog.minitab.com/en/adventures-in-statistics-2/how-to-interpret-regression-analysis-results-p-values-and-coefficients
            # build 1-step ahead LR model using lag=i : (X, y)
            # pred_y = the prediction of training data

            flatten = Flatten(
                feature_columns=feature_columns,
                target_columns=target_columns,
                lookback_win=i,
                pred_win=pred_win,
            )
            lr = LinearRegression()
            Xt, yt = flatten.fit_transform(X)
            lr.fit(Xt, yt)
            y_pred = lr.predict(Xt)
            sse = np.sum((y_pred - yt) ** 2, axis=0) / float(Xt.shape[0] - Xt.shape[1])
            se = np.array(
                [
                    np.sqrt(np.diagonal(sse[i] * np.linalg.inv(np.dot(Xt.T, Xt))))
                    for i in range(sse.shape[0])
                ]
            )
            # coef_ is the co-efficient of the each of the column in X, if lag is 5 then there are 5 columns
            t_stat = lr.coef_ / se
            p = 2 * (1 - t.cdf(np.abs(t_stat), yt.shape[0] - Xt.shape[1]))
            # find the value of p for the max_lag, assume your column 0 in X represent the most older value then
            # check t_stat and p at position 0
            # if p_value[0] (assuming the first column has observation from the older time point) > 0.95

            # updating lookback if greater
            if p[0][0] < min_p_val[0]:
                min_p_val = (p[0][0], i)

            # directly returning if greater than 0.95
            if p[0][0] < 0.05 and i >= min_lookback:
                return i

        return max(min_lookback, min_p_val[1])

    elif approach == "model-cv":
        # for cv score based approach
        # use train-test time series based 5 fold cv error
        cv = TimeSeriesKFoldSlidingSplit(n_splits=3)

        scores = []
        for i in range(1, max_lag):

            flatten = Flatten(
                feature_columns=feature_columns,
                target_columns=target_columns,
                lookback_win=i,
                pred_win=pred_win,
            )
            lr = LinearRegression()
            Xt, yt = flatten.fit_transform(X)
            scores_i = cross_val_score(
                lr, X=Xt, y=yt, scoring="neg_mean_absolute_error", cv=cv
            )
            scores.append((i, np.mean(scores_i)))

        # we need lowest MAE but since we found neg-MAE, we sort to find highest.
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        return max(min_lookback, scores[0][0])

    elif approach == "cv":
        if isinstance(X, pd.DataFrame):
            X = X.values

        lookbacks = []
        for col in feature_columns:
            arr = X[:, col]

            cv_res = [
                (i, generalized_cross_validation_error(arr, i)[0])
                for i in range(1, max_lag)
            ]
            cv_res = sorted(cv_res, key=lambda x: x[1])
            lookbacks.append(cv_res[0][0])
        if len(feature_columns) > 1:
            return max(min_lookback, lookbacks[0])
        else:
            return max(min_lookback, statistics.median(lookbacks))

    elif approach == "multi-stat":
        res = recommend_lookback_MTS(
            X,
            value_columns=feature_columns,
            time_col=time_column,
            user_lookback=-1,
            default_val=8,
            opt_order=True,
            max_lookback=max_lookback,
            option=1,
            n_jobs=-1,
        )
        return max(min_lookback, res[0])
    else:
        raise ValueError("The given value of approach is not valid.")


# questions

# 1. multiple feature columns
#     - single value for lookback
#     - column wise lookback in a list
#     - list of lookback in terms of priority
# 2. multiple target columns
#     - similar as above
# 3. only `cv` and `multi-stats` support distinct lookbacks for each column.
# 4. How will users even use column wise lookback?
