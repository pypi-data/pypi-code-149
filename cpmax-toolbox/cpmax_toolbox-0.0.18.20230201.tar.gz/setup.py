# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cpmax_toolbox']

package_data = \
{'': ['*']}

install_requires = \
['pytz>=2022.7.1,<2023.0.0', 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'cpmax-toolbox',
    'version': '0.0.18.20230201',
    'description': 'Toolbox for cpmax',
    'long_description': '',
    'author': 'JRoseCPMax',
    'author_email': 'j.rose@cpmax.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
