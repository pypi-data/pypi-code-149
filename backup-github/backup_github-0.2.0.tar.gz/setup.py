# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['backup_github']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['backup-github = main']}

setup_kwargs = {
    'name': 'backup-github',
    'version': '0.2.0',
    'description': '',
    'long_description': '',
    'author': 'Karina5005',
    'author_email': 'karinaanisimova23062001@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
