# coding: utf-8

# flake8: noqa

"""
    Recommendation API

    The <b>Recommendation API</b> returns information that sellers can use to optimize the configuration of their listings on eBay. <br><br>Currently, the API contains a single method, <b>findListingRecommendations</b>. This method provides information that sellers can use to configure Promoted Listings ad campaigns to maximize the visibility of their items in the eBay marketplace.  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from ..sell_recommendation.api.listing_recommendation_api import ListingRecommendationApi
# import ApiClient
from ..sell_recommendation.api_client import ApiClient
from ..sell_recommendation.configuration import Configuration
# import models into sdk package
from ..sell_recommendation.models.ad import Ad
from ..sell_recommendation.models.bid_percentages import BidPercentages
from ..sell_recommendation.models.error import Error
from ..sell_recommendation.models.error_parameter import ErrorParameter
from ..sell_recommendation.models.find_listing_recommendation_request import FindListingRecommendationRequest
from ..sell_recommendation.models.listing_recommendation import ListingRecommendation
from ..sell_recommendation.models.marketing_recommendation import MarketingRecommendation
from ..sell_recommendation.models.paged_listing_recommendation_collection import PagedListingRecommendationCollection
