# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stock_summary']

package_data = \
{'': ['*'],
 'stock_summary': ['demo_datasets/*', 'html_files/*', 'init_datasets/*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'pandas>=1.5.2,<2.0.0',
 'plotly>=5.11.0,<6.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['stock_summary_tool = stock_summary.main:main']}

setup_kwargs = {
    'name': 'stock-summary-tool',
    'version': '0.1.1',
    'description': 'Tool for tracking of your investments and your actual portfolio',
    'long_description': "# Stock summary tool\n\n### CREATE YOUR ENVIRONMENT\n1. Create virtual environment that you will use for the project and activate it (python3.8+ required):\n```\npython3 -m venv my_venv/\nsource my_venv/bin/activate\n```\n2. Install the package: \n```\npip3 install stock_summary_tool\n```\n3. Generate and save your token:\n   1. Register or log in to the page.\n   2. Go to https://rapidapi.com/ and register.\n   3. Subscribe to these APIs and obtain your API key:\n      1. https://rapidapi.com/sparior/api/yahoo-finance15\n      2. https://rapidapi.com/fixer/api/fixer-currency\n   4. Save your key for the project:\n   ```\n   stock_summary_tool save-token <YOUR_TOKEN>\n   ```\n### DEMO\n\n1. You can download demo datasets and import them:\n   ```\n   stock_summary_tool import-data -y -e <PATH_TO_DEMO_ENTRIES> -p <PATH_TO_DEMO_PORTFOLIO)\n   ```\n2. You can generate-html (it should open automatically in your browser):\n   ```\n   stock_summary_tool generate-html\n   ```\n3. You can update your portoflio by actual cost and generate again HTML page:\n   ```\n   stock_summary_tool generate-portfolio\n   stock_summary_tool generate-html\n   ```\n\n### CREATE YOUR PORTFOLIO\n\n1. Refresh data to empty files:\n   ```\n   stock_summary_tool import-data -y --rewrite\n   ```\n2. Add your entries (example) - stock symbol, date, count of stocks, price (sell entries are also supported, just add '-' sign before count):\n   ```\n   stock_summary_tool add-entry -s BOTZ.MI -d 12/01/2023 -c 20 -p 30\n   ```\n3. You can enter also your dividends (amount is in original currency):\n   ```\n   stock_summary_tool add-dividend -s BOTZ.MI -d 12/01/2023 -a 10 \n   ```\n4. After you add your entries and dividends, generate actual portfolio and HTML:\n   ```\n   stock_summary_tool generate-portfolio\n   stock_summary_tool generate-html\n   ```\n5. You can also export your data and share them across multiple systems (by importing them again):\n   ```\n   stock_summary_tool export-data -d <DIRECTORY_FOR_EXPORT>\n   ```\n\n### HTML tutorial\n\n*You can open example summary stock_summary/demo_datasets/index.html Right now, there is supported only czech language and CZK currency is taken as base.*\n\nYou can see plot with your actual investments in stocks, and also your profit (generated from portfolio file). Below you can see your actual holdings and \nstatistics about them. Only actual holdings with >0 count are shown. The last table is for dividends.\n\n### Rules about generating portfolio and balance\n1. Entries are converted to the base currency with conversion rate for the execution day.\n2. Dividends are converted to the base currency with conversion rate for the execution day.\n3. Value of your portfolio for the current day is counted as sum of your holdings for the day. (converted to base currency)\n4. Profit is comparison of your invested amount with dividends and your actual holdings. If you sell some stocks, profit stays same, only value of your portfolio goes down. Same with buy entries (portfolio up, profit stays same). If you get some dividends, it grows your profit by that amount.\n5. ONCE AGAIN: All amounts are automatically converted to base currency by exchange rate of the execution day. It doesn't matter if you convert them or not. Right now it's out of scope of the tool.\n\n### Plans for the future\n1. Adding option for fees to the operations.\n2. Supporting more languages and base currencies.\n3. Adding backward possibility to generate portfolio and no need to generate it manually anymore (blocked by higher number of API calls and subscription)\n4. Support for cloud storage (easy setup and option to use tool across more systems without manual import/export)\n5. Adding option to track other investments except stocks/cryptocurrencies/dividends.\n\nBe free to open issue or ask me, if you want to know something or you want to help with the project.\n\n",
    'author': 'Simon Foucek',
    'author_email': 'foucek.simon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
