# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['lcacollect_config', 'lcacollect_config.graphql']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy[asyncio]==1.4.35',
 'aiocache',
 'asyncpg>=0.26.0,<0.27.0',
 'fastapi-azure-auth',
 'pydantic',
 'sqlmodel>=0.0.8',
 'strawberry-graphql[fastapi]>=0.126.0']

setup_kwargs = {
    'name': 'lcacollect-config',
    'version': '1.0.1',
    'description': 'This package contains shared config and utils to be used across LCAcollect backends.',
    'long_description': '# LCAcollect Shared Config Package\n\nThis package contains shared config and utils to be used across LCAcollect backends. It is a Python package, distributed to\nPyPI to be consumed from the relevant backends.\n\n# Getting Started\n\nInstall the following in your virtual environment:\n\n- Python 3.10\n- [Poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)\n- [pre-commit](https://pre-commit.com/#installation)\n\n**Setup local Python environment**\n\n```shell\npoetry install\npre-commit install\n```\n\n**Run tests**\n\n```shell\npytest tests/\n```\n\n# Publishing\n\nAzure Artifacts are being used to\nmanage [versioning of this package](https://dev.azure.com/arkitema/lca-platform/_artifacts/feed/backend-packages/PyPI/lcaconfig/versions)\n. When a new version is ready to be published, remember to update the version by running the following command:\n```shell\npoetry version minor\n```\notherwise the pipeline will fail to publish the package.\nPublishing happens automatically on merges to `main` in an Azure Pipeline.\n',
    'author': 'Christian Kongsgaard',
    'author_email': 'chrk@arkitema.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lcacollect/shared-config-backend',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
