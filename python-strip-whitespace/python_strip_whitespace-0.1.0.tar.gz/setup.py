# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_strip_whitespace',
 'python_strip_whitespace.functions',
 'python_strip_whitespace.functions.regex_patterns',
 'python_strip_whitespace.html']

package_data = \
{'': ['*']}

install_requires = \
['minify-html>=0.10.8,<0.11.0']

setup_kwargs = {
    'name': 'python-strip-whitespace',
    'version': '0.1.0',
    'description': 'A powerful HTML whitespace remover for python',
    'long_description': 'HTML Whitespace remover for Python\n==================================\n|Pepy.tech Badge| |PyPi Version Badge| |Python Versions Badge| |License Badge| |Code Style| |Lines of Code Badge|\n\n.. |Pepy.tech Badge| image:: https://static.pepy.tech/personalized-badge/python-strip-whitespace?period=week&units=international_system&left_color=grey&right_color=orange&left_text=Downloads\n   :target: https://pepy.tech/project/python-strip-whitespace\n\n.. |PyPi Version Badge| image:: https://badge.fury.io/py/python-strip-whitespace.svg\n    :target: https://badge.fury.io/py/python-strip-whitespace\n\n.. |Python Versions Badge| image:: https://img.shields.io/pypi/pyversions/python-strip-whitespace\n    :alt: PyPI - Python Version\n    :target: https://github.com/baseplate-admin/python_strip_whitespace/blob/main/setup.py\n\n.. |License Badge| image:: https://img.shields.io/pypi/l/python-strip-whitespace\n   :alt: PyPI - License\n   :target: https://github.com/baseplate-admin/python_strip_whitespace/blob/main/LICENSE\n   \n.. |Code Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :alt: Code Style\n   \n.. |Lines of Code Badge| image:: https://tokei.rs/b1/github/baseplate-admin/python_strip_whitespace\n   :alt: Lines of Code\n   :target: https://github.com/baseplate-admin/python_strip_whitespace\n   \nIntroduction :\n--------------\nA powerful tool to optimize HTML\n\nWhy use "python_stip_whitespace" ?\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n*   Adds line break to InlineJS.\n*   It can automagically minify inline CSS, JS.\n*   Removes <!--prettier-ignore--> from HTML.\n*   It speeds up website by reducing the HTML size.\n*   It compiles regex at runtime. So it\'s blazing fast.\n*   Its mostly based on C ( gzip ) and Rust ( `minify-html <https://pypi.org/project/minify-html/>`__  ) libraries.\n*   Significantly lower bytes transferred when working with frameworks like AlpineJs ( Almost fully working & Please open a issue in the `Issue Tracker <https://github.com/baseplate-admin/python_strip_whitespace/issues>`__ if you encounter any bug ) & Petite Vue.\n*   Is very customizable. ( You can configure lower level `minify-html <https://github.com/wilsonzlin/minify-html/blob/master/python/src/lib.template.rs/>`_ rust bindings and also the lower level `python <https://github.com/juancarlospaco/css-html-js-minify/blob/master/css_html_js_minify/html_minifier.py/>`_ bindings when calling minify  )\n\n\nWhy shouldn\'t you use python_stip_whitespace ?\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n*   Adds unnecessary \';;\' in HTML. ( If you know any regex to fix this please put a pull request )\n\n\nRequirements :\n--------------\n\n*    `minify-html <https://github.com/wilsonzlin/minify-html>`_ \n*    Python 3 ( Should work with all version? )\n*    `Brotli <https://pypi.org/project/Brotli/>`_ ( or `BrotliPy <https://pypi.org/project/brotlipy/>`_ ) | ( Optional )\n*    `ZSTD <https://pypi.org/project/zstandard/>`_ ( Optional ) ``Isn\'t supperted by modern browsers``\n\nUsed Internally by :\n====================\n*     `django-strip-whitespace <https://github.com/baseplate-admin/django_strip_whitespace>`_ \n*     `flask-strip-whitespace <https://github.com/baseplate-admin/flask_strip_whitespace>`_ \n*     `fastapi-strip-whitespace <https://github.com/baseplate-admin/fastapi_strip_whitespace>`_ ( Doesn\'t exist  😛 )\n\nContributing :\n==============\nIf you like this project add a star. \nIf you have problems or suggestions please put them in the `Issue Tracker <https://github.com/baseplate-admin/python_strip_whitespace/issues>`__.\nIf you like to add features. Fork this repo and submit a Pull Request. 😛\n\nRoadmap :\n=========\nYou tell me. If i have free time, I will implement it.\n',
    'author': 'baseplate-admin',
    'author_email': '61817579+baseplate-admin@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
