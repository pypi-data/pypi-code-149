# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['autonote']

package_data = \
{'': ['*'], 'autonote': ['templates/*']}

install_requires = \
['atlassian-python-api>=3.32.1,<4.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'notion-client>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'autonote',
    'version': '0.3.0',
    'description': 'Automate taking notes',
    'long_description': '# autonote\n\n## Description\n\n![](docs/diagram.drawio.svg)\n\nAutomate creating daily, weekly, monthly, and quarterly manual repetitive documents:\n\n1. Daily: daily journal, habit tracker\n1. Weekly: weekly report\n1. Monthly: monthly report\n1. Quarterly: quarterly review\n\n## Prerequisite\n\n1. Confluence API Token\n1. Notion Integration Token\n\n## Installation\n\n```\npip install autonote\n```\n\n## Usage\n\n### 1. Confluence\n\n#### 1.1. Create a confluence page\n\nCurrently only support pre-defined page. TODO: make it configurable\n\n1. Set environment variables:\n\n    ```\n    export CONFLUENCE_URL=https://xxx.atlassian.net\n    export CONFLUENCE_USERNAME=<yourname>@domain.com\n    export CONFLUENCE_PASSWORD=<TOKEN>\n    ```\n\n1. Run\n    ```python\n    from autonote.confluence import ConfluenceClient\n    from autonote.html import generate\n\n    content = generate()\n    client = ConfluenceClient()\n    client.create_page(\n        parent_page_id="<confluence_parent_page_id>",\n        title="title",\n        body=content,\n    )\n    ```\n\n    Generated Page:\n\n    <table><tr><td>\n    <img src="docs/confluence_page_0.png" width="200px" />\n    </td></tr></table>\n\n### 2. Notion\n\nPrerequisite: Set environemnt variable\n\n```\nexport NOTION_INTEGRATION_TOKEN=xxx\n```\n\n#### 2.1. Create a Notion page\n\n```python\nfrom autonote.notion import NotionClient\n\nclient = NotionClient()\nclient.create_page(\n    parent_page_id="<parent_page_id>",\n    title="title",\n    body="body",\n    override=True, # update if exists\n)\n```\n\nGenerated page:\n\n<table><tr><td>\n<img src="docs/notion_page_0.png" width="200px" />\n</td></tr></table>\n\n\n#### 2.2. Create Notion database page from a template\n\n```python\nfrom autonote.notion import NotionClient\n\nclient = NotionClient()\nclient.create_page_from_template(\n    template_id="<template_id>",\n    title="OKR 2023Q1",\n    override=True,\n)\n```\n\nTemplate page:\n\n<table><tr><td>\n<img src="docs/notion_template_page_0.png" width="200px" />\n</td></tr></table>\n\nGenerated page:\n\n<table><tr><td>\n<img src="docs/notion_page_1.png" width="200px" />\n</td></tr></table>\n\n\n## Credits\n\n`autonote` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`autonote` was created by Masato Naka. It is licensed under the terms of the MIT license.\n\n## References\n1. [Atlassian Python API Confluence module](https://atlassian-python-api.readthedocs.io/confluence.html)\n1. [notion-client](https://pypi.org/project/notion-client/)\n1. [Notion API](https://developers.notion.com/)\n',
    'author': 'Masato Naka',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
