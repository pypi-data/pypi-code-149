# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ljxtools', 'ljxtools.utils', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'jinja2==3.0.3']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.15.2,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

setup_kwargs = {
    'name': 'ljxtools',
    'version': '0.3.10',
    'description': 'always use tools package.',
    'long_description': "# ljxtools\n\n\n[![pypi](https://img.shields.io/pypi/v/ljxtools.svg)](https://pypi.org/project/ljxtools/)\n[![python](https://img.shields.io/pypi/pyversions/ljxtools.svg)](https://pypi.org/project/ljxtools/)\n[![Build Status](https://github.com/ljxPython/ljxtools/actions/workflows/dev.yml/badge.svg)](https://github.com/ljxPython/ljxtools/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/ljxPython/ljxtools/branch/main/graphs/badge.svg)](https://codecov.io/github/ljxPython/ljxtools)\n\n\n\nalways use tools package\n\n\n* Documentation: <https://ljxPython.github.io/ljxtools>\n* GitHub: <https://github.com/ljxPython/ljxtools>\n* PyPI: <https://pypi.org/project/ljxtools/>\n* Free software: MIT\n\n## How To USe\n\n```\n## test\n\nfrom ljxtools.utils.date_operation import DatetimeSlove\n\nif __name__ == '__main__':\n    d = DatetimeSlove()\n    time_now = d.str_now()\n    print(time_now)\n```\n\n\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n",
    'author': 'ljxpython',
    'author_email': '1030470148@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ljxPython/ljxtools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
