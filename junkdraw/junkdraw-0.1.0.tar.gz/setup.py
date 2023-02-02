# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['junkdraw']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['junkdraw = junkdraw.run:main']}

setup_kwargs = {
    'name': 'junkdraw',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Junkdraw\n\nEasily create large numbers of arbitrary-sized random files.\n\nUsage:\n\n```shell\njunkdraw <options>\n```\n\noptions:\n\n- `--path`: Path to save the generated files (default: `./junkdrawer/<desc>`)\n- `--size`: Size of the generated file in bytes (default: 0)\n- `--min-size`: Minimum size of the generated file in bytes\n- `--max-size`: Maximum size of the generated file in bytes\n- `--count`: Number of files to generate (default: 1)\n- `--total-size`: Cumulative size of all files generated in bytes\n- `--max-children`: Create no more than this many files or directories in any one directory (default: no limit)\n- `--random`: Fill files with random data (default: leave empty)\n',
    'author': 'Hugh Wimberly',
    'author_email': 'hugh.wimberly@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
