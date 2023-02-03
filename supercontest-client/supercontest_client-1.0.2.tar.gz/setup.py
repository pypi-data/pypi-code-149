# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['supercontest-client']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0,<1', 'requests>=2,<3']

setup_kwargs = {
    'name': 'supercontest-client',
    'version': '1.0.2',
    'description': 'Client for fetching supercontest data via graphql',
    'long_description': '# Supercontest Client\n\nI have chosen to enable GraphiQL on [southbaysupercontest](https://southbaysupercontest.com) because it is protected\nby auth and CSRF. It\'s a valuable tool for users. [You may explore the data here](https://southbaysupercontest.com/graphql).\n\nThere is a Python client to fetch your data programmatically, similar to gql. Simply\n`pip install supercontest-client` and then run a query like the following example:\n\n```python\nimport supercontest-client as sbsc\n\nquery = """\n{\n  users (filters: {email_confirmed_at_lt: "2019-10-01T00:00:00"}) {\n    edges {\n      node {\n        email\n        first_name\n      }\n    }\n  }\n}\n"""\n\ndata = sbsc.query(email=\'myemail@domain.com\',\n                          password=\'mypassword\',  # your pw is encrypted over https\n                          query=query)\n```\n\nOther heavy-handed solutions like Selenium also work. The endpoint simply requires\nauth and a CSRF token.\n',
    'author': 'Brian Mahlstedt',
    'author_email': 'brian.mahlstedt@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://southbaysupercontest.com/graphql',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
