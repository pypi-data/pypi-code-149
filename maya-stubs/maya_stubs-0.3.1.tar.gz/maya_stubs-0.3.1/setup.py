# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['maya-stubs']

package_data = \
{'': ['*'], 'maya-stubs': ['api/*']}

setup_kwargs = {
    'name': 'maya-stubs',
    'version': '0.3.1',
    'description': "Stubs for Autodesk Maya's Python APIs",
    'long_description': 'None',
    'author': 'Loïc Pinsard',
    'author_email': 'muream@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*',
}


setup(**setup_kwargs)
