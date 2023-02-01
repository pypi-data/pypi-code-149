# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ms_graph_client', 'ms_graph_client.services']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=5.0.0,<6.0.0', 'requests>=2.28.0,<3.0.0']

setup_kwargs = {
    'name': 'ms-graph-client',
    'version': '0.1.1',
    'description': 'Provides a python wrapper around the Microsoft Graph API.  Current SDKs from Microsoft are in Preview mode.',
    'long_description': 'export PATH="$HOME/.local/bin:$PATH"\n\nDocs: https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0\n',
    'author': 'Nick Carpenter',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
