# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import numpy as np
from copy import deepcopy
from sklearn.base import BaseEstimator


class ModelTree(BaseEstimator):
    """
    base_model : this can be linear regression model
    max_depth :
    min_samples_leaf :
    search_type :
    loss_criteria :
    """

    def __init__(
        self,
        base_model,
        max_depth=5,
        min_samples_leaf=10,
        search_type="greedy",
        loss_criteria="mse",
        n_search_grid=100,
    ):

        self.base_model = base_model
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.search_type = search_type
        self.n_search_grid = n_search_grid
        self.loss_criteria = loss_criteria
        self.tree_ = None

    def fit(self, X, y):
        """
        Supervised fitting a model
        """

        # copy the parameters from the object class
        model = self.base_model
        min_samples_leaf = self.min_samples_leaf
        max_depth = self.max_depth
        search_type = self.search_type
        n_search_grid = self.n_search_grid
        loss_criteria = self.loss_criteria

        """
        Internal function to build tree on given X and y
        """

        def _build_tree(X, y):
            # variable to store the global index
            global index_node_global

            # create one node in a tree
            def _create_node(X, y, depth, container):
                """
                X :
                y :
                depth :
                container : dictionary to store common variables
                """

                # call another fit_model function
                loss_node, model_node = _fit_model(X, y, model, loss_criteria)
                node = {
                    "name": "node",
                    "index": container["index_node_global"],
                    "loss": loss_node,
                    "model": model_node,
                    "data": (X, y),
                    "n_samples": len(X),
                    "j_feature": None,
                    "threshold": None,
                    "children": {"left": None, "right": None},
                    "depth": depth,
                }
                container["index_node_global"] += 1
                return node

            # Recursively split node + traverse node until a terminal node is reached
            def _split_traverse_node(node, container):
                # Perform split and collect result
                result = _splitter(
                    node,
                    model,
                    max_depth=max_depth,
                    min_samples_leaf=min_samples_leaf,
                    search_type=search_type,
                    n_search_grid=n_search_grid,
                    loss_criteria=loss_criteria,
                )

                # Return terminal node if split is not advised
                if not result["did_split"]:
                    return

                # Update node information based on splitting result
                node["j_feature"] = result["j_feature"]
                node["threshold"] = result["threshold"]
                del node["data"]  # delete node stored data

                # Extract splitting results
                (X_left, y_left), (X_right, y_right) = result["data"]
                model_left, model_right = result["models"]

                # Create children nodes
                node["children"]["left"] = _create_node(
                    X_left, y_left, node["depth"] + 1, container
                )
                node["children"]["right"] = _create_node(
                    X_right, y_right, node["depth"] + 1, container
                )
                node["children"]["left"]["model"] = model_left
                node["children"]["right"]["model"] = model_right

                # Split nodes
                _split_traverse_node(node["children"]["left"], container)
                _split_traverse_node(node["children"]["right"], container)

            container = {"index_node_global": 0}  # mutatable container
            root = _create_node(X, y, 0, container)  # depth 0 root node
            _split_traverse_node(root, container)  # split and traverse root node

            return root

        """
        Call internal function
        """
        # Construct tree
        self.tree_ = _build_tree(X, y)

    def predict(self, X):
        if self.tree_ is None:
            raise ValueError("tree is None.")

        def _predict(node, x):
            no_children = (
                node["children"]["left"] is None and node["children"]["right"] is None
            )
            if no_children:
                y_pred_x = node["model"].predict([x])[0]
                return y_pred_x
            else:
                if x[node["j_feature"]] <= node["threshold"]:  # x[j] < threshold
                    return _predict(node["children"]["left"], x)
                else:  # x[j] > threshold
                    return _predict(node["children"]["right"], x)

        y_pred = np.array([_predict(self.tree_, x) for x in X])
        return y_pred

    def explain(self, X, header):
        if self.tree_ is None:
            raise ValueError("tree is None.")

        def _explain(node, x, explanation):
            no_children = (
                node["children"]["left"] is None and node["children"]["right"] is None
            )
            if no_children:
                return explanation
            else:
                if x[node["j_feature"]] <= node["threshold"]:  # x[j] < threshold
                    explanation.append(
                        "{} = {:.6f} <= {:.6f}".format(
                            header[node["j_feature"]],
                            x[node["j_feature"]],
                            node["threshold"],
                        )
                    )
                    return _explain(node["children"]["left"], x, explanation)
                else:  # x[j] > threshold
                    explanation.append(
                        "{} = {:.6f} > {:.6f}".format(
                            header[node["j_feature"]],
                            x[node["j_feature"]],
                            node["threshold"],
                        )
                    )
                    return _explain(node["children"]["right"], x, explanation)

        explanations = [_explain(self.tree_, x, []) for x in X]
        return explanations


def _splitter(
    node,
    model,
    max_depth=5,
    min_samples_leaf=10,
    search_type="greedy",
    n_search_grid=100,
    loss_criteria="mse",
):
    # Extract data
    X, y = node["data"]
    depth = node["depth"]
    N, d = X.shape

    # Find feature splits that might improve loss
    did_split = False
    loss_best = node["loss"]
    data_best = None
    models_best = None
    j_feature_best = None
    threshold_best = None

    # Perform threshold split search only if node has not hit max depth
    if (depth >= 0) and (depth < max_depth):

        for j_feature in range(d):

            # If using adaptive search type, decide on one to use
            search_type_use = search_type
            if search_type == "adaptive":
                if N > n_search_grid:
                    search_type_use = "grid"
                else:
                    search_type_use = "greedy"

            # Use decided search type and generate threshold search list (j_feature)
            threshold_search = []
            if search_type_use == "greedy":
                # this can be optimized by removing duplicate entries
                for i in range(N):
                    threshold_search.append(X[i, j_feature])
            elif search_type_use == "grid":
                x_min, x_max = np.min(X[:, j_feature]), np.max(X[:, j_feature])
                dx = (x_max - x_min) / n_search_grid
                for i in range(n_search_grid + 1):
                    threshold_search.append(x_min + i * dx)
            else:
                raise Exception(
                    "err: invalid search_type = {} given!".format(search_type)
                )

            # Perform threshold split search on j_feature
            for threshold in threshold_search:

                # Split data based on threshold
                (X_left, y_left), (X_right, y_right) = _split_data(
                    j_feature, threshold, X, y
                )
                N_left, N_right = len(X_left), len(X_right)

                # Splitting conditions
                split_conditions = [
                    N_left >= min_samples_leaf,
                    N_right >= min_samples_leaf,
                ]

                # Do not attempt to split if split conditions not satisfied
                if not all(split_conditions):
                    continue

                # Compute weight loss function
                loss_left, model_left = _fit_model(X_left, y_left, model, loss_criteria)
                loss_right, model_right = _fit_model(
                    X_right, y_right, model, loss_criteria
                )
                loss_split = (N_left * loss_left + N_right * loss_right) / N

                # Update best parameters if loss is lower
                if loss_split < loss_best:
                    did_split = True
                    loss_best = loss_split
                    models_best = [model_left, model_right]
                    data_best = [(X_left, y_left), (X_right, y_right)]
                    j_feature_best = j_feature
                    threshold_best = threshold

    # Return the best result
    result = {
        "did_split": did_split,
        "loss": loss_best,
        "models": models_best,
        "data": data_best,
        "j_feature": j_feature_best,
        "threshold": threshold_best,
        "N": N,
    }

    return result


def _calculate_loss(X, y, y_pred, loss_criteria):
    if loss_criteria == "mse":
        from sklearn.metrics import mean_squared_error

        return mean_squared_error(y, y_pred)
    elif loss_criteria == "gini":
        return _gini_impurity(y)
    else:
        raise Exception("Incorrect loss function")


def _gini_impurity(y):
    p2 = 0.0
    y_classes = list(set(y))
    for c in y_classes:
        p2 += (np.sum(y == c) / len(y)) ** 2
    loss = 1.0 - p2
    return loss


def _fit_model(X, y, model, loss_criteria):
    model_copy = deepcopy(model)  # must deepcopy the model!
    model_copy.fit(X, y)
    y_pred = model_copy.predict(X)
    loss = _calculate_loss(X, y, y_pred, loss_criteria)
    if loss < 0.0:
        raise ValueError("loss is less than 0.")
    return loss, model_copy


def _split_data(j_feature, threshold, X, y):
    idx_left = np.where(X[:, j_feature] <= threshold)[0]
    idx_right = np.delete(np.arange(0, len(X)), idx_left)
    if len(idx_left) + len(idx_right) != len(X):
        raise ValueError("Error when splitting data.")
    return (X[idx_left], y[idx_left]), (X[idx_right], y[idx_right])
