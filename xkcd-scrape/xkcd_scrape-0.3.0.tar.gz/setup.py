# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xkcdscrape']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0', 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'xkcd-scrape',
    'version': '0.3.0',
    'description': 'Scrape the XKCD comic archive',
    'long_description': '# XKCD Scrape\n\n`xkcd-scrape` is a Python module to dump the XKCD.com archive and get comic info using BS4. Honestly, it\'s a very basic module with one premise - easily get information about comics.\n\n## Examples\nBasic usage:\n```py\nfrom xkcdscrape import xkcd\n\n# Load the archive of comics into a variable\narchive = xkcd.parseArchive()\n\n# Get info about latest comic\ninfo = xkcd.getComicInfo(archive)\n\n# Get info about specific comic\n# The comic can either be an int (200), a str ("200"|"/200/"), or a link ("https://xkcd.com/200")\ninfo = xkcd.getComicInfo(archive, 2000)\n\n# Get info about a random comic\n# Passing the second paramenter as True makes the module only fetch comics that are present in the archive\ninfo = xkcd.getRandomComic(archive, False)\n\n# Dump archive to file\n# Use indent=None if you want to save space or make parsing easier\nxkcd.dumpToFile(archive, "dump.json", indent=None)\n\n# Get info using archive dump. You can do the same with getRandomComic()\ninfo = xkcd.getComicInfo("dump.json", 2000)\n```\n\nThe `getComicInfo` function (also called inside of `getRandomComic`) returns a dict with following keys:\n```py\n# xkcd.getComicInfo(archive, 2000)\n{\n    \'num\': \'2000\', \n    \'link\': \'https://xkcd.com/2000/\', \n    \'name\': \'xkcd Phone 2000\', \n    \'date\': \'2018-5-30\', \n    \'image\': \'https://imgs.xkcd.com/comics/xkcd_phone_2000.png\', \n    \'title\': \'Our retina display features hundreds of pixels per inch in the central fovea region.\'\n}\n```\nAs you can see, it returns the following list of keys:\n- `num` - comic number\n- `link` - hyperlink to comic\n- `name` - the name of the comic\n- `date` - YYYY-MM-DD formatted date of when the comic was posted\n- `image` - hyperlink to image used in the comic\n- `title` - title (hover) text of the comic\n\n## Archive\nThe [XKCD archive](https://xkcd.com/archive/) is where we get the list of comics, \nas well as their names and date of posting. This is the only place where we can get \nthe date of posting (unless we go into HTTP headers, but that\'s a mess), so it\'s \nrequired. The module is still in the `0.Y.Z` version, so bugs will be expected, \nsuch as not being able to fetch the latest comic\'s info, if it isn\'t yet in \nyour archive. That and many more things will be patched by the 1.0.0 release.\n\nThe archive is an dict containing various dicts with keys of `/num/`. Example:\n```py\n{\n    ...,\n    "/2000/": {\n        "date": "2018-5-30", \n        "name": "xkcd Phone 2000"\n    },\n    ...\n}\n```\n\n## Tests\nTests can be run from the project\'s shell after installing and activating the venv using `poetry run pytest`.\n\n## TODO\n- Rewrite docstrings, make them simpler\n- Not require archive for fetching info (dateless?)\n- Use Codeberg\'s CI/CD to push to PYPI\n- Add RSS/Atom feed support to fetch latest comic (includes date inside)\n- API setup script w/ Flask',
    'author': 'calamity',
    'author_email': 'clmty@vk.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
