# ****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# ****************************************************************#
"""Helper functions for performance computations.
"""


def kilo_chars_per_second(text_len, iterations, seconds):
    return text_len * iterations / 1000 / seconds


def kilo_chars_per_second_text(text, iterations, seconds):
    return kilo_chars_per_second(len(text), iterations, seconds)


def iterations_per_second(iterations, seconds):
    return iterations / seconds
