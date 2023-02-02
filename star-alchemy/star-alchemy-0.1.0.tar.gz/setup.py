# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['star_alchemy', 'star_alchemy.contrib']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.2.0,<21.0.0', 'pycodestyle>=2.6.0,<3.0.0', 'sqlalchemy>=1,<2']

setup_kwargs = {
    'name': 'star-alchemy',
    'version': '0.1.0',
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
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
