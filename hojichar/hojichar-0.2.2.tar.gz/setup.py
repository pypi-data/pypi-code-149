# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hojichar', 'hojichar.core', 'hojichar.dict', 'hojichar.filters']

package_data = \
{'': ['*']}

install_requires = \
['mmh3>=3.0.0,<4.0.0', 'numpy>=1.23.4,<2.0.0']

setup_kwargs = {
    'name': 'hojichar',
    'version': '0.2.2',
    'description': 'Text preprocessing management system.',
    'long_description': '# HojiChar\n[![CI wowkflow](https://github.com/HojiChar/HojiChar/actions/workflows/ci.yaml/badge.svg)](https://github.com/HojiChar/HojiChar/actions/workflows/ci.yaml)\n[![codecov](https://codecov.io/gh/HojiChar/HojiChar/branch/main/graph/badge.svg?token=16928I9U9Y)](https://codecov.io/gh/HojiChar/HojiChar)\n## 概要\nHojiChar はテキストデータの前処理のためのPythonモジュールです. 言語モデル構築時などにコーパスを前処理する目的で開発されました。\n\n`hojichar.filters` で定義された、あるいはユーザーが定義したテキスト前処理フィルタを束ね、ひとつの前処理パイプラインとして構成することができように作られています。\n\nこの前処理パイプラインは、`torchvision.transforms` に着想を得て開発されました。\n\n\n## 使い方\n### インストール\n*install via pip -- 準備中*\n\n**Poetry によるローカルインストール**\n\n`python >= 3.8, poetry >= 1.2`\n\nこのリポジトリをクローンし、poetry でインストールします。\n```\npoetry install\n```\n\n\n### Rocket start\n`Compose` クラスを使ってフィルタを作成します.\n```Python\nfrom hojichar import Compose, document_filters, cleaners\n\ncleaner = Compose([\n    document_filters.JSONLoader(key="text"),\n    cleaners.AcceptJapanese(),\n    cleaners.DocumentLengthFilter(min_doc_len=0,max_doc_len=1000),\n    document_filters.ExampleHojiChar()\n])\n```\n```\n>>> cleaner(\'{"text": "こんにちは、"}\')\n\'こんにちは、<hojichar>\'\n```\n上記のフィルタでは 1. JSONから`\'text\'` キーの値を取得 2. 日本語文字列でなければ破棄, 3. 0字以上1000字以内の文章以外を破棄, 4. 文字列に `<hojichar>` を追加 の処理をしています.\n\n各フィルタの処理についてはフィルタの Docstrings に記載されています。\n\n### ユーザー定義フィルタ\n`Filter` クラスを継承し, `apply` 関数内にフィルタの挙動を記述します.\n```Python\nfrom hojichar.core.filter_interface import Filter\n\nclass YourFilter(Filter):\n    def apply(self, document):\n        document.text = your_process(document.text)\n        return document\n```\n`apply` 関数は `hojichar.core.models.Document` 型を引数として受け取り,\n返す関数です. `Document` は文字列をカプセル化したクラスです.\n\n\n## Reference\n*準備中*\n\n各フィルタの処理内容は、`hojichar.filters` モジュール内の Docstrings に記載されています。\n\n\n\n## 開発者向け\n\n開発用のパッケージのインストールのために,\n```\npoetry install --with dev,lint,test\n```\n### テスト\nテスト実行\n```\npoetry run task test\n```\nで mypy と pytest のテストが実行されます.\n\nLint\n```\npoetry run task lint\n```\n\nFormat\n```\npoetry run task format\n```\n',
    'author': 'kenta.shinzato',
    'author_email': 'hoppiece@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/HojiChar/HojiChar',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
