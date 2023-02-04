# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kamaqi',
 'kamaqi.add',
 'kamaqi.app',
 'kamaqi.init',
 'kamaqi.remove',
 'kamaqi.run',
 'kamaqi.show',
 'kamaqi.templates',
 'kamaqi.upgrade',
 'kamaqi.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['kamaqi = kamaqi.main:app']}

setup_kwargs = {
    'name': 'kamaqi',
    'version': '0.1.0',
    'description': 'A comand line app',
    'long_description': 'A comand line app to FastAPI inspired in Artisan from Laravel and manage.py from Django',
    'author': 'Mitchell Mirano',
    'author_email': 'mitchellmirano25@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
