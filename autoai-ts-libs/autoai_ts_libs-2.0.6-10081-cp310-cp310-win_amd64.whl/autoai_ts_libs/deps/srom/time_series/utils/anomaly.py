import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from scipy import special as sp
from scipy.optimize import fmin


def _find_sequences(errors, epsilon, anomaly_padding):
    """Find sequences of values that are above epsilon.

    Parameters
    ----------
    errors (ndarray):
        Array of errors.
    epsilon (float):
        Threshold value. All errors above epsilon are considered an anomaly.
    anomaly_padding (int):
        Number of errors before and after a found anomaly that are added to the
        anomalous sequence.
    Returns
    -------
    ndarray, float:
        * Array containing start, end of each found anomalous sequence.
        * Maximum error value that was not considered an anomaly.
    """
    errors = errors.ravel()
    above = pd.Series(errors > epsilon)
    index_above = np.argwhere(above.values)

    for idx in index_above.flatten():
        above[
            max(0, idx - anomaly_padding) : min(idx + anomaly_padding + 1, len(above))
        ] = True

    shift = above.shift(1).fillna(False)
    change = above != shift

    if above.all():
        max_below = 0
    else:
        max_below = max(errors[~above])

    index = above.index
    starts = index[above & change].tolist()
    ends = (index[~above & change] - 1).tolist()

    if len(ends) == len(starts) - 1:
        ends.append(len(above) - 1)

    return np.array([starts, ends]).T, max_below


def _prune_anomalies(max_errors, min_percent):
    """Prune anomalies to mitigate false positives.
    This is done by following these steps:
        * Shift the errors 1 negative step to compare each value with the next one.
        * Drop the last row, which we do not want to compare.
        * Calculate the percentage increase for each row.
        * Find rows which are below ``min_percent``.
        * Find the index of the latest of such rows.
        * Get the values of all the sequences above that index.
    Parameters
    ----------
    max_errors (pandas.DataFrame):
        DataFrame object containing columns ``start``, ``stop`` and ``max_error``.
    min_percent (float):
        Percentage of separation the anomalies need to meet between themselves and the
        highest non-anomalous error in the window sequence.
    Returns
    -------
    ndarray:
        Array containing start, end, max_error of the pruned anomalies.
    """
    next_error = max_errors["max_error"].shift(-1).iloc[:-1]
    max_error = max_errors["max_error"].iloc[:-1]

    increase = (max_error - next_error) / max_error
    if max_error.shape[0] != 0:
        if max_error.values[0] == 0:
            increase = np.array([0])
    too_small = increase < min_percent

    if too_small.all():
        last_index = -1
    else:
        last_index = max_error[~too_small].index[-1]

    if last_index == -1:
        last_index = max_errors.shape[0] - 1
    return max_errors[["start", "stop", "max_error"]].iloc[0 : last_index + 1].values


def z_cost(z, errors, mean, std):
    """Compute how bad a z value is.
    The original formula is::
                 (delta_mean/mean) + (delta_std/std)
        ------------------------------------------------------
        number of errors above + (number of sequences above)^2
    which computes the "goodness" of `z`, meaning that the higher the value
    the better the `z`.
    In this case, we return this value inverted (we make it negative), to convert
    it into a cost function, as later on we will use scipy.fmin to minimize it.
    Parameters
    ----------
    z (ndarray):
        Value for which a cost score is calculated.
    errors (ndarray):
        Array of errors.
    mean (float):
        Mean of errors.
    std (float):
        Standard deviation of errors.
    Returns
    -------
    float:
        Cost of z.
    """
    epsilon = mean + z * std

    if errors.ndim > 1:
        errors = errors.flatten()

    below = errors[errors <= epsilon]
    if not len(below):
        delta_mean, delta_std = 0, 0
    else:
        delta_mean, delta_std = mean - below.mean(), std - below.std()

    above = errors > epsilon
    total_above = len(errors[above])
    above = pd.Series(above)
    shift = above.shift(1)
    change = above != shift
    total_consecutive = sum((above & change).values)
    # total_consecutive = sum(above & change)

    above, consecutive = total_above, total_consecutive
    if mean == 0 or std == 0:
        return np.inf
    numerator = -(delta_mean / mean + delta_std / std)
    denominator = above + consecutive ** 2
    if denominator == 0:
        return np.inf
    return numerator / denominator


def _find_threshold(errors, z_range):
    mean = errors.mean()
    std = errors.std()
    min_z, max_z = z_range
    best_z = min_z
    best_cost = np.inf
    for z in range(min_z, max_z):
        z_cost_for_z = z_cost(z, errors, mean, std)
        if z_cost_for_z < best_cost:
            best_z = z
        """
        best = fmin(
            z_cost, z, args=(errors.ravel(), mean, std), full_output=True, disp=False
        )
        z, cost = best[0:2]
        if cost < best_cost:
            best_z = z[0]
        """

    return best_z


def _merge_sequences(sequences):
    """Merge consecutive and overlapping sequences.
    We iterate over a list of start, end, score triples and merge together
    overlapping or consecutive sequences.
    The score of a merged sequence is the average of the single scores,
    weighted by the length of the corresponding sequences.
    Parameters
    ----------
    sequences (list):
        List of anomalies, containing start-index, end-index, score for each anomaly.
    Returns
    -------
    ndarray:
        Array containing start-index, end-index, score for each anomaly after merging.
    """
    if len(sequences) == 0:
        return np.array([])

    sorted_sequences = sorted(sequences, key=lambda entry: entry[0])
    new_sequences = [sorted_sequences[0]]
    score = [sorted_sequences[0][2]]
    weights = [sorted_sequences[0][1] - sorted_sequences[0][0]]

    for sequence in sorted_sequences[1:]:

        prev_sequence = new_sequences[-1]
        if sequence[0] <= prev_sequence[1] + 1:
            score.append(sequence[2])
            weights.append(sequence[1] - sequence[0])
            if np.sum(np.asarray(weights)) == 0:
                weighted_average = 0
            else:
                weighted_average = np.average(
                    np.asarray(score), weights=np.asarray(weights), axis=0
                )
            new_sequences[-1] = (
                prev_sequence[0],
                max(prev_sequence[1], sequence[1]),
                weighted_average,
            )
        else:
            score = [sequence[2]]
            weights = [sequence[1] - sequence[0]]
            new_sequences.append(sequence)

    return np.array(new_sequences)


def contextual_score(
    train_test_errors,
    observation_window=None,
    scoring_threshold=4,
    anomaly_padding=50,
    min_percent=0.1,
):
    """Find sequences of error values that are anomalous.
    We first define the window of errors, that we want to analyze. We then find the anomalous
    sequences in that window and store the start/stop index pairs that correspond to each
    sequence, along with its score.
    We then move the window and repeat the procedure.
    Lastly, we combine overlapping or consecutive sequences.

    Parameters
    ----------
    train_test_errors (ndarray):
        Array of errors.
    observation_window (int):
        Optional. Size of the window for which a threshold is calculated. If not given,
        `None` is used, which finds one threshold for the entire sequence of errors.
    scoring_threshold (int):
        Scoring threshold to be used.
    anomaly_padding (int):
        Optional. Number of errors before and after a found anomaly that are added to the
        anomalous sequence. If not given, 50 is used.
    min_percent (float):
        Optional. Percentage of separation the anomalies need to meet between themselves and
        the highest non-anomalous error in the window sequence. It nof given, 0.1 is used.
    Returns
    -------
    ndarray:
        Array containing start-index, end-index, score for each anomalous sequence that
        was found.
    """
    window_size = observation_window or len(train_test_errors)
    error_mean = np.nanmean(train_test_errors, dtype="float32")
    error_std = np.nanstd(train_test_errors, dtype="float32")
    window_start = 0
    window_end = 0
    sequences = list()

    while window_end < len(train_test_errors):
        window_end = window_start + window_size
        window = train_test_errors[window_start:window_end]
        threshold = error_mean + scoring_threshold * error_std
        window_sequences, max_below = _find_sequences(
            window, threshold, anomaly_padding
        )
        max_errors = [{"max_error": max_below, "start": -1, "stop": -1}]
        for sequence in window_sequences:
            start, stop = sequence
            sequence_errors = window[start : stop + 1]
            max_errors.append(
                {"start": start, "stop": stop, "max_error": np.nanmax(sequence_errors)}
            )
        max_errors = pd.DataFrame(max_errors).sort_values("max_error", ascending=False)
        max_errors = max_errors.reset_index(drop=True)
        pruned_anomalies = _prune_anomalies(max_errors, min_percent)

        window_sequences = list()

        denominator = error_mean + error_std
        for row in pruned_anomalies:
            max_error = row[2]
            score = (max_error - threshold) / denominator
            window_sequences.append(
                [row[0] + window_start, row[1] + window_start, score]
            )

        sequences.extend(window_sequences)

        window_start = window_start + window_size

    sequences = _merge_sequences(sequences)
    return np.asarray(sequences)


def chi_square_score(train_test_errors, observation_window, scoring_threshold):
    """Find sequences of error values that are anomalous.

    Parameters
    ----------
    train_test_errors (ndarray):
        Array of errors.
    observation_window (int):
        Size of the window for which a threshold is calculated.
    scoring_threshold (int):
        Scoring threshold to be used.
    Returns
    -------
    c_score:
        Anomaly Score by chi_score method.
    threshold_score:
        The value of the threshold detected by the algorithm.
    """

    c_score = np.empty((len(train_test_errors), 1))
    c_score.fill(np.nan)
    threshold_score = np.empty((len(train_test_errors), 1))
    threshold_score.fill(np.nan)

    past_non_outlier_error = []

    for current_error_index, current_error in enumerate(train_test_errors):

        # what if current error is nan?
        if (type(current_error) is list) or (
            (type(current_error) is np.ndarray)
            and ((len(current_error.shape) == 1) or (current_error.shape[1] == 1))
        ):
            current_error = current_error[0]

        if np.isnan(current_error):
            continue

        if current_error_index < observation_window:
            past_non_outlier_error.append(current_error)
            continue

        samples = []
        if len(past_non_outlier_error) <= observation_window:
            samples = pd.DataFrame(np.array(past_non_outlier_error)).dropna()
        else:
            samples = pd.DataFrame(
                np.array(past_non_outlier_error[-observation_window:])
            ).dropna()

        if samples.shape[0] < observation_window:
            past_non_outlier_error.append(current_error)
            continue

        scaler = MinMaxScaler()
        Q = scaler.fit_transform(samples)
        threshold = scoring_threshold * np.nanstd(Q)
        Y = scaler.transform(np.array([current_error]).reshape(-1, 1))

        c_score[current_error_index] = Y[0]
        threshold_score[current_error_index] = threshold
        if Y[0] < threshold:
            past_non_outlier_error.append(current_error)

    return (c_score, threshold_score)


def q_score(train_test_errors, observation_window, scoring_threshold):
    """Find sequences of error values that are anomalous.

    Parameters
    ----------
    train_test_errors (ndarray):
        Array of errors.
    observation_window (int):
        Size of the window for which a threshold is calculated.
    scoring_threshold (int):
        Scoring threshold to be used.
    Returns
    -------
    q_score:
        Anomaly Score by q_score method.
    threshold_score:
        The value of the threshold detected by the algorithm.
    """
    # q-score
    q_score = np.empty((len(train_test_errors), 1))
    q_score.fill(np.nan)

    threshold_score = np.empty((len(train_test_errors), 1))
    threshold_score.fill(np.nan)

    # ideally observation_window should be very very large
    # so i swapped the value
    recent_window_len = observation_window
    # reference_window_len = min(int(len(train_test_errors)*0.3), min(8000, int(recent_window_len * 10))
    reference_window_len = min(
        int(len(train_test_errors) * 0.3), recent_window_len * 10
    )

    # old
    # reference_window_len = observation_window
    # recent_window_len = min(max(int(observation_window * 0.1), 6), reference_window_len)

    # ideally we shd add some check on score distribution
    # if its distribution is uniform, the curretn setting of window is short
    # ideally we assume anomaly are rate and hence their respective score
    # we will add it soon

    for current_error_index, current_error in enumerate(train_test_errors):

        # what if current error is nan?
        threshold_score[current_error_index] = 1.0 - scoring_threshold

        # what if current error is nan?
        if (type(current_error) is list) or (
            (type(current_error) is np.ndarray)
            and ((len(current_error.shape) == 1) or (current_error.shape[1] == 1))
        ):
            current_error = current_error[0]

        if np.isnan(current_error):
            continue

        if current_error_index < reference_window_len:
            continue

        reference_window = train_test_errors[
            (current_error_index - reference_window_len) : current_error_index
        ]
        recent_window = train_test_errors[
            (current_error_index - recent_window_len) : current_error_index
        ]

        reference_window_samples = pd.DataFrame(np.array(reference_window)).dropna()
        recent_window_samples = pd.DataFrame(np.array(recent_window)).dropna()

        if len(recent_window_samples) <= 0 or len(reference_window_samples) <= 0:
            continue

        # now we get a
        reference_window_mean = np.mean(reference_window_samples.values)
        reference_window_std = np.std(reference_window_samples.values)
        recent_window_mean = np.mean(recent_window_samples.values)

        if reference_window_std > 0:
            tmp_x_value = (recent_window_mean - reference_window_mean) / (
                reference_window_std
            )
            q_function_res = 0.5 - 0.5 * sp.erf(tmp_x_value / np.sqrt(2))
            Lt = 1 - q_function_res
            q_score[current_error_index] = Lt
    return (q_score, threshold_score)


def adaptive_window_score(train_test_errors, observation_window, scoring_threshold):
    """Find sequences of error values that are anomalous.

    Parameters
    ----------
    train_test_errors (ndarray):
        Array of errors.
    observation_window (int):
        Size of the window for which a threshold is calculated.
    scoring_threshold (int):
        Scoring threshold to be used.
    Returns
    -------
    anomaly:
        Anomaly Score by adaptive_window_score method.
    threshold_score:
        The value of the threshold detected by the algorithm.
    """
    threshold_score = np.empty(len(train_test_errors))
    threshold_score.fill(np.nan)

    step_observation_window = max(1, observation_window // 3)
    window_start = 0
    window_end = 0
    while window_end < len(train_test_errors):
        window_end = min(window_start + observation_window, len(train_test_errors))
        window = train_test_errors[window_start:window_end]

        # find the bext scoring threshold
        # to be implmented as time pass
        # it shd change the following value
        best_scoring_threshold = _find_threshold(
            window, (max(1, int(scoring_threshold) - 2), int(scoring_threshold) + 2)
        )
        win_threshold = window.mean() + best_scoring_threshold * window.std()
        for item_s in range(window_start, window_end):
            if threshold_score[item_s]:
                threshold_score[item_s] = min(win_threshold, threshold_score[item_s])
            else:
                threshold_score[item_s] = win_threshold

        window_start = window_start + step_observation_window

    return (train_test_errors, threshold_score)


def window_score(train_test_errors, observation_window, scoring_threshold):
    """Find sequences of error values that are anomalous.

    Parameters
    ----------
    train_test_errors (ndarray):
        Array of errors.
    observation_window (int):
        Size of the window for which a threshold is calculated.
    scoring_threshold (int):
        Scoring threshold to be used.
    Returns
    -------
    anomaly:
        Anomaly Score by window_score method.
    threshold_score:
        The value of the threshold detected by the algorithm.
    """

    threshold_score = np.empty(len(train_test_errors))
    threshold_score.fill(np.nan)

    step_observation_window = max(1, observation_window // 3)
    window_start = 0
    window_end = 0
    while window_end < len(train_test_errors):
        window_end = min(window_start + observation_window, len(train_test_errors))
        window = train_test_errors[window_start:window_end]
        win_threshold = window.mean() + scoring_threshold * window.std()
        for item_s in range(window_start, window_end):
            if threshold_score[item_s]:
                threshold_score[item_s] = min(win_threshold, threshold_score[item_s])
            else:
                threshold_score[item_s] = win_threshold

        window_start = window_start + step_observation_window

    return (train_test_errors, threshold_score)
