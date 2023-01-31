# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

import json


class JsonDataIterator:
    """Iterator class to iterate a ".json" file where each line is a json element with "label" and
    "text" attribute which is a format chosen to comply with:
    https://github.ibm.com/watson-nlu/nlp-core-resources/blob/master/np-chunker/src/test/resources
    /docs/common/en/performance/en-50k-200.json
    Iterator returns the raw text string on each iteration
    """

    def __init__(self, directory):
        with open(directory, encoding="utf8", errors="ignore") as test_json_spec_file:
            self.files = test_json_spec_file.readlines()
            self.files_iter = iter(self.files)

    def __iter__(self):
        return self

    def __next__(self):
        file = json.loads(next(self.files_iter))
        if "text" in file:
            return file["text"]

    def __len__(self):
        return len(self.files)
