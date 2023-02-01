# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kernel_sidecar']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'kernel-sidecar',
    'version': '0.1.0',
    'description': 'A sidecar ',
    'long_description': '# kernel-sidecar\nJupyter Kernel backend sidecar!\n',
    'author': 'Matt Kafonek',
    'author_email': 'matt.kafonek@noteable.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kafonek/kernel-sidecar',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
