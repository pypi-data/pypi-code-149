# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tests', 'tests.config', 'tests.http']

package_data = \
{'': ['*']}

install_requires = \
['faker>=16.6.1,<17.0.0', 'gyver>=0.23.0,<0.24.0', 'pytest>=7.2.1,<8.0.0']

setup_kwargs = {
    'name': 'gyver-tests',
    'version': '0.2.0',
    'description': '',
    'long_description': '',
    'author': 'Gustavo Correa',
    'author_email': 'self.gustavocorrea@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
