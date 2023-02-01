# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['linear_garage_door']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'certifi>=2022.12.7,<2023.0.0',
 'dnspython>=2.3.0,<3.0.0',
 'websocket-client>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'linear-garage-door',
    'version': '0.2.1',
    'description': 'Control Linear Garage Doors with Python',
    'long_description': "# Linear Garage Door\n\n[![PyPI](https://img.shields.io/pypi/v/linear-garage-door?style=flat-square)](https://pypi.python.org/pypi/linear-garage-door/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/linear-garage-door?style=flat-square)](https://pypi.python.org/pypi/linear-garage-door/)\n[![PyPI - License](https://img.shields.io/pypi/l/linear-garage-door?style=flat-square)](https://pypi.python.org/pypi/linear-garage-door/)\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://IceBotYT.github.io/linear-garage-door](https://IceBotYT.github.io/linear-garage-door)\n\n**Source Code**: [https://github.com/IceBotYT/linear-garage-door](https://github.com/IceBotYT/linear-garage-door)\n\n**PyPI**: [https://pypi.org/project/linear-garage-door/](https://pypi.org/project/linear-garage-door/)\n\n---\n\nControl Linear Garage Doors with Python\n\n## Installation\n\n```sh\npip install linear-garage-door\n```\n\n## Development\n\n* Clone this repository\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.7+\n* Create a virtual environment and install the dependencies\n\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n\n```sh\npoetry shell\n```\n\n### Testing\n\n```sh\npytest\n```\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings\n of the public signatures of the source code. The documentation is updated and published as a [Github project page\n ](https://pages.github.com/) automatically as part each release.\n\n### Releasing\n\nTrigger the [Draft release workflow](https://github.com/IceBotYT/linear-garage-door/actions/workflows/draft_release.yml)\n(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.\n\nFind the draft release from the\n[GitHub releases](https://github.com/IceBotYT/linear-garage-door/releases) and publish it. When\n a release is published, it'll trigger [release](https://github.com/IceBotYT/linear-garage-door/blob/master/.github/workflows/release.yml) workflow which creates PyPI\n release and deploys updated documentation.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality\n checks to make sure the changeset is in good shape before a commit/push happens.\n\nYou can install the hooks with (runs for each commit):\n\n```sh\npre-commit install\n```\n\nOr if you want them to run only for each push:\n\n```sh\npre-commit install -t pre-push\n```\n\nOr if you want e.g. want to run all checks manually for all files:\n\n```sh\npre-commit run --all-files\n```\n\n---\n\nThis project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.\n",
    'author': 'IceBotYT',
    'author_email': 'icebotyt@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://IceBotYT.github.io/linear-garage-door',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
