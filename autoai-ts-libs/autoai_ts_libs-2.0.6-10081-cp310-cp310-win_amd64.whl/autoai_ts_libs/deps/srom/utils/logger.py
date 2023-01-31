# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""This module provides functionality for global logging configurations across all srom modules."""

# maintained for backward compatibility
# really don't like doing clandestine configuration
import warnings
warnings.warn(
    """srom.utils.logger is deprecated 
                 and currently performs a no-op""",
    DeprecationWarning,
)

