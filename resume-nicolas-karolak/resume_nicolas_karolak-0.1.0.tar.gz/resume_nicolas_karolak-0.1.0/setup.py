# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pkg']

package_data = \
{'': ['*']}

install_requires = \
['resume-pycli']

setup_kwargs = {
    'name': 'resume-nicolas-karolak',
    'version': '0.1.0',
    'description': 'CV de Nicolas Karolak',
    'long_description': '',
    'author': 'Nicolas Karolak',
    'author_email': 'cv@karolak.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://cv.karolak.fr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
