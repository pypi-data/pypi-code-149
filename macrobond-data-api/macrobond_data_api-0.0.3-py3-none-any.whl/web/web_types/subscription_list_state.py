# -*- coding: utf-8 -*-

# pylint: disable=invalid-name , missing-module-docstring

from enum import IntEnum


class SubscriptionListState(IntEnum):
    """The statate of the subscription list."""

    FULL_LISTING = 0
    """
    A complete listing of all series. 
    Make another request for full data at some point after timestamp in downloadFullListOnOrAfter.
    """

    UP_TO_DATE = 1
    """
    The list contains all updates since the specified start date.
    Wait 15 minutes before making another request where timeStampForIfModifiedSince is used.
    """

    INCOMPLETE = 2
    """
    The list might not contain all updates.
    Wait one minute and then use the timeStampForIfModifiedSince in an a new request.
    """
