# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trill', 'trill.utils']

package_data = \
{'': ['*'], 'trill': ['data/*']}

install_requires = \
['GitPython>=3.1.29,<4.0.0',
 'accelerate>=0.16.0,<0.17.0',
 'biotite>=0.35.0,<0.36.0',
 'datasets>=2.7.1,<3.0.0',
 'deepspeed>=0.7.6,<0.8.0',
 'fair-esm>=2.0.0,<3.0.0',
 'fairscale>=0.4.13,<0.5.0',
 'pandas>=1.5.2,<2.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'pytest>=7.2.0,<8.0.0',
 'pytorch-lightning>=1.9.0,<2.0.0',
 'transformers>=4.25.1,<5.0.0']

entry_points = \
{'console_scripts': ['trill = trill.trill_main:cli']}

setup_kwargs = {
    'name': 'trill-proteins',
    'version': '0.4.0',
    'description': 'Sandbox (in progress) for Computational Protein Design',
    'long_description': '                              _____________________.___.____    .____     \n                              \\__    ___/\\______   \\   |    |   |    |    \n                                |    |    |       _/   |    |   |    |    \n                                |    |    |    |   \\   |    |___|    |___ \n                                |____|    |____|_  /___|_______ \\_______ \\\n                                                 \\/            \\/       \\/\n\n[![pypi version](https://img.shields.io/pypi/v/trill-proteins)](https://pypi.org/project/trill-proteins)\n![status](https://github.com/martinez-zacharya/TRILL/workflows/CI/badge.svg)\n# TRILL\n**TR**aining and **I**nference using the **L**anguage of **L**ife is a sandbox for creative protein engineering and discovery. As a bioengineer myself, deep-learning based approaches for protein design and analysis are of great interest to me. However, many of these deep-learning models are rather unwieldy, especially for non ML-practitioners, due to their sheer size. Not only does TRILL allow researchers to perform inference on their proteins of interest using a variety of models, but it also democratizes the efficient fine-tuning of large-language models. Whether using Google Colab with one GPU or a supercomputer with many, TRILL empowers scientists to leverage models with millions to billions of parameters without worrying (too much) about hardware constraints. Currently, TRILL supports using these models as of v0.4.0:\n- ESM2 (All sizes, depending on hardware constraints)\n- ESM-IF1 (Generate synthetic proteins using Inverse-Folding)\n- ESMFold (Predict 3D protein structure)\n- ProtGPT2 (Generate synthetic proteins)\n\n## Documentation\nCheck out the documentation and examples at https://trill.readthedocs.io/en/latest/home.html\n',
    'author': 'Zachary Martinez',
    'author_email': 'martinez.zacharya@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/martinez-zacharya/TRILL',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
