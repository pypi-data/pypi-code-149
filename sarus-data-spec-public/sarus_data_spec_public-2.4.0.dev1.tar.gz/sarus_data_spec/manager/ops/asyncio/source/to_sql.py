from enum import Enum
import typing as t
import warnings

import pyarrow as pa

try:
    import sqlalchemy as sa
except ModuleNotFoundError:
    warnings.warn("Sqlalchemy not installed, cannot send sql queries")
try:
    from google.cloud import bigquery
    from google.oauth2 import service_account
except ModuleNotFoundError:
    warnings.warn(
        'Google API Python client and related libraries are not installed,'
        ' cannot push dataset to bigquery'
    )

from sarus_data_spec import typing as st
from sarus_data_spec.constants import (
    DATA,
    OPTIONAL_VALUE,
    PUBLIC,
    SQL_CACHING_URI,
    TO_SQL_CACHING_TASK,
    USER_COLUMN,
    WEIGHTS,
)
from sarus_data_spec.path import Path, straight_path
from sarus_data_spec.transform import filter, get_item
import sarus_data_spec.protobuf as sp

BATCH_SIZE = 500000
TAB_NAME_LENGTH = 8
SCHEMA_NAME_LENGTH = TAB_NAME_LENGTH
ALPHABET_BASE: str = "abcdefghijklmnopqrstuvwxyz"


# https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#TableFieldSchema.FIELDS.mode
class BQFieldType(Enum):
    """big query column constraint"""

    # it accepts null
    NULLABLE = 'NULLABLE'
    # id donesn't accept null values
    REQUIRED = 'REQUIRED'
    # not used for the moment
    REPEATED = 'REPEATED'


async def async_to_sql_op(
    dataset: st.Dataset,
) -> t.Tuple[str, t.Dict[str, t.Tuple[str, ...]], t.List[str]]:
    """It pushes the dataset to an SQL source.
    - It retrives the caching url from the source status.
    - It creates a schema in the DB named according to the dataset uuid.
    - It iterates over the sarus tables to retrive the correct column
        types and associated constraints (pks, fks and nullable columns).
    - It iterates over the the sarus tables a second time to push the data.

    It returns:
        (caching_uri, encoded table mapping, extended table mapping)
    """
    manager = dataset.manager()
    if manager.is_big_data(dataset):
        raise ValueError(
            f"Dataset {dataset.uuid()} is big data." "We can't push it to SQL"
        )

    source_ds = dataset.sources().pop()
    source_st = manager.status(
        dataspec=t.cast(st.DataSpec, source_ds),
        task_name=TO_SQL_CACHING_TASK,
    )

    if source_st is None:
        raise ValueError(
            f'Missing {TO_SQL_CACHING_TASK} for dataset ' f'{source_ds.uuid()}'
        )
    assert source_st
    source_st_task = source_st.task(task=TO_SQL_CACHING_TASK)
    assert source_st_task
    caching_uri = source_st_task.properties().get(SQL_CACHING_URI)
    assert caching_uri
    engine = manager.engine(uri=caching_uri)  # type:ignore
    ds_schema = await manager.async_schema(dataset)
    tables = ds_schema.tables()

    if dataset.is_source() and dataset.protobuf().spec.HasField('sql'):
        # If it is a sql source we still need to attach a ready status
        # with a table mapping
        table_map = table_mapping(tables)
        encoded_map = base64encode_table_map(table_map)
        expanded_map = expand_table_map(table_map)
    else:
        # create a schema name from the dataset uuid
        sql_schema = 's&51s_' + name_encoder(
            names=(dataset.uuid(),),
            length=SCHEMA_NAME_LENGTH,
        )
        metadata = SarusMetadata(engine, sql_schema)
        primary_keys = [
            tuple(path.to_strings_list()[0][1:])
            for path in await manager.async_primary_keys(dataset)
        ]
        foreign_keys = {}
        for key, value in (await manager.async_foreign_keys(dataset)).items():
            newkey = tuple(key.to_strings_list()[0][1:])
            if OPTIONAL_VALUE in newkey:
                foreign_keys[tuple([*newkey[:-1]])] = tuple(
                    value.to_strings_list()[0][1:]
                )
            else:
                foreign_keys[newkey] = tuple(value.to_strings_list()[0][1:])

        # table mapping: Path (withoud DATA) ->
        # (sql_schema, sql_tables)
        table_map = table_mapping(
            tables,
            encoded_name_length=TAB_NAME_LENGTH,
            sql_schema=sql_schema,
        )

        # Tuple[str] representation of table mapping -> (sql_schema,
        # sql_tables). Used to correctly map pks and fks.
        explicit_map = explicit_table_map(table_map)

        # Path (withoud DATA) -> (sql_schema, sql_tables)
        encoded_map = base64encode_table_map(table_map)
        expanded_map = expand_table_map(table_map)

        # I need to iterate twice on tables:
        # ones to fill the metadata and to create tables at once in the
        # DB. A second time to push

        # store sql table name -> sarus table dataset to be used to push data.
        sqltable_to_table_ds = {}

        # Iterate to create sql tables from sarus schema type of each table.
        for table_path in tables:
            # full path as Tuple[str]
            explicit_table_path = tuple(table_path.to_strings_list()[0][1:])
            # this is an encoded sql table name
            if not explicit_table_path:
                explicit_table_path = ('',)
            table_name = explicit_map[explicit_table_path][-1]

            # get table dataset and schema
            ds_filter = ds_schema.data_type().get(table_path)
            filtered_ds = filter(filter=ds_filter)(dataset)
            table_ds = get_item(table_path)(filtered_ds)
            schema_table = await manager.async_schema(
                t.cast(st.Dataset, table_ds)
            )
            # get pks and fks using the tables encoded names
            table_pks = [
                pk[-1] for pk in primary_keys if pk[:-1] == explicit_table_path
            ]
            table_fks = {
                keys[-1]: ".".join([explicit_map[values[:-1]][-1], values[-1]])
                for keys, values in foreign_keys.items()
                if keys[:-1] == explicit_table_path
            }

            # fill metadata depending on schma type
            metadata.fill(
                schema_table.type(),
                table_name,
                primary_keys=table_pks,
                foreign_keys=table_fks,
            )
            sqltable_to_table_ds[table_name] = table_ds

        metadata.create_all_tables()

        # Iterate for a second time to push sarus tables to sql.
        for table_name in metadata.sorted_tables():
            table_ds = sqltable_to_table_ds[table_name]
            iterator = await manager.async_to_arrow(
                t.cast(st.Dataset, table_ds), batch_size=BATCH_SIZE
            )

            async for batch in iterator:
                if DATA in batch.schema.names:
                    # Here we flatten the batch to have a struct
                    # with USER_COLUMN, WEIGHTS, PUBLIC col1, col2 etc.
                    data_arrays = batch.column(DATA).flatten()
                    colnames = [
                        field.name.replace(DATA + '.', '')
                        for field in batch.field(DATA).flatten()
                    ]

                    for col in [USER_COLUMN, WEIGHTS, PUBLIC]:
                        data_arrays.append(batch.column(col))
                        colnames.append(batch.field(col).name)

                    batch = pa.record_batch(data_arrays, names=colnames)

                if batch:
                    metadata.push_tosql(table_name, batch)

    return caching_uri, encoded_map, expanded_map


class SarusMetadata:
    """Helper to abstract the interaction with different APIs used to pushing
    data to a DB. We use for most the time SQLAlchemy but is not always optimal
    when it comes to push data to a DB (as for instance with bigquery).
    """

    def __init__(self, engine: sa.engine.Engine, sql_schema_name: str) -> None:
        self.engine = engine
        self.sql_schema_name = sql_schema_name

        self.sa_metadata: sa.MetaData
        self.bq_client: t.Any
        self.tabname_to_tabmetadata: t.Dict[str, t.Any] = {}
        self._setup()

    def _setup(self) -> None:
        """It creates the schema if the schema doesn't exists with sqlalchemy.
        For bigquery, moreover, it retrieves the credentials and instancieate
        the bigquery client.
        """
        with self.engine.connect() as conn:
            if (
                self.sql_schema_name
                not in conn.dialect.get_schema_names(  # type: ignore  # noqa
                    conn
                )
            ):
                self.engine.execute(
                    sa.schema.CreateSchema(self.sql_schema_name)
                )

        if self.engine.dialect.name == "bigquery":
            credentials_path = (
                self.engine.dialect.credentials_path  # type: ignore
            )
            credentials = (
                service_account.Credentials.from_service_account_file(
                    credentials_path
                )
            )
            self.bq_client = bigquery.Client(
                credentials=credentials,
                project=credentials.project_id,
            )

        self.sa_metadata = sa.MetaData(
            bind=self.engine, schema=self.sql_schema_name
        )

    def fill(
        self,
        schema_type: st.Type,
        table_name: str,
        primary_keys: t.List[str],
        foreign_keys: t.Dict[str, str],
    ) -> None:
        """It calls visitors to store information on column types. It should
        take a schema_type for a specific sarus table. Except for bigquery,
        we fill the sqlalchemy metadata with the a sqlalchemy Table containing
        columns with the proper datatype. For bigquery, we store the table data
        type information in a dict which will be used afterwards during pushing
        """
        if self.engine.dialect.name == "bigquery":
            # it stores the column types of the table
            bq_tabmetadata: t.Dict[str, t.Any] = {}
            to_bq_schema(
                schema_type,
                bq_tabmetadata,
                typemode=BQFieldType.REQUIRED.value,
            )
            self.tabname_to_tabmetadata[table_name] = bq_tabmetadata
        else:
            sa_tabmetadata = sa.Table(table_name, self.sa_metadata)
            to_sqlalchemy_metadata(
                schema_type,
                sa_tabmetadata,
                col_name=None,
                nullable=False,
                primary_keys=primary_keys,
                foreign_keys=foreign_keys,
            )
            self.tabname_to_tabmetadata[table_name] = sa_tabmetadata

    def create_all_tables(self) -> None:
        """Create tables for all methods that push data via sqlalchemy"""
        self.sa_metadata.create_all(self.engine)

    def sorted_tables(self) -> t.List[str]:
        """Returns sorted table names to prevent pushing
        a table with a foreign key pointing towards a table which is not yet
        pushed. SqlAlchemy metadata does that internally while order doesn't
        matter for bigquery.
        """
        if self.engine.dialect.name == "bigquery":
            return list(self.tabname_to_tabmetadata.keys())
        else:
            return [tab.name for tab in self.sa_metadata.sorted_tables]

    def push_tosql(self, table_name: str, batch: pa.RecordBatch) -> None:
        """It pushes data to the SQL DB using the most efficient method
        depending on the DB.
        """
        if self.engine.dialect.name == "bigquery":
            # https://cloud.google.com/bigquery/docs/samples/bigquery-load-table-dataframe
            bq_tabmetadata = self.tabname_to_tabmetadata[table_name]
            columns = list(bq_tabmetadata.keys())
            col_types = [bq_tabmetadata[colname] for colname in columns]
            job_config = bigquery.LoadJobConfig(schema=col_types)
            df = batch.to_pandas()[columns]
            job = self.bq_client.load_table_from_dataframe(
                df,
                f'{self.sql_schema_name}.{table_name}',
                job_config=job_config,
            )
            job.result()  # Wait for the job to complete.

        elif self.engine.dialect.name == "mssql":
            sa_tabmetadata = self.tabname_to_tabmetadata[table_name]
            mssql_insert(self.engine, batch, sa_tabmetadata)

        else:
            sa_tabmetadata = self.tabname_to_tabmetadata[table_name]
            default_insert(self.engine, batch, sa_tabmetadata)


def name_encoder(names: t.Tuple[str, ...], length: int) -> str:
    """It creates a random name with a specific length using a determined
    alphabet from a hash of names
    """
    hash_value = hash(names)
    result = []
    for _ in range(length):
        r = ALPHABET_BASE[hash_value % len(ALPHABET_BASE)]
        result.append(r)
        hash_value = int(hash_value / len(ALPHABET_BASE))
    return ''.join(result)


def default_insert(
    engine: sa.engine.Engine, batch: pa.RecordBatch, sa_table: sa.Table
) -> None:
    """SQLALCHEMY CORE API for batch insert
    This should be pretty efficient and quite general:
    https://towardsdatascience.com/how-to-perform-bulk-inserts-with-sqlalchemy-efficiently-in-python-23044656b97d
    """
    with engine.connect() as conn:
        conn.execute(sa.insert(sa_table), batch.to_pylist())


def mssql_insert(
    engine: sa.engine.Engine, batch: pa.RecordBatch, sa_table: sa.Table
) -> None:
    """Method to push data on an SQL server. This is actually though when
    the server is Azure. This is equivalent to a parametrized INSERT query
    since pyodb seems to not support fast_executemany for AZURE.
    TODO: we should be able to apply this only for azure because for
    synapse which still uses mssql-pyodb the most efficient method is different
    """
    azure_max_parameters = 2100
    chunksize = azure_max_parameters // batch.num_columns - 1
    batch_pylist = batch.to_pylist()
    with engine.connect() as conn:
        for i in range(0, len(batch_pylist), chunksize):
            conn.execute(
                sa.insert(sa_table).values(batch_pylist[i : i + chunksize])
            )


def table_mapping(
    tables: t.List[st.Path],
    encoded_name_length: t.Optional[int] = None,
    sql_schema: t.Optional[str] = '',
) -> t.Dict[Path, t.Tuple[str, ...]]:
    """Create table mapping between tables in the sarus schema to tables
    in sql.
    If encoded_name_length is provided: the table name will be encoded from
    the tuple with the table path.
    """
    mapping = {}
    for table_path in tables:
        explicit_table_nodata = table_path.to_strings_list()[0][1:]
        if not explicit_table_nodata:
            explicit_table_nodata.append('')

        path_without_data = straight_path(nodes=explicit_table_nodata.copy())

        if encoded_name_length is not None:
            table_name = [
                name_encoder(
                    names=tuple(explicit_table_nodata),
                    length=encoded_name_length,
                )
            ]
        else:
            table_name = explicit_table_nodata

        mapping[path_without_data] = (
            tuple([sql_schema, *table_name])
            if sql_schema
            else tuple(table_name)
        )
    return mapping


def base64encode_table_map(
    table_map: t.Dict[Path, t.Tuple[str, ...]]
) -> t.Dict[str, t.Tuple[str, ...]]:
    """Base64 encoding of the fully qualified table keys"""
    return {
        sp.utilities.to_base64(key.protobuf()): value
        for key, value in table_map.items()
    }


def explicit_table_map(
    table_map: t.Dict[Path, t.Tuple[str, ...]]
) -> t.Dict[t.Tuple[str, ...], t.Tuple[str, ...]]:
    """Tuple of Strings representation of the table_map Path"""
    return {
        tuple(key.to_strings_list()[0]): value
        for key, value in table_map.items()
    }


def expand_table_map(
    table_map: t.Dict[Path, t.Tuple[str, ...]]
) -> t.List[str]:
    """TODO:
    Use all possible table paths we can have to address an SQL table"""
    return []


def to_sqlalchemy_metadata(
    _type: st.Type,
    table: sa.Table,
    col_name: t.Optional[str] = None,
    nullable: bool = False,
    primary_keys: t.Optional[t.List[str]] = [],
    foreign_keys: t.Optional[t.Dict[str, str]] = {},
) -> None:
    """Visitor to create sqlalchemy metadata from a sarus type"""

    class ToSAMetaData(st.TypeVisitor):
        def Text(
            self,
            encoding: str,
            possible_values: t.Iterable[str],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.Text, nullable=nullable)
            )

        def Float(
            self,
            min: float,
            max: float,
            base: st.FloatBase,
            possible_values: t.Iterable[float],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.Float, nullable=nullable)
            )

        def Struct(
            self,
            fields: t.Mapping[str, st.Type],
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:

            for fieldname, fieldtype in fields.items():
                to_sqlalchemy_metadata(
                    fieldtype, table, col_name=fieldname, nullable=False
                )

            if primary_keys:
                table.append_constraint(
                    sa.PrimaryKeyConstraint(
                        *primary_keys, name=f'{table.name}_pks'
                    )
                )

            if foreign_keys:
                table.append_constraint(
                    sa.ForeignKeyConstraint(
                        list(foreign_keys.keys()),
                        list(foreign_keys.values()),
                        name=f'{table.name}_fks',
                    )
                )

        def Union(
            self,
            fields: t.Mapping[str, st.Type],
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise ValueError()

        def Optional(
            self,
            type: st.Type,
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            to_sqlalchemy_metadata(
                type, table, col_name=col_name, nullable=True
            )

        def Datetime(
            self,
            format: str,
            min: str,
            max: str,
            base: st.DatetimeBase,
            possible_values: t.Iterable[str],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.DateTime, nullable=nullable)
            )

        def Date(
            self,
            format: str,
            min: str,
            max: str,
            base: st.DateBase,
            possible_values: t.Iterable[str],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.Date, nullable=nullable)
            )

        def Time(
            self,
            format: str,
            min: str,
            max: str,
            base: st.TimeBase,
            possible_values: t.Iterable[str],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.Time, nullable=nullable)
            )

        def Duration(
            self,
            unit: str,
            min: int,
            max: int,
            possible_values: t.Iterable[int],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.Interval, nullable=nullable)
            )

        def Array(
            self,
            type: st.Type,
            shape: t.Tuple[int, ...],
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

        def Boolean(
            self,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.Boolean, nullable=nullable)
            )

        def Unit(
            self,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.String, nullable=True)
            )

        def Bytes(
            self,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.BINARY, nullable=nullable)
            )

        def Constrained(
            self,
            type: st.Type,
            constraint: st.Predicate,
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

        def Null(
            self, properties: t.Optional[t.Mapping[str, str]] = None
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.NullType, nullable=nullable)
            )

        def Enum(
            self,
            name: str,
            name_values: t.Sequence[t.Tuple[str, int]],
            ordered: bool,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.Enum, nullable=nullable)
            )

        def Hypothesis(
            self,
            *types: t.Tuple[st.Type, float],
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

        def Id(
            self,
            unique: bool,
            reference: t.Optional[st.Path] = None,
            base: t.Optional[st.IdBase] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            if base:
                if base == st.IdBase.STRING:
                    table.append_column(
                        sa.Column(
                            col_name, sa.types.String(450), nullable=nullable
                        )
                    )
                elif base == st.IdBase.BYTES:
                    table.append_column(
                        sa.Column(col_name, sa.types.BINARY, nullable=nullable)
                    )
                else:
                    table.append_column(
                        sa.Column(
                            col_name, sa.types.Integer, nullable=nullable
                        )
                    )

        def Integer(
            self,
            min: int,
            max: int,
            base: st.IntegerBase,
            possible_values: t.Iterable[int],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            table.append_column(
                sa.Column(col_name, sa.types.Integer, nullable=nullable)
            )

        def List(
            self,
            type: st.Type,
            max_size: int,
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

    visitor = ToSAMetaData()
    _type.accept(visitor)


def to_bq_schema(
    _type: st.Type,
    bq_schema: t.Dict[str, bigquery.SchemaField],
    col_name: t.Optional[str] = None,
    typemode: t.Optional[str] = None,
) -> None:
    """Visitor that associate to each column a bigquery.SchemaField
    containing the wanted column type.
    """

    class ToBQSchema(st.TypeVisitor):
        def Text(
            self,
            encoding: str,
            possible_values: t.Iterable[str],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "STRING", mode=typemode
            )

        def Float(
            self,
            min: float,
            max: float,
            base: st.FloatBase,
            possible_values: t.Iterable[float],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "FLOAT64", mode=typemode
            )

        def Struct(
            self,
            fields: t.Mapping[str, st.Type],
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:

            for fieldname, fieldtype in fields.items():
                to_bq_schema(
                    fieldtype,
                    bq_schema,
                    col_name=fieldname,
                    typemode=BQFieldType.REQUIRED.value,
                )

        def Union(
            self,
            fields: t.Mapping[str, st.Type],
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise ValueError()

        def Optional(
            self,
            type: st.Type,
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            to_bq_schema(
                type,
                bq_schema,
                col_name=col_name,
                typemode=BQFieldType.NULLABLE.value,
            )

        def Datetime(
            self,
            format: str,
            min: str,
            max: str,
            base: st.DatetimeBase,
            possible_values: t.Iterable[str],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "DATETIME", mode=typemode
            )

        def Date(
            self,
            format: str,
            min: str,
            max: str,
            base: st.DateBase,
            possible_values: t.Iterable[str],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "DATE", mode=typemode
            )

        def Time(
            self,
            format: str,
            min: str,
            max: str,
            base: st.TimeBase,
            possible_values: t.Iterable[str],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "TIME", mode=typemode
            )

        def Duration(
            self,
            unit: str,
            min: int,
            max: int,
            possible_values: t.Iterable[int],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

        def Array(
            self,
            type: st.Type,
            shape: t.Tuple[int, ...],
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

        def Boolean(
            self,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "BOOL", mode=typemode
            )

        def Unit(
            self,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            # Since big query has no type Null
            # We are considering as a nullable string
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "STRING", mode=BQFieldType.NULLABLE.value
            )

        def Bytes(
            self,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "BYTES", mode=typemode
            )

        def Constrained(
            self,
            type: st.Type,
            constraint: st.Predicate,
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

        def Null(
            self, properties: t.Optional[t.Mapping[str, str]] = None
        ) -> None:
            # treated in the same way as in Unit
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "STRING", mode=BQFieldType.NULLABLE.value
            )

        def Enum(
            self,
            name: str,
            name_values: t.Sequence[t.Tuple[str, int]],
            ordered: bool,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, bigquery.enums.SqlTypeNames.STRING, mode=typemode
            )

        def Hypothesis(
            self,
            *types: t.Tuple[st.Type, float],
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

        def Id(
            self,
            unique: bool,
            reference: t.Optional[st.Path] = None,
            base: t.Optional[st.IdBase] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            if base:
                if base == st.IdBase.STRING:
                    bq_schema[col_name] = bigquery.SchemaField(
                        col_name, "STRING", mode=typemode
                    )
                elif base == st.IdBase.BYTES:
                    bq_schema[col_name] = bigquery.SchemaField(
                        col_name, "BYTES", mode=typemode
                    )
                else:
                    bq_schema[col_name] = bigquery.SchemaField(
                        col_name, "INTEGER", mode=typemode
                    )

        def Integer(
            self,
            min: int,
            max: int,
            base: st.IntegerBase,
            possible_values: t.Iterable[int],
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            assert col_name
            assert typemode
            bq_schema[col_name] = bigquery.SchemaField(
                col_name, "INT64", mode=typemode
            )

        def List(
            self,
            type: st.Type,
            max_size: int,
            name: t.Optional[str] = None,
            properties: t.Optional[t.Mapping[str, str]] = None,
        ) -> None:
            raise NotImplementedError()

    visitor = ToBQSchema()
    _type.accept(visitor)
