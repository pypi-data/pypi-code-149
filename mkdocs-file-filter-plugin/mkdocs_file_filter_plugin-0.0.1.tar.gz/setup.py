# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mkdocs_file_filter_plugin']

package_data = \
{'': ['*']}

install_requires = \
['igittigitt>=2.1.2,<3.0.0',
 'mkdocs>=1.4.0,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'schema>=0.7.5,<0.8.0']

entry_points = \
{'mkdocs.plugins': ['file-filter = '
                    'mkdocs_file_filter_plugin.plugin:FileFilter']}

setup_kwargs = {
    'name': 'mkdocs-file-filter-plugin',
    'version': '0.0.1',
    'description': 'A MkDocs plugin that lets you exclude/include docs files using globs, regexes and gitignore-style file.',
    'long_description': '# File exclude/include plugin for MkDocs\n\n[![PyPI - Version](https://img.shields.io/pypi/v/mkdocs-file-filter-plugin.svg)](https://pypi.org/project/mkdocs-file-filter-plugin)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-file-filter-plugin.svg)](https://pypi.org/project/mkdocs-file-filter-plugin)\n\n---\n\n`mkdocs-file-filter` is a [mkdocs plugin](http://www.mkdocs.org/user-guide/plugins/) that allows you to exclude/include files from your input using Unix-style wildcards (globs), regular expressions (regexes) or .mkdocsignore file ([gitignore-style](https://git-scm.com/docs/gitignore) syntax).\n\n## Quick start\n\n1. Install the plugin using pip.\n\n```console\npip install mkdocs-file-filter-plugin\n```\n\n1. In your project, add a plugin configuration to `mkdocs.yml`:\n\n  ```yaml\n  plugins:\n    - file-filter:\n        mkdocsignore: true\n        mkdocsignore_file: \'custom/path/.mkdocsignore\' # relative to mkdocs.yml\n        exclude_glob:\n          - \'exclude/this/path/*\'\n          - \'exclude/this/file/draft.md\'\n          - \'*.tmp\'\n          - \'*.gz\'\n        exclude_regex:\n          - \'.*\\.(tmp|bin|tar)$\'\n        include_glob:\n          - \'include/this/path/*\'\n          - \'include/this/file/Code-of-Conduct.md\'\n          - \'*.png\'\n          - \'assets/**\' # the material theme requires this folder\n        include_regex:\n          - \'.*\\.(js|css)$\'\n  ```\n\n## External config file\n\nThe plugin supports external files for the plugin configuration. If the external config file is specified, then `*_glob:` and `*_regex:` are not taken `mkdocs.yml` - only config from the external file applies.\n\n```yaml\nplugins:\n  - file-filter:\n      # config: !ENV [MY_FILE_FILTER_CONFIG, \'mkdocs.file-filter.yml\']\n      config: mkdocs.file-filter.yml\n```\n\nExternal plugin config file example.\n\n```yaml\nmkdocsignore: false\nexclude_glob:\n  - \'exclude/this/path/*\'\n  - \'exclude/this/file/draft.md\'\n  - \'*.tmp\'\n  - \'*.gz\'\nexclude_regex:\n  - \'.*\\.(tmp|bin|tar)$\'\ninclude_glob:\n  - \'include/this/path/*\'\n  - \'include/this/file/Code-of-Conduct.md\'\n  - \'*.png\'\n  - \'assets/**\' # the material theme requires this folder\ninclude_regex:\n  - \'.*\\.(js|css)$\'\n```\n\n> **HINT**\n>\n> For external file config, you can use [MkDocs Environment Variables](https://www.mkdocs.org/user-guide/configuration/#environment-variables) to set the desired file dynamically. A useful case for serving the site with different content based on stage/environment. Works well with CI/CD automation.\n\n## .mkdocsignore\n\nSetting `mkdocsignore` to `true` will exclude the dirs/files specified in the `.mkdocsignore`. Use the same syntax as you use for gitignore.\n\nOptionally you can set `mkdocsignore_file` parameter with your path to `.mkdocsignore` file. By default, the plugin uses `.mkdocsignore` from the root of your MkDocs.\n\nYou can combine mkdocsignore with globs/regex as well. The patterns from both will apply.\n\nExternal config for mkdocsignore.\n\n```yaml\nplugins:\n  - file-filter:\n      mkdocsignore: true # default: false\n      mkdocsignore_file: \'custom/path/.myignore\' # relative to mkdocs.yml, default: .mkdocsignore\n```\n\nExample `.mkdocsignore` file.\n\n```bash\n# MkDocs\ndocs/test/**\ndocs/**/draft-*.md\n```\n\n## Conflict behavior\n\nIt is possible to exclude and include will have conflict. For example, you could exclude `drafts/*` but include `*.md`. In that case, **include** has higher priority over exclude. So all `*.md` files from the drafts folder will be included.\n\n## Some useful stuff\n\nIf you do not provide patterns, everything will stay the same - standard MkDocs behavior.\n\nBecause of the YAML syntax specifics, patterns that start with a punctuation mark must be quoted.\n\nThe preferred way for quotes is to use single quotes `\'` rather than double quotes `"` - regex backslash escapes are preserved correctly without being doubled up.\n\n## License\n\n`mkdocs-file-filter-plugin` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.\n',
    'author': 'Dariusz Porowski',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/DariuszPorowski/mkdocs-file-filter-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
