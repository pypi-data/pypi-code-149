# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tradernet', 'tradernet.symbols']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'certifi>=2022.06.15,<2023.0.0',
 'lxml>=4.9.1,<5.0.0',
 'mypy-extensions>=0.4.3,<0.5.0',
 'numpy>=1.23.0,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'tabulate>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'tradernet-sdk',
    'version': '0.3.0',
    'description': 'Public API for TraderNet',
    'long_description': "# tradernet-sdk\n\nPublic Python API for TraderNet\n\n## Installation\n\nInstalling tradernet with pip is straightforward:  \n`python -m pip install tradernet-sdk`  \nInstead of `python` you can use here and further `pypy3` depending on your preferences.\n\n## Usage\n\nImport the client library into your script:  \n`from tradernet import TraderNetAPI`  \nInitialize it with your credentials:  \n`api = TraderNetAPI('public_key', 'private_key', 'login', 'passwd')`  \nor create a config file `tradernet.ini` with the following content:  \n```\n[auth]\npublic   = public_key\nprivate  = private_key\nlogin    = login\npassword = passwd\n```\nand initialize the client with `api = TraderNetAPI.from_config('tradernet.ini')`  \nCall any of its public methods, for example:  \n`api.user_info()`  \n\n### How to trade\n\nUsage of the trading interface is similar to common API. Import and instantiate `Trading` class:  \n```\nfrom tradernet import Trading\n\n\norder = Trading.from_config('tradernet.ini')\n```\nNow let's buy 1 share of FRHC.US at the market price:  \n```\norder.buy('FRHC.US')\n```\n\n### Advanced techniques\n\nOne can import the core class to write their own methods:\n```\nfrom tradernet import TraderNetCore\n\n\nclass MyTNAPI(TraderNetCore):\n    pass\n```\nThis allows using sophisticated request methods for TN API like\n`TraderNetCore.authorized_request`.  \n\nOne can have several instances of the API serving different purposes:  \n```\nconfig = TraderNetCore.from_config('tradernet.ini')\norder = Trading.from_instance(config)\n```\nThe instance `config` stores the credentials, and `order` can be used to trade and may be destroyed after trades completed while `config` is still can be used to instantiate other classes.\n\n\n### Websockets\n\nWebsocket API can be accessed via another class `TraderNetWSAPI`. It\nimplements asynchronous interface for TraderNet API, and its usage is a bit\nmore complicated:  \n```\nfrom tradernet import TraderNetCore, TraderNetWSAPI\n\n\nasync def main() -> None:\n    api = TraderNetCore.from_config('tradernet.ini')\n    async with TraderNetWSAPI(api) as wsapi:  # type: TraderNetWSAPI\n        async for quote in wsapi.market_depth('FRHC.US'):\n            print(quote)\n```\n\n### Legacy API\n\nThe library also has the legacy `PublicApiClient.py` which provides almost\nthe same functionality as most of TraderNet users used to:\n```\nfrom tradernet import NtApi\n\n\npub_ = '[public Api key]'\nsec_ = '[secret Api key]'\ncmd_ = 'getPositionJson'\nres = NtApi(pub_, sec_, NtApi.V2)\nprint(res.sendRequest(cmd_))\n```\nThe only difference is that one doesn't have to decode the content of the\nresponse as before.\n\n### Options\n\nThe notation of options in TraderNet now can easily be deciphered:\n```\nfrom tradernet import TraderNetOption\n\n\noption = TraderNetOption('+FRHC.16SEP2022.C55')\nprint(option)  # FRHC.US @ 55 Call 2022-09-16\n```\nor the scary old notation:\n```\nfrom tradernet import DasOption\n\n\noption = DasOption('+FRHC^C7F45.US')\nprint(option)  # FRHC.US @ 45 Call 2022-07-15\n```\n\n### Wrapping market data\n\nAnother feature is to get handy pandas.DataFrame objects with market data:\n```\nfrom tradernet import TraderNetSymbol, TraderNetAPI\n\n\napi = TraderNetAPI('public_key', 'private_key', 'login', 'passwd')\nsymbol = TraderNetSymbol('AAPL.US', api)\nsymbol.get_data()\nprint(symbol.market_data.head().to_markdown())\n# | date                |     high |      low |     open |    close |      volume |\n# |:--------------------|---------:|---------:|---------:|---------:|------------:|\n# | 1980-12-12 00:00:00 | 0.128876 | 0.12834  | 0.12834  | 0.12834  | 1.17258e+08 |\n# | 1980-12-15 00:00:00 | 0.122224 | 0.121644 | 0.122224 | 0.121644 | 4.39712e+07 |\n# | 1980-12-16 00:00:00 | 0.113252 | 0.112716 | 0.113252 | 0.112716 | 2.6432e+07  |\n# | 1980-12-17 00:00:00 | 0.116064 | 0.115484 | 0.115484 | 0.115484 | 2.16104e+07 |\n# | 1980-12-18 00:00:00 | 0.119412 | 0.118876 | 0.118876 | 0.118876 | 1.83624e+07 |\n```\n\n## License\n\nThe package is licensed under permissive MIT License. See the `LICENSE` file in\nthe top directory for the full license text.\n",
    'author': 'Anton Kudelin',
    'author_email': 'a.kudelin@freedomfinance.eu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.nettrader.ru/risk/python-tradernet-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
