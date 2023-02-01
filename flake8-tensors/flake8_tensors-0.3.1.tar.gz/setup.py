# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_tensors']

package_data = \
{'': ['*']}

install_requires = \
['astpath>=0.9.0,<0.10.0',
 'flake8>=6.0,<7.0',
 'lxml>=4.9.2,<5.0.0',
 'ruamel.yaml>=0.17.21,<0.18.0',
 'setuptools>=67.1.0,<68.0.0']

entry_points = \
{'flake8.extension': ['WT = flake8_tensors:Flake8TensorsPlugin']}

setup_kwargs = {
    'name': 'flake8-tensors',
    'version': '0.3.1',
    'description': 'flake8_tensors - flake8 plugin for deep learning codes',
    'long_description': '',
    'author': 'David Völgyes',
    'author_email': 'david.volgyes@ieee.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dvolgyes/flake8_tensors',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
