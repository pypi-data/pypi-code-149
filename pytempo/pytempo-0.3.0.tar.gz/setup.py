# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytempo']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'datetime>=5.0,<6.0',
 'openpyxl>=3.1.0,<4.0.0',
 'pandas>=1.5.3,<2.0.0',
 'xlrd>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['pytempo = pytempo.main:main']}

setup_kwargs = {
    'name': 'pytempo',
    'version': '0.3.0',
    'description': '',
    'long_description': '',
    'author': 'Sebastian Blum',
    'author_email': 'sebast.blum@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
