# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aidd_codebase',
 'aidd_codebase.data_utils',
 'aidd_codebase.datamodules',
 'aidd_codebase.framework',
 'aidd_codebase.new_project',
 'aidd_codebase.new_project.src',
 'aidd_codebase.utils']

package_data = \
{'': ['*'], 'aidd_codebase.new_project': ['conf/*']}

setup_kwargs = {
    'name': 'aidd-codebase',
    'version': '0.1.10',
    'description': 'High-level codebase for deep learning development in drug discovery.',
    'long_description': '# AIDD Codebase\n\n![PyPI](https://img.shields.io/pypi/v/aidd-codebase)\n![PyPI](https://img.shields.io/pypi/pyversions/aidd-codebase)\n![PyPI](https://img.shields.io/github/license/aidd-msca/aidd-codebase)\n[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jlyEd1yxhvFCN82YqEFI82q2n0k_y06F?usp=sharing)\n\nA high-level codebase for deep learning development in drug discovery applications using PyTorch-Lightning.\n\n## Dependencies\n\nThe codebase requires the following additional dependencies\n- CUDA >= 11.4\n- PyTorch >= 1.9\n- Pytorch-Lightning >= 1.5 \n- RDKit \n- Optionally supports: tensorboard and/or wandb\n\n\n## Installation\n\nThe codebase can be installed from PyPI using `pip`, or your package manager of choice, with\n\n```bash\n$ pip install aidd-codebase\n```\n\n## Usage\n\nThe codebase is designed to be used in a modular fashion. The main components are the `DataModule`, `Model`, and `Trainer` classes. The `DataModule` is responsible for loading and preprocessing data, the `Model` is responsible for defining the model architecture, and the `Trainer` is responsible for training the model. The `Trainer` is a subclass of `pytorch_lightning.Trainer` and can be used as such. The `DataModule` and `Model` classes are designed to be used with the `Trainer` class, but can be used independently if desired.\n\n### Starting a new project\n```bash\n$ python -m aidd_codebase.start_project name dir_path\n```\nThis will create a new project folder with the following structure:\n\n```\nname\n├── conf\n│   └── config.yaml\n├── src\n└── main.py\n```\n\nThe `conf` folder contains the configuration file for the project. The `src` folder contains the source code for the project. The `main.py` file is the entry point for the project.\n\n\n## Contributors\n\nAll fellows of the AIDD consortium have contributed to the packaged.\n\n## Code of Conduct\n\nEveryone interacting in the codebase, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).\n',
    'author': 'Peter Hartog',
    'author_email': 'peter.hartog@hotmail.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aidd-msca/aidd-codebase',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
