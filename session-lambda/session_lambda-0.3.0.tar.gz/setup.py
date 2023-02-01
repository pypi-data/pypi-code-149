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
    'version': '0.3.0',
    'description': 'A simple session manager for aws lambda function using dynamodb',
    'long_description': '# Session Lambda\nA simple way to manage sessions for AWS Lambdas\n\n## Install\n```\npip install session-lambda\n```\n\n## Example\nSet `SESSION_LAMBDA_DYNAMODB_TABLE_NAME` env var:\n```\nexport SESSION_LAMBDA_DYNAMODB_TABLE_NAME=<table-name>\n```\nRun the following python code:\n```\nimport time\nfrom session_lambda import session, set_session_data, get_session_data\n\n@session\ndef lambda_handler(event, context):\n    print(get_session_data())\n    set_session_data((get_session_data() or [])+[str(time.time())])\n    return {"headers":{}}\n\n# first client_a call \nresponse = lambda_handler({\'headers\':{}}, {})  \n# get session id from response (created by the server)\nsession_id = response.get(\'headers\').get(\'session-id\')\n# use session id in subsequent calls\nlambda_handler({\'headers\':{\'session-id\':session_id}}, {})\nlambda_handler({\'headers\':{\'session-id\':session_id}}, {})\nlambda_handler({\'headers\':{\'session-id\':session_id}}, {})\n\n# first client_b call \nlambda_handler({\'headers\':{}}, {})\n```\nYou should get the following prints:\n```\nNone\n[\'1675291378.118798\']\n[\'1675291378.118798\']\n[\'1675291378.118798\']\nNone\n```\nThis time using the `update=True` mode:\n```\nimport time\nfrom session_lambda import session, set_session_data, get_session_data\n\n@session(update=True)\ndef lambda_handler(event, context):\n    print(get_session_data())\n    set_session_data((get_session_data() or [])+[str(time.time())])\n    return {"headers":{}}\n\n# first client_a call \nresponse = lambda_handler({\'headers\':{}}, {})  \n# get session id from response (created by the server)\nsession_id = response.get(\'headers\').get(\'session-id\')\n# use session id in subsequent calls\nlambda_handler({\'headers\':{\'session-id\':session_id}}, {})\nlambda_handler({\'headers\':{\'session-id\':session_id}}, {})\nlambda_handler({\'headers\':{\'session-id\':session_id}}, {})\n\n# first client_b call \nlambda_handler({\'headers\':{}}, {})\n```\nNow you should see:\n```\nNone\n[\'1675291406.785664\']\n[\'1675291406.785664\', \'1675291407.565578\']\n[\'1675291406.785664\', \'1675291407.565578\', \'1675291408.384397\']\nNone\n```\n\n## Features\n```\n@session(id_key_name=\'session-id\', update=False, ttl=0)\ndef lambda_handler(event, context):\n    ...\n```\n- `id_key_name` is the expected key name in the `event[headers]`. It is default to `session-id`. It is case-sensitive.\n- `update` flag let you decide weather to update the session data each call or just not. It is default to `False`.\n- `ttl` is seconds interval for the session to live (since the last update time). By default it is disabled. Any value larger then 0 will enable this feature. Make sure to set the TTL key name in your dynamodb to `ttl`.\n\n## Future Features\n- Support Schema validation for session data',
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
