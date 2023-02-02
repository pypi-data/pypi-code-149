# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['star_alchemy']

package_data = \
{'': ['*']}

install_requires = \
['sqlalchemy>=2,<3', 'toolz>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'star-alchemy',
    'version': '0.4.0',
    'description': '',
    'long_description': 'None',
    'author': 'Daniel Bradburn',
    'author_email': 'moagstar@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
