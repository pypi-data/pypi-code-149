"""
    NewsCatcher News API V2

    NewsCatcher is a data-as-a-service startup that has one main goal: to build the largest database of structured news articles published online. In other words, we're like Google for the news part of the web, which you can access as a source of data.  Some useful links: - [How NewsCatcher Works](https://docs.newscatcherapi.com/knowledge-base/how-newscatcher-works) - [GitHub for the Python SDK](https://github.com/NewscatcherAPI/newscatcherapi-sdk-python)   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: team@newscatcherapi.com
    Generated by: https://konfigthis.com
"""


import unittest

import os
from newscatcherapi_client.api.latest_headlines_api import LatestHeadlinesApi  # noqa: E501
from newscatcherapi_client.configuration import Configuration
from newscatcherapi_client.api_client import ApiClient
from newscatcherapi_client.models import Topic, Page, PageSize


class TestLatestHeadlinesApi(unittest.TestCase):
    """LatestHeadlinesApi unit test stubs"""

    def setUp(self):
        configuration = Configuration(api_key={'api_key': os.environ["NEWSCATCHER_API_KEY"]})
        api_client = ApiClient(configuration)
        self.api = LatestHeadlinesApi(api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_getting_Started(self):
        """Test case for Getting Started snippet from README"""
        lang = "en"
        not_lang = "af"
        countries = "US,CA"
        not_countries = "US,CA"
        topic = Topic("business")
        sources = "nytimes.com,theguardian.com"
        not_sources = "wsj.com"
        ranked_only = True
        page_size = PageSize(100)
        page = Page(1)
        api_response = self.api.get(lang=lang, not_lang=not_lang,
                                    countries=countries, not_countries=not_countries, topic=topic,
                                    sources=sources, not_sources=not_sources, ranked_only=ranked_only,
                                    page_size=page_size, page=page)
        assert api_response is not None, "Response is null"


if __name__ == '__main__':
    unittest.main()
