# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['omnipy_examples', 'omnipy_examples.scripts']

package_data = \
{'': ['*']}

install_requires = \
['omnipy>=0.8.0,<0.9.0', 'typing-inspect>=0.8.0,<0.9.0']

entry_points = \
{'console_scripts': ['dagsim_example = '
                     'omnipy_examples.scripts.dagsim_example:main']}

setup_kwargs = {
    'name': 'omnipy-examples',
    'version': '0.1.4',
    'description': '',
    'long_description': '# omnipy-examples\n\nExample projects that that makes use of the omnipy package for type-driven, scalable and interoperable data wrangling!\n\n## Main installation instructions\n\n\n- Install dependencies\n  - `pip install`\n- Run example scripts\n  - `scripts/uniprot_example` or `python scripts/uniprot_example.py`\n- Output will appear in the `data` directory with a timestamp. \n  - It is recommended to install a file viewer that are capable of browsing tar.gz files. For instance, the "File Expander" plugin in PyCharm is \n    excellent for this\n\n### Development setup\n\n- Install Poetry:\n  - `curl -sSL https://install.python-poetry.org | python3 -`\n\n- Install dependencies:\n  - `poetry install --with dev`\n\n## For mypy support in PyCharm\n\n- In PyCharm, install "Mypy" plugin (not "Mypy (Official)")\n  - `which mypy` to get path to mypy binary\n  - In the PyCharm settings for the mypy plugin:\n    - Select the mypy binary \n    - Select `pyproject.toml` as the mypy config file\n\n## For automatic formatting and linting\n\nI have added my typical setup for automatic formatting and linting. The main alternative is to use black, which is easier to set up, but it does \nnot have as many options. I am not fully happy with my config, but I at least like it better than black. \n\n- In PyCharm -> File Watchers:\n  - Click arrow down icon\n  - Select `watchers.xml`\n',
    'author': 'Sveinung Gundersen',
    'author_email': 'sveinugu@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
