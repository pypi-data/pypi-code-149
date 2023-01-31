# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: episode_feature_extractor
   :synopsis: TSFresh Feature Extraction - Useful Wrapper for Episode Information Extraction.

.. moduleauthor:: SROM Team
"""
# To do list - NEED TO IMPLEMENT "NAN" REPLACEMENT METHOD

import os
import logging
import warnings
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from autoai_ts_libs.deps.srom.feature_engineering.timeseries.function_map import mapper


def MinimalFCParameters():
    """This is a temporary function

    Returns:
        _type_: _description_
    """
    feature_dict = {
        "sum": None,
        "median": None,
        "mean": None,
        "length": None,
        "std": None,
        "variance": None,
        "maximum": None,
        "minimum": None,
    }
    return feature_dict


def EfficientFCParameters():
    """This is a temporary function

    Returns:
        _type_: _description_
    """
    feature_dict = {
        "mean": None,
        "sum_values": None,
        "minimum": None,
        "maximum": None,
        "median": None,
        "std": None,
        "variance": None,
        "skew": None,
        "kurtosis": None,
        "quantile": [
            {"q": 0.1},
            {"q": 0.2},
            {"q": 0.3},
            {"q": 0.4},
            {"q": 0.6},
            {"q": 0.7},
            {"q": 0.8},
            {"q": 0.9},
        ],
        "absoluate_sum_of_change": None,
        "abs_energy": None,
        "mean_abs_change": None,
        "mean_change": None,
        "mean_second_derivate_central": None,
        "count_above_mean": None,
        "count_below_mean": None,
        "last_location_of_maximum": None,
        "last_location_of_minimum": None,
        "first_location_of_maximum": None,
        "first_location_of_minimum": None,
        "ratio_beyond_r_sigma": [
            {"r": 0.5},
            {"r": 1},
            {"r": 1.5},
            {"r": 2},
            {"r": 2.5},
            {"r": 3},
            {"r": 5},
            {"r": 6},
            {"r": 7},
            {"r": 10},
        ],
        "large_standard_deviation": [
            {"r": 0.05},
            {"r": 0.1},
            {"r": 0.15000000000000002},
            {"r": 0.2},
            {"r": 0.25},
            {"r": 0.30000000000000004},
            {"r": 0.35000000000000003},
            {"r": 0.4},
            {"r": 0.45},
            {"r": 0.5},
            {"r": 0.55},
            {"r": 0.6000000000000001},
            {"r": 0.65},
            {"r": 0.7000000000000001},
            {"r": 0.75},
            {"r": 0.8},
            {"r": 0.8500000000000001},
            {"r": 0.9},
            {"r": 0.9500000000000001},
        ],
        "longest_strike_below_mean": None,
        "longest_strike_above_mean": None,
        "percentage_of_reoccurring_datapoints_to_all_datapoints": None,
        "percentage_of_reoccurring_values_to_all_values": None,
        "sum_of_reoccurring_values": None,
        "sum_of_reoccurring_data_points": None,
        # 'ratio_value_number_to_time_series_length': None,
        "variance_larger_than_standard_deviation": None,
        "has_duplicate_max": None,
        "has_duplicate_min": None,
        "has_duplicate": None,
        "time_reversal_asymmetry_statistic": [{"lag": 1}, {"lag": 2}, {"lag": 3}],
        "c3": [{"lag": 1}, {"lag": 2}, {"lag": 3}],
        "cid_ce": [{"normalize": True}, {"normalize": False}],
        "ar_coefficient": [
            {"coeff": 0, "k": 10},
            {"coeff": 1, "k": 10},
            {"coeff": 2, "k": 10},
            {"coeff": 3, "k": 10},
            {"coeff": 4, "k": 10},
            {"coeff": 5, "k": 10},
            {"coeff": 6, "k": 10},
            {"coeff": 7, "k": 10},
            {"coeff": 8, "k": 10},
            {"coeff": 9, "k": 10},
            {"coeff": 10, "k": 10},
        ],
        "symmetry_looking": [
            {"r": 0.0},
            {"r": 0.05},
            {"r": 0.1},
            {"r": 0.15000000000000002},
            {"r": 0.2},
            {"r": 0.25},
            {"r": 0.30000000000000004},
            {"r": 0.35000000000000003},
            {"r": 0.4},
            {"r": 0.45},
            {"r": 0.5},
            {"r": 0.55},
            {"r": 0.6000000000000001},
            {"r": 0.65},
            {"r": 0.7000000000000001},
            {"r": 0.75},
            {"r": 0.8},
            {"r": 0.8500000000000001},
            {"r": 0.9},
            {"r": 0.9500000000000001},
        ],
        "energy_ratio_by_chunks": [
            {"num_segments": 10, "segment_focus": 0},
            {"num_segments": 10, "segment_focus": 1},
            {"num_segments": 10, "segment_focus": 2},
            {"num_segments": 10, "segment_focus": 3},
            {"num_segments": 10, "segment_focus": 4},
            {"num_segments": 10, "segment_focus": 5},
            {"num_segments": 10, "segment_focus": 6},
            {"num_segments": 10, "segment_focus": 7},
            {"num_segments": 10, "segment_focus": 8},
            {"num_segments": 10, "segment_focus": 9},
        ],
        "index_mass_quantile": [
            {"q": 0.1},
            {"q": 0.2},
            {"q": 0.3},
            {"q": 0.4},
            {"q": 0.6},
            {"q": 0.7},
            {"q": 0.8},
            {"q": 0.9},
        ],
        "friedrich_coefficients": [
            {"coeff": 0, "m": 3, "r": 30},
            {"coeff": 1, "m": 3, "r": 30},
            {"coeff": 2, "m": 3, "r": 30},
            {"coeff": 3, "m": 3, "r": 30},
        ],
        "max_langevin_fixed_point": [{"m": 3, "r": 30}],
    }
    return feature_dict


def ComprehensiveFCParameters():
    """This is a temporary function

    Returns:
        _type_: _description_
    """
    feature_dict = {
        "mean": None,
        "sum_values": None,
        "minimum": None,
        "maximum": None,
        "median": None,
        "std": None,
        "variance": None,
        "skew": None,
        "kurtosis": None,
        "quantile": [
            {"q": 0.1},
            {"q": 0.2},
            {"q": 0.3},
            {"q": 0.4},
            {"q": 0.6},
            {"q": 0.7},
            {"q": 0.8},
            {"q": 0.9},
        ],
        "absoluate_sum_of_change": None,
        "abs_energy": None,
        "mean_abs_change": None,
        "mean_change": None,
        "mean_second_derivate_central": None,
        "count_above_mean": None,
        "count_below_mean": None,
        "last_location_of_maximum": None,
        "last_location_of_minimum": None,
        "first_location_of_maximum": None,
        "first_location_of_minimum": None,
        "ratio_beyond_r_sigma": [
            {"r": 0.5},
            {"r": 1},
            {"r": 1.5},
            {"r": 2},
            {"r": 2.5},
            {"r": 3},
            {"r": 5},
            {"r": 6},
            {"r": 7},
            {"r": 10},
        ],
        "large_standard_deviation": [
            {"r": 0.05},
            {"r": 0.1},
            {"r": 0.15000000000000002},
            {"r": 0.2},
            {"r": 0.25},
            {"r": 0.30000000000000004},
            {"r": 0.35000000000000003},
            {"r": 0.4},
            {"r": 0.45},
            {"r": 0.5},
            {"r": 0.55},
            {"r": 0.6000000000000001},
            {"r": 0.65},
            {"r": 0.7000000000000001},
            {"r": 0.75},
            {"r": 0.8},
            {"r": 0.8500000000000001},
            {"r": 0.9},
            {"r": 0.9500000000000001},
        ],
        "longest_strike_below_mean": None,
        "longest_strike_above_mean": None,
        "percentage_of_reoccurring_datapoints_to_all_datapoints": None,
        "percentage_of_reoccurring_values_to_all_values": None,
        "sum_of_reoccurring_values": None,
        "sum_of_reoccurring_data_points": None,
        # 'ratio_value_number_to_time_series_length': None,
        "variance_larger_than_standard_deviation": None,
        "has_duplicate_max": None,
        "has_duplicate_min": None,
        "has_duplicate": None,
        "approximate_entropy": [
            {"m": 2, "r": 0.1},
            {"m": 2, "r": 0.3},
            {"m": 2, "r": 0.5},
            {"m": 2, "r": 0.7},
            {"m": 2, "r": 0.9},
        ],
        "time_reversal_asymmetry_statistic": [{"lag": 1}, {"lag": 2}, {"lag": 3}],
        "c3": [{"lag": 1}, {"lag": 2}, {"lag": 3}],
        "cid_ce": [{"normalize": True}, {"normalize": False}],
        "ar_coefficient": [
            {"coeff": 0, "k": 10},
            {"coeff": 1, "k": 10},
            {"coeff": 2, "k": 10},
            {"coeff": 3, "k": 10},
            {"coeff": 4, "k": 10},
            {"coeff": 5, "k": 10},
            {"coeff": 6, "k": 10},
            {"coeff": 7, "k": 10},
            {"coeff": 8, "k": 10},
            {"coeff": 9, "k": 10},
            {"coeff": 10, "k": 10},
        ],
        "symmetry_looking": [
            {"r": 0.0},
            {"r": 0.05},
            {"r": 0.1},
            {"r": 0.15000000000000002},
            {"r": 0.2},
            {"r": 0.25},
            {"r": 0.30000000000000004},
            {"r": 0.35000000000000003},
            {"r": 0.4},
            {"r": 0.45},
            {"r": 0.5},
            {"r": 0.55},
            {"r": 0.6000000000000001},
            {"r": 0.65},
            {"r": 0.7000000000000001},
            {"r": 0.75},
            {"r": 0.8},
            {"r": 0.8500000000000001},
            {"r": 0.9},
            {"r": 0.9500000000000001},
        ],
        "energy_ratio_by_chunks": [
            {"num_segments": 10, "segment_focus": 0},
            {"num_segments": 10, "segment_focus": 1},
            {"num_segments": 10, "segment_focus": 2},
            {"num_segments": 10, "segment_focus": 3},
            {"num_segments": 10, "segment_focus": 4},
            {"num_segments": 10, "segment_focus": 5},
            {"num_segments": 10, "segment_focus": 6},
            {"num_segments": 10, "segment_focus": 7},
            {"num_segments": 10, "segment_focus": 8},
            {"num_segments": 10, "segment_focus": 9},
        ],
        "index_mass_quantile": [
            {"q": 0.1},
            {"q": 0.2},
            {"q": 0.3},
            {"q": 0.4},
            {"q": 0.6},
            {"q": 0.7},
            {"q": 0.8},
            {"q": 0.9},
        ],
        "friedrich_coefficients": [
            {"coeff": 0, "m": 3, "r": 30},
            {"coeff": 1, "m": 3, "r": 30},
            {"coeff": 2, "m": 3, "r": 30},
            {"coeff": 3, "m": 3, "r": 30},
        ],
        "max_langevin_fixed_point": [{"m": 3, "r": 30}],
    }
    return feature_dict


def extract_features(
    X, column_id, column_sort, column_value, column_kind, default_fc_parameters, n_jobs
):
    """_summary_

    Args:
        X (_type_): _description_
        column_id (_type_): _description_
        column_sort (_type_): _description_
        column_value (_type_): _description_
        column_kind (_type_): _description_
        default_fc_parameters (_type_): _description_
        n_jobs (_type_): _description_
    """
    # deepka here you need to write similar function like tsfresh then
    # we can remove all tsfresh import

    clms = []
    if type(X) is dict:
        clms = X.keys()
    else:
        for item in X.columns:
            if item not in [column_id, column_sort]:
                clms.append(item)

    header_clm = [column_id]
    for item in default_fc_parameters.keys():
        if default_fc_parameters[item] is None:
            for clm_itm in clms:
                header_clm.append(clm_itm + "__" + item)

    print(header_clm)
    ans_set = []

    if type(X) is dict:
        for clm in clms:
            nX = X[clm]
            for ind, grp in nX.groupby(column_id):
                grp = grp.sort_values(column_sort)
                for item in default_fc_parameters.keys():
                    if default_fc_parameters[item] is None:
                        # print (grp[[column_value]].apply(mapper(item)), ind, clm)
                        tmp_ans = list(grp[[column_value]].apply(mapper(item)).values)
                        tmp_ans.append(ind)
                        tmp_ans.append(clm + "__" + item)
                        ans_set.append(tmp_ans)
                    else:
                        pass
        pass
    else:
        for ind, grp in X.groupby(column_id):
            grp = grp.sort_values(column_sort)
            row_set = [ind]
            for item in default_fc_parameters.keys():
                if default_fc_parameters[item] is None:
                    tmp_ans = list(grp[clms].apply(mapper(item)).values)
                    row_set.extend(tmp_ans)
                else:
                    pass
            ans_set.append(row_set)
    if type(X) is dict:
        ans_set = pd.DataFrame(ans_set)
        ans_set.columns = ["value", "id", "column"]
        # ans_set['id'] = np.int(ans_set['id'])
        # print (ans_set)
        print(ans_set)
        return ans_set.pivot(index="id", columns="column", values="value")
        # write code here to make a dataframe -
    else:
        ans = pd.DataFrame(ans_set)
        print(ans)
        ans.columns = header_clm
        ans = ans.set_index(column_id)
        return ans


# from tsfresh import extract_features
# from tsfresh.feature_extraction import (
#    EfficientFCParameters,
#    ComprehensiveFCParameters,
# )
from autoai_ts_libs.deps.srom.utils.tsfresh_utils import (
    split_params_and_execute,
    generate_param_grid,
    CWT_FEATURES,
    STATISTICAL_FEATURES,
    ENTROPY_FEATUES,
    EXPENSIVE_FEATURES,
    FFT_FEATURES,
    QUANTILE_FEATURES,
)

LOGGER = logging.getLogger(__name__)


class TSFreshFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    Performs episodic feature extraction on time series data \
    using TSFresh Package.
    """

    def __init__(
        self,
        episode_id=None,
        episode_data_column=None,
        time_id=None,
        features_to_exclude=None,
        settings="efficient",
        intermediate_feature_extraction=False,
        intermediate_result_path=None,
        n_jobs=2,
        distributor=None,
        save_suffix="",
    ):
        """
        Parameters:
            episode_id (string, required): Column name w.r.t. which data extraction is performed \
                    when data is in pandas dataframe.
            episode_data_column (string, required): Column name that contains panda dataframe \
                    to describe episode data.
            time_id (string, optional): Column name for a data frame contained episode_data_column.
            features_to_exclude (string, optional): Types of features to not include in
                    the feature extraction using TSFresh.
            settings (string, optional): String specifying the TSFresh feature extractor setting. \
                    (http://tsfresh.readthedocs.io/en/latest/text/feature_extraction_settings.html) \
                    - "minimal": 8 fast calculation on time series \
                    - "efficient": 700+ large complex features on time series in an efficient manner \
                    - "comprehensive": Large complex features with widest pool of features. \
            intermediate_feature_extraction (boolean, optional): Executes the feature extraction \
                    in an iterative method by breaking the param grid and executing for each parameter setting. \
                    The intermediate results are saved in the file system. `intermediate_result_path` is the path where \
                    resulting files should be stored. `save_suffix` is the user-specified suffix which is \
                    used to identify resulting file names uniquely.
            intermediate_result_path (string, optional): The path where resulting files \
                    are saved if `intermediate_feature_extraction`= True. \
            save_suffix (string, optional): User-specified suffix which is used to identify resulting \
                    file names uniquely if `intermediate_feature_extraction`= True.
            n_jobs (optional): Parameter passed to tsfresh extractor. 
            distributor (optional): Parameter passed to tsfresh extractor. 

        Returns:
            Object of the class TSFreshFeatureExtractor.
        """
        self.episode_id = episode_id
        self.episode_data_column = episode_data_column
        self.time_id = time_id
        self.save_suffix = save_suffix
        self.settings = settings

        if features_to_exclude is None:
            self.features_to_exclude = []
        else:
            self.features_to_exclude = features_to_exclude

        self.extracted_features_columns = None
        self.fc_params = None
        self.set_fc_params(settings)
        self.intermediate_feature_extraction = intermediate_feature_extraction

        self.intermediate_result_path = intermediate_result_path
        if self.intermediate_result_path is None:
            self.intermediate_result_path = os.getcwd()

        result_file_name = "feature_extraction" + save_suffix + ".csv"
        time_file_name = "time_taken_by_params" + save_suffix + ".csv"
        self.result_file_name = os.path.join(
            os.path.realpath(self.intermediate_result_path),
            os.path.basename(result_file_name),
        )
        self.time_file_name = os.path.join(
            os.path.realpath(self.intermediate_result_path),
            os.path.basename(time_file_name),
        )

        # only available in tsfresh>0.11.0
        self.n_jobs = n_jobs
        self.distributor = distributor

    def set_fc_params(self, settings_type):
        """
        Function to set the fc_params in TSFreshFeatureExtractor.
        """
        if isinstance(settings_type, dict):
            self.fc_params = settings_type
        elif isinstance(settings_type, str):
            if settings_type == "minimal":
                self.fc_params = MinimalFCParameters()
            elif settings_type == "efficient":
                self.fc_params = EfficientFCParameters()
            elif settings_type == "comprehensive":
                self.fc_params = ComprehensiveFCParameters()
            else:
                raise Exception(
                    "unknown settings_type. Please use premade strings - "
                    "'minimal', 'efficient' or 'comprehensive'"
                )
        else:
            raise Exception(
                "`settings_type` should either be in `dict` or `str` from the"
                " predefined format.s"
            )

    def fit(self, X, y=None, **kwargs):
        """
        Fit method. (For actual transformation, use the 'transform' method instead)
        """
        return self

    def exclude_fc_params(self, features_to_exclude=None):
        """
        Function to remove feature calculators defined by the users.

        Parameters:
            features_to_exclude (list): removes the feature key words in the
            list from the feature extractor settings
        """
        if features_to_exclude is not None:
            if isinstance(features_to_exclude, list):
                self.features_to_exclude = features_to_exclude
            else:
                raise TypeError(
                    "features_to_exclude should be list of str.", RuntimeWarning
                )

        if not self.features_to_exclude:
            warnings.warn(
                "features_to_exclude list is empty. No features were excluded.",
                RuntimeWarning,
            )

        for feature in self.features_to_exclude:
            del_keys = list(s for s in self.fc_params.keys() if feature in s)
            for key in del_keys:
                del self.fc_params[key]

    def _prepare_ts_dataframe(self, X):
        """
        Data prepartion function if the user data is in panda DataFrame format.
        """

        def _add_id(row):
            row[self.episode_data_column][self.episode_id] = row[self.episode_id]
            return row

        tmp_x = X.apply(_add_id, axis=1)
        dataframe = pd.concat(list(tmp_x[self.episode_data_column]))
        return dataframe

    @split_params_and_execute
    def _tsfresh_apply(
        self, X, column_id, column_sort, column_value, column_kind, fc_params
    ):

        extracted_features_df = extract_features(
            X,
            column_id=column_id,
            column_sort=column_sort,
            column_value=column_value,
            column_kind=column_kind,
            default_fc_parameters=fc_params,
            n_jobs=self.n_jobs,
        )
        return extracted_features_df

    def _transform_df(self, X):
        """
        Transform pandas Dataframe to features
        """
        if self.episode_id is None:
            raise ValueError(
                "episode_id parameter not set in the TSFreshFeatureExtractor object"
            )

        if self.episode_data_column is None:
            raise ValueError(
                "episode_data_column parameter not set in the \
TSFreshFeatureExtractor object"
            )

        if self.time_id is None:
            raise ValueError(
                "time_id parameter not set in the TSFreshFeatureExtractor object"
            )

        # extracting features
        timeseries = self._prepare_ts_dataframe(X)
        extracted_features_df = self._tsfresh_apply(
            timeseries,
            column_id=self.episode_id,
            column_sort=self.time_id,
            column_value=None,
            column_kind=None,
            fc_params=self.fc_params,
        )

        return extracted_features_df

    def _transform_dict(self, X):
        """
        Transform input dict to features
        """
        # tests to do
        # check if the length of the episodes match
        # Attributes same in all episodes

        # check to see if all episodes have same attributes

        episode_list = list(X[self.episode_id])
        attr_list = X[self.episode_data_column][X.index[0]].keys()

        for i in range(X.shape[0]):
            if X[self.episode_data_column][X.index[i]].keys() == attr_list:
                continue
            else:
                LOGGER.info("Episodes have different attributes")
                raise ValueError(
                    "Episode "
                    + str(i)
                    + " has different attributes\
 compared the previous episodes. Every episode should have same attributes in the dataset."
                )

        extracted_features_df = pd.DataFrame()

        # refer to the link for the format
        # https://tsfresh.readthedocs.io/en/latest/text/data_formats.html#data-formats-label
        tsfresh_input_dict = {}

        for i, attr in enumerate(attr_list):

            data_col = []
            time_col = []
            id_col = []
            for j, episode in enumerate(episode_list):
                data_col += list(X[self.episode_data_column][X.index[j]][attr].values())
                time_col += list(X[self.episode_data_column][X.index[j]][attr].keys())
                id_col += [episode] * len(
                    X[self.episode_data_column][X.index[j]][attr].keys()
                )

            tmp_matrix = np.column_stack((id_col, time_col, data_col)).astype(float)
            tmp_input_df = pd.DataFrame(tmp_matrix, columns=["id", "time", "value"])
            tsfresh_input_dict[attr] = tmp_input_df

        extracted_features_df = self._tsfresh_apply(
            tsfresh_input_dict,
            column_id="id",
            column_sort="time",
            column_value="value",
            column_kind=None,
            fc_params=self.fc_params,
        )

        return extracted_features_df

    def _transform(self, X):
        """
        Main transformation function for dataframe feature extraction.
        """
        if self.episode_id is None:
            raise ValueError(
                "episode_id parameter not set in the TSFreshFeatureExtractor object"
            )

        if self.episode_data_column is None:
            raise ValueError(
                "episode_data_column parameter not set in the \
TSFreshFeatureExtractor object"
            )

        if isinstance(X[self.episode_data_column][X.index[0]], pd.DataFrame):
            return self._transform_df(X)
        elif isinstance(X[self.episode_data_column][X.index[0]], dict):
            return self._transform_dict(X)
        else:
            raise TypeError(
                "Data in episode_data_column should either pandas dataframe or dict"
            )

    def transform(self, X, **kwargs):
        """
        Parameters:
            X: pandas.DataFrame, required: transforming the input dataframe to the episode
            time series dataframe to be fed into the srom pipeline

        Returns:
            pandas.DataFrame: TS Fresh extracted dataframe
        """

        # checking if the input X is a pandas dataframe
        if not isinstance(X, pd.DataFrame):
            LOGGER.info("TSFreshFeatureExtractor needs pandas dataframe")
            raise ValueError("Input must be panda dataframe")

        extracted_features_df = self._transform(X)
        # checking if the order of the episode matches the input data

        if not (extracted_features_df.index.tolist()) == list(X[self.episode_id]):
            LOGGER.info(
                "input dataframe and ts fresh result - episode ordering not matching"
            )
            raise ValueError(
                "Sort the input dataframe by episode ID (ascending) before transform"
            )

        # replacing infinity with NaNs
        extracted_features_df = extracted_features_df.replace([np.inf, -np.inf], np.nan)
        extracted_features_columns = []

        # # excluding any columns if mentioned by the user in features_to_exclude parameter
        # if self.features_to_exclude:
        #     for col_name in extracted_features_df.columns:
        #         if any(('_'+feat) in col_name for feat in self.features_to_exclude):
        #             continue
        #         else:
        #             extracted_features_columns.append(col_name)
        # else:
        extracted_features_columns = extracted_features_df.columns

        # replacing NaNs with 0 and converting the extracted features dataframe to matrix
        extracted_features_df = extracted_features_df[extracted_features_columns]
        extracted_features_df = extracted_features_df.replace(np.nan, 0)
        extracted_features_df = extracted_features_df.values.astype(np.float64)

        # add a new column to maintain the name of column that are extraced
        self.extracted_features_columns = list(extracted_features_columns)

        return extracted_features_df


class StatisticalFeatureExtractor(TSFreshFeatureExtractor):
    """
    Performs episodic feature extraction on time series data
    using TSFresh Package with only a subset of TSFresh Params:

    'variance_larger_than_standard_deviation',
    'count_below_mean',
    'last_location_of_maximum',
    'first_location_of_maximum',
    'last_location_of_minimum',
    'first_location_of_minimum',
    'percentage_of_reoccurring_datapoints_to_all_datapoints',
    'count_above_mean',
    'percentage_of_reoccurring_values_to_all_values',
    'sum_of_reoccurring_data_points',
    'has_duplicate_min',
    'has_duplicate',
    'maximum',
    'minimum',
    'max_langevin_fixed_point',
    'sum_of_reoccurring_values',
    'longest_strike_above_mean',
    'ratio_value_number_to_time_series_length',
    'absolute_sum_of_changes',
    'sum_values',
    'has_duplicate_max',
    'mean_change',
    'mean_second_derivative_central',
    'mean_abs_change',
    'mean',
    'length',
    'standard_deviation',
    'variance',
    'skewness',
    'kurtosis',
    'median',
    'longest_strike_below_mean',
    'cid_ce',
    'spkt_welch_density',
    'range_count',
    'agg_autocorrelation',
    'time_reversal_asymmetry_statistic',
    'c3',
    'value_count',
    'number_crossing_m',
    'friedrich_coefficients',
    'linear_trend',
    'number_peaks',
    'ar_coefficient',
    'autocorrelation',
    'energy_ratio_by_chunks',
    'ratio_beyond_r_sigma',
    'large_standard_deviation',
    'symmetry_looking',
    'abs_energy',
    'agg_linear_trend'
    """

    def __init__(
        self,
        episode_id=None,
        episode_data_column=None,
        time_id=None,
        features_to_exclude=None,
        intermediate_feature_extraction=False,
        intermediate_result_path=None,
        n_jobs=2,
        distributor=None,
        save_suffix="",
    ):
        """
        Parameters:
            episode_id (string, required): column name w.r.t. which data extraction is performed
            when data is in pandas dataframe
            episode_data_column (string, required): column name that contains panda dataframe
            to describe episode data
            time_id (string, optional): column name for a data frame contained episode_data_column
            features_to_exclude (string, optional): types of features to not include in
            the feature extraction using TSFresh
            intermediate_feature_extraction (boolean, optional): Executes the feature extraction
                in an iterative method by breaking the param grid and executing for each parameter setting.
                The intermediate results are saved in the file system. `intermediate_result_path` is the path where
                resulting files should be stored. `save_suffix` is the user-specified suffix which is
                used to identify resulting file names uniquely.
            intermediate_result_path (string, optional): the path where resulting files
                are saved if `intermediate_feature_extraction`= True.
            save_suffix (string, optional): user-specified suffix which is used to identify resulting
                file names uniquely if `intermediate_feature_extraction`= True.
            n_jobs (optional): parameter passed to tsfresh extractor.
            distributor (optional):parameter passed to tsfresh extractor.

        Returns:
            Object of the class TSFreshFeatureExtractor.
        """
        super(StatisticalFeatureExtractor, self).__init__(
            episode_id=episode_id,
            episode_data_column=episode_data_column,
            time_id=time_id,
            features_to_exclude=features_to_exclude,
            intermediate_feature_extraction=intermediate_feature_extraction,
            intermediate_result_path=intermediate_result_path,
            n_jobs=n_jobs,
            distributor=distributor,
            save_suffix=save_suffix,
        )

        settings = STATISTICAL_FEATURES
        self.set_fc_params(generate_param_grid(settings))


class FFTFeatureExtractor(TSFreshFeatureExtractor):
    """
    Performs episodic feature extraction on time series data
    using TSFresh Package with only a subset of TSFresh Params:

    'fft_coefficient'
    """

    def __init__(
        self,
        episode_id=None,
        episode_data_column=None,
        time_id=None,
        features_to_exclude=None,
        intermediate_feature_extraction=False,
        intermediate_result_path=None,
        n_jobs=2,
        distributor=None,
        save_suffix="",
    ):
        """
        Parameters:
            episode_id (string, required): column name w.r.t. which data extraction is performed
            when data is in pandas dataframe
            episode_data_column (string, required): column name that contains panda dataframe
            to describe episode data
            time_id (string, optional): column name for a data frame contained episode_data_column
            features_to_exclude (string, optional): types of features to not include in
            the feature extraction using TSFresh
            intermediate_feature_extraction (boolean, optional): Executes the feature extraction
                in an iterative method by breaking the param grid and executing for each parameter setting.
                The intermediate results are saved in the file system. `intermediate_result_path` is the path where
                resulting files should be stored. `save_suffix` is the user-specified suffix which is
                used to identify resulting file names uniquely.
            intermediate_result_path (string, optional): the path where resulting files
                are saved if `intermediate_feature_extraction`= True.
            save_suffix (string, optional): user-specified suffix which is used to identify resulting
                file names uniquely if `intermediate_feature_extraction`= True.
            n_jobs (optional): parameter passed to tsfresh extractor.
            distributor (optional):parameter passed to tsfresh extractor.

        Returns:
            Object of the class TSFreshFeatureExtractor.
        """
        super(FFTFeatureExtractor, self).__init__(
            episode_id=episode_id,
            episode_data_column=episode_data_column,
            time_id=time_id,
            features_to_exclude=features_to_exclude,
            intermediate_feature_extraction=intermediate_feature_extraction,
            intermediate_result_path=intermediate_result_path,
            n_jobs=n_jobs,
            distributor=distributor,
            save_suffix=save_suffix,
        )

        settings = FFT_FEATURES
        self.set_fc_params(generate_param_grid(settings))


class EntropyFeatureExtractor(TSFreshFeatureExtractor):
    """
    Performs episodic feature extraction on time series data
    using TSFresh Package with only a subset of TSFresh Params:

        'approximate_entropy',
        'sample_entropy',
        'binned_entropy'
    """

    def __init__(
        self,
        episode_id=None,
        episode_data_column=None,
        time_id=None,
        features_to_exclude=None,
        intermediate_feature_extraction=False,
        intermediate_result_path=None,
        n_jobs=2,
        distributor=None,
        save_suffix="",
    ):
        """
        Parameters:
            episode_id (string, required): column name w.r.t. which data extraction is performed
            when data is in pandas dataframe
            episode_data_column (string, required): column name that contains panda dataframe
            to describe episode data
            time_id (string, optional): column name for a data frame contained episode_data_column
            features_to_exclude (string, optional): types of features to not include in
            the feature extraction using TSFresh
            intermediate_feature_extraction (boolean, optional): Executes the feature extraction
                in an iterative method by breaking the param grid and executing for each parameter setting.
                The intermediate results are saved in the file system. `intermediate_result_path` is the path where
                resulting files should be stored. `save_suffix` is the user-specified suffix which is
                used to identify resulting file names uniquely.
            intermediate_result_path (string, optional): the path where resulting files
                are saved if `intermediate_feature_extraction`= True.
            save_suffix (string, optional): user-specified suffix which is used to identify resulting
                file names uniquely if `intermediate_feature_extraction`= True.
            n_jobs (optional): parameter passed to tsfresh extractor.
            distributor (optional):parameter passed to tsfresh extractor.

        Returns:
            Object of the class TSFreshFeatureExtractor.
        """
        super(EntropyFeatureExtractor, self).__init__(
            episode_id=episode_id,
            episode_data_column=episode_data_column,
            time_id=time_id,
            features_to_exclude=features_to_exclude,
            intermediate_feature_extraction=intermediate_feature_extraction,
            intermediate_result_path=intermediate_result_path,
            n_jobs=n_jobs,
            distributor=distributor,
            save_suffix=save_suffix,
        )

        settings = ENTROPY_FEATUES
        self.set_fc_params(generate_param_grid(settings))


class CWTFeatureExtractor(TSFreshFeatureExtractor):
    """
    Performs episodic feature extraction on time series data
    using TSFresh Package with only a subset of TSFresh Params:

    'cwt_coefficients',
    'number_cwt_peaks'
    """

    def __init__(
        self,
        episode_id=None,
        episode_data_column=None,
        time_id=None,
        features_to_exclude=None,
        intermediate_feature_extraction=False,
        intermediate_result_path=None,
        n_jobs=2,
        distributor=None,
        save_suffix="",
    ):
        """
        Parameters:
            episode_id (string, required): column name w.r.t. which data extraction is performed
            when data is in pandas dataframe
            episode_data_column (string, required): column name that contains panda dataframe
            to describe episode data
            time_id (string, optional): column name for a data frame contained episode_data_column
            features_to_exclude (string, optional): types of features to not include in
            the feature extraction using TSFresh
            intermediate_feature_extraction (boolean, optional): Executes the feature extraction
                in an iterative method by breaking the param grid and executing for each parameter setting.
                The intermediate results are saved in the file system. `intermediate_result_path` is the path where
                resulting files should be stored. `save_suffix` is the user-specified suffix which is
                used to identify resulting file names uniquely.
            intermediate_result_path (string, optional): the path where resulting files
                are saved if `intermediate_feature_extraction`= True.
            save_suffix (string, optional): user-specified suffix which is used to identify resulting
                file names uniquely if `intermediate_feature_extraction`= True.
            n_jobs (optional): parameter passed to tsfresh extractor.
            distributor (optional):parameter passed to tsfresh extractor.

        Returns:
            Object of the class TSFreshFeatureExtractor.
        """
        super(CWTFeatureExtractor, self).__init__(
            episode_id=episode_id,
            episode_data_column=episode_data_column,
            time_id=time_id,
            features_to_exclude=features_to_exclude,
            intermediate_feature_extraction=intermediate_feature_extraction,
            intermediate_result_path=intermediate_result_path,
            n_jobs=n_jobs,
            distributor=distributor,
            save_suffix=save_suffix,
        )

        settings = CWT_FEATURES
        self.set_fc_params(generate_param_grid(settings))


class ExpensiveFeatureExtractor(TSFreshFeatureExtractor):
    """
    Performs episodic feature extraction on time series data
    using TSFresh Package with only a subset of TSFresh Params:

    'augmented_dickey_fuller',
    'partial_autocorrelation'
    """

    def __init__(
        self,
        episode_id=None,
        episode_data_column=None,
        time_id=None,
        features_to_exclude=None,
        intermediate_feature_extraction=False,
        intermediate_result_path=None,
        n_jobs=2,
        distributor=None,
        save_suffix="",
    ):
        """
        Parameters:
            episode_id (string, required): column name w.r.t. which data extraction is performed
            when data is in pandas dataframe
            episode_data_column (string, required): column name that contains panda dataframe
            to describe episode data
            time_id (string, optional): column name for a data frame contained episode_data_column
            features_to_exclude (string, optional): types of features to not include in
            the feature extraction using TSFresh
            intermediate_feature_extraction (boolean, optional): Executes the feature extraction
                in an iterative method by breaking the param grid and executing for each parameter setting.
                The intermediate results are saved in the file system. `intermediate_result_path` is the path where
                resulting files should be stored. `save_suffix` is the user-specified suffix which is
                used to identify resulting file names uniquely.
            intermediate_result_path (string, optional): the path where resulting files
                are saved if `intermediate_feature_extraction`= True.
            save_suffix (string, optional): user-specified suffix which is used to identify resulting
                file names uniquely if `intermediate_feature_extraction`= True.
            n_jobs (optional): parameter passed to tsfresh extractor.
            distributor (optional):parameter passed to tsfresh extractor.

        Returns:
            Object of the class TSFreshFeatureExtractor.
        """
        super(ExpensiveFeatureExtractor, self).__init__(
            episode_id=episode_id,
            episode_data_column=episode_data_column,
            time_id=time_id,
            features_to_exclude=features_to_exclude,
            intermediate_feature_extraction=intermediate_feature_extraction,
            intermediate_result_path=intermediate_result_path,
            n_jobs=n_jobs,
            distributor=distributor,
            save_suffix=save_suffix,
        )

        settings = EXPENSIVE_FEATURES
        self.set_fc_params(generate_param_grid(settings))


class QuantileFeatureExtractor(TSFreshFeatureExtractor):
    """
    Performs episodic feature extraction on time series data
    using TSFresh Package with only a subset of TSFresh Params:

    'quantile',
    'index_mass_quantile',
    'change_quantiles'
    """

    def __init__(
        self,
        episode_id=None,
        episode_data_column=None,
        time_id=None,
        features_to_exclude=None,
        intermediate_feature_extraction=False,
        intermediate_result_path=None,
        n_jobs=2,
        distributor=None,
        save_suffix="",
    ):
        """
        Parameters:
            episode_id (string, required): column name w.r.t. which data extraction is performed
            when data is in pandas dataframe
            episode_data_column (string, required): column name that contains panda dataframe
            to describe episode data
            time_id (string, optional): column name for a data frame contained episode_data_column
            features_to_exclude (string, optional): types of features to not include in
            the feature extraction using TSFresh
            intermediate_feature_extraction (boolean, optional): Executes the feature extraction
                in an iterative method by breaking the param grid and executing for each parameter setting.
                The intermediate results are saved in the file system. `intermediate_result_path` is the path where
                resulting files should be stored. `save_suffix` is the user-specified suffix which is
                used to identify resulting file names uniquely.
            intermediate_result_path (string, optional): the path where resulting files
                are saved if `intermediate_feature_extraction`= True.
            save_suffix (string, optional): user-specified suffix which is used to identify resulting
                file names uniquely if `intermediate_feature_extraction`= True.
            n_jobs (optional): parameter passed to tsfresh extractor.
            distributor (optional):parameter passed to tsfresh extractor.

        Returns:
            Object of the class TSFreshFeatureExtractor.
        """
        super(QuantileFeatureExtractor, self).__init__(
            episode_id=episode_id,
            episode_data_column=episode_data_column,
            time_id=time_id,
            features_to_exclude=features_to_exclude,
            intermediate_feature_extraction=intermediate_feature_extraction,
            intermediate_result_path=intermediate_result_path,
            n_jobs=n_jobs,
            distributor=distributor,
            save_suffix=save_suffix,
        )

        settings = QUANTILE_FEATURES
        self.set_fc_params(generate_param_grid(settings))
