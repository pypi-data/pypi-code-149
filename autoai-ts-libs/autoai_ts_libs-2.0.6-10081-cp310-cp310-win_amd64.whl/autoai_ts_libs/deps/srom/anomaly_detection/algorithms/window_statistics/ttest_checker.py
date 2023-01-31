# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: ttest_checker
   :synopsis: Contains TTestChecker class.

.. moduleauthor:: SROM Team
"""
from scipy.stats import ttest_ind
from sklearn.base import BaseEstimator, ClassifierMixin

class TTestChecker(BaseEstimator, ClassifierMixin):
    """
    An example of TTest based Window Comparison
    """

    def __init__(self, direction='both', threshold=0.05, axis=0, equal_var=True, nan_policy='omit'):
        """
        Initialization of the T Test checker.

        Paramters:
            threshold (float, optional): Threshold for checking using p-value. Value less than 1.
            direction ({â€˜positiveâ€™, â€˜negativeâ€™, â€˜bothâ€™}, optional): Defines which type of change \
                is considered as anomalous. 'positive' is default.
            axis (int or None, optional): Axis along which to compute test. \
                If None, compute over the whole arrays, a and b.
            equal_var (bool, optional): If True (default), perform a standard independent 2 sample \
                test that assumes equal population variances [1]. If False, perform Welchâ€™s t-test, \
                which does not assume equal population variance [2].
            nan_policy ({â€˜propagateâ€™, â€˜raiseâ€™, â€˜omitâ€™}, optional): Defines how to handle when input \
                contains nan. â€˜propagateâ€™ returns nan, â€˜raiseâ€™ throws an error, â€˜omitâ€™ performs the \
                calculations ignoring nan values. Default is â€˜omit'.
        """
        self.train_X = None
        self.threshold = threshold
        self.direction = direction
        self.axis = axis
        self.equal_var = equal_var
        self.nan_policy = nan_policy
        self.proc_p_value = None
        self.ttest = None
        self.p_value = None

    def set_threshold(self, threshold):
        """
        Setter function for threshold.
        """
        self.threshold = threshold

    def get_threshold(self):
        """
        Getter function for threshold.
        """
        return self.threshold

    def set_axis(self, axis):
        """
        Setter function for setting axis.
        """
        self.axis = axis

    def get_axis(self):
        """
        Getter function for setting axis.
        """
        return self.axis

    def set_equal_var(self, equal_var):
        """
        Setter function for 'equal_var' attribute in scipy ttests.
        """
        self.equal_var = equal_var

    def get_equal_var(self):
        """
        Getter function for 'equal_var' attribute in  scipy ttests.
        """
        return self.equal_var

    def set_nan_policy(self, nan_policy):
        """
        Setter function for Nan policies.
        """
        self.nan_policy = nan_policy

    def get_nan_policy(self):
        """
        Getter function for nan policy.
        """
        return self.nan_policy

    def apply_anomaly_direction(self):
        """
        Applies 'direction' to p values based on t-statistics. This \
        can be used to give anomalies in a particular direction only.
        """
        self.proc_p_value = self.p_value
        if self.direction == 'both':
            pass
        elif self.direction == 'positive' and self.ttest < 0:
            self.proc_p_value = -1
        elif self.direction == 'negative' and self.ttest > 0:
            self.proc_p_value = -1
        else:
            pass
        return self.proc_p_value

    def fit(self, X):
        """
        This should fit classifier for TTestChecker function.
        """
        # assert (type(self.a) == ), "intValue parameter must be integer"
        # assert (type(self.stringParam) == str), "stringValue parameter must be string"
        # assert (len(X) == 20), "X must be list with numerical values."

        self.train_X = X
        return self

    def predict(self, X):
        """
        Predict function for classifying anomaly as 1 or 0.
        """
        self.checker_score(X)
        tmp_p_value = self.apply_anomaly_direction()
        check = 0
        if abs(tmp_p_value) <= self.threshold:
            check = 1
        elif tmp_p_value == -1:
            check = -1
        else:
            pass
        return check

    def checker_score(self, X):
        """
        Generate raw checker score.
        """
        if self.train_X is None:
            raise RuntimeError("You must train checker before predicting data!")

        self.ttest, self.p_value = ttest_ind(self.train_X, X, self.axis,
                                             self.equal_var, self.nan_policy)
        return self.ttest

    def anomaly_score(self, X):
        """
        Return the anomaly value as a score.
        """
        return self.checker_score(X)

    def get_stats(self):
        """
        Getter function for statistics returned from t test function.
        """
        return {'ttest_score':self.ttest, 'p_value':self.p_value}
