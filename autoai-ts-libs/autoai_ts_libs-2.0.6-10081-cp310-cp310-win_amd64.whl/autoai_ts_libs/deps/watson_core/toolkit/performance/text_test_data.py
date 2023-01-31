# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

import os

TEST_FILE_EXTENSIONS = [".txt", ".html"]


class TextDirIterator:
    """Iterator class to iterate a directory of valid files where each file's text is read
    recursively within the dir Iterator returns the raw text string on each iteration.
    """

    def __init__(self, directory):
        self.text_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.endswith(extn) for extn in TEST_FILE_EXTENSIONS):
                    self.text_files.append(os.path.join(root, file))
        self.files_iter = iter(self.text_files)

    def __iter__(self):
        return self

    def __next__(self):
        with open(
            next(self.files_iter), "r", encoding="utf8", errors="ignore"
        ) as text_file:
            return text_file.read()

    def __len__(self):
        return len(self.text_files)
