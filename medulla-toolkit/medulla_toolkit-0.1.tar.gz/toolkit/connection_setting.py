import logging
import requests

from urllib3.exceptions import InsecureRequestWarning
from toolkit.utility import get_default_comm_logger


class ConnectionSettings:
    """
    This class contains the connection settings including but not limited to:
    Hostname, and port number for the URL. Upon successfully logged in using workstation_sign_in()
    token will be filled-up.
    """

    def __init__(self,
                 hostname="",
                 port=80,
                 comm_log_path="",
                 comm_log_level=logging.NOTSET,
                 max_log_size=(5*1024*1024)):
        """
        Creates the variables associated with the class. Variables are:
        localhost
        port

        :param hostname: contains the hostname of the URL
        :param port: contains the port number of the url
        :param max_log_size: maximum size for each log files
        :param username: contains the username of the operator
        """
        self.hostname = hostname
        self.port = port
        self.token = ""

        if not comm_log_path:
            comm_log_path = "./"

        if comm_log_level == logging.NOTSET:
            comm_log_level = logging.ERROR

        self.comm_logger = get_default_comm_logger(comm_log_path, comm_log_level, max_log_size)

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_url(self):
        """
        Returns the url string (in https).

        :return: string of the url.
        """

        return f"https://{self.hostname}:{self.port}"

    def print(self):
        """
        Print information on ConnectionSetting instance

        :return: nothing
        """
        print(f"hostname={self.hostname} port={self.port} "
              f"token={self.token}")
