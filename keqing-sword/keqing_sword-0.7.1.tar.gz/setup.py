# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kqs']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'keqing-sword',
    'version': '0.7.1',
    'description': 'A non-database Python base OSM data parser, with SQL operation simulated.',
    'long_description': '# Keqing\n\n[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword?ref=badge_shield)\n<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n\nA non-database Python base OSM data parser, with SQL operation simulated \n\n----------\n\n本项目是一个基于Python的对`.osm`文件的访问库\n\n## 使用示例 Demo\n\n### 快速开始\n\n```python\nfrom kqs.waifu import Waifu\n\nmap = Waifu()\nmap.read(mode="file", file_path="map.osm")\n```\n\n### 获取`name`\n\n### 基于输入生成`.osm`文件\n\n**更多示例可见`/docs`中[README文件](/docs/README.md)，详细列出了Keqing_Sword的各种功能**\n\n## 特性\n\n### Pypy friendly\n\nThis package don\'t depend on any package, so it\'s compatible with latest pypy.\n\n### Pure in memory\n\nDon\'t need any database environment, just a fast and out-of-the-box tool.\n\n## KQS:NOT\n\n列举出可能与本项目相近，相似，但目的并非一致的替代品\n\n## Roadmap\n\n### 1.0版本之前\n1. 初期完善Diff工作\n2. 能够正常读写到文件\n3. 正式重命名为Keqing（已预留命名空间）\n\n### 1.0版本之后\n1. 加快建设多种输入输出流\n2. 引入覆盖率测试\n3. 引入select语句，可以自定义查询（预计作为2.0发布）\n\n## 命名来源\n\n项目Leader @Jyunhou 钦点\n\n<a herf="https://zh.wikipedia.org/wiki/%E5%8E%9F%E7%A5%9E%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8#%E7%92%83%E6%9C%88%E4%B8%83%E6%98%9F"><img alt="Keqing" src="https://avatars.githubusercontent.com/u/45530478?v=4" width=249px></a>\n\n## License\n[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FOSMChina%2FOSMChina-Keqing_Sword?ref=badge_large)\n',
    'author': '快乐的老鼠宝宝',
    'author_email': 'keaitianxinmail@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
