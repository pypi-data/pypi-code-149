# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schemagpt']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.26.4,<0.27.0']

setup_kwargs = {
    'name': 'schemagpt',
    'version': '0.1.0',
    'description': 'Python library for RDF Schemas generation from prompts using GPT-3 magic 🪄🪄🪄',
    'long_description': '# SchemaGPT\n\n> **Note:** The generated RDF Schemas are not 100% accurate and may require manual correction.\n\nSchemaGPT is a Python library that utilizes the power of OpenAI\'s GPT-3 and [schema.org](https://schema.org) vocabulary to generate RDF Schemas from natural language.\n\nThe library aims to simplify the process of creating RDF Schemas by automatically generating them from a user-defined description written in natural language.\n\nThe generated Schemas are in the form of RDF, a popular data model for semantic web technologies, making it easier for developers to work with linked data.\n\n## Who can benefit from using this library?\n\nAnyone who wants to simplify the process of creating RDF Schemas for linked data can benefit from using the SchemaGPT library. This includes software developers, data scientists, semantic web practitioners, and anyone else who needs to work with RDF data. The library is especially useful for those who are not familiar with the intricacies of RDF Schema creation, as it provides a way to generate Schemas from a natural language description, making the process much easier and faster.\n\n\n## Installation\n\nTo install SchemaGPT, simply run the following command using `pip`:\n\n```bash\npip install schemagpt\n```\nor using `Poetry`:\n```bash\npoetry add schemagpt\n```\n\n## Usage\n\nUsing SchemaGPT is straightforward. Here\'s a simple example:\n\n```python\nfrom schemagpt import SchemaGPT\n\ngenerator = SchemaGPT(<YOUR_OPENAI_API_KEY>)\nschema = generator.schema("Tesla Model X")\nprint(schema)\n```\n\nThis will generate the following RDF Schema:\n```json\n{\n  "@context": "https://schema.org",\n  "@type": "Car",\n  "name": "Tesla Model X",\n  "brand": {\n    "@type": "Brand",\n    "name": "Tesla"\n  },\n  "model": "Model X"\n}\n```\n\n## Features\n| Feature | Status |\n| :------- | :------: |\n| Schemas generation/updates using natural language | :white_check_mark: |\n| Schemas validation/fixes (according to schema.org) with Pydantic | :construction: |\n\n## Supported formats for RDF Schemas\n\n| Format | Description | Status |\n| :------ | :----------- | :------: |\n| RDF/XML | The standard XML format for RDF | :x: |\n| Turtle | A terse, human-readable RDF syntax | :x: |\n| N-Triples | A line-based, plain-text format for RDF | :x: |\n| N-Quads | A line-based, plain-text format for RDF with context information | :x: |\n| JSON-LD | A JSON-based format for RDF | :white_check_mark: |\n\n## Contribution\nSchemaGPT is open-source. If you have an idea for a new feature, or you\'ve found a bug, please feel free to open an issue or submit a pull request.\n',
    'author': 'Uladzislau Hubar',
    'author_email': 'hubar.uladzislau@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
