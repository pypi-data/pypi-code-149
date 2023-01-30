import logging, importlib
import os, sys, warnings

from types import ModuleType
from typing import List, Dict

from sqlalchemy import MetaData

from ...database.models import AlphaTable

with warnings.catch_warnings():
    from flask_marshmallow import Marshmallow
from flask_sqlalchemy import DefaultMeta

from ....models.main import AlphaClass
from ....models.logger import AlphaLogger, DEFAULT_FORMAT, DEFAUT_DATE_FORMAT
from ....libs import flask_lib, io_lib

from ....models.config import AlphaConfig
from ....models.main import AlphaException
from ...api import AlphaFlask
from flask_cors import CORS

from ...database.structure import AlphaDatabase

from ....utils.tasks import start_celery

from ....config.main_configuration import CONFIGURATION


def _get_relative_path(file: str, level=0, add_to_path=True):
    if level == 0:
        root = os.path.dirname(file)
    else:
        root = os.sep.join(os.path.dirname(file).split(os.sep)[:-level])
    if add_to_path:
        sys.path.append(root)
    return root


class AlphaCore(AlphaClass):
    instance = None
    tables = None

    def __init__(self, file: str, level: int = 0, *args, **kwargs):
        super().__init__(log=None)

        self.root: str = _get_relative_path(file, level=level)

        self.root_alpha = os.path.dirname(__file__).split("models")[0]

        self.config: AlphaConfig = None

        self.initiated: bool = False
        self.loggers: Dict[str, AlphaLogger] = {}

        self.ma: Marshmallow = None
        self._db: AlphaDatabase = None
        self.api: AlphaFlask = None

        self._models_sources: List[str] = []
        self.databases_models: list = []

        configuration = (
            None
            if not CONFIGURATION.CONFIGURATION_ENV_NAME in os.environ
            else os.environ[CONFIGURATION.CONFIGURATION_ENV_NAME].lower().strip()
        )
        self.configuration: str = configuration
        self.configuration_name: str = configuration

        self.config: AlphaConfig = AlphaConfig(
            CONFIGURATION.MAIN_CONFIGURATION_NAME,
            root=self.root,
            configuration=configuration,
            core=self,
            # default=f"{self.root_alpha}{os.sep}{CONFIGURATION.DEFAULT_CONFIG_FILEPATH}.json"
        )
        """ignored_warnings = self.config.get("ignored_warnings", [])
        for ignored_warning in ignored_warnings:
            warnings.filterwarnings("ignore", message=ignored_warning)"""

        self.logger_root = self.config.get("directories/logs", required=True)
        self.log: AlphaLogger = None

        self.__set_loggers()
        self.__configure_databases()

    @property
    def db(self):
        self.prepare_api(self.configuration)
        return self._db

    def __set_loggers(self):
        colors_loggers_default_file_path = f"{self.root_alpha}{os.sep}{CONFIGURATION.DEFAULT_LOGGERS_COLORS_FILEPATH}.json"
        loggers_default_colors_config = None
        if os.path.isfile(colors_loggers_default_file_path):
            loggers_default_colors_config = AlphaConfig(
                CONFIGURATION.DEFAULT_LOGGERS_COLORS_FILEPATH,
                filepath=colors_loggers_default_file_path,
            )

        colors = (
            self.config.get("colors/loggers/rules")
            if self.config.get("colors/loggers/active")
            else loggers_default_colors_config.data
        )

        if self.config.is_path("loggers"):
            loggers_names = list(self.config.get("loggers").keys())

            for logger_name in loggers_names:
                logger_config = self.config.get_config(path=["loggers", logger_name])
                if not logger_name in self.loggers:
                    self.__set_logger(logger_name, logger_config, colors)

        loggers_default_file_path = (
            f"{self.root_alpha}{os.sep}{CONFIGURATION.DEFAULT_LOGGERS_FILEPATH}.json"
        )
        if os.path.isfile(loggers_default_file_path):
            loggers_default_config = AlphaConfig(
                CONFIGURATION.DEFAULT_LOGGERS_FILEPATH,
                filepath=loggers_default_file_path,
            )
            if loggers_default_config:
                for logger_name in loggers_default_config.data:
                    if not logger_name in self.loggers:
                        self.__set_logger(
                            logger_name,
                            loggers_default_config.get_config(logger_name),
                            colors,
                        )

        self.log = self.loggers[CONFIGURATION.MAIN_LOGGER_NAME]
        error_logger = self.loggers[CONFIGURATION.ERRORS_LOGGER_NAME]
        monitoring_logger = self.loggers[CONFIGURATION.MONITORING_LOGGER_NAME]
        for logger in self.loggers.values():
            if logger.name in [
                CONFIGURATION.ERRORS_LOGGER_NAME,
                CONFIGURATION.MONITORING_LOGGER_NAME,
            ]:
                continue

            logger.monitoring_logger = monitoring_logger
            logger.error_logger = error_logger

    def __set_logger(self, logger_name, logger_config, colors):
        root = logger_config.get("root")

        self.loggers[logger_name] = AlphaLogger(
            logger_name,
            filename=logger_config.get("filename"),
            root=root if root is not None else self.logger_root,
            cmd_output=logger_config.get("cmd_output", default=True),
            level=logger_config.get("level"),
            colors=colors,
            log_in_db=logger_config.get("log_in_db"),
            excludes=logger_config.get("excludes"),
            config=logger_config.get("config"),
            replaces=logger_config.get("replaces"),
            format_log=logger_config.get("format_log", default=DEFAULT_FORMAT),
            date_format=logger_config.get("date_format", default=DEFAUT_DATE_FORMAT),
        )

    def get_logger(
        self, name=CONFIGURATION.MAIN_LOGGER_NAME, default_level="INFO"
    ) -> AlphaLogger:
        self._check_configuration()

        if name.lower() not in self.loggers:
            self.warning(f"{name=} is not configured as a logger")
            return self.loggers[CONFIGURATION.MAIN_LOGGER_NAME]
        return self.loggers[name.lower()]

    def __configure_databases(self):
        if not self.config.is_path("databases"):
            return

        config = self.config.get("databases")
        # Databases
        structure = {"name": None, "required": False, "value": None}

        db_cnx = {}
        for db_name, cf_db in config.items():
            if type(cf_db) == str and cf_db in config:
                cf_db = config[cf_db]
            elif type(cf_db) != dict:
                continue

            # TYPE
            if not "type" in cf_db:
                self.show()
                self.error(
                    f"Missing <type> parameter in <{db_name}> database configuration"
                )

            db_type = cf_db["type"]

            content_dict = {
                "user": {},
                "password": {},
                "host": {},
                "name": {},
                "port": {},
                "sid": {},
                "path": {},
                "database_type": {"name": "type"},
                "log": {"default": self.log},
            }
            if db_type == "sqlite":
                content_dict["path"]["required"] = True
            else:
                content_dict["user"]["required"] = True
                content_dict["password"]["required"] = True
                content_dict["host"]["required"] = True
                content_dict["port"]["required"] = True

            for name, content in content_dict.items():
                for key, el in structure.items():
                    if not key in content:
                        if key == "name":
                            el = name
                        content_dict[name][key] = el

                if content_dict[name]["name"] in cf_db:
                    content_dict[name]["value"] = cf_db[content_dict[name]["name"]]
                elif content_dict[name]["required"]:
                    self.error(f"Missing {name} parameter")

                if "default" in content_dict[name]:
                    content_dict[name]["value"] = content_dict[name]["default"]
                elif name == "log":
                    if (
                        type(content_dict[name]["value"]) == str
                        and content_dict[name]["value"] in self.loggers
                    ):
                        content_dict[name]["value"] = self.loggers[
                            content_dict[name]["value"]
                        ]
                    else:
                        self.warning(
                            f"Wrong logger configuration for database {db_name}"
                        )
                        content_dict[name]["value"] = self.log

            fct_kwargs = {x: y["value"] for x, y in content_dict.items()}

            if db_type == "mysql":
                user, password, host, port, name = (
                    cf_db["user"],
                    cf_db["password"],
                    cf_db["host"],
                    cf_db["port"],
                    cf_db["name"],
                )
                cnx_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}"
            elif db_type == "oracle":
                c = ""
                user, password, host, port = (
                    cf_db["user"],
                    cf_db["password"],
                    cf_db["host"],
                    cf_db["port"],
                )
                if "sid" in cf_db:
                    name = cf_db["sid"]
                    c = f"{host}:{port}/{name}"
                elif "service_name" in cf_db:
                    name = cf_db["service_name"]
                    c = f"(DESCRIPTION = (LOAD_BALANCE=on) (FAILOVER=ON) (ADDRESS = (PROTOCOL = TCP)(HOST = {host})(PORT = {port})) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = {name})))"
                cnx_str = f"oracle://{user}:{password}@{c}"
            elif db_type == "sqlite":
                cnx_str = "sqlite:///" + cf_db["path"]

            if "ssl" in cf_db and cf_db["ssl"] is not None:
                if not all(
                    elem in cf_db["ssl"].keys()
                    for elem in ["ssl_ca", "ssl_cert", "ssl_key"]
                ):
                    raise AlphaException(
                        description=f"'ssl_ca', 'ssl_cert' and 'ssl_key' are required in ssl configuration"
                    )
                ssl_ca = cf_db["ssl"]["ssl_ca"]
                ssl_cert = cf_db["ssl"]["ssl_cert"]
                ssl_key = cf_db["ssl"]["ssl_key"]

                cnx_str = (
                    f"{cnx_str}?ssl_ca={ssl_ca}&ssl_cert={ssl_cert}&ssl_key={ssl_key}"
                )
                if "ssl_check_hostname" in cf_db["ssl"].keys():
                    cnx_str = f"{cnx_str}&ssl_check_hostname={cf_db['ssl']['ssl_check_hostname']}"

            if cnx_str is not None:
                cf_db["cnx"] = cnx_str
                db_cnx[db_name.upper()] = cf_db

        self.db_cnx = db_cnx

    def get_database(self, name):
        return self._db

    def set_configuration(self, configuration_name):
        if configuration_name is None and self.config.configuration is not None:
            configuration_name = self.config.configuration

        self.config.set_configuration(configuration_name)
        self.configuration = configuration_name
        self.configuration_name = configuration_name

    def prepare_api(self, configuration):
        if self.api is not None:
            return

        self.set_configuration(configuration)

        template_path = (
            os.path.dirname(__file__).split(os.sep + "alphaz" + os.sep)[0]
            + os.sep
            + "alphaz"
            + os.sep
            + "templates"
        )
        self.api = AlphaFlask(
            __name__,
            template_folder=template_path,
            static_folder=template_path,
            root_path=template_path,
            config_name=CONFIGURATION.API_CONFIGURATION_NAME,
            configuration=configuration,
            root=self.root,
            core=self,
        )
        # if self.config.get("cors"):
        # CORS(self.api, resources={r"*": {"origins": "*"}}, supports_credentials=True)
        # logging.getLogger("flask_cors").level = logging.DEBUG
        self.api.config["CORS_HEADERS"] = "Content-Type"

        self.ma = self.api.ma

        # Cnx
        if self.db_cnx is None:
            self.error(
                f"Databases are not configurated in config file {self.config.filepath}"
            )
            exit()

        if not CONFIGURATION.MAIN_DATABASE_NAME in self.db_cnx:
            self.config.show()
            self.config.error(
                f"Missing <{CONFIGURATION.MAIN_DATABASE_NAME}> database configuration"
            )
            exit()
        self.db_cnx = (
            {x.upper(): y for x, y in self.db_cnx.items()}
            if self.db_cnx is not None
            else {}
        )

        # bind = not "NO_BIND" in os.environ or not "Y" in str(os.environ["NO_BIND"]).upper()
        # if bind:
        self.api.set_databases(self.db_cnx)

        # databases
        db_logger = self.get_logger("sqlalchemy.engine")
        if db_logger is None:
            db_logger = self.get_logger(CONFIGURATION.MAIN_LOGGER_NAME)

        self._db = AlphaDatabase(
            self.api,
            name=CONFIGURATION.MAIN_DATABASE_NAME,
            main=True,
            log=db_logger,
            config=self.config.get("orm", default={"type": "oracle"}),
        )  #!TODO: remove oracle type
        self.api.db = self._db

        # ensure tests
        """self._db.ensure("tests", drop=True)
        self._db.ensure("files_process")"""

    def get_database(self, name=None) -> AlphaDatabase:
        self.prepare_api(self.configuration)

        name = name.lower()
        return self._db

    def _check_configuration(self):
        if self.config is None:
            self.set_configuration(None)
            if self.config is None:
                print("ERROR: Configuration need to be initialized")
                exit()

    def get_table(self, schema: str, table: str):
        db = self.get_database(schema)
        return db.get_table(schema=schema, table=table)

    def database_init_all(
        self,
        binds: List[str] = None,
        tables: List[AlphaTable] = None,
        drop: bool = False,
        create: bool = False,
        sqlite: bool = True,
    ):
        self.prepare_api(self.configuration)
        self.load_models_sources()

        if sqlite:
            binds = [
                x.upper()
                for x, y in self.db_cnx.items()
                if y["type"] == "sqlite" and (binds is None or x in binds)
            ]

        """for bind, tables_dict in self.tables.items():
            if binds is None or bind in binds:
                for table_name, table_model in tables_dict.items():
                    engine = self.db.get_engine(bind=bind)
                    if drop:
                        table_model.__table__.drop(engine)
                    table_model.__table__.create(engine)"""
        """if drop:
            self._db.drop_all(bind=binds, tables=tables)
        self._db.create_all(bind=binds, tables=tables)"""

        tables_by_bind = {}
        for table_model in tables:
            bind = (
                "MAIN"
                if not hasattr(table_model, "__bind_key__")
                else table_model.__bind_key__
            )
            if not bind in tables_by_bind:
                tables_by_bind[bind] = [table_model]
            else:
                tables_by_bind[bind].append(table_model)

        for bind, tables_models in tables_by_bind.items():
            tables = [x.__table__ for x in tables_models]
            meta = MetaData(self.db.get_engine(bind=bind))
            if drop:
                meta.drop_all(tables=tables)
            meta.create_all(tables=tables)

    def create_table(self, schema: str, table: str, drop: bool = False):
        db = self.get_database(schema)
        table_object = self.get_table(schema, table)
        if drop:
            try:
                table_object.__table__.drop(db.engine)
            except:
                pass
        table_object.__table__.create(db.engine)
        return True

    def drop_table(self, schema: str, table: str):
        db = self.get_database(schema)
        table_object = self.get_table(schema, table)
        table_object.__table__.drop(db.engine)

    @property
    def models_sources(self):
        if len(self._models_sources) == 0:
            self._models_sources = self.config.get("directories/database_models")
            if not self._models_sources:
                self.log.error(
                    f"Missing <directories/database_models> entry in configuration {self.conf.filepath}"
                )
                exit()
        return self._models_sources

    @models_sources.setter
    def models_sources(self, models_sources):
        self._models_sources = models_sources

    def load_models_sources(self):
        if len(self.models_sources) != 0 and len(self.databases_models) != 0:
            return

        self.log.info(f"Getting models definitions from {self.models_sources}")
        (
            self.databases_models,
            self.tables,
        ) = flask_lib.get_definitions_modules_and_tables(
            self.models_sources, log=self.log
        )

    def get_table_model(self, tablename: str):
        return flask_lib.get_table_model(tablename, self.models_sources, log=self.log)

    def get_data_directory(self):
        return self.config.get("directories/data", required=True)

    def save(self, object_to_save: object, filename: str, ext: str = None):
        filename = (
            filename
            if os.sep in filename
            else self.config.get("directories/tmp") + os.sep + filename
        )
        io_lib.archive_object(object_to_save=object_to_save, filename=filename, ext=ext)

    def load(self, filename: str, ext: str = None, default: object = None):
        filename = (
            filename
            if os.sep in filename
            else self.config.get("directories/tmp") + os.sep + filename
        )
        return io_lib.unarchive_object(filename=filename, ext=ext, default=default)
