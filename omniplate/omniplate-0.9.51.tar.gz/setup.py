# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['om_code', 'omniplate']

package_data = \
{'': ['*']}

install_requires = \
['gaussianprocessderivatives>=0.1.2',
 'matplotlib>=3.5.3',
 'numpy>=1.21.4',
 'openpyxl>=3.0.9',
 'pandas>=1.5.1',
 'scipy>=1.7.3',
 'seaborn>=0.11.2',
 'statsmodels>=0.13.1']

setup_kwargs = {
    'name': 'omniplate',
    'version': '0.9.51',
    'description': 'For analysing and meta-analysing plate-reader data',
    'long_description': 'A Python package for analysing data from plate-reader studies of growing biological cells. Users can correct for autofluorescence, determine growth rates and the amount of fluorescence per cell, and simultaneously analyse multiple experiments.\n',
    'author': 'Peter Swain',
    'author_email': 'peter.swain@ed.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://swainlab.bio.ed.ac.uk/software/omniplate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
