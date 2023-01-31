# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['package', 'package.scripts', 'package.templates.aws']

package_data = \
{'': ['*'], 'package': ['providers/*']}

entry_points = \
{'console_scripts': ['babble = package.entry:main']}

setup_kwargs = {
    'name': 'babble-cloud-cli',
    'version': '0.1.1',
    'description': 'serverless programming made easy',
    'long_description': '# babble-cloud-cli',
    'author': 'mkearney2023',
    'author_email': 'mkearney2023@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '==3.10.9',
}


setup(**setup_kwargs)
