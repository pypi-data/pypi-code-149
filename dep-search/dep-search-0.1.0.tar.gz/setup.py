# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['search', 'search.internals', 'search.schemas', 'search.shared']

package_data = \
{'': ['*']}

install_requires = \
['dep-module-mongo>=2.13.29,<3.0.0', 'httpx>=0.23.3,<0.24.0', 'poetry==1.1.15']

setup_kwargs = {
    'name': 'dep-search',
    'version': '0.1.0',
    'description': 'Search dep',
    'long_description': None,
    'author': 'everhide',
    'author_email': 'i.tolkachnikov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<=3.11',
}


setup(**setup_kwargs)
