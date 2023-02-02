# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['omnipy_examples']

package_data = \
{'': ['*']}

install_requires = \
['omnipy>=0.8.0,<0.9.0', 'typing-inspect>=0.8.0,<0.9.0']

setup_kwargs = {
    'name': 'omnipy-examples',
    'version': '0.1.2',
    'description': '',
    'long_description': '# omnipy-examples\n\n## Main installation instructions\n\n- Install Poetry:\n  - `curl -sSL https://install.python-poetry.org | python3 -`\n- Install Python 3.10 through e.g. Conda, or directly in your IDE:\n  - `conda create -env myenv python=3.10`\n  - `conda activate myenv`\n- Install dependencies:\n  - `poetry install --with dev --no-root`\n\n## For mypy support in PyCharm\n\n- In PyCharm, install "Mypy" plugin (not "Mypy (Official)")\n  - `which mypy` to get path to mypy binary\n  - In the PyCharm settings for the mypy plugin:\n    - Select the mypy binary \n    - Select `pyproject.toml` as the mypy config file\n\n## For automatic formatting and linting\n\nI have added my typical setup for automatic formatting and linting. The main alternative is to use black, which is easier to set up, but it does not have as many options. I am not fully happy with my config, but I at least like it better than black. \n\n- In PyCharm -> File Watchers:\n  - Click arrow down icon\n  - Select `watchers.xml`\n',
    'author': 'Sveinung Gundersen',
    'author_email': 'sveinugu@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
