"""
    NewsCatcher News API V2

    NewsCatcher is a data-as-a-service startup that has one main goal: to build the largest database of structured news articles published online. In other words, we're like Google for the news part of the web, which you can access as a source of data.  Some useful links: - [How NewsCatcher Works](https://docs.newscatcherapi.com/knowledge-base/how-newscatcher-works) - [GitHub for the Python SDK](https://github.com/NewscatcherAPI/newscatcherapi-sdk-python)   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: team@newscatcherapi.com
    Generated by: https://konfigthis.com
"""


import unittest

import os
from newscatcherapi_client.api.search_api import SearchApi  # noqa: E501
from newscatcherapi_client.configuration import Configuration
from newscatcherapi_client.api_client import ApiClient
from newscatcherapi_client.model.search import Search


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        configuration = Configuration(api_key={'api_key': os.environ["NEWSCATCHER_API_KEY"]})
        api_client = ApiClient(configuration)
        self.api = SearchApi(api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_get(self):
        """Test case for get

        Search for specific news articles  # noqa: E501
        """
        response = self.api.get(q="Apple", _from="three months ago")
        assert response is not None, "Received null response"

    def test_post(self):
        """Test case for post

        Search for specific news articles  # noqa: E501
        """
        response = self.api.post(search=Search(q='Apple', _from='three months ago'))
        assert response is not None, "Received null response"


if __name__ == '__main__':
    unittest.main()
