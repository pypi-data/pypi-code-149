# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rango']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rango-framework',
    'version': '0.1.0',
    'description': 'RangoFramework',
    'long_description': '# RangoFramework\n',
    'author': 'Sergey Shikhovtsov',
    'author_email': 'sh.sergey.yur@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/rango-framework/rango-framework',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
