# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['templtest']

package_data = \
{'': ['*']}

install_requires = \
['packaging>=22,<24']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['ansible-core>=2.11,<2.12'],
 ':python_version >= "3.8" and python_version < "3.9"': ['ansible-core>=2.13,<2.14'],
 ':python_version >= "3.9" and python_version < "4.0"': ['ansible-core>=2.14,<3.0']}

entry_points = \
{'console_scripts': ['templtest = templtest.cli:main']}

setup_kwargs = {
    'name': 'templtest',
    'version': '0.3.1',
    'description': 'A tool for testing Ansible role templates.',
    'long_description': 'None',
    'author': 'Alexey Busygin',
    'author_email': 'yaabusygin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
