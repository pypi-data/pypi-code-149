# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dictation_to_shell']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.2.2,<0.3.0']

entry_points = \
{'console_scripts': ['dictation_to_shell = dictation_to_shell.main:main']}

setup_kwargs = {
    'name': 'dictation-to-shell',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Eric Kalosa-Kenyon',
    'author_email': 'helloateric@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ekalosak/dictation-to-shell',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
