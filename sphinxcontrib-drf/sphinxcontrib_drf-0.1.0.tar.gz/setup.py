# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sphinxcontrib_drf', 'sphinxcontrib_drf.docstrings']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.1.6,<4.0.0',
 'djangorestframework>=3.14.0,<4.0.0',
 'sphinx>=6.1.3,<7.0.0']

setup_kwargs = {
    'name': 'sphinxcontrib-drf',
    'version': '0.1.0',
    'description': '',
    'long_description': '# sphinxcontrib-drf\n',
    'author': 'Bulat Kurbanov',
    'author_email': 'kurbanovbul@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
