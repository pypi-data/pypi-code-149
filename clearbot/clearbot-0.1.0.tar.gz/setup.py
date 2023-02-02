# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['main']
install_requires = \
['pillow>=9.4.0,<10.0.0', 'requests>=2.28.2,<3.0.0', 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['clearbot = main:cli']}

setup_kwargs = {
    'name': 'clearbot',
    'version': '0.1.0',
    'description': 'Clearbit Logo API client',
    'long_description': '# clearbot\nClearbit Logo API client\n',
    'author': 'Alban Siffer',
    'author_email': 'alban.siffer@irisa.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
