# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Utilities for function cacheing"""

import datetime as dt
import json
import logging
from functools import wraps

LOGGER = logging.getLogger(__name__)



class FnCaching:
    """Wraps a function call with an in-memory cache"""

    def __init__(self, maxage=dt.timedelta(hours=1)):
        """
        :param: maxage timedelta for maximum age of cache before it will expire
        """
        self._createdon = dt.datetime.now()
        self._maxage = maxage

    def set_maxage(self, maxage):
        """set the maxage
        (duration beyond which the cache will be reset)

        :param maxage: a datetime.timedelta
        """
        self._maxage = maxage

    def cache_vararg_kwarg(self, function):
        """Cache a function taking combination
        of var args and kwargs.

        In order to reset caching for a call, pass
        __fncaching_reset = True as part of **kwargs

        By default the cache will be emptied every MAXAGE (a python timedelta object).
        This is a global value for this module so users can set it (with great care) to
        adjust this behavior.

        """
        memo = {}

        @wraps(function)
        def wrapper(*args, **kwargs):
            age = dt.datetime.now() - self._createdon
            if age > self._maxage:
                LOGGER.info("max age exceeded, clearing all cached entries")
                memo.clear()
                self._createdon = dt.datetime.now()
            __fncaching_reset = kwargs.get("__fncaching_reset", False)
            # we never want this as part of the key or args passed
            # to function
            if "__fncaching_reset" in kwargs:
                kwargs.pop("__fncaching_reset")

            key = (args, json.dumps(kwargs))
            if __fncaching_reset and key in memo:
                if "filename" in kwargs:
                    LOGGER.info("Cache reset for model: %s", kwargs["filename"])
                else:
                    LOGGER.info("Cache reset.")
                memo.pop(key)

            if key in memo:
                return memo[key]
            else:
                returnval = function(*args, **kwargs)
                memo[key] = returnval
                return returnval

        return wrapper
