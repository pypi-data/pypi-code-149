# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: dataframe_scaler
   :synopsis: Dataframe Scaler module.

.. moduleauthor:: SROM Team
"""
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler as SKLStandardScaler
import pandas as pd

class StandardScaler():
    """
    Wraps a scklearn.preprocessing.StandardScaler \
    object providing Convenience functions.
    """
    def __init__(self):
        self._impl = SKLStandardScaler()

    def forward_transform(self, pdframe, dropna=True):
        """ 
        Perform forward transform.

        Parameters:
            pdframe (pandas.DataFrame): Input pandas Dataframe.
            dropna (boolean): If True, dropna will be called \
                on pdataframe first.

        Raises:
            answer: A new pandas.Dataframe that has been scaled.
        """ 
        self._impl.fit_transform(pdframe.dropna() if dropna else pdframe)
        answer = (pdframe - self._impl.mean_)/(self._impl.scale_)
        return answer
    def reverse_transform(self, pdframe, dropna=True):

        """
        Perform reverse transform.

        Parameters:
            pdframe (pandas.DataFrame): Input pandas Dataframe that has \
                already been scaled.
            dropna (boolean): If True, dropna will be called on pdataframe first.

        Raises:
            answer: A new pandas.Dataframe that has been transformed back to \
                unscaled space.
        """
        answer = pd.DataFrame(self._impl.inverse_transform(pdframe.dropna() if dropna else pdframe),
                              columns=pdframe.columns)
        return answer

def min_max_scaler(X):
    """
    Min Max scaler for any dataframe.
    """
    scaler = MinMaxScaler()
    scaler.fit_transform(X.dropna())
    X_ = (X - scaler.data_min_)/(scaler.data_max_ - scaler.data_min_)
    return X_

def standard_scaler(pdataframe, dropna=True):
    """
    Convenience method for performing fit_transform on given data.
        
    Parameters:
        pdataframe (pandas.Dataframe): Input pandas Dataframe.
        dropna (boolean): If True, dropna will be called on \
            pdataframe first.

        Raises:
            A new pandas Dataframe that has been scaled.
    """
    return StandardScaler().forward_transform(pdataframe, dropna)

if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.randint(100, size=(3,2)), dtype=np.float64)
    sc = StandardScaler()
    print(df)
    forward_transformed= sc.forward_transform(df)
    print(forward_transformed)
    print(sc.reverse_transform(forward_transformed))




