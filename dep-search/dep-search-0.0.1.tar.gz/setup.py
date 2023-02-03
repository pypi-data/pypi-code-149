# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['digest',
 'interface',
 'schemas',
 'schemas.examples',
 'schemas.raws',
 'schemas.sources']

package_data = \
{'': ['*']}

modules = \
['README',
 'shared_definitions',
 'shared_types',
 'shared_examples',
 'shared_func',
 '__init__']
install_requires = \
['dep-module-mongo>=2.13.29,<3.0.0', 'poetry==1.1.15']

setup_kwargs = {
    'name': 'dep-search',
    'version': '0.0.1',
    'description': 'Search dep',
    'long_description': None,
    'author': 'everhide',
    'author_email': 'i.tolkachnikov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<=3.11',
}


setup(**setup_kwargs)
