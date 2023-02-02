# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['manim_rhythm_graph',
 'manim_rhythm_graph.pie_mobject',
 'manim_rhythm_graph.pulse_mobject',
 'manim_rhythm_graph.stick_mobject']

package_data = \
{'': ['*']}

install_requires = \
['manim>=0.17.2,<0.18.0']

entry_points = \
{'manim.plugins': ['manim_rhythm_graph = manim_rhythm_graph']}

setup_kwargs = {
    'name': 'manim-rhythm-graph',
    'version': '0.1.0',
    'description': 'A manim plugin for creating various shapes to demonstrate musical rhythm.',
    'long_description': '',
    'author': 'RCJacH',
    'author_email': 'RCJacH@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<3.12',
}


setup(**setup_kwargs)
