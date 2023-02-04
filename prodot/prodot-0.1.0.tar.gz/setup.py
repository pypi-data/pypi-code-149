# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prodot']

package_data = \
{'': ['*']}

install_requires = \
['jsonpath-ng>=1.5.3,<2.0.0']

setup_kwargs = {
    'name': 'prodot',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Matheus Menezes Almeida',
    'author_email': 'mrotame@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
