# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mkdocs_simple', 'mkdocs_simple.cli']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['mkdocs-simple = mkdocs_simple.cli.app:run']}

setup_kwargs = {
    'name': 'mkdocs-simple',
    'version': '0.0.1',
    'description': '',
    'long_description': '# MkDocs Simple\n\n[![PyPI](https://img.shields.io/pypi/v/mkdocs-simple)](https://pypi.org/project/mkdocs-simple/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-simple)](https://www.python.org/downloads/)\n[![GitHub last commit](https://img.shields.io/github/last-commit/daxartio/mkdocs-simple)](https://github.com/daxartio/mkdocs-simple)\n[![GitHub stars](https://img.shields.io/github/stars/daxartio/mkdocs-simple?style=social)](https://github.com/daxartio/mkdocs-simple)\n\n## Installation\n\n### pip\n\n```\npip install mkdocs-simple\n```\n\n### poetry\n\n```\npoetry add mkdocs-simple\n```\n\n## Usage\n\n```python\nfrom mkdocs_simple import __version__\n```\n\n## License\n\n* [MIT LICENSE](LICENSE)\n\n## Contribution\n\n[Contribution guidelines for this project](CONTRIBUTING.md)\n',
    'author': 'Danil Akhtarov',
    'author_email': 'daxartio@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/mkdocs-simple',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
