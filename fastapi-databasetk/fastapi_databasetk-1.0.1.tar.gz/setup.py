# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_databasetk', 'fastapi_databasetk.objects']

package_data = \
{'': ['*']}

install_requires = \
['databases>=0.6.0,<0.7.0',
 'fastapi>=0.89.1,<0.90.0',
 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'fastapi-databasetk',
    'version': '1.0.1',
    'description': '',
    'long_description': '',
    'author': 'wayfaring-stranger',
    'author_email': 'zw6p226m@duck.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
