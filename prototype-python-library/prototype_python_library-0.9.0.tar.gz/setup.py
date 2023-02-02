# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prototype_python_library']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'prototype-python-library',
    'version': '0.9.0',
    'description': 'A prototype python library.',
    'long_description': 'Python Package\n==============\n\n.. image:: https://img.shields.io/badge/built%20with-Cookiecutter-ff69b4.svg?logo=cookiecutter\n    :alt: Cookiecutter\n    :target: https://github.com/91nunocosta/python-package-cookiecutter\n\n.. image:: https://img.shields.io/github/license/91nunocosta/prototype-python-library\n    :alt: GitHub\n    :target: https://github.com/91nunocosta/prototype-python-library/blob/master/LICENSE\n\n.. image:: https://app.codacy.com/project/badge/Grade/cb92f3f137454fae8697c7a6e7334f74\n    :alt: Codacy\n    :target: https://www.codacy.com/gh/91nunocosta/prototype-python-library/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=91nunocosta/prototype-python-library&amp;utm_campaign=Badge_Grade\n\n.. image:: https://app.codacy.com/project/badge/Coverage/cb92f3f137454fae8697c7a6e7334f74\n    :alt: Codacy coverage\n    :target: https://www.codacy.com/gh/91nunocosta/prototype-python-library/dashboard?utm_source=github.com&utm_medium=referral&utm_content=91nunocosta/prototype-python-library&utm_campaign=Badge_Coverage\n\n.. image:: https://img.shields.io/github/workflow/status/91nunocosta/prototype-python-library/Semantic%20Release\n    :alt: Build\n    :target: https://github.com/91nunocosta/prototype-python-library/actions/workflows/release_package.yml\n\n.. image:: https://img.shields.io/pypi/v/prototype-python-library\n    :alt: Python versions\n    :target: https://pypi.org/project/prototype-python-library/\n\n.. image:: https://img.shields.io/pypi/pyversions/prototype-python-library\n    :alt: PyPI version\n    :target: https://pypi.org/project/prototype-python-library/\n\n.. image:: https://readthedocs.org/projects/prototype-python-package/badge/?version=latest\n    :alt: ReadTheDocs\n    :target: https://prototype-python-package.readthedocs.io/en/latest/\n\nAn empty python package.\n\nInstallation\n------------\n\n.. code-block:: console\n\n    pip install prototype-python-library\n\nUsage\n-----\n\n>>> from prototype_python_library import fib\n>>> fib(0)\n0\n\n\nFor more details read the `documentation <https://prototype-python-package.readthedocs.io/en/latest/>`_.\n\nContributing\n------------\n\nIf you want to contribute, please read the `contributing guidelines <./CONTRIBUTING.md>`_ and `code of conduct <./CODE_OF_CONDUCT.md>`_.\n',
    'author': 'Nuno Costa',
    'author_email': '91nunocosta@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/91nunocosta/prototype-python-library/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
