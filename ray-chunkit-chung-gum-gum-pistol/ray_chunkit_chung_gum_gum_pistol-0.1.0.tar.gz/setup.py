# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ray_chunkit_chung_gum_gum_pistol']

package_data = \
{'': ['*']}

install_requires = \
['pytest[all]>=7.2.1,<8.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['gum = ray_chunkit_chung_gum_gum_pistol.main:app']}

setup_kwargs = {
    'name': 'ray-chunkit-chung-gum-gum-pistol',
    'version': '0.1.0',
    'description': '',
    'long_description': '# essential poetry\n\n<https://typer.tiangolo.com/tutorial/package/>\n\n## Step 1 Init project and dependencies\n\n```bash\npoetry new ray-chunkit-chung-gum-gum-pistol\ncd ray-chunkit-chung-gum-gum-pistol\npoetry add typer[all]\npoetry add pytest[all]\n```\n\n## Step 2 Define app\n\nDefine app path\n\n```toml\n[tool.poetry.scripts]\ngum = "ray_chunkit_chung_gum_gum_pistol.main:app"\n```\n\nInstall local\n\n```bash\npoetry install\n```\n\nTry app local\n\n```bash\ngum --help\ngum load\ngum shoot\n```\n\n## Step 2 Distribute app\n\nBuild wheel file\n\n```bash\npoetry build\n```\n\nTest by changing to a new venv and execute\n\n```bash\npip install ray-chunkit-chung-gum-gum-pistol\\dist\\ray_chunkit_chung_gum_gum_pistol-0.1.0-py3-none-any.whl\n```\n\n## Step 3 Upload to pypi\n\nCreate PYPI_TOKEN and export to env. Then config pypi-token in poetry\n\n```bash\npoetry config pypi-token.pypi $PYPI_TOKEN\n```\n',
    'author': 'ray-chunkit-chung',
    'author_email': 'ray.chunkit.chung@gmail.com',
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
