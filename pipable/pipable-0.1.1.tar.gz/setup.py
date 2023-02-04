# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pipable']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pipable',
    'version': '0.1.1',
    'description': 'pseudo pipe operation in python',
    'long_description': '# pipable\n\n> pseudo pipe operation in python\n\n[![ci-badge]][ci-url] [![coverage-badge]][coverage-url] [![pypi-badge]][pypi-url] [![py-version]][py-url] [![MIT-badge]][MIT-url] [![black-badge]][black-url]\n\n🔗 [source code](https://github.com/hoishing/pipable)\n\n## Quick Start\n\n### Create the Pipe Object\n\n- instantiate with the `Pipe` class\n\n```python\nfrom pipable import Pipe\n\nlist_ = Pipe(list)\n"abc" | list_    # ["a", "b", "c"]\n```\n\n#### Create Pipe Object Like Partial\n\n- turn function into Pipe by providing argument values like using the built-in `functools.partial`\n- preceding output will be assigned to the first argument while piping\n\n```python\nsquare = Pipe(pow, exp=2)\n3 | square    # 9\n```\n\nNote that assigning value to the first argument will raise exception, as it is preserved for the preceding output.\n\n```python\nbase2 = Pipe(pow, base=2)\n3 | base2    # raise !!\n```\n\n### Using Decorator\n\n- transform function to Pipe factory function with the `@Pipe` decorator\n- preceding output will be assigned to the first argument\n- instantiate Pipe object like creating partial by skipping the first argument\n\n```python\n# function with only one argument\n@Pipe\ndef hi(name: str) -> str:\n  return f"hi {name}"\n\n"May" | hi    # "hi May"\n\n\n# function with multiple arguments\n@Pipe\ndef power(base: int, exp: int) -> int:\n  return a ** b\n\n# instantiate Pipe obj by calling without the 1st argument\n2 | power(3)        # 8\n2 | power(exp=3)    # 8, better be more explicit with keyword\n\n# assign the 1st argument will cause exception\n2 | power(base=3)    # raise !!\n```\n\n## Motivation\n\nPipe operation is a handy feature in functional programming. It allows us to:\n\n- write clearer and more readable code\n- create less variables\n- easily create new functionality by chaining the output of other functions\n\nHowever it\'s still a missing feature in Python as of 2023. This package try to mimic pipe operation by overriding the bitwise-or operator, turn it into an infix function that take the output of previous expression as the first argument of the current function.\n\nThere are packages, such as [Pipe][pipe] take the similar approach. It treats pipe as iterator and work great with iterables. However, I simply want to take preceding expression as an input argument of a function then execute it. It leads to the creation of this package.\n\n## FAQ\n\nHow can I assign value to the first argument?\n  \nAssign it within a wrapper function\n\n```python\nbase2 = Pipe(lambda x: pow(2, x))\n3 | base2  # 8\n```\n\n---\n\nCan I create open pipe?\n\n`Pipe` only create closed pipe, ie. execute the function after piping with the `|` operator. You may consider other solutions such as:\n\n- [pipe][pipe], which create open pipe for iterators\n- [Coconut][coconut], a python variant that embrace functional programming\n\n---\n\nCan I append the preceding output at the end of the argument list?\n\nPut the preceding output at the end using a wrapper function\n\n```python\n# prepend is the default behaviour\nprepend = Pipe(print, \'b\', \'c\')\n\'a\' | prepend    # \'a b c\'\n\n# use wrapper if you need append\nappend = Pipe(lambda x: print(1, 2, x))\n3 | append    # \'1 2 3\'\n```\n\n## Need Help?\n\nOpen a [github issue](https://github.com/hoishing/pipable/issues) or ping me on [Twitter](https://twitter.com/hoishing) ![](https://api.iconify.design/logos/twitter.svg?width=20)\n\n[ci-badge]: https://github.com/hoishing/pipable/actions/workflows/ci.yml/badge.svg\n[ci-url]: https://github.com/hoishing/pipable/actions/workflows/ci.yml\n[coverage-badge]: https://hoishing.github.io/pipable/assets/coverage-badge.svg\n[coverage-url]: https://hoishing.github.io/pipable/assets/coverage/\n[MIT-badge]: https://img.shields.io/github/license/hoishing/pipable\n[MIT-url]: https://opensource.org/licenses/MIT\n[pypi-badge]: https://img.shields.io/pypi/v/pipable\n[pypi-url]: https://pypi.org/project/pipable/\n[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg\n[black-url]: https://github.com/psf/black\n[py-version]: https://img.shields.io/pypi/pyversions/pipable\n[py-url]: https://python.org\n[pipe]: https://pypi.org/project/pipe\n[coconut]: https://github.com/evhub/coconut\n',
    'author': 'Kelvin Ng',
    'author_email': 'hoishing@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://hoishing.github.io/pipable',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
