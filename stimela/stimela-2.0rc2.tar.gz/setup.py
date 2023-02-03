# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'tests', 'scabha_tests': 'tests/scabha_tests'}

packages = \
['scabha',
 'scabha.configuratt',
 'scabha_tests',
 'stimela',
 'stimela.backends',
 'stimela.backends.flavours',
 'stimela.backends.kubernetes',
 'stimela.backends.native',
 'stimela.cargo',
 'stimela.cargo.base',
 'stimela.commands',
 'stimela.kitchen',
 'stimela.schedulers',
 'stimela.utils',
 'stimela_tests']

package_data = \
{'': ['*'],
 'stimela.cargo': ['cab/*', 'lib/params/*'],
 'stimela.cargo.base': ['21cmfast/*',
                        'aegean/*',
                        'aimfast/*',
                        'aoflagger/*',
                        'astropy/*',
                        'base/*',
                        'casa/*',
                        'casarest/*',
                        'catdagger/*',
                        'chgcentre/*',
                        'codex-africanus/*',
                        'cubical/*',
                        'cubical_ddf/*',
                        'curl/*',
                        'ddfacet/*',
                        'eidos/*',
                        'katdal/*',
                        'lofar/*',
                        'meqtrees/*',
                        'montage/*',
                        'moresane/*',
                        'msutils/*',
                        'owlcat/*',
                        'politsiyakat/*',
                        'pybdsf/*',
                        'pyddi/*',
                        'quartical/*',
                        'ragavi/*',
                        'rfimasker/*',
                        'rfinder/*',
                        'sagecal/*',
                        'shadems/*',
                        'sharpener/*',
                        'sofia/*',
                        'sourcery/*',
                        'sunblocker/*',
                        'tigger/*',
                        'tricolour/*',
                        'wsclean/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'dill>=0.3.6,<0.4.0',
 'munch>=2.5.0,<3.0.0',
 'omegaconf>=2.1,<3.0',
 'psutil>=5.9.3,<6.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyparsing>=3.0.9,<4.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['stimela = stimela.main:cli']}

setup_kwargs = {
    'name': 'stimela',
    'version': '2.0rc2',
    'description': 'Framework for system agnostic pipelines for radio interferometry arrays',
    'long_description': '\n============\nstimela 2.0\n============\n\n\n|Pypi Version|\n|Python Versions|  \n\nA workflow management framework for radio interometry data processing pipelines.\n\n`Documentation Page <https://stimela.readthedocs.io/>`_  \n=========================================================================================\n\n\n\n.. |Pypi Version| image:: https://img.shields.io/pypi/v/stimela.svg\n                  :target: https://pypi.python.org/pypi/stimela\n                  :alt:\n\n\n.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/stimela.svg\n                     :target: https://pypi.python.org/pypi/stimela\n                     :alt:\n',
    'author': 'Sphesihle Makhathini',
    'author_email': 'sphemakh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
