# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pixeltable',
 'pixeltable.functions',
 'pixeltable.functions.pil',
 'pixeltable.tests',
 'pixeltable.utils']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=2.2.1,<3.0.0',
 'ffmpeg-python>=0.2.0,<0.3.0',
 'ftfy>=6.1.1,<7.0.0',
 'hnswlib>=0.6.2,<0.7.0',
 'jmespath>=1.0.1,<2.0.0',
 'numpy>=1.24.1,<2.0.0',
 'opencv-python-headless>=4.7.0.68,<5.0.0.0',
 'pandas>=1.5.3,<2.0.0',
 'pillow>=9.4.0,<10.0.0',
 'psycopg2-binary>=2.9.5,<3.0.0',
 'regex>=2022.10.31,<2023.0.0',
 'sqlalchemy-utils>=0.39.0,<0.40.0',
 'sqlalchemy>=1.4.41,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'pixeltable',
    'version': '0.1.2',
    'description': 'Pixeltable: a dataframe-like interface to image and video data',
    'long_description': "# Pixeltable\n\nPixeltable presents a dataframe-like interface to image and video data.\n\n## Installation\n\n1. Install Postgres\n\n    On MacOS, [postgresapp.com](postgresapp.com) is a convenient way to do that.\n\n2. `pip install pixeltable`\n\n3. Install additional dependencies\n   - Install PyTorch (required for CLIP): see [here](https://pytorch.org/get-started/locally/)\n   - Install CLIP from [here](https://github.com/openai/CLIP)\n\n## Setup\n\nPixeltable requires a home directory and a Postgres database, both are created automatically the first time you create a Pixeltable client (see below).\nThe location of the home directory is `~/.pixeltable` (or the value of the `PIXELTABLE_HOME` environment variable);\nthe name of the Postgres database is `pixeltable` (or the value of the `PIXELTABLE_DB` environment variable).\n\n## Overview\n\nImport convention:\n```\nimport pixeltable as pt\n```\n\n### Create a client\n```\ncl = pt.Client()\n```\n\n### Create a database\n```\nClient.create_db('db1')\n```\n\n### Create a table with video data\n```\nc1 = Column('video', VideoType())\nc2 = Column('frame_idx', IntType())\nc3 = Column('frame', ImageType())\nDb.create_table(\n    'video_table', [c1, c2, c3],\n    extract_frames_from='video',\n    extracted_frame_col='frame',\n    extracted_frame_idx_col='frame_idx',\n    extracted_fps=1)\n```\n\n### Query table\n\n|H1|H2|\n|----|----|\n| Look at 10 rows | `Table.show(10)` |\n| Look at row for frame 15 | `t[t.frame_idx == 15].show()` |\n| Look at all frames after index 15 | `t[t.frame_idx >= 15][t.frame].show(0)` |\n\n\n",
    'author': 'Marcel Kornacker',
    'author_email': 'marcelk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
