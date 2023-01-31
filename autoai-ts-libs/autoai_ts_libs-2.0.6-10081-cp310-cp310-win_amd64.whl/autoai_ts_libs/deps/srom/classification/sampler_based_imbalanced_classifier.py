# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: sampler_based_imbalanced_classifier
   :synopsis: Contains ImbalancedClassifier class.

.. moduleauthor:: SROM Team
"""
import numpy as np
import pandas as pd
import collections
from sklearn.base import BaseEstimator, ClassifierMixin, clone
from sklearn.ensemble import RandomForestClassifier
from autoai_ts_libs.deps.srom.data_sampling.unsupervised.random_sampler import (
    Random_MajorityClass_DownSampler,
)


class ImbalancedClassifier(BaseEstimator, ClassifierMixin):
    """
    A classifier to deal with unbalanced dataset. It support two classes only. \
    We have assumed minority sample have class label 1.
    """

    def __init__(
        self,
        base_sampler=Random_MajorityClass_DownSampler(),
        base_model=RandomForestClassifier(),
        num_iteration=10,
        voting="soft",
        save_sampler=False,
    ):
        """
        Parameters:
            base_sampler (Object, required): A sampler we want to use to generate data samples.
            base_model (Object, required): A model we want to train on each partition of the data.
            num_iteration (Integer, required): Number of base_models to include in the ensemble.
            voting (String, 'soft' or 'hard', default 'soft'): In 'soft' mode, overall vote is based on the
                average probability amoung the members of the ensemble. For 'hard' overall vote is based on
                the majority vote of the members of the ensemble. Note: the predict_proba method is only
                available in the 'soft' mode.
            save_sampler (Boolean, optional, default False): If true, trained sampler (if trained) is saved \
                when instances of the class are saved. Otherwise, untrained sampler is saved.
        """
        self.base_sampler = base_sampler
        self.base_model = base_model
        self.num_iteration = num_iteration
        self.voting = voting
        self.clfs = []
        self._num_class = 0
        self.classes_ = None

        self._is_base_sampler_trained = False
        self.save_sampler = save_sampler

    def __getstate__(self):
        """
            Method to get the state.
        """
        if self.save_sampler:
            return self.__dict__
        else:
            return {
                "_is_base_sampler_trained": False,
                "_num_class": self._num_class,
                "classes_": self.classes_,
                "base_model": self.base_model,
                "base_sampler": clone(self.base_sampler),
                "clfs": self.clfs,
                "num_iteration": self.num_iteration,
                "voting": self.voting,
                "save_sampler": self.save_sampler,
            }
            # 'classes_': self.classes_,

    def set_params(self, **kwarg):
        """
        Used to set params.
        """
        if "base_sampler" in kwarg:
            self.base_sampler = kwarg["base_sampler"]
        if "base_model" in kwarg:
            self.base_model = kwarg["base_model"]
        if "num_iteration" in kwarg:
            self.num_iteration = kwarg["num_iteration"]

        model_param = {}
        for d_item in kwarg:
            if "base_sampler__" in d_item:
                model_param[d_item.split("base_sampler__")[1]] = kwarg[d_item]
        if len(model_param) > 0:
            self.base_sampler.set_params(**model_param)

        model_param = {}
        for d_item in kwarg:
            if "base_model__" in d_item:
                model_param[d_item.split("base_model__")[1]] = kwarg[d_item]
        if len(model_param) > 0:
            self.base_model.set_params(**model_param)
        return self

    def get_params(self, deep=False):
        """
        Used to get params.
        """
        model_param = {}
        model_param["base_sampler"] = self.base_sampler
        model_param["base_model"] = self.base_model
        model_param["num_iteration"] = self.num_iteration

        if deep:
            for item in self.base_sampler.get_params().keys():
                model_param["base_sampler__" + item] = self.base_sampler.get_params()[
                    item
                ]
            for item in self.base_model.get_params().keys():
                model_param["base_model__" + item] = self.base_model.get_params()[item]
        return model_param

    def __get_samples(self, X, y):
        """
        Generate the samples for each iteration.

        Parameters:
            X (numpy array, required): numpy array.
            y (numpy array, required): numpy array.

        Returns:
            Balanced Samples : X and y Data.
        """
        if self.base_sampler is None:
            return X, y
        if self._is_base_sampler_trained and hasattr(
            self.base_sampler, "generate_samples"
        ):
            return self.base_sampler.generate_samples()
        self._is_base_sampler_trained = True
        return self.base_sampler.fit_sample(X, y)

    def fit(self, X, y):
        """
        Fits base_model, num_iteration times.

        Parameters:
            X (pandas dataframe or numpy array, required): pandas dataframe or numpy array.
            y (pandas dataframe or numpy array, required): pandas dataframe or numpy array.
        """
        self.clfs = []
        self._is_base_sampler_trained = False

        if self.voting not in ("soft", "hard"):
            raise ValueError(
                "Voting must be 'soft' or 'hard'; got (voting=%r)" % self.voting
            )

        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, pd.Series):
            y = np.array(y)

        self._num_class = len(set(y))
        # self.classes_ = np.unique(y)
        for dummy_i in range(self.num_iteration):
            cur_clf = clone(self.base_model)
            X_sample, y_sample = self.__get_samples(X, y)

            # check consistency among samplers with # of classes in original data
            if len(set(y_sample)) != self._num_class:
                raise RuntimeError(
                    "Mismatich in the number of classes in sampled result."
                )

            self.clfs.append(cur_clf.fit(X_sample, y_sample))

        if not hasattr(self.clfs[0], "classes_"):
            raise RuntimeError("Underlying classifier does not have class labels")
        self.classes_ = self.clfs[0].classes_

        return self

    def _predict_vote(self, X):
        """
        Predict vote.

        Parameters:
            X (pandas dataframe or numpy array, required): pandas dataframe or numpy array.

        Returns:
            (numpy array): Predicted votes.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        Y = np.empty([X.shape[0], len(self.clfs)])
        for i, clf in enumerate(self.clfs):
            Y[:, i] = clf.predict(X)
        y_sum = []
        for item in Y:
            y_sum.append(int(collections.Counter(item).most_common(1)[0][0]))
        y_sum = np.array(y_sum)
        return y_sum

    def _predict_avg_proab(self, X):
        """
        Predicts average probability.

        Parameters:
            X (pandas dataframe or numpy array, required): pandas dataframe or numpy array.

        Returns:
            (numpy array): Average probability.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        Y = np.zeros([X.shape[0], self._num_class])
        for _, clf in enumerate(self.clfs):
            output_x = clf.predict_proba(X)
            Y = Y + output_x
        Y = Y / (self.num_iteration * 1.0)
        return Y

    def predict(self, X):
        """
        Predict.

        Parameters:
            X (pandas dataframe or numpy array, required): pandas dataframe or numpy array.

        Returns:
            (numpy array): Predicted labels.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        if self.voting == "hard":
            vote = self._predict_vote(X)
        else:
            classes = self.classes_
            vote = classes[np.argmax(self.predict_proba(X), axis=1)]
        return vote

    def predict_proba(self, X):
        """
        Predict probability.

        Parameters:
            X (pandas dataframe or numpy array, required): pandas dataframe or numpy array.
            
        Returns:
            (numpy array): Predicted probabilities.
        """

        if self.voting == "hard":
            raise AttributeError(
                "predict_proba is not available when" " voting=%r" % self.voting
            )

        if isinstance(X, pd.DataFrame):
            X = X.values

        return self._predict_avg_proab(X)
