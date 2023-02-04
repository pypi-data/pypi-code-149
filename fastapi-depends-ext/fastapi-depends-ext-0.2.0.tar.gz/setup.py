# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_depends_ext']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.70.0,<1.0.0']

setup_kwargs = {
    'name': 'fastapi-depends-ext',
    'version': '0.2.0',
    'description': 'Extends FastAPI Depends classes to simple way of modifying them after creating',
    'long_description': None,
    'author': 'Nikakto',
    'author_email': 'mcgish@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
