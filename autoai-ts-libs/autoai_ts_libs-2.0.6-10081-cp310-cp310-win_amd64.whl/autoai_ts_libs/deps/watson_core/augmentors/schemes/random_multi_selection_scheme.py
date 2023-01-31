# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Scheme for randomly applying 1+ augmentors, where multiple augmentors may be applied.
"""
import random

from autoai_ts_libs.deps.watson_core.augmentors.schemes import SchemeBase
from autoai_ts_libs.deps.watson_core.toolkit import alog
from autoai_ts_libs.deps.watson_core.toolkit.errors import error_handler

log = alog.use_channel("RMULT_AUG_SCHEME")
error = error_handler.get(log)


class RandomMultiSelectionScheme(SchemeBase):
    def __init__(self, preserve_order, selection_probs, augmentors, random_seed=1001):
        """Create a merging augmentor scheme which allows for application of many augmentors
        simultaneously, each of which is controlled by an independent application probability.

        Args:
            preserve_order: bool
                Indicates whether or not the contained augmentors should always be considered in
                the order that they were provided when they are being applied.
            selection_probs: list(int|float) | tuple(int|float)
                Independent probability values for applying each augmentor.
            augmentors: list(AugmentorBase) | tuple(AugmentorBase)
                Augmentors to be applied (in same order as selection_probs).
            random_seed: int
                Random seed for controlling shuffling behavior.
        """
        super().__init__(preserve_order, augmentors, random_seed)
        error.type_check("<COR99517020E>", list, tuple, selection_probs=selection_probs)
        error.type_check_all(
            "<COR64536739E>", int, float, selection_probs=selection_probs
        )
        error.value_check(
            "<COR89794223E>",
            len(selection_probs) == len(augmentors),
            "Number of selection probabilties must match the number of augmentors",
        )
        error.value_check(
            "<COR74163144E>",
            all(0 <= prob <= 1 for prob in selection_probs),
            "Selection probabilities must be in the range [0, 1]",
        )
        self._selection_probs = selection_probs

    def _execute(self, obj):
        """Execute the merged scheme by sequentially applying augmentors (in a potentially
        shuffled ordering, based on the value of self.preserve_order).

        Args:
            obj: str | watson_core.data_model.DataBase
                Object to be augmented.
        Returns:
            str | watson_core.data_model.DataBase
                Augmented object of same type as input obj.
        """
        output_obj = obj
        for idx in self._current_order:
            selection_prob = self._selection_probs[idx]
            aug = self._augmentors[idx]
            if random.random() <= selection_prob:
                output_obj = aug.augment(output_obj)
        return output_obj
