"""
.. module:: augmentor
   :synopsis: Contains Base class.

.. moduleauthor:: SROM Team
"""

from abc import abstractmethod
from sklearn.base import BaseEstimator, TransformerMixin


class BaseAugmentor(BaseEstimator, TransformerMixin):
    """
    This is base class.
    """

    def fit(self, X, y=None):
        """"""
        return self

    @abstractmethod
    def transform(self, X):
        pass
