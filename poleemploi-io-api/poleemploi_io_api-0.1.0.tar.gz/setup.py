# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poleemploi_io_api',
 'poleemploi_io_api.base',
 'poleemploi_io_api.rome.v1',
 'poleemploi_io_api.tests']

package_data = \
{'': ['*']}

install_requires = \
['pydantic[email]>=1.10.4,<2.0.0', 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'poleemploi-io-api',
    'version': '0.1.0',
    'description': 'Python package to use poleemploi io api (requires account)',
    'long_description': '# PoleEmploi IO - Python Package\n\n## About\n\nThis package was intended to use the [poleemploi.io](https://pole-emploi.io/) api.\n\nTo be able to use you need valid poleemloi.io credentials.\n\n\n## How tos\n\n### Tests\n\n``` bash\nmake test\n```\n\n### Documentation\n\nThe documentation is based on [mkdocs](https://www.mkdocs.org/)\n\nTo open the docs:\n\n``` bash\nmake help\n```\n\nIt will be accessible [here](http://127.0.0.1:9999/)\n',
    'author': 'La Bonne Boite',
    'author_email': 'labonneboite@pole-emploi.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/StartupsPoleEmploi/poleemploi-io-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
