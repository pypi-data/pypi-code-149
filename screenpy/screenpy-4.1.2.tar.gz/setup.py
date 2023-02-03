# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['screenpy',
 'screenpy.actions',
 'screenpy.narration',
 'screenpy.narration.adapters',
 'screenpy.resolutions',
 'screenpy.resolutions.custom_matchers']

package_data = \
{'': ['*']}

install_requires = \
['PyHamcrest>=2.0.0', 'typing-extensions>=4.1.1']

extras_require = \
{':python_full_version >= "3.8.0" and python_full_version < "3.9.0"': ['importlib_metadata'],
 'allure': ['screenpy-adapter_allure>=4.0.1,<5.0.0'],
 'appium': ['screenpy-appium'],
 'dev': ['pre-commit', 'pytest', 'tox', 'pylint'],
 'dev-all': ['pre-commit',
             'pytest',
             'tox',
             'mypy',
             'black',
             'isort',
             'flake8',
             'pylint',
             'coverage'],
 'playwright': ['screenpy-playwright'],
 'pyotp': ['screenpy-pyotp>=4.0.1,<5.0.0'],
 'requests': ['screenpy-requests>=4.0.1,<5.0.0'],
 'selenium': ['screenpy-selenium>=4.0.3,<5.0.0'],
 'test': ['pytest', 'coverage']}

setup_kwargs = {
    'name': 'screenpy',
    'version': '4.1.2',
    'description': 'Screenplay pattern base for Python automated UI test suites.',
    'long_description': 'ScreenPy\n========\n[![Build Status](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)\n[![Build Status](../../actions/workflows/lint.yml/badge.svg)](../../actions/workflows/lint.yml)\n\n[![Supported Versions](https://img.shields.io/pypi/pyversions/screenpy.svg)](https://pypi.org/project/screenpy)\n[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n\n```\nTITLE CARD:\n                                  "ScreenPy"\nTITLE DISAPPEARS.\n                                                                      FADE IN:\nINT. DOCUMENTATION - NIGHT\n\nIlluminated by the computer\'s glow, AUDIENCE sits reading the documentation\nfor a Python library they haven\'t seen before. AUDIENCE is visibly startled\nas a dulcet voice begins to speak.\n\n                              NARRATOR (V.O.)\n            ScreenPy is a library that provides the base for an\n            automated test suite using Screenplay Pattern.\n\n                              AUDIENCE\n            Wha- who are you? Where are you? And... what is\n            Screenplay Pattern?!\n\n                              NARRATOR (V.O.)\n            It\'s a composition-based architecture pattern,\n            encouraging automated test writers to write more\n            maintainable test suites. It allows test writers to\n            use Gherkin-style language in Python to create\n            descriptive UI tests.\n\n                              AUDIENCE\n                              (reluctantly)\n            Ignoring how you avoided answering my first questions,\n            how do I get started?\n\n                              NARRATOR (V.O.)\n            I thought you\'d never ask...\n\n                                                                      FADE OUT\n```\n\n\nInstallation\n------------\n    pip install screenpy\n\n\nDocumentation\n----------\nPlease check out the [Read The Docs documentation](https://screenpy-docs.readthedocs.io/en/latest/) for the latest information about this module!\n\n\nContributing\n------------\nYou want to contribute? Great! Here are the things you should do before submitting your PR:\n\n1. Fork the repo and git clone your fork.\n1. `dev` install the project package:\n   1. `pip install -e .[dev]` \n   1. Optional (poetry users):\n      1. `poetry install --extras dev`\n1. Run `pre-commit install` once.\n1. Run `tox` to perform tests frequently.\n1. Create pull-request from your branch.\n\nThat\'s it! :)\n',
    'author': 'Perry Goy',
    'author_email': 'perry.goy@gmail.com',
    'maintainer': 'Gabe Langton',
    'maintainer_email': 'None',
    'url': 'https://github.com/ScreenPyHQ/screenpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
