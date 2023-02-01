# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['babble', 'babble.scripts', 'babble.templates.aws']

package_data = \
{'': ['*'], 'babble': ['providers/*']}

install_requires = \
['simple-term-menu==1.6.1']

entry_points = \
{'console_scripts': ['babble = babble.entry:main']}

setup_kwargs = {
    'name': 'babble-cloud-cli',
    'version': '0.1.10',
    'description': 'serverless applications made easy',
    'long_description': '# babble-cloud-cli',
    'author': 'mkearney2023',
    'author_email': 'mkearney2023@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
