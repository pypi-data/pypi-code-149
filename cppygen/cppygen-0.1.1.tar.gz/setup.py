# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cppygen']

package_data = \
{'': ['*']}

install_requires = \
['clang>=14.0,<15.0',
 'coloredlog>=0.2.5,<0.3.0',
 'pytest>=7.1.3,<8.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['cppygen = cppygen.__main__:run']}

setup_kwargs = {
    'name': 'cppygen',
    'version': '0.1.1',
    'description': 'A simple c++ code generator for pybind11',
    'long_description': '# CPPYGEN\n\nAutomatic code generation for pybind11.\n\nPybind11 is a powerful library that exposes C++ types in Python and vice versa, \n\nThis generator will be generate c++ code for pybind11, and make it easy to\nwrite a python module using c++.\n\n## Installation\n```\npip install cppygen\n```\n\n## Env\n\n```bash\nPYGEN_LIBCLANG_PATH # Path to clang shared library\nPYGEN_COMPILE_FLAGS # additional flags to parse file\n```\n',
    'author': 'Gen740',
    'author_email': 'keener_slimier_0m@icloud.com',
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
