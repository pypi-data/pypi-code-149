# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prodot']

package_data = \
{'': ['*']}

install_requires = \
['jsonpath-ng>=1.5.3,<2.0.0']

setup_kwargs = {
    'name': 'prodot',
    'version': '0.1.2',
    'description': '',
    'long_description': '# prodot\n\nA new way to deal with dictionaries and lists in python.\n\n## install\n```\npip install prodot\n```\n\n## Usage\n\nImport the dot object from the prodot library. You can create a new empty dictionary, or start with a filled one\n\n```Python\nfrom prodot import DotObject\n\n# No parameters instances an empty dictionary\nmy_new_obj = DotObject() \n\n# The Dot Object can be initialized with a dictionary\nmy_dict_obj = DotObject({"foo":["bar,"eggs"]})\n\n# The Dot Object can also initialize with a list\nmy_list_obj = DotObject([ [1,2,3], ["a","b","c"], [{"foo":"bar"}, {"bar":"eggs"}] ])\n\n```\n\n### Dot notation usage\nBy using the dot-object you can use the dictionary as a class\n```Python\n\nmy_json = {\n  "userData": {\n    "name": "John",\n    "age": "38",\n    "shoppingCart": [\n      {"cellphone": 999.99},\n      {"notebook": 2999.99},\n      {"wireless keyboard": 299.99}\n    ]\n  }\n}\n\nmy_new_obj = DotObject(my_json)\n\nshoppingCart = my_new_obj.userData.shoppingCart\n```\n\nThe DotObject will return another instance of the DotObject with the main_object attribute as being the selected path.\n\n```Python\n>>> type(shoppingCart)\n<class \'prodot.dot_object.DotObject\'>\n```\n\nTo get the brute value of the object, you can use the `.get_value()` function.\n\n```Python\n>>> shoppingCart.get_value()\n[{"cellphone": 999.99}, {"notebook": 2999.99}, {"wireless keyboard": 299.99}]\n\n# or by using the get_value directly at the path\n>>> my_new_obj.userData.shoppingCart.get_value()\n[{"cellphone": 999.99}, {"notebook": 2999.99}, {"wireless keyboard": 299.99}]\n\n>>> type(shoppingCart.get_value())\n<class \'dict\'>\n```\n\nYou can also add new information to the instancied object\n\n```Python\n# n3 means list index 3 (will be added as 4th item)\n>>> my_new_obj.userData.shoppingCart.n3 = {"monitor": 699.99}\n>>> my_new_obj.userData.shoppingCart.get_value()\n[{"cellphone": 999.99}, {"notebook": 2999.99}, {"wireless keyboard": 299.99}, {"monitor": 699.99}]\n```\nPython doesn\'t accept list indexes to be used as a class attribute. For solve this problem, list indexes start with the `n` letter (like n0, n1, ...)\n\n',
    'author': 'Matheus Menezes Almeida',
    'author_email': 'mrotame@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
