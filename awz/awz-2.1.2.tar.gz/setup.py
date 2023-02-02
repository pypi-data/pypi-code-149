import os
import re
from setuptools import setup,find_packages


requires = ["pycryptodome==3.16.0","aiohttp==3.8.3","asyncio==3.4.3","tinytag==1.8.1","Pillow==9.4.0"]
_long_description = """

### How to import the Rubik's library

``` bash
from Awz import Messenger

Or

from Awz import Robot_Rubika
```

### How to import the Robino class

``` bash
from Awz import Robino
```

### How to import the anti-advertising class

``` bash
from Awz.Zedcontent import Antiadvertisement
```

### How to install the library

``` bash
pip install awz==1.2.1
```

## An example:
``` python
from Awz import Messenger

bot = Messenger("Your Auth Account")

gap = "your guid or gap or pv or channel"

bot.sendMessage(gap,"libraryawz")
```

## And Or:
``` python
from Awz import Messenger

bot = Robot_Rubika("Your Auth Account")

gap = "your guid or gap or pv or channel"

bot.sendMessage(gap,"awz")
```
"""

setup(
    name = "awz",
    version = "2.1.2",
    author = "rebackk",
    author_email = "aryongram@gmail.com",
    description = (" libraryawz"),
    license = "MIT",
    keywords = ["bot","Bot","BOT","Robot","ROBOT","robot","self","api","API","Api","rubika","Rubika","RUBIKA","Python","python","aiohttp","asyncio","awz","Awz","AWZ"],
    url = "https://www.rubika.ir/awz_lib",
    packages = find_packages(),
    long_description=_long_description,
    long_description_content_type = 'text/markdown',
    install_requires=requires,
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: Implementation :: PyPy",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11'
    ],
)
