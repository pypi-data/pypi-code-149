# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pre_commit_update']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.29,<4.0.0', 'click>=8.1,<9.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['pre-commit-update = pre_commit_update.cli:cli']}

setup_kwargs = {
    'name': 'pre-commit-update',
    'version': '0.0.5',
    'description': 'Simple CLI tool to check and update pre-commit hooks.',
    'long_description': '# pre-commit-update\n\n![Version](https://img.shields.io/pypi/pyversions/pre-commit-update)\n![Downloads](https://pepy.tech/badge/pre-commit-update)\n![Formatter](https://img.shields.io/badge/code%20style-black-black)\n![License](https://img.shields.io/pypi/l/pre-commit-update)\n\n**pre-commit-update** is a simple CLI tool to check and update pre-commit hooks.\n\n## Table of contents\n\n1. [ Reasoning ](#reasoning)\n2. [ Installation ](#installation)\n3. [ Usage ](#usage)\n    1. [ Pipeline usage example ](#usage-pipeline)\n    2. [ pre-commit hook usage example ](#usage-hook)\n\n<a name="reasoning"></a>\n## 1. Reasoning\n\n`pre-commit` is a nice little tool that helps you polish your code before releasing it into the wild.\nIt is fairly easy to use. A single `pre-commit-config.yaml` file can hold multiple hooks (checks) that will go through\nyour code or repository and do certain checks. The trick is that file is static and once you pin your hook versions\nafter a while they get outdated.\n\n`pre-commit` has a CLI that helps with that by making use of `pre-commit autoupdate` command so the question is\nwhy the f* are you reading this?\n\n`pre-commit-update` was created mostly because there is no easy way to update your hooks by using\n`pre-commit autoupdate` and avoiding non-stable (alpha, beta, ...) hook versions. `pre-commit-update` comes\nwith a CLI that can be configured to solve that problem - along with other use cases.\n\nOther than that - I was bored ^^\n\n\n<a name="installation"></a>\n## 2. Installation\n\n`pre-commit-update` is available on PyPI:\n```console \n$ python -m pip install pre-commit-update\n```\nPython >= 3.7 is supported.\n\n*NOTE:* Please make sure that `git` is installed.\n\n\n<a name="usage"></a>\n## 3. Usage\n\n`pre-commit-update` CLI can be used as below:\n\n```console\nUsage: pre-commit-update [OPTIONS]\n\nOptions:\n  -d, --dry-run       Dry run only checks for the new versions\n  -a, --all-versions  Include the alpha/beta versions\n  -v, --verbose       Display the complete output\n  -e, --exclude TEXT  Exclude specific hook(s) by the `id` of a hook\n  -h, --help          Show this message and exit.\n```\n\nIf you want to just check for updates (without updating `pre-commit-config.yaml`), for example, you would use:\n```python\npre-commit-update -d\nOR\npre-commit-update --dry-run\n```\n\n<a name="usage-pipeline"></a>\n### Pipeline usage example\n#### GitLab job:\n\n```yaml\npre-commit-hooks-update:\n  stage: update\n  script:\n    # install git if not present in the image\n    - pip install pre-commit-update\n    - pre-commit-update --dry-run\n  except:\n    - main\n  when: manual\n  allow_failure: true\n```\n\n*NOTE*: This is just an example, feel free to do your own configuration\n\n<a name="usage-hook"></a>\n### pre-commit hook usage example\n\nYou can also use `pre-commit-update` as a hook in your `pre-commit` hooks:\n\n```yaml\n- repo: local\n  hooks:\n    - id: pre-commit-update\n      entry: pre-commit-update\n      language: python\n      name: pre-commit-update\n      pass_filenames: false\n      args: [--dry-run --exclude black --exclude isort]\n```\n',
    'author': 'Vojko Pribudić',
    'author_email': 'dmanthing@gmail.com',
    'maintainer': 'Vojko Pribudić',
    'maintainer_email': 'dmanthing@gmail.com',
    'url': 'https://gitlab.com/vojko.pribudic/pre-commit-update',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
