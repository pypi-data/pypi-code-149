# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: asset_scaler
   :synopsis: Scale Each Asset Separately.

.. moduleauthor:: SROM Team
"""
import copy
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

class AssetScaler(BaseEstimator, TransformerMixin):
    """
    Apply Scalling on each Asset, one after another Normal Scaler \
    is applied on dataset, where  AssetScaler is applied for each \
    group of the data identified using id columns.

    Parameters:
    asset_id (string, required): Name of column in input data that \
        represent the name of asset.
    scaler (scaler object, required): An object of scaler that will \
        be applied to each assets.
    columns_to_be_ignored (list of strings, optional): columns to be \
        used for no scaling.

    Examples
    --------
    >>> data = [[0, 0], [0, 0], [1, 1], [1, 1], [0, 0], [0, 0], [1, 1], [1, 1]]
    >>> D = pd.DataFrame(data)
    >>> D.columns = ['va1','va2']
    >>> D['id'] = ['a','a','a','a','b','b','b','b']
    >>> print (D)
    >>> A = AssetScaler(asset_id='id',execute_on_spark=False)
    >>> print (A.fit(D))
    >>> print (A.transform(D))
    """
    def __init__(self, asset_id=None,
                 columns_to_be_ignored=None, scaler=StandardScaler()):
        self._asset_id = asset_id
        self._scaler = copy.deepcopy(scaler)
        if not columns_to_be_ignored:
            self._columns_to_ignored = []
        else:
            self._columns_to_ignored = columns_to_be_ignored
        self._scaled_asset_ids = None
        self._fitted_scalers = None
        self._scale_clms = None

    def fit(self, X):
        """
        The function is used to create scaling range \
        from the fitting data provided by the user.

        Parameters:
        X (dataframe or matrix like object, required): User provided \
            dataframe over which the scaling range is fitted by the scaler.
        """
        self._scaled_asset_ids = []
        self._fitted_scalers = []
        self._scale_clms = list(X.columns)
        self._scale_clms.remove(self._asset_id)
        for item in self._columns_to_ignored:
            self._scale_clms.remove(item)

        for name, grp in X.groupby(self._asset_id):
            tmp_scaler = copy.deepcopy(self._scaler)
            tmp_scaler.fit(grp[self._scale_clms])
            self._scaled_asset_ids.append(name)
            self._fitted_scalers.append(tmp_scaler)
        return self

    def transform(self, X):
        """
        Function to scale the a new dataframe based on \
        the fitted scaler.

        Parameters:
        X (dataframe or matrix like object, required): User provided \
            dataframe over which the scaling range is transformed by \
            the fitted scaler.

        Returns:
        scaled_df (dataframe or matrix like object): Scaled dataframe \
            is returned.
        """
        if not self._scaled_asset_ids and not self._fitted_scalers and not self._scale_clms:
            raise Exception("Please call fit method first")

        tmp_result = []
        for name, grp in X.groupby(self._asset_id):
            ind_retainer = (grp.index)
            tmp_ind = self._scaled_asset_ids.index(name)
            tmp_out = self._fitted_scalers[tmp_ind].transform(grp[self._scale_clms])
            tmp_out = pd.DataFrame(tmp_out)
            tmp_out = tmp_out.set_index(ind_retainer)
            tmp_out.columns = self._scale_clms
            tmp_out[self._asset_id] = name
            for item in self._columns_to_ignored:
                tmp_out[item] = list(grp[item])
            tmp_result.append(tmp_out)

        scaled_df = pd.concat(tmp_result)
        scaled_df.sort_index(inplace=True)
        return scaled_df
