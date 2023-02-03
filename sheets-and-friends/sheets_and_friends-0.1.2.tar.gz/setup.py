# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sheets_and_friends', 'sheets_and_friends.converters']

package_data = \
{'': ['*'], 'sheets_and_friends': ['.idea/*', '.idea/inspectionProfiles/*']}

entry_points = \
{'console_scripts': ['do_shuttle = sheets_and_friends.shuttle:do_shuttle']}

setup_kwargs = {
    'name': 'sheets-and-friends',
    'version': '0.1.2',
    'description': 'Create a LinkML model with as-is imported slots, imported but modified slots (via yq), or newly minted slots (via schemasheets)',
    'long_description': 'None',
    'author': 'Mark Andrew Miller',
    'author_email': 'MAM@lbl.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
