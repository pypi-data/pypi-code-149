# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_mini']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=15.3.3,<16.0.0',
 'PyYAML>=6.0,<7.0',
 'allure-pytest>=2.11.1,<3.0.0',
 'allure-python-commons>=2.11.1,<3.0.0',
 'attrs>=22.1.0,<23.0.0',
 'certifi>=2022.9.24,<2023.0.0',
 'charset-normalizer>=3.0.1,<4.0.0',
 'concurrent-log-handler>=0.9.20,<0.10.0',
 'ddt>=1.6.0,<2.0.0',
 'exceptiongroup>=1.0.4,<2.0.0',
 'future>=0.18.2,<0.19.0',
 'idna>=3.4,<4.0',
 'iniconfig>=2.0.0,<3.0.0',
 'minium>=1.3.1,<2.0.0',
 'packaging>=23.0,<24.0',
 'pluggy>=1.0.0,<2.0.0',
 'portalocker>=2.6.0,<3.0.0',
 'pyee>=9.0.4,<10.0.0',
 'pyparsing>=3.0.9,<4.0.0',
 'pytest-assume>=2.4.3,<3.0.0',
 'pytest-dependency>=0.5.1,<0.6.0',
 'pytest-lazy-fixture>=0.6.3,<0.7.0',
 'pytest-ordering>=0.6,<0.7',
 'pytest>=7.2.0,<8.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'six>=1.16.0,<2.0.0',
 'tomli>=2.0.1,<3.0.0',
 'twine>=4.0.2,<5.0.0',
 'typing_extensions>=4.4.0,<5.0.0',
 'urllib3>=1.26.12,<2.0.0']

entry_points = \
{'pytest11': ['mini = pytest_mini.mini', 'mp = pytest_mini.plugin:Plugin']}

setup_kwargs = {
    'name': 'pytest-mini',
    'version': '0.1.4',
    'description': 'A plugin to test mp',
    'long_description': '# pytest-mini\n\n微信小程序自动化测试',
    'author': '听白',
    'author_email': '490336534@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
