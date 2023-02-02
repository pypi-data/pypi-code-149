# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git2ignore']

package_data = \
{'': ['*'],
 'git2ignore': ['templates/*',
                'templates/.github/*',
                'templates/Global/*',
                'templates/community/*',
                'templates/community/AWS/*',
                'templates/community/DotNet/*',
                'templates/community/Elixir/*',
                'templates/community/GNOME/*',
                'templates/community/Golang/*',
                'templates/community/Java/*',
                'templates/community/JavaScript/*',
                'templates/community/Linux/*',
                'templates/community/PHP/*',
                'templates/community/Python/*',
                'templates/community/embedded/*']}

entry_points = \
{'console_scripts': ['git2ignore = git2ignore.__init__:main']}

setup_kwargs = {
    'name': 'git2ignore',
    'version': '0.1.4',
    'description': 'python interface to generate .gitignore file.',
    'long_description': None,
    'author': 'Kyoungseoun Chung',
    'author_email': 'kyoungseoun.chung@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
