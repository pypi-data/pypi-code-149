# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tao_poetry_example']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['inc = first_steps.cli:cli']}

setup_kwargs = {
    'name': 'tao-poetry-example',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Tao',
    'author_email': 'twang15@ncsu.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
