"""Helper functions to construct and use randomized classifiers.
"""
import logging
from abc import ABC, abstractmethod

import numpy as np
from scipy.spatial import ConvexHull


class Classifier(ABC):
    @abstractmethod
    def __call__(self, X: np.ndarray, group: np.ndarray = None) -> np.ndarray:
        """Return predicted class, Y, for the given input features, X.
        """
        raise NotImplementedError


class BinaryClassifier(Classifier):
    """Constructs a deterministic binary classifier, by thresholding a
    real-valued score predictor.
    """

    def __init__(
            self,
            score_predictor: callable,
            threshold: float,
        ):
        """Constructs a deterministic binary classifier from the given
        real-valued score predictor and a threshold \in {0, 1}.
        """
        self.score_predictor = score_predictor
        self.threshold = threshold

    def __call__(self, X: np.ndarray, group: np.ndarray = None) -> np.ndarray:
        """Computes predictions for the given samples, X.

        Parameters
        ----------
        X : np.ndarray
            The input samples, in shape (num_samples, num_features).
        group : None, optional
            None. This argument will be ignored by this classifier as it does 
            not consider sensitive attributes.

        Returns
        -------
        y_pred_binary : np.ndarray[int]
            The predicted class for each input sample.
        """
        return (self.score_predictor(X) >= self.threshold).astype(int)


# TODO - WARNING - THERE'S SOME BUG IN THIS CLASSIFIER!
class BinaryClassifierAtROCDiagonal(Classifier):
    """A dummy classifier whose predictions have no correlation with the input
    features, but achieves whichever target FPR or TPR you want (on ROC diag.)
    """

    def __init__(
            self,
            target_fpr: float = None,
            target_tpr: float = None,
            seed: int = 42,
        ):
        err_msg = (
            f"Must provide exactly one of 'target_fpr' or 'target_tpr', "
            f"got target_fpr={target_fpr}, target_tpr={target_tpr}."
        )
        if target_fpr is not None and target_tpr is not None:
            raise ValueError(err_msg)

        # Provided FPR
        if target_fpr is not None:
            self.target_fpr = target_fpr
            self.target_tpr = target_fpr

        # Provided TPR
        elif target_tpr is not None:
            self.target_tpr = target_tpr
            self.target_fpr = target_tpr
        
        # Provided neither!
        else:
            raise ValueError(err_msg)
        
        # Initiate random number generator
        self.rng = np.random.default_rng(seed)

    def __call__(self, X: np.ndarray, group: np.ndarray = None) -> np.ndarray:
        return (self.rng.random(size=len(X)) >= (1 - self.target_fpr)).astype(int)


class EnsembleGroupwiseClassifiers(Classifier):
    """Constructs a classifier from a set of group-specific classifiers.
    """

    def __init__(self, group_to_clf: dict[int | str, callable]):
        """Constructs a classifier from a set of group-specific classifiers.

        Must be provided exactly one classifier per unique group value.

        Parameters
        ----------
        group_to_clf : dict[int  |  str, callable]
            A mapping of group value to the classifier that should handle 
            predictions for that specific group.
        """
        self.group_to_clf = group_to_clf

    def __call__(self, X: np.ndarray, group: np.ndarray) -> np.ndarray:
        """Compute predictions for the given input samples X, given their
        sensitive attributes, group.

        Parameters
        ----------
        X : np.ndarray
            Input samples, with shape (num_samples, num_features).
        group : np.ndarray, optional
            The sensitive attribute value for each input sample.

        Returns
        -------
        y_pred : np.ndarray
            The predictions, where the prediction for each sample is handed off
            to a group-specific classifier for that sample.
        """
        assert len(X) == len(group)
        num_samples = len(X)

        # Array to store predictions
        y_pred = np.zeros(num_samples)

        # Filter to keep track of all samples that received a prediction
        cumulative_filter = np.zeros(num_samples).astype(bool)

        for group_value, group_clf in self.group_to_clf.items():
            group_filter = (group == group_value)
            y_pred[group_filter] = group_clf(X[group_filter])
            cumulative_filter |= group_filter

        assert np.sum(cumulative_filter) == num_samples, (
            f"Computed group-wise predictions for {np.sum(cumulative_filter)} "
            f"samples, but got {num_samples} input samples."
        )

        return y_pred


class RandomizedClassifier(Classifier):
    """Constructs a randomized classifier from the given  classifiers and 
    their probabilities.
    """

    def __init__(
            self,
            classifiers: list[Classifier],
            probabilities: list[float],
            seed: int = 42,
        ):
        """Constructs a randomized classifier from the given  classifiers and 
        their probabilities.
        
        This classifier will compute predictions for the whole input dataset at 
        once, which will in general be faster for larger inputs (when compared 
        to predicting each sample separately).

        Parameters
        ----------
        classifiers : list[callable]
            A list of classifiers
        probabilities : list[float]
            A list of probabilities for each given classifier, where 
            probabilities[idx] is the probability of using the prediction from 
            classifiers[idx].
        seed : int, optional
            A random seed, by default 42.

        Returns
        -------
        callable
            The corresponding randomized classifier.
        """
        assert len(classifiers) == len(probabilities)
        self.classifiers = classifiers
        self.probabilities = probabilities
        self.rng = np.random.default_rng(seed)
    
    def __call__(self, X: np.ndarray, group: np.ndarray = None) -> int:
        # Assign each sample to a classifier
        clf_idx = self.rng.choice(
            np.arange(len(self.classifiers)),       # possible choices
            size=len(X),                            # size of output array
            p=self.probabilities,                   # prob. of each choice
        )
        
        # Run predictions for all classifiers on all samples
        y_pred_choices = [clf(X) for clf in self.classifiers]
        # TODO:
        # we could actually just run the classifier for the samples that get
        # matched with it... similar to the EnsembleGroupwiseClassifiers call
        # method.
        
        return np.choose(clf_idx, y_pred_choices)


    @staticmethod
    def find_weights_given_two_points(
            point_A: np.ndarray,
            point_B: np.ndarray,
            target_point: np.ndarray,
        ):
        """Given two ROC points corresponding to existing binary classifiers,
        find the weights that result in a classifier whose ROC point is target_point.
        
        May need to interpolate the two given points with a third point corresponding
        to a random classifier (random uniform distribution with different thresholds).
        
        Returns
        -------
        tuple[np.ndarray, np.ndarray]
            Returns a tuple of numpy arrays (Ws, Ps), such that Ws @ Ps == target_point.
            The 1st array, Ws, corresponds to the weights of each point in the 2nd array, Ps.
        """
        # Check if the target point is actually point A or B
        if all(np.isclose(point_A, target_point)):
            return np.array([1]), np.expand_dims(point_A, axis=0)

        if all(np.isclose(point_B, target_point)):
            return np.array([1]), np.expand_dims(point_B, axis=0)
        
        # If not, we'll have to triangulate the target using A and B
        point_A_fpr, point_A_tpr = point_A
        point_B_fpr, point_B_tpr = point_B
        target_fpr, target_tpr = target_point
        assert point_A_fpr <= target_fpr <= point_B_fpr, (
            f"FALSE: {point_A_fpr} <= {target_fpr} <= {point_B_fpr}"
        )

        # Calculate weights for points A and B
        weight_A = (target_fpr - point_B_fpr) / (point_A_fpr - point_B_fpr)

        # Result of projecting target point P directly UPWARDS towards the AB line
        weights_AB = np.array([weight_A, 1 - weight_A])
        point_P_upwards = weights_AB @ np.vstack((point_A, point_B))
        assert np.isclose(point_P_upwards[0], target_fpr)
        
        # Check if the target point lies in the AB line (and return if so)
        if all(np.isclose(point_P_upwards, target_point)):
            return weights_AB, np.vstack((point_A, point_B))

        # Result of projecting target point P directly DOWNWARDS towards the diagonal tpr==fpr
        point_P_downwards = np.array([target_fpr, target_fpr])

        # Calculate weights for P upwards and P downwards
        weight_P_upwards = (target_tpr - point_P_downwards[1]) / (point_P_upwards[1] - point_P_downwards[1])

        # Sanity check...
        all_points = np.vstack((point_A, point_B, point_P_downwards))
        all_weights = np.hstack((weight_P_upwards * weights_AB, 1 - weight_P_upwards))

        assert np.isclose(all_weights.sum(), 1)
        # assert all(all_weights <= 1) and all(all_weights >= 0)
        assert all(np.isclose(target_point, all_weights @ all_points))

        return all_weights, all_points

    @staticmethod
    def construct_at_target_ROC(
            predictor: callable,
            roc_curve_data: tuple,
            target_roc_point: np.ndarray,
            seed: int = 42,
        ) -> "RandomizedClassifier":
        """Constructs a randomized classifier in the interior of the
        convex hull of the classifier's ROC curve, at a given target
        ROC point.
        
        Parameters
        ----------
        predictor : callable
            A predictor that outputs real-valued scores in range [0; 1].
        roc_curve_data : tuple[np.array...]
            The ROC curve of the given classifier, as a tuple of
            (FPR values; TPR values; threshold values).
        target_roc_point : np.ndarray
            The target ROC point in (FPR, TPR).
        
        Returns
        -------
        rand_clf : callable
            A (randomized) binary classifier whose expected FPR and TPR
            corresponds to the given target ROC point.
        """
        # Unpack useful constants
        target_fpr, target_tpr = target_roc_point
        fpr, tpr, thrs = roc_curve_data

        # Compute hull of ROC curve
        roc_curve_points = np.stack((fpr, tpr), axis=1)
        hull = ConvexHull(roc_curve_points)

        # Filter out ROC points in the interior of the convex hull and other suboptimal points
        points_above_diagonal = np.argwhere(tpr >= fpr).ravel()
        useful_points_idx = np.array(sorted(set(hull.vertices) & set(points_above_diagonal)))

        fpr = fpr[useful_points_idx]
        tpr = tpr[useful_points_idx]
        thrs = thrs[useful_points_idx]

        # Find points A and B to construct the randomized classifier from
        # > point A is the last point with FPR smaller or equal to the target
        point_A_idx = 0
        if target_fpr > 0:
            point_A_idx = max(np.argwhere(fpr <= target_fpr).ravel())

        # > point B is the first point with FPR larger than the target
        point_B_idx = min(point_A_idx + 1, len(thrs) - 1)

        weights, points = RandomizedClassifier.find_weights_given_two_points(
            point_A=roc_curve_points[useful_points_idx][point_A_idx],
            point_B=roc_curve_points[useful_points_idx][point_B_idx],
            target_point=target_roc_point,
        )

        # Instantiate classifiers for points A and B
        clf_a = BinaryClassifier(predictor, threshold=thrs[point_A_idx])
        clf_b = BinaryClassifier(predictor, threshold=thrs[point_B_idx])

        # Instatiate a randomized classifier if needed (at the diagonal)
        clf_rand = None
        if len(weights) > 2:
            fpr_rand, tpr_rand = points[2]
            assert fpr_rand == tpr_rand
            # >>> BUG this would be better but for some reason it doesn't work!
            # rng = np.random.default_rng(42)
            # clf_rand = lambda X: (rng.random(size=len(X)) >= (1 - fpr_rand)).astype(int)
            # # or...
            # clf_rand = BinaryClassifierAtROCDiagonal(target_fpr=fpr_rand)   # BUG
            # <<<
            clf_rand = lambda X: (np.random.random(size=len(X)) >= (1 - fpr_rand)).astype(int)

        # Create a weighted ensemble from all classifiers
        rand_clf = RandomizedClassifier(
            classifiers=[clf_a, clf_b, clf_rand][: len(weights)],
            probabilities=weights,
            seed=seed,
        )

        return rand_clf

    @staticmethod
    def find_points_for_target_ROC(roc_curve_data, target_roc_point):
        """Retrieves a set of realizable points (and respective weights) in the
        provided ROC curve that can be used to realize any target ROC in the
        interior of the ROC curve.

        NOTE: this method is a bit redundant -- has functionality in common with
        RandomizedClassifier.construct_at_target_ROC()
        """
        # Unpack useful constants
        target_fpr, target_tpr = target_roc_point
        fpr, tpr, thrs = roc_curve_data

        # Compute hull of ROC curve
        roc_curve_points = np.stack((fpr, tpr), axis=1)
        hull = ConvexHull(roc_curve_points)

        # Filter out ROC points in the interior of the convex hull and other suboptimal points
        points_above_diagonal = np.argwhere(tpr >= fpr).ravel()
        useful_points_idx = np.array(sorted(set(hull.vertices) & set(points_above_diagonal)))

        fpr = fpr[useful_points_idx]
        tpr = tpr[useful_points_idx]
        thrs = thrs[useful_points_idx]

        # Find points A and B to construct the randomized classifier from
        # > point A is the last point with FPR smaller or equal to the target
        point_A_idx = max(np.argwhere(fpr <= target_fpr).ravel())
        # > point B is the first point with FPR larger than the target
        point_B_idx = point_A_idx + 1

        weights, points = RandomizedClassifier.find_weights_given_two_points(
            point_A=roc_curve_points[useful_points_idx][point_A_idx],
            point_B=roc_curve_points[useful_points_idx][point_B_idx],
            target_point=target_roc_point,
        )

        return weights, points
