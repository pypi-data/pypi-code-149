# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fabproj_manager', 'fabproj_manager.modules']

package_data = \
{'': ['*'], 'fabproj_manager.modules': ['img/*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'nbformat>=5.7.3,<6.0.0']

entry_points = \
{'console_scripts': ['fabproj = fabproj_manager.fabproj:create_project']}

setup_kwargs = {
    'name': 'fabproj-manager',
    'version': '0.1.5',
    'description': '',
    'long_description': '# fabproj-manager\nA CLI to help create new fabric project templates in an effort to standardize experiment structure.\n\n## Usage\n`fabproj --add --name --local <fabric project name>`\n- Replace <fabric project name> with a desired name\n- `--add`: required to add project\n- `--name`: optional, default is myProj\n- `--local`: only include if you will be running scripts on local machine as well; creates another folder for these.\nOnce you run the above command, you should see a new set of folders that serve as a template\nfor your fabric project.',
    'author': 'Devin Lane',
    'author_email': 'silvertenor@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
