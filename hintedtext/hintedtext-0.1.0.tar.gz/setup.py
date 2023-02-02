# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['hintedtext']
setup_kwargs = {
    'name': 'hintedtext',
    'version': '0.1.0',
    'description': 'Tkinter Text widget with an extra hint attribute.',
    'long_description': None,
    'author': 'Billy',
    'author_email': 'billydevbusiness@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
