# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['suppenloffel']

package_data = \
{'': ['*']}

install_requires = \
['autopep8>=1.6.0,<2.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'numpy>=1.23.0,<2.0.0',
 'pandas>=1.5.3,<2.0.0']

setup_kwargs = {
    'name': 'suppenloffel',
    'version': '0.2.5.2',
    'description': 'suppenlöffel is a library build upon bs4 to provide fast webscraping scripting experience',
    'long_description': '',
    'author': 'Qubut',
    'author_email': 's-aahmed@haw-landshut.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
