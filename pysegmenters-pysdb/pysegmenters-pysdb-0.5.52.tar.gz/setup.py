#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['pysegmenters_pysdb']

package_data = \
{'': ['*']}

package_dir = \
{'': 'src'}

install_requires = \
['pymultirole-plugins>=0.5.0,<0.6.0', 'spacy==3.4.0', 'spacy[lookups]', 'pysbd']

extras_require = \
{'dev': ['flit', 'pre-commit', 'bump2version'],
 'docs': ['sphinx',
          'sphinx-rtd-theme',
          'm2r2',
          'sphinxcontrib.apidoc',
          'jupyter_sphinx'],
 'test': ['pytest',
          'pytest-cov',
          'pytest-flake8',
          'pytest-black',
          'flake8==3.9.2',
          'tox']}

entry_points = \
{'pysegmenters.plugins': ['pysdb = '
                          'pysegmenters_pysdb.pysdb_segmenter:PySDBSegmenter']}

setup(name='pysegmenters-pysdb',
      version='0.5.52',
      description='Rule-based segmenter',
      author='Olivier Terrier',
      author_email='olivier.terrier@kairntech.com',
      url='https://github.com/oterrier/pysegmenters_pysdb/',
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>=3.8',
     )
