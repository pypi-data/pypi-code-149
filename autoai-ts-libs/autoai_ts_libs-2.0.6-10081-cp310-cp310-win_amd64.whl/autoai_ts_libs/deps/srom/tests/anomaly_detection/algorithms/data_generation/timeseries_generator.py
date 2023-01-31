from typing import List

import numpy as np


def analyze_change_points(change_points: np.ndarray) -> List:
    return np.where(change_points == -1)[0].tolist()


def generate_seasonal_sawtooth_series(number_of_cycles: int = 12, points_per_cycle: int = 30, jump_magnitude: int = 5, jump_time_step: int = 250,
                                      noise_factor: float = 0.15, rng=None):
    """Generates sawtooth-shaped time series as it might come from seasonality in the time series.

    :param number_of_cycles: Number of sawteeth, e.g. 12 for monthly cycles.
    :param points_per_cycle: How many data points are captured per cycles, e.g. about 30 data points to represent days in month
    :param jump_magnitude: How many units series jumps at jump point
    :param jump_time_step: Time step where jump occurs
    :param noise_factor: Noise is scaled by magnitude of jump times this factor
    :return: Sawtooth time series
    """
    # Repeat sawtooth curve to form seasonal time series
    seasonal_signal = np.concatenate([np.linspace(0, 5, num=points_per_cycle) for x in range(number_of_cycles)])

    # Add jump
    seasonal_signal[jump_time_step:] = seasonal_signal[jump_time_step:] + jump_magnitude

    # Add noise
    if rng is None:
        noise = np.random.normal(scale=jump_magnitude * noise_factor, size=seasonal_signal.shape)
    else:
        noise = rng.normal(scale=jump_magnitude * noise_factor, size=seasonal_signal.shape)
    seasonal_signal += noise

    return seasonal_signal.reshape(len(seasonal_signal), 1)


def generate_change_in_mean_series(simple: bool = False, rng=None):
    """
    Generates timeseries with change in mean. Might not yield enough data for mSSA base matrix.
    :param rng: Random generator to seed function, e.g. rng = np.random.default_rng(1337)
    :param simple: Whether to use simplified way of generating time series or one with explicit spikes
    :return:
    """

    if simple:
        if rng is None:
            return np.concatenate([np.random.rand(200)+5, np.random.rand(200)+10, np.random.rand(200)+5]).reshape(-1, 1)
        else:
            return np.concatenate([rng.random(200) + 5, rng.random(200) + 10, rng.random(200) + 5]).reshape(
                -1, 1)

    signal_with_spikes = np.random.normal(scale=1, size=200)
    signal_with_spikes[:50] += 20
    signal_with_spikes[50:] += 75
    signal_with_spikes[150:] -= 30
    signal_with_spikes[60] = 100
    signal_with_spikes[110] = 0
    return signal_with_spikes.reshape(len(signal_with_spikes), 1)


def generate_outlier_series():
    """
    Generates outlier time series
    :return: Outlier time series
    """
    signal = 10 * np.sin(np.linspace(0, 30 * np.pi, num=300))
    signal[105:155] *= 0.05

    noise = np.random.normal(scale = 1.5, size=300)
    signal += noise
    return signal.reshape(len(signal), 1)


def generate_change_in_periodicity(rng=None):
    """
    Generates change in periodicity dataset
    :return:
    """
    signal = 10 * np.sin(np.linspace(0, 20 * np.pi, num=1200))
    signal2 = 10 * np.sin(np.linspace(0, 75 * np.pi, num=1200))
    if rng is None:
        noise = np.random.normal(scale=0.5, size=1200)
    else:
        noise = rng.normal(scale=0.5, size=1200)
    signal += noise
    signal[375:800] = signal2[375:800]
    return signal.reshape(len(signal), 1)
