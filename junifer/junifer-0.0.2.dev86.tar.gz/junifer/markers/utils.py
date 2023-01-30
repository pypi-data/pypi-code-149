"""Provide utility functions shared by different markers."""

# Authors: Leonard Sasse <l.sasse@fz-juelich.de>
#          Nicolás Nieto <n.nieto@fz-juelich.de>
#          Sami Hamdan <s.hamdan@fz-juelich.de>
#          Synchon Mandal <s.mandal@fz-juelich.de>
#          Federico Raimondo <f.raimondo@fz-juelich.de>
# License: AGPL

from typing import Any, Callable, Dict, List, Type, Union

import numpy as np
import pandas as pd
from scipy.stats import zscore

from ..utils import raise_error


def singleton(cls: Type) -> Type:
    """Make a class singleton.

    Parameters
    ----------
    cls : class
        The class to designate as singleton.

    Returns
    -------
    class
        The only instance of the class.

    """
    instances: Dict = {}

    def get_instance(*args: Any, **kwargs: Any) -> Type:
        """Get the only instance for a class.

        Parameters
        ----------
        *args : tuple
            The positional arguments to pass to the class.
        **kwargs : dict
            The keyword arguments to pass to the class.

        Returns
        -------
        class
            The only instance of the class.

        """
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def _ets(
    bold_ts: np.ndarray, roi_names: Union[None, List[str]] = None
) -> np.ndarray:
    """Compute the edge-wise time series based on BOLD time series.

    Take a timeseries of brain areas, and calculate timeseries for each
    edge according to the method outlined in [1]_. For more information,
    check https://github.com/brain-networks/edge-ts/blob/master/main.m

    Parameters
    ----------
    bold_ts : np.ndarray
        BOLD time series (time x ROIs)
    roi_names : List[str] or None
        List containing the names of the ROIs.
        Order of the ROI names should correspond to order of the columns
        in bold_ts. If None (default), only the edge-wise time series are
        returned, without corresponding edge labels.

    Returns
    -------
    ets : np.ndarray
        edge-wise time series, i.e. estimate of functional connectivity at each
        time point.
    edge_names : List[str]
        List of edge names corresponding to columns in the
        edge-wise time series. This is only returned if the roi_names
        are specified.

    References
    ----------
    .. [1] Zamani Esfahlani et al. (2020)
            High-amplitude cofluctuations in cortical activity drive
            functional connectivity
            doi: 10.1073/pnas.2005531117

    """
    # Compute the z-score for each brain region's timeseries
    timeseries = zscore(bold_ts)
    # Get the number of ROIs
    _, n_roi = timeseries.shape
    # indices of unique edges (lower triangle)
    u, v = np.tril_indices(n_roi, k=-1)
    # Compute the ETS
    ets = timeseries[:, u] * timeseries[:, v]
    # Obtain the corresponding edge labels if specified else return
    if roi_names is None:
        return ets
    else:
        if len(roi_names) != n_roi:
            raise_error(
                "List of roi names does not correspond "
                "to the number of ROIs in the timeseries!"
            )
        roi_names = np.array(roi_names)
        edge_names = [
            "~".join([x, y]) for x, y in zip(roi_names[u], roi_names[v])
        ]
        return ets, list(edge_names)


def _correlate_dataframes(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    method: Union[str, Callable] = "pearson",
) -> pd.DataFrame:
    """Column-wise correlations between two dataframes.

    Correlates each column of `df1` with each column of `df2`.
    Output is a dataframe of shape (df2.shape[1], df1.shape[1]).
    It is required that number of rows are matched.

    Parameters
    ----------
    df1 : pandas.DataFrame
        The first dataframe.
    df2 : pandas.DataFrame
        The second dataframe.
    method : str or callable, optional
        any method that can be passed to
        :func:`pandas.DataFrame.corr` (default "pearson").

    Returns
    -------
    df_corr : pandas.DataFrame
        The correlated values as a dataframe.

    Raises
    ------
    ValueError
        If number of rows between dataframes are not matched.

    """

    if df1.shape[0] != df2.shape[0]:
        raise_error("pandas.DataFrame's have unequal number of rows!")
    return (
        pd.concat([df1, df2], axis=1, keys=["df1", "df2"])  # type: ignore
        .corr(method=method)  # type: ignore
        .loc["df2", "df1"]
    )
