# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['alpha_kentaurus']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['alpha = alpha_kentaurus.main:main']}

setup_kwargs = {
    'name': 'alpha-kentaurus-macos',
    'version': '0.1.9',
    'description': "Ah ah ah, you didn't say the magic word",
    'long_description': "## Not what you're looking for\n![nope](http://www.quickmeme.com/img/18/1894ca69f1f5ce970323f815c551a1890cc1609c1e20a963d8f8cf1b20b64e03.jpg)  \n[Ah ah ah, you didn't say the magic word](https://www.youtube.com/watch?v=RfiQYRn7fBg)  \n\n",
    'author': 'nope',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.youtube.com/watch?v=RfiQYRn7fBg',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0',
}


setup(**setup_kwargs)
