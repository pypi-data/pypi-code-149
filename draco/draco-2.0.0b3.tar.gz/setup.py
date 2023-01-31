# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['draco',
 'draco.renderer',
 'draco.renderer.altair',
 'draco.server',
 'draco.server.models',
 'draco.server.routers',
 'draco.server.services']

package_data = \
{'': ['*'], 'draco': ['asp/*', 'asp/examples/*']}

install_requires = \
['clingo>=5.5.2,<6.0.0',
 'fastapi>=0.85,<0.90',
 'matplotlib>=3.6.0,<4.0.0',
 'pandas>=1.4.2,<2.0.0',
 'scikit-learn>=1.1.1,<2.0.0',
 'uvicorn>=0.18.3,<0.21.0']

setup_kwargs = {
    'name': 'draco',
    'version': '2.0.0b3',
    'description': 'Visualization recommendation using constraints',
    'long_description': '<p align="center">\n   <a href="https://github.com/cmudig/draco2">\n      <picture>\n         <source media="(prefers-color-scheme: dark)" srcset="https://github.com/cmudig/draco2/raw/main/docs/logo-light.png">\n         <source media="(prefers-color-scheme: light)" srcset="https://github.com/cmudig/draco2/raw/main/docs/logo-dark.png">\n         <img alt="The Draco logo. A set of circles connected by lines depicting the draco star constellation." src="https://github.com/cmudig/draco2/raw/main/docs/logo-light.png" width=260>\n      </picture>\n   </a>\n</p>\n\n# Draco v2\n\n[![PyPi](https://img.shields.io/pypi/v/draco.svg)](https://pypi.org/project/draco/)\n[![Test](https://github.com/cmudig/draco2/actions/workflows/test.yml/badge.svg)](https://github.com/cmudig/draco2/actions/workflows/test.yml)\n[![code style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![codecov](https://codecov.io/gh/cmudig/draco2/branch/main/graph/badge.svg)](https://codecov.io/gh/cmudig/draco2)\n[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cmudig/draco2/HEAD)\n\n**Work in Progress**\n\nDraco is a formal framework for representing design knowledge about effective visualization design as a collection of\nconstraints. You can use Draco to find effective visualization designs or validate existing ones. Draco\'s constraints\nare based on Answer Set Programming (ASP) and solved with the [Clingo](https://github.com/potassco/clingo) constraint\nsolver. We also implemented a way to learn weights for the recommendation system directly from the results of graphical\nperception experiment. Draco v2 is a much improved version of the first iteration of\n[Draco](https://github.com/uwdata/draco).\n\n## Documentation\n\nRead about Draco in the online book at [https://dig.cmu.edu/draco2/](https://dig.cmu.edu/draco2/) or launch it in\ninteractive mode using [Binder](https://mybinder.org/v2/gh/cmudig/draco2/HEAD). In the documentation, we just refer to\n_Draco_ without a version.\n\n## What\'s different from [Draco v1](https://github.com/uwdata/draco)?\n\n- Draco v2 is completely written in Python. No more need to run both Python and Node. We still use ASP for the knowledge\n  base.\n- Generalized and extended chart specification format. The new format is more extensible with custom properties.\n- Support for multiple views and view composition.\n- High test-coverage, documentation, and updated development tooling.\n\n## Contributing\n\nWe welcome any input, feedback, bug reports, and contributions. You can learn about setting up your development\nenvironment in [CONTRIBUTING.md](https://github.com/cmudig/draco2/blob/main/CONTRIBUTING.md).\n',
    'author': 'Dominik Moritz',
    'author_email': 'domoritz@cmu.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cmudig/draco2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.0,<3.11',
}


setup(**setup_kwargs)
