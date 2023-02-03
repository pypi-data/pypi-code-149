import datetime
import logging, logging.handlers, logging.config
import os
import platform
from threading import Lock

from muphyn.packages.core.utils.file import CreateDirectory
from muphyn.packages.core.utils.singleton import SingletonMetaClass

# class LogManagerMeta(type):
#     """
#     This is a thread-safe implementation of Singleton.
#     """

#     _instances = {}

#     _lock: Lock = Lock()
#     """
#     We now have a lock object that will be used to synchronize threads during
#     first access to the Singleton.
#     """

#     def __call__(cls, *args, **kwargs):
#         with cls._lock:
#             if cls not in cls._instances:
#                 instance = super().__call__(*args, **kwargs)
#                 cls._instances[cls] = instance
#         return cls._instances[cls]


class LogManager(metaclass=SingletonMetaClass):

    DisabledLoggers = ['PIL.Image', 'PIL', 'PIL.PngImagePlugin', 'matplotlib.ticker', 'matplotlib', 'matplotlib.dates', 'matplotlib.artist', 'matplotlib.lines', 'matplotlib.dviread', 'matplotlib.afm', 'matplotlib.font_manager', 'matplotlib.mathtext', 'matplotlib.textpath', 'matplotlib.backend_bases', 'matplotlib.text', 'matplotlib.colorbar', 'matplotlib.image', 'matplotlib.style.core', 'matplotlib.style', 'matplotlib.category', 
'matplotlib.axis', 'matplotlib.axes._base', 'matplotlib.axes', 'matplotlib.axes._axes', 'matplotlib.gridspec', 'matplotlib.figure', 'matplotlib.pyplot', 'opcua.ua.uatypes', 'opcua.ua', 'opcua', 'concurrent.futures', 'concurrent', 'asyncio', '__name__', 'opcua.uaprotocol', 'opcua.common.copy_node', 'opcua.common', 'opcua.common.instantiate', 'opcua.common.structures', 'opcua.client.client', 'opcua.client', 'opcua.server.binary_server_asyncio', 'opcua.server', 'opcua.server.server', 'OMPython', 'opcua.client.ua_client', 'opcua.client.ua_client.Socket', 'matplotlib.backends.qt_editor._formlayout', 'matplotlib.backends.qt_editor', 'matplotlib.backends', 'matplotlib.legend']

    def __init__(self, log_level: int = logging.INFO) -> None:
        logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s")

        # Set logging level
        logging.root.setLevel(log_level)

        # Disable matplotlib font manager debug
        for logger_name in LogManager.DisabledLoggers:
            logging.getLogger(logger_name).disabled = True

        # Init selected project
        self._current_project_id = -1

        # Create Global Log File Directory
        if platform.system() == "Windows":
            global_log_file_directory = os.path.join(os.getenv("APPDATA"), "Muphyn", "LOGS")
        else:
            global_log_file_directory = os.path.join(os.getcwd(), "LOGS")
        CreateDirectory(global_log_file_directory)

        # Build Global Log File
        global_log_file_path = os.path.join(global_log_file_directory, self._build_log_filename())

        # Create Global logger
        global_logger_name = self._create_logger(-1, "", global_log_file_path, logger_name="main_logger")

        # Init Tab ID 
        self._project_log_files = {
            self._current_project_id: {"ProjectName": "Global", "LoggerName": global_logger_name}
        }

    
    # ----------------
    # Logging Methods
    # ----------------

    def _log_message(self, message: str, level: int, logger_name: str):
        """
        Private Function: It writes in the selected log file the log message

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - level: int
            Level of the log message
        
        - log_file: str
            Target File Path for log message
        """
        # Get Logger
        logger = logging.getLogger(logger_name)

        # Log message
        logger.log(level, message)

    def _log_global_message(self, message: str, level: int):
        """
        Private Function: It writes in the global log file the log message

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - level: int
            Level of the log message
        """
        # Get Global Loger Name
        logger_name = self._project_log_files[-1]["LoggerName"]

        # Current Project Name
        current_project_name = self._project_log_files[self._current_project_id]["ProjectName"]

        # Log Message
        self._log_message(f"({current_project_name}) {message}", level, logger_name)

    def _log_current_project(self, message: str, level:int):
        """
        Private Function: It writes in the current project log file the log message.
            If there is no project opened or log file created for the current project 
            it writes into the global log file

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - level: int
            Level of the log message
        """
        if self._current_project_id != -1 and self._current_project_id in self._project_log_files:
            # Get logger name
            project_logger_name = self._project_log_files[self._current_project_id]["LoggerName"]

            # Log Message
            self._log_message(message, level, project_logger_name)
        else:
            # Log message in global Log File
            self._log_global_message(message, level)

    def log(self, message: str, level: int, is_global_message=False):
        """
        Public Function: It writes a log message in a Log File. 
            The target Log file can be selected between global log file or current project log file

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - level: int
            Level of the log message. Possible values : 
                * logging.DEBUG
                * logging.ERROR
                * logging.INFO
                * logging.WARNING

        - is_global_message: bool (optional)
            Select if the log message is written in the current project log file or global log file
        """
        # Log in global log file
        self._log_global_message(message, level)

        # Log in project log file
        if not is_global_message:
            self._log_current_project(message, level)

    def critical(self, message: str, is_global_message=False):
        """
        Public Function: It writes a critical message in the target Log File

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - is_global_message: bool (optional)
            Select if the log message is written in the current project log file or global log file
        """
        self.log(message, logging.CRITICAL, is_global_message)

    def debug(self, message: str, is_global_message=False):
        """
        Public Function: It writes a debug message in the target Log File

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - is_global_message: bool (optional)
            Select if the log message is written in the current project log file or global log file
        """
        self.log(message, logging.DEBUG, is_global_message)

    def error(self, message: str, is_global_message=False):
        """
        Public Function: It writes an error message in the target Log File

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - is_global_message: bool (optional)
            Select if the log message is written in the current project log file or global log file
        """
        self.log(message, logging.ERROR, is_global_message)

    def info(self, message: str, is_global_message=False):
        """
        Public Function: It writes an information message in the target Log File

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - is_global_message: bool (optional)
            Select if the log message is written in the current project log file or global log file
        """
        self.log(message, logging.INFO, is_global_message)

    def warning(self, message: str, is_global_message=False):
        """
        Public Function: It writes a warning message in the target Log File

        Parameters :
        ------------
        - message: str
            Log message to write in the file

        - is_global_message: bool (optional)
            Select if the log message is written in the current project log file or global log file
        """
        self.log(message, logging.WARNING, is_global_message)

    def setLevel(self, logging_level:int):
        logging.root.setLevel(logging_level)

    
    # ----------------
    # Other Methods
    # ----------------

    def _build_log_filename(self, project_name: str = None):
        """
        Private Function: Build the log file name based on the time of creation
            and the project name if this one is given

        Parameters :
        ------------
        - project_name: str (optionnal)
            Project name related to the log file

        Returns :
        ---------
        str
            Built log file name
        """
        # Get Time
        now = datetime.datetime.now()

        # Build File Name
        log_filename = now.strftime("%Y-%m-%d_%H-%M-%S")+".log"

        if project_name is not None:
            log_filename = f"{project_name}_{log_filename}"

        return log_filename

    def _create_logger(self, tab_id: int, project_name: str, project_log_file_path: str, logger_name:str = None):
        """
        Private Function: Create a logging.Logger object based on project information
        
        Parameters :
        ------------
        - tab_id: int
            ID of the project tab

        - project_name: str
            Project name

        - project_directory: str
            Project directory path

        - logger_name: str (optionnal)
            Logger name. The default logger name is equal to "{tab_id}_{project_name}"

        Returns :
        ---------
        str
            Name of the previously created logger object.
            This name is used to access the logger by using the function logging.getLogger(logger_name)

        """
        # Build Logger Name
        if logger_name is None:
            logger_name = f"{tab_id}_{project_name}" 

        # Get Logger if it exists or Build Logger
        logger = logging.getLogger(logger_name)
        # logger.setLevel(LogManager.LoggingLevel)

        # Remove all existing handler if it exists
        for handler in logger.handlers:
            logger.removeHandler(handler)
        
        # Build formatter
        formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

        # Build File Handler
        file_handler = logging.FileHandler(project_log_file_path, mode="w", encoding="utf-8")
        file_handler.setFormatter(formatter)

        # Append handler
        logger.addHandler(file_handler)

        return logger_name

    def add_project_logger(self, tab_id: int, project_name: str, project_directory: str):
        """
        Public Function: Append the project general informations (tab ID, project name & project directory path)

        Parameters :
        ------------
        - tab_id: int
            ID of the project tab

        - project_name: str
            Project name

        - project_directory: str
            Project directory path

        """
        if tab_id in self._project_log_files:
            # Write information in global LOG File
            self.info("Trying to add project information that already exists", is_global_message=True)
        else:
            # Create Log Directory
            project_log_directory = os.path.join(project_directory, "LOGS")
            CreateDirectory(project_log_directory)

            # Build Log File path
            project_log_file_path = os.path.join(project_log_directory, self._build_log_filename(project_name))

            # Create Logger
            logger_name = self._create_logger(tab_id, project_name, project_log_file_path)

            # Append Project Log File Informations
            self._project_log_files[tab_id] = {"ProjectName": project_name, "LoggerName": logger_name}

    def remove_project_logger(self, tab_id):
        """
        Public Function: Remove logger related a project

        Parameters :
        ------------
        - tab_id: int
            ID of the project tab
        """
        if tab_id in self._project_log_files:
            # Get Project Name
            logger_name = self._project_log_files[tab_id]["LoggerName"]

            # Remove from dictionnary
            del self._project_log_files[tab_id]
            
            if logger_name in logging.Logger.manager.loggerDict:
                # Remove logger
                del logging.Logger.manager.loggerDict[logger_name]

    def set_project_name(self, tab_id: int, project_name: str):
        """
        Public Function: Set logger path by deleting the existing logger and recreating a new logger

        Parameters :
        ------------
        - tab_id: int
            ID of the project tab
        - project_name: str
            New project name
        """
        if tab_id in self._project_log_files:
            self._project_log_files[tab_id]["ProjectName"] = project_name

    def set_project_path(self, tab_id: int, project_path: str):
        """
        Public Function: Set logger path by deleting the existing logger and recreating a new logger

        Parameters :
        ------------
        - tab_id: int
            ID of the project tab
        - project_path: str
            New project path
        """
        if tab_id in self._project_log_files:
            # Get Project Name
            project_name = self._project_log_files[tab_id]["ProjectName"]

            # Remove Existing Logger
            self.remove_project_logger(tab_id)

            # Create New Logger
            self._create_logger(tab_id, project_name, project_path)

    def set_current_project_id(self, tab_id: int):
        """
        Public Function: Set the current active project

        Parameters :
        ------------
        - tab_id: int
            ID of the project tab
        """
        if tab_id in self._project_log_files:
            # Set the current project id
            self._current_project_id = tab_id
        else:
            # Reset the current project id
            self._current_project_id = -1

    def reset_current_project_id(self):
        """
        Public Function: Reset the current active project
        """
        self.set_current_project_id(-1)

    def get_all_logger(self) -> list[str]:
        return [name for name in logging.root.manager.loggerDict]