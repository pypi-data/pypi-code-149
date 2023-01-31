# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#


class DataValidationError(Exception):
    """This error is used for data validation problems during training"""

    def __init__(self, reason, item_number=None):
        if item_number:
            message = "Training data validation failed on item {}. {}".format(
                item_number, reason
            )
        else:
            message = "Training data validation failed: {}".format(reason)
        super().__init__(message)
        self._reason = reason
        self._item_number = item_number

    @property
    def reason(self) -> str:
        """The reason given for this data validation error"""
        return self._reason

    @property
    def item_number(self) -> int:
        """The index of the training data item that failed validation. Probably zero indexed"""
        return self._item_number
