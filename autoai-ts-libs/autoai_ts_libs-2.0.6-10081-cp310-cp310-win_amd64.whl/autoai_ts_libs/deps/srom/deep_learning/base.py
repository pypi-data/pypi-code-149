# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: base
   :synopsis: base

.. moduleauthor:: SROM Team
"""

from abc import abstractmethod, ABC
import numpy as np
import pandas as pd

# write a base class that provide all the capability
class BaseAutoEncoderAnomalyDetector(ABC):
    """This is a base class to provide all the capability

    Args:
        ABC ([type]): [description]

    Returns:
        [type]: [description]
    """
    
    def predict(self, X, **kwargs):
        """
        Generate anomaly score - single score per record.

        Parameters:
            X : Pandas dataframe or numpy ndarray
            **kwargs : keyword arguments.
        Returns:
            tmp_score: len(X) scores.
        """
        tmp_score = self.anomaly_score(X, **kwargs)
        return tmp_score

    def anomaly_score(self, X, **kwargs):
        """
        Generate Anomaly Score.
        Parameters:
            X : Pandas dataframe or numpy ndarray.
            **kwargs : keyword arguments.
        """
        if self.model is None:
            raise Exception("Model is not trained")

        # each sample will be scored separately
        X = X.astype(np.float64)

        # get the projected data
        if isinstance(X, np.ndarray):
            data_n = pd.DataFrame(X)
        else:
            data_n = X

        data_n = data_n.astype("float32")
        data_out = self.model.predict(data_n.values)

        dist = np.zeros(len(data_n.values))
        for i, x in enumerate(data_n.values):
            dist[i] = np.linalg.norm(x - data_out[i])  # euclidean distance

        return dist

    def attribute_wise_anomaly_score(self, X, **kwargs):
        """
        Attribute wise anomaly score.
        Paramters:
            X: Testing set (Pandas dataframe or numpy ndarray).

        Returns:
            scores: Array of anomaly score, with size equal to X.shape.
        """

        if self.model is None:
            raise Exception("No train model provided")

        # each sample will be scored separately
        X = X.astype(np.float64)

        # get the projected data
        # get the projected data
        if isinstance(X, np.ndarray):
            data_n = pd.DataFrame(X)
        else:
            data_n = X
        data_n = data_n.astype("float32")

        scores = np.zeros([data_n.shape[0], data_n.shape[1]])
        scores[:] = np.NAN

        for i, x in enumerate(data_n.values):
            scores[i, :] = abs(self._compute_error_per_dim(x))

        return scores

    def _compute_error_per_dim(self, p):
        """
            Internal method to compute error per dim
        """
        p = np.array(p).reshape(1, self.input_dim)
        data_out = self.model.predict(p)
        return np.array(p - data_out)[0]

    def decision_function(self, X):
        """
        Predict raw anomaly score of X using the fitted detector.
        Paramters:
            X: (Pandas dataframe or numpy ndarray).
        """
        return self.anomaly_score(X)
