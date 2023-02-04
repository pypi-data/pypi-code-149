# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['juftin_scripts']

package_data = \
{'': ['*']}

install_requires = \
['art>=5.7,<6.0',
 'click>=8.1.2,<9.0.0',
 'fsspec>=2023.1.0,<2024.0.0',
 'pandas>=1.5',
 'rich-click>=1.5.2,<2.0.0',
 'rich>=12.6.0,<13.0.0',
 'textual>=0.5.0,<0.6.0',
 'universal-pathlib>=0.0.21,<0.0.22']

extras_require = \
{'all': ['pyarrow>=10.0.0,<11.0.0',
         's3fs>=2023.1.0,<2024.0.0',
         'aiohttp>=3.8.3,<4.0.0',
         'requests>=2.28.2,<3.0.0',
         'gcsfs>=2023.1.0,<2024.0.0',
         'adlfs>=2023.1.0,<2024.0.0'],
 'fsspec': ['s3fs>=2023.1.0,<2024.0.0',
            'aiohttp>=3.8.3,<4.0.0',
            'requests>=2.28.2,<3.0.0',
            'gcsfs>=2023.1.0,<2024.0.0',
            'adlfs>=2023.1.0,<2024.0.0'],
 'parquet': ['pyarrow>=10.0.0,<11.0.0']}

entry_points = \
{'console_scripts': ['browse = juftin_scripts.code_browser:browse',
                     'juftin = juftin_scripts.__main__:cli']}

setup_kwargs = {
    'name': 'juftin-scripts',
    'version': '0.3.1',
    'description': 'Helpful Python scripts by @juftin',
    'long_description': '# juftin-scripts\n\nHelpful Python scripts by [@juftin](https://github.com/juftin)\n\n#### Check Out the [Docs](https://juftin.github.io/juftin-scripts/)\n\n___________\n___________\n\n<br/>\n\n<p align="center"><a href="https://github.com/juftin"><img src="https://raw.githubusercontent.com/juftin/juftin/main/static/juftin.png" width="120" height="120" alt="logo"></p>\n',
    'author': 'Justin Flannery',
    'author_email': 'juftin@juftin.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/juftin/juftin-scripts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
