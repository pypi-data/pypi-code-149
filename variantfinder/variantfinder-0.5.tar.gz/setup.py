# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['variantfinder',
 'variantfinder.ParseAlignments',
 'variantfinder.ReadFiles',
 'variantfinder.WriteFiles']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20.3,<2.0.0', 'pysam>=0.19.0,<0.20.0', 'tqdm>=4.61,<5.0']

entry_points = \
{'console_scripts': ['variantfinder = variantfinder.__main__:main']}

setup_kwargs = {
    'name': 'variantfinder',
    'version': '0.5',
    'description': 'python package to scan bam files for alignemnts variants of interest',
    'long_description': None,
    'author': 'StephanHolgerD',
    'author_email': 'stephdruk@googlemail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
