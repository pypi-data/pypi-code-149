# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ghome_foyer_api']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.51.1,<2.0.0', 'protobuf>=4.21.12,<5.0.0']

setup_kwargs = {
    'name': 'ghome-foyer-api',
    'version': '1.0.0',
    'description': 'Generated protobuf stubs for Google Home Foyer API',
    'long_description': '# Google Home Foyer API\n\nWith this package, multiple libraries can use Foyer API without having to deal with Protobuf version conflicts.\n\n- Only one version of stubs can be loaded by Protobuf at the same time even if stubs are coming from different libraries and modules have different names. Using this package ensures that only one version is installed at any given time.\n- The package defines dependencies on Protobuf and GRPC, ensuring compatibility of generated files.\n- Type hints are generated and exported as well.\n\n## Credits\n\nThe proto file is taken from [here](https://github.com/rithvikvibhu/GHLocalApi/issues/39).\nThanks [@rithvikvibhu](https://github.com/rithvikvibhu) for extracting it.\n',
    'author': 'Ruslan Sayfutdinov',
    'author_email': 'ruslan@sayfutdinov.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/KapJI/ghome-foyer-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
