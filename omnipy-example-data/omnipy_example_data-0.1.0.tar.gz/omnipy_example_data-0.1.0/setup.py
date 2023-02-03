# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omnipy_example_data']

package_data = \
{'': ['*'], 'omnipy_example_data': ['bif/*', 'gff/*', 'isa-json/*']}

setup_kwargs = {
    'name': 'omnipy-example-data',
    'version': '0.1.0',
    'description': 'Example data files for use in the `omnipy_examples` package',
    'long_description': '# omnipy_example_data\n\nExample data files for use in the `omnipy_examples` package. \nLicense info available under each subdirectory.',
    'author': 'Sveinung Gundersen',
    'author_email': 'sveinugu@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
