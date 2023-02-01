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
    'version': '0.1.1',
    'description': 'A simple session manager for aws lambda function using dynamodb',
    'long_description': '# Session Lambda\nA simple way to manage sessions for AWS Lambdas\n\n## Install\n```\npip install session-lambda\n```\n\n## Example\nSet `SESSION_LAMBDA_DYNAMODB_TABLE_NAME` env var:\n```\nexport SESSION_LAMBDA_DYNAMODB_TABLE_NAME=<table-name>\n```\nRun the following python code:\n```\nfrom session_lambda import session, set_session_data, get_session_data\n\n@session\ndef lambda_handler(event, context):\n    \n    session_data = get_session_data()\n\n    # core_logic(event, context, session_data)\n        \n    set_session_data(data="hello world")\n    \n    return {"session_data_before": session_data, "session_data_after": get_session_data()}\n    \n        \nprint(lambda_handler({\'headers\':{"session-id": "0"}}, {}))\nprint(lambda_handler({\'headers\':{"session-id": "0"}}, {}))\nprint(lambda_handler({\'headers\':{"session-id": "1"}}, {}))\n```\nYou should get the following prints:\n```\n{\'session_data_before\': None, \'session_data_after\': \'hello world\'}\n{\'session_data_before\': \'hello world\', \'session_data_after\': \'hello world\'}\n{\'session_data_before\': None, \'session_data_after\': \'hello world\'}\n```\n\n## Features\n```\n@session(id_key_name=\'session-id\', return_session_id_in_header=True, update=False)\ndef lambda_handler(event, context):\n    ...\n```\n- `id_key_name` is the expected key name in the `event[headers]`. It is default to `session-id`. It is case-sensitive.\n- `update` flag let you decide weather to update the session data each call or just not. It is default to `False`.\n- `return_session_id_in_header` flag lets you control is the `session-id` is added to the response\'s headers (if `headers` exists in response). It is default to `True`.\n\n## Future Features\n- Support TTL\n- Support Schema validation for session data',
    'author': 'Roy Pasternak',
    'author_email': 'roy.pasternakk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/roy-pstr/session-lambda',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
