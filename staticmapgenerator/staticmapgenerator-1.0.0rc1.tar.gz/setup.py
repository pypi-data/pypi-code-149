# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['staticmapgenerator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'staticmapgenerator',
    'version': '1.0.0rc1',
    'description': '',
    'long_description': '# map-python',
    'author': 'D1ffic00lt',
    'author_email': 'dm.filinov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/D1ffic00lt/map-generator-python',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
