# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hal9']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0', 'streamlit>=1.17.0,<2.0.0']

setup_kwargs = {
    'name': 'hal9',
    'version': '1.0.0',
    'description': '',
    'long_description': '# Hal9: Data apps powered by code and LLMs\n\n[![Hal9 PyPi Downloads](https://img.shields.io/pypi/dm/hal9?label=PyPI)](https://pypi.org/project/hal9/) [![Hal9 NPM Downloads](https://img.shields.io/npm/dm/hal9.svg?label=NPM)](https://www.npmjs.com/package/hal9)\n\nHal9 is a framework for building *interactive data apps*. It allows you to utilize your DS/ML code with minimal overhead, and frees you from having to worry about frontend web frameworks. Hal9 consists of the following components:\n\n- **LLM**: A text interface to design your app using large language models.\n<!-- - **Multi-Lingual**: Packages in R, Python (and more on the way!). -->\n\n## Getting started\n\nThe quickest place to test things out is this hosted demo: [hal9.com/new](https://hal9.com).\n <!-- Refer to the Docs at [hal9.com/docs](https://hal9.com/docs/). -->\n\n### Python\n\n```bash\npip install hal9\n```\n\n```python\nimport hal9 as h9\nh9.get_app("asks for your name and prints hello")\n```\n\n### R \n\nThe development version of the package can be installed via\n\n```r\nremotes::install_github("hal9ai/hal9", subdir = "r")\n\nlibrary(hal9)\nh9_start("asks for your name and prints hello")\n```\n\n<!-- ## Principles\n\n- Easy to get started. You don\'t need to read a book or build a reactive execution graph in your head\n before you can build a dashboard.\n- First-class multi-lingual support. Power your apps with Python, or R, or combine them, *natively*, without having\nto use interop tools such as reticulate or rpy2. Rust and TypeScript APIs are being developed next, with many more to come.\n- Respect code and reproducibility. While we make it easy to build apps, all artifacts should be in standard formats\nso that you can (if you\'d like) work with actual web designers on your team to fulfill corporate styling needs.\n- Seamless deployment from applications to production. -->\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
}


setup(**setup_kwargs)
