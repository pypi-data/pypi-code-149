# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['octopusserver',
 'octopusserver.Http',
 'octopusserver.Http.Router',
 'octopusserver.Utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'octopusserver',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Octopusserver\n\n![Octopus](https://github.com/pab-h/octopusserver/blob/main/assets/octopus.png)\n\n## How to install\n### Pypi\n```bash \npip install octopusserver\n```\n### Poetry\n```bash \npoetry add octopusserver\n```\n\n## Getting Started\n```python\nfrom octopusserver import Octopus\nfrom octopusserver import Request\nfrom octopusserver import Response\n\nPORT = 3000\n\napp = Octopus(PORT)\n\ndef hello_world(req: Request, res: Response):\n    res.send("Hello, World!")\n\napp.router.get("/", [hello_world])\n\napp.listen(lambda: print(f"Server listen on http://localhost:{ PORT }/"))\n```\n\n## How to register your application\'s routes\n```python\nfrom octopusserver import Octopus\n\nPORT = 3000\n\napp = Octopus(PORT)\n\nrouter = app.router\n\nrouter.get("path/to/get/route/", [trigger_get_route])\n\nrouter.post("path/to/post/route/", [trigger_post_route])\n\n```',
    'author': 'pab-h',
    'author_email': 'dev.pab.2020@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
