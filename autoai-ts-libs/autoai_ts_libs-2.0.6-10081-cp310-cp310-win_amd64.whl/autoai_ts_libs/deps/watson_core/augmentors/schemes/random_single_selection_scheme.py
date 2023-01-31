# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Scheme for randomly picking 1 augmentor from a list per object.
"""
import random

from autoai_ts_libs.deps.watson_core.augmentors.schemes import SchemeBase
from autoai_ts_libs.deps.watson_core.toolkit import alog
from autoai_ts_libs.deps.watson_core.toolkit.errors import error_handler

log = alog.use_channel("RSING_AUG_SCHEME")
error = error_handler.get(log)


class RandomSingleSelectionScheme(SchemeBase):
    def __init__(self, selection_probs, augmentors, random_seed=1001):
        """Create a merging augmentor scheme which randomly applies one of many encapsulated
        augmentors when executed.

        Args:
            selection_probs: list(int|float) | tuple(int|float)
                Probability values for applying each augmentor (must sum to 1).
            augmentors: list(AugmentorBase) | tuple(AugmentorBase)
                Augmentors to be applied (in same order as selection_probs).
            random_seed: int
                Random seed for controlling shuffling behavior.
        """
        super().__init__(True, augmentors, random_seed)
        error.type_check("<COR26721310E>", list, tuple, selection_probs=selection_probs)
        error.type_check_all(
            "<COR89551931E>", int, float, selection_probs=selection_probs
        )
        error.value_check(
            "<COR22821754E>",
            len(selection_probs) == len(augmentors),
            "Number of selection probabilties must match the number of augmentors",
        )
        error.value_check(
            "<COR82891072E>",
            all(0 <= prob <= 1 for prob in selection_probs),
            "Selection probabilities must be in the range [0, 1]",
        )
        error.value_check(
            "<COR00872610E>",
            sum(selection_probs) == 1,
            "Selection probabilities must sum up to one to create a single selection scheme",
        )
        self._selection_probs = selection_probs

    def _execute(self, obj):
        """Execute the merged scheme by picking one random augmentor and applying it.

        Args:
            obj: str | watson_core.data_model.DataBase
                Object to be augmented.
        Returns:
            str | watson_core.data_model.DataBase
                Augmented object of same type as input obj.
        """
        aug = random.choices(self._augmentors, weights=self._selection_probs)[0]
        return aug.augment(obj)
