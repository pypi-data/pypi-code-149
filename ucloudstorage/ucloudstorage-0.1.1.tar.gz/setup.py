# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ucloudstorage', 'ucloudstorage.drivers', 'ucloudstorage.drivers.amazon']

package_data = \
{'': ['*']}

install_requires = \
['aiobotocore>=2.4.2,<3.0.0',
 'pytest-asyncio>=0.20.3,<0.21.0',
 'pytest>=7.2.1,<8.0.0']

setup_kwargs = {
    'name': 'ucloudstorage',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Unified Cloud Storage\n\nA simple project that provides an API to consume multiples Cloud Storage from different providers (just s3 at the moment).\n\n## Quick Installation\nTBD\n\n## Usage\nTBD\n\n### Reference\nThe project was based on the [scottwernervt Cloud Storage project](https://github.com/scottwernervt/cloudstorage).\nI did just for praticing purpose.',
    'author': 'Breno Moura',
    'author_email': 'breno.mm@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
