# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['modelicalang']

package_data = \
{'': ['*']}

install_requires = \
['Arpeggio>=0.8', 'typing-extensions>=3.10']

setup_kwargs = {
    'name': 'modelicalang',
    'version': '0.1.0a0',
    'description': 'Modelica parser and class representation for Python',
    'long_description': '# ModelicaLang\n\nModelica parser and class representation for Python\n\n[See document](https://ijknabla.github.io/ModelicaLanguageForPython/)\n',
    'author': 'ijknabla',
    'author_email': 'ijknabla@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ijknabla/ModelicaLanguageForPython',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
