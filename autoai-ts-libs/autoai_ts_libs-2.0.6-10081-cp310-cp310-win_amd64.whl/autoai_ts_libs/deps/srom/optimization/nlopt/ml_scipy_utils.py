"""Utilities for bridging scipy and ml model
data input requirements."""

from typing import List, Tuple, Iterable

import pandas as pd
import numpy as np

import copy

from collections import namedtuple

from pandas.core.frame import DataFrame

# Point = namedtuple('Point', ['x', 'y', 'z'], defaults = [1]);
# a = Point(1, 1, 0); # a.x = 1, a.y = 1, a.z = 0

# Default value used for `z`
# b = Point(2, 2); # b.x = 2, b.y = 2, b.z = 1 (default)

#
FlattenInfo = namedtuple(
    "FlattenInfo",
    [
        "fctrlvals",
        "fobsvals",
        "fctrlnames",
        "fobsnames",
        "u2fmapping",
        "uctrlnames",
        "uobsnames",
    ],
)


def dedup(colnames: List[str]):
    uniq = set(colnames)
    acopy: List[str] = copy.copy(colnames)

    mapping = {}

    for u in uniq:
        mapping[u] = []
        count = 0
        for idx, val in enumerate(colnames):
            if u == val:
                acopy[idx] = f"{u}_{count}"
                count += 1
                mapping[u].append(acopy[idx])

    return acopy, mapping


def flatteninfo(
    ucontrols: List[str], uobservables: List[str], adataframe: pd.DataFrame
) -> FlattenInfo:
    """Flattens a given pandas dataframe
    into a 1x(mxn) array where m and n are the number
    of rows and columns in X respectively.
    Returns a namedtuple
    """
    if len(adataframe.columns) != len(set(adataframe.columns)):
        raise Exception("data frame contains non-unique columns, this is not allowed")

    rows, _ = adataframe.shape

    control_cols = rows * len(ucontrols)
    obs_cols = rows * len(uobservables)
    fctrlvals = adataframe[ucontrols].values.reshape(1, control_cols)
    fobsvals = adataframe[uobservables].values.reshape(1, obs_cols)

    obs_names, obsmapping = dedup(uobservables * rows)
    fctrlnames, control_mapping = dedup(ucontrols * rows)

    allmapping = {}
    allmapping.update(obsmapping)
    allmapping.update(control_mapping)

    answer = FlattenInfo(
        fctrlvals=fctrlvals,
        fobsvals=fobsvals,
        fctrlnames=fctrlnames,
        fobsnames=obs_names,
        u2fmapping=allmapping,
        uctrlnames=ucontrols,
        uobsnames=uobservables,
    )
    return answer


def flatten(info: FlattenInfo) -> pd.DataFrame:
    """Flattens a given pandas dataframe returning it as 1 x (rows x columns)
    pandas DataFrame
    """
    cdf: pd.DataFrame = pd.DataFrame(data=info.fctrlvals, columns=info.fctrlnames)
    odf: pd.DataFrame = pd.DataFrame(data=info.fobsvals, columns=info.fobsnames)
    answer = cdf.join(odf)
    return answer


def unflatten(info: FlattenInfo, flattened_df: pd.DataFrame = None) -> pd.DataFrame:
    """Perform inverse operation of flatten, returning a dataframe.
    if flattened_df is not None, it will substitute current
    data from this dataframe to do the unflattending"""

    crows = int(len(info.fctrlnames) / len(info.uctrlnames))

    if flattened_df is None:
        cdata = info.fctrlvals
        odata = info.fobsvals
    else:
        cdata = flattened_df[info.fctrlnames].iloc[0].values
        odata = flattened_df[info.fobsnames].iloc[0].values

    control_df = pd.DataFrame(
        data=cdata.reshape(
            crows,
            len(info.uctrlnames),
        ),
        columns=info.uctrlnames,
    )

    orows = int(len(info.fobsnames) / len(info.uobsnames))
    observable_df = pd.DataFrame(
        data=odata.reshape(
            orows,
            len(info.uobsnames),
        ),
        columns=info.uobsnames,
    )

    return control_df.join(observable_df)


if __name__ == "__main__":

    df: pd.DataFrame = pd.DataFrame(
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], columns=["C1", "O1", "C2", "O2"]
    )

    print("original", "**********")
    print(df)

    f: FlattenInfo = flatteninfo(
        ucontrols=["C1", "C2"], uobservables=["O1", "O2"], adataframe=df
    )

    print("flatteninfo", "**********")
    print(f)

    print("flattened df", "*************")
    print(flatten(f))

    print("unflattened (should be same as original)", "**********")
    print(unflatten(f))

    flattened = flatten(f)
    flattened["C1_0"] = [-10]
    flattened["C1_1"] = [-20]
    flattened["C1_2"] = [-30]
    flattened["O1_0"] = [-100]
    flattened["O1_1"] = [-200]
    flattened["O1_2"] = [-300]

    print("flattened df", "*************")
    print(unflatten(f, flattened))
