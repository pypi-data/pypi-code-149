# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['argparge']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'argparge',
    'version': '0.1.0',
    'description': 'A very simple tool to create beautiful console application by using native argparse.',
    'long_description': None,
    'author': 'Ozcan Yarimdunya',
    'author_email': 'ozcan.yarimdunya@sahibinden.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
