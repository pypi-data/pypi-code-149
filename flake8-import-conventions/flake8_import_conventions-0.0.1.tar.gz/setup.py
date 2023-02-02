# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_import_conventions']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.2.0,<23.0.0', 'flake8>=5']

entry_points = \
{'flake8.extension': ['IC = flake8_import_conventions:Plugin']}

setup_kwargs = {
    'name': 'flake8-import-conventions',
    'version': '0.0.1',
    'description': 'An opinionated plugin for Flake8 on how certain packages should be imported or aliased.',
    'long_description': '# flake8-import-conventions\n\nAn opinionated plugin for Flake8 on how certain packages should be imported or aliased.\n\nIt is based on the [`pandas-vet`](https://github.com/deppen8/pandas-vet) and [`flake8-2020`](https://github.com/asottile/flake8-2020) plugins.\n\n## Development\n\n```bash\npoetry install --with dev\n```\n\n```bash\npoetry shell\n```\n\nOpen the `manual_test.py` file in VS Code to see the error messages.\n\n```bash\npytest tests/ -v\n```\n\nor (to see `print()`s)\n\n```bash\npytest tests/ -v -s\n```\n\n## Deployment\n\n```bash\npoetry check\n```\n\n```bash\npoetry version minor\n```\n\nor\n\n```bash\npoetry version patch\n```\n\n```bash\ngit tag\n```\n\n```bash\ngit tag "v$(poetry version --short)"\n```\n\n```bash\ngit push origin "v$(poetry version --short)"\n```\n\n## References\n\n- Anthony Sottile\'s "[a flake8 plugin from scratch (intermediate) anthony explains #025](https://youtu.be/ot5Z4KQPBL8)" tutorial.\n- [flake8-pie](https://github.com/sbdchd/flake8-pie).\n- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide).\n\n## Notes\n\n- [flake8-class-attributes-order](https://github.com/best-doctor/flake8-class-attributes-order).\n- [astpretty](https://github.com/asottile/astpretty).\n- [babi](https://github.com/asottile/babi) (text editor).\n- `self.generic_visit(node)`: call it at the end of each `visit_*` method for the recursion to continue.\n- [attrs](https://www.attrs.org/):\n  - "Classes without boilerplate".\n  - No need to implement object protocols (dunder methods).\n  - "It does _nothing_ dynamic at runtime, hence zero runtime overhead."\n  - `__attrs_post_init__` method.\n- [Dict vs. slotted classes](https://www.attrs.org/en/stable/glossary.html).\n- `poetry add flake8@^3.0.0 attrs`.\n- `flake8 formatter.py flake8_import_conventions --jobs 1`.\n- `poetry install --no-root` (don\'t install _this_ package).\n- `import typing as t` ([flake8-annotations](https://github.com/sco1/flake8-annotations)).\n- `import geopandas` ([source](https://github.com/geopandas/geopandas/issues/716)).\n- https://github.com/asottile/flake8-2020/commit/10ba36520cca00ecbc812b2b96fcaaf9f8999c06\n- Poetry:\n  - https://python-poetry.org/docs/#installing-with-the-official-installer\n  - `poetry --version` (1.3.2)\n  - `poetry init` (https://python-poetry.org/docs/basic-usage/#initialising-a-pre-existing-project)\n  - https://python-poetry.org/docs/dependency-specification/#exact-requirements\n  - `poetry add attrs`\n  - `poetry add mypy black bandit pytest --group dev`\n  - `poetry add isort@^5.11.5 --group dev` or `poetry add isort --group dev --allow-prereleases` (https://github.com/PyCQA/isort/issues/2084 + https://pypi.org/project/isort/6.0.0b2/#history + https://github.com/PyCQA/isort/issues/2083)\n  - `flake8 = ">=5"` (https://github.com/asottile/flake8-2020/blob/v1.7.0/setup.cfg#L25)\n  - https://python-poetry.org/docs/cli/#add (_Allow >=2.0.5 versions, without upper bound_)\n  - `poetry config virtualenvs.in-project true --local`\n  - `poetry env remove --all`\n  - `poetry config --list`\n- https://www.attrs.org/en/latest/index.html#getting-started\n- Delete local tag: `git tag -d v0.0.1`\n\n**Minimal boilerplate for the `Plugin` class**:\n\n```python\nimport ast\nimport importlib.metadata\nfrom typing import Any, Generator, Tuple, Type\n\n\nclass Plugin:\n    name = __name__\n    version = importlib.metadata.version(__name__)\n\n    def __init__(self, tree: ast.AST) -> None:\n        # The AST that represents a single file\n        self._tree = tree\n\n    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:\n        # Tuple[line number, character offset, message]\n        # Type[Any] is not being used (use `type(self)`)\n        pass\n```\n\n**Syntactic sugar for `attr.ib(default=attr.Factory(f))`**:\n\n```python\n@attr.s\nclass C(object):\n    x = attr.ib(factory=list)\n    # instead of\n    # x = attr.ib(default=attr.Factory(list))\n```\n',
    'author': 'João Palmeiro',
    'author_email': 'joaopalmeiro@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
