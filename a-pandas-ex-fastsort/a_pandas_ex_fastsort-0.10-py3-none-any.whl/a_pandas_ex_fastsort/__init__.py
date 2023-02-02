from npfastsortcpp import parallelsort
import pandas as pd
from pandas.core.frame import DataFrame, Series


def fast_reindex(df, *args, **kwargs):
    indi = df.index.__array__().copy()
    parallelsort(indi)
    return df.reindex(indi, *args, **kwargs)


def sort_series_copy(df):
    indi = df.__array__().copy()
    parallelsort(indi)
    return pd.Series(indi)


def sort_series_inpl(df):
    indi = df.__array__()
    parallelsort(indi)


def pd_add_fastsort():
    Series.s_fastsort_inplace = sort_series_inpl
    Series.s_fastsort_copy = sort_series_copy
    DataFrame.d_fast_reindex = fast_reindex

