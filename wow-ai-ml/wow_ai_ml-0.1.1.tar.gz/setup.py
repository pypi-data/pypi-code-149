# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wow_ai_ml']

package_data = \
{'': ['*'], 'wow_ai_ml': ['default_configs/*', 'templates/*']}

setup_kwargs = {
    'name': 'wow-ai-ml',
    'version': '0.1.1',
    'description': '',
    'long_description': '# DocCrawler\n\n<!--\n[TOC]\n-->\n\n## Updates\n\n2022.09.21:\n\n- Now Moodle Crawler can download **videos** and **folders**\n- Now you can exclude particluar courses in Moodle Crawler\n\n- Now Moodle Crawler supports **login by scanning WeChat QRCode**.\n- Download path is changed to `.../DocCrawler/Download`\n- Now the crawler will show whether a file was updated\n\n## Setup\n\n```\npython = "^3.10"\nrich = "^12.5.1"\nPyYAML = "^6.0"\nbs4 = "^0.0.1"\nrequests = "^2.28.1"\nPillow = "^9.2.0"\nrarfile = "^4.0"\nhtml5lib = "^1.1\n```\n\nDependencies are managed by Poetry. Hence you can either install them manually or (requiring Poetry installed):\n\n```shell\n.../DocCrawler> poetry install\n.../DocCrawler> poetry run python ./doccrawler/general_crawler.py # General\n.../DocCrawler> poetry run python ./doccrawler/moodle_crawler.py # Moodle\n```\n\n## Usage\n\nDocCrawler contains two tools.\n\n### GeneralCrawler\n\nCan be used to crawl docs on any websites, filtered by extensions or regex pattern.\n\nDefault output directory is `.../DocCrawler/Download`\n\nYou can use it with cli arguments:\n\n```\nusage: general_crawler.py [-h] [-u URL] [-r REGEX] [-e EX [EX ...]] \n\t\t\t\t\t\t\t\t\t\t\t\t\t[-a] [-n] [-d DIR]\n                          [-o] [-U] [-z]\n\noptions:\n  -h, --help            show this help message and exit\n  -u URL, --url URL     Target url\n  -r REGEX, --regex REGEX\n                        Target regex\n  -e EX [EX ...], --ex EX [EX ...]\n                        Target extensions\n  -a, --all             Match all\n  -n, --name            Use tag text as filename\n  -d DIR, --dir DIR     Output directory\n  -o, --order           Add order prefix\n  -U, --update          Update existed file\n  -z, --unzip           Unzip compressed files\n```\n\nOr execute it without any args to enter the interactive setup:\n\n<img src="assets/image-20220918104510929.png" alt="image-20220918104510929" style="zoom:30%;" />\n\n#### Configs\n\nThe config file is `.../DocCrawler/general_config.yaml`, using YAML syntax.\n\nYou can add presets to the configs in the following manner:\n\n```yaml\nwebsites:\n  $Preset_name$:\n    $arg0$: ...\n    $arg1$: ...\n    ...\n```\n\nExample:\n\n```yaml\nwebsites:\n  CAT Assignments:\n    dir: "~/Library/CloudStorage/OneDrive-Personal/CAT - Concurrency-Algorithms and Theories/Assignments"\n    ex:\n      - pdf\n    name: false\n    url: https://h*******g.github.io/teaching/concurrency/\n  CAT Slides:\n    dir: "~/Library/CloudStorage/OneDrive-Personal/CAT - Concurrency-Algorithms and Theories/Slides"\n    ex:\n      - ppt\n      - pptx\n    name: false\n    url: https://h*******g.github.io/teaching/concurrency/\n  FLA Slides:\n    dir: "~/Library/CloudStorage/OneDrive-Personal/FLA - Formal Languages and Automata/Slides"\n    ex:\n      - ppt\n      - pptx\n    name: true\n    order: true\n    url: https://c*******n/bulei/FLA22.html\n  SPA - Slides:\n    dir: "~/Library/CloudStorage/OneDrive-Personal/SPA - Static Program Analysis/Slides"\n    ex:\n      - pdf\n    name: false\n    order: true\n    url: http://t*******b.net/lectures.html\n```\n\n<img src="assets/image-20220918105813267.png" alt="image-20220918105813267" style="zoom:50%;" />\n\n### MoodleCrawler\n\nCan be used on the new Moodle website of NJU SE. This will automatically scan all the courses you have joined and download their resources.\n\nA valid Cookies string should be provided when you run it for the first time, or when the previous cookies is invalid.\n\n<img src="assets/image-20220918110143776.png" alt="image-20220918110143776" style="zoom:50%;" />\n\n#### Configs\n\nThe config file is `.../DocCrawler/general_config.yaml`, using YAML syntax, which will be generated automatically.\n\nYou can edit the configs in the following manner:\n\n```yaml\nmoodle:\n  cookies: ...\n  courses:\n    $CourseID$: # Generated\n      dir: ...\n      my_args: [$arg1$, $arg2$, ...]\n      name: ... # Generated\n      exclude: ... # True or False\n```\n\n',
    'author': 'TonyShark',
    'author_email': 'quoi@wow-ai.inc',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
