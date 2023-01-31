# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
from autoai_ts_libs.deps.watson_core.beta.remotes import RemoteClient


class NoOpRemote(RemoteClient):
    """Simple implementation of RemoteClient that does nothing!"""

    def list(self, *args, **kwargs):
        """no-op"""
        return []

    def upload(self, *args, **kwargs):
        """no-op"""

    def download(self, *args, **kwargs):
        """no-op"""
