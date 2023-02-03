# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_aliases']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'poetry>=1.3.2,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['aliases = '
                               'poetry_aliases.plugin:PoetryAliasesPlugin']}

setup_kwargs = {
    'name': 'poetry-aliases',
    'version': '1.0.0',
    'description': '',
    'long_description': '# poetry-aliases\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry-aliases?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/poetry-aliases)\n[![PyPI](https://img.shields.io/pypi/v/poetry-aliases?logo=pypi&color=green&logoColor=white&style=for-the-badge)](https://pypi.org/project/poetry-aliases)\n[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/poetry-aliases?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/poetry-aliases/releases)\n[![PyPI - License](https://img.shields.io/pypi/l/poetry-aliases?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/poetry-aliases/blob/main/LICENSE)\n[![Code style: black](https://aegis.celsiusnarhwal.dev/badge/black?style=for-the-badge)](https://github.com/psf/black)\n\npoetry-aliases is a [Poetry](https://python-poetry.org/) plugin that enables the creation of aliases for Poetry \ncommands.\n\n## Installation\n\n```bash\npoetry self add poetry-aliases\n```\n\n## Usage\n\nFirst, add aliases via `poetry aliases`.\n\n```bash\npoetry aliases\n```\n\n`poetry aliases` will open a file in `$EDITOR` where you can view, add, and edit your aliases.\n\n```toml\n# Write each alias on a separate line, e.g.:\n\n# i = "install"\n# r = "remove"\n# dev = "add --group dev"\n# plugins = "self show plugins"\n\n# Aliases that are not strings or conflict with other Poetry commands will be ignored.\n\n# Save this file and close the editor when you\'re done.\n\ni = "install"\nr = "remove"\ndev = "add --group dev"\nplugins = "self show plugins"\n```\n\nYour aliases will be saved to Poetry\'s `config.toml` file.\n\nOnce your aliases have been saved, you can use them like any other Poetry command.\n\n```bash\npoetry i\n\n# Installing dependencies from lock file\n\npoetry r yapf\n\n# Package operations: 0 installs, 0 updates, 1 removal\n\n#  • Removing yapf (0.32.0)\n\n\npoetry dev black\n\n# Package operations: 3 installs, 0 updates, 0 removals\n\n#  • Installing mypy-extensions (0.4.3)\n#  • Installing pathspec (0.11.0)\n#  • Installing black (23.1.0)\n\n\npoetry plugins\n\n#  • poetry-aliases (1.0.0) Create aliases for Poetry commands\n#      1 application plugin\n#\n#      Dependencies\n#        - click (>=8.1.3,<9.0.0)\n#        - poetry (>=1.3.2,<2.0.0)\n```\n\n## License\n\npoetry-aliases is licensed under the [MIT License](LICENSE.md).',
    'author': 'celsius narhwal',
    'author_email': 'hello@celsiusnarhwal.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
