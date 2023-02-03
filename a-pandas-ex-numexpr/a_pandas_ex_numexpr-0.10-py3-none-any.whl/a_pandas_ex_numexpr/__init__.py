import pandas as pd
from pandas.core.frame import DataFrame, Series
from tolerant_isinstance import isinstance_tolerant
import numpy as np

import numexpr


def search_in_all_columns(df, expr, dtype=None, *args, **kwargs):
    allindis = []
    for col in df.columns:
        try:
            if not dtype:
                b = df[col].__array__()
            else:
                b = df[col].__array__().astype(dtype)
            evas = numexpr.evaluate(expr, *args, **kwargs)
            exa = np.array(np.where(evas)).flatten()
            if len(exa) > 0:
                allindis.append(exa)
        except Exception as fe:
            continue
    if len(allindis) > 0:
        return np.concatenate(allindis)
    return []


def search_string_dataframe_allhits_contains(df, stri, *args, **kwargs):
    return df.loc[search_for_string_series_contains(df, stri=stri, *args, **kwargs)]


def search_string_dataframe_contains(df, stri, *args, **kwargs):
    return df.loc[
        search_for_string_series_contains(df, stri=stri, *args, **kwargs)
    ].drop_duplicates()


def search_string_dataframe_allhits_equal(df, stri, *args, **kwargs):
    return df.loc[search_for_string_series_equal(df, stri=stri, *args, **kwargs)]


def search_string_dataframe_equal(df, stri, *args, **kwargs):
    return df.loc[
        search_for_string_series_equal(df, stri=stri, *args, **kwargs)
    ].drop_duplicates()


def search_for_string_series_equal(df, stri, *args, **kwargs):

    b = df.__array__().astype("S")
    stra = stri.encode()
    return numexpr.evaluate(f"(b == {stra})", *args, **kwargs)


def search_for_string_series_contains(df, stri, *args, **kwargs):

    b = df.__array__().astype("S")
    stra = stri.encode()
    return numexpr.evaluate(f"contains(b, {stra})", *args, **kwargs)


def ne_equal_df_ind(df, expr, dtype=None, *args, **kwargs):
    return search_in_all_columns(df, f"(b == {expr})", dtype=dtype, *args, **kwargs)


def ne_equal_df_ind_no_dup(df, expr, *args, **kwargs):
    ini = ne_equal_df_ind(df, expr, *args, **kwargs)
    return np.unique(ini)


def ne_equal_df_dup(df, expr, *args, **kwargs):
    ini = ne_equal_df_ind(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_equal_df_no_dup(df, expr, *args, **kwargs):
    ini = ne_equal_df_ind_no_dup(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_equal(df, expr, *args, **kwargs):
    b = df.__array__()
    return numexpr.evaluate(f"(b == {expr})", *args, **kwargs)


def ne_not_equal_df_ind(df, expr, dtype=None, *args, **kwargs):
    return search_in_all_columns(df, f"(b != {expr})", dtype=dtype, *args, **kwargs)


def ne_not_equal_df_ind_no_dup(df, expr, *args, **kwargs):
    ini = ne_not_equal_df_ind(df, expr, *args, **kwargs)
    return np.unique(ini)


def ne_not_equal_df_dup(df, expr, *args, **kwargs):
    ini = ne_not_equal_df_ind(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_not_equal_df_no_dup(df, expr, *args, **kwargs):
    ini = ne_not_equal_df_ind_no_dup(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_not_equal(df, expr, *args, **kwargs):
    b = df.__array__()
    return numexpr.evaluate(f"(b != {expr})", *args, **kwargs)


def ne_greater_than_df_ind(df, expr, dtype=None, *args, **kwargs):
    return search_in_all_columns(df, f"(b > {expr})", dtype=dtype, *args, **kwargs)


def ne_greater_than_df_ind_no_dup(df, expr, *args, **kwargs):
    ini = ne_greater_than_df_ind(df, expr, *args, **kwargs)
    return np.unique(ini)


def ne_greater_than_df_dup(df, expr, *args, **kwargs):
    ini = ne_greater_than_df_ind(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_greater_than_df_no_dup(df, expr, *args, **kwargs):
    ini = ne_greater_than_df_ind_no_dup(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_greater_than(df, expr, *args, **kwargs):
    b = df.__array__()
    return numexpr.evaluate(f"(b > {expr})", *args, **kwargs)


def ne_less_than_df_ind(df, expr, dtype=None, *args, **kwargs):
    return search_in_all_columns(df, f"(b < {expr})", dtype=dtype, *args, **kwargs)


def ne_less_than_df_ind_no_dup(df, expr, *args, **kwargs):
    ini = ne_less_than_df_ind(df, expr, *args, **kwargs)
    return np.unique(ini)


def ne_less_than_df_dup(df, expr, *args, **kwargs):
    ini = ne_less_than_df_ind(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_less_than_df_no_dup(df, expr, *args, **kwargs):
    ini = ne_less_than_df_ind_no_dup(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_less_than(df, expr, *args, **kwargs):
    b = df.__array__()
    return numexpr.evaluate(f"(b < {expr})", *args, **kwargs)


def ne_greater_than_or_equal_to_df_ind(df, expr, dtype=None, *args, **kwargs):
    return search_in_all_columns(df, f"(b >= {expr})", dtype=dtype, *args, **kwargs)


def ne_greater_than_or_equal_to_df_ind_no_dup(df, expr, *args, **kwargs):
    ini = ne_greater_than_or_equal_to_df_ind(df, expr, *args, **kwargs)
    return np.unique(ini)


def ne_greater_than_or_equal_to_df_dup(df, expr, *args, **kwargs):
    ini = ne_greater_than_or_equal_to_df_ind(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_greater_than_or_equal_to_df_no_dup(df, expr, *args, **kwargs):
    ini = ne_greater_than_or_equal_to_df_ind_no_dup(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_greater_than_or_equal_to(df, expr, *args, **kwargs):
    b = df.__array__()
    return numexpr.evaluate(f"(b >= {expr})", *args, **kwargs)


def ne_less_than_or_equal_to_df_ind(df, expr, dtype=None, *args, **kwargs):
    return search_in_all_columns(df, f"(b <= {expr})", dtype=dtype, *args, **kwargs)


def ne_less_than_or_equal_to_df_ind_no_dup(df, expr, *args, **kwargs):
    ini = ne_less_than_or_equal_to_df_ind(df, expr, *args, **kwargs)
    return np.unique(ini)


def ne_less_than_or_equal_to_df_dup(df, expr, *args, **kwargs):
    ini = ne_less_than_or_equal_to_df_ind(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_less_than_or_equal_to_df_no_dup(df, expr, *args, **kwargs):
    ini = ne_less_than_or_equal_to_df_ind_no_dup(df, expr, *args, **kwargs)
    return df.loc[ini]


def ne_less_than_or_equal_to(df, expr, *args, **kwargs):
    b = df.__array__()
    return numexpr.evaluate(f"(b <= {expr})", *args, **kwargs)


def ne_query(df, expr, return_np=True, *args, **kwargs):
    if isinstance_tolerant(df, (pd.DataFrame, pd.Series)):
        b = df.__array__()
    else:
        b = df
    if "local_dict" in kwargs:
        for key, item in kwargs.items():
            if isinstance_tolerant(item, (pd.DataFrame, pd.Series)):
                kwargs[key] = kwargs[key].__array__()
        kwargs["local_dict"]["b"] = b
    resa=numexpr.evaluate(f"({expr})", *args, **kwargs)
    if not return_np:
        return pd.Series(resa,index=df.index)
    return resa



def pd_add_numexpr():

    DataFrame.ne_search_in_all_columns = search_in_all_columns

    DataFrame.ne_search_string_allhits_contains = (
        search_string_dataframe_allhits_contains
    )

    Series.ne_search_string_allhits_contains = search_string_dataframe_allhits_contains

    DataFrame.ne_search_string_dataframe_contains = search_string_dataframe_contains

    DataFrame.ne_search_string_dataframe_allhits_equal = (
        search_string_dataframe_allhits_equal
    )

    Series.ne_search_string_dataframe_allhits_equal = (
        search_string_dataframe_allhits_equal
    )

    DataFrame.ne_search_string_dataframe_equal = search_string_dataframe_equal

    Series.ne_search_for_string_series_equal = search_for_string_series_equal

    DataFrame.ne_search_for_string_contains = search_for_string_series_contains

    Series.ne_search_for_string_contains = search_for_string_series_contains

    DataFrame.ne_equal_df_ind = ne_equal_df_ind

    DataFrame.ne_equal_df_ind_no_dup = ne_equal_df_ind_no_dup

    DataFrame.ne_equal_df_dup = ne_equal_df_dup

    DataFrame.ne_equal_df_no_dup = ne_equal_df_no_dup

    Series.ne_equal = ne_equal

    DataFrame.ne_not_equal_df_ind = ne_not_equal_df_ind

    DataFrame.ne_not_equal_df_ind_no_dup = ne_not_equal_df_ind_no_dup

    DataFrame.ne_not_equal_df_dup = ne_not_equal_df_dup

    DataFrame.ne_not_equal_df_no_dup = ne_not_equal_df_no_dup

    Series.ne_not_equal = ne_not_equal

    DataFrame.ne_greater_than_df_ind = ne_greater_than_df_ind

    DataFrame.ne_greater_than_df_ind_no_dup = ne_greater_than_df_ind_no_dup

    DataFrame.ne_greater_than_df_dup = ne_greater_than_df_dup

    DataFrame.ne_greater_than_df_no_dup = ne_greater_than_df_no_dup

    Series.ne_greater_than = ne_greater_than

    DataFrame.ne_less_than_df_ind = ne_less_than_df_ind

    DataFrame.ne_less_than_df_ind_no_dup = ne_less_than_df_ind_no_dup

    DataFrame.ne_less_than_df_dup = ne_less_than_df_dup

    DataFrame.ne_less_than_df_no_dup = ne_less_than_df_no_dup

    Series.ne_less_than = ne_less_than

    DataFrame.ne_greater_than_or_equal_to_df_ind = ne_greater_than_or_equal_to_df_ind

    DataFrame.ne_greater_than_or_equal_to_df_ind_no_dup = (
        ne_greater_than_or_equal_to_df_ind_no_dup
    )

    DataFrame.ne_greater_than_or_equal_to_df_dup = ne_greater_than_or_equal_to_df_dup

    DataFrame.ne_greater_than_or_equal_to_df_no_dup = (
        ne_greater_than_or_equal_to_df_no_dup
    )

    Series.ne_greater_than_or_equal_to = ne_greater_than_or_equal_to

    DataFrame.ne_less_than_or_equal_to_df_ind = ne_less_than_or_equal_to_df_ind

    DataFrame.ne_less_than_or_equal_to_df_ind_no_dup = (
        ne_less_than_or_equal_to_df_ind_no_dup
    )

    DataFrame.ne_less_than_or_equal_to_df_dup = ne_less_than_or_equal_to_df_dup

    DataFrame.ne_less_than_or_equal_to_df_no_dup = ne_less_than_or_equal_to_df_no_dup

    Series.ne_less_than_or_equal_to = ne_less_than_or_equal_to

    DataFrame.ne_query = ne_query

    Series.ne_query = ne_query
