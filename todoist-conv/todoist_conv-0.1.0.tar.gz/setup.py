# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['todoist_conv',
 'todoist_conv.formats',
 'todoist_conv.formats.csv',
 'todoist_conv.formats.opml']

package_data = \
{'': ['*']}

install_requires = \
['chardet>=5.1.0,<6.0.0', 'click>=8.1.3,<9.0.0', 'pydantic>=1.9.1,<2.0.0']

entry_points = \
{'console_scripts': ['todoist-conv = todoist_conv.cli:cli']}

setup_kwargs = {
    'name': 'todoist-conv',
    'version': '0.1.0',
    'description': 'Convert Todoist generated CSVs to/from other formats',
    'long_description': 'None',
    'author': 'Ygor Mutti',
    'author_email': 'ygormutti@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '==3.10.4',
}


setup(**setup_kwargs)
