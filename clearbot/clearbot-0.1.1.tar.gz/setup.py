# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['main']
install_requires = \
['pillow>=9.4.0,<10.0.0', 'requests>=2.28.2,<3.0.0', 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['clearbot = main:cli']}

setup_kwargs = {
    'name': 'clearbot',
    'version': '0.1.1',
    'description': 'Clearbit Logo API client',
    'long_description': "# clearbot\n\nClearbit Logo API client.\n\n`clearbot` fetches the logo of company (png file) based on their domain name.\n\n## Install\n\nThe script in available through a python package.\n\n```shell\npip install clearbot\n```\n\n## Get started\n\nYou can run directly the script on a domain.\n\n```shell\nclearbot github.com\n```\n\nYou can pass several domains as well.\n\n```shell\nclearbot github.com gitlab.com\n```\n\nBy default it will output `/tmp/github.com.png`. You can change the destination directory with the `-o` option.\n\n```shell\nclearbot -o . github.com\n```\n\nBy default it outputs 512px png file (i.e. the greatest side has 512px). You can change it with the `-s` option.\n\n```shell\nclearbot -s 128 github.com\n```\n\nFinally sometimes we may want to remove the white background (transparence). For this purpose, you can use the `-t` options that thresholds the whites (it must between 0 and 255 as it is applied on a grayscale version of the image).\n\n```shell\nclearbot -t 250 github.com\n```\n\n## What's next?\n\n- Use a file as input\n- Colorize image\n",
    'author': 'Alban Siffer',
    'author_email': 'alban.siffer@irisa.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
