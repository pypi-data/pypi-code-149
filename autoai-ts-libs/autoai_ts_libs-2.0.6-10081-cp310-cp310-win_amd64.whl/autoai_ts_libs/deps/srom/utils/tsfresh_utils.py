# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""A collection of utilities for working with the tsfresh package."""

import functools
import pandas as pd
from inspect import getmembers, isfunction
import autoai_ts_libs.deps.srom as srom
#tsfresh.feature_extraction.settings import ComprehensiveFCParameters
#from tsfresh.feature_extraction import feature_calculators
from autoai_ts_libs.deps.srom.feature_engineering.timeseries import functions

extractors_list = getmembers(functions, isfunction)
AVOID_FUNC = [
    "set_property",
    "_fft_aggregated",
    "_tmp_acf",
    "_time_delay_embed",
    "_revese_time_delay_embed",
    "_multivariate_time_delay_embed",
    "_multivariate_reverse_time_delay_embed",
    "_estimate_friedrich_coefficients",
    "_get_length_sequences_where",
    "_into_subchunks",
    "_roll",
]
FEATURE_CALC_MAPPER = {i[0]: i[1] for i in extractors_list if i[0] not in AVOID_FUNC}

EXPENSIVE_FEATURES = ["augmented_dickey_fuller", "partial_autocorrelation"]

ENTROPY_FEATUES = ["approximate_entropy", "sample_entropy", "binned_entropy"]

CWT_FEATURES = ["cwt_coefficients", "number_cwt_peaks"]

QUANTILE_FEATURES = ["quantile", "index_mass_quantile", "change_quantiles"]

FFT_FEATURES = ["fft_coefficient", "fft_aggregated"]

STATISTICAL_FEATURES = [
    "variance_larger_than_standard_deviation",
    "lempel_ziv_complexity",
    "count_below_mean",
    "last_location_of_maximum",
    "first_location_of_maximum",
    "last_location_of_minimum",
    "first_location_of_minimum",
    "percentage_of_reoccurring_datapoints_to_all_datapoints",
    "count_above_mean",
    "percentage_of_reoccurring_values_to_all_values",
    "sum_of_reoccurring_data_points",
    "has_duplicate_min",
    "has_duplicate",
    "maximum",
    "minimum",
    "max_langevin_fixed_point",
    "sum_of_reoccurring_values",
    "longest_strike_above_mean",
    "ratio_value_number_to_time_series_length",
    "absolute_sum_of_changes",
    "sum_values",
    "has_duplicate_max",
    "mean_change",
    "mean_second_derivative_central",
    "mean_abs_change",
    "mean",
    "length",
    "standard_deviation",
    "variance",
    "skewness",
    "kurtosis",
    "median",
    "longest_strike_below_mean",
    "cid_ce",
    "spkt_welch_density",
    "range_count",
    "agg_autocorrelation",
    "time_reversal_asymmetry_statistic",
    "c3",
    "value_count",
    "number_crossing_m",
    "friedrich_coefficients",
    "linear_trend",
    "number_peaks",
    "ar_coefficient",
    "autocorrelation",
    "energy_ratio_by_chunks",
    "ratio_beyond_r_sigma",
    "large_standard_deviation",
    "symmetry_looking",
    "abs_energy",
    "agg_linear_trend",
]


def get_feature_calc_mapper():
    """
    Utility to interact with the TSFresh library and extract doc strings for all Feature Calculator.
    Return a dict with keys as function name and value as dictionary.
    """
    feature_calc_desc_mapper = {}
    for item in dir(functions):
        doc = getattr(functions, item).__doc__
        pos_end_desc = doc.split("\n")[0].index("")
        desc = doc.split("\n")[1 : pos_end_desc + 2]

        #latex_string = ""
        #if ".. math::" in doc:
        #    pos = doc.split("\n").index("    .. math::") + 2
        #    formula = doc.split("\n")[pos]
        #    latex_string = formula.replace("\\\\", "\\") + " (latex formula)"

        #desc += [latex_string]
        feature_calc_desc_mapper[item] = "\n".join(desc)
    return feature_calc_desc_mapper

#from autoai_ts_libs.deps.srom.feature_engineering.timeseries.episode_feature_extractor

def generate_param_grid(feature_set):
    """
    Utility function to give a subset param grid for tsfresh.
    """
    comprehensive_features = srom.feature_engineering.timeseries.episode_feature_extractor.ComprehensiveFCParameters()

    subset_features = {}
    for f in comprehensive_features.keys():
        if f in feature_set:
            subset_features[f] = comprehensive_features[f]

    return subset_features


def breakdown_tsfresh_params(fc_params):
    """
    Utility to break tsfresh param grid into a list of parameter settings.
    """
    tmp_fc_params_list = []

    for i in fc_params.keys():

        if isinstance(fc_params[i], list):
            for j in fc_params[i]:
                tmp_fc_params = {i: [j]}
                tmp_fc_params_list.append(tmp_fc_params)

        else:
            tmp_fc_params = {i: fc_params[i]}
            tmp_fc_params_list.append(tmp_fc_params)

    return tmp_fc_params_list


# decorator to break params and execute
def split_params_and_execute(func):
    """
    Decorator to split the parameters of TSFresh and execcute feature extraction
    """

    def save_intermediate_results_csv(result, path):
        result.to_csv(path)

    @functools.wraps(func)
    def wrapper_split_params_and_execute(*args, **kwargs):

        # only if intermediate feature extraction option is `True`
        if args[0].intermediate_feature_extraction:
            all_params = breakdown_tsfresh_params(args[0].fc_params)
            value = None
            for param_set in all_params:
                import time

                try:
                    start = time.time()
                    del kwargs["fc_params"]
                    tmp_value = func(fc_params=param_set, *args, **kwargs)
                    end = time.time()
                    total_time = end - start
                    num_features_added = len(tmp_value.columns)
                except Exception:
                    tmp_value = None
                    total_time = -1
                    num_features_added = 0

                # if feature extraction is taking place first time
                if value is None:
                    # change the 'value' df only if no error
                    if tmp_value is not None:
                        value = tmp_value
                    save_intermediate_results_csv(value, args[0].result_file_name)

                    time_result = pd.DataFrame(
                        [[param_set, total_time, num_features_added]],
                        columns=["param", "time", "num_features_added"],
                    )
                    save_intermediate_results_csv(time_result, args[0].time_file_name)

                # if feature extraction is taking place after the first feature added
                else:
                    # change the 'value' df only if no error
                    if tmp_value is not None:
                        value = pd.concat([value, tmp_value], axis=1)

                    # can be replaced later with COS based storage methods
                    save_intermediate_results_csv(value, args[0].result_file_name)

                    time_result = time_result.append(
                        {
                            "param": param_set,
                            "time": total_time,
                            "num_features_added": num_features_added,
                        },
                        ignore_index=True,
                    )
                    save_intermediate_results_csv(time_result, args[0].time_file_name)

        else:
            del kwargs["fc_params"]
            value = func(fc_params=args[0].fc_params, *args, **kwargs)

        return value

    return wrapper_split_params_and_execute
