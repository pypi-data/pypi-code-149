# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['zeversolar']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.2.1,<8.0.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'zeversolar',
    'version': '0.3.0',
    'description': '',
    'long_description': 'None',
    'author': 'Koen van Zuijlen',
    'author_email': '8818390+kvanzuijlen@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
