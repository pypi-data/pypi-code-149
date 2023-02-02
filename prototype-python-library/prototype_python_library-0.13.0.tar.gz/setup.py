# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prototype_python_library']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'prototype-python-library',
    'version': '0.13.0',
    'description': 'A prototype python library.',
    'long_description': '# Python Package\n\n[![Cookiecutter](https://img.shields.io/badge/built%20with-Cookiecutter-ff69b4.svg?logo=cookiecutter)](https://github.com/91nunocosta/python-package-cookiecutter)\n\n[![GitHub](https://img.shields.io/github/license/91nunocosta/prototype-python-library)](https://github.com/91nunocosta/prototype-python-library/blob/master/LICENSE)\n\n[![Codacy](https://app.codacy.com/project/badge/Grade/cb92f3f137454fae8697c7a6e7334f74)](https://www.codacy.com/gh/91nunocosta/prototype-python-library/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=91nunocosta/prototype-python-library&amp;utm_campaign=Badge_Grade)\n\n[![Codacy coverage](https://app.codacy.com/project/badge/Coverage/cb92f3f137454fae8697c7a6e7334f74)](https://www.codacy.com/gh/91nunocosta/prototype-python-library/dashboard?utm_source=github.com&utm_medium=referral&utm_content=91nunocosta/prototype-python-library&utm_campaign=Badge_Coverage)\n\n[![Build](https://img.shields.io/github/workflow/status/91nunocosta/prototype-python-library/Semantic%20Release)](https://github.com/91nunocosta/prototype-python-library/actions/workflows/release_package.yml)\n\n[![Python versions](https://img.shields.io/pypi/v/prototype-python-library)](https://pypi.org/project/prototype-python-library/)\n\n[![PyPI version](https://img.shields.io/pypi/pyversions/prototype-python-library)](https://pypi.org/project/prototype-python-library/)\n\nAn empty python package.\n\n## Installation\n\n```bash\npip install prototype-python-library\n```\n\n## Usage\n\n```python\n   >>> from prototype_python_library\n   >>> import fib\n   >>> fib(0)\n   ... 0\n```\n\nFor more details read the\n[documentation](https://91nunocosta.github.io/prototype-python-library/prototype_python_library.html).\n\n## Contributing\n\nIf you want to contribute, please read the [contributing guidelines](./CONTRIBUTING.md)\nand [code of conduct](./CODE_OF_CONDUCT.md).\n',
    'author': 'Nuno Costa',
    'author_email': '91nunocosta@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/91nunocosta/prototype-python-library/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
