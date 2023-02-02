""" Azure storage blob manager 
    Authors: Joshoua Bigler

    Description
    -----------
    Module contains a BlobManager class for working with the azure storage account
"""

import json
from dataclasses import dataclass
from azure.storage.blob import BlobClient


@dataclass
class BlobManager:
  """ Class for working with the blob azure storage. """

  conn_str: str
  container_name: str
  blob_name: str
  blob_client: BlobClient = None

  def connect(self, logging_enable: bool = False):
    """ Connects to the blob client """

    self.blob_client = BlobClient.from_connection_string(conn_str=self.conn_str,
                                                         container_name=self.container_name,
                                                         blob_name=self.blob_name,
                                                         logging_enable=logging_enable)

  def get_blob(self):
    if not self.blob_client:
      raise Exception('Blob client is not connected!')
    try:
      stream = self.blob_client.download_blob()
    except Exception as exc:
      raise (Exception(f"{self.blob_name} could not be downloaded from the Blobstorage! \n{exc}"))
    try:
      data_encoded = stream.readall()
    except Exception as exc:
      raise (Exception(f"{self.blob_name} could not be decoded! \nMay there is an typo in the json file? \n{exc}"))
    data = json.loads(data_encoded.decode("utf-8"))
    return data
