# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['delphai_search_utils', 'delphai_search_utils.tests']

package_data = \
{'': ['*'], 'delphai_search_utils': ['data/*']}

install_requires = \
['delphai-utils[config,grpc,database]>=0.2.20,<4.0.0', 'nltk', 'sacremoses']

setup_kwargs = {
    'name': 'delphai-search-utils',
    'version': '0.1.9',
    'description': 'delphai search utilities',
    'long_description': None,
    'author': 'Christopher Schiefer',
    'author_email': 'christopher.schiefer@delphai.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/delphai/delphai-search-utils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
