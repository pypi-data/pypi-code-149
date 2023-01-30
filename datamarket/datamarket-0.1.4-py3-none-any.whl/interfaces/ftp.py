########################################################################################################################
# IMPORTS

import logging
from ftplib import FTP, FTP_TLS
from pathlib import Path

########################################################################################################################
# CLASSES

logger = logging.getLogger(__name__)


class FTPInterface:
    def __init__(self, config):
        if "ftp" in config:
            self.config = config["ftp"]

            self.ftp = self.get_ftp()
        else:
            logger.warning("no ftp section in config")

    def get_ftp(self):
        ftps = self.config["ftps"]

        if ftps:
            ftp_conn = FTP_TLS(self.config["server"])

        else:
            ftp_conn = FTP(self.config["server"])

        ftp_conn.login(self.config["username"], self.config["password"])

        return ftp_conn

    def upload_file(self, local_file, remote_folder):
        self.ftp.cwd(remote_folder)

        with open(local_file, "rb") as f:
            self.ftp.storbinary(f"STOR {Path(local_file).name}", f)

    def download_file(self, local_file, remote_file):
        with open(local_file, "wb") as f:
            self.ftp.retrbinary(f"RETR {remote_file}", f.write)
