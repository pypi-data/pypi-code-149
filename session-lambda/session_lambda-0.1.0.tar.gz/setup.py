# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['session_lambda', 'session_lambda.store']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.60,<2.0.0']

setup_kwargs = {
    'name': 'session-lambda',
    'version': '0.1.0',
    'description': 'A session manager for aws lambda function using dynamodb',
    'long_description': '',
    'author': 'Roy Pasternak',
    'author_email': 'roy.pasternakk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
