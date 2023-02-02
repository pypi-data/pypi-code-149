# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plugins', 'sqlalchemy_history', 'sqlalchemy_history.plugins']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy-Utils>=0.30.12', 'SQLAlchemy>=1.4,<2', 'cached-property']

setup_kwargs = {
    'name': 'sqlalchemy-history',
    'version': '2.0.0',
    'description': 'History tracking extension for SQLAlchemy.',
    'long_description': "# SQLAlchemy-History\n\nSQLAlchemy-history is a fork of sqlalchemy-continuum.\nAn auditing extension for sqlalchemy which keeps a track of the history of your sqlalchemy models\n\n## Features\n\n- Supports sqlalchemy 1.4+ and python 3.6+\n- Tracks history for inserts, deletes, and updates\n- Does not store updates which don't change anything\n- Supports alembic migrations\n- Can revert objects data as well as all object relations at given transaction even if the object was deleted\n- Transactions can be queried afterwards using SQLAlchemy query syntax\n- Query for changed records at given transaction\n- Temporal relationship reflection. Get the relationships of an object in that point in time.\n\n## QuickStart\n\n```sh\npip install sqlalchemy-history\n```\n\nIn order to make your models versioned you need two things:\n\n1. Call `make_versioned()` before your models are defined.\n2. Add `__versioned__` to all models you wish to add versioning to\n\n```python\n>>> from sqlalchemy_history import make_versioned\n>>> make_versioned(user_cls=None)\n>>> class Article(Base):\n...    __versioned__ = {}\n...    __tablename__ = 'article'\n...    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)\n...    name = sa.Column(sa.Unicode(255))\n...    content = sa.Column(sa.UnicodeText)\n>>> article = Article(name='Some article', content='Some content')\n>>> session.add(article)\n>>> session.commit()\n'article has now one version stored in database'\n>>> article.versions[0].name\n'Some article'\n>>> article.name = 'Updated name'\n>>> session.commit()\n>>> article.versions[1].name\n'Updated name'\n>>> article.versions[0].revert()\n'lets revert back to first version'\n>>> article.name\n'Some article'\n```\n\nFor completeness, below is a working example.\n\n```python\nfrom sqlalchemy_history import make_versioned\nfrom sqlalchemy import Column, Integer, Unicode, UnicodeText, create_engine\nfrom sqlalchemy.ext.declarative import declarative_base\nfrom sqlalchemy.orm import create_session, configure_mappers\nmake_versioned(user_cls=None)\nBase = declarative_base()\nclass Article(Base):\n    __versioned__ = {}\n    __tablename__ = 'article'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(Unicode(255))\n    content = Column(UnicodeText)\nconfigure_mappers()\nengine = create_engine('sqlite://')\nBase.metadata.create_all(engine)\nsession = create_session(bind=engine, autocommit=False)\narticle = Article(name='Some article', content='Some content')\nsession.add(article)\nsession.commit()\nprint(article.versions[0].name) # 'Some article'\narticle.name = 'Updated name'\nsession.commit()\nprint(article.versions[1].name) # 'Updated name'\narticle.versions[0].revert()\nprint(article.name) # 'Some article'\n```\n\n## Resources\n\n- [Documentation](https://sqlalchemy-continuum.readthedocs.io/)\n- [Issue Tracker](http://github.com/corridor/sqlalchemy-history/issues)\n- [Code](http://github.com/corridor/sqlalchemy-history/)\n\n## More information\n\n- [http://en.wikipedia.org/wiki/Slowly_changing_dimension](http://en.wikipedia.org/wiki/Slowly_changing_dimension)\n- [http://en.wikipedia.org/wiki/Change_data_capture](http://en.wikipedia.org/wiki/Change_data_capture)\n- [http://en.wikipedia.org/wiki/Anchor_Modeling](http://en.wikipedia.org/wiki/Anchor_Modeling)\n- [http://en.wikipedia.org/wiki/Shadow_table](http://en.wikipedia.org/wiki/Shadow_table)\n- [https://wiki.postgresql.org/wiki/Audit_trigger](https://wiki.postgresql.org/wiki/Audit_trigger)\n- [https://wiki.postgresql.org/wiki/Audit_trigger_91plus](https://wiki.postgresql.org/wiki/Audit_trigger_91plus)\n- [http://kosalads.blogspot.fi/2014/06/implement-audit-functionality-in.html](http://kosalads.blogspot.fi/2014/06/implement-audit-functionality-in.html)\n- [https://github.com/2ndQuadrant/pgaudit](https://github.com/2ndQuadrant/pgaudit)\n\n## Comparison\n\nPrimary reasons to create another library:\n\n- Be future looking and support sqlalchemy 1.4 and 2.x\n- Support multiple databases (sqlite, mysql, postgres, mssql, oracle)\n- Focus on the history tracking and be as efficient as possible when doing it\n\nWe found multiple libraries which has an implementation of history tracking:\n\n1. [sqlalchemy-continuum](https://github.com/kvesteri/sqlalchemy-continuum)\n    - Does not support oracle, mssql\n    - Feature filled making it difficult to maintain all plugins/extensions\n2. [flask-continuum](https://github.com/bprinty/flask-continuum)\n    - Thin wrapper on sqlalchemy-continuum specifically for flask\n3. [postgresql-audit](https://github.com/kvesteri/postgresql-audit)\n    - Supports only postgres\n4. [versionalchemy](https://github.com/NerdWalletOSS/versionalchemy)\n    - Not updated in a while\n    - No reverting capability, Relationship queries on history not available\n5. [django-simple-history](https://github.com/jazzband/django-simple-history)\n    - Uses django ORM, does not support sqlalchemy\n6. [sqlalchemy example versioning-objects](http://docs.sqlalchemy.org/en/latest/orm/examples.html#versioning-objects)\n    - Simple example to demonstrate implementation - but very minimal\n",
    'author': 'Corridor Platforms',
    'author_email': 'postmaster@corridorplatforms.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/corridor/sqlalchemy-history',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
