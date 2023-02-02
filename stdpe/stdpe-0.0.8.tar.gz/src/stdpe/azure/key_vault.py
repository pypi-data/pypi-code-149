""" Azure Key Vault Module 
    Authors: Joshoua Bigler

    Description
    -----------
    Module contains a KeyVault class for working with the key vault
"""

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, ClientSecretCredential


class KeyVault:
  """Class to work with the azure key vault."""

  client: SecretClient = None

  def __init__(self, url: str):
    self.url = url

  def connect(self, client_id: str = None, client_secret: str = None, tenant_id: str = None):
    """Connects to the key vault. If no client/secret id is given, the default azure credential will be used to authentificate"""
    if client_id or client_secret or tenant_id:
      # credential = ServicePrincipalCredentials(client_id=client_id, secret=client_secret, tenant=tenant_id)
      credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
    else:
      credential = DefaultAzureCredential(additionally_allowed_tenants=['*'])
    self.client = SecretClient(vault_url=self.url, credential=credential)

  def get_secret(self, secret_name: str):
    secret = self.client.get_secret(secret_name)
    return secret