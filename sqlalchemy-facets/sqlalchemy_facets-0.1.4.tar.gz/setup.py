# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqlalchemy_facets']

package_data = \
{'': ['*']}

install_requires = \
['sqlalchemy>=1.3.13,<2.0.0']

setup_kwargs = {
    'name': 'sqlalchemy-facets',
    'version': '0.1.4',
    'description': 'Faceted search for SQLAlchemy',
    'long_description': 'None',
    'author': 'Thibaut Frain',
    'author_email': 'thibaut.frain@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
