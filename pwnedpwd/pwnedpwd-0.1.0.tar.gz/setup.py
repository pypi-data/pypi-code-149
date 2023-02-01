# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pwnedpwd']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'pwnedpwd',
    'version': '0.1.0',
    'description': 'Pwned Passwords',
    'long_description': '# PwnedPwd\nHave my passwords been compromised?\n\n[![Latest\nVersion](https://img.shields.io/pypi/v/pwnedpwd.svg)](https://pypi.python.org/pypi/pwnedpwd)\n\n[![tests](https://github.com/ratoaq2/pwnedpwd/actions/workflows/test.yml/badge.svg)](https://github.com/ratoaq2/pwnedpwd/actions/workflows/test.yml)\n\n[![License](https://img.shields.io/github/license/ratoaq2/pwnedpwd.svg)](https://github.com/ratoaq2/pwnedpwd/blob/master/LICENSE)\n\n  - Project page  \n    <https://github.com/ratoaq2/pwnedpwd>\n\n## Info\n\n**PwnedPwd** is a tiny CLI tool which uses the **online** service [Pwned Passwords](https://haveibeenpwned.com/API/v3#PwnedPasswords) to check\nwhether a given password have been compromised in known data breaches. Credits to [Troy Hunt](https://www.troyhunt.com/) for hosting such service.\n\n\n## How it works?\n\nGiven the input password, this tool will\n- hash it using SHA-1 algorithm, resulting in a 40-characters hexadecimal string\n- Use the first 5 characters from the generated string to query the online service\n- The online service returns a list of all matching hashes for the given prefix\n- Verify if your SHA-1 hash is present in the response\n\nFor instance, given an input password `P@ssword`\n- SHA-1 hash is `9E7C97801CB4CCE87B6C02F98291A6420E6400AD`\n- The first 5 characters are `9E7C9`\n- We query the online service using `GET https://api.pwnedpasswords.com/range/9E7C9`\n- The online service returns a list of all matching hashes (777 hashes for this example):\n  ```\n  ...\n  77B1EE4BF1B49FEB288C7FC65EE604C0C54:24\n  780087028CF36AF6A5A1DCF096748FB7090:10\n  7801CB4CCE87B6C02F98291A6420E6400AD:10848\n  782545129CEA7F3BD1A076F25B94C064CFE:3\n  788872DE964354319100FCE0EF4DEA00311:4\n  ...\n  ```\n- We verify that `7801CB4CCE87B6C02F98291A6420E6400AD` is present and have `10848` occurrences in data breaches\n\n\n## About Pwned Passwords\n\nExtracted from their website:\n\n>> Pwned Passwords are more than half a billion passwords which have previously been exposed in data breaches. The service is detailed in the launch blog post then further expanded on with the release of version 2. The entire data set is both downloadable and searchable online via the Pwned Passwords page.\n>> In order to protect the value of the source password being searched for, Pwned Passwords also implements a k-Anonymity model that allows a password to be searched for by partial hash.\n\nDetailed information can be found\n- https://haveibeenpwned.com/API/v3#PwnedPasswords\n- https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/\n\n## Installation\n\n```bash\n$ [sudo] pip install pwnedpwd\n```\n\n## Usage\n\n```bash\n$ pwnedpwd\nPassword: ******\n[GOOD] Password is not present in any known data breach. (source https://haveibeenpwned.com/Passwords)\n```\n\n```bash\n$ pwnedpwd\nPassword: 12345\n[BAD] Password appeared 2570791 times in data breaches. (source https://haveibeenpwned.com/Passwords)\n```\n',
    'author': 'Rato',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ratoaq2/pwnedpwd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
