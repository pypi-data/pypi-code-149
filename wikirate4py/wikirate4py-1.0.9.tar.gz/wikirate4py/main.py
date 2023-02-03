from pprint import pprint

import requests

import wikirate4py

api = wikirate4py.API('ThessaloWikiRate',
                      wikirate_api_url="https://staging.wikirate.org",
                      auth=('wikirate', 'wikirat'))

file = "C:/Users/vasgat/Desktop/Modern Slavery Statement SugaRich.pdf"
response = api.add_source(title='Hello World', file=file)
print(response)

# # response = requests.request("post", url="https://staging.wikirate.org/update/Source_000172231",
# #                             auth=('wikirate', 'wikirat'),
# #                             headers={"content-type": "application/pdf",
# #                                      'X-API-Key': "ThessaloWikiRate"},
# #                             files={'card[subcards][+File]': open("TestSource.pdf", 'rb')})
# #
# # print(response.status_code)
