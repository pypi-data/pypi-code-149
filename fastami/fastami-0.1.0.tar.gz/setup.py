# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastami']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1', 'scikit-learn>=1.2.0', 'scipy>=1.10.0']

setup_kwargs = {
    'name': 'fastami',
    'version': '0.1.0',
    'description': 'A Monte Carlo approximation to the adjusted and standardized mutual information for faster clustering comparisons',
    'long_description': '# FastAMI\n\nA Monte Carlo approximation to the adjusted and standardized mutual information for faster clustering comparisons\n\n\n',
    'author': 'FastAMI',
    'author_email': 'kai.klede@fau.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
