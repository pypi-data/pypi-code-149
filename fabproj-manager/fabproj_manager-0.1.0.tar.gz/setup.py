# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fabproj_manager', 'fabproj_manager.modules']

package_data = \
{'': ['*'], 'fabproj_manager.modules': ['img/*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'nbformat>=5.7.3,<6.0.0']

entry_points = \
{'console_scripts': ['fabproj = fabproj_manager.fabproj:create_project']}

setup_kwargs = {
    'name': 'fabproj-manager',
    'version': '0.1.0',
    'description': '',
    'long_description': 'README',
    'author': 'Devin Lane',
    'author_email': 'silvertenor@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
