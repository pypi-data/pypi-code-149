""" Steineman DPE Microsoft SQL Module
    Authors: Joshoua Bigler

    Description
    -----------
    Module contains an Microsft SQL class for working with MS SQL databases 
   
"""

from sqlmodel import SQLModel, Session, create_engine, select, col
from sqlalchemy.engine import URL


class MsSQL:
  """ Class for working with Microsoft SQL databases. """

  @staticmethod
  def connect_to_db_cstr(conn_str: str, echo: bool = False, autocommit: bool = False):
    """ Connects to MS-SQL Database with connection string and returns an _engine.Connection objec. """

    conn_url = URL.create(
        'mssql+pyodbc',
        query={
            'odbc_connect': conn_str,
            'autocommit': f"{autocommit}"
        },
    )
    engine = create_engine(conn_url, echo=echo)
    return engine

  @staticmethod
  def connect_to_db(server: str,
                    database: str,
                    USERNAME_DB: str,
                    PASSWORD_DB: str,
                    echo: bool = False,
                    autocommit: bool = False):
    """Connects to MS-SQL Database with given parameters and returns an _engine.Connection object."""

    connection_string = f"""DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=tcp:{server};DATABASE={database};UID={USERNAME_DB};PWD={PASSWORD_DB};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"""

    connection_url = URL.create(
        'mssql+pyodbc',
        query={
            'odbc_connect': connection_string,
            'autocommit': f"{autocommit}"
        },
    )
    engine = create_engine(connection_url, echo=echo)
    return engine

  @staticmethod
  def select_records(engine, table: SQLModel, nr_of_records: int = None) -> list:
    """ Returns all records within the JobStatistics table """

    with Session(engine) as session:
      if nr_of_records:
        statement = select(table).limit(nr_of_records)
      else:
        statement = select(table)
      result = session.exec(statement)
      result_all = result.fetchall()
      return result_all

  # def select_specific_metrics(engine, table: SQLModel, list_of_metrics: list) -> list:
  #   """Select specific metrics"""
  #   with Session(engine) as session:
  #     statement = select(list_of_metrics).where(col(table.metricIdentifier).in_(list_of_metrics))
  #     result = session.exec(statement)
  #     result_all = result.all()
  #     return result_all
