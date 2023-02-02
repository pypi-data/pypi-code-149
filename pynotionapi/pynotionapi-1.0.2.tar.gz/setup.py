# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynotion', 'pynotion.endpoints', 'pynotion.schemas']

package_data = \
{'': ['*']}

install_requires = \
['marshmallow>=3.19.0,<4.0.0', 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'pynotionapi',
    'version': '1.0.2',
    'description': 'Notion API client for Python',
    'long_description': '[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua)\n\n# Python Notion API\n\nNotion API client in Python.\n',
    'author': 'Andrew Yatsura',
    'author_email': 'andrewyazura203@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/andrewyazura/pynotion',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
