import datetime
import math
from multiprocessing import cpu_count

import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from scipy import signal
from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.model_selection import cross_val_score
from sklearn.utils.validation import column_or_1d
from statsmodels.tsa.stattools import adfuller, kpss


def check_model_type_is_dl(model):
    """
    check if model is deep learning
    """
    from scikeras.wrappers import KerasRegressor

    MODEL_TYPES_SUPPORTED_FOR_DEEP_LEARNING = [KerasRegressor]

    for i in MODEL_TYPES_SUPPORTED_FOR_DEEP_LEARNING:
        if isinstance(model, i):
            return True
    return False


def check_object_is_estimator(model):
    """
    check if model is estimator
    """
    from scikeras.wrappers import KerasRegressor

    MODEL_TYPES_SUPPORTED_AS_ESTIMATOR = [KerasRegressor, BaseEstimator]

    for i in MODEL_TYPES_SUPPORTED_AS_ESTIMATOR:
        if isinstance(model, i):
            return True
    return False


def get_optimized_n_jobs(n_jobs=-1, no_outputs=1):
    """
    return optimized n_jobs based on n_jobs and no_outputs
    """
    if n_jobs == -1:
        n_jobs = cpu_count() - 1
    if n_jobs < 1:
        n_jobs = 1
    return min(no_outputs, n_jobs)


def kpss_stationarity_test(series, alpha):
    _, p_value, _, _ = kpss(series, regression="c")
    return p_value < alpha


def adf_stationarity_test(series, alpha):
    dftest = adfuller(series, autolag="AIC")
    p_value = dftest[1]
    return (1.0 - p_value) < alpha


def stationarity_test(series, alpha, test_name="kpss"):
    if test_name == "kpss":
        return kpss_stationarity_test(series, alpha)
    elif test_name == "adf":
        return adf_stationarity_test(series, alpha)
    else:
        return False


def is_constant(x):
    x = column_or_1d(x)
    return (x == x[0]).all()


def diff(x):
    x = column_or_1d(x)
    return x[1:] - x[:-1]


def seasonality_test(original_ts, ppy):
    """
    Seasonality test
    :param original_ts: time series
    :param ppy: periods per year
    :return: boolean value: whether the TS is seasonal
    """
    s = acf(original_ts, 1)
    for i in range(2, ppy):
        s = s + (acf(original_ts, i) ** 2)
    limit = 1.645 * (math.sqrt((1 + 2 * s) / len(original_ts)))
    return (abs(acf(original_ts, ppy))) > limit


def acf(x, k):
    """
    Autocorrelation function
    :param data: time series
    :param k: lag
    :return:
    """
    m = np.mean(x)
    s1 = 0
    for i in range(k, len(x)):
        s1 = s1 + ((x[i] - m) * (x[i - k] - m))
    s2 = 0
    for i in range(0, len(x)):
        s2 = s2 + ((x[i] - m) ** 2)
    return float(s1 / s2)


def recommend_ndiffs(x, alpha=0.05, test_name="kpss", max_d=5):
    d = 0
    if is_constant(x):
        return d

    dodiff = stationarity_test(x, alpha, test_name)
    while dodiff and d < max_d:
        d += 1
        x = diff(x)
        if is_constant(x):
            return d
        dodiff = stationarity_test(x, alpha, test_name)
    return d


def smape(A, F):
    return 100 / len(A) * np.sum(2 * np.abs(F - A) / (np.abs(A) + np.abs(F)))


def update_best_score(best_score, score):
    if not score:
        return best_score
    if best_score:
        if best_score < score:
            return score
        else:
            return best_score
    else:
        return score


def check_duplicate(rSet, p, d, q):
    for item in rSet:
        if item[0][0] == p and item[0][1] == d and item[0][2] == q:
            return True
    return False


def check_duplicate_all(rSet, p, d, q, P, D, Q, s):
    for item in rSet:
        if (
            item[0][0] == p
            and item[0][1] == d
            and item[0][2] == q
            and item[0][3] == P
            and item[0][4] == D
            and item[0][5] == Q
            and item[0][6] == s
        ):
            return True
    return False


def find(condition):
    """
    Returns non zero indices.

    Parameters:
        condition (numpy array, required): array of integers
    Returns:
       list
    """
    (res,) = np.nonzero(np.ravel(condition))
    return res


def get_frequency(ts):
    """
    Returns the most likely frequency.

    Parameters:
        ts (pandas series, required): series of timeseries data.

    Returns:
        int
    """
    frq = None
    try:
        df = list(ts)
        if not isinstance(df[0], datetime.date):
            df = list(pd.to_datetime(df))
        if len(df) > 10:  # only need 3, but we give little more
            frq = pd.infer_freq(df[0:10])
        else:
            frq = pd.infer_freq(df)
    except Exception:
        pass
    if frq is None:
        if isinstance(ts[1], (np.float64, np.int64)):
            first = ts[1]
            second = ts[2]
            diff = second - first
            if (diff) == 0.0:
                count = 1
            else:
                count = 1 / (diff)
            count = round(count)
            if count == 1:
                frq = "A"
            elif count == 4:
                frq = "Q"
            elif count == 12:
                frq = "M"
            elif count == 52 or count == 7:
                frq = "W"
            elif count == 365:
                frq = "D"
            else:
                frq = "A"
    if frq is None:
        frq = "A"
    return frq


def freq_zero_crossing(sig):
    """
    Return zero crossing.

    Parameters:
        sig (array type, required): array of timeseries data.

    Return:
        float
    """
    sig = sig - np.mean(sig)

    indices = find((sig[1:] >= 0) & (sig[:-1] < 0))
    crossings = [i - sig[i] / (sig[i + 1] - sig[i]) for i in indices]
    delta_t = np.diff(crossings)
    period = np.mean(delta_t)
    return period


def frequency_spectrum(sig, fs):
    """
    Returns frequency spectrum

    Parameters:
        sig (pandas series, required): series of timeseries data.
        fs (int, required) : sampling frequency
    Return:
        float
    """
    sig = sig - np.mean(sig)
    f, Pxx = signal.periodogram(sig, fs=fs, window="hann", scaling="spectrum")
    for amp_arg in np.argsort(np.abs(Pxx))[::-1][1:2]:
        if f[amp_arg] == 0:
            f[amp_arg] = f[amp_arg + 1]
        day = 1 / f[amp_arg]
        return day


def lookback_feature_importance(ts, lookback=1, step_ahead=1):

    """
    This function generate linear, non_liner and model based feature importance discovery for
    time series k-step ahead prediction problem

    input parameter:
    ts: univariate time series
    lookback: length og history window to use
    feature_fun: the function that we want to apply for generating features
    step_ahead: next step prediction vs k-step prediction
    shuffle_label: shall we shuffle the label, this is for evaluation purpose
    """

    # get X, y from ts and lookback
    number_of_samples = 3000
    X = pd.DataFrame(ts, columns=["signal"])
    X_col = ["signal"]
    for lag_i in range(1, lookback):
        X_col.append("signal_" + str(lag_i))
        X["signal_" + str(lag_i)] = X["signal"].shift(lag_i)
    X["y"] = X["signal"].shift(-1 * step_ahead)
    # print (X.head(10))
    X = X.dropna()

    if len(X) > number_of_samples:
        X = X.sample(n=number_of_samples, random_state=1)

    y = X["y"]
    X = X[X_col].values

    # establish the relationship
    # part 1
    try:
        f_test, _ = f_regression(X, y)
        f_test = np.max(f_test)
    except Exception:
        f_test = np.nan
    # part 2
    try:
        mi = mutual_info_regression(X, y, random_state=0)
        mi = np.max(mi)
    except Exception:
        mi = np.nan
    # part 3
    rf = RandomForestRegressor(n_estimators=20, max_depth=4, random_state=0)
    score = cross_val_score(rf, X, y, cv=5, scoring="neg_mean_absolute_error")
    ml_scores = np.mean(score)
    return [f_test, mi, ml_scores, step_ahead, lookback]


def order_lookback(X, data_column, rec_lookback, n_jobs=-1):
    """
    the lookback we want to evaluate
    """
    results = []
    max_look_back = 800

    if n_jobs == -1:
        n_jobs = cpu_count() - 1

    if n_jobs <= 0:
        n_jobs = 1

    rec_lookback = list(filter(lambda x: x <= max_look_back, rec_lookback))

    results = Parallel(n_jobs=n_jobs)(
        delayed(lookback_feature_importance)(X[:, data_column], lookback=item)
        for item in rec_lookback
    )
    if len(results) > 0:
        df = pd.DataFrame(results)
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.dropna()
        if df.shape[0] > 0:
            df[0] = df[0].rank()
            df[1] = df[1].rank()
            df[2] = df[2].rank()
            df["avg"] = df[[0, 1, 2]].mean(axis=1)
            df.sort_values("avg", inplace=True, ascending=False)
            return list(df[4].values)
            """            
            df.sort_values(df.columns[4], inplace=True, ascending=True)
            avg_val = df["avg"].values
            lookback_val_opt = df[4].values
            if len(avg_val) == 1:
                return list(lookback_val_opt)
            if sum(np.diff(avg_val) > 0) == len(avg_val) - 1:
                df.sort_values("avg", inplace=True, ascending=False)
                return list(df[4].values)
            elif sum(np.diff(avg_val) < 0) == len(avg_val) - 1:
                return list(df[4].values)
            else:
                ret_lw = []
                if avg_val[0] >= avg_val[1]:
                    ret_lw.append(lookback_val_opt[0])
                for i in range(1, len(avg_val) - 1):
                    if avg_val[i] > avg_val[i - 1] and avg_val[i] >= avg_val[i + 1]:
                        ret_lw.append(lookback_val_opt[i])
                if avg_val[-1] > avg_val[-2]:
                    ret_lw.append(lookback_val_opt[-1])
                return ret_lw
            """
    return rec_lookback


def recommend_seasonal_period(ts):
    """
    Returns the frequency depeding upon the period cycle.
    Parameters:
        ts (pandas series, required): series of timeseries data.
    Returns:
        list
    """
    size = len(ts)
    frq = get_frequency(ts)
    frq = frq[0]
    quartely_values = [4, 1]
    month_values = [12, 1]
    week_values = [54, 4, 1]
    day_values = [365, 30, 7, 1]
    hour_values = [8766, 730, 168, 24, 1]
    min_values = [525960, 43800, 10080, 1440, 60, 1]
    sec_values = [31557600, 2628000, 604800, 86400, 3600, 60]
    if frq == "A" or frq == "BA":
        return [1]
    elif frq == "Q":
        return [i for i in quartely_values if size >= 16]
    elif frq == "M" or frq == "MS":
        return [i for i in month_values if size >= 60]
    elif frq == "W":
        return [i for i in week_values if size >= 2 * i]
    elif frq == "D":
        return [i for i in day_values if size >= i * 2]
    elif frq == "H":
        return [i for i in hour_values if size >= 2 * i]
    elif frq == "T":
        return [i for i in min_values if size >= 2 * i]
    elif frq == "S":
        return [i for i in sec_values if size >= 2 * i]
    else:
        return [1]


def recommend_lookback(
    X,
    value_column,
    time_column=None,
    user_lookback=-1,
    default_val=8,
    opt_order=True,
    max_lookback=200,
    n_jobs=-1,
):
    """
    Returns a sorted list of recommended lookback values

    Parameters:
        X (dataframe, required): The dataset for which lookback is to be calculated.
        time_column (str, required): The column name of time values.
        value_column (str, required): The column name of values.
        user_lookback (int, optional): The recommended value by user.
        default_val (int, optional): The default value incase every thing failed.
    Return:
        list
    """
    if isinstance(X, pd.DataFrame):
        X = X.values

    # give priority to user_lookback
    if user_lookback > 0:
        return [user_lookback]

    lookback = []
    periods = [365, 30, 7, 1]

    if time_column is not None:
        periods = recommend_seasonal_period(X[:, time_column].flatten())

    # use of zero crossing for period detection
    v1_fre = freq_zero_crossing(X[:, value_column])
    if not math.isnan(v1_fre) and not math.isinf(v1_fre):
        lookback.append(int(round(v1_fre)))

    # use of spectral analysis for period detection
    for period in periods:
        v2_fre = frequency_spectrum(X[:, value_column], period)
        if not math.isnan(v2_fre) and not math.isinf(v2_fre):
            lookback.append(int(round(v2_fre)))
        if period > 1.0:
            lookback.append(int(period))
    lookback = list(set(lookback))

    # ignore length higher than size of data
    lookback = [x for x in lookback if x < X.shape[0]]

    if len(lookback) > 1:
        lookback = [x for x in lookback if x not in (0, 1)]
    else:
        lookback = [1 if x == 0 else x for x in lookback]

    # added max lookback cutoff.
    if len(lookback) > 0 and max(lookback) > max_lookback and max_lookback > 0:
        tmp_lookback = lookback.copy()
        lookback = []
        for item in tmp_lookback:
            if item <= max_lookback:
                lookback.append(item)

    if user_lookback > 0 and user_lookback <= 2 * max(lookback):
        return [user_lookback]

    if len(lookback) > 0:
        if opt_order:
            return order_lookback(X, value_column, lookback, n_jobs=n_jobs)
        else:
            return sorted(lookback)

    if default_val > 0:
        return [default_val]

    return [1]


def recommend_lookback_MTS(
    X,
    value_columns,
    time_col=None,
    user_lookback=-1,
    default_val=8,
    opt_order=True,
    max_lookback=200,
    option=1,
    n_jobs=-1,
):
    """
    Returns a sorted list of recommended lookback values

    Parameters:
        X (dataframe, required): The dataset for which lookback is to be calculated.
        time_column (str, required): The column indice of time values.
        value_columns (str, required): The list of column indices of values.
        user_lookback (int, optional): The recommended value by user.
        default_val (int, optional): The default value incase every thing failed.
    Return:
        list
    """

    if isinstance(X, pd.DataFrame):
        X = X.values

    # univariate setting
    if len(value_columns) == 1:
        lookback = recommend_lookback(
            X,
            value_columns[0],
            time_col,
            user_lookback,
            default_val,
            opt_order,
            max_lookback,
            n_jobs=n_jobs,
        )
        return lookback
    # multivariate setting
    else:
        num_timeseries = len(value_columns)
        lwSet = []
        for i in range(num_timeseries):
            lookback_i = recommend_lookback(
                X,
                value_columns[i],
                time_col,
                user_lookback,
                default_val,
                opt_order,
                max_lookback,
                n_jobs=n_jobs,
            )
            # take the first preferred elements
            lwSet.append(lookback_i[0])

        if option == 1:
            # get the maximum value of best recommended lookback
            lwSet.sort(reverse=True)

            selectedLW = []
            for lwSet_max in lwSet:
                if (lwSet_max * num_timeseries) > max_lookback:
                    selectedLW.append(
                        max(1, (int)(max_lookback * 1.0 / num_timeseries))
                    )
                else:
                    selectedLW.append(lwSet_max)
            if len(selectedLW) != 0:
                return selectedLW
        else:
            lwSet.sort(reverse=True)
            selectedLW = []
            for item in lwSet:
                if (item * num_timeseries) <= max_lookback:
                    selectedLW.append(item)
            if len(selectedLW) != 0:
                return selectedLW

        return [max(1, (int)(max_lookback * 1.0 / num_timeseries))]


def get_max_lookback(lookback_win):
    """function to return max window """
    if isinstance(lookback_win, list):
        max_win = -1
        for win in lookback_win:
            if isinstance(win, list):
                max_local = max(win) + 1
                if max_win < max_local:
                    max_win = max_local
            else:
                if max_win < win:
                    max_win = win
        return max_win
    else:
        return lookback_win
