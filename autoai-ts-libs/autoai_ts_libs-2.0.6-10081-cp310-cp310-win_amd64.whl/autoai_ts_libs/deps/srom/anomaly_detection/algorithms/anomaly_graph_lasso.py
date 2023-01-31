# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: srom_graph_lasso
   :synopsis: srom_graph_lasso.
   
.. moduleauthor:: SROM Team
"""

import logging
from sklearn.covariance import GraphicalLasso as SKLGraphLasso
from sklearn.covariance import empirical_covariance, shrunk_covariance, graphical_lasso

#''' our fix to deal with singular value issue'''

LOGGER = logging.getLogger(__name__)

class AnomalyGraphLasso(SKLGraphLasso):
    """
    AnomalyGraphLasso
    """

    def fit(self, X):
        """
        Fit estimator

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features) \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.

        Returns:
            self: Trained instance of AnomalyGraphLasso.
        """
        try:
            super(AnomalyGraphLasso, self).fit(X)
        except FloatingPointError:
            emp_cov = empirical_covariance(X)
            shrinkage_th = 0.1
            shrunk_cov = None
            while shrinkage_th < 1:
                try:
                    shrunk_cov = shrunk_covariance(emp_cov, shrinkage=shrinkage_th)
                    tmp_result = graphical_lasso(shrunk_cov, alpha=self.alpha, return_n_iter=True)
                    self.covariance_ = tmp_result[0].copy()
                    self.precision_ = tmp_result[1].copy()
                    self.n_iter_ = tmp_result[2]
                    break
                except FloatingPointError:
                    shrinkage_th = shrinkage_th + 0.1
        except Exception as ex:
            LOGGER.exception(ex)
            raise Exception("Error while training AnomalyGraphLasso")

        return self
