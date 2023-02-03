# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shifter_pandas']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['certifi', 'openpyxl', 'pandas', 'requests', 'toml', 'wikidata']

setup_kwargs = {
    'name': 'shifter-pandas',
    'version': '0.2.1',
    'description': 'Convert some data into Panda DataFrames',
    'long_description': '# Convert some data into Panda DataFrames\n\n## British Petroleum (BP)\n\nIt parse sheet like `Primary Energy Consumption` (not like `Primary Energy - Cons by fuel`).\n\nOpen: http://www.bp.com/statisticalreview\nor https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html\n\nDownload `Statistical Review of World Energy – all data`.\n\nUse:\n\n```python\nfrom shifter_pandas.bp import UNITS_ENERGY, BPDatasource\n\nshifter_ds = BPDatasource("bp-stats-review-2021-all-data.xlsx")\n\ndf = shifter_ds.datasource(units_filter=UNITS_ENERGY, regions_filter=["Switzerland"])\ndf\n```\n\n## Swiss Office Federal of Statistics (OFS)\n\nFrom https://www.bfs.admin.ch/bfs/fr/home/services/recherche/stat-tab-donnees-interactives.html\ncreate a stat table.\n\nClick on `À propos du tableau`\n\nClick on `Rendez ce tableau disponible dans votre application`\n\nUse:\n\n```python\nfrom shifter_pandas.ofs import OFSDatasource\n\nshifter_ds = OFSDatasource("<URL>")\n\ndf = shifter_ds.datasource(<Requête Json>)\ndf\n```\n\nAnd replace `<URL>` and `<Requête Json>` with the content of the fields of the OFS web page.\n\n### Interesting sources\n\n- [Parc de motocycles par caractéristiques techniques et émissions](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1103020100_165/-/px-x-1103020100_165.px/)\n- [Bilan démographique selon l\'âge et le canton](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-0102020000_104/-/px-x-0102020000_104.px/)\n\n## Our World in Data\n\nSelect a publication.\n\nClick `Download`.\n\nClick `Full data (CSV)`.\n\nUse:\n\n```python\nimport pandas as pd\nfrom shifter_pandas.wikidata_ import WikidataDatasource\n\ndf_owid = pd.read_csv("<file name>")\nwdds = WikidataDatasource()\ndf_wd = wdds.datasource_code(wikidata_id=True, wikidata_name=True, wikidata_type=True)\ndf = pd.merge(df_owid, df_wd, how="inner", left_on=\'iso_code\', right_on=\'Code\')\ndf\n```\n\n### Interesting sources\n\n- [GDP, 1820 to 2018](https://ourworldindata.org/grapher/gdp-world-regions-stacked-area)\n- [Population, 1800 to 2021](https://ourworldindata.org/grapher/population-since-1800)\n\n## World Bank\n\nOpen https://data.worldbank.org/\n\nFind a chart\n\nIn `Download` click `CSV`\n\nUse:\n\n```python\nfrom shifter_pandas.worldbank import wbDatasource\n\ndf = wbDatasource("<file name>")\ndf\n```\n\n### Interesting sources\n\n- [GDP (current US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)\n- [GDP (constant 2015 US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD)\n\n## Wikidata\n\nBy providing the `wikidata_*` parameters, you can ass some data from WikiData.\n\nCareful, the WikiData is relatively slow then the first time you run it il will be slow.\nWe use a cache to make it fast the next times.\n\nYou can also get the country list with population and ISO 2 code with:\n\n```python\nfrom shifter_pandas.wikidata_ import (\n    ELEMENT_COUNTRY,\n    PROPERTY_ISO_3166_1_ALPHA_2,\n    PROPERTY_POPULATION,\n    WikidataDatasource,\n)\n\nshifter_ds = WikidataDatasource()\ndf = shifter_ds.datasource(\n    instance_of=ELEMENT_COUNTRY,\n    with_id=True,\n    with_name=True,\n    properties=[PROPERTY_ISO_3166_1_ALPHA_2, PROPERTY_POPULATION],\n    limit=1000,\n)\ndf\n```\n',
    'author': 'Stéphane Brunner',
    'author_email': 'stephane.brunner@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://hub.docker.com/r/sbrunner/shifter-pandas/',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
