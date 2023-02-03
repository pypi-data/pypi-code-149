# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mscan', 'mscan.scanner']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.89.1,<0.90.0',
 'icmplib>=3.0.3,<4.0.0',
 'mac-vendor-lookup>=0.1.12,<0.2.0',
 'psutil>=5.9.4,<6.0.0',
 'uvicorn[standard]>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['mscan = mscan.main:main']}

setup_kwargs = {
    'name': 'modern-scan',
    'version': '0.1.5',
    'description': 'Modern network scanner',
    'long_description': '# Mscan\n\n<img with="150px" height="150px" src="https://user-images.githubusercontent.com/61390950/182006521-350c306a-2567-49eb-b77a-42224783768f.png">  \n\n## A modern network scanner\n## 🖥 User Interface\n![image](https://user-images.githubusercontent.com/61390950/182006567-5e5cfcbe-7549-4205-902e-54706d2c1793.png)\n\n## 💿 Installation\nInstall from pypi\n```\npip3 install --upgrade modern-scan\n```\nthen simply execute\n```mscan```\n\n## ✨ Features\n\n- 🕹 Simple and clear user interface\n- 🚀 Super fast\n- 🛠 More features in development\n',
    'author': 'thewh1teagle',
    'author_email': '61390950+thewh1teagle@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
