# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

import os

from . import json_test_data
from . import text_test_data


def test_data_iter(directory):
    if os.path.isdir(directory):
        return text_test_data.TextDirIterator(directory)

    if directory.endswith(".json"):
        return json_test_data.JsonDataIterator(directory)

    raise ValueError(
        "Incorrect test directory. Must be either a directory or a .json file "
        "with `text` attribute"
    )
