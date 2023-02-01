# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['y']

package_data = \
{'': ['*']}

install_requires = \
['lark==1.1.5', 'ruamel.yaml==0.17.21']

entry_points = \
{'console_scripts': ['y = y.__main__:main']}

setup_kwargs = {
    'name': 're-y',
    'version': '1.0.0',
    'description': '',
    'long_description': 'None',
    'author': 'skphilipp',
    'author_email': 'philipp@release-engineers.com',
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
