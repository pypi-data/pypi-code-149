# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pretty_markdown_tables']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0',
 'markdown2>=2.4.7,<3.0.0',
 'pandas>=1.5.3,<2.0.0',
 'pretty-html-table>=0.9.16,<0.10.0',
 'pytest>=7.2.1,<8.0.0']

setup_kwargs = {
    'name': 'pretty-markdown-tables',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'vidigalp',
    'author_email': 'vidigal.pedro@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
