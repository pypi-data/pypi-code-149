# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exphub',
 'exphub.aggregators',
 'exphub.download',
 'exphub.selectors',
 'exphub.vizualization']

package_data = \
{'': ['*']}

install_requires = \
['neptune-client>=0.16.17,<0.17.0', 'plotly>=5.13.0,<6.0.0']

setup_kwargs = {
    'name': 'exphub',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
