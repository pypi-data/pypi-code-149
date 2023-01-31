# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: scorecard
   :synopsis: Scorecard based Optimized decision tree.

.. moduleauthor:: SROM Team
"""
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin


class Scorecard(BaseEstimator, ClassifierMixin):
    """
    A classifier to Sets up the IP model to solve for a scorecard and then solves it.
    """

    def __init__(self, M=2, K=3, C=1, recall_constraint=False, recall_frac=0.95):
        """
        Parameters:
            M (Integer, Optional) : The minimum score required to predict a 1 label.
            C (Integer, Optional, default 1) : Weight on negative-class examples \
                    (set less than 1 to emphasize positive-class examples).
            K (Integer, Optional) : The total l1 norm of the learned hyperplane.
            recall_constraint (Boolean, Optional, default False) : An indicator to specify whether \
                    to include a recall constraint (see writeup).
            recall_frac (Float, default = .95) if recall_constraint=True, the minimum recall required \
                    by the solution on the training set
        """
        self.M = M
        self.C = C
        self.K = K
        self.recall_constraint = recall_constraint
        self.recall_frac = recall_frac

    def _build_card(self, X, y):
        """
            Method to build the card.
        """
        M = self.M
        K = self.K
        C = self.C
        recall_constraint = self.recall_constraint
        recall_frac = self.recall_frac

        try:
            import cplex
        except ImportError:
            raise Exception("Please install cplex dependency")
        p = cplex.Cplex()
        p.objective.set_sense(p.objective.sense.maximize)

        num_samples = len(X)
        num_features = len(X[0])

        # establish variables
        names = []
        for j in range(num_features):
            name = "z_" + repr(j)
            names.append(name)
        z_ = num_features

        for i in range(num_samples):
            name = "c_" + repr(i)
            names.append(name)
        zc_ = z_ + num_samples

        A = np.zeros((num_samples + 2, zc_))
        rhs = []
        ineq = ""
        constraint_cnt = 0
        cnames = []

        for j in range(num_features):
            A[constraint_cnt, j] = 1
        rhs.append(float(K))
        ineq = ineq + "L"
        constraint_cnt += 1
        cname = "SumToK"
        cnames.append(cname)

        eps = 1e-3

        for i in range(num_samples):
            if y[i] == 1:
                A[constraint_cnt, :z_] = X[i]
                A[constraint_cnt, z_ + i] = -M
                rhs.append(0.0)
                ineq = ineq + "G"
                constraint_cnt += 1
                cname = "Sample_" + repr(i)
                cnames.append(cname)

            else:
                A[constraint_cnt, :z_] = X[i]
                A[constraint_cnt, z_ + i] = K - M + 1
                ineq = ineq + "L"
                rhs.append(float(K))
                constraint_cnt += 1
                cname = "Sample_" + repr(i)
                cnames.append(cname)
        if recall_constraint:
            num_pos = np.count_nonzero(y)
            for i in range(num_samples):
                if y[i] == 1:
                    A[constraint_cnt, z_ + i] = 1
            ineq = ineq + "G"
            rhs.append(np.ceil(recall_frac * num_pos))
            constraint_cnt += 1
            cname = "RecallConstraint"
            cnames.append(cname)

        num_rows = constraint_cnt
        num_cols = zc_

        indices = [
            [i for i in range(num_rows) if A[i, j] != 0] for j in range(num_cols)
        ]
        values = [
            [A[i, j] for i in range(num_rows) if A[i, j] != 0] for j in range(num_cols)
        ]
        cols = [[indices[i], values[i]] for i in range(num_cols)]

        rhs = np.array(rhs)
        senses = ineq

        # objective
        if len(np.shape(C)) == 0:
            obj = np.zeros(num_cols)
            for i in range(num_samples):
                if y[i] == 0:
                    obj[z_ + i] = C
                else:
                    obj[z_ + i] = 1
        elif len(np.shape(C)) == 1:
            obj = np.zeros(num_cols)
            obj[z_:] = C
        # types
        types = num_cols * "I"

        lb = np.zeros(num_cols)
        ub = np.ones(num_cols)
        ub[:z_] = K * np.ones(num_features)

        p.linear_constraints.add(rhs=rhs, senses=senses)
        p.linear_constraints.set_names(zip(range(num_rows), cnames))
        p.variables.add(obj=obj, lb=lb, ub=ub, columns=cols, types=types, names=names)

        p.write("dnf.lp")
        p.solve()
        sol = p.solution
        trial = sol.get_objective_value()
        print("Solution value = ", trial)

        hyperplane = np.zeros(num_features)

        for j in range(num_features):
            val = sol.get_values(j)
            hyperplane[j] = val
        return hyperplane

    def fit(self, X, y):
        """
        Predict vote.

        Parameters:
            X (pandas dataframe/matrix, required): Input Data (Ony limited to Binary Data).
            y (pandas dataframe, required): Label for Input Data.

        Returns:
            <description>
        """
        self.hyperplane = self._build_card(X, y)
        return self

    def _test_card(self, I):
        """
            Method to test the card.
        """
        num_samples = len(I)
        assigned = np.zeros(num_samples)

        for i in range(num_samples):
            tmp_sum = np.dot(self.hyperplane, I[i])
            if tmp_sum >= self.M:
                assigned[i] = 1

        return assigned

    def predict(self, X):
        """
        Predict.

        Parameters:
            X (pandas dataframe, required): pandas dataframe.

        Returns:
            <description>
        """
        return self._test_card(X)
