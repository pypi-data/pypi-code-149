# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webpage_searcher',
 'webpage_searcher.finders',
 'webpage_searcher.finders.phrase',
 'webpage_searcher.finders.url',
 'webpage_searcher.outputs',
 'webpage_searcher.utils']

package_data = \
{'': ['*']}

install_requires = \
['bs4==0.0.1', 'requests==2.28.2']

setup_kwargs = {
    'name': 'webpage-searcher',
    'version': '0.0.1',
    'description': 'hello',
    'long_description': '# Webpage Searcher\n\n### Description\nA library that search for a phrase or a url in an html document\n\n### Usage\nTo search for a url:\n```\nfrom webpage_searcher import UrlFinder\n\nhtml = "<html><a href="https://google.com">google</a></html>"\nfinder = UrlFinder(html)\nresults = finder.find("google.com")\n```\n\nTo search for a phrase:\n```\nfrom webpage_searcher import PhraseFinder\n\nhtml = "<html>hello</html>"\nfinder = PhraseFinder(html)\nresults = finder.find("hello")\n```\n\n### Contributing\nTo run the tests:\n1. Install dev dependencies: `poetry install --all-extras`\n2. Run the tests: `pytest -v`\n',
    'author': 'john-blmns',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
