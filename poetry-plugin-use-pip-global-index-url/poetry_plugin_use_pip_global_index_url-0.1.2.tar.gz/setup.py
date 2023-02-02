# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_plugin_use_pip_global_index_url']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.1,<1.3.0']

entry_points = \
{'poetry.plugin': ['demo = '
                   'poetry_plugin_use_pip_global_index_url.plugins:UsePipGlobalIndexUrlPlugin']}

setup_kwargs = {
    'name': 'poetry-plugin-use-pip-global-index-url',
    'version': '0.1.2',
    'description': 'Poetry plugin that sets the global index with the value obtained from pip.',
    'long_description': 'None',
    'author': 'Jacob Henner',
    'author_email': 'code@ventricle.us',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
