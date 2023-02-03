# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_nav3']

package_data = \
{'': ['*']}

install_requires = \
['dominate>=2.7.0,<3.0.0', 'flask>=2.2.2,<3.0.0', 'visitor>=0.1.3,<0.2.0']

setup_kwargs = {
    'name': 'flask-nav3',
    'version': '0.7.0',
    'description': 'Easily create navigation for Flask applications.',
    'long_description': "# Flask-Nav3\n\n[![Build Status](https://github.com/wtfo-guru/Flask-Nav3/workflows/test/badge.svg?branch=main&event=push)](https://github.com/wtfo-guru/Flask-Nav3/actions?query=workflow%3Atest)\n[![codecov](https://codecov.io/gh/wtfo-guru/Flask-Nav3/branch/main/graph/badge.svg)](https://codecov.io/gh/wtfo-guru/Flask-Nav3)\n[![Python Version](https://img.shields.io/pypi/pyversions/Flask-Nav3.svg)](https://pypi.org/project/Flask-Nav3/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\nFlask-Nav3 is a fork of [Flask-Nav](https://github.com/mbr/flask-nav) which seems to be unmaintained.\n\nI was using Flask-Nav in several personal projects, when I started seeing deprecation notices, therefore I decided to fork the project and hopefully maintain this fork. Although I don't believe the changes I have made affect backwards compatibility, I am only testing on python 3.7 through 3.11 at this time.\n\nI have also attempted to make the source compatible with [wemake-python-styleguide]](https://github.com/wemake-services/wemake-python-styleguide).\n\n[Flask-Nav README](README-Flask-Nav.rst)\n",
    'author': 'Quien Sabe',
    'author_email': 'qs5779@mail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/wtfo-guru/flask-nav3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
