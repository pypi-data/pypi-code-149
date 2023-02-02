# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hintedtext']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hintedtext',
    'version': '0.6.0',
    'description': 'Tkinter Text widget with an extra hint attribute.',
    'long_description': '# Hinted Text \nHinted text widget for tkinter.\n\nThis custom `HintedText` class inherits from `tk.Text` and adds a hint parameter in the constructor. The `clear_hint` method is bound to the `<FocusIn>` event and will clear the hint text if the widget has focus and the text is the same as the hint. The `add_hint` method is bound to the `<FocusOut>` event and will add the hint text back if the widget loses focus and the text is empty.\n\n\n\n# Installation\n\n```bash\npip install hintedtext\n```\n\n# Usage\n\n```py\nimport tkinter as tk\nfrom hintedtext import HintedText, HintedEntry\n\nroot = tk.Tk()\ntext = HintedText(root, hint="Enter your text here")\ntext.pack()\nentry = HintedEntry(root, hint="Enter your text here")\nentry.pack()\nroot.mainloop()\n```\n',
    'author': 'Billy',
    'author_email': 'billydevbusiness@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/billyeatcookies/hintedtext',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
