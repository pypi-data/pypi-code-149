# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['octopusserver',
 'octopusserver.Http',
 'octopusserver.Http.Router',
 'octopusserver.Utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'octopusserver',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Octopusserver\n\n![Octopus](./assets/octopus.png)\n',
    'author': 'pab-h',
    'author_email': 'dev.pab.2020@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
