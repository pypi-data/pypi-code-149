import logging
import os
import pathlib

from prefs_config import Preferences
from logging.handlers import RotatingFileHandler

prefs = Preferences().get_prefs()

PREFS_LOGGER_KEY = 'logging'

PREFS_KEY_NAME = 'name'
PREFS_KEY_FOLDER = 'folder'
PREFS_KEY_FILENAME = 'filename'
PREFS_KEY_CONSOLE_LEVEL = 'console_level'
PREFS_KEY_FILE_LEVEL = 'file_level'
PREFS_KEY_MAX_SIZE = 'max_size'
PREFS_KEY_FILE_COUNT = 'file_count'

DEFAULT_NAME = 'app'
DEFAULT_FOLDER = 'log'
DEFAULT_FILENAME = 'app.log'
DEFAULT_LEVEL = 'INFO'
DEFAULT_MAX_SIZE = 1024 * 1024 * 10  # 10 Megabytes
DEFAULT_FILE_COUNT = 30
DEFAULT_ENCODING = 'utf-8'

#: Log line format
LOG_FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
LOG_BASEPATH = str(pathlib.Path().absolute())


class Logger:
    _initialized = False
    _external_logger = False

    def __init__(self, logger: logging.Logger = None):
        if not self._initialized and logger:
            self._logger = logger
            self._initialized = True
            self._external_logger = True
        if not self._initialized:
            self._initialized = True
            self._log_name = Logger._get_prefs_attr_str(PREFS_KEY_NAME, DEFAULT_NAME)
            self._console_level = self._translate_level(
                Logger._get_prefs_attr_str(PREFS_KEY_CONSOLE_LEVEL, DEFAULT_LEVEL))
            self._logger = logging.getLogger(self._log_name)
            self._logger.setLevel(logging.DEBUG)
            _formatter = logging.Formatter(LOG_FORMAT)
            ch = logging.StreamHandler()
            ch.setLevel(self._console_level)
            ch.setFormatter(_formatter)
            self._logger.addHandler(ch)
            if Logger._get_prefs_attr_str(PREFS_KEY_FOLDER, '') and Logger._get_prefs_attr_str(PREFS_KEY_FILENAME, ''):
                self._log_folder = os.path.join(
                    LOG_BASEPATH,
                    Logger._get_prefs_attr_str(PREFS_KEY_FOLDER, DEFAULT_FOLDER))
                self._log_filename = os.path.join(
                    self._log_folder,
                    Logger._get_prefs_attr_str(PREFS_KEY_FILENAME, DEFAULT_FILENAME))
                self._file_level = self._translate_level(
                    Logger._get_prefs_attr_str(PREFS_KEY_FILE_LEVEL, DEFAULT_LEVEL))
                if not os.path.exists(self._log_folder):
                    os.mkdir(self._log_folder)
                should_roll_over = os.path.isfile(self._log_filename)
                fh = RotatingFileHandler(
                    self._log_filename,
                    encoding=DEFAULT_ENCODING,
                    backupCount=Logger._get_prefs_attr_int(PREFS_KEY_FILE_COUNT, DEFAULT_FILE_COUNT),
                    maxBytes=Logger._get_prefs_attr_int(PREFS_KEY_MAX_SIZE, DEFAULT_MAX_SIZE)
                )
                fh.setLevel(self._file_level)
                fh.setFormatter(_formatter)
                if should_roll_over:
                    fh.doRollover()
                self._logger.addHandler(fh)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Logger, cls).__new__(cls)
        return cls._inst

    @staticmethod
    def _translate_level(level: str):
        _lv = logging.INFO
        if level == "DEBUG":
            _lv = logging.DEBUG
        elif level == "WARNING":
            _lv = logging.WARNING
        elif level == "ERROR":
            _lv = logging.ERROR
        elif level == "CRITICAL":
            _lv = logging.CRITICAL
        return _lv

    def get_logger(self):
        return self._logger

    def release_handlers(self):
        if not self._external_logger:
            _handlers = self._logger.handlers[:]
            for _handler in _handlers:
                _handler.close()
                self._logger.removeHandler(_handler)

    @staticmethod
    def _get_prefs_attr_str(attribute: str, default: str = "") -> str:
        _result = default
        if prefs and PREFS_LOGGER_KEY in prefs:
            if attribute in prefs[PREFS_LOGGER_KEY]:
                _result = prefs[PREFS_LOGGER_KEY][attribute]
        return _result

    @staticmethod
    def _get_prefs_attr_int(attribute: str, default: int = 0) -> int:
        _result = default
        if prefs and PREFS_LOGGER_KEY in prefs:
            if attribute in prefs[PREFS_LOGGER_KEY]:
                _result = prefs[PREFS_LOGGER_KEY][attribute]
        return _result
