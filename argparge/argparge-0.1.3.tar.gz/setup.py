# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['argparge']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'argparge',
    'version': '0.1.3',
    'description': 'A very simple tool to create beautiful console application by using native argparse.',
    'long_description': '# Argparge\n\n> A very simple tool to create beautiful console application by using native argparse.\n\n| Project       | Commander                                    |\n|---------------|----------------------------------------------|\n| Author        | Özcan Yarımdünya                             |\n| Documentation | https://ozcanyarimdunya.github.io/argparge/  |\n| Source code   | https://github.com/ozcanyarimdunya/argparge/ |\n\n`argparge` is a library that you can create beautiful class based cli application.\n\n## Installation\n\nWorks on `python3+` with no extra dependencies.\n\n```shell\npip install argparge\n```\n\n## Usage\n\n**example.py**\n\n```python\nfrom argparge import Application\nfrom argparge import Command\n\n\nclass GreetCommand(Command):\n    name = "greet"\n    help = "Greeting a person"\n\n    def add_arguments(self, parser: "Command"):\n        parser.add_argument("name", help="Person name")\n\n    def handle(self, **arguments):\n        print("Greeting, ", arguments.get("name"))\n\n\nif __name__ == \'__main__\':\n    app = Application(description="A simple argparge application")\n    app.add_argument("-V", "--version", action="version", version="1.0.0")\n    app.add_commands(\n        GreetCommand(),\n    )\n    app.run()\n```\n\nIf we run we get such output.\n\n![gif](./docs/images/1.gif)\n\nFor more checkout [tutorials.](https://ozcanyarimdunya.github.io/argparge/tutorial/)\n\n## LICENSE\n\n```text\nMIT License\n\nCopyright (c) 2023 yarimdunya.com\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n```\n',
    'author': 'Özcan Yarımdünya',
    'author_email': 'ozcanyd@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ozcanyarimdunya.github.io/argparge/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
