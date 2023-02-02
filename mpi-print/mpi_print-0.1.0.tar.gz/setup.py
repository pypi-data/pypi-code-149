# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mpi_print']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mpi-print',
    'version': '0.1.0',
    'description': '<Enter a one-sentence description of this project here.>',
    'long_description': "*********\nmpi-print\n*********\n\nPrint statements from MPI programs can be confusing, as you do not now\nby which rank the output was produced. The import of\n\n.. code-block:: python\n\n    from mpi_print import print\n\noverloads the the builtin print function to first print the rank and\na timestamp. E.g.\n\n.. code-block:: python\n\n    from mpi_print import print, builtin_print\n    builtin_print('hello world.') # prints:\n    #   hello world.\n    print('hello world.') # prints:\n    #   MPI rank: 1 [timestamp: 2023-02-02 20:48:26.544420]\n    #   hello world.\n\n* Documentation: https://mpi_print.readthedocs.io\n",
    'author': 'Bert Tijskens',
    'author_email': 'engelbert.tijskens@uantwerpen.be',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/etijskens/mpi-print',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
