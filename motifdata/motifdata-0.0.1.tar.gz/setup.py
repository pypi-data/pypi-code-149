# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['motifdata']

package_data = \
{'': ['*'], 'motifdata': ['resources/*']}

install_requires = \
['numpy>=1.21.5,<2.0.0']

setup_kwargs = {
    'name': 'motifdata',
    'version': '0.0.1',
    'description': 'A tool for handling biological sequence motifs in Python',
    'long_description': None,
    'author': 'adamklie',
    'author_email': 'aklie@ucsd.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.12,<3.11',
}


setup(**setup_kwargs)
