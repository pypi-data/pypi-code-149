import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DEFAULT_DB_PATH = os.path.join(os.path.sep, str(Path.home()), ".azureml", "piprun", "localrun.db")

def db_setup(default_db_path: str = None, table_list: list = None):
    Base = declarative_base()
    db_path = os.environ.get('AML_LOCAL_RUN_DB_PATH')
    if db_path is None:
        db_path = default_db_path
    if db_path is None:
        db_path = DEFAULT_DB_PATH
    engine = create_engine(f'sqlite:///{db_path}', echo = False)
    Base.metadata.create_all(
        engine,
        tables = table_list,
        checkfirst = True
    )
    Session = sessionmaker(bind = engine)
    return Session

def drop_tables(default_db_path: str = None, table_list: list = None):
    Base = declarative_base()
    db_path = os.environ.get('AML_LOCAL_RUN_DB_PATH')
    if db_path is None:
        db_path = default_db_path
    if db_path is None:
        db_path = DEFAULT_DB_PATH
    engine = create_engine(f'sqlite:///{db_path}', echo = False)
    Base.metadata.drop_all(engine, tables = table_list)