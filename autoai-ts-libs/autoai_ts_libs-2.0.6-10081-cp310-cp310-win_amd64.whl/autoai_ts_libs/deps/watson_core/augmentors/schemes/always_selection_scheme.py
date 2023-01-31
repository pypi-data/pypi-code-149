# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Scheme for always selecting an augmentation behavior.
"""
from autoai_ts_libs.deps.watson_core.augmentors.schemes import SchemeBase


class AlwaysSelectionScheme(SchemeBase):
    def __init__(self, preserve_order, augmentors, random_seed=1001):
        """Create a merging augmentor scheme which always applies every contained augmentor.

        Args:
            preserve_order: bool
                Indicates whether or not the contained augmentors should always be considered in
                the order that they were provided when they are being applied.
            augmentors: list(AugmentorBase) | tuple(AugmentorBase)
                Augmentors to be applied (in same order as selection_probs).
            random_seed: int
                Random seed for controlling shuffling behavior.
        """
        super().__init__(preserve_order, augmentors, random_seed)

    def _execute(self, obj):
        """Execute the merged scheme by always applying every contained augmentor (in a potentially
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
            aug = self._augmentors[idx]
            output_obj = aug.augment(output_obj)
        return output_obj
