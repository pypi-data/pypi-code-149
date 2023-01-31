# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Module contains SROM specific Exceptions
"""


class MissingParameterException(Exception):
    """
    Exception class for missing parameter exception
    """

    def __init__(self, param_name):
        Exception.__init__(
            self, "Parameter {0} is missing in the function call".format(param_name)
        )


class InputDataParamMissingException(Exception):
    """
    Exception class for input data missing parameters
    """

    def __init__(self, param_names):
        Exception.__init__(self, param_names)


class InputDataParamBlankException(Exception):
    """
    Exception class for input data blank parameters
    """

    def __init__(self, param_names):
        Exception.__init__(self, param_names)


class IncorrectValueException(Exception):
    """Exception class for incorrect value"""

    def __init__(self, message):
        Exception.__init__(self, message)
