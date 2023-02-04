# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_depends_ext']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.70.0,<1.0.0']

setup_kwargs = {
    'name': 'fastapi-depends-ext',
    'version': '0.2.1',
    'description': 'Extends FastAPI Depends classes to simple way of modifying them after creating',
    'long_description': '![CDNJS](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-2334D058)\n![CDNJS](https://shields.io/badge/FastAPI-%3E=0.7.0-009485)\n\n# FastAPI depends extension\n\n## Introduction\n\nSometimes your FastAPI dependencies have to get value from functions cannot be available on initialization. The problem is particularly acute to use class dependencies with inheritance. This project try to solve problem of modify `Depends` after application initialization.\n\n## Installation\n\n```\npip install fastapi-depends-ext\n```\n\n## Tutorial\n\n#### DependsAttr\n\n```python\nfrom typing import List\n\nfrom fastapi import Depends\nfrom fastapi import FastAPI\nfrom fastapi import Query\nfrom pydantic import conint\n\nfrom fastapi_depends_ext import DependsAttr\nfrom fastapi_depends_ext import DependsAttrBinder\n\n\nclass ItemsPaginated(DependsAttrBinder):\n    _items = list(range(100))\n\n    async def get_page(self, page: conint(ge=1) = Query(1)):\n        return page\n\n    async def items(self, page: int = DependsAttr("get_page")):\n        _slice = slice(page * 10, (page + 1) * 10)\n        return self._items[_slice]\n\n\nclass ItemsSquarePaginated(ItemsPaginated):\n    async def items(self, items: List[int] = DependsAttr("items", from_super=True)):\n        return [i**2 for i in items]\n\n\napp = FastAPI()\n\n\n@app.get("/")\ndef items_list(items: List[int] = Depends(ItemsPaginated().items)) -> List[int]:\n    return items\n\n\n@app.get("/square")\ndef items_list_square(items: List[int] = Depends(ItemsSquarePaginated().items)) -> List[int]:\n    return items\n```\n\nUse `DependsAttr` to `Depends` from current instance attributes. All examples use `asyncio`, but you can write all methods synchronous.\n\n`DependsAttr` support next properties:\n- class variables (must contains `callable` object)\n- class methods\n- static methods\n- instance methods\n- `property` returning `callable`\n\nYour class must inherit from `DependsAttrBinder` and attributes must be `DependsAttr`. `DependsAttrBinder` automatically patch all methods with `DependsAttr` by instance attributes.\n\n`DependsAttr` arguments:\n- `method_name` - `str`, name of instance attribute to use as dependency\n- `from_super` - `bool`, on true, will use attribute `method_name` from super class like `super().method_name()`\n- `use_cache` - `bool`, allow to cache depends result for the same dependencies in request\n\n#### DependsExt\n\nUseless(?) class created to proof of concept of patching methods and correct work `FastAPI` applications.\n\n`DependsExt` allow you define default values of method arguments after `FastAPI` endpoint has been created.  \n\nExample:\n```\nfrom fastapi import FastAPI\nfrom fastapi import Query\n\nfrom fastapi_depends_ext import DependsExt\n\n\ndef pagination(page: int = Query()):\n    return page\n\n\ndepends = DependsExt(pagination)\n\n\napp = FastAPI()\n\n\n@app.on_event("startup")\ndef setup_depends():\n    depends.bind(page=Query(1))\n\n\n@app.get("/")\ndef get_method(value: int = depends) -> int:\n    return value\n\n```\n\nIs equivalent for\n```\nfrom fastapi import Depends\nfrom fastapi import FastAPI\nfrom fastapi import Query\n\n\ndef pagination(page: int = Query(1)):\n    return page\n\n\napp = FastAPI()\n\n\n@app.get("/")\ndef get_method(value: int = Depends(pagination)) -> int:\n    return value\n\n```',
    'author': 'Nikakto',
    'author_email': 'mcgish@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Nikakto/fastapi-depends-ext',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
