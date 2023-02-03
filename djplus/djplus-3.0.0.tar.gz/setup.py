# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dj',
 'dj.auth',
 'dj.auth.migrations',
 'dj.auth.validators',
 'dj.blog',
 'dj.blog.migrations',
 'dj.project',
 'dj.project.settings',
 'dj.project_template',
 'dj.project_template.project_name',
 'dj.project_template.project_name.settings']

package_data = \
{'': ['*'],
 'dj.auth': ['templates/auth/*'],
 'dj.blog': ['templates/blog/*'],
 'dj.project': ['static/css/*', 'static/js/*', 'templates/*'],
 'dj.project_template': ['requirements/*',
                         'static/css/*',
                         'static/js/*',
                         'templates/*']}

install_requires = \
['Django>=4.0.3,<5.0.0', 'django-ipware>=4.0.2,<5.0.0']

entry_points = \
{'console_scripts': ['dj = dj.__main__:main',
                     'djonfig = dj.__main__:generate_config_file']}

setup_kwargs = {
    'name': 'djplus',
    'version': '3.0.0',
    'description': 'A collection of Django apps',
    'long_description': '![djplus version](https://img.shields.io/pypi/v/djplus?style=flat-square)\n![django version](https://img.shields.io/pypi/djversions/djplus?style=flat-square)\n![python version](https://img.shields.io/pypi/pyversions/djplus?style=flat-square)\n![license](https://img.shields.io/pypi/l/djplus?color=blue&style=flat-square)\n\n# Why does this package exist?\nBecause 80% of customer projects have common apps \nsuch as authentication, store, admin, blog, forum, academy, etc. \nTherefore, as freelancers, we decided to code all these apps only once in one place \nand use them in different projects as often as desired, \nand all these apps can be customized by the settings of each project.\nThis helps to save our time and increase our income in exchange for doing projects.\n\n# Installing\nYou can use pip to install `djplus` for usage:\n```shell\npip install djplus\n```\n\n# Usage\n## Create Project\nSimple command line for jumpstarting production-ready Django projects:\n```shell\ndj\n```\nor\n```shell\npython -m dj\n```\n\n## Auth\n\n```python\n#settings.py\n\nINSTALLED_APPS = [\n    # ...\n    "dj.auth", \n    # ...\n]\n\nMIDDLEWARE = [\n    # ...\n    \'dj.auth.middleware.AuthenticationMiddleware\',\n    # ...\n]\n```\n```python\n# urls.py\n\nurlpatterns = [\n    # ...\n    path("auth/", include("dj.auth.urls", namespace="auth")),\n    # ...\n]\n```\n## Blog\n```python\n#settings.py\n\nINSTALLED_APPS = [\n    # ...\n    "dj.blog", \n    # ...\n]\n```\n```python\n# urls.py \n\nurlpatterns = [\n    # ...\n    path("blog/", include("dj.blog.urls", namespace="blog")),\n    # ...\n]\n```\n# Contributing\nContributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.\n\nIf you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".\nDon\'t forget to give the project a star! Thanks again!\n\n1. Fork the Project\n2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some AmazingFeature\'`)\n4. Push to the Branch (`git push origin feature/AmazingFeature`)\n5. Open a Pull Request\n',
    'author': 'githashem',
    'author_email': 'PersonalHashem@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/githashem/dj',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
